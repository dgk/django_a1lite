# -*- coding: utf-8 -*-

import sys
from django.conf import settings

def __settings_value(name, default=None):
    setattr(sys.modules[__name__], name, getattr(settings, name, default))

__settings_value('A1LITE_IPS', (
    '78.108.178.206',
    '79.137.235.129',
    '95.163.96.79',
    '212.24.38.100',
))

__settings_value('A1LITE_PAYMENT_TYPE_LOGO_UPLOAD_TO', 'a1lite_logo')
__settings_value('A1LITE_SECRET')
__settings_value('A1LITE_KEY')
__settings_value('A1LITE_SERVICE_ID')
