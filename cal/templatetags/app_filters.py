from django import template
from datetime import *
import pytz


register = template.Library()

@register.filter(name='combine_datetime')
def combine_datetime(date, time):
   
    return  datetime.combine(date, time).replace(tzinfo=pytz.utc)
    
@register.filter(name='timedeltaDays')
def timedeltaDays(day, x):
    day = day + timedelta(x)
    
    day = day.strftime('%Y%m%d')
    
    return day