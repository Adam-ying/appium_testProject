from appium import webdriver
import os
import yaml
import logging
import logging.config

CON_LOG = 'D:\code\kyb_testProject\config\log.conf'
logging.config.fileConfig(CON_LOG)
logging = logging.getLogger()

def appium_desired():
    with open('D:\code\kyb_testProject\config\desired_cap.yaml', 'r', encoding='utf-8') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)

    base_dir = os.path.dirname(os.path.dirname(__file__))
    app_path = os.path.join(base_dir, 'app', 'kyb_ali213.apk')
    desired_cap = {
        'platformName': data['platformName'],
        'app': app_path,
        'deviceName': data['deviceName'],
        'platformVersion': data['platformVersion'],
        'appPackage': data['appPackage'],
        'automationName': data['automationName'],
        'appActivity': data['appActivity'],
        'noReset': data['noReset']
    }

    logging.info('===========start app===============')
    driver = webdriver.Remote(f"http://{str(data['ip'])}:{str(data['port'])}/wd/hub", desired_cap)
    driver.implicitly_wait(3)
    return driver

if __name__ == '__main__':
    appium_desired()