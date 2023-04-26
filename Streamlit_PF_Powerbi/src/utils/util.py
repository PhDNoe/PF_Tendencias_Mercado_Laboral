import streamlit as st
import pickle


def show_logo():
    img_path = './src/imgs/1.png'
    st.image(img_path, caption="   ", use_column_width=True)



def inicio():
    st.title("Inicio")
    st.write("Este Modelo de recomendación es una herramienta para mejorar la selección del personal en los diferentes puestos de IT.")
    st.write("Se toman como parámetros las diferentes tecnologías que el Candidato/a ultiliza o utlizó en su experiencia laboral o académica.")
    st.subheader('Instrucciones')
    st.write('1_ En la opción "Área" debe introducir al menors 3 tecnologías' )
    st.write('2_ Luego de la recomendación de "Área" debe introducir los mismos parámetros en los puestos IT ("Data Science", "Data Engineer", "Data Analytics", "Full-Stack", "Front-End", "Back-End")')
    st.write('3_ Esperar recomendación de puesto')   

    img_path2 = "./src/imgs/icemd-big-data.jpg"

    st.image(img_path2, caption="   ", use_column_width=True)



def get_options():
    make_reco = False
    # st.write("Ingrese las referencias de las tecnologías utilizadas: ")
    st.write("Please enter the references of the technologies used:")
    options_dict = {'Ninguna': 0, 'Elasticsearch': 1, 'PostgreSQL': 2, 'Redis': 3, 'MySQL': 4, 'SQLite': 5, 'Microsoft SQL Server': 6, 'Oracle': 7, 'DynamoDB': 8, 'MongoDB': 9, 'Firebase': 10, 'MariaDB': 11, 'Cassandra': 12, 'Couchbase': 13, 'IBM DB2': 14}
    options_dict2 = {'Ninguna': 0, 'Flask': 1, 'Express': 2, 'jQuery': 3, 'React.js': 4, 'Django': 5, 'FastAPI': 6, 'Angular': 7, 'ASP.NET Core': 8, 'Ruby on Rails': 9, 'Vue.js': 10, 'Laravel': 11, 'Spring': 12, 'Angular.js' : 13, 'ASP.NET': 14, 'Gatsby': 15, 'Symfony': 16, 'Svelte': 17, 'Drupal': 18}
    options_dict3 = {'Ninguna': 0, 'Bash/Shell': 1, 'HTML/CSS': 2, 'Python': 3, 'SQL': 4, 'C': 5, 'C#': 6, 'C++': 7, 'Java': 8, 'JavaScript': 9, 'Node.js': 10, 'PowerShell': 11, 'Swift': 12, 'TypeScript': 13, 'Perl': 14, 'Ruby': 15, 'R': 16, 'PHP': 17, 'Kotlin': 18, 'Julia': 19, 'Haskell': 20, 'Assembly': 21, 'Rust': 22, 'Go': 23, 'VBA': 24, 'Matlab': 25, 'Scala': 26, 'Groovy': 27, 'Clojure': 28, 'Objective-C': 29, 'Dart': 30, 'F#': 31, 'LISP': 32, 'Delphi': 33, 'APL': 34, 'Erlang': 35, 'Elixir': 36, 'Crystal': 37, 'COBOL': 38}
    options_dict4 = {'Ninguna': 0, 'AWS': 1, 'Microsoft Azure': 2, 'Heroku': 3, 'Google Cloud Platform': 4, 'DigitalOcean': 5, 'Oracle Cloud Infrastructure': 6, 'IBM Cloud or Watson': 7}

    # Crea el menú desplegable
    selected_option = st.selectbox("Database", list(options_dict.keys()))
    selected_option1 = st.selectbox("Framework", list(options_dict2.keys()))
    selected_option2 = st.selectbox("Language", list(options_dict3.keys()))
    selected_option3 = st.selectbox("Plataform", list(options_dict4.keys()))

    # Obtiene el número correspondiente a la opción seleccionada
    selected_number1 = options_dict[selected_option]
    selected_number3 = options_dict2[selected_option1]
    selected_number4 = options_dict3[selected_option2]
    selected_number5 = options_dict4[selected_option3]
    selec_totalnumber = [selected_number1, selected_number3, selected_number4, selected_number5]
    if selec_totalnumber.count(0) >= 2 or selec_totalnumber.count("ninguno") >= 2:
        st.write("At least introduce 3 technologies")
    else:    
        if st.button("Recomendación"):
            make_reco = True
    return selec_totalnumber, make_reco


def area(options, make_reco):
    st.markdown("### Area Recomendation")
    
    model = ''
    MODEL_PATH='./models/pkl_areasgenerales01.pickle'

    
    if model=='':
        with open(MODEL_PATH, 'rb') as file:
            model = pickle.load(file)
    # options = get_options()
    # selec_totalnumber = [selected_number1, selected_number3, selected_number4, selected_number5]
    if make_reco:
        selec_totalnumber = [*options]

        # if selec_totalnumber.count(0) >= 2 or selec_totalnumber.count("ninguno") >= 2:
        #     st.write("Introduzca al menos 3 tecnologias")
        # else:    
        #     if st.button("Recomendación"):
        prediction = model.predict([selec_totalnumber])[0]
        st.write(f"Puesto: {prediction}")      
        print(prediction)


def data_science(options, make_reco):
    st.markdown("### Data Science Recomendation")
    MODEL_PATH2 = "./models/pkl_areadatascience1.pickle"
    model=''

    # Se carga el modelo
    if model=='':
        with open(MODEL_PATH2, 'rb') as file:
            model = pickle.load(file)

    if make_reco:
        selec_totalnumber = [*options]    
        prediction = model.predict([selec_totalnumber])[0]
        st.write(f"Puesto: {prediction}")


def data_engineer(options, make_reco):
    st.markdown("### Data Engineer Recomendation")
    MODEL_PATH3 = "./models/pkl_areadataingeniero4.pickle"
    model=''

    # Se carga el modelo
    if model=='':
        with open(MODEL_PATH3, 'rb') as file:
            model = pickle.load(file)

    if make_reco:
        selec_totalnumber = [*options]
        prediction = model.predict([selec_totalnumber])[0]
        st.write(f"Puesto: {prediction}") 


# Pestaña de Data Analitic
def data_analytics(options, make_reco):
    st.markdown(" ### Data Analytics  Recomendation")
    MODEL_PATH4 = "./models/pkl_areadataanalitics1.pickle"
    model=''

    # Se carga el modelo
    if model=='':
        with open(MODEL_PATH4, 'rb') as file:
            model = pickle.load(file)

    if make_reco:
        selec_totalnumber = [*options]

        prediction = model.predict([selec_totalnumber])[0]
        st.write(f"Puesto: {prediction}")



def full_stack(options, make_reco):
    st.markdown("### Full-Stack  Recomendation")     
    MODEL_PATH5 = "./models/pkl_areadevefull1.pickle"
    model=''

    # Se carga el modelo
    if model=='':
        with open(MODEL_PATH5, 'rb') as file:
            model = pickle.load(file)

    
    if make_reco:
        selec_totalnumber = [*options]
        prediction = model.predict([selec_totalnumber])[0]
        st.write(f"Puesto: {prediction}")



    # # Pestaña de Frent-end
def front_end(options, make_reco):
    st.markdown("### Front-End  Recomendation")    
    MODEL_PATH6 = "./models/pkl_areadevefront1.pickle"
    model=''

    # Se carga el modelo
    if model=='':
        with open(MODEL_PATH6, 'rb') as file:
            model = pickle.load(file)

    
    if make_reco:
        selec_totalnumber = [*options]
    
        prediction = model.predict([selec_totalnumber])[0]
        st.write(f"Puesto: {prediction}")



# Pestaña de developer - backend
def back_End(options, make_reco):
    st.markdown("### Back-End  Recomendation") 
    MODEL_PATH7 = "./models/pkl_areadeveback1.pickle"
    model=''

    # Se carga el modelo
    if model=='':
        with open(MODEL_PATH7, 'rb') as file:
            model = pickle.load(file)

    if make_reco:
        selec_totalnumber = [*options]

        prediction = model.predict([selec_totalnumber])[0]
        st.write(f"Puesto: {prediction}")