import time
print(time.gmtime(0))
print(time.localtime())
print(time.time())


time_here = time.localtime()
# output is named tuple, since the put put is
# time.struct_time(tm_year=2021, tm_mon=9, tm_mday=17, tm_hour=15,
# tm_min=35, tm_sec=26, tm_wday=4, tm_yday=260, tm_isdst=1)
# since we can access the values by position or name, rather easy
print(time_here)

print("Year: ", time_here[0], 'or the output will be same from named tuple',
      time_here.tm_year)
print("month: ", time_here[1], 'or the output will be same from named tuple',
      time_here.tm_mon)
print("day: ", time_here[2], 'or the output will be same from named tuple',
      time_here.tm_mday)
