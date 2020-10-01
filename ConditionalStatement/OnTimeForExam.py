
exam_hour = int(input())
exam_minutes = int(input())
hour_arrive = int(input())
minutes_arrive = int(input())

time_of_exam_in_minutes = exam_hour * 60 + exam_minutes
time_of_arrive_in_minutes = hour_arrive * 60 + minutes_arrive

diff = abs(time_of_exam_in_minutes - time_of_arrive_in_minutes)

if time_of_arrive_in_minutes > time_of_exam_in_minutes:
    print("Late")
elif time_of_exam_in_minutes - 30 <= time_of_arrive_in_minutes <= time_of_exam_in_minutes:
    print("On time")
elif time_of_arrive_in_minutes < time_of_exam_in_minutes - 30:
    print("Early")

if time_of_exam_in_minutes - 60 < time_of_arrive_in_minutes < time_of_exam_in_minutes:
    print(f"{diff} minutes before the start")
elif time_of_arrive_in_minutes <= time_of_exam_in_minutes - 60:
    hours = diff // 60
    minutes = diff % 60
    if minutes <= 9:
        print(f"{hours}:0{minutes} hours before the start")
    else:
        print(f"{hours}:{minutes} hours before the start")
elif time_of_exam_in_minutes < time_of_arrive_in_minutes < time_of_exam_in_minutes + 60:
    print(f"{diff} minutes after the start")
elif time_of_arrive_in_minutes >= time_of_exam_in_minutes + 60:
    hours = diff // 60
    minutes = diff % 60
    if minutes <= 9:
        print(f"{hours}:0{minutes} hours after the start")
    else:
        print(f"{hours}:{minutes} hours after the start")