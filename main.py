import requests

def login_account(number, password):
    url = "https://capi.upay.uz/rest/ar/authorization"
    payload = {
        'password': password,
        "phone": number
    }
    headers = {
        "Authorization" : "Basic Y2FiaW5ldDpDZGU3NTYjQCFQbE0=",
        "Content-Type": "application/json"
    }

    response = requests.post(url=url, json=payload, headers=headers)
    return response.json()



def confirm_akk(confirmId, verifyCode):
    url = "https://capi.upay.uz/rest/ar/confirm_authorization"
    payload = {
        'confirmId': confirmId,
        "isTrust": True,
        "verifyCode": verifyCode
    }
    headers = {
        "Authorization" : "Basic Y2FiaW5ldDpDZGU3NTYjQCFQbE0=",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    return response.json()

def info_user(account, sessionid):
    url = "https://capi.upay.uz/rest/ucoins/user"
    headers = {
        "Account":account,
        "Authorization": "Basic Y2FiaW5ldDpDZGU3NTYjQCFQbE0=",
        "Sessionid": sessionid
    }
    response = requests.get(url, headers=headers)
    return response.json()


def get_balance (account, sessionid):
    url = "https://capi.upay.uz/rest/uo/balance"

    headers = {
        "Account":account,
        "Authorization": "Basic Y2FiaW5ldDpDZGU3NTYjQCFQbE0=",
        "Sessionid": sessionid
    }
    response = requests.get(url=url, headers=headers)
    return response.text


def cheque_create(number, account):

    url = 'https://capi.upay.uz/rest/uid_create'


    payload = {
    'account': number,
    'amount': 1000,
    'from': "",
    'phone': '',
    'regioncode': '',
    'serviceId': 40,
    'subRegionCode': '',
    'to': "",
    'type': "91",
    "uidType": 0
    
    }

    headers = {
        "Account":account,
        "Authorization": "Basic Y2FiaW5ldDpDZGU3NTYjQCFQbE0=",
    }

    response = requests.post(url=url, json=payload, headers=headers)
    return response.json()
