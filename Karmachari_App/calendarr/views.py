from django.shortcuts import render
from django.http import JsonResponse 
from mainapp.models import Events,Profile
from mainapp.models import Attendance
import json
from django.utils import timezone
from datetime import datetime
 
# Create your views here.
# def calendar(request):  
#     user = request.user
#     all_events = Events.objects.filter(user=user)
#     profile=Profile.objects.get(user=request.user)
#     events = []
#     for event in all_events:
#         events.append({
#             'title': event.event_status,                                                                                         
#             'id': event.id,                                                                                              
#             'start': event.start.strftime("%m/%d/%Y, %H:%M:%S"),                                                         
#             'end': event.end.strftime("%m/%d/%Y, %H:%M:%S"),
#         })
    
#     context = {
#         'events': json.dumps(events),
#         'profile':profile,
#         'navbar':'attendance',
#     }
#     return render(request, 'calendar.html', context)

def calendar(request):    
    user = request.user
    all_events = Events.objects.filter(user=user)
    profile = Profile.objects.get(user=request.user)
    events = []
    user_agent = request.META['HTTP_USER_AGENT']
    if 'Mobile' in user_agent:
        width=450  
    else:
        width=600
    for event in all_events:
        events.append({
            'title': event.event_status,                                                                                         
            'id': event.id,                                                                                              
            'start': event.start.strftime("%m/%d/%Y, %H:%M:%S"),                                                         
            'end': event.end.strftime("%m/%d/%Y, %H:%M:%S"),
        })
    all_attendance = Attendance.objects.filter(user=user)
    default_time=timezone.now()
    for attendance in all_attendance:
        if attendance.checkInTime is not None and attendance.checkOutTime is not None:
            start = attendance.checkInTime.strftime("%m/%d/%Y, %H:%M:%S")
            end = attendance.checkOutTime.strftime("%m/%d/%Y, %H:%M:%S")
        else:
            start = attendance.checkInTime.strftime("%m/%d/%Y, %H:%M:%S")
            end = None
        if attendance.status == 'Present':
            className = 'fc-attendance-present'
        elif attendance.status == 'Late':
            className = 'fc-attendance-late'
        elif attendance.status == 'Leave':
            className = 'fc-attendance-leave'
        elif attendance.status == 'Absent':
            className = 'fc-attendance-absent'
        else:
            className = ''
            # start = None
            # end = None

        events.append({
            'title': attendance.status,                                                                                         
            'id': attendance.id,                                                                                              
            'start': start,                                                         
            'end': end,
            'className': 'attendance ' + className,
        })
    print(events)
    context = {
        'events': json.dumps(events),
        'profile':profile,
        'width':width,
        'navbar':'attendance',
    }
    return render(request, 'calendar.html', context)
