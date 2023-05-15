from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import random as rand

class GetLinkedInProfileLink():

    def __init__(self):
        self.SEARCH_QUERY = "{} {} {} site:linkedin.com"
        self.GOOGLE_SEARCH = "https://www.google.com/search?q={}"

    def random_sleep(self):
        time.sleep(rand.randint(1, 5))

    def get_linkedin_profile(self, first_name, last_name, company):
        # specifies the path to the chromedriver.exe
        chrome_options = Options()
        chrome_options.headless = True

        driver = webdriver.Chrome(options=chrome_options, service=Service(ChromeDriverManager().install()))
        self.random_sleep()

        # SEARCH FOR THE QUERY ON GOOGLE
        search_query = self.SEARCH_QUERY.format(first_name, last_name, company)
        driver.get(self.GOOGLE_SEARCH.format(search_query))

        self.random_sleep()
        search_results = driver.find_elements(By.CSS_SELECTOR, "div.g")
        linkedin_url = None
        self.random_sleep()

        # GET LINKED PROFILE
        for result in search_results:
            url = result.find_element(By.TAG_NAME, "a").get_attribute("href")
            if "linkedin.com/in/" in url:
                linkedin_url = url
                break
        driver.close()
        return linkedin_url
