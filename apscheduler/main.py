from flask import Flask

from flask_apscheduler import APScheduler

app = Flask(__name__)

scheduler = APScheduler()


@scheduler.task(trigger="interval", id="test_job", seconds=5)
def test_job():
    print("hello ")


class BaseConfig(object):
    SCHEDULER_API_ENABLED = True


if __name__ == '__main__':
    app.config["SCHEDULER_API_ENABLED"]=True # 通过http api管理任务
    scheduler.init_app(app)
    scheduler.start()
    aa= app.url_map.iter_rules() # 查看注册的url的信息
    print(list(aa))
    app.run()
