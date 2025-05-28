class Clock:
    def __init__ (self,hour=0,minute=0,second=0):
        self.hour=hour
        self.minute=minute
        self.second=second

    def setTime(self,hour,minute,second):
        self.hour=hour
        self.minute=minute
        self.second=second

    def getTime(self):
        print(f"It is {self.hour:02} hr {self.minute:02} minutes {self.second:02} seconds in 24hr format.")
    
    def tick(self):
        self.second+=1
        if self.second>=60:
            self.minute+=1
            self.second-=60
            if self.minute>=60:
                self.hour+=1
                if self.hour==24:
                    self.hour=0
                self.minute-=60
    
    def displayTime(self):
        if 0<=self.hour<=11:
            format="AM"
        else:
            format="PM"

        print(f"{self.hour%12:02} hr {self.minute:02} minutes {self.second} seconds "+format)

time=Clock()
#time.setTime(22,45,33)
#time.setTime(23,59,59)
time.setTime(8,42,59)
time.getTime()
time.tick()
print("increased 1 second.")
time.displayTime()
