# a="indu"
# a[0]='i'#typerror:'str'object does not support item assignment
# print (dir(str))
# n="Indu priya"
# print(n.capitalize()) #Indu priya
# name="Indu Priya"
# print(len(name))#10
# print(name.center(50))#          Indu Priya
# print(name.center(50,'*'))#********************Indu Priya************************
# print(name.center(70,'@'))#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@Indu Priya@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# name="Vamsynagandla"
# print(name.capitalize())#Vamsynagandla
# name="Vamsy naGandLAa"
# print(name.casefold())#vamsy nagandlaaa
# print(name.lower())#vamsy nagandlaa
# name="VAMSY"
# print(type(name))#str
# n=name.encode()
# print(n)#b'VAMSY'
# print(name.decode())#attributeerror
# name=b'vamsy'
# print(type(name))#bytes
# n=name.encode
# print(n)#attributrerror
# print(name.decode())
# name='VAMSY'
# print(name.upper())#VAMSY
# print(name.lower())#vamsy
# print(name.isupper())#True
# print(name.islower())#False
# b="GAME"
# print(b.isupper())#True
# m='INDU'
# print(m.islower())#False
# t='iNDU PRIYa'
# # print(t.title())# Indu Priya
# print(t.capitalize())#indu priya
# print(t.istitle())#False
# c='Indu Priya'
# print(c.istitle())#True
# c='indu priya'
# print(c.istitle())#False
# n='hELLo pyThon'
# print(n.endswith())#typeerror:endswitch()takes at least 1 arguent
# print(n.endswith('')) #True
# print(n.endswith(' '))#False
# print(n.endswith('n'))#True
# print(n.endswith('h'))#False
# print(n.endswith(""))#True
# print(n.endswith(" "))#False
# print(n.endswith(''' ''')) #False
# print(n.endswith(''''''))#True
# print(n.endswith(""" """))#False
# print(n,endswith(""""""))#nameerror
# n='hELLo Python'
# print(n.startswith(''))#True
# print(n.startswith(' '))#False
# print(n.startswith('h'))#True
# print(n.startswith('n'))#False
# print(n.starswith(','))#attributeerror
# print(n.startswith(""))#True
# print(n.startswith(","))#False 
# z=' hELLo python'
# print(z.startswith(''))#true
# print(z.startswith(' '))#True
# print(z.startswith('h'))#False
# print(z.startswith(' h'))#True
# v=''
# g='    '
# print(v.isspace())#False
# prnt(g.isspace())#True
# q="hELLo pyotholno"
# print(q.index('l'))#12
# print(q.index('L',4))#
# print(q.index('o'))
# print(q.index('o',5))
# print(q.index('h'))#0
# print(q.index(1))
# print(q.index('b'))
# c="python programming"
# print(c.removeprefix('p'))#ython programming
# print(c.removeprefix('p'))#python programming
# print(c.removeprefix('py'))#thon programming
# print(c.removesuffix('g'))#python programmin
# print(c.removesuffix('ng'))#python programmi
# print(c.removesuffix('ming'))#python program
# print(c.removesuffix(''))#python programming
# a="hello python"
# print(a.isalnum())#False
# a="hellopython"
# print(a.isalnum())#True
# a="hello . python"
# print(a.isalnum())#False
# a="hellopython35"
# print(a.isalnum())#True
# b="indu priya"
# print(b.isalpha())#False
# b="indupriya"
# print(b.isalpha())#True
# b="indupriya44"
# print(b.isalpha())#False
# b="2"
# print(b.isalpha())#False
# b="v"
# print(b.isalpha())#True
# b=""
# print(b.isalpha())#False
# b=" "
# print(b.isalpha())#True
# v="august python"
# print(v.isascii())#True
# b=chr(0)#False
# b=chr(32)#True
# print(b.isspace())#False
# print(b.isspace())#True
# print("hello"+chr(32)+"python")#hello python
# print("hello"+''+"python")#hellopython
# print("indu","priya",sep=' ')#indu priya
# print("indu","priya")#indu priya
# print(chr(32)+"mama")# mama
# print(chr(0)+"mama")#mama
# print(ord('a'))#97
# print(ord('z'))#122
# print(ord('A'))#65
# print(ord('Z'))#90
# print(ord('0'))#48
# print(ord('9'))#57
# print(ord(' '))#32
# print(ord('!'))#33
# v=bin(5)
# print(v,type(v))#0b101 str
# h=0b101
# print(h,type(h))#5 int
# j=0B101
# print(j,type(j))#5 int
# print(bin(23))#0b1011
# print(0o13)#11
# print(0o13)#11
# f=oct(11)
# print(f,type(f))#0o13 str
# print(0o13)#11
# print(0o13)#11
# w=hex(18)
# print(w,type(w))#0X12 str
# print(0x12)#18
# print(0X12)#18
# print(0XA)#10
# print(0XD)#13
# print(0XF)#15
