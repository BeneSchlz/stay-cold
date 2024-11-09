import time
from datetime import datetime
from blocker import start_block

def schedule_block_started(block_name, start_hour = 23, start_minute = 0):
    while True:
        now = datetime.now()
        if now.hour == start_hour and now.minute == start_minute:
            start_block(block_name)
            time.sleep(60*60*24)
        time.sleep(60)

if __name__ == "__main__":
    block_name = "reddit week"
    schedule_block_started(block_name)
