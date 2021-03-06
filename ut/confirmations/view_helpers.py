import flask
import os
from twilio.rest import Client


def get_creds():
    TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
    TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
    _from_ = "+12057362289"
    return (TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, _from_)


def send_confirm_text(number, message):
    "sends _message_ to _number_"
    sid, token, _from_ = get_creds()
    client = Client(sid, token)
    message = client.messages.create(body=message, from_=_from_, to=number)
    return message


def twiml(resp):
    resp = flask.Response(str(resp))
    resp.headers["Content-Type"] = "text/xml"
    return resp


def parse_date_as_string(_date_as_string):
    "This function returns two strings, 1 is the date and 1 is the time"
    _day = _date_as_string.split(" ")[0]
    _time = _date_as_string.split(" ")[-1]
    return _day, _time
