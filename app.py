import streamlit as st

# Título do aplicativo
st.title("Meu App de Saúde")

# Menu lateral
menu = st.sidebar.selectbox("Selecione uma opção", ["Página Inicial", "Cadastro de Pacientes", "Visualizar Pacientes"])

if menu == "Página Inicial":
    st.write("Bem-vindo ao aplicativo de organização de dados de saúde!")
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

st.sidebar.info("Versão 1.0 - Teste inicial")
