from django import template
from datetime import datetime

register = template.Library()


@register.filter
def l2l_dt(date):
    if isinstance(date, str):
        return datetime.strptime(date, '%Y-%m-%dT%H:%M:%S')
    elif isinstance(date, datetime):
        return date.strftime("%Y-%m-%dT%H:%M:%S")
    else:
        raise template.TemplateSyntaxError("Incorrect arg format")
