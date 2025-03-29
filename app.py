import streamlit as st

# Configuração da página
st.set_page_config(page_title="Meu App", page_icon="🏠", layout="wide")
st.title("Meu App")  
st.write("Bem-vindo, Ataide!")

# Sidebar para opções secundárias
with st.sidebar:
    st.header("Outras Opções")
    
    if st.button("📋 Cartões Espelho"):
        st.info("Visualize informações resumidas e detalhadas sobre atendimentos.")

    if st.button("📝 Laudos e Receitas"):
        st.info("Acesse documentos médicos e prescrições.")

# Organização dos botões principais em seções
st.subheader("Cadastros")

# Divisão em colunas
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🏠 Domicílios"):
        st.info("Gerencie os endereços cadastrados e veja quem mora em cada residência.")

with col2:
    if st.button("👨‍👩‍👧 Famílias"):
        st.info("Acompanhe os núcleos familiares e suas informações essenciais.")

with col3:
    if st.button("🧑 Cidadãos"):
        st.info("Visualize os dados individuais dos cidadãos atendidos.")

st.subheader("Análises e Relatórios")

# Divisão em colunas
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("📊 Relatórios"):
        st.info("Gere relatórios detalhados para análises e planejamento.")

with col2:
    if st.button("📈 Resumo de Produção"):
        st.info("Acompanhe os indicadores de produtividade e desempenho.")

with col3:
    if st.button("👶⚰️ Nascimentos e Óbitos"):
        st.info("Registre e consulte informações sobre nascimentos e óbitos na comunidade.")
