import requests
from bs4 import BeautifulSoup as bs
import lxml.etree as xml
import lxml
import streamlit as st
import time


st.title("This is the simplest web dictionary")
st.subheader("This dictionary gives you the most common meaning of the word your enter")
st.subheader("And in some cases, it also gives you a simple sentence for the use of that word")



word = st.text_input("")
# st.text("The most common meaning  of the word is: ")
# word = input('enter the word: ')
try:
    url = f'https://www.dictionary.com/browse/{word}?s=t'
    web_page = bs(requests.get(url, {}).text, "lxml")
    meanings = web_page.find_all('div', attrs={'class': 'css-1ghs5zt e1q3nk1v2'})
    # print('\nThe meaning(s) of the word is: ')
    # for all the meanings
    # for meaning in meanings:
    #   print('* '+ meaning.text)
    #   print('\n')

    common_meaning = meanings[0].text
    try:
        m = common_meaning.split(':')[0]
        sentence = common_meaning.split(':')[1]
        st.subheader("The meaning is: ")
        st.write(m)
        st.subheader("And the sentence is ")
        st.write(sentence)
    except:
        # for most common meaning
        # print(meanings[0].text)
        st.write(common_meaning)

except:
    st.markdown("### Enter the word: ")
time.sleep(1)

st.sidebar.markdown('''
created by Sanket Chavan 
''')

st.sidebar.markdown('''
Connect on <a href = "https://www.linkedin.com/in/sanket-chavan5595/"> Linkedin </a>
''', True)