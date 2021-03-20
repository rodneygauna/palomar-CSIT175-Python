numbers = (1, 2, 3, 4)

def main():
    print(numbers)
    adds_numbers(numbers)

def adds_numbers(num):
    print("Tuple Total is:", sum(num))

if __name__ == "__main__":
    main()