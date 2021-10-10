a = int(input("입력할 값의 갯수를 입력하시오: "))
i = []
for _ in range(a):
    i.append(int(input()))

d = { }
for t in i:
    d[t] = i.count(t)

m = max(d.values())       #d.keys =>앞의 값 

r = []
for key,value in d.items():   #items = value ,key 값을 같이 가지고옴
    if value == m:
        r.append(key)

if len(r) == 1:         #r의 길이
    mid = r[0]
else:
    mid = sorted(r)[1]

av = round(sum(i) / a)

s = sorted(i)[a//2]

r = max(i) - min(i)



print("평균:",av)
print("중앙 값:",s)
print("최빈 값:",mid)
print("범위:",r)
