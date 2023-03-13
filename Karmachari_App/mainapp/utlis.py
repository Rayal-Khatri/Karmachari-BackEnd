from django.http import HttpResponse
from .models import *
from xhtml2pdf import pisa
from io import BytesIO
from django.template.loader import get_template

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
    
def render_to_pdf(template_src, context={}):
	template = get_template(template_src)
	html  = template.render(context)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None

def date_formatting(datte):
    date_string =  datte
    date_string = date_string.strip('“”')
    date_object = datetime.strptime(date_string, '%Y-%m-%dT%H:%M:%S.%f')
    return(date_object.date())