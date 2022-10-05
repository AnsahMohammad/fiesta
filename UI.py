import streamlit as st

# st.subheader(" Entering your private Information in this Version is deprecated ! Thank You ! ")*************
st.title('Fiesta : Wear Uniquely !')

def exit():
    st.error("Sorry an error occured")

def Shuff(t):
    u_length = int(t/3)
    kernal_length = int(t/3) * 2
    solution = []
    t1 = [i for i in range(1,kernal_length+1)]
    u = [i+kernal_length+1 for i in range(u_length)]
    initial = list(t1)
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
        u = t1[kernal_length//2:]
        t1 = t2
    
        if(t2 == initial):
            break
        solution.append(t2)
    return solution

def fetch(num,database):
    sol = Shuff(len(database))
    return sol[(num-1)%len(sol)]

def work(database):
    k = st.number_input('Select a Week',1,100)
    data = fetch(k,database)
    days = ['Mon','Tue','Wed','Thu','Fri','Sat']
    i = 0
    for each in data:
        st.write("{} {}".format(days[i%6],database[each]))
        i += 1 

tab1, tab2 = st.tabs(["Wadrobe","Edit the Wadrobe"])

with tab2:
    st.warning("Current database will erased after editing !")
    num = st.radio("Enter number of clothes : ",[3,6,9,12,15,18,21,24,27,30],0)
    if(num >= 6):
        dress = st.text_area("Feed in your clothes saperated by ',' :")
    else:
        st.write("Clothes Must be multiple of three for this Algorithm to work")
    k = st.button("Confirm")
    if(k):
        f = open('data.txt','w')
        f.write(dress)
        f.close()
        dress = dress.split(',')
        j = 1
        database = {}
        for each in dress:
            database[j] = each
            j += 1
        st.success('Added {} clothes to the Wadrobe ✅'.format(len(dress)))

database = {}
with tab1:
    try:
        f = open('data.txt','r')
    except:
        st.error("You have Not created a Wadrobe")
        st.write("Go to Wadrobe Tab to create One")
    else:
        col1, col2, col3 = st.columns(3)
        st.subheader("Wadrobe")
        dress = f.read().split(",")
        for i in range(0,len(dress)):
            if i%3  == 0:
                col1.write(dress[i])
            elif i%3 == 1:
                col2.write(dress[i])
            elif i%3 == 2:
                col3.write(dress[i])

        j = 1
        for each in dress:
            database[j] = each
            j += 1

        st.subheader("What to Wear ? :")     
        work(database)


# st.write("With ❤️ from AnsahMohammad")
