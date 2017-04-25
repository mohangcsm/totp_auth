'''
Created on 25-April-2017
@author: mohan.kallepalli
Python imeplementation of TOTP with Authenticator app
'''

import pyotp, sys, uuid, base64, pyqrcode, os

from pymongo import MongoClient
from time import gmtime, strftime

MONGO_HOST = '127.0.0.1'
MONGO_PORT = 27017
MONGO_USERNAME = ''
MONGO_PASSWORD = ''

# -------------------------------------
client = MongoClient(MONGO_HOST,MONGO_PORT)
db=client.otp_auth			# db initialization
# -------------------------------------

def check_otp(email,totp,secret):
	otp_generated = totp.now()
	dt = strftime("%a, %d %b %Y %H:%M:%S", gmtime())
	otp_entered = raw_input("\nPlease Enter OTP generated in authenticator: ")
	if(otp_generated == otp_entered):
		res = res = db.secrets.update({'email':email,'used':'false'},{'$set':{'used':'true','date':dt}})
		os.remove('qrcodes/'+email.replace('@','-')+".svg")
		return "OTP enabled succesfully on Authenticator"
	else:
		print "Invalid Key. Try again"
		return check_otp(email,totp,secret)
def verify_otp(argv):
	email = argv[1]
	otp = argv[2]

	find = db.secrets.find({'email':email,'used':'true'})
	if find.count() != 0:
		for ele in find:
			totp = pyotp.TOTP(ele['secret'])
			otp_generated = totp.now()

			if otp == otp_generated:
				exit("OTP Matched")
		exit("OTP Matching Failed")
	else:
		exit('Authenticator app not registerd. Please register first.')


def main(argv):
    try:
		if len(argv) == 3:
			verify_otp(argv)

		if len(argv) == 2:
			email = argv[1]

		elif len(argv) == 1:
			email = raw_input("\nEnter Email ID to be used: ").strip(" ")

		else:
			print "Error. Try again\n"
			exit("Usage : python totp.py <email -optional> <otp -optional>\n")

		dt = strftime("%a, %d %b %Y %H:%M:%S", gmtime())
		secret = base64.b32encode(str(uuid.uuid4())).strip("=")

		find = db.secrets.find({'email':email,'used':'false'})
		if find.count() == 0:
			res = db.secrets.insert({'email':email,'date':dt,'secret':secret,'used':'false'})
		else:
			for ele in find:
				secret = ele['secret']

		totp = pyotp.TOTP(secret)
		qr_str = totp.provisioning_uri(email)

		img = pyqrcode.create(qr_str)
		if not os.path.exists('qrcodes'):
			os.makedirs('qrcodes')

		img.svg('qrcodes/'+email.replace('@','-')+".svg", scale=8)
		print '\nQRCode is saved as "qrcodes/'+email.replace('@','-')+'.svg"'

		raw_input('\npress enter after scanning QR code with Authenticator app')
		print check_otp(email,totp,secret)


    except KeyboardInterrupt:
        print " Identified. Program Terminated"
    except Exception as Ae:
        print "Program Terminated: " + str(Ae)

# -------------------------------------
if __name__ == '__main__':
# -------------------------------------
    main(sys.argv[0:])
