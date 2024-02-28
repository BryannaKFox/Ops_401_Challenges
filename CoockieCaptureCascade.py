#!/usr/bin/env python3

# Script:                       opschallange 37
# Author:                       Bryanna Fox
# Date of latest revision:      2/27/2024
# Purpose:                      Coockie Capture

import requests
from bs4 import BeautifulSoup
import webbrowser

# Target site to retrieve and send cookies
target_site = "http://www.whatarecookies.com/cookietest.asp"

# Function to retrieve cookies from the target site
def retrieve_cookies():
    response = requests.get(target_site)
    cookie = response.cookies
    return cookie

# Function to send cookies back to the target site
def send_cookies(cookie):
    response = requests.get(target_site, cookies=cookie)
    return response

# Function to generate HTML file with HTTP response content
def generate_html(response_content):
    with open("response_content.html", "w") as file:
        file.write(response_content)

# Function to open the generated HTML file in Firefox
def open_in_firefox():
    webbrowser.get("firefox").open("response_content.html")

def main():
    cookie = retrieve_cookies()
    response = send_cookies(cookie)
    response_content = response.text
    generate_html(response_content)
    open_in_firefox()

if __name__ == "__main__":
    main()
