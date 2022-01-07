from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from convert_date import Text_convert
import os
import pandas as pd
from __pycache__ import extra_byte


class Zoom_link:
    df = pd.DataFrame(columns = ['title','due','notes'])
    def __init__(self):
        self.text_convert = Text_convert()
        if "GOOGLE_CHROME_BIN" in os.environ:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument("--no-sandbox")
            self.driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
        else:
            options = webdriver.ChromeOptions()
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            #create webdriver
            self.driver = webdriver.Chrome(ChromeDriverManager().install())
        #create action chain (to run chain of actions like move to element and click)
        self.actions = ActionChains(self.driver)

    def go_to_homeworks(self):
        self.driver.get("https://www.mycourseville.com/api/login")
        Username = self.driver.find_element_by_id("username")
        #make selenium to type username field
        Username.send_keys(extra_byte.username)
        password = self.driver.find_element_by_id("password")
        #make selenium to type password field
        password.send_keys(extra_byte.password)
        #click on submit
        submit = self.driver.find_element_by_id("cv-login-cvecologinbutton")
        submit.click()
        #click on cud+
        cudplus = self.driver.find_elements_by_class_name("cv-userhome-apptitle")
        cudplus[1].click()
        #click on courses
        courses = self.driver.find_elements_by_xpath('//a[contains(@href,"/lms/homeworkbook")]')
        courses[1].click()
        sleep(3)
        return self.get_all_homeworks()

    def get_all_homeworks(self):
        links = self.get_link_to_click()
        print(links)
        for i,link in enumerate(links):
            link.click()
            sleep(5)
            p = self.driver.current_window_handle
            #get first child window
            chwd = self.driver.window_handles
            for w in chwd:
            #switch focus to child window
                if(w!=p):
                    self.driver.switch_to.window(w)
            notes = self.driver.find_elements_by_tag_name("div")[48].text
            due = self.driver.find_elements_by_tag_name("div")[44].text
            title = self.driver.find_element_by_tag_name("h2").text
            self.df.loc[i] = [title, self.text_convert.convert_to_dt(self.text_convert.convert_to_date(due)), notes]
            self.driver.close()
            self.driver.switch_to.window(p)
            sleep(1)
            
        self.driver.quit()
        return self.df

    def get_link_to_click(self):
        return self.driver.find_elements_by_tag_name('a')[23:]
    




