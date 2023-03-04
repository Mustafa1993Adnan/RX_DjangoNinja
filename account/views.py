from django.contrib.auth import authenticate
from django.shortcuts import render

# Create your views here.
from ninja import Router
from ninja.responses import codes_4xx


from account.authorization import get_tokens_for_user
from account.schemas import AccountLoginBody, AccountOut
from utilities.schemas import MessageOut

account_controller = Router(tags=['Accounts'])


@account_controller.post('/login', response={200: AccountOut, codes_4xx: MessageOut})
def login_user(request, paylod: AccountLoginBody):
    user = authenticate(email=paylod.email, password=paylod.password)
    if not user:
        return 404, {'msg': 'Email or password are incorrect, please try again'}
    # if not user.is_verified:
    #     otp = Otp.objects.create(user=user)
    #     mail_to_send = EmailMessage(
    #         subject='Password Reset',
    #         body=f"Your password reset otp is: {otp.number}",
    #         to=[user.email, ]
    #     )
    #     mail_to_send.send(fail_silently=True)
    #     return 403, {'msg': 'Please Verify your account'}
    token = get_tokens_for_user(user)
    print(token)
    return 200, {
        'token': token,
        'user': user,
    }
