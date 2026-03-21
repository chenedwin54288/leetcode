from collections import deque

class RecentCounter(object):

    def __init__(self):
        # Use a deque for O(1) pops from the left
        self.queue = deque()

    def ping(self, t):
        # 1. Add the current ping to the end
        self.queue.append(t)
        
        # 2. Remove all pings that are outside the [t-3000, t] window
        # Since t is increasing, these will always be at the front
        while self.queue[0] < t - 3000:
            self.queue.popleft()
            
        # 3. The length is now the number of pings in the last 3000ms
        return len(self.queue)