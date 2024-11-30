import pandas as pd
import pymysql
import streamlit as st
from streamlit_option_menu import option_menu
#import plotly.express as px 

#APSRTC bus route
lists_A=[]
df_A=pd.read_csv(r"C:\Users\vasan\Desktop\route\route1.csv")
for i,r in df_A.iterrows():
    lists_A.append(r["Route_name"])
    
#KERALA bus route
lists_K=[]
df_k=pd.read_csv(r"C:\Users\vasan\Desktop\route\route2.csv")
for i,r in df_k.iterrows():
    lists_K.append(r["Route_name"])
    
    #TSRTC bus route
lists_T=[]
df_T=pd.read_csv(r"C:\Users\vasan\Desktop\route\route3.csv")
for i,r in df_T.iterrows():
    lists_T.append(r["Route_name"])
    
    #RSRTC bus route
lists_R=[]
df_R=pd.read_csv(r"C:\Users\vasan\Desktop\route\route4.csv")
for i,r in df_R.iterrows():
    lists_R.append(r["Route_name"])
    
    #SBSTC bus route
lists_S=[]
df_S=pd.read_csv(r"C:\Users\vasan\Desktop\route\route5.csv")
for i,r in df_S.iterrows():
    lists_S.append(r["Route_name"])
    
    #HRTC bus route
lists_H=[]
df_H=pd.read_csv(r"C:\Users\vasan\Desktop\route\route6.csv")
for i,r in df_H.iterrows():
    lists_H.append(r["Route_name"])
    
    #UPSRTC bus route
lists_U=[]
df_U=pd.read_csv(r"C:\Users\vasan\Desktop\route\route7.csv")
for i,r in df_U.iterrows():
    lists_U.append(r["Route_name"])
    
    #WBTC bus route
lists_W=[]
df_W=pd.read_csv(r"C:\Users\vasan\Desktop\route\route8.csv")
for i,r in df_W.iterrows():
    lists_W.append(r["Route_name"])
    
    #PEPSU bus route
lists_P=[]
df_P=pd.read_csv(r"C:\Users\vasan\Desktop\route\route9.csv")
for i,r in df_P.iterrows():
    lists_P.append(r["Route_name"])
    
    #WBSTC bus route
lists_WB=[]
df_WB=pd.read_csv(r"C:\Users\vasan\Desktop\route\route10.csv")
for i,r in df_WB.iterrows():
    lists_WB.append(r["Route_name"])
    
    #STREAMLIT PAGE

st.set_page_config(layout="wide")

web=option_menu(menu_title="🔴OnlineBus🚌",
                options=["🏡Home","📌States and Routes"],
                icons=[":house:","info-circle"],
                orientation="horizontal"
                
                
                )
#home page setting
if web == "🏡Home":
    st.image(r"C:\Users\vasan\Pictures\Redbus_logo.jpg",width=200)
    st.title(":red[Redbus Data Scraping with Selenium & Dynamic Filtering using Streamlit]")
    st.video(r"C:\Users\vasan\Pictures\redBus_Hire___Product_Video(1080p).mp4")
    st.image(r"C:\Users\vasan\Pictures\Screenshots\redbuslogo.png",width=200)
    st.markdown("[⬇️Download Redbus app](https://play.google.com/store/apps/details?id=in.redbus.android&hl=en_IN&pli=1)")
    st.subheader(":red[Domain:] Transportion")
    st.subheader(":red[Ojective: ]")
    st.markdown(" The 'Redbus Data Scraping and Filtering with Streamlit Application' aims to revolutionize the transportation industry by providing a comprehensive solution for collecting, analyzing, and visualizing bus travel data. By utilizing Selenium for web scraping, this project automates the extraction of detailed information from Redbus, including bus routes, schedules, prices, and seat availability.")
    st.subheader(":red[Overview: ]")
    st.markdown("selenium : selenium is atool used for automating web browsers. It is commonly used for web scraping, which involves extractig data from websites.")
    st.markdown("Pandas : Pandas is a popular open-source library in Python for data manipulation and analysis. It provides data structures and tools to efficiently handle and process structured data, such as datasets stored in spreadsheets or databases. Pandas is built on top of NumPy, and it is widely used in data science, machine learning, and statistical analysis.")
    st.markdown("MySQL : MySQL is an open-source relational database management system (RDBMS) that uses Structured Query Language (SQL) for managing and manipulating data. It is widely used in web applications, data storage, and analytics due to its speed, reliability, and ease of use.")
    st.markdown("Streamlit : Streamlit is an open-source Python library designed for creating interactive, data-driven web applications with ease. It is widely used in data science and machine learning projects to build dashboards and visualization tools. Streamlit simplifies the process of turning Python scripts into web apps without requiring extensive knowledge of web development frameworks like HTML, CSS, or JavaScript.")
    st.subheader(":red[Skill-taken:]") 
    st.markdown("selenium, python, pandas, MYSQL,mysql-connector-python,Streamlit.")
    st.subheader(":red[Devaloped-by:] G.Vasanth Raj")
    
#state & Route page setting..
if web =="📌States and Routes":
    s=st.selectbox("List of States",["Andhra Pradesh","Kerala","Telangana","Rajasthan",
                                     "South Bengal","Himachal","Uttar Pradesh","West Bangal(CTC)","Panjab","WBSTC"])
    select_fare=st.radio("Choose bus fare range",("40-1000","1000-2000","2000 and above"))
    
    #Andhara pradesh 1
    if s=="Andhra Pradesh":
        A=st.selectbox("List of routes",lists_A)
        
        if select_fare=="40-1000":
            conn=pymysql.connect(host="localhost", user="root",password="14201420vj",database="redbus_details")
            my_cursor = conn.cursor()
            query=f'''select * from redbus_details.bus_routedetails 
                               where price Between 40 and 1000 and Route_name="{A}"
                               order by price desc'''
            my_cursor.execute(query)
            out=my_cursor.fetchall()
            df=pd.DataFrame(out,columns=["Route_name","Route_link","Bus_name","Bus_type","Departing_time",
                                      "Duration","Reach_time","Star_rating","price","Seat_available"])
            st.write(df)
        
        if select_fare=="1000-2000":
            conn=pymysql.connect(host="localhost", user="root",password="14201420vj",database="redbus_details")
            my_cursor = conn.cursor()
            query=f'''select * from redbus_details.bus_routedetails 
                               where price Between 1000 and 2000 and Route_name ="{A}"
                               order by price desc '''
            my_cursor.execute(query)
            out=my_cursor.fetchall()
            df=pd.DataFrame(out,columns=["Route_name","Route_link","Bus_name","Bus_type","Departing_time",
                                      "Duration","Reach_time","Star_rating","price","Seat_available"])
            st.write(df)
        
        if select_fare=="2000 and above":
            conn=pymysql.connect(host="localhost", user="root",password="14201420vj",database="redbus_details")
            my_cursor = conn.cursor()
            query=f'''select * from redbus_details.bus_routedetails 
                               where price > 2000 and Route_name ="{A}"
                               order by price desc '''
            my_cursor.execute(query)
            out=my_cursor.fetchall()
            df=pd.DataFrame(out,columns=["Route_name","Route_link","Bus_name","Bus_type","Departing_time",
                                      "Duration","Reach_time","Star_rating","price","Seat_available"])
            st.write(df)
 
            #Karala 2
    if s=="Kerala":
        K=st.selectbox("List of routes",lists_K)
        
        if select_fare=="40-1000":
            conn=pymysql.connect(host="localhost", user="root",password="14201420vj",database="redbus_details")
            my_cursor = conn.cursor()
            query=f'''select * from redbus_details.bus_routedetails 
                               where price Between 40 and 1000 and Route_name="{K}"
                               order by price desc'''
            my_cursor.execute(query)
            out=my_cursor.fetchall()
            df=pd.DataFrame(out,columns=["Route_name","Route_link","Bus_name","Bus_type","Departing_time",
                                      "Duration","Reach_time","Star_rating","price","Seat_available"])
            st.write(df)
        
        if select_fare=="1000-2000":
            conn=pymysql.connect(host="localhost", user="root",password="14201420vj",database="redbus_details")
            my_cursor = conn.cursor()
            query=f'''select * from redbus_details.bus_routedetails 
                               where price Between 1000 and 2000 and Route_name ="{K}"
                               order by price desc '''
            my_cursor.execute(query)
            out=my_cursor.fetchall()
            df=pd.DataFrame(out,columns=["Route_name","Route_link","Bus_name","Bus_type","Departing_time",
                                      "Duration","Reach_time","Star_rating","price","Seat_available"])
            st.write(df)
        
        if select_fare=="2000 and above":
            conn=pymysql.connect(host="localhost", user="root",password="14201420vj",database="redbus_details")
            my_cursor = conn.cursor()
            query=f'''select * from redbus_details.bus_routedetails 
                               where price > 2000 and Route_name ="{K}"
                               order by price desc '''
            my_cursor.execute(query)
            out=my_cursor.fetchall()
            df=pd.DataFrame(out,columns=["Route_name","Route_link","Bus_name","Bus_type","Departing_time",
                                      "Duration","Reach_time","Star_rating","price","Seat_available"])
            st.write(df)
        
                
    #Telangana 3
    if s=="Telangana":
        T=st.selectbox("List of routes",lists_T)
        
        if select_fare=="40-1000":
            conn=pymysql.connect(host="localhost", user="root",password="14201420vj",database="redbus_details")
            my_cursor = conn.cursor()
            query=f'''select * from redbus_details.bus_routedetails 
                               where price Between 40 and 1000 and Route_name="{T}"
                               order by price desc'''
            my_cursor.execute(query)
            out=my_cursor.fetchall()
            df=pd.DataFrame(out,columns=["Route_name","Route_link","Bus_name","Bus_type","Departing_time",
                                      "Duration","Reach_time","Star_rating","price","Seat_available"])
            st.write(df)
        
        if select_fare=="1000-2000":
            conn=pymysql.connect(host="localhost", user="root",password="14201420vj",database="redbus_details")
            my_cursor = conn.cursor()
            query=f'''select * from redbus_details.bus_routedetails 
                               where price Between 1000 and 2000 and Route_name ="{T}"
                               order by price desc '''
            my_cursor.execute(query)
            out=my_cursor.fetchall()
            df=pd.DataFrame(out,columns=["Route_name","Route_link","Bus_name","Bus_type","Departing_time",
                                      "Duration","Reach_time","Star_rating","price","Seat_available"])
            st.write(df)
        
        if select_fare=="2000 and above":
            conn=pymysql.connect(host="localhost", user="root",password="14201420vj",database="redbus_details")
            my_cursor = conn.cursor()
            query=f'''select * from redbus_details.bus_routedetails 
                               where price > 2000 and Route_name ="{T}"
                               order by price desc '''
            my_cursor.execute(query)
            out=my_cursor.fetchall()
            df=pd.DataFrame(out,columns=["Route_name","Route_link","Bus_name","Bus_type","Departing_time",
                                      "Duration","Reach_time","Star_rating","price","Seat_available"])
            st.write(df)

    #Rajasthan 4
    if s=="Rajasthan":
        R=st.selectbox("List of routes",lists_R)
        
        if select_fare=="40-1000":
            conn=pymysql.connect(host="localhost", user="root",password="14201420vj",database="redbus_details")
            my_cursor = conn.cursor()
            query=f'''select * from redbus_details.bus_routedetails 
                               where price Between 40 and 1000 and Route_name="{R}"
                               order by price desc'''
            my_cursor.execute(query)
            out=my_cursor.fetchall()
            df=pd.DataFrame(out,columns=["Route_name","Route_link","Bus_name","Bus_type","Departing_time",
                                      "Duration","Reach_time","Star_rating","price","Seat_available"])
            st.write(df)
        
        if select_fare=="1000-2000":
            conn=pymysql.connect(host="localhost", user="root",password="14201420vj",database="redbus_details")
            my_cursor = conn.cursor()
            query=f'''select * from redbus_details.bus_routedetails 
                               where price Between 1000 and 2000 and Route_name ="{R}"
                               order by price desc '''
            my_cursor.execute(query)
            out=my_cursor.fetchall()
            df=pd.DataFrame(out,columns=["Route_name","Route_link","Bus_name","Bus_type","Departing_time",
                                      "Duration","Reach_time","Star_rating","price","Seat_available"])
            st.write(df)
        
        if select_fare=="2000 and above":
            conn=pymysql.connect(host="localhost", user="root",password="14201420vj",database="redbus_details")
            my_cursor = conn.cursor()
            query=f'''select * from redbus_details.bus_routedetails 
                               where price > 2000 and Route_name ="{R}"
                               order by price desc '''
            my_cursor.execute(query)
            out=my_cursor.fetchall()
            df=pd.DataFrame(out,columns=["Route_name","Route_link","Bus_name","Bus_type","Departing_time",
                                      "Duration","Reach_time","Star_rating","price","Seat_available"])
            st.write(df)

    #South Bengal 5
    if s=="South Bengal":
        S=st.selectbox("List of routes",lists_S)
        
        if select_fare=="40-1000":
            conn=pymysql.connect(host="localhost", user="root",password="14201420vj",database="redbus_details")
            my_cursor = conn.cursor()
            query=f'''select * from redbus_details.bus_routedetails 
                               where price Between 40 and 1000 and Route_name="{S}"
                               order by price desc'''
            my_cursor.execute(query)
            out=my_cursor.fetchall()
            df=pd.DataFrame(out,columns=["Route_name","Route_link","Bus_name","Bus_type","Departing_time",
                                      "Duration","Reach_time","Star_rating","price","Seat_available"])
            st.write(df)
        
        if select_fare=="1000-2000":
            conn=pymysql.connect(host="localhost", user="root",password="14201420vj",database="redbus_details")
            my_cursor = conn.cursor()
            query=f'''select * from redbus_details.bus_routedetails 
                               where price Between 1000 and 2000 and Route_name ="{S}"
                               order by price desc '''
            my_cursor.execute(query)
            out=my_cursor.fetchall()
            df=pd.DataFrame(out,columns=["Route_name","Route_link","Bus_name","Bus_type","Departing_time",
                                      "Duration","Reach_time","Star_rating","price","Seat_available"])
            st.write(df)
        
        if select_fare=="2000 and above":
            conn=pymysql.connect(host="localhost", user="root",password="14201420vj",database="redbus_details")
            my_cursor = conn.cursor()
            query=f'''select * from redbus_details.bus_routedetails 
                               where price > 2000 and Route_name ="{S}"
                               order by price desc '''
            my_cursor.execute(query)
            out=my_cursor.fetchall()
            df=pd.DataFrame(out,columns=["Route_name","Route_link","Bus_name","Bus_type","Departing_time",
                                      "Duration","Reach_time","Star_rating","price","Seat_available"])
            st.write(df)    
            
            
    #Himachal 6
    if s=="Himachal":
        H=st.selectbox("List of routes",lists_H)
        
        if select_fare=="40-1000":
            conn=pymysql.connect(host="localhost", user="root",password="14201420vj",database="redbus_details")
            my_cursor = conn.cursor()
            query=f'''select * from redbus_details.bus_routedetails 
                               where price Between 40 and 1000 and Route_name="{H}"
                               order by price desc'''
            my_cursor.execute(query)
            out=my_cursor.fetchall()
            df=pd.DataFrame(out,columns=["Route_name","Route_link","Bus_name","Bus_type","Departing_time",
                                      "Duration","Reach_time","Star_rating","price","Seat_available"])
            st.write(df)
        
        if select_fare=="1000-2000":
            conn=pymysql.connect(host="localhost", user="root",password="14201420vj",database="redbus_details")
            my_cursor = conn.cursor()
            query=f'''select * from redbus_details.bus_routedetails 
                               where price Between 1000 and 2000 and Route_name ="{H}"
                               order by price desc '''
            my_cursor.execute(query)
            out=my_cursor.fetchall()
            df=pd.DataFrame(out,columns=["Route_name","Route_link","Bus_name","Bus_type","Departing_time",
                                      "Duration","Reach_time","Star_rating","price","Seat_available"])
            st.write(df)
        
        if select_fare=="2000 and above":
            conn=pymysql.connect(host="localhost", user="root",password="14201420vj",database="redbus_details")
            my_cursor = conn.cursor()
            query=f'''select * from redbus_details.bus_routedetails 
                               where price > 2000 and Route_name ="{H}"
                               order by price desc '''
            my_cursor.execute(query)
            out=my_cursor.fetchall()
            df=pd.DataFrame(out,columns=["Route_name","Route_link","Bus_name","Bus_type","Departing_time",
                                      "Duration","Reach_time","Star_rating","price","Seat_available"])
            st.write(df)


    #Uttar Pradesh 7
    if s=="Uttar Pradesh":
        U=st.selectbox("List of routes",lists_U)
        
        if select_fare=="40-1000":
            conn=pymysql.connect(host="localhost", user="root",password="14201420vj",database="redbus_details")
            my_cursor = conn.cursor()
            query=f'''select * from redbus_details.bus_routedetails 
                               where price Between 40 and 1000 and Route_name="{U}"
                               order by price desc'''
            my_cursor.execute(query)
            out=my_cursor.fetchall()
            df=pd.DataFrame(out,columns=["Route_name","Route_link","Bus_name","Bus_type","Departing_time",
                                      "Duration","Reach_time","Star_rating","price","Seat_available"])
            st.write(df)
        
        if select_fare=="1000-2000":
            conn=pymysql.connect(host="localhost", user="root",password="14201420vj",database="redbus_details")
            my_cursor = conn.cursor()
            query=f'''select * from redbus_details.bus_routedetails 
                               where price Between 1000 and 2000 and Route_name ="{U}"
                               order by price desc '''
            my_cursor.execute(query)
            out=my_cursor.fetchall()
            df=pd.DataFrame(out,columns=["Route_name","Route_link","Bus_name","Bus_type","Departing_time",
                                      "Duration","Reach_time","Star_rating","price","Seat_available"])
            st.write(df)
        
        if select_fare=="2000 and above":
            conn=pymysql.connect(host="localhost", user="root",password="14201420vj",database="redbus_details")
            my_cursor = conn.cursor()
            query=f'''select * from redbus_details.bus_routedetails 
                               where price > 2000 and Route_name ="{U}"
                               order by price desc '''
            my_cursor.execute(query)
            out=my_cursor.fetchall()
            df=pd.DataFrame(out,columns=["Route_name","Route_link","Bus_name","Bus_type","Departing_time",
                                      "Duration","Reach_time","Star_rating","price","Seat_available"])
            st.write(df)
            
            
    #West Bangal(CTC) 8
    if s=="West Bangal(CTC)":
        W=st.selectbox("List of routes",lists_W)
        
        if select_fare=="40-1000":
            conn=pymysql.connect(host="localhost", user="root",password="14201420vj",database="redbus_details")
            my_cursor = conn.cursor()
            query=f'''select * from redbus_details.bus_routedetails 
                               where price Between 40 and 1000 and Route_name="{W}"
                               order by price desc'''
            my_cursor.execute(query)
            out=my_cursor.fetchall()
            df=pd.DataFrame(out,columns=["Route_name","Route_link","Bus_name","Bus_type","Departing_time",
                                      "Duration","Reach_time","Star_rating","price","Seat_available"])
            st.write(df)
        
        if select_fare=="1000-2000":
            conn=pymysql.connect(host="localhost", user="root",password="14201420vj",database="redbus_details")
            my_cursor = conn.cursor()
            query=f'''select * from redbus_details.bus_routedetails 
                               where price Between 1000 and 2000 and Route_name ="{W}"
                               order by price desc '''
            my_cursor.execute(query)
            out=my_cursor.fetchall()
            df=pd.DataFrame(out,columns=["Route_name","Route_link","Bus_name","Bus_type","Departing_time",
                                      "Duration","Reach_time","Star_rating","price","Seat_available"])
            st.write(df)
        
        if select_fare=="2000 and above":
            conn=pymysql.connect(host="localhost", user="root",password="14201420vj",database="redbus_details")
            my_cursor = conn.cursor()
            query=f'''select * from redbus_details.bus_routedetails 
                               where price > 2000 and Route_name ="{W}"
                               order by price desc '''
            my_cursor.execute(query)
            out=my_cursor.fetchall()
            df=pd.DataFrame(out,columns=["Route_name","Route_link","Bus_name","Bus_type","Departing_time",
                                      "Duration","Reach_time","Star_rating","price","Seat_available"])
            st.write(df)
            

    #Panjab 9
    if s=="Panjab":
        P=st.selectbox("List of routes",lists_P)
        
        if select_fare=="40-1000":
            conn=pymysql.connect(host="localhost", user="root",password="14201420vj",database="redbus_details")
            my_cursor = conn.cursor()
            query=f'''select * from redbus_details.bus_routedetails 
                               where price Between 40 and 1000 and Route_name="{P}"
                               order by price desc'''
            my_cursor.execute(query)
            out=my_cursor.fetchall()
            df=pd.DataFrame(out,columns=["Route_name","Route_link","Bus_name","Bus_type","Departing_time",
                                      "Duration","Reach_time","Star_rating","price","Seat_available"])
            st.write(df)
        
        if select_fare=="1000-2000":
            conn=pymysql.connect(host="localhost", user="root",password="14201420vj",database="redbus_details")
            my_cursor = conn.cursor()
            query=f'''select * from redbus_details.bus_routedetails 
                               where price Between 1000 and 2000 and Route_name ="{P}"
                               order by price desc '''
            my_cursor.execute(query)
            out=my_cursor.fetchall()
            df=pd.DataFrame(out,columns=["Route_name","Route_link","Bus_name","Bus_type","Departing_time",
                                      "Duration","Reach_time","Star_rating","price","Seat_available"])
            st.write(df)
        
        if select_fare=="2000 and above":
            conn=pymysql.connect(host="localhost", user="root",password="14201420vj",database="redbus_details")
            my_cursor = conn.cursor()
            query=f'''select * from redbus_details.bus_routedetails 
                               where price > 2000 and Route_name ="{P}"
                               order by price desc '''
            my_cursor.execute(query)
            out=my_cursor.fetchall()
            df=pd.DataFrame(out,columns=["Route_name","Route_link","Bus_name","Bus_type","Departing_time",
                                      "Duration","Reach_time","Star_rating","price","Seat_available"])
            st.write(df)


    #WBSTC 10
    if s=="WBSTC":
        WB=st.selectbox("List of routes",lists_WB)
        
        if select_fare=="40-1000":
            conn=pymysql.connect(host="localhost", user="root",password="14201420vj",database="redbus_details")
            my_cursor = conn.cursor()
            query=f'''select * from redbus_details.bus_routedetails 
                               where price Between 40 and 1000 and Route_name="{WB}"
                               order by price desc'''
            my_cursor.execute(query)
            out=my_cursor.fetchall()
            df=pd.DataFrame(out,columns=["Route_name","Route_link","Bus_name","Bus_type","Departing_time",
                                      "Duration","Reach_time","Star_rating","price","Seat_available"])
            st.write(df)
        
        if select_fare=="1000-2000":
            conn=pymysql.connect(host="localhost", user="root",password="14201420vj",database="redbus_details")
            my_cursor = conn.cursor()
            query=f'''select * from redbus_details.bus_routedetails 
                               where price Between 1000 and 2000 and Route_name ="{WB}"
                               order by price desc '''
            my_cursor.execute(query)
            out=my_cursor.fetchall()
            df=pd.DataFrame(out,columns=["Route_name","Route_link","Bus_name","Bus_type","Departing_time",
                                      "Duration","Reach_time","Star_rating","price","Seat_available"])
            st.write(df)
        
        if select_fare=="2000 and above":
            conn=pymysql.connect(host="localhost", user="root",password="14201420vj",database="redbus_details")
            my_cursor = conn.cursor()
            query=f'''select * from redbus_details.bus_routedetails 
                               where price > 2000 and Route_name ="{WB}"
                               order by price desc '''
            my_cursor.execute(query)
            out=my_cursor.fetchall()
            df=pd.DataFrame(out,columns=["Route_name","Route_link","Bus_name","Bus_type","Departing_time",
                                      "Duration","Reach_time","Star_rating","price","Seat_available"])
            st.write(df)