#!/usr/bin/env python3
'''
  File: main.py
  Author: Ryan Jennings
'''

import os

from sys import argv

import requests

from bs4 import BeautifulSoup
from selenium import webdriver

class Crosswalk:
    """Crosswalk Object"""
    version = "1.1.1"
    CHROME_DRIVER_FILEPATH = os.getenv("HOME") + "/.chromedriver/chromedriver"
    driver = webdriver.Chrome(CHROME_DRIVER_FILEPATH)

    def run(self, email_address):
        """Run method"""
        print("Running ...")
        self.open_browser(email_address)

    def open_browser(self, email_address):
        """open browser method"""
        # Open up webpage using selenium
        self.driver.get("http://www.crosswalk.com/newsletters/")

        completed_checkboxes_list = []

        bsoup_checkboxes_list = self.bsoup()
        self.get_checkboxes(completed_checkboxes_list, bsoup_checkboxes_list)
        self.adjust_checkboxes(completed_checkboxes_list)
        self.enter_email(email_address)

    def bsoup(self):
        """bsoup method"""
        # Get the source text and create a list of
        # checkboxes using BeautifulSoup
        url = "http://www.crosswalk.com/newsletters/"
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")
        bsoup_checkboxes_list = soup.findAll("input", {"type":"checkbox"})
        return bsoup_checkboxes_list

    def get_checkboxes(self, completed_checkboxes_list, bsoup_checkboxes_list):
        """get checkboxes"""
        # For each <input> tag create a string of the
        # checkbox number
        for i in range(185):
            checkbox_content = bsoup_checkboxes_list[i]
            checkbox_content_str = str(checkbox_content)
            checkbox_spliced = checkbox_content_str[11:22]
            completed_checkboxes_list.append(checkbox_spliced)

    def adjust_checkboxes(self, completed_checkboxes_list):
        """adjust checkboxes method"""
        # Adjust the checkbox number if there
        # is a space or quote mark in string
        for i in range(len(completed_checkboxes_list)):
            lst = list(completed_checkboxes_list[i])
            for j in range(len(lst)):
                completed_item = "".join(lst)
                if completed_item[-1] == '"':
                    completed_item = completed_item[0:-1]
                elif completed_item[-2] == '"':
                    completed_item = completed_item[0:-2]
                elif completed_item[-1] == ' ':
                    completed_item = completed_item[0:-1]
                elif completed_item[-2] == ' ':
                    completed_item = completed_item[0:-2]
            # Selected checkbox and click using selenium
            print(".", end='')
            checkbox = self.driver.find_element_by_id(completed_item)
            checkbox.click()
        print("\nBox checking complete")

    def enter_email(self, email):
        """enter email"""
        # Select and print email using selenium
        email_address = self.driver.find_element_by_class_name("emailAddress")
        email_address.send_keys(email)
        print("Email address submitted")

# End of Class

def print_usage():
    """print usage method"""
    # Print when argument of '--help' is supplied
    print('''
Usage:
crosswalk [parameter]

Parameters:
  [email] 	- Email that is submitted after boxes checked.

Other Parameters:
  --help		- Display this menu.
  --v, --version	- Display version number
	''')

def invalid_argument():
    """invalid argument method"""
    print("Invalid argument supplied")
    print_usage()

def argument_handler(arg):
    """argument handler"""
    crosswalk = Crosswalk()
    if arg == " ":
        invalid_argument()
    elif arg == "--help":
        print_usage()
    elif arg in ("--v", "--version"):
        print(crosswalk.version)
    else:
        crosswalk.run(email_address=arg)

if __name__ == "__main__":
    if len(argv) == 1:
        print("No command line arguments specified. \nPlease enter an email address")
        print_usage()
    elif len(argv) == 2:
        argument_handler(argv[1].lower())
    else:
        print("Only one command line argument is supported")
