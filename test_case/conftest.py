from Utils.tools import del_path_files
from common.desired_cap import appium_desired
from common.common_func import Common
import pytest
import logging
import os


@pytest.fixture(scope="function", autouse=True)
def setup_teardown(request):
    logging.info('=========setUp==========')
    driver = appium_desired()
    request.cls.driver = driver

    yield

    logging.info('==============tearDown===========')
    driver.close_app()


@pytest.fixture(scope="class", autouse=True)
def generate_allure_report(request):
    del_path_files('D:\code\kyb_testProject\\temp')
    yield
    # 获取当前测试用例的节点对象
    node = request.node
    # 获取节点对象的完整路径
    node_path = node.nodeid
    # 提取出文件名部分
    file_name = os.path.basename(node_path).split(".py")[0] + Common.getTime()
    logging.info('allure generate D:\code\kyb_testProject\\temp -o D:\code\kyb_testProject\\reports\Report_%s --clean' % file_name )
    os.system('allure generate D:\code\kyb_testProject\\temp -o D:\code\kyb_testProject\\reports\Report_%s --clean' % file_name )