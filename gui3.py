# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 10:08:56 2020

@author: Prathmesh
"""


import streamlit as st
import pickle

pik = open('latest.p', 'rb')
model = pickle.load(pik)




def main():
    
    st.title("Loan Approval Prediction")
    print('')
    
    st.image('img.jpg')
    
    st.subheader('Please Enter Your Name')
    
    nm = st.text_input('')
    st.write(nm)
    
    st.subheader('Please Enter Your Gender')
    gen = st.selectbox(' ', ['select','Female', 'Male']) 
    
    if gen == 'Female':
        gen1 = 0
        st.write(gen)
    
    elif gen == 'Male':
        gen1 = 1
        st.write(gen)
        
    else:
        st.write('Please''\n' +gen+' a option')
        
    
    
    
    st.subheader(' Enter Applicant Income')
    
    an = st.number_input(label = '')
    an = round(an)
    st.write(an)
    
    st.subheader(' Enter Coapplicant Income')
    
    cn = st.number_input(label = '',key = 2)
    #cn = round(cn)
    st.write(cn)
    
    st.subheader('Enter the amount you want')
    
    fa = st.slider('',17000,700000)
    #fa = round(cn)
    st.write(fa)
    
    st.subheader('Enter your credit history (1 = Yes, 0 = No)')
    cr = st.selectbox(' ', ['select',1, 0])
    
    if cr == 1:
        cr = 1.0 
        st.write(cr)
        
    elif cr == 0:
        cr = 0.0
        st.write(cr)
    else:
        st.write('Please''\n' +cr+' a option')
        

    
    st.subheader('Enter the loan amount term')
    lmt = st.selectbox(' ', ['select', '4 months', '6 months', '8 months', '10 months', '1 year', '1.5 years'])
    
    if lmt =='4 months':
        lmt1 = 120.0
        st.write(lmt)
    
    elif lmt == '6 months':
        lmt1 = 180.0
        st.write(lmt)
        
    elif lmt == '8 months':
        lmt1 = 240.0
        st.write(lmt)
        
    elif lmt == '10 months':
        lmt1 = 300
        st.write(lmt)
       
    elif lmt == '1 year':
        lmt1 = 360.0
        st.write(lmt)
        
    elif lmt == '1.5 years':
        lmt1 = 480.0
        st.write(lmt)
    
    else:
        st.write('Please''\n' +lmt+' a option')
        
       
       
        
    
    
    st.subheader('Please Enter Your Maritial Status')
    sta = st.selectbox(' ', ['select', 'Married', 'Single'], key = 6)
    
    if sta == 'Married':
        sta1 = 1
        st.write(sta)
    
    elif sta == 'Single':
        sta1 = 0
        st.write(sta)
        
    else:
        st.write('Please''\n' +sta+' a option')
        
    
    
    st.subheader('Please enter the number of dependents you have')
    dep = st.selectbox(' ', ['select', '0', '1', '2', '3+'])
    
    if dep == '0':
        
        dep0 = 1
        dep1 = 0
        dep2 = 0
        dep3 = 0
        st.write(dep)
    
    elif dep == '1':
        
        dep0 = 0
        dep1 = 1
        dep2 = 0
        dep3 = 0
        st.write(dep)
        
    elif dep == '2':
        
        dep0 = 0
        dep1 = 0
        dep2 = 1
        dep3 = 0
        st.write(dep)
    
    elif dep == '3+':
        
        dep0 = 0
        dep1 = 0
        dep2 = 0
        dep3 = 1
        st.write(dep)
        
    
    else:
        
        st.write('Please''\n' +dep+' a option')
        
        
        
        
        
    st.subheader('Have you compleated your graduation?')
    edu = st.selectbox(' ', ['select', 'Yes', 'No'])
    
    if edu == 'Yes':
        edu1 = 0
        st.write(edu)
    elif edu == 'No':
        edu1 = 1
        st.write(edu)
    else:
        st.write('Please''\n' +edu+' a option')
        
    
    st.subheader('Are you self-employed?')
    emp = st.selectbox(' ', ['select', 'Yes', 'No'], key = 8)
    
    if emp == 'Yes':
        emp1 = 1
        st.write(emp)
    elif emp == "No":
        emp1 = 0
        st.write(emp)
    
    else:
        st.write('Please''\n' +emp+' a option')
    
    
    
    
    try:
        
        
        output = model.predict([[an,cn,lmt1,cr,gen1,sta1,dep0,dep1,dep2,dep3,edu1,emp1,fa]])
        
        if st.button('Click to check'):
            if output == 1:
                opp = 'You are eligable to get the loan'
                st.success(opp)
            else:
                opp = 'Sorry you are not eligable to get the loan'
                st.error(opp)
    
    except Exception as e:
         
         st.write('Please enter the required fields')
         #st.write(e)
        
    
  
    
    
    
    
    
    
    
    
    
    
    
if __name__ == '__main__':
    main()