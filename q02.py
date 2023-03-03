l=input("enter the list to be updated:").split(',')

def triple_num(b):
    return int(b)*3  

result=list(map(triple_num,l))
print(result)
