# Function to swap values of four variables
def swap_variables(a, b, c, d):
    # Displaying values before swapping
    print("Before swapping")
    print(f"a={a}, b={b}, c={c}, d={d}")

    # Swapping values
    a, b, c, d = d, c, b, a

    # Displaying values after swapping
    print("After swapping")
    print(f"a={a}, b={b}, c={c}, d={d}")

# Taking user input for four values
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))
d = int(input("Enter the value of d: "))

# Calling the function to swap values
swap_variables(a, b, c, d)
