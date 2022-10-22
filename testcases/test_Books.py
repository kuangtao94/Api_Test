import pytest
import json
from base.method import Requests
from common.OperaExcel import OperationExcel
from common.helper import *
from requests.auth import HTTPBasicAuth



class TestBooks:
    excel = OperationExcel()
    obj = Requests()
    auth = HTTPBasicAuth('Admin','admin')

    def test_book_001(self):
        """查询所有书籍信息"""
        r = self.obj.get(url=self.excel.readUrl(1),auth=self.auth)
        assert self.excel.readExpect(1) in json.dumps(r.json()['data'][0]['author'])
        assert r.status_code == 200
        log("查询所有书籍成功")

    def test_book_002(self):
        """添加书籍请求"""
        r = self.obj.post(
            url=self.excel.readUrl(2),
            json=self.excel.readJsonValues(2),
            auth=self.auth
        )
        writeBookID(r.json()['data']['ID'])
        assert self.excel.readExpect(2) in json.dumps(r.json()['msg'],ensure_ascii=False)
        assert r.status_code == 200
        log("添加书籍成功")

    def test_book_003(self):
        """查看已添加的书籍"""
        r = self.obj.get(
            url=self.excel.readUrl(3),
            auth=self.auth
        )
        assert self.excel.readExpect(3) == float(r.json()["status"])
        assert r.status_code == 200
        log("查看已添加书籍成功")


    def test_book_004(self):
        """更新/修改已添加的书籍"""
        r = self.obj.put(
            url=self.excel.readUrl(4),
            json=self.excel.readJsonValues(4),
            auth=self.auth
        )
        assert self.excel.readExpect(4) in json.dumps(r.json()['msg'],ensure_ascii=False)
        assert r.status_code == 200
        log("更新/修改已添加的书籍成功")

    def test_book_005(self):
        """删除已编辑的书籍"""
        r = self.obj.delete(
            url=self.excel.readUrl(5),
            auth=self.auth
        )
        assert self.excel.readExpect(5) in json.dumps(r.json()['msg'], ensure_ascii=False)
        assert r.status_code == 200
        log("删除已编辑的书籍成功")

if __name__ == '__main__':
    pytest.main(["-s","-v","test_Books.py","--alluredir","./report/result"])
    import subprocess
    subprocess.call('allure generate report/result/ -o report/html --clean',shell=True)
    subprocess.call('allure open -h 127.0.0.1 -p  8088 ./report/html',shell=True)

