while True:
    num = int(input("Please enter a whole number (i.e. an integer): "))
    print(f"The number you entered is {num}.")

    # Check if the number is even or odd
    if num % 2 == 0:
        print(f"{num} is an even number.")
    else:
        print(f"{num} is an odd number.")

    # Check if the number has a perfect square root
    #if int(num.sqrt(2)) == num.sqrt(2)
    if int(num**0.5)**2 == num:
        print(f"{num} has a perfect square root.")
    else:
        print(f"{num} does not have a perfect square root.")

    # Find factors of the number
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    print(f"The factors of {num} are {', '.join(map(str, factors))}.")

    choice = input("Would you like to enter another number? (Y/n): ").strip().lower()
    if choice != 'y':
        print("Thank you for playing!")
        break
