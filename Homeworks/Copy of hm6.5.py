oneTNote=0
fiveHNote=0
oneHNote=0
fiftyNote=0
twentyNote=0
twoNote=0
oneNote=0
baht=int(input("Input your amount of money  :  "))
if baht>=1000:
    oneTNote=baht//1000
    hundred=baht%1000
    fiveHNote=hundred//500
    lessThanFiveH=hundred%500
    oneHNote=lessThanFiveH//100
    lessThanOneH=lessThanFiveH%100
    fiftyNote=lessThanOneH//50
    lessThanFifty=lessThanOneH%50
    twentyNote=lessThanFifty//20
    lessThanTwenty=lessThanFifty%20
    twoNote=lessThanTwenty//2
    oneNote=lessThanTwenty%2
elif baht>=500:
    fiveHNote=baht//500
    lessThanFiveH=baht%500
    oneHNote=lessThanFiveH//100
    lessThanOneH=lessThanFiveH%100
    fiftyNote=lessThanOneH//50
    lessThanFifty=lessThanOneH%50
    twentyNote=lessThanFifty//20
    lessThanTwenty=lessThanFifty%20
    twoNote=lessThanTwenty//2
    oneNote=lessThanTwenty%2
elif baht>=100:
    oneHNote=baht//100
    lessThanOneH=baht%100
    fiftyNote=lessThanOneH//50
    lessThanFifty=lessThanOneH%50
    twentyNote=lessThanFifty//20
    lessThanTwenty=lessThanFifty%20
    twoNote=lessThanTwenty//2
    oneNote=lessThanTwenty%2
elif baht>=50:
    fiftyNote=baht//50
    lessThanFifty=baht%50
    twentyNote=lessThanFifty//20
    lessThanTwenty=lessThanFifty%20
    twoNote=lessThanTwenty//2
    oneNote=lessThanTwenty%2
elif baht>=20:
    twentyNote=baht//20
    lessThanTwenty=baht%20
    twoNote=lessThanTwenty//2
    oneNote=lessThanTwenty%2
elif baht>0:
    twoNote=baht//2
    oneNote=baht%2
else:
    print("Invalid amount")

print("1000-Baht notes: ",oneTNote)
print("500-Baht notes: ",fiveHNote)
print("100-Baht notes: ",oneHNote)
print("50-Baht notes: ",fiftyNote)
print("20-Baht notes: ",twentyNote)
print("2-Baht coins: ",twoNote)
print("1-Baht coins: ",oneNote)