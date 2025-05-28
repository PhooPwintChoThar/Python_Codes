import time

class  Clock(object):
    def __init__(self):
        currentTotalSeconds=int(time.time())
        self.hh=currentTotalSeconds//3600%24+7
        self.mm=(currentTotalSeconds%3600)//60
        self.ss=(currentTotalSeconds%3600)%60

    def run(self):
        while True:
            self.ss+=1
            if self.ss==60:
                self.mm+=1
                self.ss%=60
            
            if self.mm==60:
                self.hh+=1
                self.mm%=60

            if self.hh==24:
                self.hh%=24

            print(f"Current Time : {self.hh:02d} : {self.mm:02d} : {self.ss:02d}")



    def setTime(self, h, m, s):
        self.hh=h
        self.mm=m
        self.ss=s

class AlarmClock(Clock):
    def __init__(self):
        super().__init__()
        self.alarm_hh=0
        self.alarm_mm=0
        self.alarm_ss=0
        self.alarm_on_off=False

    def setAlarmTime(self,h,m,s):
        self.alarm_hh=h
        self.alarm_mm=m
        self.alarm_ss=s
        self.alarm_on_off=True

    def alarm_on(self):
        self.alarm_on_off=True
        

    def alarm_off(self):
        self.alarm_on_off=False

    def run(self):
        while self.alarm_on_off:
            self.ss+=1
            if self.ss==60:
                self.mm+=1
                self.ss%=60
            
            if self.mm==60:
                self.hh+=1
                self.mm%=60

            if self.hh==24:
                self.hh%=24
            print("\n \n")
            print(f"Current Time : {self.hh:02d} : {self.mm:02d} : {self.ss:02d}")
            print(f"Alarm Time : {self.alarm_hh:02d} : {self.alarm_mm:02d} : {self.alarm_ss:02d}")
            if self.hh==self.alarm_hh and self.mm==self.alarm_mm and self.ss==self.alarm_ss:
                print("~~~~~~~~~~~beep beep beep beep~~~~~~~~")
                break




t=Clock()    


#Test 1 = Check running Clock
#t.setTime(6,5,3)
#t.run()

#Test 2 = Check Alarm clock
a=AlarmClock()
a.setAlarmTime(00,34,58)
a.run()
a.alarm_off()
print(f"Current Time : {a.hh:02d} : {a.mm:02d} : {a.ss:02d}")#check current time works in alarm clock


