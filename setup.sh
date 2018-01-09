#!/bin/bash

# Prompts for username:
echo "Creating script crontabs for Root."
echo "**A non-Sudo User must be created before using this script.**"
echo "============================================================="
read -p 'Username (Do Not Enter Root): ' uservar

# Create folder in user director for auth-logs to copy to
# Remove 
#rmdir ~/auth-log
mkdir ~/Record-Auth-Log/auth-log

# Below is for the Record-Auth-Log Scripts
# Create cron file for cp auth.log
crontab -l > cpauthcron

# Crontab to chmod the auth.log directory periodically
echo "0 * * * * chmod -R 777 /home/${uservar}/Record-Auth-Log/auth-logs" >> cpauthcron

# Crontab to execute the copy-log.py script
echo "59 23 * * * cd /home/${uservar}/Record-Auth-Log/script/copy-log.py &&  /usr/bin/python /home/${uservar}/Record-Auth-Log/script/copy-log.py" >> cpauthcron

# Install new cron file in crontab
sudo crontab cpauthcron
rm cpauthcron
