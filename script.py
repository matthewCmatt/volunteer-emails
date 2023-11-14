import csv
import pyperclip as clip
import pandas as pd

df = pd.read_csv("in.csv")

events = pd.read_csv("events.csv", index_col=0)

for i, row in df.iterrows():
    clip.copy(row.loc["OU Email"])
    input("Done with address?")

    clip.copy("Green Weekend Volunteer Instructions!")
    input("Done with subject?")

    with open("template.html", "r") as template:
        email = template.read()

        signups = row[5:12].dropna()

        # Build schedule string
        schedule = "<hr>"
        for event in signups.index.to_list():
            event_data = events.loc[event]

            schedule = schedule + ("<b>" + event_data.eventName + "</b><br>")
            schedule = schedule + (
                str(event_data.date) + " at " + str(event_data.location) + "<br>"
            )
            schedule = schedule + ("Total Runtime: " + event_data.time + "<br>")
            if event == "Sunset Zumba (7:00pm - 7:45pm)":
                schedule = (
                    schedule
                    + "<br>NOTE: This event has been reschedule from our original sign-up times. You indicated that you could attend, so please reply or message @Matt in Slack if you are STILL able to come :)"
                )
            else:
                schedule = schedule + "<ul>"
                for time in signups[event].split(";"):
                    schedule = schedule + ("<li>" + time + "</li>")
                schedule = schedule + "</ul>"
            schedule = (
                schedule
                + "<u>Instructions:</u> "
                + event_data.instructions
                + "<br><hr>"
            )

    clip.copy(email.format(schedule=schedule))
    input("Done with sent?")
    print("----------")
