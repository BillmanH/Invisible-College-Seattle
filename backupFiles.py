from boto.s3.connection import S3Connection
import os, boto


with open('C:\Users\Bill\Documents\Invisible-College-Seattle\keys.json') as data_file:    
    mykeys = json.load(data_file)

my_key = mykeys['aws']['key']
my_secret = mykeys['aws']['secret']

conn = S3Connection(my_key, my_secret)
mybucket = conn.get_bucket('williamjeffreyharding.com')
#mybucket.list()

local_path = "C:\Users\Bill\Documents\Invisible-College-Seattle\{}"

file = "dev_test/sample_page.html"
possible_key = mybucket.get_key(file)
		
possible_key.set_contents_from_string(open(local_path.format("sample_page.html")).read())
