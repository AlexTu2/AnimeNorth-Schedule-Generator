
# Anime North Schedule Generator

A python script that converts the Anime North Guidebooks JSON
 data into an ical file.

## Authors

- [@HenryTwo](https://github.com/henrytwo)
- [@ryanz34](https://github.com/ryanz34)
- [@AlexTu2](https://github.com/AlexTu2)
## Installation 

You will need python 3 installed

Perform the following steps (**in order**):
### 1. Clone the project

  `git clone https://github.com/AlexTu2/AnimeNorth-Schedule-Generator`

### 2. Go to the project directory

  `cd AnimeNorth-Schedule-Generator`

### 3. Create A Virtual Environment

  `pip install virtualenv`

  `python3 -m venv venv`

### 4. Activate the Virtual Environment 

#### On Windows using the Command Prompt: path\to\venv\Scripts\activate.bat
  `venv\Scripts\activate.bat`

#### On Windows using PowerShell: path\to\venv\Scripts\Activate.ps1
  `venv\Scripts\Activate.ps1`

#### On Unix or MacOS, using the bash shell: source /path/to/venv/bin/activate
  `source venv/bin/activate`

### 5. Install the Requirements in `requirements.txt`

  `pip install -r requirements.txt`



## Usage/Examples

### 1. Grab your personal Schedule

1. Go to the Guidebooks Guide for Anime North [here](https://guidebook.com/g/#/guides/animenorth2022) and make sure you're logged in

2. Open up your Web Developer Tools (Inspect Element) with Ctrl + Shift + I 

3. Go to the Networks Tab (Filter by Fetch/XHR)

4. Click on "Schedule" and then "My Schedule"

5. Look for a request from [get-all-registered-sessions](https://builder.guidebook.com/api/cover-page-widgets/pschedule/190888/get-all-registered-sessions/)

6. Copy & paste the response into a selections.json file

*You may need to clear website cache before step 4

### 2. Execute the program in the shell

  `python animenorth.py`


### 3. Using the Calendar file

The program outputs a "Calendar.ics" file which you can import into Google Calendar, Apple iCloud, Outlook Calendar & more

## Notes

The repository provides the Anime North 2022 schedule (data.json).  
To retrieve your own incase it's outdated, perform the following steps (**in order**):

1. Go to the Guidebooks Guide for Anime North [here](https://guidebook.com/g/#/guides/animenorth2022) not required to log in

2. Open up your Web Developer Tools (Inspect Element) with Ctrl + Shift + I 

3. Go to the Networks Tab (Filter by Fetch/XHR)

4. Click on "Schedule"

5. Look for a request from [QJpHdsp1PFyZ1Nkcpe7aVwFXfw6zoW4zFhE6vGtY.json?version=16](https://s3.amazonaws.com/media.guidebook.com/service/guide_bundle_data/QJpHdsp1PFyZ1Nkcpe7aVwFXfw6zoW4zFhE6vGtY.json?version=16) (As of 2022)

6. Copy & paste the response into a data.json file

*You may need to clear website cache before step 4
***