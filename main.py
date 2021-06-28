from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

ACCOUNT_MAIL = "nadiraziziyah@gmail.com"
ACCOUNT_PASSWORD = ""
PHONE = "+91 9995957505"

PROMISED_UP = 60
PROMISED_DOWN = 10


NETWORK_SPEED_URL = "https://www.speedtest.net/"
TWITTER_URL = "https://twitter.com/"

CHROMEDRIVER_PATH = "C:\Development\chromedriver.exe"


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(CHROMEDRIVER_PATH)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get(NETWORK_SPEED_URL)
        time.sleep(3)
        start = self.driver.find_element_by_class_name("start-text")
        start.click()
        time.sleep(40)
        self.down = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.up = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text
        print(self.down)
        print(self.up)

    def tweet_at_provider(self):
        self.driver.get(TWITTER_URL)
        login_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/a[2]')
        login_button.click()
        time.sleep(3)
        username_input = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
        username_input.send_keys(ACCOUNT_MAIL)

        pass_input = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
        pass_input.send_keys(ACCOUNT_PASSWORD)
        pass_input.send_keys(Keys.ENTER)

        time.sleep(5)
        blog_input = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
        blog_input.send_keys(f'Network speed [ Download speed = {self.down}, Upload speed = {self.up} ] ')

        time.sleep(3)
        tweet_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]')
        tweet_button.click()

check = InternetSpeedTwitterBot()
check.get_internet_speed()
time.sleep(3)
check.tweet_at_provider()