year = input("Enter a year: --> ")
year = int(year)


if year % 400 == 0:
    print("This year is a leap year")
elif year % 100 == 0:
    print("This year is a not a leap year")
elif year % 4 == 0:
    print("This year is a leap year")
else: 
    print("This year is a not a leap year")
