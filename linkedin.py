#coding=utf-8
import requests
import re
from bs4 import BeautifulSoup, Comment
import lxml
import time
from lxml import html
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import MySQLdb
import random

user = ''
pswd = ''
URL = 'http://www.linkedin.com/feed/'
driver = webdriver.Chrome('./chromedriver')

def login(s):
    driver.get('https://www.linkedin.com/uas/login')
    u=driver.find_element_by_xpath('//input[@id="session_key-login"]')
    p=driver.find_element_by_xpath('//input[@id="session_password-login"]')
    u.send_keys(user)
    p.send_keys(pswd)
    driver.find_element_by_xpath('//input[@value="Sign In"]').click()
    sleep(2)
    search=driver.find_element_by_xpath('//input[@aria-autocomplete="list"]')
    search.send_keys("Google")
    driver.find_element_by_xpath('//button[@data-control-name="nav.search_button"]').click()
    conn = MySQLdb.connect("127.0.0.1","root","65326166","linktest",charset="utf8")
    cur = conn.cursor()
    for j in range(0,12):
        sleep(random.uniform(1,5))
        js="var q=document.body.scrollTop=3000"
        driver.execute_script(js)
        sleep(1)
        js="var q=document.body.scrollTop=5000"
        driver.execute_script(js)
        sleep(random.uniform(2,4))
        tree = html.fromstring(driver.page_source)
        el = tree.xpath('//ul[contains(@class,"results-list")]/li')
        el1 = el[0].xpath('//span[contains(@class,"actor-name")]')
        el2 = el[0].xpath('//div[@class="search-result search-entity search-result--person search-result--occlusion-enabled ember-view"]//div[@class="search-result__wrapper"]//div[@class="search-result__info pt3 pb4 ph0"]//p[contains(@class,"subline-level-1")]')
        for i in range(0,(len(el1))):
            el3 = el[0].xpath('//div[contains(@class,"search-result--occlusion-enabled")]//div[@class="search-result__wrapper"]//div[@class="search-result__info pt3 pb4 ph0"]//a[@data-control-name="search_srp_result"]')[i]
            el4 = el1[i].text.split()
            lid = el3.attrib['href'].rstrip('/').lstrip('/in/')
            # timenow = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            timenow = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
            sql = "SELECT * FROM users WHERE linkedin_id = '"+lid+"';"
            aa = cur.execute(sql)
            if aa==0:
                sql = "INSERT INTO users (first_name,last_name,linkedin_url,linkedin_id,created_at,updated_at) VALUES ('"+el4[0]+"','"+el4[len(el4)-1]+"','http://www.linkedin.com"+el3.attrib['href']+"','"+lid+"','"+timenow+"','"+timenow+"');"
            else:
                sql = "UPDATE users SET first_name = '"+el4[0]+"',last_name = '"+el4[len(el4)-1]+"',updated_at='"+timenow+"' WHERE linkedin_id='"+lid+"';"

            print sql
            cur.execute(sql)
            conn.commit()
            
        driver.find_element_by_xpath('//button[@class="next"]').click()
    conn.close()


s = requests.session()
s = login(s)
