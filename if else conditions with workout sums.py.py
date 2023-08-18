#if else condition:
rcb="lose"
if rcb == "win":
    print("ee sala cup namade")
else:
    print("this time also no cup")

#if else condition:
rcb="win"
if rcb == "win":
    print("ee sala cup namade")
else:
    print("this time also no cup")


#get user input for variable meghna, if meghna==died. print "surya meets priya"
#else "surya weds meghna"

meghna = input()
if meghna == "Died":
    print("surya meets priya")
else:
    print("surya weds meghna")


#Get input for variable mark.if marks>35. print pass.else print fail.

mark = int(input("enter your mark: "))
if mark>=35:
    print("pass")
else:
    print("fail")


#Get input for variable income.if income is greater than 7000 not eligible for scholarship.
# else print  eligible for scholarship .

income = int(input("Enter your income: "))
if income>7000:
    print("not Eligible for scholarship")
else:
    print("Eligible for scholarship")


#Get input for a number and check whether it is divisible by both 3 and 5 or not. if yes then print,
#the number is divisible 3 and 5 . else print the number is not divisible by 3 and 5

a = int(input("Enter your number: "))
if a%3==0 and a%5==0:
    print("the number is divisible by 3 and 5")
else:
    print("the number is not divisible by 3 and 5")


#Get input for a number and find it is odd or even:

a = int(input("Enter a number: "))
if a%2==0:
    print("Even")
else:
    print("odd")

#Get input for score out of 100.
#if score is <35= "poor student"
#if score is >35 but < than 70 = "Average student"
#if score is >70= "Good student"

a = int(input("Enter your score: "))
if a<35:
    print("poor student")
elif a>35 and a<70:
    print("Average student")
elif a>70:
    print("Good student")
else:
    print("invalid score")


#get a input for score percentage. only if the percentage is greater than 70, get input for his name, department and location.
#then print you are eligible. if not print you are not eligible.

a = int(input("score percentage is: "))
if a>70:
    name = input("Enter your name: ")
    department = input("Enter your department: ")
    location = input("Enter your location: ")
    print("your are eligible")
else:
    print("your are not eligible")


#get a input for salary and age.
# if salary is greater than or equal to 20,000 or age less than or equal 25.
#get input for required loan amount.if not, print you are not eligible for loan.
#then print you are eligible.
#if required loan amount is less than or equal to 50,000. print maximum loan amount is 50,000.

salary = int(input("Enter your salary: "))
age = int(input("Enter your age: "))
if salary>=20000 and age<=25:
    loan_amount = int(input("Enter your loan amount: "))
    if loan_amount>50000:
        print("maximum loan amount is 50,000")
    else:
        print("your are eligible for loan")
else:
    print("your are not eligible for loan")


#get a input for five subject marks. add all of it,and find average.if average mark is less than 35.
#print "Additional class is required". else print "you are good to go"

a = int(input("Enter your mark: "))
b = int(input("Enter your mark: "))
c = int(input("Enter your mark: "))
d = int(input("Enter your mark: "))
e = int(input("Enter your mark: "))
average = (a+b+c+d+e/5)
if average<35:
    print("Additional class is required")
else:
    print("you are good to go")


