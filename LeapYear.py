def is_leap(year):
    notleap = False
    leap = True
    # Write your logic here
    if year%100==0 and  year%400==0:
        return leap
    elif year%4==0 and year%100!=0:
        return leap
    else:
            return notleap

year = int(input())
print(is_leap(year))