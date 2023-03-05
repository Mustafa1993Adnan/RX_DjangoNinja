from django.shortcuts import get_object_or_404
from ninja import Router, Schema
from pydantic.types import UUID4

from RX.models import DistributorWarehouse
from RX.schemas.DWSchema import DWOut
from RX.schemas.SBItemStock import SBStockOut, ScientificOfficeOut, SBInvoiceInBody
from account.authorization import TokenAuthentication
from account.models import User
from utilities.schemas import MessageOut

dw_controller = Router(tags=['Distributor Warehouse'])


@dw_controller.get('/DW/', auth=TokenAuthentication(),
                   response={200: list[DWOut], 403: MessageOut})
def get_all_sb(request):
    auth_user = User.objects.get(id=request.auth['id'])
    if User.has_perm(perm='RX.view_distributorwarehouse', self=auth_user):
        dw = DistributorWarehouse.objects.all()
        if dw:
            return 200, dw
        else:
            return 403, {'msg': "There are no DW yet."}
    else:
        return 403, {'msg': "You don't have permission to access this endpoint"}
