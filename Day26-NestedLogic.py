# Enter your code here. Read input from STDIN. Print output to STDOUT
actual = str(input()).split(" ")
day = int(actual[0])
month = int(actual[1])
year = int(actual[2])

expected = str(input()).split(" ")
day1 = int(expected[0])
month1 = int(expected[1])
year1 = int(expected[2])

fine = 0
if year > year1 :
    fine = 10000
elif year == year1:
    if month > month1:
        fine = (month - month1) * 500
    elif month == month1 and day > day1:
        fine = (day - day1) * 15

print(fine)

