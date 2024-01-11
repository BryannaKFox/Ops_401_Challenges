# Script:                       ops401d10-Challenge02
# Author:                       Bryanna Fox
# Date of latest revision:      1/10/2024
# Purpose:                      Create an Uptime Sensor Tool Part 2

import platform
import subprocess
import time
from datetime import datetime
from ping3 import ping
import smtplib
from email.mime.text import MIMEText

def is_host_up(host):
    try:
        # Using ping3 library to send an ICMP Echo Request packet
        response = ping(host, timeout=1)
        if response is not None:
            return True
        else:
            return False
    except Exception as e:
        print(f"Error checking {host}: {e}")
        return False

def get_user_credentials():
    email = input("Enter your email address: ")
    password = input("Enter your password: ")
    return email, password

def send_email(email, password, subject, body):
    try:
        server = smtplib.SMTP("smtp.mail.yahoo.com", 587)  
        server.starttls()
        server.login(email, password)

        message = MIMEText(body)
        message["Subject"] = subject
        server.sendmail(email, email, message.as_string())

        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")

def main():
    destination_ip = "192.168.2.103"

    # Get user credentials
    email, password = get_user_credentials()

    # Initialize the previous status to None
    prev_status = None

    while True:
        try:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]

            # Check if the host is up
            current_status = is_host_up(destination_ip)

            # Check if the status has changed
            if prev_status is not None and current_status != prev_status:
                status_change_message = f"Host status changed from {'up' if prev_status else 'down'} to {'up' if current_status else 'down'} at {timestamp}"
                send_email(email, password, "Host Status Change Notification", status_change_message)

            # Update the previous status
            prev_status = current_status

            # Print the status along with a comprehensive timestamp and destination IP
            print(f"{timestamp} {'Network Active' if current_status else 'Network Inactive'} to {destination_ip}")

            # Wait for 2 seconds before the next transmission
            time.sleep(2)
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main()
