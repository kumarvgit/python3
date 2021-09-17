# import datetime
# import time
#
# # // zero seconds after epoch
# print('Epoch starts at: ' + time.strftime('%c', time.gmtime(0)))
# print('the current time zone is {0} with an offset of {1} '.format(time.tzname[0], time.timezone))
#
# if time.daylight != 0:
#     print('\t Daylight is in effect')
#     print('\t DST time zone is: ' + time.tzname[1])
#
# print('Local time is ' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
# print('UTC time is ' + time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime()))


# print('*' * 80)


import datetime

print(datetime.datetime.today())
print(datetime.datetime.now())
print(datetime.datetime.utcnow())
