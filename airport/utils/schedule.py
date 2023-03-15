import schedule
import time

from ..views import update_airport


def schedule_airpots():
    update_airport()


# schedule.every().day.at('05:00').do(update_airport)
# schedule.every(5).seconds.do(update_airport)
schedule.every(5).seconds.do(schedule_airpots)

while 1:
    schedule.run_pending()
    time.sleep(1)
