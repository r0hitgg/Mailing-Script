import smtplib
import time
i = 0
def send_maail():
	rm = "Recievr's Mail id Goes here"
	sm = "Your Mail ID goes here"
	pw ='Your password for coresponding mail id'
	message ="""your message goes here
	use for fun only 
	
	"""

	server = smtplib.SMTP('smtp.gmail.com',587)
	server.ehlo()
	server.starttls()
	server.login(sm,pw)
	server.sendmail(sm,rm,message)
	print("Sent succesfully")
	server.close()

while(i < 500):
	send_maail()
	time.sleep(1)
	i = i+1
	print("sent " + str(i) + " times")