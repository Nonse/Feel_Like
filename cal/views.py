from django.shortcuts import render
from datetime import * #specify later
from reservations.models import Reservation 


    
def calendar(request, mondayParam = None):
    
    #first calendar to load starts on Monday of current week
    today = date.today()
    if mondayParam == None:
        monday = today - timedelta(days=today.weekday())
    else:
        monday = datetime.strptime(mondayParam, "%Y%m%d").date()
    
    #fill list with days of week displayed
    weekdates = [ monday + timedelta(days=x) for x in range(0, 7)] 
    
    #fill list with hours for calendar. datetime necessary to use timedelta for incrementing
    hours = []
    t = time(6, 30)
    d = date(1,1,1)    
    
    for y in range(0,31):
        t = (datetime.combine(d,t) + timedelta(minutes=30)).time()
        hours.append(t)
    
    
    reservations = Reservation.objects.all()
    #gets the number of half hours in a reservation and add number as attribute to reservation
    for y in reservations:
        timeDifference = y.end_time - y.start_time 
        reservationLength = timeDifference.seconds / 1800
        setattr(y, "reservationLength", reservationLength)
  
    context = {'weekdates': weekdates, 'hours': hours, 'reservations': reservations, 'today': today}
    
    return render(request, 'cal/calendar.html', context)