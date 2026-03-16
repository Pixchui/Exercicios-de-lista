dic = {

}

string = "a rata roeu a roupa do rei de roma"

frase = string.split()

for i in frase:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
    
print(dic.items())