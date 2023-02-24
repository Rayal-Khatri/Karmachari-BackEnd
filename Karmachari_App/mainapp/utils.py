from django.http import HttpResponse
from .models import AllowedIP

def check_allowed_ip(request):
    x_forw_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forw_for is not None:
        user_ip = x_forw_for.split(',')[0]
    else:
        user_ip = request.META.get('REMOTE_ADDR')
    allowed_ips = AllowedIP.objects.all()
    print('IP ADDRESS OF USER IS:', user_ip)

    if any(ip.ip_address == user_ip for ip in allowed_ips):
        # User's IP address is present in the database
        return True
    else:
        # User's IP address is not present in the database
        return False