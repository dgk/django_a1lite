# -*- coding: utf-8 -*-
import django.dispatch

payment_processed = django.dispatch.Signal()
success_page_visited = django.dispatch.Signal(providing_args=['request', ])
error_page_visited = django.dispatch.Signal(providing_args=['request', ])
