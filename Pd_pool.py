import streamlit as st
import pandas as pd
import csv
import os


st.set_page_config(layout="wide")

st.title('Snooker & POOL "RD"') 

st.text("Created By Ravi Mire")

st.write('')

st.write('')

st.write('')

st.write("Select the numbers and click Add+ to increase or Sub- to decrease the Score")
col1,col2, = st.columns([0.2,0.7])

if not os.path.exists('Player.csv'):
    fields = (["Name","Score","RD"])
    with open('Player.csv','a') as file:
        writer = csv.writer(file)
        writer.writerow(fields)

if 'count' not in st.session_state:
    st.session_state.count = 0



x = st.radio("",("15",'8','7','6','5','4','3','2','1'), horizontal=True )


def increment_counter():
    if x=='15':
        st.session_state.count += 15
    if x=='8':
        st.session_state.count += 8
    if x=='7':
        st.session_state.count += 7
    if x=='6':
        st.session_state.count += 6
    if x=='5':
        st.session_state.count += 5
    if x=='4':
        st.session_state.count += 4
    if x=='3':
        st.session_state.count += 3
    if x=='2':
        st.session_state.count += 2
    if x=='1':
        st.session_state.count += 1

def Decrement_counter():
    if x=='15':
        st.session_state.count -= 15
    if x=='8':
        st.session_state.count -= 8
    if x=='7':
        st.session_state.count -= 7
    if x=='6':
        st.session_state.count -= 6
    if x=='5':
        st.session_state.count -= 5
    if x=='4':
        st.session_state.count -= 4
    if x=='3':
        st.session_state.count -= 3
    if x=='2':
        st.session_state.count -= 2
    if x=='1':
        st.session_state.count -= 1
with col1:
    st.button('Add+', on_click=increment_counter)
with col2:
    st.button('Sub-', on_click=Decrement_counter)

# st.write('Count = ', st.session_state.count)




# if 'count' not in st.session_state:
#     st.session_state.count = 0

# def inc():
#     st.session_state.count += 1

# bt = st.button("1",on_click=inc)
# st.write(" Count = ", st.session_state.count)
def cng():
    add_s = pd.read_csv("Player.csv")
    core = add_s.loc[add_s.Name == bn ,"Score"]
    count_add =  st.session_state.count = core
    add_s.loc[add_s.Name == bn ,"Score"] = count_add
    add_s.to_csv('Player.csv', index=False)
    # st.write(add_s)

# ascore = st.checkbox("To Add Score")
# if ascore:

add_score = pd.read_csv("Player.csv")
bn = st.radio("",(add_score.values),horizontal=True)
add_s = pd.read_csv("Player.csv")
core = add_s.loc[add_s.Name == bn ,"Score"]
count_add =  st.session_state.count
cd = count_add + core
add_s.loc[add_s.Name == bn ,"Score"] = cd
add_s.to_csv('Player.csv', index=False)
st.session_state.count = 0

colrd, colrd1 = st.columns([0.2,0.7])
with colrd:
    rdd = st.checkbox('RD + 1')
    if rdd:
        num3 = add_s.loc[add_s.Name == bn ,"RD"]
        cd3 = num3 + 1
        add3 = add_s.loc[add_s.Name == bn ,"RD"] = cd3
        add_s.to_csv('Player.csv', index=False)
        st.session_state.count = 0

with colrd1:
    rdd2 = st.checkbox('RD - 1')
    if rdd2:
        num3 = add_s.loc[add_s.Name == bn ,"RD"]
        cd3 = num3 - 1
        add3 = add_s.loc[add_s.Name == bn ,"RD"] = cd3
        add_s.to_csv('Player.csv', index=False)
        st.session_state.count = 0





    # num2 = st.number_input("",value=float(core2))
    # if num2:
    #     cd2 = num2 + core2
    #     add_s.loc[add_s.Name == bn ,"RD"] = cd2

    # st.write(core2)
    # count_add2 =  st.session_state.count
    # st.write(count_add2)
    # cd2 = count_add2 + core2
    # add_s.loc[add_s.Name == bn ,"RD"] = cd2





    


    # calcu = add_score.loc[add_score.Name == bn ,"Score"] = count_add
    # if calcu:
    #     full = (calcu + core)
    #     print(full)
    
st.write('Click player name to make the changes to Score/RD')    
daa = pd.read_csv("Player.csv")
st.markdown(daa.style.hide(axis="index").to_html(), unsafe_allow_html=True)







colx, coly = st.columns(2)

with colx:
    
    
    st.write('')
    st.write('')
    st.write('')
    st.write('')

colm1, colm2 = st.columns([0.2,0.4])


if 'my_text' not in st.session_state:
    st.session_state.my_text = ""

def add():
    x1 = st.session_state['pat']
    

        
    # st.write(x1)

with colm2:
    a1 = st.button("Add Players Name", on_click=add, key='pat')
    st.button("Refresh")
with colm1:
    a = st.text_input('',placeholder="Add Players Name..." ,on_change=add )
my_text = st.session_state.my_text
# st.write(my_text)

emp = ([a,0,0])

if a1:
    with open('Player.csv','a', newline='') as file:
        # emp.append(my_text)
        writer = csv.writer(file)
        writer.writerow(emp)
        



rmo = st.checkbox("To remove the Player...")
if rmo:
    st.write("Selected player, Check and Uncheck the check_box to remove the Player...")
    remov1 = pd.read_csv("Player.csv", index_col='Name')
    remov2 = pd.read_csv("Player.csv")
    xnam = st.radio(" ",(remov2.values),horizontal=True)
    dele = st.checkbox("Check to remove",key=xnam)
    if dele:
        remov1.drop([xnam], inplace= True)
        remov1.to_csv('Player.csv')
    






# daa.loc[daa.Name == 'Fash' ,"Score"] = 100
# daa.to_csv("Player.csv" , index=False)


# def removee():

# st.markdown(daa.style.hide(axis="index").to_html(), unsafe_allow_html=True)



# check1 = st.checkbox("To Remove Player...")
# if check1:
#     remov1 = pd.read_csv("Player.csv", index_col='Name')
#     # remov1.drop(['Avni'], inplace=True)
#     # st.write(remov1)

#     bn1 = st.radio(" ",(remov1.values),horizontal=True)
#     if bn1:
#         ch = st.checkbox(bn1, key=bn1)
#         if ch:
#             try:
#                 remov1.drop([bn1],axis=1, inplace=True)
#                 remov1.to_csv('Player.csv', index=False)
#                 st.write(remov1)
#             except KeyError:
#                 st.write('Cant Remove The Player Please Try After Sometime ')
            



# st.write(daa)


    # x = remov1.loc[remov1.Name == ch]   
    # print(x)
    
    # remov1.drop([ch], axis=1, inplace=True)
    # st.write(remov1)

# print(bn1)

# if check:
#     rem = st.radio(" ",(remov.values), on_change= removee,horizontal=True)




# Imp *****************************************************************
# df = pd.read_csv('Player.csv')
# df.replace(to_replace ="Fashion",  
#                  value = "Fash",  
#                   inplace = True)   

# df.to_csv('Player.csv', index=False)

# Imp *****************************************************************


# st.write(daa)



# if 'my_text' not in st.session_state:
#     st.session_state.my_text = ''
# def add():
#     st.session_state.my_text = st.session_state.pat
#     st.session_state.pat = ''
    


# Imp *****************************

# data = pd.read_csv('Player.csv')

# data_top = data.head() 
   
# bn = list(data_top.values)
# st.write(bn)


    # st.write(d)
    

# check1 = st.checkbox("To Remove Player...")
# if check1:
# xnam = st.radio(" ",(remov1.values),horizontal=True)
# dele = st.checkbox("Check to remove",key=xnam)
# rdata = pd.read_csv("Player.csv", index_col=1)
# if dele:
# remov1.drop([xnam], inplace= True)
# remov1.to_csv('Player.csv')

    

        


# if check1:
#     remov1 = pd.read_csv("Player.csv", index_col='Name')
#     # remov1.drop(['Avni'], inplace=True)
#     # st.write(remov1)

#     bn1 = st.radio(" ",(remov1.values),horizontal=True)
#     if bn1:
#         ch = st.checkbox(bn1, key=bn1)
#         if ch:
#             try:
#                 remov1.drop([bn1],axis=1, inplace=True)
#                 remov1.to_csv('Player.csv', index=False)
#                 st.write(remov1)
#             except KeyError:
#                 st.write('Cant Remove The Player Please Try After Sometime ')
            


