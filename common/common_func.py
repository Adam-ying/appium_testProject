from baseView.baseView import BasicView
from common.desired_cap import appium_desired
from selenium.common.exceptions import NoSuchElementException
import logging, time, os
from selenium.webdriver.common.by import By
import csv

class Common(BasicView):
    infobutton = (By.ID, 'com.tal.kaoyan:id/tip_commit')
    permissionbutton = (By.ID, 'com.android.packageinstaller:id/permission_deny_button')
    skipbutton = (By.ID, 'com.tal.kaoyan:id/tv_skip')

    def check_info(self):
        logging.info('================= xieyi button==================')
        try:
            info = self.driver.find_element(*self.infobutton)
        except NoSuchElementException:
            logging.info("meiyouxieyixinyi")
        else:
            info.click()

    def check_perm(self):
        logging.info('================= perm button==================')
        try:
            info = self.driver.find_element(*self.permissionbutton)
        except NoSuchElementException:
            logging.info("shifouxuyaogeiyuquanxian")
        else:
            info.click()

    def check_skip(self):
        logging.info('================= skip button==================')
        try:
            info = self.driver.find_element(*self.skipbutton)
        except NoSuchElementException:
            logging.info("meiyoukaichangshipin")
        else:
            info.click()

    def get_size(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return x, y

    def swipeDown(self):
        logging.info('=======swipeDown=======')
        l = self.get_size()
        x1 = int(l[0] * 0.5)
        y1 = int(l[1] * 0.2)
        y2 = int(l[1] * 0.8)
        self.swipe(x1, y2, x1, y1, 1000)

    def getTime(self):
        self.now = time.strftime("%Y-%m-%d %H-%M-%S")
        return self.now

    def getScreenShot(self, module):
        time = self.getTime()
        image_file = os.path.dirname(os.path.dirname(__file__)) + '/screenshots/%s %s.png'%(module, time)
        print(image_file)
        logging.info('get %s screenshot', module)
        self.driver.get_screenshot_as_file(image_file)

    def get_csv_data(self, csv_file, line):
        logging.info('============get csv data=============')
        with open(csv_file, 'r', encoding='utf-8-sig') as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader, 1):
                if line == i:
                    return row

if __name__ == '__main__':
    driver = appium_desired()
    com = Common(driver)
    # com.check_info()
    # driver.implicitly_wait(3)
    # com.check_perm()
    # driver.implicitly_wait(3)
    # com.check_skip()
    # com.swipeDown()
    com.getScreenShot('start_app')

