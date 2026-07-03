# 5] to check if its a leap year

year = int(input("Enter Year:"))

if year % 400 == 0:
    print(year, "is  a Leap Year")
elif year % 100 == 0:
    print(year, " is NOT a Leap Year")
elif year % 4 == 0:
    print(year, " is A Leap Year")
else:
    print(year, "Not a Leap Year")

# print(f"{year} is not a Leap Year")
