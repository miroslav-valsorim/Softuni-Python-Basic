v_in_liters = int(input())
p1_for_hour = int(input())
p2_for_hour = int(input())
hours_missing = float(input())

p1_work = p1_for_hour * hours_missing
p2_work = p2_for_hour * hours_missing
both_pipes = p1_work + p2_work
both_in_percentage = both_pipes / v_in_liters * 100
pipe_p1_in_percentage = p1_work / both_pipes * 100
pipe_p2_in_percentage = p2_work / both_pipes * 100
liters_over = both_pipes - v_in_liters

if both_pipes <= v_in_liters:
    print(f"The pool is {both_in_percentage:.2f}% full. Pipe 1: {pipe_p1_in_percentage:.2f}%. Pipe 2: {pipe_p2_in_percentage:.2f}%.")
else:
    print(f"For {hours_missing} hours the pool overflows with {abs(liters_over):.2f} liters.")
