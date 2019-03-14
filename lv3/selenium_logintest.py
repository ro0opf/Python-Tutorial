from selenium import webdriver
from bs4 import BeautifulSoup as bs

LOGIN_INFO = {
    'login_user_id': 'id',
    'login_password': 'pass'
}

if __name__ == "__main__":
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    driver = webdriver.Chrome('./chromedriver', options= options)
    driver.implicitly_wait(3)

    driver.get('https://www.acmicpc.net/login?next=%2F')
    driver.find_element_by_name('login_user_id').send_keys(LOGIN_INFO['login_user_id'])
    driver.find_element_by_name('login_password').send_keys(LOGIN_INFO['login_user_password'])
    
    driver.find_element_by_class_name('btn-u').click()
    driver.implicitly_wait(2)
    
    while(1):
        driver.get('https://www.acmicpc.net/submit/10945/12169127')
        driver.find_element_by_id('submit_button').click()
        driver.implicitly_wait(70)


    