#methods_reverse
var1= [1,2,3,4,5,6,7,9]
var1.reverse()
print(var1)
#methods_count
word_nums ='我们今天不去上学，我们去踢足球'.count('我们')
print(word_nums)
#methods_find
str2 = '哈哈哈我们今天不去上学，我们去踢足球'
pos2 = str2.find('我们',0)
print(pos2)


#Decorators
def funA(fn):
    print("hello 1")
    fn()
    print("damn 2")
    return "body"

@funA
def funB():
    print("fuck c")