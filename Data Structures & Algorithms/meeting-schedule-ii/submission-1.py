"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        temp = []
        for interval in intervals:
            temp.append((interval.start, 1))
            temp.append((interval.end, -1))
        temp.sort()
        max_meeting = 0
        curr_meeting = 0
        for e in temp:
            curr_meeting += e[1]
            max_meeting = max(max_meeting, curr_meeting)
        return max_meeting


    
        
