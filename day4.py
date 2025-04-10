class Solution(object):
    def largestAltitude(self, gain):
        highest_altitude=0
        answer=0
        for i in range(len(gain)):
            answer=((answer+gain[i]))
            highest_altitude= max(highest_altitude,answer)
        return highest_altitude    
