# to check wheather senior citizen or sttudent is eligible for a discount
age=int(input("Enter yout age: "))
if (age>=60) or (age<=18):
    print("You are eligible for a discount")
if (age<60) and (age>18):
    print("You are not eligible for a discount")

#login check 
is_logged_in = True
if (not is_logged_in) or ((age > 18) and (age<60)):
    print("Access denied")
elif (not is_logged_in) or (age>=60) or (age<=18):
    print("Access granted")
    print("Please Login first")
else:
    print("Welcome") 