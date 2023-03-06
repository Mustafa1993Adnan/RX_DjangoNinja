from django.shortcuts import get_object_or_404
from ninja import Router, Schema
from pydantic.types import UUID4

from RX.models import ScientificOfficeStock, ScientificOffice, ScientificOfficeItems, Invoices, DistributorWarehouse
from RX.schemas.SBItemStock import SBStockOut, ScientificOfficeOut, SBInvoiceInBody, SBInvoiceOut
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


@sb_stock_controller.get('/list_items_all/', auth=TokenAuthentication(),
                         response={200: list[SBStockOut], 404: MessageOut})
def list_sb_stock_all(request):
    # print(request.auth)
    print(request.user.get_all_permissions())
    auth_user = User.objects.get(id=request.auth['id'])
    print(auth_user.userSB.id)
    # so = ScientificOffice.objects.get(id=auth_user.userSB.id)
    # print(so.id)
    # soi = ScientificOfficeItems.objects.get(ScientificOfficeID=so.id)
    # print(soi.id)
    if User.has_perm(perm='RX.view_scientificofficestock', self=auth_user):
        scientific_stock = ScientificOfficeStock.objects.all()
        if scientific_stock:
            return 200, scientific_stock
        else:
            return 404, {'msg': "There are no SB yet."}
    else:
        return 403, {'msg': "You don't have permission to access this endpoint"}


@sb_stock_controller.get('/list_items_sb_id/', auth=TokenAuthentication(), response={200: SBStockOut, 404: MessageOut})
def list_sb_stock(request):
    # print(request.auth)
    print(request.user.get_all_permissions())
    auth_user = User.objects.get(id=request.auth['id'])
    print(auth_user.userSB.id)
    so = ScientificOffice.objects.get(id=auth_user.userSB.id)
    print(so.id)
    soi = ScientificOfficeItems.objects.get(ScientificOfficeID=so.id)
    print(soi.id)
    if User.has_perm(perm='RX.view_scientificofficestock', self=auth_user):
        scientific_stock = ScientificOfficeStock.objects.get(ItemID=soi.id)
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


@sb_stock_controller.post('/addInvoices/', auth=TokenAuthentication(),
                          response={200: MessageOut, 404: MessageOut})
def add_invoice(request, payload: SBInvoiceInBody):
    auth_user = User.objects.get(id=request.auth['id'])
    if User.has_perm(perm='RX.add_invoices', self=auth_user):
        item_stock_instance = ScientificOfficeStock.objects.get(id=payload.ProductName)
        print(item_stock_instance.Quantity)
        item_stock_instance.Quantity = item_stock_instance.Quantity - payload.Quantitiy
        print(item_stock_instance.Quantity)
        item_stock_instance.save()
        distributor_warehouse = DistributorWarehouse.objects.get(id=payload.InvoiceDW)
        invoice = Invoices.objects.create(InvoiceNumber=payload.InvoiceNumber, InvoiceDate=payload.invoice_date,
                                          InvoiceDW=distributor_warehouse, PaymentTerms=payload.PaymentTerms,
                                          DueDate=payload.DueDate, ProductName=item_stock_instance,
                                          Quantitiy=payload.Quantitiy, SellPrice=payload.SellPrice)
        invoice.save()

        return 200, {'msg': "The invoice created successfully"}
    else:
        return 403, {'msg': "You don't have permission to access this endpoint"}


@sb_stock_controller.get('/invoices/', auth=TokenAuthentication(),
                         response={200: list[SBInvoiceOut], 403: MessageOut})
def get_invoice(request):
    print(request.user.get_all_permissions())
    auth_user = User.objects.get(id=request.auth['id'])
    # print(auth_user.userSB.id)
    # so = ScientificOffice.objects.get(id=auth_user.userSB.id)
    # print(so.id)
    # soi = ScientificOfficeItems.objects.get(ScientificOfficeID=so.id)
    # print(soi.id)
    if User.has_perm(perm='RX.view_invoices', self=auth_user):
        invoice = Invoices.objects.all()
        if invoice:
            return 200, invoice
        else:
            return 404, {'msg': "There are no invoice yet."}
    else:
        return 403, {'msg': "You don't have permission to access this endpoint"}

    # auth_user = User.objects.get(id=request.auth['id'])
    # if User.has_perm(perm='RX.add_invoices', self=auth_user):
    #     item_stock_instance = ScientificOfficeStock.objects.get(id=payload.ProductName)
    #     distributor_warehouse = DistributorWarehouse.objects.get(id=payload.InvoiceDW)
    #     invoice = Invoices.objects.create(InvoiceNumber=payload.InvoiceNumber, InvoiceDate=payload.invoice_date,
    #                                       InvoiceDW=distributor_warehouse, PaymentTerms=payload.PaymentTerms,
    #                                       DueDate=payload.DueDate, ProductName=item_stock_instance,
    #                                       Quantitiy=payload.Quantitiy, SellPrice=payload.SellPrice)
    #     invoice.save()
    #
    #     return 200, {'msg': "The invoice created successfully"}
    # else:
    #     return 403, {'msg': "You don't have permission to access this endpoint"}


@sb_stock_controller.get('/invoices/{id}', auth=TokenAuthentication(),
                         response={200: SBInvoiceOut, 403: MessageOut})
def get_invoice_by_id(request, id: UUID4):
    print(request.user.get_all_permissions())
    auth_user = User.objects.get(id=request.auth['id'])
    if User.has_perm(perm='RX.view_invoices', self=auth_user):
        invoice = get_object_or_404(Invoices, id=id)
        if invoice:
            return 200, invoice
        else:
            return 404, {'msg': "There are no invoice yet."}
    else:
        return 403, {'msg': "You don't have permission to access this endpoint"}

    # auth_user = User.objects.get(id=request.auth['id'])
    # if User.has_perm(perm='RX.add_invoices', self=auth_user):
    #     item_stock_instance = ScientificOfficeStock.objects.get(id=payload.ProductName)
    #     distributor_warehouse = DistributorWarehouse.objects.get(id=payload.InvoiceDW)
    #     invoice = Invoices.objects.create(InvoiceNumber=payload.InvoiceNumber, InvoiceDate=payload.invoice_date,
    #                                       InvoiceDW=distributor_warehouse, PaymentTerms=payload.PaymentTerms,
    #                                       DueDate=payload.DueDate, ProductName=item_stock_instance,
    #                                       Quantitiy=payload.Quantitiy, SellPrice=payload.SellPrice)
    #     invoice.save()
    #
    #     return 200, {'msg': "The invoice created successfully"}
    # else:
    #     return 403, {'msg': "You don't have permission to access this endpoint"}

# # 'RX.view_scientificofficestock'
# def custom_has_perm(auth_user: User, permParam: str):
#     for perm in auth_user.get_all_permissions():
#         if perm == permParam:
#             return True
#
#     return False
#     # print(auth_user.has_perm('RX.view_scientificofficestock', obj=ScientificOfficeStock))
