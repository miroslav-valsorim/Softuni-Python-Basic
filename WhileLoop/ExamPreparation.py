failed_threshold = int(input())

failed_times = 0
problem_solved_count = 0
grades_sum = 0
last_problem = ''
has_failed = True

while failed_times < failed_threshold:
    problem_name = input()
    if problem_name == "Enough":
        has_failed = False
        break

    grade = int(input())
    if grade <= 4:
        failed_times += 1

    grades_sum += grade
    problem_solved_count += 1
    last_problem = problem_name

if has_failed:
    print(f"You need a break, {failed_threshold} poor grades.")
else:
    print(f"Average score: { grades_sum / problem_solved_count:.2f}")
    print(f"Number of problems: {problem_solved_count}")
    print(f"Last problem: {last_problem}")