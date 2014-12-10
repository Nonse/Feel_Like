from django.shortcuts import render
from datetime import * #specify later
from reservations.models import Reservation, Coach

#duration of one slot in the calendar, also used to create reservations
timeIncrement = timedelta(minutes=30)
activeCoach = 1
     
def calendar(request, mondayParam = None, coachParam = None):
    
    #first calendar to load starts on Monday of current week
    today = date.today()
    if mondayParam == None:
        monday = today - timedelta(days=today.weekday())
    else:
        monday = datetime.strptime(mondayParam, "%Y%m%d").date()
    
    global activeCoach    
    #set coach 
    if coachParam != None:
        activeCoach = coachParam
    
    #fill list with days of week displayed
    weekdates = [ monday + timedelta(days=x) for x in range(0, 7)] 
    
    #fill list with hours for calendar. datetime necessary to use timedelta for incrementing
    hours = []
    t = time(6, 30)
    d = date(1,1,1)    
    
    for y in range(0,31):
        t = (datetime.combine(d,t) + timeIncrement).time()
        hours.append(t)
    
    #query for reservations .select_related gets connects coach and customer tables
    coaches = Coach.objects.all()
    reservations = Reservation.objects.filter(coach = activeCoach).select_related(
    'coach__last_name' 
    'coach__first_name' 
    'customer__last_name' 
    'customer__first_name')
    startTimes = []
    for x in reservations:
        startTimes.append(x.start_time)
    #gets the number of half hours in a reservation and add number as attribute to reservation
    for y in reservations:
        timeDifference = y.end_time - y.start_time 
        reservationLength = timeDifference.seconds / 1800
        setattr(y, "reservationLength", reservationLength)
  
    #Shunt everything off to the calendar
    context = {
    'weekdates': weekdates, 
    'hours': hours, 
    'reservations': reservations, 
    'startTimes': startTimes, 
    'coaches': coaches,
    'activeCoach' : activeCoach,
    'today': today}
    if request.user.is_authenticated():
        return render(request, 'cal/calendar.html', context)
    else:
        return render(request, 'cal/calendarUnauthenticated.html', context)