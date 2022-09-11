def Shuff(t):
    if(t%3!=0):
        raise ValueError
        return None
    u_length = int(t/3)
    kernal_length = int(t/3) * 2
    solution = []
    t1 = [i for i in range(1,kernal_length+1)]
    u = [i+kernal_length+1 for i in range(u_length)]
    initial = list(t1)
    # print(t1)
    # print(u)
    solution.append(t1)
    flag = True
    while(True):
        t2 = []
        i=0
        j=0
        while(len(t2) != kernal_length):
            t2.append(u[i])
            i += 1
            t2.append(t1[j])
            j += 1
        # print("Finished iteration ",t2)
        u = t1[kernal_length//2:]
        t1 = t2
    
        if(t2 == initial):
            # print("Solution Found")
            break
        solution.append(t2)
    return solution


def fetch(num,database):
    sol = Shuff(len(database))
    return sol[(num-1)%len(sol)]

def work(database):
    k = int(input("which week data do you want ? "))
    if(k == 0):
        return 0
    data = fetch(int(k),database)
    days = ['Mon','Tue','Wed','Thu','Fri','Sat']
    i = 0
    for each in data:
        print("{} {}".format(days[i%6],database[each]))
        i += 1
    work(database)

def main():
    print("Welcome to Fiesta")
    num = int(input("Enter number of your clothes : "))
    if(num%3 != 0):
        print("Number of clothes should be multiple of 3 : ")
        return 0

    f = open('data.txt','w')
    dress = input("Feed-in your clothes : ")
    f.write(dress)
    f.close()
    dress = dress.split()
    j = 1
    database = {}
    for each in dress:
        database[j] = each
        j += 1
    
    work(database)

try:
    f = open('data.txt','r')
except:
    main()
else:
    print("Looks like you have a database already made : ")
    i = int(input('Make a new data base ? 1/0 : '))
    if(i==1):
        main()
    dress = f.read().split(" ")
    j = 1
    database = {}
    for each in dress:
        database[j] = each
        j += 1
    print(database)
    work(database)