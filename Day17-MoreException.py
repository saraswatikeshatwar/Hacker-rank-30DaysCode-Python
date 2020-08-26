class Calculator:
    def power(self,n,p):
        #check n and p negative if yes then raise exception otherwise return power
        if n<0 or p<0:
            raise Exception("n and p should be non-negative")
        return pow(n,p)


myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)
