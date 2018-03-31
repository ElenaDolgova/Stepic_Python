def recursion(n,k):
     if k==0:
         return 1
     elif k>n:
         return 0
     else:
         return recursion(n-1,k)+recursion(n-1,k-1)

n, k = map(int, input().split())
q=input().split(" ")
print(recursion(int(q[0]),int(q[1])))