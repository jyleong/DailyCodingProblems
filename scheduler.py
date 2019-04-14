from threading import Timer, Thread, Event
import time

class ScheduleTimer(object):
    def __init__(self, interval, function, *args, **kwargs):
        self._timer     = None
        self.interval   = interval # set interval of when to start
        self.function   = function # ref to func
        self.args       = args # non keyword args
        self.kwargs     = kwargs #key word args
        self.is_running = False
        #self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False

class SchedulerThreader(object):
    def __init__(self, interval, function, *args, **kwargs):
        self.interval = interval
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.event = Event()
        self.thread = Thread(target=self.runner)
        self.thread.start()

    def runner(self):
        # wait after interval, and then run function
        while not self.event.wait(self.interval):
            self.function(*self.args, **self.kwargs)

    def stop(self):
        self.event.set()
        self.thread.join()

def print_hello(name):
    print("#############")
    print("hello my name is: ", name)
    print("#############")
    return

def test_thread(start):
    print("#############")
    print("Time difference: ", time.time()-start)
    print("#############")
    return

print("testing...")
timeStart = time.time()
threadTest = SchedulerThreader(5,test_thread, timeStart)

time.sleep(16)
threadTest.stop()

# scheduler = ScheduleTimer(5, print_hello, "Matt")

# scheduler.start()

# time.sleep(12)
# scheduler.stop()
# print("stopping scheduler and exit")


# print('timer test')

# def test_1():
#     print("test the timer")

# t = Timer(2, test_1)
# t.start()

# time.sleep(6)
# t.cancel();
print('timer test done')