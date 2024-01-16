from selenium import webdriver
import time 

web = webdriver.Chrome()
web.get('https://forms.gle/jMeyLsYmVT81XLZPA')
time.sleep(5)

sname = "Badhusha"
name = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
name.send_keys(sname)

ple = 'changanacherry'
place = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
place.send_keys(ple)

pnum = "+919946971423"
phone = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div[2]/textarea')
phone.send_keys(pnum)

but = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div[1]/div/span/div/div[1]/label/div/div[2]/div/span')
but.click()

dob = 26-12-2003
date = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input')
date.send_keys(dob)

time.sleep(5)

mit = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
mit.click()