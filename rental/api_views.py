from rest_framework import viewsets
from . import models
from . import serializers
from .permissions import IsOwner
from django.core.mail import send_mail
from rest_framework.decorators import action
from rest_framework.response import Response
import django_filters
from rest_framework_extensions.mixins import NestedViewSetMixin
from rest_flex_fields import FlexFieldsModelViewSet
from django.conf import settings


class FriendViewSet(NestedViewSetMixin, FlexFieldsModelViewSet):
    queryset = models.Friend.objects.with_overdue()
    serializer_class = serializers.FriendSerializer
    permission_classes = [IsOwner]


class BelongingViewSet(FlexFieldsModelViewSet):
    queryset = models.Belonging.objects.all()
    serializer_class = serializers.BelongingSerializer
    permission_classes = [IsOwner]


class BorrowedFilterSet(django_filters.FilterSet):
    missing = django_filters.BooleanFilter(field_name="returned", lookup_expr="isnull")
    overdue = django_filters.BooleanFilter(method="get_overdue", field_name="returned")

    class Meta:
        model = models.Borrowed
        fields = ["what", "to_who", "missing", "overdue"]

    def get_overdue(self, queryset, field_name, value):
        if value:
            return queryset.overdue()
        return queryset


class BorrowedViewSet(NestedViewSetMixin, FlexFieldsModelViewSet):
    queryset = models.Borrowed.objects.all().select_related('to_who', 'what')
    permit_list_expands = ['what', 'to_who']
    serializer_class = serializers.BorrowedSerializer
    permission_classes = [IsOwner]
    filterset_fields = ('to_who',)
    filterset_class = BorrowedFilterSet

    @action(detail=True, url_path="remind", methods=["post"])
    def remind_single(self, request, *args, **kwargs):
        obj = self.get_object()
        send_mail(
            subject=f"Please return my belonging: {obj.what.name}",
            message=f'You forgot to return my belonging: "{obj.what.name}"" that you borrowed on {obj.when}. Please return it.',
            from_email="agam@gmail.com",  # your email here
            recipient_list=[obj.to_who.email],
            fail_silently=False,
        )
        return Response("Email sent.")

    @action(detail=False, url_path="remind-many", methods=["post"])
    def remind_many(self, request, *args, **kwargs):
        objs = models.Borrowed.objects.all()
        cnt = 0
        for obj in objs:
            if send_mail(
                subject=f"Please return my belonging: {obj.what.name}",
                message=f'You forgot to return my belonging: "{obj.what.name}"" that you borrowed on {obj.when}. Please return it.',
                from_email=settings.EMAIL_HOST_USER,  # your email here
                recipient_list=[obj.to_who.email],
                fail_silently=False,
            ):
                cnt += 1

        return Response(f"Email sent to total {cnt} borrowers")