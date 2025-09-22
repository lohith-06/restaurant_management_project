import string
import secrets
from .models import Coupon  # Assuming you have a Coupon model to store codes

def generate_coupon_code(length=10):
    """
    Generate a unique alphanumeric coupon code.

    Args:
        length (int): Length of the coupon code. Default is 10.

    Returns:
        str: Unique alphanumeric coupon code.
    """
    characters = string.ascii_uppercase + string.digits  # A–Z, 0–9

    while True:
        # Generate a secure random string
        code = ''.join(secrets.choice(characters) for _ in range(length))

        # Check database to ensure uniqueness
        if not Coupon.objects.filter(code=code).exists():
            return code