class ProcessNumber:
    def __init__(self):
        self.numbers = []  # Initialize an empty list to store numbers
        
    def input_numbers(self, n):
        for _ in range(n):
            num = int(input("Please enter a number: "))
            self.numbers.append(num)
    
    def search_index(self, x):
        if x in self.numbers:
            return self.numbers.index(x) + 1  # Return 1-based index
        else:
            return -1
