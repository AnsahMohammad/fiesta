import streamlit as st
st.title('Fiesta : Wear Unique !')

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
    k = st.number_input('Select a Week',1,100)
    # if(k == 0):
    #     return 0
    data = fetch(k,database)
    days = ['Mon','Tue','Wed','Thu','Fri','Sat']
    i = 0
    for each in data:
        st.write("{} {}".format(days[i%6],database[each]))
        i += 1
    # work(database)   

tab1, tab2 = st.tabs(["Wadrobe","Edit the Wadrobe"])
# tab1.write("What to Wear")
# tab2.write("Edit")

with tab2:
    num = st.slider('Select Number of Clothes',5,33)
    if(num%3==0):
        f = open('data.txt','w')
        dress = st.text_area("Feed in your clothes saperated by ',' :")
        f.write(dress)
        f.close()
        dress = dress.split(',')
        j = 1
        database = {}
        for each in dress:
            database[j] = each
            j += 1
    else:
        st.write("Clothes Must be multiple of three for this Algorithm to work")

    if(num%3 == 0 and len(dress) > 0 ):
        st.write('Added {} clothes to the Wadrobe ✅'.format(len(dress)))

#flag to know if data is present or not
cflag = 0
database = {}
with tab1:
    try:
        f = open('data.txt','r')
    except:
        st.write("You have Not created a Wadrobe")
        st.write("Go to Wadrobe Tab to create One")
    else:
        st.subheader("Wadrobe")
        dress = f.read().split(",")
        for i in range(0,len(dress),3):
            st.write("{}     |     {}     |      {}".format(dress[i],dress[i+1],dress[i+2]))
        j = 1
        for each in dress:
            database[j] = each
            j += 1
        cflag = 1

if(cflag):
    st.subheader("What to Wear ? :")     
    work(database)



st.write("With ❤️ from AnsahMohammad")