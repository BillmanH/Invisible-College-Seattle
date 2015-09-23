from boto.s3.connection import S3Connection
import os, boto


with open('C:\Users\Bill\Documents\Invisible-College-Seattle\keys.json') as data_file:    
    mykeys = json.load(data_file)

my_key = mykeys['aws']['key']
my_secret = mykeys['aws']['secret']

conn = S3Connection(my_key, my_secret)
mybucket = conn.get_bucket('williamjeffreyharding.com')
#mybucket.list()

local_path = "C:\Users\Bill\Documents\Invisible-College-Seattle"




def post_main_web_files(web_path, mybucket):
	'''
	post_main_web_files(web_path, mybucket)
	'''
	bucket_keys = mybucket.list()
	file_list = [n for n in os.listdir(web_path) if "." in n]
	folder_list = [n for n in os.listdir(web_path) if "." not in n]
	for file in file_list:
		print file
		if mybucket.lookup(file) != None:
			possible_key = mybucket.get_key(file)
			possible_key.set_contents_from_string(open(web_path + "\\" + file).read())
	print len(file_list), "files updated"


def post_web_files(web_path, folder, mybucket):
	web_path = web_path + "\\" + folder
	file_list = [n for n in os.listdir(web_path) if ".ini" not in n]
	for file in file_list:
		print file
		if mybucket.lookup(folder + "/" + file) != None:
			possible_key = mybucket.get_key(folder + "/" + file)
			possible_key.set_contents_from_string(open(web_path + "\\" + file).read())
	print len(file_list), "files updated"

#post one article
file = "dev_test/IC_Meetup.html"
possible_key = mybucket.get_key(file)
#then you can just upload one file at a time
possible_key.set_contents_from_string(open(web_path = r'C:\Users\Bill\Google Drive\Website\Website Resources\dataprocess\keen_log_test.html').read())
