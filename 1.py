num=int(input())
def fun(m):
    return m*(m+1);
for j in range(num):
    x =int(input())
    x -=1;
    p=int(x/3);
    q=int(x/5);
    r=int(x/15);
    print(int(int(3*fun(p) + 5*fun(q) - 15*fun(r))>>1));
    