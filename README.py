import time

def focus_timer(total_time):
    start_time = time.time()
    end_time = start_time + total_time * 60

    print("专注时间开始！")
    while time.time() < end_time:
        # 在此处添加你想要执行的专注任务
        pass

    print("专注时间结束！")

# 设置总时间为25分钟
focus_timer(25)
