# Task
# The included code stub will read an integer, n, from STDIN.
#
# Without using any strings methods, try to print the following:
#
# 123……..n
#
# Note that “…..” represents the consecutive values in between.

if __name__ == '__main__':
    n = int(input("Enter Number: "))
    for i in range(1, n + 1):
        print(i, end=" ")

# https://www.codingbroz.com/python-print-function-solution/
