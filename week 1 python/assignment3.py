def is_even(number):
    """Returns True if the number is even, False otherwise."""
    return number % 2 == 0

def is_prime(number):
    """Returns True if the number is prime, False otherwise."""
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

# Example Usage
test_num = 29
print(f"Number: {test_num}")
print(f"Is Even? {is_even(test_num)} (So it is {'Even' if is_even(test_num) else 'Odd'})")
print(f"Is Prime? {is_prime(test_num)}")