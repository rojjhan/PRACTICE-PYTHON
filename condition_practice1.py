#divisibility of the number by 3
numb = int(input('enter number:'))
if numb % 3 == 0 :
    print(f"The number { numb } is divisible by 3")
else:
    print(f"The number {numb} is not divisible by 3")
    
    
    
#win the race

myRank = 2

if myRank == 1:
    print("You got GOLD medal")
elif myRank == 2:
    print("You got SILVER medal")
elif myRank == 3:
    print("You got BORONZ medal")
else:
    print("You got no medal")
    
print("You win this race") if myRank == 1 else print("You dont win")
