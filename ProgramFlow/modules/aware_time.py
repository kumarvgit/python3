import datetime
import pytz

local_time = datetime.datetime.now()
utc_time = datetime.datetime.utcnow()

print(f"Naive local time {local_time}")
print(f"Naive utc {utc_time}")

# store with time zone, this is good practice to have utc with time zone
aware_local_time = pytz.utc.localize(utc_time).astimezone()
aware_utc_time = pytz.utc.localize(utc_time).astimezone()

print("Aware local time: {}".format(aware_local_time))
print("Aware utc time: {}".format(aware_utc_time))


gap_time = datetime.datetime(2015, 10, 25, 1, 30, 0, 0)
print(gap_time)
print(gap_time.timestamp())


# UK time for 25 oct, 2015, 1:30 AM
s = 1445733000
t = s + (60 * 60)

gb = pytz.timezone('GB')
dt1 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(s)).astimezone(gb)
dt2 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(t)).astimezone(gb)

print(f"{s} seconds in {dt1}")
print(f"{t} seconds in {dt2}")
