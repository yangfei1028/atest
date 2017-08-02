#coding:utf-8
"""
Created on 2017/08/01
@author: David
"""
from appium import webdriver
import os
import sys
Path = sys.path[0]

def setUp(self):
    """docstring for """
    desired_caps = {}
    desired_caps["platformVersion"] = "6.0"
    desired_caps["platformName"] = "Android"
    desired_caps["appActivity"] = ".ui.activity.MainActivity"
    desired_caps["appPackage"] = "com.guokr.fanta"
    #desired_caps["androidInstallPath"] = "/Users/yangfei/Downloads/2.9.0-Fanta-release-QDHome.apk"
    desired_caps["androidInstallPath"] = Path+"2.9.0-Fanta-release-QDHome.apk"
    desired_caps["automationName"] = "Appium"
    desired_caps["deviceName"] = "testly"
    self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
def tearDown(self):
    self.driver.quit()
    print '........end........'
