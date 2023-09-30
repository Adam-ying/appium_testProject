import logging
import time

from common.desired_cap import appium_desired
from common.common_func import Common, NoSuchElementException
from selenium.webdriver.common.by import By



class LoginView(Common):
    passButton = (By.ID, 'com.tal.kaoyan:id/login_code_touname')
    usernameButton = (By.ID, 'com.tal.kaoyan:id/login_email_edittext')
    passwordButton = (By.ID, 'com.tal.kaoyan:id/login_password_edittext')
    dengluButton = (By.ID, 'com.tal.kaoyan:id/login_login_btn')
    tip_commit = (By.ID, 'com.tal.kaoyan:id/tip_commit')

    button_mysefl = (By.ID, 'com.tal.kaoyan:id/mainactivity_button_mysefl')
    statu_button = (By.ID, 'com.tal.kaoyan:id/activity_usercenter_username')

    setbutton = (By.ID, 'com.tal.kaoyan:id/usercenter_setting')
    logoutbutton = (By.ID, 'com.tal.kaoyan:id/setting_logout_text')


    def login_action(self, username, password):
        self.check_info()
        self.check_perm()
        self.check_skip()

        logging.info('================login==============')
        self.driver.find_element(*self.passButton).click()

        logging.info('input username %s' %username)
        self.driver.find_element(*self.usernameButton).send_keys(username)

        logging.info('input password %s' %password)
        self.driver.find_element(*self.passwordButton).send_keys(password)

        logging.info('click loginBtn')
        self.driver.find_element(*self.dengluButton).click()
        logging.info('login finished')

    def check_account_alert(self):
        logging.info('==============check account alert===============')
        try:
            element = self.driver.find_element(*self.tip_commit)
        except NoSuchElementException:
            pass
        else:
            logging.info('close tip commit')
            element.click()

    def check_login_status(self):
        logging.info('=================check_loginStatus=============')
        try:
            self.driver.find_element(*self.button_mysefl).click()
            self.driver.find_element(*self.statu_button)
        except NoSuchElementException:
            logging.error('login fail!')

            self.getScreenShot('login fail')
            return False
        else:
            logging.info('login success')
            self.logout_action()
            return True

    def logout_action(self):
        logging.info('===============logout action===============')
        self.driver.find_element(*self.setbutton).click()
        self.driver.find_element(*self.logoutbutton).click()
        self.driver.find_element(*self.tip_commit).click()



if __name__ == '__main__':
    driver = appium_desired()
    login = LoginView(driver)
    login.login_action('111', 'yingtao123')
    login.check_account_alert()
    login.check_login_status()