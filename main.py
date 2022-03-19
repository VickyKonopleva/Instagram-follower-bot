from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os


CHROME_DRIVER_PATH = "C:/Users/v_kon/PycharmProjects/chromedriver"
ACCOUNT=os.environ['ACC']
PASSWORD=os.environ['PASS']

class InstagramFollowerBot():

    def __init__(self, PATH):
        self.driver = webdriver.Chrome(executable_path=PATH)

    def login(self, account_name, password):
        self.driver.get("https://www.instagram.com/accounts/login/?next=/englishyopta/followers/")
        time.sleep(5)
        entry_account_name=self.driver.find_element(By.XPATH,"/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[1]/div/label/input")
        time.sleep(5)
        entry_password=self.driver.find_element(By.XPATH,"/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[2]/div/label/input")
        time.sleep(5)
        entry_account_name.send_keys(account_name)
        entry_password.send_keys(password)
        login_button=self.driver.find_element(By.XPATH,"/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[3]")
        login_button.click()
        time.sleep(5)
        popup_button=self.driver.find_element(By.XPATH,"/html/body/div[1]/section/main/div/div/div/div/button")
        popup_button.click()
        time.sleep(5)


    def find_accounts_to_follow(self):
        followers_button = self.driver.find_element(By.XPATH,
                                                    "/html/body/div[1]/section/main/div/header/section/ul/li[2]/a")
        followers_button.click()
        time.sleep(5)
        #scrolling all the accounts
        self.pop_up_window=self.driver.find_element(By.XPATH,"/html/body/div[6]/div/div/div[2]")
        time.sleep(3)
        while True:
            self.follow()

    def follow(self):
        accounts_to_follow = self.driver.find_elements(By.CSS_SELECTOR, ".y3zKF")
        time.sleep(3)
        for person in accounts_to_follow:
            try:
                person.click()
                time.sleep(5)
            except ElementClickInterceptedException:
                cancel_button=self.driver.find_element(By.XPATH,"/html/body/div[7]/div/div/div/div[3]/button[2]")
                cancel_button.click()
        self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", self.pop_up_window)
        time.sleep(3)


Bot=InstagramFollowerBot(CHROME_DRIVER_PATH)
Bot.login(ACCOUNT, PASSWORD)
Bot.find_accounts_to_follow()




