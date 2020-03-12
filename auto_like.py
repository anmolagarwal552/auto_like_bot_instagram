from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()

def login(usr,pss):
    driver.get("https://www.instagram.com/")
    time.sleep(2)

    usr_ent = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input")
    usr_ent.clear()
    usr_ent.send_keys(usr)
    time.sleep(2)

    pss_ent = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input")
    pss_ent.clear()
    pss_ent.send_keys(pss)
    pss_ent.send_keys(Keys.ENTER)
    time.sleep(5)

def like(hashtag):
    driver.get(f"https://www.instagram.com/explore/tags/{hashtag}/")
    time.sleep(5)

    for i in range(7):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    href_found = driver.find_elements_by_tag_name("a")

    pic_href = [ele.get_attribute('href') for ele in href_found if '.com/p' in ele.get_attribute('href')]

    for ele in pic_href:
        driver.get(ele)
        time.sleep(3)

        like = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div[2]/section[1]/span[1]/button")
        like.click()
        time.sleep(5)




login("") #add the credentials here as login(username,password)
like('hacking')


