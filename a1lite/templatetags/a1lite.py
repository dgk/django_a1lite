# -*- coding: utf-8 -*-
from django import template

from .. import a1lite_settings

register = template.Library()

@register.inclusion_tag('a1lite/a1lite_form.html', takes_context=True)
def a1lite_form(context, payment):
    assert (a1lite_settings.A1LITE_KEY
            and a1lite_settings.A1LITE_SERVICE_ID)

    context.update(dict(
        payment=payment,
        a1lite_key=a1lite_settings.A1LITE_KEY,
        a1lite_service_id=a1lite_settings.A1LITE_SERVICE_ID,
    ))
    return context
