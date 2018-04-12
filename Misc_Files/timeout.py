import time



timeout = 1
strt_time = time.time()
time_stamp = strt_time
i = 0
print "\nStart Time: " + str(strt_time)
while i <10:
    
    time.sleep(0.1)
    i = i + 1
    time_stamp = time.time()
    time_elapsed = time.time() - strt_time
    new_timeout = timeout - time_elapsed
    print"\nInside Loop at " + str(time_stamp)
    print "\nTime elapsed = " + str(time_elapsed)
    print "\nNew Timeout: " + str(new_timeout)
    if (timeout - (time_stamp - strt_time)) <= 0:
        print "\n timeout occured at i = " + str(i)
        break
    
