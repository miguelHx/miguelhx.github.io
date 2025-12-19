Title: Intro to CS: Problem Set 1
Date: 2025-12-19 13:47
Category: Intro to CS using Python
Tags: computer-science,python

I was able to do part A and B in less than 1 hour.  Part C, however, I will have to watch the related lectures because I need to know the bisection search algorithm, which I don’t know off the top of my head.  Part A and B were good exercises, dealing with compound interests and it was basically how many months to save up for a house down payment given certain inputs like yearly salary, savings rate, etc.

Here is my solution for A and B:

Part A:
```python
yearly_salary = float(input('enter yearly salary: '))
portion_saved = float(input('enter % of salary to save, as a decimal: '))
cost_of_dream_home = float(input('enter cost of dream home: '))

portion_down_payment = 0.25
r = 0.05
down_payment_amount = cost_of_dream_home * portion_down_payment

first_month_saved = (yearly_salary / 12.0) * portion_saved
amt_saved = 0
monthly_return = first_month_saved * (r / 12)

months = 0
while amt_saved <= down_payment_amount:
    amt_saved += first_month_saved + monthly_return
    monthly_return = amt_saved * (r / 12)
    months += 1
print('number of months: ', months)
```

Part B:
```python
yearly_salary = float(input('enter yearly salary: '))
portion_saved = float(input('enter % of salary to save, as a decimal: '))
cost_of_dream_home = float(input('enter cost of dream home: '))
semi_annual_raise = float(input('enter semi-annual raise, as a decimal: '))

portion_down_payment = 0.25
r = 0.05
down_payment_amount = cost_of_dream_home * portion_down_payment

first_month_saved = (yearly_salary / 12.0) * portion_saved
amt_saved = 0
monthly_return = first_month_saved * (r / 12)

months = 0
while amt_saved <= down_payment_amount:
    amt_saved += first_month_saved + monthly_return
    monthly_return = amt_saved * (r / 12)
    months += 1
    if months % 6 == 0:
        yearly_salary += yearly_salary * semi_annual_raise
        first_month_saved = (yearly_salary / 12.0) * portion_saved
print('number of months: ', months)
```

Part B was just an extension of part A.  It's pretty easy if you have strong programming and math fundamentals. I can see beginners potentially struggling with this though.

Problem set 1 isn’t due until like after lecture 9, so I have plenty of time to complete it as I just finished lecture 2. Then I will update this post with my solution to part C.