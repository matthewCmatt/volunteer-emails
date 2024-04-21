import csv
import pyperclip as clip
import pandas as pd

df = pd.read_csv("in.csv")

events = pd.read_csv("events.csv", index_col=0)

for i, row in df.iterrows():
    email_address = row.loc["Email Address"]
    clip.copy(email_address)
    input("Done with " + email_address + "?")

    clip.copy("Green Week Volunteer Instructions!")
    input("Done with subject?")

    firstname = row.loc["name "].split(" ")[0].title()
    signups = row[3:13].dropna()

    # Build schedule string
    schedule = "<hr>"
    for event in signups.index.to_list():
        event_data = events.loc[event]

        schedule += "<b>" + event_data.eventName + "</b><br>"

        if event == "Wildcare Rehab Talk! (1pm-3pm Wednesday)":
            schedule += "The Wildcare Talk has been dropped from this years schedule :(<br>"
            continue

        schedule += str(event_data.date) + " " + str(event_data.locationPhrase) + "<br>"
        schedule += "Total Runtime: " + event_data.time + "<br>"
        schedule += "Your volunteer times:<br><ul>"
        for time in signups[event].split(","):
            if (time):
                schedule += "<li>" + time.strip() + "</li>"
        schedule += "</ul>"
        schedule += "<u>Instructions:</u> " + str(event_data.instructions) + "<br><hr>"

    with open("template.html", "r") as template:
        email = template.read()

    clip.copy(email.format(firstname=firstname, schedule=schedule))
    input("Done with sent?")
    print("----------")
