def convertTime(hr):
    if hr>=0 and hr<=11 :
        zone="AM"
    elif hr>=12 and hr<=23:
        zone="PM"
    else:
        zone="Invalid time"
    if hr==12 or hr==0:
        return 12,zone
    else:
       return hr%12,zone
def main():
    hours=0
    minutes=33
    hour,zone_time=convertTime(hours)
    print(f"time24hourTo12hour(\"{hours}:{minutes}\")=> \"{hour:02}:{minutes:02} {zone_time}\"")

main()