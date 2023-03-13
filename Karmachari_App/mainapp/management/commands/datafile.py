import random
import pytz
from datetime import datetime, time, timedelta
from django.core.management.base import BaseCommand
from django.utils import timezone
from mainapp.models import *


class Command(BaseCommand):
    help = 'Generates random check-in and check-out data'

    def add_arguments(self, parser):
        parser.add_argument('month', type=int, help='Month number (1-12)')
        parser.add_argument('year', type=int, help='Year number (e.g. 2023)')

    def random_time(self, date, start_time, end_time):
        start_datetime = datetime.combine(date, start_time)
        end_datetime = datetime.combine(date, end_time)
        random_datetime = start_datetime + timedelta(minutes=random.randint(0, int((end_datetime - start_datetime).total_seconds() / 60)))
        return timezone.make_aware(random_datetime, pytz.UTC)

    def handle(self, *args, **options):
        month = options['month']
        year = options['year']

        start_checkin_time = time(hour=10, minute=0)
        end_checkin_time = time(hour=10, minute=30)
        start_checkout_time = time(hour=18, minute=0)
        end_checkout_time = time(hour=18, minute=30)

        users = User.objects.all()

        for user in users:
            for day in range(1, 32):
                date_of_question = datetime(year=year, month=month, day=day)

                # Check if an Attendance object already exists for this user and date
                if Attendance.objects.filter(user=user, dateOfQuestion=date_of_question).exists():
                    self.stdout.write(self.style.SUCCESS(f'Skipping generation of attendance data for user {user.id} on {date_of_question.date()} (data already exists)'))
                    continue  # Skip to the next iteration of the loop

                checkin_time = self.random_time(date_of_question, start_checkin_time, end_checkin_time)
                checkout_time = self.random_time(date_of_question, start_checkout_time, end_checkout_time)

                # Determine the status based on the schedule and check-in time
                profile = Profile.objects.get(user=user)
                department = profile.department.id
                schedule = Schedule.objects.get(department=department)
                late_time = datetime.combine(date_of_question.date(), schedule.schedule_start) + timedelta(minutes=15)
                late_time = late_time.time()

                if checkin_time.time() < late_time:
                    status = 'Present'  # Late
                else:
                    status = 'Late'  # Presents

                duration = (checkout_time - checkin_time).total_seconds()/3600.0
                try:
                    attendance = Attendance.objects.filter(user=user, dateOfQuestion=date_of_question).latest('checkInTime')
                except Attendance.DoesNotExist:
                    attendance = None

                if attendance is not None:
                    attendance.checkOutTime = checkout_time
                    attendance.duration = duration
                    attendance.status = status
                    attendance.save()
                else:
                    Attendance.objects.create(user=user, checkInTime=checkin_time, checkOutTime=checkout_time, duration=duration, status=status, dateOfQuestion=date_of_question)
                self.stdout.write(self.style.SUCCESS(f'Successfully generated attendance data for user {user.id} on {date_of_question.date()}'))


