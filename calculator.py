import math

def square_root(x):
    return math.sqrt(x)

def factorial(x):
    return math.factorial(x)

def natural_logarithm(x):
    return math.log(x)

def power_function(x, b):
    return math.pow(x, b)

def main():
    while True:
        print("\nScientific Calculator Menu:")
        print("1. Square Root (√x)")
        print("2. Factorial (x!)")
        print("3. Natural Logarithm (ln(x))")
        print("4. Power Function (x^b)")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            x = float(input("Enter a number to find its square root: "))
            print(f"Square Root of {x} is: {square_root(x)}")
        elif choice == '2':
            x = int(input("Enter a number to find its factorial: "))
            print(f"Factorial of {x} is: {factorial(x)}")
        elif choice == '3':
            x = float(input("Enter a number to find its natural logarithm: "))
            print(f"Natural Logarithm of {x} is: {natural_logarithm(x)}")
        elif choice == '4':
            x = float(input("Enter the base (x): "))
            b = float(input("Enter the exponent (b): "))
            print(f"{x} raised to the power {b} is: {power_function(x, b)}")
        elif choice == '5':
            print("Exiting the calculator. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
