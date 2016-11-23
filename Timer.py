from Constants import *

# A timer object allows the game to keep track of time
class Timer(object):
    
    def __init__(self):
        self.frame_count = 0
        self.total_seconds = 0
        self.seconds = 0
        self.minutes = 0
        self.start_time = 0
        self.count_down = False
        self.time_expired = False
        
    # secs is the number of seconds the timer starts with    
    def set_start_time(self, secs):
        self.start_time = secs
            
    # Returns the value of seconds
    def calc_seconds(self):
        self.seconds = self.total_seconds % 60
          
    # Calculate total seconds
    def calc_total_seconds(self):
        if(self.count_down):
            self.total_seconds = self.start_time - (self.frame_count // FRAME_RATE)
            if self.total_seconds < 0:
                self.total_seconds = 0
        else:
            self.total_seconds = self.frame_count // FRAME_RATE
        
    # Calculate total minutes
    def calc_total_minutes(self):
        # Divide by 60 to get total minutes
        self.minutes = self.total_seconds // 60
                
    def tick(self):
        self.frame_count += 1
        self.calc_total_seconds()
        self.calc_total_minutes()
        self.calc_seconds()    