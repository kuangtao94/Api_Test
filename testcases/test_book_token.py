import pytest,json
from common.OperaExcelOne import *
from base.method import Requests
from requests.auth import HTTPBasicAuth
from common.helper import *

obj = OperationExcel()
excel = ExcelValues()
obje = Requests()
auth = HTTPBasicAuth('Admin', 'admin')


@pytest.mark.parametrize("datas",obj.runs)

def test_books(datas):
    #对请求参数做反序列化的出处理
    params = datas[excel.Params]
    if len(str(params).strip()) == 0:
        pass
    elif len(str(params).strip()) >= 0:
        # str->dict，字符串的反序列化loads
        # print(json.loads(params))
        params = json.loads(params)

    # 对请求头做反序列化的出处理
    header = datas[excel.Headers]
    if len(str(header).strip()) == 0:
        pass
    elif len(str(header).strip()) >= 0:
        # str->dict，字符串的反序列化loads
        header = json.loads(header)
        # return json.loads(params)

    """
    1、找到所有前置条件关联的测试用例
    2、执行前置测试条件测试点
    3、获取结果信息token的值
    4、拿到返回的值替换对应测试点的变量
    """
    r = obje.post(
        url=obj.case_praams('login')[excel.CaseUrl],
        json=json.loads(obj.case_praams('login')[excel.Params])
    )
    preResult=r.json()["access_token"]

    #替换被关联测试点中请求头信息的变量
    header = obj.preHeaders(preResult)

    #协议码
    statusCode = int(datas[excel.StatusCode])

    def case_assert_result(r):
        #断言分离
        assert r.status_code == statusCode
        assert datas[excel.Expect] in json.dumps(r.json(),ensure_ascii=False)

    def GetUrl():
        """url路径封装"""
        return str(datas[excel.CaseUrl]).replace('{bookid}',readBookID())

    if datas[excel.Method] == 'get':
        if '/books' in datas[excel.CaseUrl]:
            r = obje.get(url=datas[excel.CaseUrl],headers=header)
            case_assert_result(r=r)
        else:
            r = obje.get(url=GetUrl(),headers=header)
            case_assert_result(r=r)

    elif datas[excel.Method] == 'post':
        r = obje.post(
            url=datas[excel.CaseUrl],
            json=params,headers=header)
        writeBookID(content=str(r.json()[0]['datas']['id']))
        case_assert_result(r=r)

    elif datas[excel.Method] == 'put':
        r = obje.put(url=GetUrl(),json=params,headers=header)
        case_assert_result(r=r)

    elif datas[excel.Method] == 'delete':
        r = obje.delete(url=GetUrl(),headers=header)
        case_assert_result(r=r)

if __name__ == '__main__':
    pytest.main(['-s','-v','test_book_token.py','--alluredir','./report/result'])
    import subprocess
    subprocess.call('allure generate report/result/ -o report/html --clean',shell=True)
    subprocess.call('allure open -h localhost -p 8880 ./report/html',shell=True)