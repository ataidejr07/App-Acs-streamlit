import streamlit as st

st.set_page_config(page_title="Meu App", page_icon="🏥", layout="centered")

# Estilo com CSS para abas azuis
top_bar = """
    <style>
    .top-bar {
        background-color: #007BFF;
        padding: 10px;
        text-align: center;
        color: white;
        font-size: 24px;
        font-weight: bold;
        border-radius: 10px 10px 0 0;
    }
    .bottom-bar {
        background-color: #007BFF;
        padding: 15px;
        position: fixed;
        bottom: 0;
        width: 100%;
        text-align: center;
        color: white;
        font-size: 16px;
        border-radius: 0 0 10px 10px;
    }
    </style>
"""

st.markdown(top_bar, unsafe_allow_html=True)
st.markdown("<div class='top-bar'>Meu App de Saúde</div>", unsafe_allow_html=True)

# Navegação entre páginas
menu = st.sidebar.radio("Navegação", ["Página Inicial", "Cadastro de Pacientes", "Visualizar Pacientes", "Agrupar por Endereço", "Registrar Visitas"])

if menu == "Página Inicial":
    st.subheader("Bem-vindo! Escolha uma opção no menu lateral.")

elif menu == "Cadastro de Pacientes":
    st.subheader("Cadastro de Pacientes")
    nome = st.text_input("Nome do Paciente")
    idade = st.number_input("Idade", min_value=0, max_value=120, step=1)
    endereco = st.text_area("Endereço")
    comorbidades = st.text_area("Comorbidades")
    if st.button("Salvar"):
        st.success(f"Paciente {nome} cadastrado com sucesso!")

elif menu == "Visualizar Pacientes":
    st.subheader("Lista de Pacientes (Em breve)")

elif menu == "Agrupar por Endereço":
    st.subheader("Agrupar por Endereço (Em breve)")

elif menu == "Registrar Visitas":
    st.subheader("Registrar Visitas (Em breve)")

st.markdown("<div class='bottom-bar'>Rodapé - Futuras Funcionalidades</div>", unsafe_allow_html=True)

    
