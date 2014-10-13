from django.shortcuts import render
from datetime import * #specify later


    
def calendar(request, mondayParam = None):
    #this sort of url for prev and next--pass an incremented monday back to this view
    #{% url views.calendar weekdates|first|timedeltaDays:-7 %}
    
    #first calendar to load starts on Monday of current week
    if mondayParam == None:
        today = date.today()
        monday = today - timedelta(days=today.weekday())
    else:
        monday = mondayParam
        
    weekdates = [ monday + timedelta(days=x) for x in range(0, 7)] 
    
    hours = [time(x) for x in range(6, 24)]

    #sample reservation datetimes
    testDates = [datetime(2014,10,13,13,00), 
        datetime(2014,10,14,14,00),
        datetime(2014,10,15,15,00),
        datetime(2014,10,16,15,00),
        datetime(2014,10,16,16,00),
        datetime(2014,10,17,17,00)]
    
    reservations = testDates
    

    
    
    context = {'weekdates': weekdates, 'hours': hours, 'reservations': reservations, 'today': today}
    
    return render(request, 'cal/calendar.html', context)