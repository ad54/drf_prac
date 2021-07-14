# drf_prac

This is a django rest framework api.

This api provide facility to store your belongings and the friends to whom you have lend the same.
It also helps you to send reminder to them.

It uses following concepts of drf

- CRUD using ModelViewSet 
- login and authentication using [djoser](https://djoser.readthedocs.io/en/latest/) library
- custom field using djano's case function / conditional expression
- pagination using custom pagination class overrighting rest framework's LimitOffsetPagination, (drf_prac/pagination.py)
- filtering  using django-filter and custom filterset
- functional endpoint using @action decorator
- nested api using nested mixin , drf-extensions
- selective fields and related objects using FlexFieldsModelSerializer, drf-flex-fields



Note :  Will soon add the series of blogs to create this api.


Happy Coding
