# -*- coding: utf-8 -*-
#import urllib.request
import hashlib

print(input hash code)
hash = input()
data = ['あ','い','う','え','お','か','き','く','け','こ','さ','し','す','せ','そ','た','ち','つ','て','と','な','に','ぬ','ね','の','は','ひ','ふ','へ','ほ','ま','み','む','め','も','や','ゆ','よ','ら','り','る','れ','ろ','わ','を','ん','が','ぎ','ぐ','げ','ご','ざ','じ','ず','ぜ','ぞ','だ','ぢ','づ','で','ど','ば','び','ぶ','べ','ぼ','ぱ','ぴ','ぷ','ぺ','ぽ','ぁ','ぃ','ぅ','ぇ','ぉ','ゃ','ゅ','ょ','っ']

for i in data:
    for j in data:
        for k in data:
            for l in data:
                if hashlib.md5((i+j+k+l).encode('utf-8')).hexdigest() == hash:
                    print(i+j+k+l)
                    exit()

print("nothing")
