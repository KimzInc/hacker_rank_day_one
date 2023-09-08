"""
Task
Given an integer, n, perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of  to , print Not Weird
If n is even and in the inclusive range of  to , print Weird
If n is even and greater than , print Not Weird
Input Format

A single line containing a positive integer, n.

Constraints
1<=n<=100
Output Format

Print Weird if the number is weird. Otherwise, print Not Weird.
"""


def check_number(num):
    if (n % 2) != 0:
        print("Weird")
    elif ((n % 2) == 0) and (2 <= n <= 5):
        print("Not Weird")
    elif ((n % 2) == 0) and (6 <= n <= 20):
        print("Weird")
    elif ((n % 2) == 0) and (n > 20):
        print("Not Weird")


n = int(input().strip())
check_number(n)

# if __name__ == '__main__':
#     n = int(input().strip())
#     check_number(n)
