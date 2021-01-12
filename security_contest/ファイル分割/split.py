#coding: UTF-8
a = [0,6943,9727,26632,2791486,2794240,2796217,2813627,5578481,5580896,5583378,5601221,8366075,8368830,8371932,8388384]
#アドレス
b = ['gif','png','jpg','bmp']
#拡張子
f = open("MrFusion.gif", "rb")
#ファイルの読み込み
for x in range(len(a)-1):
    open('result{:02d}.{}'.format(x, b[x % 4]), 'wb').write(f.read(a[x + 1] - a[x]))
