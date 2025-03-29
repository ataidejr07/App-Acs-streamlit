import streamlit as st
from streamlit_option_menu import option_menu

def main():
    st.set_page_config(page_title='ACS Micro Área', layout='wide')
    
    # Barra de cabeçalho azul fixa
    st.markdown(
        '<div style="background-color: #007bff; padding: 10px; text-align: center; font-size: 24px; color: white; font-weight: bold;">ACS Micro Área</div>',
        unsafe_allow_html=True
    )
    
    # Criando a barra lateral com menu
    with st.sidebar:
        selected = option_menu("Menu", ["Página Inicial", "Domicílios", "Famílias", "Cidadãos", "Relatórios", "Resumo de Produção", "Nascimentos e Óbitos"],
                               icons=['house', 'people', 'person', 'bar-chart', 'clipboard-data', 'activity', 'heart'],
                               menu_icon="cast", default_index=0)
    
    # Ajustando o espaçamento da mensagem de boas-vindas
    st.markdown("<h3 style='text-align: center;'>Bem-vindo, Ataide!</h3>", unsafe_allow_html=True)
    
    # Seções principais
    st.write("### Cadastros")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.button("🏠 Domicílios")
    with col2:
        st.button("👨‍👩‍👧‍👦 Famílias")
    with col3:
        st.button("🧑 Cidadãos")
    
    st.write("### Análises e Relatórios")
    col4, col5, col6 = st.columns(3)
    with col4:
        st.button("📊 Relatórios")
    with col5:
        st.button("📈 Resumo de Produção")
    with col6:
        st.button("❤️ Nascimentos e Óbitos")
    
    # Rodapé azul fixo
    st.markdown(
        '<div style="background-color: #007bff; padding: 10px; position: fixed; bottom: 0; width: 100%; text-align: center; color: white;">Desenvolvido para ACS</div>',
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
