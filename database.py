import pandas
import datetime

def get_df(file_name):
    return pandas.read_csv(file_name)

def get_event_time(Date, Time):
    return datetime.datetime.strptime(Date + " " + Time, "%d/%m/%Y %H:%M")

def simple_event_message(eventID, Time):
    return f"Event: {eventID} at {Time}"

def event_already_added(row, event_json):
    return row["Status"] or row["eventID"] in event_json.keys()

def generate_event(events, file_name="data.csv"):

    df = get_df(file_name)
    for _, row in df.iterrows():

        if event_already_added(row, events):
            continue
        
        Date, Time, eventID, Info = row["Date"], row["Time"], row["eventID"], row["Info"]

        # Extract the event time
        events[eventID] = {
            "event_time":  get_event_time(Date, Time),
            "event_message": simple_event_message(eventID, Time),
            "event_occured": False,
            "event_reminder_time": 0,
            "event_reminder_occured": False,
            "extra_info": Info
        }

    return events

def editcsv_event_occured(event_id, file="data.csv", ):
        
        df = pandas.read_csv(file)
        df.loc[df["eventID"] == event_id, "Status"] = "True"
        df.to_csv(file, index=False)

def write_to_csv(event_id, date, time, info, file="data.csv"):
    df = pandas.read_csv(file)
    new_row = {"eventID": event_id, "Date": date, "Time": time, "Info": info, "Status": False}
    df.loc[len(df)] = new_row
    df.to_csv(file, index=False)