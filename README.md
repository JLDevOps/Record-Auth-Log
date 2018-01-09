# Automate Recording Auth Logs

A script to automate the recording of the auth.log files onto a user's directory.

The script utilizes a text file to keep track of the amount of days that have passed before executing the recording of tthe auth.log.  Each recorded auth.log file is appended with datetime (i.e. DD-MM-YYYY).

(Special Note): This script only works on Linux, and is intended for servers.

## Getting Started

These instructions will get you a copy of the project up and running on your server or linux box.

### Prerequisites
A list of packages and software needed to be installed before testing:
1. Python 2
2. Linux

### Setting Up the Environment

After cloning or downloading the project on your own server or Linux computer:

Go into the **Record-Auth-Log**.
```
cd Record-Auth-Log
```
Then run the setup.sh via command:
```
./setup.sh
```
(If the command fails, then do:)
```
chmod +x setup.sh
```
As the script setups, the setup.sh will ask for:
1. Username
2. Password for Sudo.

Once complete, two cronjobs have been added for your Root user.
1. Chmod the auth-log folder on your user's directory (not var/log/)
2. Execute the copy-log.py file everyday at 11:59PM

## Usage
Run the project, only after following the setup guide.

### Automated Execution

The crontabs from the setup guide will automatically run copy-log.py at 11:59PM each day without any interaction needed. 

### Manual Execution

If you wanted to run the script for testing or development:

Go into the **script** directory:
``` 
cd script
```

Then run the script via:
```
python copy-log.py
```

