from collections import deque

class RecentCounter(object):

    def __init__(self):
        self.deq=deque()

    def ping(self, t):
        self.deq.append(t)

        while self.deq and self.deq[0]<t-3000:
            self.deq.popleft()
        return len(self.deq)

obj = RecentCounter()
param_1 = obj.ping(1)
param_1 = obj.ping(100)
param_1 = obj.ping(3001)
param_1 = obj.ping(3002)
