def change(money):
    count = 0
    while money > 0:
        if money >= 10:
            money = money-10
            count+=1
        elif money >= 5:
            money = money-5
            count+=1 
        else: 
            money= money-1 
            count+=1
    return count

if __name__ == '__main__':
    m = int(input())
    print(change(m))