from flask import Flask, jsonify, make_response, abort, Response, request
from flask_restful import Api, Resource, reqparse
from flask_httpauth import HTTPBasicAuth
from flask_jwt import jwt_required ,JWT
from werkzeug.security import safe_str_cmp

app = Flask(__name__)
api = Api(app=app)
auth = HTTPBasicAuth()


# 认证通过
@auth.get_password
def get_password(username):
    if username == "Admin":
        return "admin"


# 认证不通过的错误信息
@auth.error_handler
def authrized():
    return make_response(jsonify({'msg': '您好，请认证'}), 401)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"error": "请求页面不存在！"}), 404)


@app.errorhandler(405)
def not_found(error):
    return make_response(jsonify({"error": "请求方式不对！"}), 405)


books = [
    {'ID': 1, 'author': 'Teacher', 'name': 'Python', 'done': True},
    {'ID': 2, 'author': 'Teacher', 'name': 'Selenium', 'done': True},
    {'ID': 3, 'author': 'Teacher', 'name': 'Appium', 'done': False},
]


class Books(Resource):
    # 鉴权认证（登录）
    decorators = [auth.login_required]

    # 查看全部书籍
    def get(self):
        return jsonify({'data': books})

    # 添加部分书籍
    def post(self):
        if not Response.json:
            abort(404)
        else:
            book = {
                'ID': books[-1]['ID'] + 1,
                'author': request.json.get('author'),
                'name': request.json.get('name'),
                'done': False
            }
            books.append(book)
            return jsonify({'status': 1001, 'msg': '添加书籍成功', 'data': book})


class Book(Resource):
    # 鉴权认证（登录）
    decorators = [auth.login_required]

    # 根据ID查询对应书籍
    def get(self, book_id):
        book = list(filter(lambda t: t['ID'] == book_id, books))
        if len(book) == 0:
            abort(404)

        else:
            return jsonify({'status': 1002, 'msg': 'ok', 'data': book})

    # 根据ID删除对应书籍
    def delete(self, book_id):
        book = list(filter(lambda t: t['ID'] == book_id, books))
        if len(book) == 0:
            abort(404)
        else:
            books.remove(book[0])
            return jsonify({'status': 1003, 'msg': '删除书籍成功', 'data': book})

    # 根据ID更新对应书籍
    def put(self, book_id):
        book = list(filter(lambda t: t['ID'] == book_id, books))
        if len(book) == 0:
            abort(404)

        elif not Response.json:
            abort(404)

        elif 'author' not in request.json and 'name' not in request.json:
            abort(404)

        elif 'done' not in request.json and type(request.json['done'] is not bool):
            abort(404)

        else:
            book[-1]['author'] = request.json.get('author', book[-1]['author'])
            book[-1]['name'] = request.json.get('name', book[-1]['name'])
            book[-1]['done'] = request.json.get('done', book[-1]['done'])
            return jsonify({'status': 1004, 'msg': '更新书籍成功', 'data': book})


api.add_resource(Books, '/v1/api/books')
api.add_resource(Book, '/v1/api/book/<int:book_id>')

if __name__ == "__main__":
    app.run(debug=True,port=5555)