import sys

"""Simple example: greet and compute factorial."""

def factorial(n: int) -> int:
    """Return n! for non-negative integer n."""
    if n < 0:
        raise ValueError("n must be >= 0")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def main() -> None:
    print("Hello from a simple Python script.")
    try:
        s = input("Enter a non-negative integer (or press Enter to exit): ").strip()
        if not s:
            print("Goodbye.")
            return
        n = int(s)
        print(f"{n}! = {factorial(n)}")
    except ValueError as e:
        print("Invalid input:", e)
        sys.exit(1)

if __name__ == "__main__":
    main()