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
            'subject':forms.TextInput(attrs={'class':'answer_leave'}),
            'date':forms.DateInput(attrs={'class':'answer_leave'}),
            'duration':forms.DateInput(attrs={'class':'answer_leave'}),
            'leave_type':forms.Select(attrs={'class':'option_leave'}),
            'message':forms.TextInput(attrs={'class':'message_leave','height':'800px'}),
}
        
class PayrollForm(forms.ModelForm):
    class Meta:
        model = Payroll
        fields = ('basic_pay_rate', 'overtime', 'deductions', 'net_pay', 'hours_worked')
        widgets = {
            'net_salary': forms.TextInput(attrs={'readonly': True}),
            'hours_worked': forms.TextInput(attrs={'readonly': True}),
        }