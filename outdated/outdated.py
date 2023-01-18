months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date = input("Date: ")
        month, day, year = date.split("/")
        if(1<=int(month)<=12) and (1<=int(day)<=31):
            print(f"{year.strip()}-{int(month):02}-{int(day):02}")
            break
        #September 8, 1636
    except:
        try:
            new_month, new_day, new_year = date.split(" ")
            new_day = new_day.replace("," , "")
            new_month = months.index(new_month) + 1
            if(1<=int(new_month)<=12) and (1<=int(new_day)<=31 and "," in date):
                print(f"{new_year.strip()}-{int(new_month):02}-{int(new_day):02}")
                break
        except:
            pass





