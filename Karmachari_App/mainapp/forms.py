from django import forms
from .models import *

class LeavesForm(forms.ModelForm):
    class Meta:
        model = Leaves
        fields = ['subject', 'date', 'duration', 'leave_type', 'message', ]
        
class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['attendee', 'is_present', 'duration']