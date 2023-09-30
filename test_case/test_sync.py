import multiprocessing
import pytest
from test_case.test_login import TestLogin
from common.multi_desired_cap import MultiDevicesSync

class TestSync:
    def run_tests(self, udid, port):
        mds = MultiDevicesSync()
        driver = mds.multi_devices_sync(udid, port)
        # 实例化对应设备的 Page Object 类，并调用相应的测试方法
        page = TestLogin(driver)  # 根据需要替换为你自己的 Page Object 类
        page.test_login1()# 根据需要调用你的测试方法
        page.test_login2()
        page.test_final()

    @pytest.mark.parametrize('devices_list', [(['U4AIUKFAL7W4MJLR', 'U4AIUKFAL7W4MHUHUDS'])])
    def test_start_multi_device(self, devices_list):
        self.desired_process = []
        for i in range(len(devices_list)):
            port = 4723 + 2 * i
            desired = multiprocessing.Process(target=self.run_tests, args=(devices_list[i], port))
            self.desired_process.append(desired)

        # 启动多设备执行测试
        for desired in self.desired_process:
            desired.start()

        # 等待所有进程结束后关闭
        for desired in self.desired_process:
            desired.join()