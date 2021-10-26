import datetime
import pdb
import csv


class Student:
    def view_studata(self, stuid, checkdate):
        count = 0
        with open("Attend_data.csv", "r") as csvfile:
            csv_reader = csv.DictReader(csvfile)
            next(csv_reader) # skips the first row
            date_present = [row['date'].split(",")[0] for row in csv_reader]


            for check in range(len(date_present)):
                if checkdate == date_present[check]:
                    print(f"{stuid} is present on {checkdate}")
                if checkdate != date_present[check]:
                    count +=1
                    if count == len(date_present):
                        print(f"{stuid} is absent on {checkdate}")

    def week_attendance(self, startdate, enddate):
        present_count = 0
        with open("Attend_data.csv", "r") as csvfile:
            csv_reader = csv.DictReader(csvfile)

            next(csv_reader)
            date_present2 = [row['date'].split(",")[0] for row in csv_reader]

            start_date_conv = datetime.datetime.strptime(startdate, "%Y-%m-%d")
            end_date_conv = datetime.datetime.strptime(enddate, "%Y-%m-%d")
            delta = datetime.timedelta(days=1)
            # pdb.set_trace()
            for n in range(int((end_date_conv - start_date_conv).days)):
                if startdate == date_present2[n]:
                    present_count += 1
                    startdate += delta
                print(present_count)











objStudent = Student()
print("Welcome to Attendance Report and Analytics")
while True:
    print("1. View Student Report on a particular day")
    print("2. View Student Report in a particular week")
    print("3. View Student Report for a particular month")
    response = input("Please enter your response: ")

    while True:
        if response == "1":
            stu_id = input("Please enter user name: ")
            check_date = input("Please enter date in YYYY-MM-DD format: ")
            objStudent.view_studata(stu_id, check_date)
            # objStudent.view_studata()

        if response == "2":
            week_start = input("Please enter week's starting date in YYYY-MM-DD format: ")
            week_end = input("Please enter week's ending date in YYYY-MM-DD format: ")
            objStudent.week_attendance(week_start, week_end)

        else:
            print("Please enter a valid input")
            break
    break