import praw
import datetime
import time

reddit = praw.Reddit("_s0me_guy_", config_interpolation="basic")
realtime = [datetime.datetime.now().hour, datetime.datetime.now().minute, datetime.datetime.now().second]

print("Axisbot started")

for x in range(1000):
    cycle = open("AxisBotCycles.txt", "r")
    cycle_content = cycle.readlines()

    second = int(cycle_content[0])
    minute = int(cycle_content[1])
    hour = int(cycle_content[2])

    waitingtime = [hour, minute, second]
    print(waitingtime)
    submission = reddit.submission(url="https://www.reddit.com/r/axisorderbot/comments/p1g7hm/official_pray_thread_7/")
    for y in range(1000):
        while realtime != waitingtime:
            realtime = [datetime.datetime.now().hour, datetime.datetime.now().minute, datetime.datetime.now().second]
            time.sleep(0.5)
        submission.reply('!axisbot !pray all')

        second += 1
        if second == 60:
            second = 0
            minute += 1
            minute = str(minute)
            cycle_content[1] = minute + "\n"

        if minute == 60:
            minute = 0
            hour += 1
            hour = str(hour)
            cycle_content[2] = hour + "\n"

        second = str(second)
        cycle_content[0] = second + "\n"

        cycle = open("AxisBotCycles.txt", "w")
        cycle.writelines(cycle_content)
        cycle.close()

        time.sleep(2)
        realtime = [datetime.datetime.now().hour, datetime.datetime.now().minute, datetime.datetime.now().second]
        break
