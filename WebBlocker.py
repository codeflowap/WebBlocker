""" Website Blocker """

from datetime import datetime as dt
import time

# Adding the host path
hostPath = r"D:\DataScience\Python\PythonUdemyArditSulce\Python10Apps\WebBlocker\WebBlocker\HOSTS"
# hostPath = r"C:\Windows\System32\drivers\etc\HOSTS"

# The IP the program redirects the web browser for the blocked websites
redirect = "127.0.0.1"

# Website list to be blocked
websiteList = ["www.facebook.com", "facebook.com", "www.google.com", "google.com"]

while True:
    # Check whether the current time is between working hours 8-16
    if dt(dt.now().year, dt.now().month, dt.now().day,8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,21):
        print("Working hours ... WebBlock is running")
        with open(hostPath, 'r+') as file:
            content = file.read()
            for website in websiteList:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
    else:
        with open(hostPath, 'r+') as file:
            content = file.readlines()
            for line in content:
                if not any(website in line for website in websiteList):
                    file.write(line)
    time.sleep(1000)
        
