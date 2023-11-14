import csv
import pyperclip as clip
import pandas as pd

df = pd.read_csv("in.csv")

for i, row in df.iterrows():
    clip.copy(row.loc["OU Email"])
    input("Done with address?")

    with open("template.html", "r") as template:
        email = template.read()

        signups = row[5:12].dropna()

        schedule = ""

        for event in signups.index.to_list():
            schedule = schedule + (event + "\n")
            for time in signups[event].split(";"):
                schedule = schedule + (time + "\n")
            schedule = schedule + ("\n")

    clip.copy(email.format(schedule=schedule, instructions=None))
    input("Done with sent?")
    print("----------")
