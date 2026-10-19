"""Magic date"""
def magic_date(d,m,y):
    if d*m==y :
        return "Magic date"
    else:
        return False
for y in range(1,100):
    for m in range(1,13):
        for d in range(1,32):
            res=magic_date(d,m,y)
            if res=="Magic date":
                print(d,m,y,"is a magic date in the 20th century.")



