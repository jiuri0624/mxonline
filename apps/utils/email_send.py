from random import Random
from django.core.mail import send_mail

from users.models import EmailVerifyRecord
from mxonline.settings import EMAIL_FROM

def random_str(randomlength=8):
    str =''
    chars = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890'
    length = len(chars)-1
    random = Random()
    for i in range(randomlength):
        str+= chars[random.randint(0, length)]
    return str


def send_register_email(email, send_type='register'):
    email_record = EmailVerifyRecord()
    if send_type == 'update_email':
        code = random_str(4)
    else:
        code = random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    email_title = ''
    email_body = ''

    if send_type == 'register':
        email_title = 'mx注册激活'
        email_body = '点击下面链接注册激活账号 http://127.0.0.1:8000/active/{0}'.format(code)
    elif send_type == 'forget':
        email_title = 'mx找回密码'
        email_body = '点击下面链接重置密码 http://127.0.0.1:8000/reset/{0}'.format(code)
    elif send_type == 'update_email':
        email_title = 'mx修改邮箱验证码'
        email_body = '验证码为： {0}'.format(code)

    send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
    if send_status:
        pass