from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


def run_webdriver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach', True)
    options.add_argument('--start-maximized')
    driver = webdriver.Chrome(options=options)
    chains = ActionChains(driver)

    driver.get('https://www.thsrc.com.tw/')
    search = driver.find_element(By.XPATH, '/html/body/div[5]/div/div[3]/button[2]')
    chains.click(search).perform()

    search01 = driver.find_element(By.ID, 'select_location01')
    Select(search01).select_by_visible_text('台北')
    search02 = driver.find_element(By.ID, 'select_location02')
    Select(search02).select_by_visible_text('新竹')

    result = driver.find_element(By.XPATH,
                                 '/html[1]/body[1]/div[4]/div[2]/div[1]/section[1]/div[1]/div[3]/div[1]/div[1]/div[5]/button[1]')
    chains.click(result).perform()

    driver.implicitly_wait(5)

    time = driver.find_element(By.XPATH,
                               '/html[1]/body[1]/div[4]/div[2]/section[4]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/a[1]/div[1]/span[1]')
    print(time.text)


if __name__ == '__main__':
    run_webdriver()


