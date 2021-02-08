
# GITAM-Meetings

GITAM Meetings is a simple python script to automate the login process of the GITAM website to make the students life easier in this pandemic without having the trouble of logging in when there is a timeout for every few minutes by the server. This script comes handy as it helps in retrieving the scheduled zoom meetings links, title, timings and captures them and they can be saved into a .csv file or can be updated into any Discord Server or Telegram bots. 

- This script uses selenium for python to initialize a chrome driver and login using the custom username and password given by the user. 

- After logging in the page is going to be redirected to GLearn page and it will be waiting until 5 min and going to click Attendance page and the process will repeat to make the server feel the user is still using the website without any idle behaviour.

- The meetings feature is automatically initiated once the user is logged in. The data is collected and stored in a .csv file which is later feed into Custom Discord webhook or Telegram bot of your choice.

- Tired of logging in? Integrated discord webhook script. You can receive a Message from your server bot using webhooks.

## Getting Started

### 1. Downloading/Cloning the repo
### Download the repo:
   - Download as a ZIP File:

https://github.com/hariperisetla4431/GITAM-Meetings/archive/main.zip

### Clone the repo:
   - using CLI:
```
git clone https://github.com/hariperisetla4431/GITAM-AutoLogin
```
   - using link:
                 
   https://github.com/hariperisetla4431/GITAM-Meetings
   
### 2. Opening the script
   - The script can be opened by opening the gstudent.exe or gstudent-32.exe files
   - Login in with your username and password
   - You can add your discord server and get notification of all the classes and urls to the meetings whenever you login using the script
   - Depending upon the PC Configuration the cmd files may load slowly
   - If your login is new after you are logged in all the settings are automatically saved to the local save.txt file. In the next login session you may use the previous settings or you can overrite the existing settings
   - To stop the script press ctrl+c

## Issues
   Ran into an issue? No problem! Create a new issue and I will help you!
   
   - https://github.com/hariperisetla4431/GITAM-Meetings/issues
