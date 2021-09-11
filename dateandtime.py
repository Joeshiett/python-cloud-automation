from datetime import datetime #import date and time module

user_input = input('Enter goal and deadline: ')
goal_deadline = user_input.split(':')
goal = goal_deadline[0]
deadline = goal_deadline[1]

till_date = datetime.strptime(deadline, '%d.%m.%Y')
today_date = datetime.today()
deadline_days = till_date - today_date

print(deadline_days)