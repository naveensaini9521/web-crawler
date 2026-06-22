import re
import qrcode
import os

def validate_email(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if re.fullmatch(regex, email):
        return True
    return False


def validate_phone(phone):
    regex = r'^\+?1?\d{9,15}$'
    if re.fullmatch(regex, phone):
        return True
    return False


def generate_qr_code(value):
    """
    Generates a QR code of a given value.
    :param value: Phonepe://upi/pay?pa=8527676521@ybl&pn=8527676521&tr=1213&am=1.00&cu=INR
    :return:
    """
    img = qrcode.make(value)
    img.save('qrcodes/qrcode2.png')


def shutdown_pc():
    os.system("sudo shutdown -h now")


