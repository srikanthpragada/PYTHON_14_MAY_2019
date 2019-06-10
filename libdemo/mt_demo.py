import threading
from threading import Thread


def print_nums():
    for i in range(1, 11):
        print("Child " , i)


ct = threading.current_thread()
print("Current Thread : ", ct.name)

t1 = Thread(target=print_nums, name="Child")
t1.start()
print("Thread Count   : ", threading.active_count())

t1.join() # wait for t1 to terminate

for i in range(1,11):
    print("Main ", i)

print("End of MainThread")
