import math

# Function to calculate total area
def calculate_total_area(front_length, front_width, rear_length, rear_width, left_length, left_width, right_length, right_width):
    front_area = front_length * front_width
    rear_area = rear_length * rear_width
    left_area = left_length * left_width
    right_area = right_length * right_width
    total_area = front_area + rear_area + left_area + right_area
    return total_area

# Function to calculate bags of fertilizer needed
def calculate_fertilizer(total_area):
    bags_of_fertilizer = total_area / 2000  # 1 bag covers 2000 sq. feet
    return math.ceil(bags_of_fertilizer)  # Round up using math.ceil()

# Function to calculate total cost of fertilizer
def calculate_fertilizer_cost(bags_of_fertilizer, cost_per_bag):
    fertilizer_cost = bags_of_fertilizer * cost_per_bag
    return fertilizer_cost

# Function to calculate total labor hours and labor cost
def calculate_labor_cost(total_area, labor_rate_per_hour):
    labor_hours = total_area / 2500  # Assuming 1 hour covers 2500 sq. feet
    labor_hours_rounded_up = math.ceil(labor_hours)  # Round up using math.ceil()
    labor_cost = labor_hours_rounded_up * labor_rate_per_hour
    return labor_hours_rounded_up, labor_cost

# Function to calculate total cost to the company
def calculate_total_cost(fertilizer_cost, labor_cost):
    total_cost = fertilizer_cost + labor_cost
    return total_cost

# Function to calculate pounds of nitrogen and potassium
def calculate_npk(bags_of_fertilizer):
    pounds_of_nitrogen = bags_of_fertilizer * 0.5 # Assuming 0.5 pounds of nitrogen per sq. feet
    pounds_of_potassium = bags_of_fertilizer * 0.125 # Assuming 0.125 pounds of potassium per sq. feet
    return pounds_of_nitrogen, pounds_of_potassium

# Input dimensions of the sections
front_length = float(input("What is the length of the front section? "))
front_width = float(input("What is the width of the front section? "))
rear_length = float(input("What is the length of the rear section? "))
rear_width = float(input("What is the width of the rear section? "))
left_length = float(input("What is the length of the left section? "))
left_width = float(input("What is the width of the left section? "))
right_length = float(input("What is the length of the right section? "))
right_width = float(input("What is the width of the right section? "))

# Fixed cost per bag of fertilizer
cost_per_bag = 27  # Fixed cost per bag

# Fixed labor rate per hour
labor_rate_per_hour = 20  # Fixed labor rate per hour

# Calculate total area
total_area = calculate_total_area(front_length, front_width, rear_length, rear_width, left_length, left_width, right_length, right_width)

# Calculate bags of fertilizer needed
bags_of_fertilizer = calculate_fertilizer(total_area)

# Calculate total cost of fertilizer
fertilizer_cost = calculate_fertilizer_cost(bags_of_fertilizer, cost_per_bag)

# Calculate total labor hours and labor cost
labor_hours_rounded_up, labor_cost = calculate_labor_cost(total_area, labor_rate_per_hour)

# Calculate total cost to the company
total_cost = calculate_total_cost(fertilizer_cost, labor_cost)

# Calculate pounds of nitrogen and potassium
pounds_of_nitrogen, pounds_of_potassium = calculate_npk(total_area)

# Output the results
print(f"Your application has a total area of {total_area} sq. feet. That will require {bags_of_fertilizer} bags of fertilizer. The cost of the fertilizer will be ${fertilizer_cost:.2f}.")
print(f"Our technicians will require {labor_hours_rounded_up} hours to finish the job and the labor cost will be ${labor_cost:.2f}.")
print(f"The total cost to the company will be ${total_cost:.2f}. The application will result in {pounds_of_nitrogen:.0f} pounds of nitrogen and {pounds_of_potassium:.3f} pounds of potassium being added to the soil.")
