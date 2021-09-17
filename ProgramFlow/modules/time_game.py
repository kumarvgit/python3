# import time
# from time import time as my_timer
# import random
#
# input('Enter to start')
# wait_time = random.randint(1, 6)
# time.sleep(wait_time)
# start_time = my_timer()
# input('Enter to stop time')
# end_time = my_timer()
# print('started at ' + time.strftime("%X", time.localtime(start_time)))
# print('end at ' + time.strftime("%X", time.localtime(end_time)))
#
# print(f'How quick you were {end_time - start_time}')


# import time
# # perf_counter is most accurate time
# from time import perf_counter as my_timer
# import random
#
# input('Enter to start')
# wait_time = random.randint(1, 6)
# time.sleep(wait_time)
# start_time = my_timer()
# input('Enter to stop time')
# end_time = my_timer()
# print('started at ' + time.strftime("%X", time.localtime(start_time)))
# print('end at ' + time.strftime("%X", time.localtime(end_time)))
#
# print(f'How quick you were {end_time - start_time}')


# import time
# from time import monotonic as my_timer
# import random
#
# input('Enter to start')
# wait_time = random.randint(1, 6)
# time.sleep(wait_time)
# start_time = my_timer()
# input('Enter to stop time')
# end_time = my_timer()
# print('started at ' + time.strftime("%X", time.localtime(start_time)))
# print('end at ' + time.strftime("%X", time.localtime(end_time)))
#
# print(f'How quick you were {end_time - start_time}')

import time
# calc how much cpu took to execute
from time import process_time as my_timer
import random

input('Enter to start')
wait_time = random.randint(1, 6)
time.sleep(wait_time)
start_time = my_timer()
input('Enter to stop time')
end_time = my_timer()
print('started at ' + time.strftime("%X", time.localtime(start_time)))
print('end at ' + time.strftime("%X", time.localtime(end_time)))

print(f'How quick you were {end_time - start_time}')