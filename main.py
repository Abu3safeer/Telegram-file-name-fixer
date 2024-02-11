import json
from pathlib import Path


# Get all files in the current directory
get_all_files = Path().glob('*')
files = []

for file in get_all_files:
    if file.is_file():
        files.append(file)

# Load Telegram file list from exported json with TDL with content
loag_tg = open('telegram_files.json', 'r')
telegram_files = json.load(loag_tg)['messages']
loag_tg.close()


# Fix names process
def fix_names():
    for file in files:
        current_file_name = file.name
        for telegram_file in telegram_files:
            telegram_file_name = telegram_file['file']
            telegram_file_text = telegram_file['text']
            if telegram_file_name in current_file_name:
                file.rename(current_file_name.replace(telegram_file_name, telegram_file_text))


if __name__ == '__main__':
    fix_names()
