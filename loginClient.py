#!/usr/bin/python
import datetime
import requests # Install with 'pip install requests'
import os # For reading env vars

import xml.etree.ElementTree as ET

cr_login_url='http://192.168.0.1:8090/login.xml'
cr_keep_alive_url='http://192.168.0.1:8090/live'
cr_logout_url='http://192.168.0.1:8090/logout.xml'

cr_username=os.environ['CR_USERNAME']
cr_password=os.environ['CR_PASSWORD']

def print_log(log_text):
  print("%s - " % datetime.datetime.now() + log_text)

def cr_login():
  print_log ('cyberoam logging in.')
  login_payload = {'mode': '191', 'username': cr_username, 'password': cr_password}
  login_req = requests.post(cr_login_url, data = login_payload)
  return login_req.text;

def cr_keep_alive():
  print_log ('cyberoam keep alive.')
  keep_alive_payload = {'mode': '192', 'username': cr_username}
  keep_alive_req = requests.get(cr_keep_alive_url, params=keep_alive_payload)
  return keep_alive_req.text;

def cr_logout():
  print_log ('cyberoam log out.')

  logout_payload = {'mode': '193', 'username': cr_username}
  login_req = requests.post(cr_logout_url, data = logout_payload)
  return;


keep_alive_res = cr_keep_alive()

keep_alive_res_parse = ET.fromstring(keep_alive_res)
ack_res = keep_alive_res_parse.find('ack').text

if ack_res == 'login_again':
  print_log ('Logged Out! Logging in again..')
  login_res = cr_login()
  login_res_parse = ET.fromstring(login_res)
  print_log ('Staus: ' + login_res_parse.find('status').text + ', Message: ' + login_res_parse.find('message').text)
else:
  print_log ('acked')
