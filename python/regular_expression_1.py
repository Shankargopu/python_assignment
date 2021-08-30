
import datetime

def monthcheck(month):
        if month > 0 and month <= 12: 
            return True
        else:
            return False
def daycheck(month,day):
    monthlist1 = [1,3,5,7,8,10,12]
    monthlist2 = [4,6,9,11]
    monthlist3 = 2 

    for mon in monthlist1: 
        if month == mon: 
            if day >=1 and day <= 31:
                return True
            else:
                return False

    for mon in monthlist2: 
        if month == mon: 
            if day >= 1 and day <= 30: 
                return True
            else:
                return False

    if month == monthlist3: 
        if day >=1 and day <= 28: 
            return True
        else:
            return False



def yearcheck(year):
    if len(year) >= 1 and len(year) <= 4:
        return True
    else:
        return False


def main():
    date = str(input("Enter the date in mm/dd/yyyy format: "))

    month,day,year = date.split("/")

    monthvalidity = monthcheck(int(month)) 

    dayvalidity = daycheck(int(month),int(day)) 

    yearvalidity = yearcheck(year) 

    if monthvalidity == True and dayvalidity == True and yearvalidity == True:
        d=datetime.datetime.strptime(month,"%m")
        full_month_name = d.strftime("%B")
        print(full_month_name,end="")
        print(day,year)
    else:
        print("The date {0} is invalid.".format(date))

main()
