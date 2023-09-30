import logging
from businessView.loginView import LoginView
import pytest



class TestLogin:
    csv_file = '../data/login.csv'
    def __init__(self, driver=None):
        if driver:
            self.driver = driver

    def test_login1(self):
        driver = self.driver
        logging.info('test1')
        l = LoginView(driver)
        data = l.get_csv_data(self.csv_file, 1)
        l.login_action(data[0], data[1])
        final = l.check_login_status()
        assert final == True

    def test_login2(self):
        driver = self.driver
        logging.info('test2')
        l = LoginView(driver)
        data = l.get_csv_data(self.csv_file, 2)
        l.login_action(data[0], data[1])
        final = l.check_login_status()
        assert final == True

    def test_final(self):
        pass

if __name__ == '__main__':
    pytest.main()