import streamlit as st

st.set_page_config(page_title="Meu App", page_icon="🏥", layout="centered")

# Personalizando o estilo
st.markdown(
    """
    <style>
    body {
        background-color: white;
        color: black;
        font-family: Arial, sans-serif;
    }
    .stButton>button {
        width: 100%;
        height: 80px;
        font-size: 18px;
        border-radius: 10px;
        background-color: #007BFF;
        color: white;
        border: none;
    }
    .stButton>button:hover {
        background-color: #0056b3;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("📋 Meu App de Saúde")

st.write("### Bem-vindo! Escolha uma opção:")

# Criando um layout de grade com os botões
col1, col2 = st.columns(2)

with col1:
    if st.button("📝 Cadastro de Pacientes"):
        st.session_state["page"] = "cadastro"

    if st.button("📊 Visualizar Pacientes"):
        st.session_state["page"] = "visualizar"

with col2:
    if st.button("🏠 Agrupar por Endereço"):
        st.session_state["page"] = "endereco"

    if st.button("📅 Registrar Visitas"):
        st.session_state["page"] = "visitas"

# Controle de navegação entre as páginas
if "page" in st.session_state:
    if st.session_state["page"] == "cadastro":
        st.subheader("Cadastro de Pacientes")
        nome = st.text_input("Nome do Paciente")
        idade = st.number_input("Idade", min_value=0, max_value=120, step=1)
        endereco = st.text_area("Endereço")
        comorbidades = st.text_area("Comorbidades")
        if st.button("Salvar"):
            st.success(f"Paciente {nome} cadastrado com sucesso!")

    elif st.session_state["page"] == "visualizar":
        st.subheader("Lista de Pacientes (Em breve)")

    elif st.session_state["page"] == "endereco":
        st.subheader("Agrupar por Endereço (Em breve)")

    elif st.session_state["page"] == "visitas":
        st.subheader("Registrar Visitas (Em breve)")
