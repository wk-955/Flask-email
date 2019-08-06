from flask import Flask,render_template
from flask_mail import Mail,Message
import config
import os
path = os.path.dirname(__file__)
filename = os.path.join(path,'test.jpg')

mail = Mail()

app = Flask(__name__)
app.config.from_object(config)

mail.init_app(app)

#发送文本
@app.route('/email_send_charactor/')
def email_send_charactor():
    message = Message(subject='hello flask-mail',recipients=['2585765186@qq.com'],body='flask-mail测试代码')
    try:
        mail.send(message)
        return '发送成功，请注意查收~'
    except Exception as e:
        print(e)
        return '发送失败'


#发送一个html
@app.route('/email_send_html/')
def email_send_html():
    message = Message(subject='hello flask-mail',recipients=['2585765186@qq.com'])
    try:
        #发送渲染一个模板
        message.html = render_template('email_temp.html')
        mail.send(message)
        return '发送成功，请注意查收~'
    except Exception as e:
        print(e)
        return '发送失败'


if __name__ == '__main__':
    app.run(debug=True)