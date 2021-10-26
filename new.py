import datetime
import pandas as pd
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
        # with open("Attend_data.csv", "r") as csvfile:
        #     csv_reader = csv.DictReader(csvfile)
        #
        #     next(csv_reader)
            #date_present2 = [row['date'].split(",")[0] for row in csv_reader]

        df = pd.read_csv("Attend_data.csv")
        # df = pd.DataFrame()
        df['date'] = pd.to_datetime(df['date'], format="%Y-%m-%d")
        start_date_conv = datetime.datetime.strptime(startdate, "%Y-%m-%d")
        end_date_conv = datetime.datetime.strptime(enddate, "%Y-%m-%d")
        delta = datetime.timedelta(days=1)
        # print(dfr['date'][0])

        for n in range(len(df['date'])):
            if start_date_conv == df['date'][n]:
                present_count += 1
                start_date_conv += delta
                if end_date_conv == df['date'][n]:
                    break
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

        # view_more = input("Want to see details again?").lower()
        # if view_more =='y':
        #     continue


        else:
            print("Please enter a valid input")
            break
    break