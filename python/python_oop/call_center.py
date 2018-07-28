class Call(object):
    def __init__(self, call_id, call_name, call_number, call_time, call_reason):
        super(Call, self).__init__()
        self.call_id = call_id
        self.call_name = call_name
        self.call_number = call_number
        self.call_time = call_time
        self.call_reason = call_reason
    
    def display_info(self):
        print 'Call ID: ' + str(self.call_id)
        print 'Name: ' + str(self.call_name)
        print 'Number: ' + str(self.call_number)
        print 'Time: ' + str(self.call_time)
        print 'Reason: ' + str(self.call_reason)
        return self

class CallCenter(Call):
    def __init__(self, calls, queue):
        super(CallCenter, self).__init__(calls, queue)
        self.calls = []
        self.queue = len(self.calls)

    def add(self):
        self.calls = calls
        calls.append(self.call_name)
        
        return self
    
    def remove(self):
        self.call -= 1
    
    def info(self):
        print "Name: " + str(self.name)
        print "Number: " + str(self.number)
        print "Queue: " + len(self.queue)


mike = Call(1, 'Mike', '213-449-2212', '9:20PM', 'Emergency')
mike.display_info()

mike = CallCenter('joe', 1)
mike.add()