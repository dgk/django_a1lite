# -*- coding: utf-8 -*-

from django.core.exceptions import PermissionDenied
from django.http import (
    HttpResponse,
    HttpResponseNotAllowed,
    HttpResponseBadRequest,
)

from django.views.decorators.csrf import csrf_exempt

from .models import Payment, PaymentType

import a1lite_settings

@csrf_exempt
def process(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed('Method not allowed')

    _check_ip(request)

    order_id = request.POST.get('order_id')
    try:
        payment = Payment.objects.get(id=order_id)
    except Payment.DoesNotExist:
        return HttpResponseBadRequest('Payment for order_id=%s not found' % order_id)

    try:
        payment.process(request.POST)
    except Payment.InvalidSignature:
        return HttpResponseBadRequest('Invalid signature')

    return HttpResponse('OK')

def success(request):
    pass

def error(request):
    pass



def _check_ip(request):
    a1lite_ips = a1lite_settings.A1LITE_IPS
    if a1lite_ips:
        if (request.META['REMOTE_ADDR'] not in a1lite_ips
            and request.META.get('X_REAL_IP') not in a1lite_ips):
            raise PermissionDenied()
