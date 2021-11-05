# datetime is better choice than time module
from datetime import datetime, timezone

import pytz as pytz
from termcolor import colored

now = datetime(2020, 8, 27, 10, 13, 4)
now_utc = now.replace(tzinfo=timezone.utc)
now_local = now_utc.astimezone()
print(colored(f'now_local: {now_local}', 'green'))
print(colored(f'now_utc: {now_utc}', 'green'))


def use_pytz_eastern_to_korea():
    arrival_sfo = '2020-08-28 04:13:04.123'
    time_format = '%Y-%m-%d %H:%M:%S.%f'
    sfo_dt_naive = datetime.strptime(arrival_sfo, time_format)  # naive object: not include exact timezone information
    # strptime return datetime object, strftime return string
    eastern = pytz.timezone('US/Pacific')
    sfo_dt = eastern.localize(sfo_dt_naive)  # sfo means San Francisco
    utc_dt = pytz.utc.normalize(sfo_dt.astimezone(pytz.utc))
    print(colored(f'utc: {utc_dt}', 'green'))

    korea = pytz.timezone('Asia/Seoul')
    korea_dt = korea.normalize(utc_dt.astimezone(korea))
    print(colored(f'korea: {korea_dt}', 'green'))

    nepal = pytz.timezone('Asia/Katmandu')
    nepal_dt = nepal.normalize(utc_dt.astimezone(nepal))
    print(colored(f'nepal: {nepal_dt}', 'green'))


if __name__ == '__main__':
    use_pytz_eastern_to_korea()
