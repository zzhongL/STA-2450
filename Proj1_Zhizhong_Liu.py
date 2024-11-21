# Proj1_lastname_firstname.py

def proper_factors(n):
    """
    This function takes an integer n and returns a list of its proper factors.
    Proper factors are all divisors of n excluding the number itself.

    :param n: Integer whose proper factors need to be found.
    :return: List of proper factors of n.
    """
    factors = [i for i in range(1, n) if n % i == 0]
    return factors


def classify_number(n):
    """
    This function classifies a number as 'abundant', 'deficient', or 'perfect'
    based on the sum of its proper factors.

    :param n: Integer to classify.
    :return: String indicating if the number is 'abundant', 'deficient', or 'perfect'.
    """
    factors_sum = sum(proper_factors(n))
    if factors_sum < n:
        return "deficient"
    elif factors_sum > n:
        return "abundant"
    else:
        return "perfect"


def find_perfect_numbers(limit):
    """
    This function finds and returns a list of perfect numbers less than the given limit.

    :param limit: Integer limit up to which to find perfect numbers.
    :return: List of perfect numbers less than limit.
    """
    perfect_nums = [i for i in range(2, limit) if classify_number(i) == "perfect"]
    if not perfect_nums:
        print(f"There are no perfect numbers less than {limit}.")
    return perfect_nums


# Example implementation
if __name__ == "__main__":
    num = 12  # You can change this value for different examples

    # Testing proper factors function
    print(f"Proper factors of {num}: {proper_factors(num)}")

    # Testing classification function
    classification = classify_number(num)
    print(f"The number {num} is classified as: {classification}")

    # Testing perfect number finder
    limit = 30  # You can adjust the limit to test different ranges
    perfect_nums = find_perfect_numbers(limit)
    if perfect_nums:
        print(f"Perfect numbers less than {limit}: {perfect_nums}")
