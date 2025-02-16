from module5_mod import ProcessNumber

def main():
    n = int(input("Please enter the number of elements N: "))
    
    processor = ProcessNumber()
    
    # Read N numbers from the user
    processor.input_numbers(n)
    
    # User input for X (the number to search for)
    x = int(input("Please enter the number X to search for: "))
    
    # Find and display the index of X
    index = processor.search_index(x)
    print(index)

if __name__ == "__main__":
    main()
