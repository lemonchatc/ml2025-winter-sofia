import numpy as np


# show error message if user input negative or invalid numbers
def check_positive(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Oops! Please enter a positive integer.")
        except ValueError:
            print("Invalid number. Please enter a number.")


def knn(data, target, k):
    if k > len(data):
        return "Error: k cannot be greater than the number of points."
    
    # calculate distance
    dist = np.abs(data[:, 0] - target)
    # sort the distance
    near = np.argsort(dist)[:k]
    return np.mean(data[near, 1])



def main():
    N = check_positive("Please enter the number of points N: ")
    k = check_positive("Please enter the number of neighbors K: ")
    
    data = []
    for i in range(N):
        x = float(input(f"Enter x[{i+1}]: "))
        y = float(input(f"Enter y[{i+1}]: "))
        data.append([x, y])
    
    data = np.array(data)
    target = float(input("Please enter the value of X: "))
    result = knn(data, target, k)

    print(f"The predicted Y value is: {result}")

if __name__ == "__main__":
    main()
