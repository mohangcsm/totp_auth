This project shows the python implementation for Time-based OTP with Authenticator App.

The following are the dependency libraries. Use PIP or EASY_INSTALL or BREW to install the below.

	pyotp==2.3.0
	image==1.5.31
	pymongo==3.10.1
	PyQRCode==1.2.1

Installation using PIP:

	pip install -r requirements.txt

Make sure "Mongo" running with following values:

	MONGO_HOST = '127.0.0.1'
	MONGO_PORT = 27017
	MONGO_USERNAME = ''
	MONGO_PASSWORD = ''

Running Program:

	# python totp.py    			(For registering Authenticator app)
	# python totp.py email   		(For registering Authenticator app)
	# python totp.py email otp_value  	(For checking OTP generated in Authenticator app)
	

This will generate a QR code image (.svg) in the "qrcodes" folder, which can be scanned using any Authenticator app like Google Authenticator or DUO authenticator etc. 
Once the QRCode is scanned, enter the generated OTP value at the prompt to complete the Authenticator enabling.

