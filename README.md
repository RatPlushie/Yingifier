# Yingifier
A simple Python script to watch your Telegram account and translate what you post into "Yinglish".

### Prerequisites
- PIP
	- telethon
	- python-decouple
- You will also have to create your own .env in the working directory with the following fields:
    ```
    api_id=
    api_hash=
    phonenum_to_watch=
    debug_mode=False
    ```
You can fill out this form (https://my.telegram.org/apps) to get the information for the .env file

### How to run
1. Execute main.py
2. If first time running the script you will be prompted to login to your Telegram account via the CLI
3. Type in any chat/channel and your messages will be edited into proper Yinglish