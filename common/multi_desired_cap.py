import multiprocessing
from appium import webdriver
import yaml
from time import ctime


class MultiDevicesSync:

    def __init__(self):
        self.desired_process = []

    def multi_devices_sync(self, udid, port):
        with open(r"E:\study\Fork\WeiboDemo\Weibo\config\desired_caps.yaml", 'r') as file:
            data = yaml.load(file, Loader=yaml.FullLoader)

        desired_caps = {
            'platformName': data['platformName'],
            'platformVersion': data['platformVersion'],
            'deviceName': data['deviceName'],
            'udid': udid,
            'appPackage': data['appPackage'],
            'appActivity': data['appActivity'],
            'automationName': data['automationName'],
            'autoGrantPermissions': data['autoGrantPermissions'],
            'noReset': data['noReset']
        }

        print('appium port:%s start run %s at %s' % (port, udid, ctime()))

        driver = webdriver.Remote('http://' + str(data['url']) + ':' + str(port) + '/wd/hub', desired_caps)
        driver.implicitly_wait(3)
        return driver




if __name__ == '__main__':
    pass