# fibonacci series

def fibonacci(n):
    """Generate Fibonacci sequence up to n terms."""
    fib_sequence = [0, 1]  # Initial Fibonacci sequence with first two terms
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])  # Generate next Fibonacci term
    return fib_sequence

def main():
    """Main function to demonstrate Fibonacci sequence generation."""
    n_terms = 10  # Number of Fibonacci terms to generate
    fib_sequence = fibonacci(n_terms)
    print("Fibonacci sequence up to {} terms:".format(n_terms))
    print(fib_sequence)

if __name__ == "__main__":
    main()
