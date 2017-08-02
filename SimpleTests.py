# -*- coding: utf-8 -*- 
"""
Created on 2017/07/31
@author :David
"""
import traceback
from appium import webdriver
from time import sleep
import unittest
import Initialize

class SimpleTests(unittest.TestCase):
    """docstring for ClassName"""  
    def setUp(self):
        """docstring for fname"""
        #初始化环境
        Initialize.setUp(self)
    def tearDown(self):
        """docstring for fname"""
        #测试用例完成后的操作
        Initialize.tearDown(self)
        
    def test_FendaLoginTest(self):
        """docstring for fname"""
        '''
            手机号登录
            1. 手机号登录
        '''
        try:
            print '... start test_Mobilelogin test ...  '
            sleep(2)
            self.driver.find_element_by_id("com.guokr.fanta:id/image_view_close_ad").click()#开屏广告
            sleep(2)
            self.driver.get_screenshot_as_file('screenshot.png')
            sleep(2)
            self.driver.find_element_by_id("com.guokr.fanta:id/dialog_positive_btn").click()#存储
            sleep(2)
            self.driver.find_element_by_id("android:id/button1").click()#授权
            sleep(2)
            self.driver.find_element_by_id("android:id/button1").click()#授权
            sleep(2)
            self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout[4]/android.widget.TextView").click()
            sleep(2)
            self.driver.find_element_by_id("com.guokr.fanta:id/login").click()#点击登录
            sleep(2)
            self.driver.find_element_by_id("com.guokr.fanta:id/edit_text_mobile_number").click()#点击电话号码框
            sleep(2)
            self.driver.find_element_by_id("com.guokr.fanta:id/edit_text_mobile_number").send_keys("18011111111")#输入电话号码
            sleep(2)
            self.driver.find_element_by_id("com.guokr.fanta:id/text_view_send_verification_code").click()#发送验证码
            sleep(2)
            self.driver.find_element_by_id("com.guokr.fanta:id/edit_text_verification_code").click()#点击验证码
            sleep(2)
            self.driver.find_element_by_id("com.guokr.fanta:id/edit_text_verification_code").send_keys("123456")#输入验证码
            sleep(0.5)
            self.driver.find_element_by_id("com.guokr.fanta:id/text_view_login_with_mobile").click()#点击登录
            sleep(3)
        except Exception,e:
            print traceback.format_exc() #returns a string instead of printing to a file
            CutScreenshot.cutScreenShot(self,sys._getframe().f_code.co_name)
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
    #unittest.main()
