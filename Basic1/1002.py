# 读入一个正整数 n，计算其各位数字之和，用汉语拼音写出和的每一位数字。

# 输入格式：
# 每个测试输入包含 1 个测试用例，即给出自然数 n 的值。这里保证 n 小于 10
# 100

# 输出格式：
# 在一行内输出 n 的各位数字之和的每一位，拼音数字间有 1 空格，但一行中最后一个拼音数字后没有空格。

# 输入样例：
# 1234567890987654321123456789
# 输出样例：
# yi san wu

n = input()
t = 0
for i in n:
    t += int(i)
str_word = str(t)
dic = {
    "0": "ling",
    "1": "yi",
    "2": "er",
    "3": "san",
    "4": "si",
    "5": "wu",
    "6": "liu",
    "7": "qi",
    "8": "ba",
    "9": "jiu",
}
list_word = []
for i in str_word:
    if i in dic:
        list_word.append(dic[i])
str_lian = " "
print(str_lian.join(list_word))
