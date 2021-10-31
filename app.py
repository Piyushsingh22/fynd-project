from flask import Flask, render_template, request
import csv

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
   pass


@app.route("/month", methods=['GET', 'POST'])
def month():
   pass


if __name__ == "__main__":
    app.run(debug=True)