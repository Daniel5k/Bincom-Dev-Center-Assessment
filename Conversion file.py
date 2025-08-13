import random

number= ""
for num in range(0, 4):
    number+=str(random.randint(0,1))

decimal_number = 0
power_number = 0

for num in reversed(number):
    decimal_number += int(num) * (2**power_number)
    power_number +=1
    
print(f"The base 10 of {number} is : {decimal_number}")