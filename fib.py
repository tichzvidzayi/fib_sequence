if __name__ == '__main__':

    def fib_sequence(n):
        fib_arr = [0, 1]  # Declare an array with the first 2 elements
        for i in range(2, n+1):  # Loop from range 2 up to n
            # Append fib_numbers to array
            fib_arr.append(fib_arr[-1] + fib_arr[-2])
        return fib_arr

    n = int(input("Enter the number of fib sequence : ") or "10")
    print(fib_sequence(n))

# Another approach is to use recursion but it calculates te previous number more than once
#
