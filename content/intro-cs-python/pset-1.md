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
while amt_saved < down_payment_amount:
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
while amt_saved < down_payment_amount:
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

Update: Finished part C. It wasn't too bad. I liked the exercise.  I didn't one-shot it due to small nuances like updating the high/low to r instead of guess and checking the absolute value of amount - guess within epsilon. Wrote print statements to debug then got the answer. Also had to run into infinite loop before fixing case where initial deposit is too small to reach desired amount in 36 months. Here is my solution:

```python
##############################################
## Get user input for initial_deposit below ##
##############################################
initial_deposit = float(input('Enter the initial deposit: '))


#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
house_cost = 800000
down_payment_rate = 0.25
down_payment_amount = house_cost * down_payment_rate
months = 36
epsilon = 100


##################################################################################################
## Determine the lowest rate of return needed to get the down payment for your dream home below ##
##################################################################################################

low = 0.0
high = 1.0
r = (high + low) / 2.0
guess = (initial_deposit * (1 + (r / 12.0)) ** months)
steps = 1
while abs(down_payment_amount - guess) > epsilon:
    if guess > down_payment_amount:
        high = r
    else:
        low = r
    r = (high + low) / 2.0
    if r == 1.0:
        r = None
        steps = 0
        break
    guess = (initial_deposit * (1 + (r / 12.0)) ** months)
    steps += 1

print('Best savings rate:', r, '[or very close to this number]')
print('Steps in bisection search:', steps, '[or very close to this number]')
```