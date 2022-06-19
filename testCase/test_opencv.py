import random
word = ['a','b','c','d','e','f','g','h','i','j',
        'k','l','m','n','o','p','q','r','s','t',
        'u','v','w','x','y','z','_','-','/','#'
        '^','&','*','|','.','0','1','2','3','4','5','6','7','8','9']
ans = int(input("密码长度(小于40)："))

try:
    for a in range(ans):
        n = random.randint(0,44)
        print(word[n],end="")
except:
    print("\n你的数是不是大于40了?")
