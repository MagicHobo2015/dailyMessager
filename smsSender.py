# ---------------------------------------------------------------------------- #
#                                                                              #
#   A module to send texts through gmail.                                      #
#       AUTHOR: Joshua Land                                                    #
#                                                                              #
# ---------------------------------------------------------------------------- #


import smtplib, ssl
from dotenv import dotenv_values

# dictionary to hold carriers gateways. send sms with number + carrier[carrier]
CARRIERS = {
    'google_fi' : '@msg.fi.google.com',
    'att' : '@txt.att.net',
    'Boost' : '@myboostmobile.com',
    'cricket' : '@sms.mycricket.com',
    'metro_pcs' : '@metropcs.sms.us',
    'sprint_pcs' : '@messaging.sprintpcs.com',
    't_mobile' : '@tmomail.com',
    'verizon' : '@vtext.com',
    'virgin' : '@vmobl.com'
            }

# EMAIL, PASSWORD
env_vars = dotenv_values(".env")
# list to text.
who = { 'josh' : ['6572935902', "google_fi"] }

# for the mail
sender_email = env_vars['EMAIL']
sender_password = env_vars['PASSWORD']
receiver_email = f'7143166476{CARRIERS["verizon"]}'
# message ="""
# From: magichoboemailtosms@gmail.com
# To: 6572935902@msg.fi.google.com
# Subject: This is a test email.
# This is a test email.
# \t- Josh
# """
message = '\r\n\r\n last one I swear, did the nasty go away?'

try:
    smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
    smtp_server.ehlo()
    smtp_server.starttls()
    smtp_server.login( sender_email, sender_password )
    smtp_server.sendmail(sender_email, receiver_email, message)
    smtp_server.close()
    print('Mail Succesfully Sent')

except Exception as e:
    print('Looks like something went wrong')
    print(f'The exception was: { e }')

