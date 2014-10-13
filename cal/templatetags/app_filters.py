from django import template
from datetime import datetime, timedelta

register = template.Library()

@register.filter(name='combine_datetime')
def combine_datetime(date, time):
   
    return datetime.combine(date, time)
    
@register.filter(name='timedeltaDays')
def timedeltaDays(day, x):
    day = day + timedelta(x)
    return day