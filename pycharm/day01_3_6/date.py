months = ["Jan",
          "Feb",
          "Mar",
          "Apr",
          "May",
          "June",
          "July",
          "Aug",
          "Sept",
          "Oct",
          "Nov",
          "Dec"]
ending = ["st","nd","rd"] + 17*["th"] + ["st","nd","rd"] + 7*["th"] + ["st"]
year = input("enter year:")
month = input("enter month:")
day = input("enter day:")

month_number = int(month)
day_number = int(day)

result = months[month_number-1] + ' ' + day + ending[day_number-1] \
    + ', ' + year
print(result)