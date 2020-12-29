import requests

class Requests:
    # def __init__(self):
    #     self.s = requests.Session()

    def request(self,url,method='get',**kwargs):
        if method == 'get':
            return requests.Session().request(url=url,method=method,**kwargs)
        elif method == 'post':
            return requests.Session().request(url=url,method=method,**kwargs)
        elif method == 'delete':
            return requests.Session().request(url=url,method=method,**kwargs)
        elif method == 'put':
            return requests.Session().request(url=url,method=method,**kwargs)

    def get(self,url,**kwargs):
        return self.request(url=url,**kwargs)

    def post(self,url,**kwargs):
        return self.request(url=url,method='post',**kwargs)

    def delete(self,url,**kwargs):
        return self.request(url=url,method='delete',**kwargs)

    def put(self,url,**kwargs):
        return self.request(url=url,method='put',**kwargs)