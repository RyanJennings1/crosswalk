#!/usr/bin/python

from sys import argv
from selenium import webdriver
from bs4 import BeautifulSoup
import requests, time, time

class Crosswalk(object):
  def getEmail(self):
    # Select email address to use
    email = raw_input("Enter email address: ")
    return email


  def openBrowser(self):
    #email = self.getEmail()
    email = str(raw_input("Enter email address: "))

    # Open up webpage using selenium
    driver = webdriver.Firefox()
    driver.get("http://www.crosswalk.com/newsletters/")

    list1 = []

    list2 = self.bSoup()
    self.getCheckboxes(list1, list2)
    self.adjustCheckboxes(list1, driver)
    self.enterEmail(driver, email)

      
  def bSoup(self):
    # Get the source text and create a list of 
    #   checkboxes using BeautifulSoup
    url = "http://www.crosswalk.com/newsletters/"
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    list2 = soup.findAll("input", {"type":"checkbox"})
    return list2


  def getCheckboxes(self, list1, list2):
    # For each <input> create a string of the
    #   checkbox number
    for i in range(185):
      alpha = list2[i]
      beta = str(alpha)
      gamma = beta[11:22]
      list1.append(gamma)

  def adjustCheckboxes(self, list1, driver):
    # Adjust the checkbox number if there 
    #   is a space or quote mark in string
    for i in range(len(list1)):
      lst = list(list1[i])
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
      checkbox = driver.find_element_by_id(completed_item)
      checkbox.click()
    print "Box checking complete"

  def enterEmail(self, driver, email):
    # Select and print email using selenium
    muhemail = str(raw_input("Enter email address: "))
    emailAddress = driver.find_element_by_class_name("emailAddress")
    emailAddress.send_keys(muhemail)
    print "Email address submitted"


crosswalk = Crosswalk()
crosswalk.openBrowser()
