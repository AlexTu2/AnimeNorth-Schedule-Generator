import pprint
import json
import os
from icalendar import Calendar, Event
from datetime import datetime
from dateutil.parser import parse
from tzlocal import get_localzone
from dateutil.tz import gettz, tzutc


if __name__ == '__main__':
    datetime.now()
    with open('data.json') as file:
        anime_north_data = json.load(file)

    with open('selections.json') as file:
        selections = json.load(file)['self_registrations']

    events = {}
    guidebook_location = {}

    for i in anime_north_data["guidebook_location"]:
        guidebook_location[i["id"]] = i["name"]

    for i in anime_north_data["guidebook_event"]:
        events[i["id"]] = {
            "start_time": i["startTime"],
            "end_time": i["endTime"],
            "description": i["description"].replace("<p>", "").replace("</p>", "").replace("</blockquote>", "\"").replace("<blockquote>", "\"").strip(),
            "name": i["name"],
            "location": guidebook_location[int(i["locations"])]
        }

    local_tz = get_localzone()

    cal = Calendar()
    cal['summary'] = "Anime North"
    cal['description'] = "Anime North schedule generator from Guidebooks"
    cal['version'] = '2.0'

    for id in selections:
        event = events[id]

        calendar_event = Event()

        calendar_event['summary'] = event['name']
        calendar_event['description'] = event['description']
        calendar_event['uid'] = id
        calendar_event['location'] = event['location']

        start_date = parse(event['start_time']).replace(tzinfo=local_tz).astimezone(tzutc())
        end_date = parse(event['end_time']).replace(tzinfo=local_tz).astimezone(tzutc())

        calendar_event['dtstart'] = start_date.strftime("%Y%m%dT%H%M%SZ")
        calendar_event['dtend'] = end_date.strftime("%Y%m%dT%H%M%SZ")
        calendar_event['dtstamp'] = datetime.now().astimezone(tzutc()).strftime("%Y%m%dT%H%M%SZ")
        
        cal.add_component(calendar_event)

    with open('calendar.ics', 'wb') as file:
        file.write(cal.to_ical())
