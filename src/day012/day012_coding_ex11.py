# Coding Exercise 11
# Prime Number Checker


def is_prime(number):
    """Return True if number is a prime number, False otherwise."""
    if number < 2:
        return False
    if number % 2 == 0:
        return number == 2
    divisor = 3
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 2
    return True


def main():
    for candidate in (1, 2, 4, 7, 97, 100):
        print(f"{candidate}: {is_prime(candidate)}")


if __name__ == "__main__":
    main()
