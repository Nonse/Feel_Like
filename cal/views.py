from django.shortcuts import render
from datetime import * #specify later
from reservations.models import Reservation 


    
def calendar(request, mondayParam = None):
    #this sort of url for prev and next--pass an incremented monday back to this view
    #{% url views.calendar weekdates|first|timedeltaDays:-7 %}
    
    #first calendar to load starts on Monday of current week
    today = date.today()
    if mondayParam == None:
        monday = today - timedelta(days=today.weekday())
    else:
        monday = datetime.strptime(mondayParam, "%Y%m%d").date()
        
    weekdates = [ monday + timedelta(days=x) for x in range(0, 7)] 
    
    hours = [time(x) for x in range(6, 24)]
    
    x = Reservation.objects.all()
    
    
    
    testDates = [x[y].start_time.replace(tzinfo = None) for y in range(0, len(x))]
    
        
        

    #sample reservation datetimes
    """testDates = [datetime(2014,10,13,13,00), 
        datetime(2014,10,14,14,00),
        datetime(2014,10,15,15,00),
        datetime(2014,10,16,15,00),
        datetime(2014,10,16,16,00),
        datetime(2014,10,17,17,00),
        datetime(2014,10,1,14,00),
        datetime(2014,10,6,15,00),
        datetime(2014,10,8,15,00),
        datetime(2014,10,28,16,00),
        datetime(2014,10,25,17,00)
        
        
        ]"""
    
    reservations = testDates
    

    
    
    context = {'weekdates': weekdates, 'hours': hours, 'reservations': reservations, 'today': today, 'x' : x}
    
    return render(request, 'cal/calendar.html', context)