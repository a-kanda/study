# -*- coding: utf-8 -*-
#import urllib.request
import crypt

print("input hash code")
hash = input()
data = [chr(i) for i in range(41,123)]

for i in data:
    for j in data:
        if crypt.crypt(("tanaka"+i+j),"89") == (hash):
            print("answer")
            print(i+j)
            exit()


print("nothing")
