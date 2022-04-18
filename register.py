import selenium
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

import time,sys

try:
    print(sys.argv)
    email = sys.argv[1]
    pword = str(sys.argv[2])
except:
    print("please privide a email and password to register")
    quit()

link = "https://ddm-chat.herokuapp.com/"

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

driver.get(link)
register = driver.find_element_by_tag_name("a[href='/register']")

register.click()

username = driver.find_element_by_tag_name("input[name='username']")

username.click()

username.send_keys(email)

password = driver.find_element_by_tag_name("input[name='password']")

password.click()

password.send_keys(pword)

submitbutton = driver.find_element_by_tag_name("button[class='btn btn-dark']")

submitbutton.click()

print("Go to the email and click the link")
