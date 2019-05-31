'''
Design and implement a HitCounter class that keeps track of requests (or hits). It should support the following operations:

record(timestamp): records a hit that happened at timestamp
total(): returns the total number of hits recorded
range(lower, upper): returns the number of hits that occurred between timestamps lower and upper (inclusive)
Follow-up: What if our system has limited memory?
'''
import bisect

RECORD_LIMIT = 256

class Record(object):

    def __init__(self):
        self.start_timestamp = None
        self.end_timestamp = None
        self.times = []

class HitCounter(object):

    def __init__(self):
        self.old_records = []
        self.current_record = Record()

    def record(self, timestamp):
        if not self.current_record.start_timestamp:
            self.current_record.start_timestamp = timestamp

        self.current_record.times.append(timestamp)
        self.current_record.end_timestamp = timestamp

        if len(self.current_record.times) == RECORD_LIMIT:
            
            self.old_records.append(self.current_record)
            self.current_record = Record()
        return

    def total(self):
        total = len(self.old_records) * RECORD_LIMIT + len(self.current_record.times)
        return total

    def range(self, lower, upper):
        all_records = self.old_records + [self.current_record]
        start_times = [r.start_timestamp for r in all_records]
        end_times = [r.end_timestamp for r in all_records]

        start_index = bisect.bisect_left(start_times, lower) - 1
        end_index = bisect.bisect_left(end_times, upper)
        start_record = all_records[start_index]
        end_record = all_records[end_index]

        start_rec_idx = bisect.bisect(start_record.times, lower)
        end_rec_idx = bisect.bisect(end_record.times, upper)

        counter = 0
        # get from start to end of these end files
        counter += len(start_record.times[start_rec_idx:])
        counter += len(end_record.times[:end_rec_idx])
        # then add end-start * maxlen
        print("end {} start {}".format(end_index, start_index))
        counter += (end_index - (start_index + 1) ) * RECORD_LIMIT
        return counter


hitcounter = HitCounter()

for i in range(130000):
    hitcounter.record(i)

print("total records: ", hitcounter.total())

print("show range 500 - 600: ", hitcounter.range(500, 600))

print("show range 300 - 600: ", hitcounter.range(300, 600))

print("show range 350 - 1200: ", hitcounter.range(350, 1200))

print("show range 200 - 5400: ", hitcounter.range(200, 5400))






