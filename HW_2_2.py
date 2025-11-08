number = int(input("Введіть 5-значне число:"))
a = number // 10000
b = (number // 1000) % 10
c = (number // 100) % 10
d = (number // 10) % 10
e = number % 10
reversed = (e*10000+d*1000+c*100+b*10+a)
print(reversed)
