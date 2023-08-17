from everphoto import Everphoto
from config import config
from push import PushSender, parse


def parse_message(message, push_type):
    if push_type == "pushplus":
        return parse(message, template="html")
    else:
        return parse(message, template="markdown")


def pushMessage(message, config):
    if isinstance(config, list):
        for item in config:
            t = item.get("type")

            p = PushSender(t, item.get("key"))

            p.send(parse_message(message, t), title="时光相册")
    else:
        t = config.get("type")

        p = PushSender(config.get("type"), config.get("key"))

        p.send(parse_message(message, t), title="时光相册")


def main(*args):
    accounts = config.get("multi")
    push_together = config.get("push")

    messages = []

    for item in accounts:
        obj = Everphoto(**item)

        res = obj.start()

        push = item.get("push")

        if push is None:
            if push_together is not None:
                messages.extend(res)
        else:
            pushMessage(res, push)
        # --------------------  原项目自修改: Bark推送 -------------------
        bark_title = "时光相册签到"
        bar_url = "https://<地址>/<token>/"
        try:
            bark_false = res[0]['txt']['content']
        except KeyError:
            try:
                bark_success = f"执行结果: {res[2]['txt']['content']}"
            except Exception as e:
                print('其他错误: ', e)
            else:
                resp = requests.get(url=f"{bar_url}{bark_title}/{bark_success}?group=ServerCron")
                resp.close()
                print("签到成功!")
        else:
            resp = requests.get(url=f"{bar_url}{bark_title}/{bark_false}?group=ServerCron")
            resp.close()
            print("签到失败!")
    # -------------- 自定义结束 --------------------------
    if len(messages) != 0 and push_together is not None:
        pushMessage(messages, push_together)


if __name__ == "__main__":
    main()
