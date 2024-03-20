is_even = lambda number: number % 2 == 0
has_perfect_square_root = lambda number: int(number**0.5)**2 == number
find_factors = lambda number: [i for i in range(1, number + 1) if number % i == 0]

while True:
    num = int(input("Please enter a whole number (i.e. an integer): "))
    
    print(f"The number you entered is {num}.")
    
    print(f"{num} is an {'even' if is_even(num) else 'odd'} number.")
    
    print(f"{num} {'has' if has_perfect_square_root(num) else 'does not have'} a perfect square root.")
    
    factors = find_factors(num)
    print(f"The factors of {num} are {', '.join(map(str, factors))}.")
    
    choice = input("\033[1mWould you like to enter another number? (Y/n): \033[0m").strip().lower()
    if choice != 'y':
        print("Thank you for playing!")
        break