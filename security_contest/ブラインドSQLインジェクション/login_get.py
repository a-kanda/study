import urllib.request

#get request

params = {
    "id": "admin",
    "pass": 1
}
p = urllib.parse.urlencode(params)
url = "http://ctfq.sweetduet.info:10080/~q6/?" + p
print(url)

with urllib.request.urlopen('url') as response:
    html = response.read().decode("utf-8")
    print(html)

