import re
import sys
#12 -> 24
# $ python working.py
# Hours: 9:00 AM to 5:00 PM
# 09:00 to 17:00
# $ python working.py
# Hours: 9 AM to 5 PM
# 09:00 to 17:00
# $ python working.py
# Hours: 9 AM to 5:30 PM
# 09:00 to 17:30
# $
# 12am -- > 00:00
#12pm --> 12:00
def main():
    time = input("Hours: ").strip()
    print(convert(time))


def convert(s):
    if matches := re.search(r"^(([1][0-2])|([0-9]))(:[0-5][0-9])? (AM|PM) (?:to )?(([1][0-2])|([0-9]))(:[0-5][0-9])? (AM|PM)$", s):
        if matches.group(5) == "AM":
            if matches.group(4):
                if len(matches.group(1)) == 1:
                    x = "0" + matches.group(1) + matches.group(4)
                elif matches.group(1) == "12":
                    x = "00" + matches.group(4)
                else:
                    x = matches.group(1) + matches.group(4)
            else:
                if len(matches.group(1)) == 1:
                    x = "0" + matches.group(1) + ":00"
                elif matches.group(1) == "12":
                    x = "00:00"
                else:
                    x = matches.group(1) + ":00"

        elif matches.group(5) == "PM":
            if matches.group(4):
                if matches.group(1) == "12":
                    x = matches.group(1) + matches.group(4)
                else:
                    x = str(int(matches.group(1))+ 12) + matches.group(4)
            else:
                if matches.group(1) == "12":
                    x = matches.group(1) + ":00"
                else:
                    x = str(int(matches.group(1))+ 12) + ":00"

        if matches.group(10) == "AM":
            if matches.group(9):
                if len(matches.group(6)) == 1:
                    y = "0" + matches.group(6) + matches.group(9)
                elif matches.group(6) == "12":
                    y = "00" + matches.group(9)
                else:
                    y = matches.group(6) + matches.group(9)
            else:
                if len(matches.group(6)) == 1:
                    y = "0" + matches.group(6) + ":00"
                elif matches.group(6) == "12":
                    y = "00:00"
                else:
                    y = matches.group(6) + ":00"

        elif matches.group(10) == "PM":
            if matches.group(9):
                if matches.group(6) == "12":
                    y = matches.group(6) + matches.group(9)
                else:
                    y = str(int(matches.group(6))+ 12) + matches.group(9)
            else:
                if matches.group(6) == "12":
                    y = matches.group(6) + ":00"
                else:
                    y = str(int(matches.group(6))+ 12) + ":00"

        return (x + " to " + y)
    else:
        raise ValueError

if __name__ == "__main__":
    main()