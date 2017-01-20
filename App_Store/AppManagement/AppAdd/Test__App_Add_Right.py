# coding=utf-8

from selenium import webdriver
import unittest
from time import sleep
import os

class TestAppManagementLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.base_url = 'http://10.110.1.55:8082/admin/home.html'
        #http://10.110.1.55:8082/login.html
        self.driver.get(self.base_url)
        self.driver.find_element_by_id("username").send_keys("admin")
        self.driver.find_element_by_id("password").send_keys("123456")
        self.driver.find_element_by_xpath("//input[@value='登录']").click()
        sleep(1) 
        sreach_window=self.driver.current_window_handle    
        self.driver.find_element_by_link_text("应用管理").click()
        sleep(1)
        sreach_window=self.driver.current_window_handle 
        self.driver.find_element_by_link_text("待审核").click()
        sleep(1)
        sreach_window=self.driver.current_window_handle    
        self.driver.find_element_by_link_text("添加应用").click()
        sleep(1)
        self. write_file_name_to_txt()
    def write_file_name_to_txt(self):
        #packagepath = 'D:\\workspace\\Test1\\test\\test.py\\Package'
        #allfilename = 'D:\\workspace\\Test1\\test\\test.py\\Package\\all.txt'
        print (os.getcwd())
        current_path = os.getcwd()
        packagepath = current_path + '\\Package'
        allfilename = current_path + '\\Package\\all.txt'
        print("all file is exit %r"%os.path.exists(allfilename))
        print("is file exit %r"%os.path.isfile(allfilename))
        print("is file exit test 3 %r"%os.path.isfile(r'.\Package\all.txt'))

        if not os.path.exists(allfilename):
            f = open('all.txt','w')
            for filename in os.listdir(packagepath):
                fullname=os.path.join(packagepath,filename)
                if os.path.isfile(fullname):
                    f.write(fullname)
                    f.write("\n")
            f.close()
            f = open('all.txt','r')
            f2 = open('apk.txt','w')
            f3 = open('jpg.txt','w')
            f4 = open('other.txt','w')
            for line in f.readlines():
              print(line)
              name = line.split()[0]
              if name.endswith('.apk'):
                f2.write(name)
                f2.write("\n")
              elif name.endswith('.jpg'):
                f3.write(name)
                f3.write("\n")
              else:
                f4.write(name)
                f4.write("\n") 
            f4.close()      
            f3.close()
            f2.close()          
            f.close()
        else:
            print("files is exist")
    def check_upload_app(self, appurl,exit_flag): 
        driver = self.driver
        sreach_window=driver.current_window_handle          
        upload = driver.find_element_by_id('apkFile')
        upload.send_keys(appurl)
        if( (appurl.endswith('.apk')) &(exit_flag == False) ):
            rst = True
        else:
            rst = False
        return rst
    ''' 
    def test_upload_app_not_exit_apk(self):
        f1 = open('apk.txt','r')
        lines = f1.readlines()
        for line in lines:
            appurl = line.split()[0]        
            exit_flag = False
            result = self.check_upload_app(appurl, exit_flag)
            f2 = open('apk_exit.txt','w')
            f2.write(appurl)
            f2.write("\n")
            break 
        f2.close() 
        f1 = open('apk.txt','w')
        f1.writelines(lines[1:])
        f1.close()         
        self.assertTrue(result) 
    '''
    def is_chinese(self, uchar):
        """判断一个unicode是否是汉字"""
        if uchar >= u'\u4e00' and uchar<=u'\u9fa5':
                return True
        else:
                return False 

    def is_number(self, uchar):
            """判断一个unicode是否是数字"""
            if uchar >= u'\u0030' and uchar<=u'\u0039':
                    return True
            else:
                    return False 
    
    def is_alphabet(self, uchar):
            """�判断一个unicode是否是英文字母"""
            if (uchar >= u'\u0041' and uchar<=u'\u005a') or (uchar >= u'\u0061' and uchar<=u'\u007a'):
                    return True
            else:
                    return False 
    
    def is_other(self, uchar):
            """判断是否非汉字，数字和英文字符"""
            if not (self.is_chinese(uchar) or self.is_number(uchar) or self.is_alphabet(uchar)):
                    return True
            else:
                    return False
    def is_banjiao(self, uchar):
        """判断一个unicode是否是半角"""
        for c in uchar:
            inside_code = ord(c)
            if inside_code<0x0020 or inside_code>0x7e:    #���ǰ�ǵ��ж�  
                return False
            else:
                return True
    def check_app_name_len(self, uchar): 
        if (len(uchar)<=20):
            return True
        else:
            return False
    
    def check_app_name_format_and_len(self, appname): 
        driver = self.driver
        sreach_window=driver.current_window_handle 
        driver.find_element_by_id("appName").clear()
        driver.find_element_by_id("appName").send_keys(appname)
        print(not self.is_other(appname))
        print(self.is_banjiao(appname))
        print(self.check_app_name_len(appname))
        if ((not self.is_other(appname)) and (self.is_banjiao(appname)) and self.check_app_name_len(appname)):
            rst = True
        else:
            rst = False
        return rst
    '''    
    def test_app_name_num_right(self):
        result = self.check_app_name_format_and_len("123456")
        self.assertTrue(result)
    
       
    def test_app_name_english_right(self):
        result = self.check_app_name_format_and_len("English")
        self.assertTrue(result)
     '''
    #ToDo 判断是否是选中状态״̬
    def check_app_category(self):
        sreach_window = self.driver.current_window_handle
        checkboxs = self.driver.find_elements_by_xpath('//*[@class="jstree-anchor"]/i[1]')
        for i in checkboxs:
            print(i.is_selected())
            print(i.get_attribute("aria-selected"))  
            i.click()
            sleep(1) 
            break
       # haschil = self.driver.find_element_by_xpath(r'//*[@aria-expanded="false"]/i')
       # haschil.click()
        return True 
    '''
    def test_app_category(self):
        result = self.check_app_category()
        self.assertTrue(result)
    '''
               
    def check_upload_printscreen(self, printscreen_url):
        upload = self.driver.find_element_by_id('file-2')
        upload.send_keys(printscreen_url)
        if(printscreen_url.endswith('.jpg')):
            rst = True
        else:
            rst = False
        return rst
    '''
    def test_upload_printscreen_format_right(self):
        f = open('jpg.txt','r')
        lines = f.readlines()
        for line in lines:
            printscreen_url = line.split()[0]        
            result = self.check_upload_printscreen(printscreen_url)
            break  
        f.close()         
        self.assertTrue(result)
    '''
    def check_upload_icon(self, icon_url):
        upload = self.driver.find_element_by_id('file-3')
        upload.send_keys(icon_url)
        if(icon_url.endswith('.jpg')):
            rst = True
        else:
            rst = False
        return rst
    '''
    def test_upload_icon_format_right(self):
        f = open('jpg.txt','r')
        lines = f.readlines()
        for line in lines:
            icon_url = line.split()[0]        
            result = self.check_upload_icon(icon_url)
            break  
        f.close()         
        self.assertTrue(result)
    '''
    def check_app_desc_format_and_len(self, appdec): 
        driver = self.driver
        sreach_window=driver.current_window_handle 
        driver.find_element_by_id("appDesc").clear()
        driver.find_element_by_id("appDesc").send_keys(appdec)
        print(not self.is_other(appdec))
        print(self.is_banjiao(appdec))
        print(self.check_app_name_len(appdec))
        if ((not self.is_other(appdec)) and (self.is_banjiao(appdec)) and self.check_app_name_len(appdec)):
            rst = True
        else:
            rst = False
        return rst  
    '''      
    def test_app_desc_right(self):
        result = self.check_app_desc_format_and_len("mmm")
        self.assertTrue(result)
    '''    
    def check_ver_desc_format_and_len(self, verdec): 
        driver = self.driver
        sreach_window=driver.current_window_handle 
        driver.find_element_by_id("verDesc").clear()
        driver.find_element_by_id("verDesc").send_keys(verdec)
        print(not self.is_other(verdec))
        print(self.is_banjiao(verdec))
        print(self.check_app_name_len(verdec))
        if ((not self.is_other(verdec)) and (self.is_banjiao(verdec)) and self.check_app_name_len(verdec)):
            rst = True
        else:
            rst = False
        return rst  
    ''' 
    def test_app_ver_desc_right(self):
        result = self.check_ver_desc_format_and_len("nnn")
        self.assertTrue(result)
    '''
    def check_keyword_format_and_len(self, keyword): 
        driver = self.driver
        sreach_window=driver.current_window_handle 
        driver.find_element_by_id("keyword").clear()
        driver.find_element_by_id("keyword").send_keys(keyword)
        print(not self.is_other(keyword))
        print(self.is_banjiao(keyword))
        print(self.check_app_name_len(keyword))
        if ((not self.is_other(keyword)) and (self.is_banjiao(keyword)) and self.check_app_name_len(keyword)):
            rst = True
        else:
            rst = False
        return rst 
    '''      
    def test_app_keyword_right(self):
        result = self.check_keyword_format_and_len("ccc")
        self.assertTrue(result)
    '''
    def check_app_price(self, appprice): 
        driver = self.driver
        sreach_window=driver.current_window_handle 
        driver.find_element_by_id("appPrice").clear()
        driver.find_element_by_id("appPrice").send_keys(appprice)
        print(appprice)
        if (self.is_number(appprice) and self.is_banjiao(appprice)):
            rst = True
        else:
            rst = False
        return rst
    '''
    def test_app_keyword_right(self):
        result = self.check_app_price("2")
        self.assertTrue(result)  
    '''           
    def check_app_area_world(self): 
       driver = self.driver
       sreach_window=driver.current_window_handle 
       driver.find_element_by_id("appArea").find_elements_by_tag_name("option")[0].click()
       txt1 = driver.find_element_by_id("appArea").text
       print(txt1)
       '''
       if (txt1 == 全球):
           rst = True
       else:
           rst = False
        '''
       return True
    '''   
    def test_app_area_world_right(self):
        result = self.check_app_area_world()
        self.assertTrue(result)
    '''
    def check_app_area_china(self): 
       driver = self.driver
       sreach_window=driver.current_window_handle 
       driver.find_element_by_id("appArea").find_elements_by_tag_name("option")[1].click()
       txt2 = driver.find_element_by_id("appArea").text
       print(txt2)
       if (txt1 == "中国大陆"):
           rst = True
       else:
           rst = False
       return rst
    '''   
    def test_app_area_china_right(self):
        result = self.check_app_area_china()
        self.assertTrue(result)
    ''' 
     
    def check_save_submit_right(self): 
        driver = self.driver
        sreach_window=driver.current_window_handle 
        print("Current url is %s"%driver.current_url)
        print("Current title is %s"%driver.title)   
        f1 = open('apk.txt','r')
        lines = f1.readlines()
        for line in lines:
            appurl = line.split()[0]        
            exit_flag = False
            result1 = self.check_upload_app(appurl, exit_flag)
            print("result1 = %r"%result1)
            f2 = open('apk_exit.txt','w')
            f2.write(appurl)
            f2.write("\n")
            break 
        f2.close() 
        f1.close()
        f1 = open('apk.txt','w')
        f1.writelines(lines[1:])
        f1.close()         
        
        result2 = self.check_app_name_format_and_len("English")
        print("result2 = %r"%result2)
        result3 = self.check_app_category()
        print("result3 = %r"%result3)
        f = open('jpg.txt','r')
        lines = f.readlines()
        for line in lines:
            printscreen_url = line.split()[0]        
            result4 = self.check_upload_printscreen(printscreen_url)
            print("result4 = %r"%result4)
            break  
        f.close() 
        f = open('jpg.txt','r')
        lines = f.readlines()
        for line in lines:
            icon_url = line.split()[0]        
            result5 = self.check_upload_icon(icon_url)
            print("result5 = %r"%result5)
            break  
        f.close()
        result6 = self.check_app_desc_format_and_len("mmm")
        print("result6 = %r"%result6)
        result7 = self.check_ver_desc_format_and_len("nnn")
        print("result7 = %r"%result7)
        result8 = self.check_keyword_format_and_len("ccc")
        print("result8 = %r"%result8)
        result9 = self.check_keyword_format_and_len("ccc")
        print("result9 = %r"%result9)
        result10 = self.check_app_price("2")
        print("result10 = %r"%result10)
        result11 = self.check_app_area_world()
        print("result11 = %r"%result11)
        driver.find_element_by_id("savebtn").click()
        sleep(10)
        sreach_window=driver.current_window_handle 
        alert_text = self.driver.switch_to_alert().text
        print(alert_text)
        sleep(1)
        self.driver.switch_to_alert().accept()
        sleep(1)
        sreach_window= self.driver.current_window_handle 
        print("Current url is %s"%driver.current_url)
        print("Current title is %s"%driver.title)
        main_page_url = 'http://10.110.1.55:8082/admin/apkpendinglist.html'
        if(main_page_url == driver.current_url):           
            result12 = True
        else:
            result12 = False   
        print("result12 = %r"%result12)
        return (result1 and result2 and result3 and result4 and result5 and result6 and result7 and result8 and result9 and result10 and result11 and result12 )
    def test_save_submit_right(self):
        result = self.check_save_submit_right()
        self.assertFalse(result)
        
    '''  
    #//*[@id="appName-error"]
    def check_save_submit_not_select_category(self): 
        driver = self.driver
        sreach_window=driver.current_window_handle 
        result1 = self.check_app_name_format_and_len("English") 
        print("check_save_submit_not_select_category result1: %r"%result1)      
        driver.find_element_by_id("savebtn").click()
        sleep(10)
        sreach_window=driver.current_window_handle 
        sleep(1)
        alert_text = self.driver.switch_to_alert().text
        print(alert_text)
        if((alert_text == 'select category') and result1):
            rst = True
        else:
            rst = False
        return rst       
    def test_save_submit_no_appnamet(self):
        result = self.check_save_submit_not_select_category()
        self.assertTrue(result)
    
    def check_save_submit_not_updload_apk(self): 
        driver = self.driver
        sreach_window=driver.current_window_handle 
        result1 = self.check_app_name_format_and_len("English") 
        
        print("check_save_submit_not_select_category result1: %r"%result1)      
        driver.find_element_by_id("savebtn").click()
        sleep(10)
        sreach_window=driver.current_window_handle 
        sleep(1)
        alert_text = self.driver.switch_to_alert().text
        print(alert_text)
        if((alert_text == 'select category') and result1):
            rst = True
        else:
            rst = False
        return rst       
    def test_save_submit_not_updload_apk(self):
        result = self.check_save_submit_not_updload_apk()
        self.assertTrue(result)  
    '''   
if __name__ == '__main__':
  unittest.main()