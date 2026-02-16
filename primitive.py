# Alex's Life Story Using Primitive Data Types

name = "Alex"
age = 5
is_student = True

favorite_food = "pizza"
hometown = "Lagos"

greeting = "Hello, my name is " + name
age_statement = "I am " + str(age) + " years old."

next_year_age = age + 1
future_age_statement = "Next year I will be " + str(next_year_age) + "."

school_years = 12
graduation_age = age + school_years

height = 1.1
growth = 0.6
adult_height = height + growth

has_job = False
first_salary = 30000
salary_raise = 5000
new_salary = first_salary + salary_raise

dream_job = "Software Engineer"
life_goal = name + " wants to become a " + dream_job

summary = greeting + ". " + age_statement + " I live in " + hometown + " and love " + favorite_food + "."

print(summary)
print(future_age_statement)
print("I will graduate at age:", graduation_age)
print("My adult height might be:", adult_height, "meters")
print("Current student status:", is_student)
print("Do I have a job?", has_job)
print("Future salary after raise:", new_salary)
print("Life goal:", life_goal)