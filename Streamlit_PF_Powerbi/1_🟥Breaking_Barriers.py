import streamlit as st
import streamlit.components.v1 as components


st.set_page_config(
        page_title="Breaking Barriers",
        page_icon="🟥",
        layout="wide",
    )
col1,col2 = st.columns([3,1])
with col1:
    st.header("Breaking Barriers")
    st.markdown("### :blue[Enhancing Gender Inclusion in IT Recruitment across LATAM]")

with col2:
    st.image('./src/imgs/1.png', width=100)

st.markdown('---')

col3,col4 = st.columns([3,1])
problem = """
>Currently, the world of Information Technology (IT) has become one of the most in-demand
and continuously growing job fields worldwide. 
However, women seeking a career in this field face a different reality compared to men. 
One of the most notable differences is the gender pay gap.  Is this difference real? 
Is it due to gender discrimination or are there other reasons?"
"""

with col3:
    st.markdown(problem)
with col4:
    st.image('./src/imgs/personas_pensando_problematica.png')

st.markdown('---')
st.markdown("### Our Product")
product = """
At Pentabyte Solutions, we have developed a comprehensive product to help our 
client meet the goals of their gender inclusion program  in the IT industry for 
Latin America.

**What's included in this package?**

* :red[Power BI dashboards] to understand the reasons behind the gender pay gap 
and job offers towards women, taking into account the demographic distribution 
of developers, level of education achieved, average salaries in the region, etc.

* The dashboards include 2 specific, measurable, achievable, and relevant KPIs:
    * :red[Gender Inclusion KPI]: Increase the number of women in IT employment by at 
    least 3% annually.
    * :red[Educational Achievement KPI]: Retain 5% of online training through boot camps, 
    including free courses and certification. This way, we can increase the academic level of successful profiles (with a focus on females) in IT employment.
* :red[Machine learning models for efficient candidate screening].
    The goal of these models is to speed up the hiring process by evaluating a candidate's proficiency in relevant technologies.
"""
st.markdown(product)

