# Nesting Functions is the action of calling a function inside another function
# Nesting Functions can be used to make code cleaner and easier to read

height = int(input("Height: "))
print(f'Height: {height} meters')


cost_of_room = int(input("Cost of room: "))
days_of_stay = int(input("Days of stay: "))
total_cost = cost_of_room * days_of_stay
print(f"total cost: {total_cost} USD")


length_1 = len(input("Enter a random word: "))
length_2 = len(input("Enter a random word: "))
total_length = length_1 + length_2
print(f"Total length: {total_length} characters")