import requests
from datetime import datetime, timedelta
import random


# 计算两个日期之间的天数
def days_until(target_date):
    today = datetime.now()
    delta = target_date - today
    return delta.days


# 计算两个日期之间的工作日天数
def workdays_until(target_date):
    today = datetime.now()
    delta_days = (target_date - today).days
    workdays = 0
    for i in range(delta_days):
        day = today + timedelta(days=i)
        if day.weekday() < 5:  # 0-4代表周一到周五
            workdays += 1
    return workdays


# 主函数
def main():
    # 目标日期
    target_date = datetime(2024, 8, 30)
    today = datetime.now()

    # 检查当前日期是否早于目标日期
    if today >= target_date:
        print("已超过2024年8月30日，脚本停止执行。")
        return

    # 计算剩余天数和工作日
    days_left = days_until(target_date)
    workdays_left = workdays_until(target_date)

    # 吉祥话数组
    blessings = [
        "请大家多喝热水，关爱自己身体健康。",
        "愿大家天天开心，身体健康！",
        "记得多喝水，多锻炼，保持健康！",
        "祝大家工作顺利，心情愉快！",
        "保持健康生活方式，幸福每一天！",
        "愿你每天都充满正能量！",
        "祝你好运连连，事事顺心！"
    ]

    # 随机选择一句吉祥话
    blessing = random.choice(blessings)

    # 生成提醒文本
    reminder_text = (
        f"各位，今天距离2024年8月30日还有{days_left}天，其中有{workdays_left}个工作日。\n"
        f"{blessing}"
    )

    # 设置请求的URL和数据
    url = "https://open.larksuite.com/open-apis/bot/v2/hook/57a964aa-57f1-4bc4-8830-73e280a461d0"
    headers = {"Content-Type": "application/json"}
    data = {
        "msg_type": "text",
        "content": {
            "text": reminder_text
        }
    }

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        print("提醒发送成功")
    else:
        print(f"提醒发送失败，状态码: {response.status_code}")


# 执行入口
if __name__ == "__main__":
    main()
