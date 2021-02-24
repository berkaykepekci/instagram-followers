from selenium import webdriver
import time





driver=webdriver.Firefox()
driver.get("https://www.instagram.com/accounts/login/")

time.sleep(2)

username=input("Username:")
password=input("Password:")

loginbutton=driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[3]/button/div")

username.send_keys("username")
password.send_keys("password")

loginbutton.click()

time.sleep(5)

button2=driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/section/div/button")
button2.click()

time.sleep(5)

button3=driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")
button3.click()

time.sleep(5)

button4=driver.find_element_by_xpath("/html/body/div[1]/section/main/section/div[3]/div[1]/div/div/div[2]/div[1]/div/div/a")
button4.click()

time.sleep(5)

folbutton=driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a")
folbutton.click()

time.sleep(5)


jscommand1="""
newf=document.querySelector(".isgrP");
newf.scrollTo(0,newf.scrollHeight);
var lenOfPage=newf.scrollHeight;
return lenOfPage;
"""

lenOfPage = driver.execute_script(jscommand1)
match=False
while(match==False):
    lastCount = lenOfPage
    time.sleep(3)
    lenOfPage = driver.execute_script(jscommand1)
    if lastCount == lenOfPage:
        match=True


followers=driver.find_elements_by_css_selector(".Jv7Aj.mArmR.MqpiF  ")

followerslist=[]

for i in followers:
    followerslist.append(i.text)



driver.back()

followingbutton=driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a")
followingbutton.click()

jscommand2="""
followings=document.querySelector(".isgrP")
followings.scrollTo(0,followings.scrollHeight)
var lenOfPage=followings.scrollHeight;
return lenOfPage;
"""
lenOfPage = driver.execute_script(jscommand2)
match=False
while(match==False):
    lastCount = lenOfPage
    time.sleep(3)
    lenOfPage = driver.execute_script(jscommand2)
    if lastCount == lenOfPage:
        match=True

followings=driver.find_elements_by_css_selector(".Jv7Aj.mArmR.MqpiF  ")

followinglist=[]

for i in followings:
    followinglist.append(i.text)


hayranlarin=[]
hayranolduklarin=[]

for i in followerslist:
    if i not in followinglist:
        hayranlarin.append(i)

for k in followinglist:
    if k not in followerslist:
        hayranolduklarin.append(k)


print("***************FUNS***************")
for j in hayranlarin:
    print(j)

print("**************THE ONES YOU FUN OF**************")
for g in hayranolduklarin:
    print(g)