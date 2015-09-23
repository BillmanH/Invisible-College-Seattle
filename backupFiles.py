from boto.s3.connection import S3Connection
import os, boto


with open('C:\Users\Bill\Documents\Invisible-College-Seattle\keys.json') as data_file:    
    mykeys = json.load(data_file)

my_key = mykeys['aws']['key']
my_secret = mykeys['aws']['secret']

conn = S3Connection(my_key, my_secret)
mybucket = conn.get_bucket('williamjeffreyharding.com')
#mybucket.list()



backup_path = r'C:\Users\Bill\Google Drive\Website\AWS Backup'
web_path = r'C:\Users\Bill\Google Drive\Website\Website Resources'
#my 'other' laptop:
#web_path = r'C:\Users\WilliamLaptop\Google Drive\Website\Website Resources'

#backup all files to local folder
def backup_all_files(mybucket):
	'''
	backup_all_files(mybucket)
	'''
	for key in mybucket.list():
		key_name = key.name.encode('utf-8')	
		key_text = key.get_contents_as_string()
		print key_name	
		if key_name[-1] == '/':
			if not os.path.exists(backup_path + "\\" + key_name):
				os.makedirs(backup_path + "\\" + key_name)
		else:
			text_file = open(backup_path + "\\" + key_name, "w")
			text_file.write(key_text)
			text_file.close()
		


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

def post_all_files():
	'''
	Just to push all of the files at once with a single command.
	This will ensure that all of your files are current with the S3.
	'''
	post_main_web_files(web_path, mybucket)
	folder_list = [n for n in os.listdir(web_path) if "." not in n]
	for folder in folder_list:
		post_web_files(web_path, folder, mybucket)
		
#Process
#first you back up your files:
backup_all_files(mybucket)
#then you post:	

#single command to push all of the files:
#post_all_files()

#just post the main ones:
post_main_web_files(web_path, mybucket)

#post one article
file = "dataprocess/keen_log_test.html"
possible_key = mybucket.get_key(file)
#then you can just upload one file at a time
possible_key.set_contents_from_string(open(web_path = r'C:\Users\Bill\Google Drive\Website\Website Resources\dataprocess\keen_log_test.html').read())
