import turtle as t

t.tracer(False)
a, b, c = t.Pen(), t.Pen(), t.Pen()
NumT = 0

def try1(d, ang, Num):
    for x in range(100 * (Num + 1)):
        d.forward(x)
        d.left(ang)
        Num += 1

a.color("#008000")
try1(a, 39, NumT)
NumT += 1
b.color("#808000")
try1(b, 59, NumT)
NumT += 1
c.color("#800000")
try1(c, 99, NumT)
NumT += 1

t.done()