import pytest,allure,json
from base.method import Requests
from common.OperaExcel import OperationExcel
from common.helper import *
from requests.auth import HTTPBasicAuth


@allure.feature('测试图书管理系统')
class TestBooks:
    excel = OperationExcel()
    obj = Requests()
    auth = HTTPBasicAuth('Admin','admin')

    @allure.step("查询所有书籍信息")
    def test_book_001(self):
        """查询所有书籍信息"""
        r = self.obj.get(url=self.excel.readUrl(1),auth=self.auth)
        try:
            assert self.excel.readExpect(1) in json.dumps(r.json()['data'][0]['author'])
            assert r.status_code == 200
            TestReult = 'PASS'
            log("查询所有书籍成功")
        except AssertionError as e:
            print('执行接口测试出错,错误原因{0}'.format(e))
            TestReult = 'Fail'
            raise e
        finally:
            # 测试用例执行结果
            self.excel.write_data(1,6,TestReult)
            # 测试用例实际结果
            self.excel.write_data(1,7,str(r.json()))

    @allure.step("添加书籍请求")
    def test_book_002(self):
        """添加书籍请求"""
        r = self.obj.post(
            url=self.excel.readUrl(2),
            json=self.excel.readJsonValues(2),
            auth=self.auth
        )
        writeBookID(r.json()['data']['ID'])
        try:
            assert self.excel.readExpect(2) in json.dumps(r.json()['msg'],ensure_ascii=False)
            assert r.status_code == 200
            TestReult = 'PASS'
            log("添加书籍成功")
        except AssertionError as e:
            print('执行接口测试出错,错误原因{0}'.format(e))
            TestReult = 'Fail'
            raise e
        finally:
            # 测试用例执行结果
            self.excel.write_data(2,6,TestReult)
            # 测试用例实际结果
            self.excel.write_data(2,7,str(r.json()))

    @allure.step("查看已添加的书籍")
    def test_book_003(self):
        """查看已添加的书籍"""
        r = self.obj.get(
            url=self.excel.readUrl(3),
            auth=self.auth
        )
        try:
            assert self.excel.readExpect(3) == float(r.json()["status"])
            assert r.status_code == 200
            TestReult = 'PASS'
            log("查看已添加书籍成功")
        except AssertionError as e:
            print('执行接口测试出错,错误原因{0}'.format(e))
            TestReult = 'Fail'
            raise e
        finally:
            # 测试用例执行结果
            self.excel.write_data(3,6,TestReult)
            # 测试用例实际结果
            self.excel.write_data(3,7,str(r.json()))

    @allure.step("更新/修改已添加的书籍")
    def test_book_004(self):
        """更新/修改已添加的书籍"""
        r = self.obj.put(
            url=self.excel.readUrl(4),
            json=self.excel.readJsonValues(4),
            auth=self.auth
        )
        try:
            assert self.excel.readExpect(4) in json.dumps(r.json()['msg'],ensure_ascii=False)
            assert r.status_code == 200
            TestReult = 'PASS'
            log("更新/修改已添加的书籍成功")
        except AssertionError as e:
            print('执行接口测试出错,错误原因{0}'.format(e))
            TestReult = 'Fail'
            raise e
        finally:
            # 测试用例执行结果
            self.excel.write_data(4,6,TestReult)
            # 测试用例实际结果
            self.excel.write_data(4,7,str(r.json()))

    @allure.step("删除已编辑的书籍")
    def test_book_005(self):
        """删除已编辑的书籍"""
        r = self.obj.delete(
            url=self.excel.readUrl(5),
            auth=self.auth
        )
        try:
            assert self.excel.readExpect(5) in json.dumps(r.json()['msg'], ensure_ascii=False)
            assert r.status_code == 200
            TestReult = 'PASS'
            log("删除已编辑的书籍成功")
        except AssertionError as e:
            print('执行接口测试出错,错误原因{0}'.format(e))
            TestReult = 'Fail'
            raise e
        finally:
            # 测试用例执行结果
            self.excel.write_data(5,6,TestReult)
            # 测试用例实际结果
            self.excel.write_data(5,7,str(r.json()))

if __name__ == '__main__':
    pytest.main(["-s","-v","test_BooksByDict.py","--alluredir","../report/result"])
    # import subprocess
    # subprocess.call('allure generate ../repo.rt/result/ -o ../report/html --clean',shell=True)
    # #     # subprocess.call('allure open -h 127.0.01 -p  8081 ./report/html',shell=True)
    # subprocess.call('allure serve -p  8081 ../report/result',shell=True)
