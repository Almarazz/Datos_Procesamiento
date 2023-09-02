meses = ["Enero", "Febrero", "Marzo"]
(x,y,z) = meses

print(x)
print(y)
print(z)

meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo"]
(x,y,*z) = meses

print(x)
print(y)
print(z)

meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo"]

(x,y,*w,z) = meses

print(x)
print(y)
print(w)
print(z)