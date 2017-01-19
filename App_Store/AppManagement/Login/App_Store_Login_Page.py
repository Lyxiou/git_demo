# coding=utf-8

from selenium import webdriver
import unittest
from time import sleep

def check_is_login_page(self):    
    login_page_title = '应用商店登录'
    if(login_page_title == self.driver.title):
        rst = True
    else:
        rst = False

def check_is_login_text_exist(self):
    login_page_text = self.driver.find_element_by_xpath('/html/body/div/div/div/div/div[1]/h3').text
    login_page_text_dest = u'应用商店-控制台'
    if (login_page_text == login_page_text_dest):
        rst = True
    else:
        rst = False

def check_is_login_username_icon_exist(self):        
    if(self.driver.find_element_by_xpath('/html/body/div/div/div/div/div[2]/form/div[2]/div/span/span')):
        rst = True
    else:
        rst = False

def check_is_login_password_icon_exist(self):        
    if(self.driver.find_element_by_xpath('/html/body/div/div/div/div/div[2]/form/div[3]/div/span/span')):
        rst = True
    else:
        rst = False
    
def check_is_username_frame_exist(self):        
    if (self.driver.find_element_by_id("username")):
        rst = True
    else:
        rst = False
    
def check_is_password_frame_exist(self):
    if (self.driver.find_element_by_id("password")):
        rst = True
    else:
        rst = False
    
def check_is_login_button_exist(self):
    if (self.driver.find_element_by_xpath("//input[@value='登录']")):
        rst = True
    else:
        rst = False
    