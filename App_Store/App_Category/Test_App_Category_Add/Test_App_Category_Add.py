# coding=utf-8

from selenium import webdriver
import unittest
from time import sleep
from Test_App_Base import *


class TestAppCategory(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.base_url = "http://10.110.1.55:8082/admin/home.html"
        #http://10.110.1.55:8082/login.html
        self.driver.get(self.base_url)
        self.driver.find_element_by_id("username").send_keys("admin")
        self.driver.find_element_by_id("password").send_keys("123456")
        self.driver.find_element_by_xpath("//input[@value='登录']").click()
        sleep(1) 
        sreach_window=self.driver.current_window_handle    
        self.driver.find_element_by_link_text("应用分类").click()
        sleep(1)         
        
    def check_select_parent_category(self):
        sreach_window = self.driver.current_window_handle 
        parent_categories = self.driver.find_element_by_id("parent").find_elements_by_tag_name("option")
        parent_category_text = []
        
        for parent_category in parent_categories:
            parent_category.click()
            parent_category_text.append(parent_category.text)
            print(parent_category.text)
            
        for catgry in parent_category_text:            
            print("List %s"%catgry)
            str = u'不选择为父类'
            print(str)
            if (catgry == str):
                rst = True
                break
            else:
                rst = False
        return rst
          
    def check_category_name(self, category_name):  
        self.driver.find_element_by_id('catName').clear()
        self.driver.find_element_by_id('catName').send_keys(category_name)
        for chrct in category_name:
            if(check_is_chinese(category_name)):
                rst = check_chinese_name_format_and_len(category_name)
            else:
                rst = check_name_format_and_len(category_name)
            return rst
        
    def check_category_order(self, category_order):
        self.driver.find_element_by_id('seqNum').clear()
        self.driver.find_element_by_id('seqNum').send_keys(category_order)
        return check_is_number(category_order)
    
    def check_select_file(self, file_url):
        self.driver.find_element_by_id('catImgFile').send_keys(file_url)
        if(file_url.endswith('.jpg')):
            rst = True
        else:
            rst = False
        return rst
    
    def check_list_item_total(self):
        list_items = self.driver.find_elements_by_xpath('//*[@id="grid-data"]/tbody/tr')
        list_total = 0
        for list_item in list_items:
            list_total = list_total + 1
        print("Total list items is %r"%list_total )
        return list_total
    
    def check_save(self , list_item_sub):
        sreach_window=self.driver.current_window_handle        
        category_add_page_url = r'http://10.110.1.55:8082/admin/catnew.html'
        category_page_url = r'http://10.110.1.55:8082/admin/catlist.html'
        if((category_page_url == self.driver.current_url) & (list_item_sub == 1)):
            return True
        elif((category_add_page_url == self.driver.current_url) & (list_item_sub == 0)):
            return False    
        
    def test_select_parent_category_right(self):
        list_item_total_before = self.check_list_item_total()  
        sreach_window=self.driver.current_window_handle    
        self.driver.find_element_by_link_text("添加分类").click()
        sleep(1)      
        self.assertTrue(self.check_select_parent_category())
        self.assertTrue(self.check_category_name('english name'))
        self.assertTrue(self.check_category_name('12345'))
        #self.assertFalse(self.check_category_name(u'中文字符？》《'))
        self.assertFalse(self.check_category_name('#$%'))
        self.assertFalse(self.check_category_name(u'＃＄％'))
        self.assertTrue(self.check_category_name(u'中文名'))
        self.assertFalse(self.check_category_order(u'顺序'))
        self.assertTrue(self.check_category_order('5'))
        f = open('jpg.txt','r')
        lines = f.readlines()
        for line in lines:
            file_url = line.split()[0]        
            break
        self.assertTrue(self.check_select_file(file_url))
        f.close()  
        
        self.driver.find_element_by_id('savebtn').click()
        sleep(1)
        sreach_window=self.driver.current_window_handle   
        list_item_total_after = self.check_list_item_total()   
        list_item_sub = list_item_total_after -  list_item_total_before
        self.assertTrue(self.check_save(list_item_sub))
        sleep(1)        
    '''
    def test_select_parent_category_False(self):        
        self.assertTrue(self.check_select_parent_category())
        self.assertTrue(self.check_category_name('english name'))
        self.assertFalse(self.check_category_name(u'＃＄％'))
        self.assertFalse(self.check_category_order(u'顺序'))
        f = open('jpg.txt','r')
        lines = f.readlines()
        for line in lines:
            file_url = line.split()[0]        
            break
        self.assertTrue(self.check_select_file(file_url))
        f.close()
        self.assertFalse(self.check_save())
    '''    
        
    
        
if __name__ == '__main__':
  unittest.main()