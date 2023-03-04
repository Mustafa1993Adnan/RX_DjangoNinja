# import datetime
# from decimal import Decimal
#
# from django.shortcuts import render
# from ninja.security import django_auth
#
# # Create your views here.
# from ninja import Router
# from pydantic.types import UUID4
#
# from account.models import User
#
# scientific_controller = Router(tags=['Scientific'])
#
# from ninja import Schema
#
#
# class MessageOut(Schema):
#     msg: str
#
#
# class MovieOut(Schema):
#     id: UUID4
#     title: str
#     description: str
#     image: str
#     thumbnail: str
#     # trailer_url: Optional = str
#     release_date: datetime.date
#     rating: Decimal
#
#
# from django.contrib.auth.decorators import user_passes_test
#
#
# def group_required(*group_names):
#     """Requires user membership in at least one of the groups passed in."""
#
#     def in_groups(u):
#         if u.is_authenticated():
#             if bool(u.groups.filter(name__in=group_names)) | u.is_superuser:
#                 return True
#         return False
#
#     return user_passes_test(in_groups, login_url='403')
#
#
# @group_required('Professor')
# def action_only_for_professor(request):
#     pass
#
#
# @scientific_controller.get('/Scientific',  response={200: list[MovieOut], 404: MessageOut})
# def scientific(request):
#     print(request.user)
#     for g in request.user.groups:
#         print(g)
#     x = request.user.groups.filter(email=request.user)
#     group_required(x)
#     movies = User.objects.filter(user__exact=request.auth['id'])
#     if movies:
#         return 200, movies
#     return 404, {'msg': 'There are no featured movies.'}
