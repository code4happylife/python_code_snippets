import json
import socket
from concurrent.futures.thread import ThreadPoolExecutor


class Server:

    def __init__(self, ip='127.0.0.1', port=7788):
        # 创建tcp 套接字
        self.server_sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        # 绑定ip 和 端口
        self.server_sock.bind((ip, port))
        # 开启监听，设置最大的连接数
        self.server_sock.listen(100)
        # 访问路径和对应的处理函数的映射关系
        self.url_maps = {}

    def run(self):
        with ThreadPoolExecutor(max_workers=10) as tps:
            while True:
                # 等待客户端的连接
                cli, addr = self.server_sock.accept()
                tps.submit(self.handle_request, cli)
                # print(connect)
                # 接收客户端的请求数据，解析http 请求报文

    def recv_data(self, cli):
        data = b''
        while True:
            res = cli.recv(1024)
            if len(res) < 1024:
                data += res
                break
            else:
                data += res
        return data.decode()

    def parse_request(self, request_info):
        """
        解析请求报文
        :param request_info: 请求报文
        :return:
        {
            "path":"请求路径"，
            "method":请求方法，
            headers:请求头（字典）
            params: 请求参数（查询字符串）
            data:表单参数
            json:json参数
        }
        """
        request_info_list = request_info.split('\r\n')
        # print(request_info_list)
        # 获取请求方法
        method = request_info_list[0].split(' ')[0]
        # 获取请求路径
        path = request_info_list[0].split(' ')[1]
        # 获取请求头
        header_list = request_info.split('\r\n\r\n')[0].split('\r\n')[1:]
        headers = {i.split(':')[0]: i.split(':')[1].strip() for i in header_list}
        # 判断是否有查询字符串参数
        """
        GET /?key1=value1&key2=value2 HTTP/1.1
        Host: 127.0.0.1:9988
        User-Agent: python-requests/2.24.0
        Accept-Encoding: gzip, deflate
        Accept: */*
        Connection: keep-alive
        """

        if "?" in path:
            path, params_str = path.split('?')
            params_ = {i.split('=')[0]: i.split('=')[1] for i in params_str.split('&')}
            request_type = '请求中有查询字符串参数'
        else:
            params_ = {}
        json_params = {}
        form_data = {}

        # 判断是否有请求体
        if headers.get('Content-Type'):
            # 判断是否有json参数
            if headers.get('Content-Type') == 'application/json':
                request_body = request_info.split('\r\n\r\n')[1]
                json_params = json.loads(request_body)
            # 判断是否有表单参数
            elif headers.get('Content-Type') == 'application/x-www-form-urlencoded':
                request_body = request_info.split('\r\n\r\n')[1]
                form_data = {i.split('=')[0]: i.split('=')[1] for i in request_body.split('&')}

        # 判断是否有json参数
        """
        POST / HTTP/1.1
        Host: 127.0.0.1:9988
        User-Agent: python-requests/2.24.0
        Accept-Encoding: gzip, deflate
        Accept: */*
        Connection: keep-alive
        Content-Length: 36
        Content-Type: application/json
    
        {"key1": "value1", "key2": "value2"}
        """

        # 判断是否有表单参数
        """
        POST / HTTP/1.1
        Host: 127.0.0.1:9988
        User-Agent: python-requests/2.24.0
        Accept-Encoding: gzip, deflate
        Accept: */*
        Connection: keep-alive
        Content-Length: 23
        Content-Type: application/x-www-form-urlencoded
        """

        return {
            'path': path,
            'method': method,
            'headers': headers,
            'params': params_,
            'json': json_params,
            'form': form_data
        }

    def handle_request(self, cli):
        """
        处理客户端请求的方法
        :param cli:
        :return:
        """
        request_info = self.recv_data(cli)
        print(request_info)

        # 解析http请求报文
        request = self.parse_request(request_info)
        print()
        # 处理相关业务（后端开发）
        # 判断请求路径，调用对应的处理函数处理该请求
        run_func = self.url_maps.get(request['path'])
        if run_func:
            body = run_func()
        else:
            body = '404 你访问的路径不存在'

        header = 'HTTP/1.1 200 OK\r\n'
        header += 'Content-Type: text/html;charset=utf-8\r\n'
        header += '\r\n'
        # 将响应头和响应体进行拼接
        response = header + body
        # 转换为二进制返回
        cli.send(response.encode())
        cli.close()

    def route(self, path):
        def wrapper(func):
            # path: 访问的路径
            # func: 对应的处理函数
            self.url_maps[path] = func
            return func

        return wrapper


app = Server()


@app.route('/login')  # login = wrapper(login)
def login():
    return '登录页面'


@app.route('/user')
def usr():
    return '用户页面'


if __name__ == '__main__':
    app.run()
