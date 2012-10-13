# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import Payment, PaymentType

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_payed', 'status_verbose', 'created', )
    list_display_links = list_display
    list_filter = ('status', 'payment_type')

admin.site.register(Payment, PaymentAdmin)
admin.site.register(PaymentType)
