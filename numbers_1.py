def is_even(number):
    return number % 2 == 0

def has_perfect_square_root(number):
    return int(number**0.5)**2 == number

def find_factors(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

def main():
    while True:
        num = int(input("\033[1mPlease enter a whole number (i.e. an integer): \033[0m"))
        
        print(f"The number you entered is {num}.")
        
        if is_even(num):
            print(f"{num} is an even number.")
        else:
            print(f"{num} is an odd number.")
        
        if has_perfect_square_root(num):
            print(f"{num} has a perfect square root.")
        else:
            print(f"{num} does not have a perfect square root.")
        
        factors = find_factors(num)
        print(f"The factors of {num} are {', '.join(map(str, factors))}.")
        
        choice = input("\033[1mWould you like to enter another number? (Y/n): \033[0m").strip().lower()
        if choice != 'y':
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    main()