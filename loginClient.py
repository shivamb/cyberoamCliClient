#!/usr/bin/python
import time
import requests # Install with 'pip install requests'

import xml.etree.ElementTree as ET

cr_login_url='http://192.168.0.1:8090/login.xml'
cr_keep_alive_url='http://192.168.0.1:8090/live'
cr_logout_url='http://192.168.0.1:8090/logout.xml'
cr_username='username'
cr_password='password'

print 'cyberoam login initiated..'

def cr_login():
  print 'cyberoam login in.'
  login_payload = {'mode': '191', 'username': cr_username, 'password': cr_password}
  login_req = requests.post(cr_login_url, data = login_payload)
  return;

def cr_keep_alive():
  print 'cyberoam keep alive.'
  keep_alive_payload = {'mode': '192', 'username': cr_username}
  keep_alive_req = requests.get(cr_keep_alive_url, params=keep_alive_payload)
  return keep_alive_req.text;

def cr_logout():
  print 'cyberoam log out.'
  logout_payload = {'mode': '193', 'username': cr_username}
  login_req = requests.post(cr_logout_url, data = logout_payload)
  return;


keep_alive_res = cr_keep_alive()

keep_alive_res_parse = ET.fromstring(keep_alive_res)
ack_res = keep_alive_res_parse.find('ack').text

if ack_res == 'login_again':
  print 'Logged Out! Login in again..'
  cr_login()
else:
  print 'acked'

