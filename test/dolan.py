from _ast import Assert

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import Select
driver=webdriver.Chrome(executable_path="D:\drivers\chromedriver.exe")
driver.maximize_window()
driver.get("http://dolan-qa.pimcoreclients.com/admin/")
print(driver.title)
#Login screen
driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("password").send_keys("admin@123")
#New import product selection in slider menu
driver.find_element_by_xpath("//button[contains(text(),'Login')]").click()
driver.implicitly_wait(100)
driver.find_element_by_xpath("//body/div[@id='pimcore_sidebar']/div[@id='pimcore_navigation']/ul[1]/li[6]/img[1]").click()
driver.find_element_by_xpath("//span[@id='menuitem-1172-textEl']").click()
#Handle child window
handles = driver.window_handles
size = len(handles)
parent_handle = driver.current_window_handle
for x in range(size):
  if handles[x] != parent_handle:
    driver.switch_to.window(handles[x])
    break
#Vendor selection
driver.find_element_by_xpath("//input[@id='combo-1205-inputEl']").send_keys("George Kovacs Lighting")
driver.find_element_by_xpath("//input[@id='combo-1205-inputEl']").send_keys(Keys.ENTER)
#Upload product File
driver.find_element_by_id("fileuploadfield-1206-button-fileInputEl").send_keys("D://file.xlsx")
driver.find_element_by_xpath("//span[@id='button-1208-btnWrap']").click()
# alert object creation and switching focus to alert
#alert = driver.switch_to.alert()
#alert_text = alert.text
# validate the alert text
#alert.accept()
driver.switch_to.window(parent_handle)

