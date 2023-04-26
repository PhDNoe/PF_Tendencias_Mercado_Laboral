import streamlit as st
import streamlit.components.v1 as components
import webbrowser


st.set_page_config(
        page_title="PowerBi",
        page_icon="🟩",
        layout="wide",
    )

coln, colm  = st.columns([4,1])
with coln:
    st.header("📈 Tableros de Power BI")
with colm:
        st.image('./src/imgs/1.png', width=150)
st.markdown('---')

powerbi_url = 'https://app.powerbi.com/view?r=eyJrIjoiYjYyODI3NzYtZGVhZi00MjM2LWFmMzItNDNhZmFlYzZmZGU5IiwidCI6IjJkOTgzYTE2LTM1ZGItNDgwOC04ZDQyLTE0MzY3ZTFiNWQ2ZiIsImMiOjR9 '

def toPowerBi():
    webbrowser.open_new_tab(powerbi_url)
    


container1 = st.container()

with container1:
    cola, colb, colc = st.columns([2,4,2])


# powerbi_url = 'https://app.powerbi.com/view?r=eyJrIjoiNmRiYjM2NmQtNGNkYy00MWQzLWE0MTktZmU2OTBhNzE1ZDczIiwidCI6IjJkOTgzYTE2LTM1ZGItNDgwOC04ZDQyLTE0MzY3ZTFiNWQ2ZiIsImMiOjR9'
with colb:
    # embed streamlit docs in a streamlit app
    components.iframe(powerbi_url, width=768, height=603, scrolling=True)
    # components.html('''<iframe title="PFJobTrends_V2" width="600" height="636" 
    # src="https://app.powerbi.com/view?r=eyJrIjoiYjYyODI3NzYtZGVhZi00MjM2LWFmMzItNDNhZmFlYzZmZGU5IiwidCI6IjJkOTgzYTE2LTM1ZGItNDgwOC04ZDQyLTE0MzY3ZTFiNWQ2ZiIsImMiOjR9" 
    # frameborder="0" allowFullScreen="true"></iframe>''', height=603, width=768)
with cola:
    st.button(label='See in PowerBI', on_click=toPowerBi)


