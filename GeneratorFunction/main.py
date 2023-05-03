# Python3 program to find all generators

# Function to return gcd of a and b
def gcd(a, b):
    if (a == 0):
        return b;
    return gcd(b % a, a);


# Print generators of n
def printGenerators(n):
    # 1 is always a generator
    print("1", end=" ");

    for i in range(2, n):

        # A number x is generator
        # of GCD is 1
        if (gcd(i, n) == 1):
            print(i, end=" ");


# Driver Code
n = 10;
printGenerators(n);

# This code is contributed by mits

