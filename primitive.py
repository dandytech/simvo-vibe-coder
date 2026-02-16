# Alex's Expanding Life Story

name = "Alex"
age = 5
is_student = True
is_happy = True

hometown = "Lagos"
country = "Nigeria"

favorite_subject = "Math"
favorite_food = "Pizza"

current_grade = 1
years_in_school = 12
graduation_age = age + years_in_school

height_child = 1.1
yearly_growth = 0.07
years_growth = 10
height_teen = height_child + (yearly_growth * years_growth)

dream_job = "Software Engineer"
first_salary = 30000
bonus = 7000
total_income = first_salary + bonus

monthly_income = total_income / 12
savings_rate = 0.2
yearly_savings = total_income * savings_rate

future_partner = "Jamie"
future_family = name + " & " + future_partner

identity = name + " from " + hometown + ", " + country
school_story = "I love " + favorite_subject + " and I am in grade " + str(current_grade)
growth_story = "At graduation I will be " + str(graduation_age) + " years old."
career_story = "My dream job is " + dream_job
money_story = "My yearly savings will be " + str(yearly_savings)

print("Identity:", identity)
print("Age:", age)
print("Student status:", is_student)
print("Happy status:", is_happy)
print(school_story)
print(growth_story)
print("Teen height:", height_teen, "meters")
print(career_story)
print("Total income:", total_income)
print("Monthly income:", monthly_income)
print(money_story)
print("Future family:", future_family)