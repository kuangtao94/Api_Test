from flask import  Flask,jsonify
from flask_restful import  Api,Resource,reqparse


app=Flask(__name__)
api=Api(app)

class LoginView(Resource):
   def get(self):
      return {'status':0,'msg':'ok','data':'this is a login page','content':[{'id':123,'name':'Tao'},{'id':122,'name':'AAAA'}]}

   def post(self):
      parser=reqparse.RequestParser()
      parser.add_argument('username', type=str, required=True, help='您的用户名验证错误')
      parser.add_argument('password',type=str,required=True,help='账户密码不能为空')
      parser.add_argument('age',type=int,help='年龄必须为正正数')
      parser.add_argument('sex',type=str,help='性别只能是男或者女',choices=['女','男'])
      args=parser.parse_args()
      return jsonify(args)


api.add_resource(LoginView,'/login',endpoint='login')

if __name__ == '__main__':
   app.run(debug=True)