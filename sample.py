import streamlit as st
st.title('wow')
st.text('amazing')
st.subheader('great')
st.markdown('##### wow')
st.success('wow')
st.error('Error')
st.warning('Go back')


# Checkbox
if st.checkbox("Show/Hide"):
    st.text("Showing or Hiding Widget")

# Radio Button
status = st.radio("What is your status",('Active','Inactive'))
if status == 'Active':
    st.text("Status is Active")
else:
    st.warning("Not Active Yet")


# SelectBox
occupation = st.selectbox("Your Occupation",['Data Scientist','Programmer','Doctor','Businessman'])
st.write("You selected this option",occupation)

# MultiSelect
location = st.multiselect("Where do you stay",("London","New York","Accra","Kiev","Berlin","New Delhi"))
st.write("You selected",len(location),"location")

# Text Area
c_text = st.text_area("Enter Text","Type Here...")
if st.button('Analyze'):
    c_result = c_text.title()
    st.success(c_result)


st.sidebar.header("Side Bar Header")
st.sidebar.text("Hello")

st.balloons()

