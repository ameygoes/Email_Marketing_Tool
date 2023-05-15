from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# Set up the Selenium driver with Chrome browser
options = webdriver.ChromeOptions()
options.add_argument('--disable-notifications')
driver = webdriver.Chrome(options=options)
NUM_PAGES = 10
# Navigate to the LinkedIn home page and log in
driver.get('https://www.linkedin.com')
driver.find_element(By.NAME, 'session_key').send_keys('email')
time.sleep(1)
driver.find_element(By.NAME, 'session_password').send_keys('pass')
time.sleep(1)
driver.find_element(By.NAME, 'session_password').send_keys(Keys.RETURN)

# Navigate to the LinkedIn company search page
driver.get('https://www.linkedin.com/search/results/companies/?companyHqGeo=%5B%22103644278%22%5D&industryCompanyVertical=%5B%226%22%5D&origin=FACETED_SEARCH&sid=1DA')
time.sleep(2)
for i in range(1, NUM_PAGES):
    # find the "5" page number button in the page's footer
    time.sleep(5)
    btn_xpth = f"//button[@aria-label='Page {i}']"
    page_button = button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, btn_xpth)))
    # next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Next' and contains(@class, 'artdeco-pagination__button--next')]")))


    # # click the "5" button to go to the 5th page
    # elements = driver.find_elements(By.CLASS_NAME, 'app-aware-link')
    # for element in elements:
    #     href = element.get_attribute('href')
    #     driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    #     driver.implicitly_wait(3)
    #     if "www.linkedin.com/company/" in href:
    #         print(href)
    # time.sleep(5)

    # # Click on the "Next" button
    page_button.click()
    

time.sleep(10)
driver.close()
# # Filter the search results by location (USA) and industry (Technology)
# location_filter = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'location-facet-values')))
# location_filter.find_element_by_xpath("//button[contains(text(),'United States')]").click()

# industry_filter = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'industry-facet-values')))
# industry_filter.find_element_by_xpath("//button[contains(text(),'Technology')]").click()

# Scroll down to load more search results
# time.sleep(5)
# scroll_count = 0
# while scroll_count < 5:
#     driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
#     scroll_count += 1
#     driver.implicitly_wait(3)
#     time.sleep(2)

# # Extract the LinkedIn profiles of companies from the search results
# profiles = []
# for result in driver.find_elements(By.CSS_SELECTOR, 'li.search-result div.search-result__info'):
#     link = result.find_element(By.CSS_SELECTOR, 'a.search-result__result-link')
#     profiles.append(link.get_attribute('href'))
#     time.sleep(2)

# # Print the LinkedIn profiles of product-based companies in the USA
# print(profiles)

# # Close the Selenium driver and the browser window
# driver.quit()
