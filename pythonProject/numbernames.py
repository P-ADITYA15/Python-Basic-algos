lst = ["","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thriteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty"]
n = input("enter natural number: ")
t = ["","ten","twenty","thrity","fourty","fifty","sixxty","seventy","eighty","ninty","hundred"]
g = ["","hundred","hundred","hundred"]
b = int(n[0])
if len(n)==2:
    c = int(n[1])
elif len(n)==3:
    c = int(n[1])
    d = int(n[2])
elif len(n)==4:
    c = int(n[1])
    d = int(n[2])
    e=int(n[3])
if int(n)<=20:
    print(lst[int(n)])

elif int(n)>20 and int(n)<100:
    print(t[b],lst[c])
elif int(n)==100:
    print(t[10])
elif c==0 and d==0 and len(n)==3:
    print(lst[b],"hundred")
elif len(n)==3 and c==0 and len(n)==3:
    print(lst[b],"hundred",lst[d])
elif d==0 and len(n)==3:
    print(lst[b], "hundred", t[c])
elif int(n)<1000:
    print(lst[b], "hundred", t[c],lst[d])
elif n=="1000":
    print("one thousand")
elif c==0 and d==0 and e==0:
    print(lst[b],"thousand")
elif int(n)>1000:
    print(lst[b],"thousand",lst[c],g[c],t[d],lst[e])






