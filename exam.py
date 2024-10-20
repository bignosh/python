working_days = int(input("Enter number of days your were present: "))
absent_days = int(input("Enter number of days your were absent: "))
present_days = working_days - absent_days

attendance = (present_days / working_days) * 100

if attendance < 75:
    medical = input("Do you have a medical condition? ")
    if medical == "yes":
        print("Eligible for exam")
    else:
        print("Not eligible for exam")
else:
    print("Eligible for exam")
