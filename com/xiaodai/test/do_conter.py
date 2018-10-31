def creat_conter():
    l=[0]
    def conter():
        l[0]+=1
        return l[0]
    return conter
con= creat_conter()
print(con(),con())
print(con())