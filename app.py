import webbrowser
import streamlit as st
import random

st.title("Visual versus Text Attribute Representation in Choice Experiments")
st.write("As a part of neuroeconomics course we are condicting a survey to analyze the effect of visual and text treatment on willing to pay (WTP) for food products on online deivery platforms.")
# st.write("The aim of this survey is to collect data to analyze the effect of text and visual treatment on willingness to pay (WTP) for food products available on online delivery platforms.")
st.write("The survey is anonymous and will take around 3 min to fill.")
st.write("Please click on the link below to redirect to the from.")
# result = st.button("Click here")
# if result:
#     st.write("Thank you! :smile:")
# url = 'https://www.streamlit.io/'
# if st.button('Open browser'):
#     webbrowser.open_new_tab(url)

link1 = '[Form - Text Attribute](https://forms.gle/JuSfjLu5USQR8SWw7)'
link2 = '[Form - Visual Attribute](https://forms.gle/A6opEmMgk8Nmq9Tp7)'
# a = random.uniform(0, 1)
a = random.randint(0, 10**5)/ 10**5
print(a)
if a < 0.5:
    link = link1
else:
    link = link2
st.markdown(link, unsafe_allow_html=True)