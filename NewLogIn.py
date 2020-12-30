from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import json
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
import asyncio
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import difflib
import asyncio
from concurrent.futures import ThreadPoolExecutor

class InstaBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(executable_path = r'C://Users/Acer/Desktop/chromedriver_win32/chromedriver.exe')
        self.login()


    def login(self):
        
        self.driver.get('https://www.instagram.com/accounts/login')

        time.sleep(4)

        self.driver.find_element_by_name('username').send_keys(self.username)
        password = self.driver.find_element_by_name('password')      
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(4)
        

    def nav_user(self, user):
        self.driver.get('https://www.instagram.com/' + user)


    def following(self, user, limit=5):
        self.nav_user(user)  
        time.sleep(4)
        
        #switch this wethe followers or following u want to get
        #following_button = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a')
        following_button = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[3]/a')
        count = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[3]/a/span')
        count_txt = str(count.text)
        count_int = int(count_txt)
        print(count_int)
        following_button.click()
        time.sleep(4)
        fbody = self.driver.find_element_by_xpath("//div[@class='isgrP']")
        scroll = 0
        
        while scroll < (count_int/12)*3:
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fbody)
            #self.driver.execute_script("scroll(0, 250);", fbody)
            scroll += 1
            time.sleep(1)
        
        
        time.sleep(2)

        following_list = []
        follower_count = len(self.driver.find_elements_by_xpath("//a[@class='FPmhX notranslate  _0imsa ']"))
        
        for i in range(follower_count):
            follower = self.driver.find_elements_by_xpath("//a[@class='FPmhX notranslate  _0imsa ']")[i]
            following_list.append(follower.text)
        print(following_list, follower_count)
        return following_list

    def go_to_page(self, users):
        for user in users:
            
            desc_list=[]
            self.nav_user(user)
            time.sleep(4)
                        
            desc = self.driver.find_elements_by_xpath("//div[@class='-vDIg']")[0]

            time.sleep(3)
            x = str(desc.text)
            xx = re.findall(r"[\w']+", x)
            #print(xx)

            hacettepe = ['Hacettepe', 'hacettepe', 'hu', 'HU']
            time.sleep(2)

            if any(s in xx for s in hacettepe):
                #usernamee = self.driver.find_elements_by_xpath("//div[@class='nZSzR']")[0]
                usernamee=self.driver.find_elements_by_css_selector("div.nZSzR > h1")[0]
                usernamee_txt = str(usernamee.text)

                print(usernamee_txt)

                #print("Hacettepe") 



                

                try:
                    private = self.driver.find_elements_by_xpath("//div[@class='QlxVY']")[0]
                    print('Private')
                    with open("Desc.txt", "a", encoding='utf-8') as f:
                            f.write('\n')
                            f.write(str(usernamee_txt) + ' ' + 'Private')
                            f.close()



                except IndexError:
                    print('Public')
                    
                    with open("Desc.txt", "a", encoding='utf-8') as f:
                            f.write('\n')
                            f.write(str(usernamee_txt) + ' ' + 'Public')
                            f.close()


            else:

                pass


            time.sleep(2)


bot = InstaBot('r1gos_tm', 'karayev88')
bot.go_to_page(bot.following('garayevarif'))
