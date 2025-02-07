# User input N
N = int(input("Please enter a positive integer: "))

numbers = []
for i in range(N):
    num = int(input(f"Please enter your number {i + 1}: "))
    numbers.append(num)

# User input X
X = int(input("Please enter an integer: "))

if X in numbers:
    print(numbers.index(X) + 1)
else:
    print("-1")