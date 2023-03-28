print("Hi")
print("Let`s calculate yuor Body Mass Index(BMI)")

w = float(input("please enter your weight(kg):"))
h = float(input("please enter your height(m):"))
bmi = w/h**2

print("Your BMI:",bmi)

if 18.5>bmi:
        print("You`re in Underweight status")
elif 25>bmi>=18.5:
        print("You`re in Normal status")
elif 30>bmi>=25:
        print("You`re in Overweight status")
elif 35>bmi>=30:
        print("You`re in Obese status")
elif bmi>35:
        print("You`re in Extremely Obese status")