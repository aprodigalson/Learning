import json
import os
from ocr import OCRNeuralNetwork
from http.server import HTTPServer, BaseHTTPRequestHandler

'''
linked : https://github.com/HT524/500LineorLess_CN/blob/master/%E5%85%89%E5%AD%A6%E6%96%87%E5%AD%97%E8%AF%86%E5%88%AB%20Optical%20Character%20Recognition%20(OCR)%2F%E5%85%89%E5%AD%A6%E6%96%87%E5%AD%97%E8%AF%86%E5%88%AB.md
'''

nn = OCRNeuralNetwork(False)


class MyServer(BaseHTTPRequestHandler):
    Error_Page = '''
         <html>
            <body>
            <h1>Error accessing {path}</h1>
            <p>{msg}</p>
            </body>
            </html>
        '''
    def do_GET(self):
        self.get_static_page()

    def get_static_page(self):
        try:
            self.full_path = os.getcwd() + self.path
            print(self.full_path)
            self.handle_file(self.full_path)

        except Exception as msg:
            self.handle_error(msg)

    def handle_file(self,full_path):
        try:
            with open(full_path, 'r') as reader:
                content = reader.read()
            self.send_content(content)
        except IOError as msg:
            msg = "'{0}' cannot be read: {1}".format(full_path, msg)
            self.handle_error(msg)

    def send_content(self, content, status=200):
        self.send_response(status)
        self.send_header('Content-Type', "text/html")
        self.send_header('Content-Length', str(len(content)))
        self.end_headers()
        try:
            print(type(content))

            self.wfile.write(bytes(content, encoding='utf-8'))
        except Exception:
            print('coding problem')
            self.handle_error("coding problem")

    def handle_error(self, msg):
        content = self.Error_Page.format(path=self.path, msg=msg)
        self.send_content(content, 404)


    def do_POST(self):
        response_code = 200
        response = ""
        var_len = int(self.headers.get('Content-Length'))
        content = self.rfile.read(var_len)
        payload = json.loads(content)
        if payload.get('train'):
            nn.train(payload['trainArray'])
            nn.save()
        elif payload.get('predict'):
            try:
                response = {
                    "type": "test",
                    "result": nn.predict(str(payload['image']))
                }
            except:
                response_code = 500
        else:
            response_code = 400
        self.send_response(response_code)
        self.send_header("Content-type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        if response:
            self.wfile.write(json.dumps(response))
        return


if __name__ == '__main__':
    serverAddress = ('', 8081)
    server = HTTPServer(serverAddress, MyServer)
    server.serve_forever()
