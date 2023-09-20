import streamlit as st

st.set_page_config(page_title="Hello World Demo", page_icon=":smiley:", layout="wide")
st.title("This is app title") 
st.write("Hello world in plain text") 
st.header("This is header") 
st.subheader("This is subheader")
st.text("This is text") 
st.markdown("This is markdown") 
st.markdown("**This is markdown**") 
st.success("Success") 
st.info("Info")
st.warning("Warning") 
st.error("Error")
st.warning("Warning")
st.error("Error")
st.exception(RuntimeError("This is exception"))

st.divider()

t=st.empty()

def login_function(usr,pwd):
    if usr == 'Sarathi' and pwd == 'admin':
      st.session_state['Loggedin'] = True    
      st.success('You are logged in. Welcome {}!'.format(usr))
      st.balloons()
      t.write("You are logged in. Welcome!")
    else:
      st.error('Invalid username or password')

if 'Loggedin' not in st.session_state:
    t.write('You are not loggedin')
    
    usr=st.text_input("Username")
    pwd=st.text_input("Password",type="password")
    st.button('Login now',on_click=login_function(usr,pwd))
    

st.divider()

name = st.text_input('Name')

if not name:
  st.warning('Please type in a name.')
  st.stop()

st.success('Welcome {}!'.format(name))
st.divider()

animal_shelter = ['Dog', 'Cat', 'Rabbit'] # list
stock=['dog', 'cat'] # list

animal =st.selectbox('Select Animal', animal_shelter)

if st.button('Check Availablity'):
    have_it = animal.lower() in stock
    if have_it:
        st.success('We have it!')
    else:
        st.error('Sorry, we do not have it.')

