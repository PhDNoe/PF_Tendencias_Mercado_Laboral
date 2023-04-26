import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
        page_title="ML",
        page_icon="🟨",
        layout="wide",
    )

from src.utils.util import inicio, show_logo, area, data_science, data_engineer, data_analytics
from src.utils.util import front_end, full_stack, back_End, get_options


header_ML = st.container()
body_ML = st.container()

with header_ML:
    col1, col2 = st.columns([4,1])
    with col1:
        st.markdown('# Candidate Classification System')
    with col2:
        show_logo()
    show_instructions = st.expander(label='See Instructions')
    with show_instructions:
        inicio()

with body_ML:
    st.markdown('---')

    col3,col4 = st.columns([1,2])

    with col3:
        options,make_reco = get_options()
    with col4:
        tab_area, tab_data, tab_developer = st.tabs(['Area', 'Data', 'Developer'])
        with tab_area:
            area(options, make_reco)
        with tab_data:
            data_science(options, make_reco)
            st.markdown('---')
            data_engineer(options, make_reco)
            st.markdown('---')
            data_analytics(options, make_reco)

        with tab_developer:
            full_stack(options, make_reco)
            st.markdown('---')
            front_end(options, make_reco)
            st.markdown('---')
            back_End(options, make_reco)