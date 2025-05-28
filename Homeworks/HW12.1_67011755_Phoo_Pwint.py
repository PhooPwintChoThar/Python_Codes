dictionary= {
    "b": "be",
    "cuz": "because",
    "cu": "see you",
    "c": "see",
    "da": "the",
    "ok": "okay",
    "r": "are",
    "u": "you",
    "w/o": "without",
    "y": "why",
    "8": "ate",
    "gr8": "great",
    "m8": "mate",
    "w8": "wait",
    "l8r": "later",
    "2mro": "tomorrow",
    "4": "for",
    "b4": "before",
    "1ce": "once",
    "&": "and",
    "ur": "your",
    "afaik": "as far as I know",
    "ASAP": "as soon as possible",
    "atm": "at the moment",
    "brb": "be right back",
    "btw": "by the way",
    "fyi": "for your information",
    "imho": "in my humble opinion",
    "imo": "in my opinion",
    "lol": "laugh out loud",
    "omg": "oh my god",
    "rofl": "roll on the floor laughing",
    "ttyl": "talk to you later"
}

def textese(s):
    
    string=s.split()
    for x in range(len(string)):
        for d in dictionary:
            if d==string[x]:
                string[x]=dictionary[d]
               
    new_string=""
    for s in string:
        new_string+=s+" "

    return new_string

def untextese(s):
    string=s
    for d in dictionary:
        if dictionary[d] in string:
            string=string.replace(dictionary[d], d)
    return string



print(textese("I will cu 2mro at da meeting"))
print(textese("Send me da document ASAP ."))
print(textese("w8 for me"))
print("\n\n")
print(untextese("I will see you tomorrow at the meeting "))
print(untextese("Send me the document as soon as possible . "))
print(untextese("wait for me."))
