# got grade and show rank

corse = int(input("enter your grade:"))

if 0 <= corse <= 70 :
    print("fail")
elif 71 <= corse <= 80 :
    print("good")
elif 81 <= corse <= 90:
    print("verygood")
elif 91 <= corse <= 100:
    print("excellent")
else:
    print("invalid grade")


#--------------------------------------------------------------------
# give number x and show 1 until number x next multiplication 1-x

number = int(input("enter number :"))
p = 1
for i in range(1,number,1):
    p = i * p
    print(i, end = "\t")
print("Multiply = ", p)


#--------------------------------------------------------------------
# The largest digit

num = int(input("enter number:"))
max = num % 10
while num > 0:
    if max < num % 10:
        max = num % 10
    num = num // 10
print(max)


#--------------------------------------------------------------------
# Prime numbers

number = int(input("Enter number:"))

prime = False
for i in range(2,number //2,1):
    if number % i == 0:
        prime = True
if prime is True:
    print(f"number {number} is not prime")
else:
    print(f"number {number} is prime")