import os
import math
import random
import smtplib
digits="0123456789"
OTP=""
for i in range(6):
OTP+=digits[math.floor(random.random()*10)]
otp = OTP + " is your login OTP"
msg=otp
s=smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("python.saketh.15@gmail.com","bmwb ypgarwspmeiu")
emailid = input("Enter your email: ")
s.sendmail('python.saketh.15@gmail.com',emailid,msg)
a = input("Enter Your OTP >>: ")
if a == OTP:
print("Verified.you successfully login.!")
else:
print("Please Check your OTP again")
