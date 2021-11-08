import datetime
import pandas as pd
import csv
import matplotlib.pyplot as plt


class Student:
    def view_studata(self, stuid, checkdate):
        count = 0
        with open("Attend_data.csv", "r") as csvfile:
            csv_reader = csv.DictReader(csvfile)
            date_present = [row['date'].split(",")[0] for row in csv_reader]

            for check in range(len(date_present)):
                if checkdate == date_present[check]:
                    print(f"{stuid} was present on {checkdate}")
                if checkdate != date_present[check]:
                    count += 1
                    if count == len(date_present):
                        print(f"{stuid} was absent on {checkdate}")

    def week_attendance(self, startdate, enddate, working_days, user_name):
        present_count = 0
        df = pd.read_csv("Attend_data.csv")
        # df = pd.DataFrame()
        df['date'] = pd.to_datetime(df['date'], format="%Y-%m-%d")
        start_date_conv = datetime.datetime.strptime(startdate, "%Y-%m-%d")
        end_date_conv = datetime.datetime.strptime(enddate, "%Y-%m-%d")
        delta = datetime.timedelta(days=1)
        # print(dfr['date'][0])


        for name in range(len(df['user_name'])):
            if df['user_name'][name] == user_name:
                # for n in range(len(df['date'])):
                while start_date_conv < df['date'][name]:
                    start_date_conv += delta

                if start_date_conv == df['date'][name]:
                    if end_date_conv <= df['date'][name]:
                        break
                    else:
                        present_count += 1
                        start_date_conv += delta

        print("\nNo. of days present in a week: ", present_count)
        print("Total no. of working days: ", working_days)

        # creating pie chart
        data = [present_count, working_days - present_count]
        # print(data[1])

        labels = ["Present", "Absent"]
        explode = [0.2, 0]

        fig = plt.subplots(figsize=(10, 7))
        plt.pie(data, labels=labels, explode=explode, shadow=True, autopct='%1.1f%%')
        # plt.show()
        plt.legend()
        plt.title(f"{user_name}'s weekly attendance report")
        plt.savefig(rf'/home/piyush/PycharmProjects/Finalproject/fynd-project/Attendance_Stats/{user_name}week.png', bbox_inches='tight')

    def month_attendance(self, monthstart, month_end, working_days_mon, user_name):
        monthly_pre_count = 0
        df = pd.read_csv("Attend_data.csv")
        # df = pd.DataFrame()
        df['date'] = pd.to_datetime(df['date'], format="%Y-%m-%d")
        start_date_mon = datetime.datetime.strptime(monthstart, "%Y-%m-%d")
        end_date_mon = datetime.datetime.strptime(month_end, "%Y-%m-%d")
        delta = datetime.timedelta(days=1)
        # print(dfr['date'][0])

        for name in range(len(df['user_name'])):
            if df['user_name'][name] == user_name:
                # for n in range(len(df['date'])):
                while start_date_mon < df['date'][name]:
                    start_date_mon += delta

                if start_date_mon == df['date'][name]:
                    monthly_pre_count += 1
                    start_date_mon += delta
                    if end_date_mon <= df['date'][name]:
                        break

        print("\nNo. of days present in a month: ", monthly_pre_count)
        print("Total no. of working days: ", working_days_mon)

        #creating pie chart
        data = [monthly_pre_count, working_days_mon - monthly_pre_count]
        labels = ["Present", "Absent"]
        explode = [0.2, 0]

        fig = plt.subplots(figsize=(10, 7))
        plt.pie(data, labels=labels, explode=explode, shadow=True, autopct='%1.1f%%')
        # plt.show()
        plt.legend()
        plt.title(f"{user_name}'s monthly attendance report")
        plt.savefig(rf'/home/piyush/PycharmProjects/Finalproject/fynd-project/Attendance_Stats/{user_name}month.png', bbox_inches='tight')


objStudent = Student()
run = True
print("Welcome to Attendance Report and Analytics")
while run:
    print("\n1. View Student Report on a particular day")
    print("2. View Student Report in a particular week")
    print("3. View Student Report for a particular month")
    print("4. Quit\n")
    response = input("Please enter your response: ")

    while True:
        if response == "1":
            stu_id = input("Please enter user name: ")
            check_date = input("Please enter date in YYYY-MM-DD format: ")
            objStudent.view_studata(stu_id, check_date)
            while True:
                see_more = input("\nWant to see details again?\nans(y/n): ").lower()
                if see_more == "y" or see_more == "n":
                    break
                else:
                    print("Please enter a valid input: ")
            if see_more == "y":
                continue
            else:
                break

        elif response == "2":
            week_start = input("Please enter week's starting date in YYYY-MM-DD format: ")
            week_end = input("Please enter week's ending date in YYYY-MM-DD format: ")
            working_days = int(input("Please enter no. of working days in a week: "))
            user_name = input("Please enter user name: ")
            objStudent.week_attendance(week_start, week_end, working_days, user_name)
            while True:
                see_more = input("\nWant to see details again?\nans(y/n): ").lower()
                if see_more == "y" or see_more == "n":
                    break
                else:
                    print("Please enter a valid input: ")
            if see_more == "y":
                continue
            else:
                break

        elif response == "3":
            month_start = input("Please enter month's starting date in YYYY-MM-DD format: ")
            month_end = input("Please enter month's ending date in YYYY-MM-DD format: ")
            working_days_mon = int(input("Please enter no. of working days in a month: "))
            user_name = input("Please enter user name: ")
            objStudent.month_attendance(month_start, month_end, working_days_mon, user_name)
            while True:
                see_more = input("\nWant to see details again?\nans(y/n): ").lower()
                if see_more == "y" or see_more == "n":
                    break
                else:
                    print("Please enter a valid input: ")
            if see_more == "y":
                continue
            else:
                break
        elif response == "4":
            run = False
            break

        else:
            print("Please enter a valid input ")
            break
