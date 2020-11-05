# 寻找输入数字中的全数字pandigital
# 2020-10-30
# fyj

def pandigital(nums):
    flag = False
    for num in nums:
        num = str(num)
        all_number_list = [str(i) for i in range(1, len(num) + 1)]
        all_number_in_num_list = [j for j in all_number_list if j in num]
        if len(all_number_list) == len(all_number_in_num_list):
            print(num)
            flag = True
    if flag == 0:
        print('not found')

if __name__ == "__main__":
    lst = pandigital(eval(input("输入数字串: ")))
