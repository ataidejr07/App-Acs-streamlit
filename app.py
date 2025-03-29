import streamlit as st

# Configuração da página

st.set_page_config(page_title="ACS Micro Área", page_icon="🏠", layout="wide")

# Estilização com CSS

st.markdown( """ <style> .header { position: fixed; top: 0; left: 0; width: 100%; background-color: #007BFF; color: white; text-align: center; padding: 15px; font-size: 24px; font-weight: bold; z-index: 1000; } .footer { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #007BFF; color: white; text-align: center; padding: 10px; font-size: 14px; z-index: 1000; } .container { margin-top: 80px; margin-bottom: 50px; padding: 20px; } .card { display: flex; align-items: center; justify-content: center; height: 80px; background-color: #f8f9fa; border-radius: 10px; border: 1px solid #ddd; text-align: center; cursor: pointer; font-size: 18px; font-weight: bold; margin-bottom: 10px; transition: 0.3s; } .card:hover { background-color: #e9ecef; transform: scale(1.05); } </style> """, unsafe_allow_html=True, )

# Cabeçalho Fixo

st.markdown('<div class="header">ACS Micro Área</div>', unsafe_allow_html=True)

# Conteúdo principal

st.markdown('<div class="container">', unsafe_allow_html=True)

st.subheader("Cadastros") col1, col2, col3 = st.columns(3)

with col1: if st.button("🏠 Domicílios"): st.info("Gerencie os endereços cadastrados e veja quem mora em cada residência.")

with col2: if st.button("👨‍👩‍👧 Famílias"): st.info("Acompanhe os núcleos familiares e suas informações essenciais.")

with col3: if st.button("🧑 Cidadãos"): st.info("Visualize os dados individuais dos cidadãos atendidos.")

st.subheader("Análises e Relatórios") col1, col2, col3 = st.columns(3)

with col1: if st.button("📊 Relatórios"): st.info("Gere relatórios detalhados para análises e planejamento.")

with col2: if st.button("📈 Resumo de Produção"): st.info("Acompanhe os indicadores de produtividade e desempenho.")

with col3: if st.button("👶⚰️ Nascimentos e Óbitos"): st.info("Registre e consulte informações sobre nascimentos e óbitos na comunidade.")

st.markdown('</div>', unsafe_allow_html=True)

# Rodapé Fixo

st.markdown('<div class="footer">Desenvolvido para ACS | 2025</div>', unsafe_allow_html=True)

