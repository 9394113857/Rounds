# Problem
# Let’s learn about list comprehensions! You are given three integers x, y and z,
# representing the dimensions of a cuboid along with an integer n.
# Print a list of all possible coordinates given by (i, j, k) on a 3D grid
# where the sum of i + j + k is not equal to n.
# Here, 0 <= i <= x; 0 <= j <= y; 0 <= k <= z.
# Please use list comprehensions rather than multiple loops, as a learning exercise.

if __name__ == '__main__':
    x = int(input("Enter x Value: "))
    y = int(input("Enter y Value: "))
    z = int(input("Enter z Value: "))
    n = int(input("Enter n Value: "))
    output = [];
    abc = [];
    for X in range(x+1):
        for Y in range(y+1):
            for Z in range(z+1):
                if X+Y+Z != n:
                    abc = [X,Y,Z];
                    output.append(abc);
print(output);

# https://www.codingbroz.com/list-comprehensions-in-python-solution/





