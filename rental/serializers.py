from rest_framework import serializers
from .models import Friend, Borrowed, Belonging
from rest_flex_fields import FlexFieldsModelSerializer


class FriendSerializer(FlexFieldsModelSerializer):
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Friend
        fields = ("id", "name", "owner", "has_overdue")


class BelongingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Belonging
        fields = ('id', 'name')


class BorrowedSerializer(FlexFieldsModelSerializer):
    what = BelongingSerializer()
    to_who = FriendSerializer()
    expandable_fields = {
        'what': (BelongingSerializer, {'source': 'what'}),
        'to_who': (FriendSerializer, {'source': 'to_who'})
    }

    class Meta:
        model = Borrowed
        fields = ('id', 'what', 'to_who', 'when', 'returned')
