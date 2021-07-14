# drf_prac

This is a django rest framework api.

This api provide facility to store your belongings and the friends to whom you have lend the same.
It also helps you to send reminder to them.

It uses following concepts of drf

- CRUD using __ModelViewSet__
- login and authentication using __[djoser](https://djoser.readthedocs.io/en/latest/) library__
- custom field using __djano's case function / conditional expression__
- pagination using __custom pagination class overrighting rest framework's LimitOffsetPagination, (drf_prac/pagination.py)__
- filtering  using __django-filter and custom filterset__
- functional endpoint using __@action decorator__
- nested api using __nested mixin , drf-extensions__
- selective fields and related objects using __FlexFieldsModelSerializer, drf-flex-fields__



Note :  Will soon add the series of blogs to create this api.


Happy Coding
