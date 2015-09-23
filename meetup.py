from __future__ import unicode_literals
 
import requests
import json
import time
import codecs
import sys

import pandas as pd

UTF8Writer = codecs.getwriter('utf8')
sys.stdout = UTF8Writer(sys.stdout)
 
# Get your key here https://secure.meetup.com/meetup_api/key/

with open('C:\Users\Bill\Documents\Invisible-College-Seattle\keys.json') as data_file:    
    mykeys = json.load(data_file)

api_key = mykeys['meetup']['key']


city = "Seattle"
state = "WA"
per_page = 200
offset = 0

# Meetup.com documentation here: http://www.meetup.com/meetup_api/docs/2/groups/
 
def get_groups(params): 
	request = requests.get("http://api.meetup.com/2/groups",params=params)
	data = request.json()
	return data

def get_discussion(params):
	request = requests.get("https://api.meetup.com/Invisible-College/boards",params=params)
	data = request.json()
	return data

def get_rsvps(params):
	request = requests.get("https://api.meetup.com/2/rsvps",params=params)
	data = request.json()
	return data
	
def get_member(params,m_id):
	request = requests.get("https://api.meetup.com/2/member/" + str(m_id),params=params)
	data = request.json()
	return data

if __name__=="__main__":
	main()
	
response=get_groups({"sign":"true","country":"US", "city":city, "state":state, "radius": 10, "key":api_key, "page":per_page, "offset":offset })
groups_df = pd.DataFrame(response['results'])

response=get_discussion({"sign":"true","photo-host":"public","key":api_key, "page":per_page})
discussions_df = pd.DataFrame(response['results'])

response=get_rsvps({"sign":"true","event_id":"222816846","photo-host":"public","key":api_key, "page":per_page})
rsvps_df = pd.DataFrame(response['results'])

m_id = 8188978
Bill=get_member({"sign":"true","photo-host":"public","key":api_key, "page":per_page},m_id)

m_id=183885830
John=get_member({"sign":"true","photo-host":"public","key":api_key, "page":per_page},m_id)

m_id=87046362
Ray=get_member({"sign":"true","photo-host":"public","key":api_key, "page":per_page},m_id)
