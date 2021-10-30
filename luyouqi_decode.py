# function getpasswd1(b) 
# {
#             a = "RDpbLfCPsJZ7fiv";
#             c = "yLwVl0zKqws7LgKPRQ84Mdt708T1qQ3Ha7xv3H7NyU84p21BriUWBU43odz3iP4rBL3cD02KZciXTysVXiV8ngg6vL48rPJyAUw0HurW20xqxv9aYb4M9wK1Ae0wlro510qXeU07kV57fQMc8L6aLgMLwygtc0F10a0Dg70TOoouyFhdysuRMO51yY5ZlOZZLEal1h0t9YQW0Ko7oBwmCAHoic4HYbUyVeU3sfQ1xtXcPcf1aT303wAQhv66qzW";
#             var e = "", f, g, h, k, l = 187, n = 187;
#             g = a.length;
#             h = b.length;
#             k = c.length;
#             f = g > h ? g : h;  //f取a和b中  的最大长度
#             for (var p = 0; p < f; p++)
#                 n = l = 187,
#                 p >= g ? n = b.charCodeAt(p) : p >= h ? l = a.charCodeAt(p) : (l = a.charCodeAt(p),
#                 n = b.charCodeAt(p)),
#                 e += c.charAt((l ^ n) % k);
#             console.log(e)
# }
def get_index(chr):

    ins = []
    c = "yLwVl0zKqws7LgKPRQ84Mdt708T1qQ3Ha7xv3H7NyU84p21BriUWBU43odz3iP4rBL3cD02KZciXTysVXiV8ngg6vL48rPJyAUw0HurW20xqxv9aYb4M9wK1Ae0wlro510qXeU07kV57fQMc8L6aLgMLwygtc0F10a0Dg70TOoouyFhdysuRMO51yY5ZlOZZLEal1h0t9YQW0Ko7oBwmCAHoic4HYbUyVeU3sfQ1xtXcPcf1aT303wAQhv66qzW";
    begin = 0
    while (c.find(chr, begin)!=-1):
        i = c.find(chr, begin)
        ins.append(i)
        begin = i+1
    return ins
    


def password_decode(e):
    a = "RDpbLfCPsJZ7fiv"
    g = len(a)
    c = 'yLwVl0zKqws7LgKPRQ84Mdt708T1qQ3Ha7xv3H7NyU84p21BriUWBU43odz3iP4rBL3cD02KZciXTysVXiV8ngg6vL48rPJyAUw0HurW20xqxv9aYb4M9wK1Ae0wlro510qXeU07kV57fQMc8L6aLgMLwygtc0F10a0Dg70TOoouyFhdysuRMO51yY5ZlOZZLEal1h0t9YQW0Ko7oBwmCAHoic4HYbUyVeU3sfQ1xtXcPcf1aT303wAQhv66qzW'
    k = len(c)
    h = len(e)
    if (g > h):
        f = g
    else:
        f = h
    inss = []
    for i in range(0,f,1):# i指密文的每个字符序号
        inss.append(get_index(e[i]))
    print(inss)                              # [ [] [] ]密文每个字符可能对应的值
    for i in range(0,f,1):# i 指密文的字符序号 
        for j in inss[i]:
            n = 187
            if (i >= g):
                l = 187 
                c_maybe = (j^l)
                if (c_maybe>=33 and c_maybe<126):
                    print('第' + str(i + 1) + '位可能的值为:' + chr(c_maybe))
            elif(j == (ord(a[i])) ^ n):
                print('第' + str(i + 1) + '位可能是填充位')
                break
            else:
                l = ord(a[i])  
                c_maybe = (j^l)
                if (c_maybe>=33 and c_maybe<126):
                    print('第' + str(i+1) + '位可能的值为:' + chr(c_maybe))


# password_decode('H42n9Jw2PTefbwK')
password_decode('0KcgeX92i0q0gPcQfXq7')




