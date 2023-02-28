# For the following list of numbers:

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:

even_ints = []
for num in numbers:
    if num % 2 == 0:
        even_ints.append(num)
print(even_ints)

# 2. Print the difference between the largest and smallest value:
print(max(numbers) - min(numbers))

# 3. Print True if the list contains a 2 next to a 2 somewhere.

last_index = -1
value_to_search = 2 #no magic numbers!
result = False

if numbers.count(value_to_search) >= 2: #only bother if there's more at least 2 2s
    for i in range(numbers.count(value_to_search) - 1): #number of potential matches is the count minus 1
        #don't include the last_index and before otherwise infinite loop
        current_index = numbers.index(value_to_search, last_index + 1)

        #if the next value after a given 2 is also a 2, we good
        if numbers[current_index + 1] == value_to_search:
            result = True
        
        #in the words of Dave Grohl: 
        #done, done, onto the next one
        last_index = current_index

if result:
    print(result)

# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    
#    So [11, 6, 4, 99, 7, 11] would have sum of 22
active = True
result = 0
for elem in numbers:
    if active and elem == 6:
        active = False

    if active:
        result += elem
    
    if not active and elem == 7:
        active = True
print(result)

# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5.

after_13 = False
#no index tracking for me, no sir
result = 0
for num in numbers:
    if num == 13:
        after_13 = True
    if not after_13:
        result += num
    if num != 13:
        after_13 = False
print(result)