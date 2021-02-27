import datetime
from datetime import date
from datetime import datetime
today_date=date.today()
print(today_date)
issue_date=datetime(2021,2,5)
print(issue_date.date())
count_days=today_date-issue_date.date()
no_of_days=(count_days.days)
print(no_of_days)
dead_line=15
if no_of_days>dead_line:
    fine=no_of_days-dead_line
    due_fine=fine*5
    print(due_fine)

else:
    print("no due")

