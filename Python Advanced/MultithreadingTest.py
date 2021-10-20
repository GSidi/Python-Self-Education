""" import time
import threading

def calc_avg(numbers):
    print("Calculating average of numbers")
    count = 0
    for n in numbers:
        count += 1
        time.sleep(0.3)
        print("Average is :", (n+n)/count)

def calc_avg_odd(numbers):
    print("Calculate te average of odd numbers")
    count = 0
    for n in numbers:
        if n%2 == 1:
            time.sleep(0.3)
            print("Odd average is: ", (n+n)/count)
        else:
            print("Not an odd number")

def calc_avg_even(numbers):
    print("Calculate average of even numbers")
    count = 0
    for n in numbers:
        if n%2 == 0:
            time.sleep(0.3)
            print("Even average is: ", (n+n)/count)
        else:
            print("TROLOLOL")

arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

for i in range(len(arr)):
    t1 = threading.Thread(target=calc_avg, args= (arr,))
    t2 = threading.Thread(target=calc_avg_odd, args= (arr,))
    t3 = threading.Thread(target=calc_avg_even, args= (arr,))

    t1.start()
    t2.start()
    t3.start()

    t1.join()  
    t2.join()
    t3.join()


print("Done in : ", time.time() - t)
"""

import time
import threading
from threading import Thread

def sleepMe(i):
    print("Thread %i will sleep." % i)
    time.sleep(5)
    print("Thread %i is awake" % i)

for i in range(10):
    th = Thread(target=sleepMe, args=(i, ))
    th.start()
    print("Current Threads: %i." % threading.active_count())