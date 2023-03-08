from django import forms
from .models import *
from django.views.generic import DetailView

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
        
# class PayrollForm(forms.ModelForm):
#     class Meta:
#         model = Payroll
#         fields = ('basic_pay_rate', 'overtime', 'deductions', 'net_pay', 'hours_worked')
#         widgets = {
#             'net_pay': forms.TextInput(attrs={'readonly': True}),
#             'hours_worked': forms.TextInput(attrs={'readonly': True}),
#        }
        
# class PayrollDetailView(DetailView):
#     model = Payroll
#     template_name = 'payroll_detail.html'

#     def get_queryset(self):
#         return super().get_queryset().filter(employee=self.request.user)

# class PayrollDetailView(DetailView):
#     model = Payroll
#     template_name = 'payroll_detail.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         payroll = self.get_object()
#         net_salary = payroll.calculate_net_salary()
#         context['net_salary'] = net_salary
#         return context