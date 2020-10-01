# 一个0-10内猜数字的益智小游戏
# 2020-09-12
# fyj

numcor = 7   # 谜底数字

print("字谜游戏")
print("规则：你共有3次猜测机会，我们会给出偏大还是偏小的提示，你的猜测次数超过3次后则失败！")
print("Are You Ready? ")
ans1 = input("Yes(1) or No(0) ?: ")
ans1 = int(ans1)
if(ans1 == 0):
    print("已退出程序！")
else:
    print("Game Begin!")

    times = 3
    
    print("The number is in 0-10")
    ans2 = input("Your answer: ")
    ans2 = int(ans2)

    times = times - 1
    
    if ans2 == numcor:
        print("You Got it!You Win!")
    else:
        if(ans2 > numcor):
            print("你猜的数字大了，你的机会还剩%d次" % (times))
        else:
            print("你猜的数字小了，你的机会还剩%d次" % (times))
        
        ans2 = input("Your answer: ")
        ans2 = int(ans2)
        
        times = times - 1
        if ans2 == numcor:
            print("You Got it!You Win!")
        else:
            if(ans2 > numcor):
                print("你猜的数字大了，你的机会还剩%d次" % (times))
            else:
                print("你猜的数字小了，你的机会还剩%d次" % (times))
            
            ans2 = input("Your answer: ")
            ans2 = int(ans2)
            
            times = times - 1
            if ans2 == numcor:
                print("You Got it!You Win!")
            else:
                print("猜错了，你没有机会了")
                







