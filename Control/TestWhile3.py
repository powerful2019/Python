
n = 100

while n > 0 :
    n = n-1
    print("还有n天学习",n)
    if n <= 10 :
        print("准备考试了")
# 这里用break会在 n < 10时退出当前的while循环
        break 
