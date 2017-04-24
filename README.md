This project shows the python implementation for Time-based OTP with Authenticator App.

The following are the dependency libraries. Use PIP or EASY_INSTALL or BREW to install the below.

	pyotp
	pyqrcode
	pymongo
	base64
	Image

Make sure "Mongo" running with following values:

	MONGO_HOST = '127.0.0.1'
	MONGO_PORT = 27017
	MONGO_USERNAME = ''
	MONGO_PASSWORD = ''

Running Program : 	
    # python totp.py <email>   				(For registering Authenticator app)
    # python totp.py <email> <otp value>  	(For checking OTP generated in Authenticator app)
