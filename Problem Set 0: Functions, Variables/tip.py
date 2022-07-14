# Define main function
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

# Accept a str as input (formatted as $##.##, wherein each # is a decimal digit),
# removes the leading $, and returns the amount as a float.
def dollars_to_float(d):
    # Replace '$' with an empty character to remove it
    d = d.replace('$','')

    # Convert to a float and return the result
    f1 = float(d)
    return f1

# Accepts a str as input (formatted as ##%, wherein each # is a decimal digit),
# removes the trailing %, and returns the percentage as a float.
def percent_to_float(p):
    # Replace '%' with an empty character to remove it and convert to a float
    p = p.replace('%','')
    f2 = float(p)

    # Divide by 100 to convert the percentage to a decimal
    f2 = f2 / 100

    # Return result
    return f2

main()
