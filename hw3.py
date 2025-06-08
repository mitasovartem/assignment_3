#Elementary_level
array = [1,3,4,5,-2,7,-9,13,53]
suma = sum(array)
minimum = min(array)
print(f"The sum of list is {suma}, and the minimum is {minimum}")
array.reverse()
print(f"Reversed list: {array}")
array.reverse()
for i in range(len(array)):
    if array[i]%2!=0:
        print(array[i], end=" ")




number = int(input("Input number for multiplication: "))
multiplication = []
for i in array:
    new_element = number*i
    multiplication.append(new_element)
print(f"Multiplied list:{multiplication}", end=" ")




#Easy_level
# 1. Filter values greater than X
x = int(input("Input number for filter: "))
filtered_list = []
for i in array:
    if i>x:
        filtered_list.append(i)
print(f"Filtered numbers from list, greater than {x}, is :{filtered_list}", end=" ")



# 2. Average of positive numbers
average_list = []
for i in array:
    if i>0:
        average_list.append(i)
        average_list = average_list+i
average_list=average_list/len(average_list)
print(f"Average of a positive numbers in list is: {average_list}", end=" ")



# 3. Maximum of numbers less than X
less_list = []
for i in array:
    if i<x:
        less_list.append(i)
if less_list:
    print("Maximum of values that are less than x< is: ",max(less_list), end=" ")
else:
    print("Non values that are less than x")



# 4. Sum of numbers divisible by Y
division_list = []
y = int(input("Input your divisiour: "))
suma_divisiours = 0
for i in array:
    if i%y==0:
        suma_divisiours = suma_divisiours + i
print(f"The sum of numbers divisibles by {y}, is {suma_divisiours}")




# 5. List of squares
square_list = []
for i in array:
    square_numb = i**2
    square_list.append(square_numb)
print(f"Squared list: {square_list}", end=" ")



# 6. Extract positive numbers
dodatniy_list = []
for i in array:
    if i>0:
        dodatniy_list.append(i)
print(f"Positive list: {dodatniy_list}", end=" ")



# 7. Filter strings by prefix
string_list = ["list","bug","kse","python","ukraine"]
prefix = str(input("Input your prefix: "))
matching = []
for i in string_list:
    if i.startswith(prefix):
        matching.append(i)
print(f"Matched strings are: {matching}", end=" ")


        
# 8. Sum of first n numbers
n = int(input("Input the aamount of operated numbers in list: "))
sum_less_n = 0
for i in range(min(n,len(array))):
    if i<=n:
        sum_less_n = sum_less_n + array[i]
print(f"Thse sum of first {n} numbers is {sum_less_n}")



# 9. Find all palindromes
palindromes_str = ["list","kse","Dnipro","Kyiv","kse"]
palindromes = []
for i in palindromes_str:
    if i == i[::-1]:
        palindromes.append(i)
print(f"The palindromes are: {palindromes}", end=" ")



# 10. Divisibility check list
division_numb = int(input("Input your number for division: "))
divisionable_array = []
for i in array:
    divisionable_array.append(i%division_numb==0)
print(f"Array that is divisible by {division_numb} is: {divisionable_array}", end=" ")
divisionable_array.clear()




#Medium_level
# 1. Filtering of list
x = int(input("Input the first number for filtering: "))
x = int(input("Input the second number for filtering: "))
for i in array:
    if i%x==0 and i%y!=0:
        divisionable_array.append(i)
print(f"New filtered list is: {divisionable_array}", end=" ")



# 2. Flatten nested lists
list_1 = [[3,5],[7,1],[],[947,329]]
list_together = [] 
for i in list_1:
    for j in i:
        list_together.append(j)
print(f"Together it is the list: {list_together}", end=" ")



# 5. Conditional merge of two lists
list1 = [1, 42, 253, 44, 1]
list2 = [10, 24, 324, 0, 50]
merged_list = []
for i, j in zip(list1, list2):
    merged_list.append(i if i % 2 == 0 else j)
print(f"Conditionally merged list: {merged_list}", end=" ")



# 6. Dictionary aggregation by key
dictionary = [{'i': 11}, {'j': -5}, {'i': 47}, {'j': 23}]
aggr_key = {}
for d in dictionary:
    for k, v in d.items():
        aggr_key[k] = aggr_key.get(k, 0) + v
print(f"Aggregated values are: {aggr_key}", end=" ")



# 7. Conditional replacement in list
replaced_list = []
for i in array:
    if i<0:
        replaced_list.append(0)
    else:
        replaced_list.append(i)
print(f"List with negative numbers replaced by 0: {replaced_list}")



# 8. Count strings longer than X
x = int(input("Input the minimum string length: "))
array_biggerx = 0
for i in string_list:
    if len(i)>x:
        array_biggerx = array_biggerx + i
print(f"The amont of strings that are longer than {x}, is {array_biggerx}")



# 9. Altered merging of two lists
list_str = ["richka","kse","student","para"]
altered_list = []
for i,j in zip(list_str,string_list):
        altered_list.append(i)
        altered_list.append(j)
print(f"Your altered list is: {altered_list}", end=" ")



# 10. Multiply on y, if greater than X
x = int(input("Input the x-number: "))
y = int(input("Input the y-number for multiplication: "))
multiply_filtered_list = []
for i in array:
    if i>x:
        multiply_filtered_list.append(i*y)
    else:
        multiply_filtered_list.append(i)
print(f"New list after multiplication is: {multiply_filtered_list}", end=" ")