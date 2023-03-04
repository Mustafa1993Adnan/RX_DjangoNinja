from django.shortcuts import get_object_or_404
from ninja import Router, Schema
from pydantic.types import UUID4

from RX.models import ScientificOfficeStock, ScientificOffice
from RX.schemas.SBItemStock import SBStockOut, ScientificOfficeOut
# from RX.views import MessageOut
from account.authorization import TokenAuthentication
from account.models import User
from utilities.schemas import MessageOut
from ninja.security import django_auth

sb_stock_controller = Router(tags=['Scientific Bureau Stock'])


@sb_stock_controller.get('/ScientificOffice/', auth=TokenAuthentication(),
                         response={200: list[ScientificOfficeOut], 404: MessageOut})
def get_all_sb(request):
    auth_user = User.objects.get(id=request.auth['id'])
    if User.has_perm(perm='RX.view_scientificoffice', self=auth_user):
        scientific = ScientificOffice.objects.all()
        if scientific:
            return 200, scientific
        else:
            return 404, {'msg': "There are no SB yet."}
    else:
        return 403, {'msg': "You don't have permission to access this endpoint"}


@sb_stock_controller.get('/{id}', auth=TokenAuthentication(), response={200: ScientificOfficeOut, 404: MessageOut})
def get_sb_stock_by_id(request, id: UUID4):
    auth_user = User.objects.get(id=request.auth['id'])
    if User.has_perm(perm='RX.view_scientificoffice', self=auth_user):
        scientific = get_object_or_404(ScientificOffice, id=id)
        if scientific:
            return 200, scientific
        else:
            return 404, {'msg': "There are no SB yet."}
    else:
        return 403, {'msg': "You don't have permission to access this endpoint"}


@sb_stock_controller.get('/list_items/', auth=TokenAuthentication(), response={200: list[SBStockOut], 404: MessageOut})
def list_sb_stock(request):
    # print(request.auth)
    print(request.user.get_all_permissions())
    auth_user = User.objects.get(id=request.auth['id'])
    if User.has_perm(perm='RX.view_scientificofficestock', self=auth_user):
        scientific_stock = ScientificOfficeStock.objects.all()
        if scientific_stock:
            return 200, scientific_stock
        else:
            return 404, {'msg': "There are no SB yet."}
    else:
        return 403, {'msg': "You don't have permission to access this endpoint"}


@sb_stock_controller.get('/list_items/{id}', auth=TokenAuthentication(),
                         response={200: SBStockOut, 404: MessageOut})
def list_sb_stock(request, id: UUID4):
    # print(request.auth)
    print(request.user.get_all_permissions())
    auth_user = User.objects.get(id=request.auth['id'])
    if User.has_perm(perm='RX.view_scientificofficestock', self=auth_user):
        scientific_stock = get_object_or_404(ScientificOfficeStock, id=id)
        if scientific_stock:
            return 200, scientific_stock
        else:
            return 404, {'msg': "There are no SB yet."}
    else:
        return 403, {'msg': "You don't have permission to access this endpoint"}

# # 'RX.view_scientificofficestock'
# def custom_has_perm(auth_user: User, permParam: str):
#     for perm in auth_user.get_all_permissions():
#         if perm == permParam:
#             return True
#
#     return False
#     # print(auth_user.has_perm('RX.view_scientificofficestock', obj=ScientificOfficeStock))
