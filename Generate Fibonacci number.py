number = 1
first_list_value= 0
second_list_value = 1
numbers = []

total_of_first_fifty = 0

for i in range(25): #25 loops x 2 numbers = 50 terms
    numbers.append(first_list_value)
    numbers.append(second_list_value)
    first_list_value += second_list_value
    second_list_value += first_list_value
    total_of_first_fifty +=first_list_value
   
    
print(numbers)
print(total_of_first_fifty)