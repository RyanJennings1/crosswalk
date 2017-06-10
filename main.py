#!/usr/bin/python

'''
  File: main.py
  Author: Ryan Jennings
'''

from sys import argv
from selenium import webdriver
from bs4 import BeautifulSoup
import requests, time

version = "1.0.1"

class Crosswalk(object):
  def run(self, emailCommandLine):
    print "Running"
    self.openBrowser(emailCommandLine)

  def openBrowser(self, emailCommandLine):
    email = emailCommandLine

    # Open up webpage using selenium
    driver = webdriver.Firefox()
    #driver = webdriver.Chrome('ChromeDriver/chromedriver')
    driver.get("http://www.crosswalk.com/newsletters/")

    completedCheckboxesList = []

    bSoupCheckboxesList = self.bSoup()
    self.getCheckboxes(completedCheckboxesList, bSoupCheckboxesList)
    self.adjustCheckboxes(completedCheckboxesList, driver)
    self.enterEmail(driver, email)


  def bSoup(self):
    # Get the source text and create a list of 
    #   checkboxes using BeautifulSoup
    url = "http://www.crosswalk.com/newsletters/"
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    bSoupCheckboxesList = soup.findAll("input", {"type":"checkbox"})
    return bSoupCheckboxesList


  def getCheckboxes(self, completedCheckboxesList, bSoupCheckboxesList):
    # For each <input> tag create a string of the
    #   checkbox number
    for i in range(185):
      checkboxContent = bSoupCheckboxesList[i]
      checkboxContentStr = str(checkboxContent)
      checkboxSpliced = checkboxContentStr[11:22]
      completedCheckboxesList.append(checkboxSpliced)

  def adjustCheckboxes(self, completedCheckboxesList, driver):
    # Adjust the checkbox number if there 
    #   is a space or quote mark in string
    for i in range(len(completedCheckboxesList)):
      lst = list(completedCheckboxesList[i])
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
      print ".",
      checkbox = driver.find_element_by_id(completed_item)
      checkbox.click()
    print "Box checking complete"

  def enterEmail(self, driver, email):
    # Select and print email using selenium
    emailAddress = driver.find_element_by_class_name("emailAddress")
    emailAddress.send_keys(email)
    print "Email address submitted"

# End of Class


def printUsage():
  # Print when argument of '--help' is supplied
  print '''
Usage:
crosswalk [parameter]

Parameters:
  [email] 	- Email that is submitted after boxes checked.

Other Parameters:
  --help		- Display this menu.
  --v, --version	- Display version number
	'''

def invalidArgument():
  print "Invalid argument supplied"
  printUsage()

def argumentHandler(arg):
  if arg == " ":
    invalidArgument()
  elif arg == "--help":
    printUsage()
  elif arg == "--v" or arg == "--version":
    print version
  else:
    crosswalk = Crosswalk()
    crosswalk.run(arg)


if __name__ == "__main__":
  # Entrance to the program
  if len(argv) == 1:
    print "No command line arguments specified. \nPlease enter an email address"
    printUsage()
  elif len(argv) == 2:
    argumentHandler(argv[1].lower())
  else:
    print "Only one command line argument is supported"
