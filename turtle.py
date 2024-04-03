import turtle
import random

def draw_polygon(sides, side_length, color):
    angle = 360 / sides
    for _ in range(sides):
        turtle.color(color())
        turtle.forward(side_length)
        turtle.right(angle)

def rainbow_color():
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
    return random.choice(colors)

def main():
    turtle.speed(0)
    while True:
        sides = int(input("Enter the number of sides for the polygon (1-100): "))
        if sides <= 0 or sides >= 100:
            print("Please enter a valid number of sides (1-100).")
            continue
        side_length = int(input("Enter the length of each side in pixels: "))

        print("Choose a color for the polygon:")
        print("1. Red")
        print("2. Blue")
        print("3. Orange")
        print("4. Purple")
        print("5. Black")
        print("6. Violet")
        print("7. Green")
        print("8. Gold")
        print("9. Indigo")
        print("10. Cyan")
        print("11. Rainbow")

        color_choice = input("Enter the number corresponding to your color choice: ")

        if color_choice == '11':
            draw_polygon(sides, side_length, rainbow_color)
        elif color_choice not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
            print("Invalid color choice. Please enter a number from 1 to 11.")
            continue
        else:
            colors = ['red', 'blue', 'orange', 'purple', 'black', 'violet', 'green', 'gold', 'indigo', 'cyan']
            chosen_color = colors[int(color_choice) - 1]
            draw_polygon(sides, side_length, lambda: chosen_color)

        again = input("Do you want to draw another polygon? (yes/no): ")
        if again.lower() != 'yes':
            break

    turtle.done()

if __name__ == "__main__":
    main()
