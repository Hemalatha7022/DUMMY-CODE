from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://frontend-service-bjc4nbo65a-uc.a.run.app/")
driver.maximize_window()
driver.implicitly_wait(20)
driver.find_element("id","username").send_keys("cemsadmin@delfers.com")
driver.find_element("id","password").send_keys("1234")
driver.find_element("xpath","//button[@type='submit']").click()
ele=driver.find_element("xpath","//span[.='Event Log']")
a=ActionChains(driver)
a.move_to_element(ele).perform()
driver.find_element("xpath","//span[.='Medical Kit']").click()
ele1 = driver.find_element("xpath", "//h5[.='Search By Symptoms']")
driver.execute_script("arguments[0].scrollIntoView();", ele1)
driver.find_element("xpath","//div[.='Headache']").click()
ele2=driver.find_element("xpath","//a[.='Airline']")
driver.execute_script("arguments[0].scrollIntoView();", ele2)
driver.find_element("xpath","(//input[@type='checkbox'])[1]").click()




