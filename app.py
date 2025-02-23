from flask import Flask, request, make_response
import hashlib
import os

app = Flask(__name__)

# 微信 Token
TOKEN = os.getenv('WECHAT_TOKEN', 'your_token')  # 从环境变量中读取 Token

@app.route('/wechat', methods=['GET', 'POST'])
def wechat():
    if request.method == 'GET':
        # 验证服务器
        signature = request.args.get('signature', '')
        timestamp = request.args.get('timestamp', '')
        nonce = request.args.get('nonce', '')
        echostr = request.args.get('echostr', '')

        tmp_list = [TOKEN, timestamp, nonce]
        tmp_list.sort()
        tmp_str = ''.join(tmp_list)
        tmp_str = hashlib.sha1(tmp_str.encode('utf-8')).hexdigest()

        if tmp_str == signature:
            return echostr
        else:
            return 'error'
    else:
        # 处理消息
        xml_data = request.data
        # 解析 XML 数据，获取用户消息
        # 调用 DeepSeek API 获取响应
        deepseek_response = call_deepseek_api(xml_data)
        # 返回响应给用户
        return make_response(deepseek_response)

def call_deepseek_api(user_message):
    # 调用 DeepSeek API 的逻辑
    # 返回 DeepSeek 的响应
    pass

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
