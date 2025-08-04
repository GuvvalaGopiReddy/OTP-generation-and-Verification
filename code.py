import os
import math
import random
import smtplib

# Generate 6-digit OTP
digits = "0123456789"
OTP = ""
for i in range(6):
    OTP += digits[math.floor(random.random() * 10)]

# Create the OTP message
otp_message = OTP + " is your login OTP"
msg = otp_message

# Setup the SMTP server
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()

# Login to your Gmail (use App Password, not your regular Gmail password)
s.login("....@gmail.com", "key")

# Get recipient email and send the OTP
emailid = input("Enter your email: ")
s.sendmail('guvvalagopireddy51@gmail.com', emailid, msg)

# Close the SMTP session
s.quit()

# Ask user for OTP and verify
a = input("Enter Your OTP >>: ")
if a == OTP:
    print("Verified. You successfully logged in!")
else:
    print("Please check your OTP again.")
