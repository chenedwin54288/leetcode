from collections import deque

class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        # This question was too pain in the ass to understand
        # so I just watched a Youtube video that explained what
        # I needed to do

        # Bascially the idea is to have 2 queues
        # R_queue = []
        # D_queue = []
        # When you have "RDD"....
        # - R[0] disables D[0]
        #   R_queue = [0]
        #   D_queue = []

        # - D[0] cannot do anything
        #   R_queue = [0]
        #   D_queue = [1]
        #   0 < 1, thus remove 1
        #   append D[0] back to the queue for the next round
        #   but do D[0].index + n
        #   R_queue = [3]
        #   D_queue = [1]   

        # - D[1] disables R[0]
        #   R_queue = [3]
        #   D_queue = [2]
        #   2 < 3, thus remove 3
        #   ....
        #   R_queue = []
        #   D_queue = [5]

        # - R[0] cannot do anything

        # - D[1] is the only want able to do stuff, thus Dire wins


        R_queue = deque()
        D_queue = deque()
       
    
        # append to the queue
        for i in range(0, len(senate)):
            if senate[i] == 'R':
                R_queue.append(i)
            else:
                D_queue.append(i)
        
        # perform the analysis operation
        while len(R_queue) > 0 and len(D_queue) > 0:
            # pop from both queue and compare
            R_ele = R_queue.popleft() 
            D_ele = D_queue.popleft()
            if R_ele < D_ele: #D has been disabled
                R_queue.append(R_ele + len(senate))       
            else:             #R has been disabled
                D_queue.append(D_ele + len(senate))
        
        if len(R_queue) > 0:
            return "Radiant"
        else:
            return "Dire"
            
        
            
               
            


        
        