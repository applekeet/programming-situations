"""


3
1 6 13
8 0
3 6 0
12 30
14 45
6 0
2 23 35
20 15
10 30


time of sleep: 23 35

10 55

======
25 minutes
+ 10 30
10 55 answer

6 13
only one option: 8 0 == 1 47

"""
import datetime

n = int(input())

for y in range(n):
    a, s_hour, s_min = input().split(" ")
    sleep_time = datetime.timedelta(hours=int(s_hour), minutes=int(s_min))
    # print(a, s_hour, s_min)
    alarm_list = []
    for z in range(int(a)):
        a_hour, a_min = input().split(" ")
        a_time = datetime.timedelta(hours=int(a_hour), minutes=int(a_min))
        alarm_list.append(a_time)
    # print(a, sleep_time, alarm_list)
    alarm_list.sort()
    flag = False
    for alarm in alarm_list:
        # print(alarm, sleep_time)
        if alarm > sleep_time:
            prt = alarm - sleep_time
            print(prt.seconds // 3600, (prt.seconds % 3600) // 60)
            flag = True
            break
        elif alarm == sleep_time:
            print("0 0")
            flag = True
            break
    if not flag:
        # this means the alarm is lower and sleep_time is higher number
        time_to_midnight = datetime.timedelta(hours=24) - sleep_time
        nice_duration = time_to_midnight + alarm_list[0]
        print(nice_duration.seconds // 3600, (
            nice_duration.seconds % 3600) // 60)



