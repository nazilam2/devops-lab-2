# Define a list of numbers
numbers = [5, 10, 15, 20, 25]

# Calculate the average
if len(numbers) > 0:
    average = sum(numbers) / len(numbers)
    print(f"The average of the numbers is: {average}")
else:
    print("No numbers to calculate the average.")

# FORK START
large = 0
small = numbers[0]
for i in numbers:
	if(i > large):
		large = i
	if(i < small):
		small = i

print('Largest = ', large)
print('Smallest = ', small)
