#!/usr/bin/env python3
#!/usr/bin/env python3

# Function 1: Validate and return user input
def get_positive_integer():
    # Prompt the user for a positive integer and validate input.
    while True:
        user_input = input("Enter the number of Fibonacci terms you want: ")
        if user_input.isdigit():
            n = int(user_input)
            if n > 0:
                return n
            else:
                print("Please enter a positive integer.")
        else:
            print("Invalid input, please enter a positive integer.")

# Function 2: Generate Fibonacci sequence
def generate_fibonacci(n):
    """Generate the Fibonacci sequence up to n terms and return as a list."""
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Function 3: Print the sequence
def print_fibonacci(sequence):
    """Print the Fibonacci sequence in a readable format."""
    print(f"Fibonacci sequence up to {len(sequence)} terms:")
    print(" ".join(map(str, sequence)))

# Main program
def main():
    n = get_positive_integer()
    fibonacci_sequence = generate_fibonacci(n)
    print_fibonacci(fibonacci_sequence)

if __name__ == "__main__":
    main()

# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)
