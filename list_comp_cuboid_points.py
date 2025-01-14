# Given three integers x, y, and z to represent dimensions of a cuboid, and a fourth integer n;
# print all possible points (i, j, k) where i+j+k does not equal n and 0<=i<=x, 0<=j<=y, 0<=k<=z.

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    all_perms = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]
    print(all_perms)
