from math import floor
from math import ceil

hours_needed = int(input())
days_for_work = int(input())
overtime_workers = int(input())
normal_shift = 8

learn_time = days_for_work - days_for_work * 10 / 100
hours_for_work = learn_time * normal_shift
overtime = overtime_workers * (2 * days_for_work)
all_time = hours_for_work + overtime

if hours_needed <= all_time:
    time_left = hours_needed - floor(all_time)
    print(f"Yes!{abs(time_left)} hours left.")
elif hours_needed > all_time:
    time_needed = all_time - hours_needed
    print(f"Not enough time!{ceil(abs(time_needed))} hours needed.")