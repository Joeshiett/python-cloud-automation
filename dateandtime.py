from datetime import datetime

user_input = input('Enter Goal and deadline in this format; <Goal:dd.mm.YYYY>\n')

goal_deadline = user_input.split(':')
goal = goal_deadline[0]
deadline = goal_deadline[1]

till_date = datetime.strptime(deadline, '%d.%m.%Y')
today_date = datetime.today()

deadline_date = till_date - today_date
print(f'{goal} in {deadline_date.days} days')
