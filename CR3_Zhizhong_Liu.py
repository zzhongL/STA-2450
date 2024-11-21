#Assignment:Code Reading 3
#Student Name:Zhizhong Liu

def fib(x):
    """
    Calculate the Fibonacci number for a given position x

    This fib function uses the num_fib_calls variable as a counter to keep track of the number
    of times the function is called. It increments time the function is using.
    The Fibonacci sequence is defined as:

    - fib(0) = 1
    - fib(1) = 1
    - fib(n) = fib(n-1) + fib(n-2) for n > 1

    Parameters:
    x (int): The position in the Fibonacci sequence.

    Returns:
    int: The Fibonacci number at position x.
    """
    global num_fib_calls
    num_fib_calls += 1
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x - 1) + fib(x - 2)


def test_fib(n):
    """
    The test_fib function test the fib function by calculating Fibonacci numbers from 0 to n

    This function iterates over all positions in the Fibonacci sequence from 0 to n,
    and for each position, it set the num_fib_calls to 0. It then uses the fib function
    to calculate the Fibonacci number and prints the result and the number of times
    the fib function was called.

    Parameters:
    n (int): The highest position in the Fibonacci sequence
    """
    for i in range(n + 1):
        global num_fib_calls
        num_fib_calls = 0
        print('fib of', i, '=', fib(i))
        print('fib called', num_fib_calls, 'times.')

    """
    In general, these two functions use recursive programming ideas to create the Fibonacci sequence
    and test it.
    """