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

driver = webdriver.Chrome('./chromedriver')
driver.get('https://www.linkedin.com/uas/login')
u=driver.find_element_by_xpath('//input[@id="session_key-login"]')
p=driver.find_element_by_xpath('//input[@id="session_password-login"]')
u.send_keys(user)
p.send_keys(pswd)
subm = driver.find_element_by_xpath('//input[@value="Sign In"]')
subm.send_keys(Keys.ENTER)
sleep(2)
conn = MySQLdb.connect("127.0.0.1","root","65326166","linktest",charset="utf8")
cur = conn.cursor()
aa = cur.execute('select linkedin_url,linkedin_id from users')
info = cur.fetchmany(aa)
for i in range(0,10):
	driver.get(info[i][0])
	sleep(random.uniform(2,6))
	js="var q=document.body.scrollTop=2000"
	driver.execute_script(js)
	sleep(1)
	js="var q=document.body.scrollTop=4000"
	driver.execute_script(js)
	sleep(random.uniform(2,6))
	tree = html.fromstring(driver.page_source)
	des = tree.xpath('//div[contains(@class,"pv-top-card-section__summary")]//span[contains(@class,"truncate-multiline--last-line-wrapper")]/span')

	elexp = tree.xpath('//div[contains(@class,"profile-detail")]//div[contains(@class,"pv-oc")]//section[contains(@class,"experience-section")]/ul[contains(@class,"section-info")]/li[contains(@class,"ember-view")]')
	eledu = tree.xpath('//div[contains(@class,"profile-detail")]//div[contains(@class,"pv-oc")]//section[contains(@class,"education-section")]/ul[contains(@class,"section-info")]/li[contains(@class,"ember-view")]')


	jlink = tree.xpath('//div[contains(@class,"profile-detail")]//div[contains(@class,"pv-oc")]//section[contains(@class,"experience-section")]//li[contains(@class,"ember-view")]//a')
	jposition = tree.xpath('//div[contains(@class,"profile-detail")]//div[contains(@class,"pv-oc")]//section[contains(@class,"experience-section")]//li[contains(@class,"ember-view")]//h3')
	jcompany = tree.xpath('//div[contains(@class,"profile-detail")]//div[contains(@class,"pv-oc")]//section[contains(@class,"experience-section")]//li[contains(@class,"ember-view")]//span[text()="Company Name"]/following-sibling::span[1]')
	jdate = tree.xpath('//div[contains(@class,"profile-detail")]//div[contains(@class,"pv-oc")]//section[contains(@class,"experience-section")]//li[contains(@class,"ember-view")]//span[text()="Dates Employed"]/following-sibling::span[1]')
	jdes = tree.xpath('//div[contains(@class,"profile-detail")]//div[contains(@class,"pv-oc")]//section[contains(@class,"experience-section")]//li[contains(@class,"ember-view")]//div[contains(@class,"pv-entity__extra-details")]/p')
	jj = tree.xpath('//div[contains(@class,"profile-detail")]//div[contains(@class,"pv-oc")]//section[contains(@class,"experience-section")]/ul[contains(@class,"section-info")]/li[contains(@class,"ember-view")]')
	jj2 = tree.xpath('//div[contains(@class,"profile-detail")]//div[contains(@class,"pv-oc")]//section[contains(@class,"experience-section")]/ul[contains(@class,"section-info")]/li[contains(@class,"ember-view")]/div[contains(@class,"ember-view")]')
	if len(elexp)>0:

		counter1 = 0
		for j in range(0,len(elexp)):
			jlinkedinid = jj[j].attrib['id']
			if "ember" in jlinkedinid:
				jlinkedinid = jj2[counter1].attrib['id']
				counter1 = counter1 + 1
			print jlinkedinid
			companyid = jlink[j].attrib['href'].rstrip('/').lstrip('/company-beta/')
			timenow = time.strftime('%Y-%m-%d-%H:%M:%S',time.localtime(time.time()))
			thedate = jdate[j].text
			startdate = thedate.split(u'\u2013')[0].rstrip(' ')
			enddate = thedate.split(u'\u2013')[1].lstrip(' ')
			sql = "SELECT * FROM companies WHERE company_id = '"+companyid+"';"
			bb = cur.execute(sql)
			if bb==0:
				companyurl = "http://www.linkedin.com"+jlink[j].attrib['href']
				sql = "INSERT INTO companies (company_id,company_name,linkedin_url,created_at,updated_at) VALUES ('"+companyid+"','"+jcompany[j].text.replace("\'","\\\'")+"','"+companyurl+"','"+timenow+"','"+timenow+"');"
				cur.execute(sql)
				conn.commit()
			sql = "SELECT * FROM user_in_companies WHERE linkedin_id = '"+jlinkedinid+"';"
			cc = cur.execute(sql)
			if cc==0:
				sql = "INSERT INTO user_in_companies (user_id,company_id,start_date,end_date,position,created_at,updated_at) VALUES ('"+info[i][1]+"','"+companyid+"','"+startdate+"','"+enddate+"','"+jposition[j].text.replace("\'","\\\'")+"','"+timenow+"','"+timenow+"');"
				cur.execute(sql)
				conn.commit()
			else:
				jid = cur.fetchmany(cc)
				sql = "UPDATE user_in_companies SET position='"+jposition[j].text+"',updated_at='"+timenow+"' WHERE id="+str(jid[0][0])+";"
				cur.execute(sql)
				conn.commit()
	
	elink = tree.xpath('//div[contains(@class,"profile-detail")]//div[contains(@class,"pv-oc")]//section[contains(@class,"education-section")]//li[contains(@class,"ember-view")]//a')
	eschool = tree.xpath('//div[contains(@class,"profile-detail")]//div[contains(@class,"pv-oc")]//section[contains(@class,"education-section")]//li[contains(@class,"ember-view")]//h3')
	edegree = tree.xpath('//div[contains(@class,"profile-detail")]//div[contains(@class,"pv-oc")]//section[contains(@class,"education-section")]//li[contains(@class,"ember-view")]//span[text()="Degree Name"]/following-sibling::span[1]')
	efield = tree.xpath('//div[contains(@class,"profile-detail")]//div[contains(@class,"pv-oc")]//section[contains(@class,"education-section")]//li[contains(@class,"ember-view")]//span[text()="Field Of Study"]/following-sibling::span[1]')
	estart = tree.xpath('//div[contains(@class,"profile-detail")]//div[contains(@class,"pv-oc")]//section[contains(@class,"education-section")]//li[contains(@class,"ember-view")]//span[text()="Dates attended or expected graduation"]/following-sibling::span[1]/time[1]')
	eend = tree.xpath('//div[contains(@class,"profile-detail")]//div[contains(@class,"pv-oc")]//section[contains(@class,"education-section")]//li[contains(@class,"ember-view")]//span[text()="Dates attended or expected graduation"]/following-sibling::span[1]/time[2]')
	ee = tree.xpath('//div[contains(@class,"profile-detail")]//div[contains(@class,"pv-oc")]//section[contains(@class,"education-section")]/ul[contains(@class,"section-info")]/li[contains(@class,"ember-view")]')
	ee2 = tree.xpath('//div[contains(@class,"profile-detail")]//div[contains(@class,"pv-oc")]//section[contains(@class,"education-section")]/ul[contains(@class,"section-info")]/li[contains(@class,"ember-view")]/div')
	if len(eledu)>0:
		counter1 = 0
		for k in range(0,len(eledu)):
			elinkedinid = ee[k].attrib['id']
			if "ember" in elinkedinid:
				elinkedinid = ee2[counter1].attrib['id']
				counter1 = counter1 + 1
			print elinkedinid
			schoolid = elink[k].attrib['href'].rstrip('/').lstrip('/school/')
			timenow = time.strftime('%Y-%m-%d-%H:%M:%S',time.localtime(time.time()))

			sql = "SELECT * FROM education WHERE school_id = '"+schoolid+"';"
			bb = cur.execute(sql)
			if bb==0:
				schoolurl = "http://www.linkedin.com"+elink[k].attrib['href']
				sql = "INSERT INTO education (school_id,school_name,linkedin_url,created_at,updated_at) VALUES ('"+schoolid+"','"+eschool[k].text.replace("\'","\\\'")+"','"+schoolurl+"','"+timenow+"','"+timenow+"');"
				cur.execute(sql)
				conn.commit()
			sql = "SELECT id FROM user_in_schools WHERE (user_id = '"+info[i][1]+"') & (school_id = '"+schoolid+"') & (start_date = '"+estart[k].text+"') & (end_date = '"+eend[k].text+"');"			
			cc = cur.execute(sql)
			if cc==0:
				sql = "INSERT INTO user_in_schools (user_id,school_id,start_date,end_date,degree,fields,created_at,updated_at) VALUES ('"+info[i][1]+"','"+schoolid+"','"+estart[k].text+"','"+eend[k].text+"','"+edegree[k].text.replace("\'","\\\'")+"','"+efield[k].text.replace("\'","\\\'")+"','"+timenow+"','"+timenow+"');"
				
				
				print sql
				

				cur.execute(sql)
				conn.commit()
			else:
				eid = cur.fetchmany(cc)
				sql = "UPDATE user_in_schools SET degree='"+edegree[k].text.replace("\'","\\\'")+"',fields='"+efield[k].text.replace("\'","\\\'")+"',updated_at='"+timenow+"' WHERE id="+str(eid[0][0])+";"
				cur.execute(sql)
				conn.commit()
