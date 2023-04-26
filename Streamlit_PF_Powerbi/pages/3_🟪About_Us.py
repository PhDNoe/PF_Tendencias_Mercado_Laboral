import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
        page_title="About",
        page_icon="🟪",
        layout="wide",
    )



speech = """
We are a consulting firm specialized in Big Data and information technology. 
We provide services to other companies that require extracting important information 
from unstructured data or from various sources of information to maximize their businesses.
"""

speech2 = """
Our mission in this project is to develop technological tools that enable our client
(IT recruitment companies) to achieve their objectives. 
The requesting company aims to be a pioneer in gender inclusion, specifically in terms 
of the inclusion of women and the democratization of highly demanded IT positions today.
"""
st.markdown("## About us")


col1, col2 = st.columns([3,2])
with col1:
    st.markdown(speech)
    st.markdown('---')
    st.markdown('### Our Mision')
    st.markdown(speech2)

with col2: 
    st.markdown('### Our team')
    st.markdown('---')
    cola, colb = st.columns([1,1])
    with colb:
        st.image('./src/imgs/1_Noelia.png')
    with cola:
        a = """
            :blue[CDO - Data Scientist]
        """
        st.markdown("**Noelia Echeverría**")
        st.write(a)
    
    st.markdown('---')
    colc, cold = st.columns([1,1])
    with cold:
        st.image('./src/imgs/2_Andres.png')
    with colc:
        b = """
            :blue[Data Engineer]
        """
        st.markdown("**Andrés Alejando Baez**")
        st.write(b)

    st.markdown('---')
    cole, colf = st.columns([1,1])
    with colf:
        st.image('./src/imgs/3_Marcelo.png')
    with cole: 
        st.markdown("**Jorge Marcelo Mendez**")
        st.write(b)

    st.markdown('---')
    colg, colh = st.columns([1,1])
    with colh:
        st.image('./src/imgs/4_Milton.png')
    with colg:
        c = """
            :blue[Data Analyst]
        """
        st.markdown("**Milton Gastón Aquino**")
        st.write(c)

    
    st.markdown('---')
    coli, colj = st.columns([1,1])
    with colj:
        st.image('./src/imgs/5_Camilo.png')
    with coli:
        d = """
            :blue[Data Analyst - Project Manager]
        """
        st.markdown("**Camilo Santamaría Murillo**")
        st.write(d)

    st.markdown('---')
    colk, coll = st.columns([1,1])
    with coll:
        st.image('./src/imgs/6_Maico.png')
    with colk:
        e = """
            :blue[Scrum Master]
        """
        st.markdown("**Maico Bernal**")
        st.write(e)
    