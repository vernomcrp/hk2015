import requests
import json

headers = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'}


def utiba_deduct(mobile, amount):
    data1 = {
        'password': '<password>',
        'type': 'mobile',
        'username': mobile
    }
    url1 = '<url1>'
    raw1 = requests.post(url1, data=json.dumps(data1), headers=headers)
    print raw1.json()
    token = raw1.json().get('data').get('accessToken')
    print token

    url2 = '<url2>/{}'.format(token)
    data2 = {
        "mobileNumber": "<mobileNumber>",
        "amount": "%s" % amount
    }
    raw2 = requests.post(url2, data=json.dumps(data2), headers=headers)
    print raw2.json()
    draft_trans = raw2.json().get('data').get('draftTransactionID')

    print draft_trans

    url3 = 'url3/{draft}/action/{access}'.format(
        draft=draft_trans,
        access=token
    )
    data3 = {
        "personalMessage": "",
        "amount": "%s" % amount
    }
    raw3 = requests.put(url3, data=json.dumps(data3), headers=headers)
    print raw3.json()
    otp_ref = raw3.json().get('data').get('otpRefCode')
    print otp_ref
    url4 = '<url4>/{draft}/{access}'.format(
        draft=draft_trans,
        access=token
    )
    data4 = {
        "mobileNumber": mobile,
        "otpString": "999999",
        "otpRefCode": otp_ref
    }
    raw4 = requests.post(url4, data=json.dumps(data4), headers=headers)
    print raw4.json()
    return raw4.status_code
