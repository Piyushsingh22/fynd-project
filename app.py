from flask import Flask, render_template, request
import csv
import pandas as pd
import matplotlib.pyplot as plt
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/day", methods=['GET', 'POST'])
def day():
    ans = ""

    if request.method == 'POST':
        user_name = request.form.get('user_name')
        check_date = request.form.get('check_date')
        # print(user_name)
        # print(check_date)

        count = 0
        with open("Attend_data.csv", "r") as csvfile:
            csv_reader = csv.DictReader(csvfile)
            date_present = [row['date'].split(",")[0] for row in csv_reader]

            for check in range(len(date_present)):
                if check_date == date_present[check]:
                    ans = f"{user_name} was present on {check_date}"
                if check_date != date_present[check]:
                    count += 1
                    if count == len(date_present):
                        ans = f"{user_name} was absent on {check_date}"

    return render_template("day.html",ans=ans)


@app.route("/week", methods=['GET', 'POST'])
def week():
    present_count = 0

    if request.method == 'POST':
        user_name_week = request.form.get('user_name_week')
        week_start = request.form.get("week_start")
        week_end = request.form.get("week_end")
        workdays_week = request.form.get("workdays_week")
        # print(workdays_week)


        df = pd.read_csv("Attend_data.csv")
        # df = pd.DataFrame()
        df['date'] = pd.to_datetime(df['date'], format="%Y-%m-%d")
        start_date_conv = datetime.datetime.strptime(week_start, "%Y-%m-%d")
        end_date_conv = datetime.datetime.strptime(week_end, "%Y-%m-%d")
        delta = datetime.timedelta(days=1)
        # print(dfr['date'][0])

        for n in range(len(df['date'])):
            while start_date_conv < df['date'][n]:
                start_date_conv += delta

            if start_date_conv == df['date'][n]:
                present_count += 1
                start_date_conv += delta
                if end_date_conv == df['date'][n]:
                    break

        print("\nNo. of days present in a week: ", present_count)
        print("Total no. of working days: ", workdays_week)

        # creating pie chart
        workdays_wk = int(workdays_week)
        data = [present_count, workdays_wk - present_count]
        # print(data[1])

        labels = ["Present", "Absent"]
        explode = [0.2, 0]

        fig = plt.subplots(figsize=(10, 7))
        plt.pie(data, labels=labels, explode=explode, shadow=True, autopct='%1.1f%%')
        # plt.show()
        plt.legend()
        plt.title(f"{user_name_week}'s weekly attendance report")
        plt.savefig(f'/home/piyush/PycharmProjects/Finalproject/fynd-project/Attendance_Stats/{user_name_week}week.png',
                    bbox_inches='tight')

    return render_template("week.html")

@app.route("/month", methods=['GET', 'POST'])
def month():
   pass


if __name__ == "__main__":
    app.run(debug=True)