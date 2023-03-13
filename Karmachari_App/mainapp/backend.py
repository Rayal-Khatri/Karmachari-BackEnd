from django_otp import OTPBackend
from django_otp.plugins.otp_totp.models import TOTPDevice

class TOTPBackend(OTPBackend):
    """
    Authenticates a user against their TOTP device.
    """
    def authenticate(self, request, username=None, password=None, otp_token=None, **kwargs):
        # Call the parent authenticate() method to authenticate the user's
        # username and password first
        user = super().authenticate(request, username=username, password=password, **kwargs)
        
        if user is not None and otp_token is not None:
            # Authenticate the user's TOTP device using the provided OTP token
            try:
                device = TOTPDevice.objects.get(user=user)
                if device.verify_token(otp_token):
                    return user
            except TOTPDevice.DoesNotExist:
                pass
            
        return None
