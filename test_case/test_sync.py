import multiprocessing
import pytest
from test_case.test_login import TestLogin
from common.multi_desired_cap import MultiDevicesSync

class TestSync:
    def run_tests(self, udid, port):
        mds = MultiDevicesSync()
        driver = mds.multi_devices_sync(udid, port)
        # ʵ������Ӧ�豸�� Page Object �࣬��������Ӧ�Ĳ��Է���
        page = TestLogin(driver)  # ������Ҫ�滻Ϊ���Լ��� Page Object ��
        page.test_login1()# ������Ҫ������Ĳ��Է���
        page.test_login2()
        page.test_final()

    @pytest.mark.parametrize('devices_list', [(['U4AIUKFAL7W4MJLR', 'U4AIUKFAL7W4MHUHUDS'])])
    def test_start_multi_device(self, devices_list):
        self.desired_process = []
        for i in range(len(devices_list)):
            port = 4723 + 2 * i
            desired = multiprocessing.Process(target=self.run_tests, args=(devices_list[i], port))
            self.desired_process.append(desired)

        # �������豸ִ�в���
        for desired in self.desired_process:
            desired.start()

        # �ȴ����н��̽�����ر�
        for desired in self.desired_process:
            desired.join()