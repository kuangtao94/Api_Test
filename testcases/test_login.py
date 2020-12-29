import  pytest
import json
from TestCase.ApiLogin_Po.common.OperaYaml import OperaYaml
from TestCase.ApiLogin_Po.base.method import Requests

obj = Requests()
OperaYa = OperaYaml()

#pytest参数化
# @pytest.mark.parametrize('datas',OperaYa.readYaml())
@pytest.mark.parametrize('datas1',
[
    {'url': 'http://127.0.0.1:5000/login', 'method': 'post', 'data': {'username': 'Admin', 'password': 'Admin', 'age': 22, 'sex': '男'}, 'except': {'username': 'Admin', 'password': 'Admin', 'age': 22, 'sex': '男'}},
    {'url': 'http://127.0.0.1:5000/login', 'method': 'post', 'data': {'password': 'Admin', 'age': 22, 'sex': '男'}, 'except': {'message': {'username': '您的用户名验证错误'}}},
    {'url': 'http://127.0.0.1:5000/login', 'method': 'post', 'data': {'username': 'Admin', 'age': 22, 'sex': '男'}, 'except': {'message': {'password': '账户密码不能为空'}}},
    {'url': 'http://127.0.0.1:5000/login', 'method': 'post', 'data': {'username': 'Admin', 'password': 'Admin', 'age': 'nan', 'sex': '男'}, 'except': {'message': {'age': '年龄必须为正正数'}}},
    {'url': 'http://127.0.0.1:5000/login', 'method': 'post', 'data': {'username': 'Admin', 'password': 'Admin', 'age': 22.8, 'sex': '第三方'}, 'except': {'message': {'sex': '性别只能是男或者女'}}}
],ids=['case1','case2','case3','case4','case5']


)

# def test_login_01(datas):
#     r = obj.post(
#         url=datas['url'],
#         json=datas['data']
#     )
#     # print(type(json.dumps(r.json())))
#     # print(json.dumps(r.json(),ensure_ascii=False))
#     assert datas['except'] == json.loads(json.dumps(r.json(),ensure_ascii=False))

def test_login_02(datas1):
    r = obj.post(
    url=datas1['url'],
    json=datas1['data']
)
    assert datas1['except'] == json.loads(json.dumps(r.json(),ensure_ascii=False))

if __name__ == '__main__':
    pytest.main(['-s','-v','test_login.py'])