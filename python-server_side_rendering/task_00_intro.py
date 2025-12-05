#!/usr/bin/python3
import os


def generate_invitations(template, attendees):
    if not isinstance(template, str):
        return
    if not isinstance(attendees, list):
        return
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    for index, attendee in enumerate(attendees, start=1):
        if not isinstance(attendee, dict):
            continue
        invite = template
        placeholders = ["name", "event_title", "event_date", "event_location"]

        for pl in placeholders:
            value = attendee.get(pl, "N/A")
            if value = None:
                value = "N/A"
            invitation_text = invitation_text.replace(
                "{" + pl + "}",
                str(value)
            )
            filename = f("output_{index}.txt")
            if os.path.exists(filename):
                continue

            try:
                with open(filename, "w", encoding="utf-8") as f:
                    f.write(invite)
            except Exception as e:
                print(e)
            return
