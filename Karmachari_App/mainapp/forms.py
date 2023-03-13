from django import forms
from .models import *

# class EventForm(forms.ModelForm):
#     class Meta:
#         model = Calendar
#         fields = '__all__'
        
class LeavesForm(forms.ModelForm):
    class Meta:
        model = Leaves
        fields = ['subject', 'date', 'duration', 'leave_type', 'message', ]
        
        widgets={
            'subject':forms.TextInput(attrs={'class':'answer_leave','rows':'1'}),
            'date':forms.DateInput(attrs={'class':'answer_leave'}),
            'duration':forms.DateInput(attrs={'class':'answer_leave'}),
            'leave_type':forms.Select(attrs={'class':'option_leave'}),
            'message':forms.Textarea(attrs={'class':'message-leave','rows':"5"}),
}
        