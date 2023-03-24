import random


# Method 1: populate list with random integers between 10 and 50
def populate_list(length):
  lst = [random.randint(10, 50) for i in range(length)]
  return lst


# Method 2: sum up the list
def list_sum(lst):
  total = sum(lst)
  return total


# This while true loop makes it so the prompt keeps asking for an integer if the input is not valid
while True:
  user_input = input("Enter an integer number between 5 and 15: ")
  if user_input.isnumeric() and 5 <= int(user_input) <= 15:
    break
  else:
    print("Please enter a valid integer between 5 and 15.")

# Executes the first method, which is to populate the list
length = int(user_input)
lst = populate_list(length)
print("The elements of the array are:", end=" ")

# Prints out the list of generated numbers
for i in lst:
  print(i, end=" ")
print()

# Executes second method, which is to sum the list up
total = list_sum(lst)

# Prints out the sum
print("The sum is:", total)
