from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import datetime
from mainapp.models import Attendance, User
import schedule
import calendar
from django.utils.timezone import make_aware
from datetime import date, timedelta,time


class Command(BaseCommand):
    help = 'Marks users as absent if they did not check in/out'
    def handle(self, *args, **options):
        def mark_absent():
            # Get all users
            users = User.objects.all()
            # Get today's date
            today = timezone.now().date()
            # Loop through each user
            for user in users:
                # Check if the user has a check-in/out record for today
                attendance_exists = Attendance.objects.filter(user=user, dateOfQuestion=today).exists()
                if not attendance_exists:
                    # If no attendance record exists, create a new one with a status of 'Absent'
                    attendance = Attendance(user=user, dateOfQuestion=today, status='Absent',checkInTime=datetime.now(),checkOutTime=datetime.now())
                    attendance.save()
                    print('saved')
                    
        def mark_saturdays_as_leave(year, month):
            # Get the first and last day of the month
            first_day = date(year, month, 1)
            last_day = date(year, month, calendar.monthrange(year, month)[1])
            today = timezone.now().date()
            
            # Loop through each Saturday in the month and mark it as Leave
            for day in range(1, last_day.day + 1):
                loop_date = timezone.datetime(year, month, day).date()
                
                if loop_date.weekday() == 5:  # Saturday is the 5th day of the week
                    for user in User.objects.all():
                        next_saturday = loop_date + timedelta((6 - today.weekday()) % 7 + 1)
                        attendance, _ = Attendance.objects.get_or_create(user=user, dateOfQuestion=next_saturday)
                        attendance.status = 'Leave'
                        attendance.checkInTime = make_aware(datetime.combine(next_saturday, time(0, 0)))
                        attendance.checkOutTime = make_aware(datetime.combine(next_saturday, time(0, 0)))
                        attendance.save()
                        print('saturday')

        # Schedule the function to run at the end of the day
        schedule.every().day.at('23:59').do(mark_absent)

        # Schedule the function to run at the end of each month
        schedule.every(calendar.monthrange(timezone.now().year, timezone.now().month)[1]).days.do(lambda: mark_saturdays_as_leave(timezone.now().year, timezone.now().month))
        
        mark_saturdays_as_leave(timezone.now().year, timezone.now().month)
        # Run the schedule loop
        while True:
            # mark_absent()
            schedule.run_pending()