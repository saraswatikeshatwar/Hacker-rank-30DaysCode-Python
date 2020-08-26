# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
#take name and phn number from user
name_phnnumbers = [input().split() for _ in range (n)]
#create dictionary
phonebook = {k: v for k,v in name_phnnumbers}
while True:
    try:
        #take name from user to check whether it present in dictionary or not
        name = input()
        if name in phonebook:
            print('%s=%s' %(name,phonebook[name]))
        else:
            print('Not found')
    except:
        break

    
