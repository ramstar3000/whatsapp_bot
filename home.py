from flask import Flask, render_template, request, redirect, url_for
from database import write_to_csv
import datetime
from base import generate_response_gpt
app = Flask(__name__)

from database import generate_event, editcsv_event_occured


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        print(request.form)
        
        event_id = request.form["EventID"]
        date = request.form["EventDate"]
        time = request.form["EventTime"]
        info = request.form["Extra Info"]
        recur = request.form["Repetitions"]

        # Reformat the date from '2023-09-16' to '%d/%m/%Y'
        date = date.split("-")
        date = f"{date[2]}/{date[1]}/{date[0]}"

        # If already happened, do not add
        if datetime.datetime.now() > datetime.datetime.strptime(date + " " + time, "%d/%m/%Y %H:%M"):
            return redirect(url_for("home"))
        
        if event_id == "":
            event_id = generate_response_gpt(f"Can you suggest a name for the event? for event {info} {recur}. Return a single word", blank=True)
        
        if recur not in ["Never", "Weekly", "Monthly"]:
            # Get gpt to suggest a recurrence
            recur = generate_response_gpt(f"Can you suggest a recurrence for the event? for event {event_id}. Return one of the following: Never, Weekly, Monthly. We have been told {recur} and {info}", blank=True)



        if recur == "Never":
            write_to_csv(event_id, date, time, info)
        elif recur == "Weekly":
            for i in range(1, 3):
                newdate = datetime.datetime.strptime(date, "%d/%m/%Y") + datetime.timedelta(weeks=i)
                newdate = newdate.strftime("%d/%m/%Y")
                write_to_csv(event_id + f"_{i}", newdate, time, info)
        elif recur == "Monthly":
            for i in range(1, 3):
                newdate = datetime.datetime.strptime(date, "%d/%m/%Y") + datetime.timedelta(weeks=i*4)
                newdate = newdate.strftime("%d/%m/%Y")
                write_to_csv(event_id + f"_{i}", newdate, time, info)


        return redirect(url_for("home"))
    else:
        events = generate_event({})


        # Sort the events by time and take top 5
        events = sorted(events.items(), key=lambda x: x[1]["event_time"])[:3]

        # Make the datetime into a string
        for i in range(len(events)):
            if isinstance(events[i][1]["event_time"], datetime.datetime):
                a = events[i][1]["event_time"].strftime("%d/%m/%Y %H:%M")
            else:
                a = 0
            events[i] = (events[i][0], events[i][1]["event_time"].strftime("%d/%m/%Y %H:%M"), events[i][1]["extra_info"], events[i][1]["event_message"], a)

        return render_template("base.html", events=events, l = len(events))

@app.route("/allevents", methods=["GET"])
def allevents():
    events = generate_event({})
    events = sorted(events.items(), key=lambda x: x[1]["event_time"])

    for i in range(len(events)):
        if isinstance(events[i][1]["event_reminder_time"], datetime.datetime):
            a = events[i][1]["event_reminder_time"].strftime("%d/%m/%Y %H:%M")
        else:
            a = 0
        events[i] = (events[i][0], events[i][1]["event_time"].strftime("%d/%m/%Y %H:%M"), events[i][1]["extra_info"], events[i][1]["event_message"], a)

    print(events)

    return render_template("allevents.html", events=events, l = len(events))



if __name__ == "__main__":
    app.run(debug=True)
