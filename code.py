name = input('Please enter your name here: ')
dob = input ('Please enter your month of birth, in the format Month year (Ex: February 1900): ')
dob = dob.split(" ")
month = str(dob[0])
try:
    year = int(dob[1])
    year = 2026-year
    if (month == 'January'):
        pass
    elif (month == 'February'):
        pass
    elif (month == 'March'):
        pass
    elif (month == 'April'):
        pass
    elif (month == 'May'):
        pass
    elif (month == 'June'):
        pass
    elif (month == 'July'):
        pass
    elif (month == 'August'):
        pass
    elif (month == 'September'):
        pass
    elif (month == 'October'):
        year = year - 1
    elif (month == 'November'):
        year = year - 1
    elif (month == 'December'):
        year = year - 1
    else:
        print('Invalid month')
    if (year < 0):
        print("This was written in October, 2026, so during that time, you weren't... born yet?")
    elif (year < 1):
        print("This was written in October, 2026, so during that time, you were a few months old.")
    else:
        print('Hello '+name+',This was written in October, 2026, so during that time, you would be about', year, 'years old')
except:
    print("Error, please try again")
