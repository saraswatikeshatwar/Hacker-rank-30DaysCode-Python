# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())
for i in range(0,T):
    S = input()
    odd = S[1::2]
    even = S[0::2]
    print(even,odd)
