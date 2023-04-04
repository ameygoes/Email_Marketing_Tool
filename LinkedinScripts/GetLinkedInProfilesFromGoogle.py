from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import random as rand
# Set up Chrome options to run headless
chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')

class GetLinkedinProfileLink():

    def __init__(self):
        self.SEARCH_QUERY = "{} {} {} site:linkedin.com"
        self.GOOGLE_SEARCH = "https://www.google.com/search?q={}"

    def randomSleep(self):
        time.sleep(rand.randint(1,5))

    def getLinkedInProfile(self, firstName, lastName, company):
        # specifies the path to the chromedriver.exe
        driver = webdriver.Chrome(options=chrome_options, service=Service(ChromeDriverManager().install()))
        self.randomSleep()
        # SEARCH FOR THE QUERY ON GOOGLE
        search_query = self.SEARCH_QUERY.format(firstName, lastName, company)
        driver.get(self.GOOGLE_SEARCH.format(search_query))

        self.randomSleep()
        search_results = driver.find_elements(By.CSS_SELECTOR, "div.g")
        linkedin_url = None
        self.randomSleep()
        # GET LINKED PROFILE
        for result in search_results:
            url = result.find_element(By.TAG_NAME, "a").get_attribute("href")
            if "linkedin.com/in/" in url:
                linkedin_url = url
                break
        driver.close()
        return linkedin_url