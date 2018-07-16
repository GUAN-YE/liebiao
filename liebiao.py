import sys
import time


start_time1 = time.time()
p1 = [x for x in range(10000000) if x >5000]
end_time1 = time.time()

print('列表生成式用时：', end_time1-start_time1)
print('列表生成式内存是：', sys.getsizeof(p1))
def yeilds(start,end):
    for i in range(start,end):
        yield i

start_time2 = time.time()

p2 = yeilds(0,10)
end_time2 = time.time()

print ('yeilds用时：',end_time2-end_time1)
print('yeilds内存：',sys.getsizeof(p2))

# 生成器（yield）比（列表生成式和for循环）省时间和内存


start_time3 = time.time()
p3 = []
for s in range(10000000):
    if s >5000:
        p3.append(s)

end_time3 = time.time()
print('for 循环 用时：',end_time3-start_time3)
print('for 循环内存：', sys.getsizeof(p3))

print ([100 * x + 10 * c + v for x in range(1,10) for c in range(1,10) for v in range(1,10) if x==v])

