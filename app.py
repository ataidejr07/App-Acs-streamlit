import streamlit as st
from streamlit_option_menu import option_menu

# Personalização das abas (em cima e no rodapé)
st.set_page_config(page_title="Meu App", page_icon="🏠")

# Abas no topo (usando a biblioteca option_menu)
with st.container():
    selected = option_menu(
        menu_title=None,  # Título do menu
        options=["Início", "Cadastro", "Relatórios", "Configurações"],  # Opções de menu
        icons=["house", "person", "file-earmark", "gear"],  # Ícones dos botões
        menu_icon="cast",  # Ícone do menu
        default_index=0,  # Aba padrão selecionada
        orientation="horizontal",  # Horizontal para o topo
        styles={
            "container": {"padding": "5px", "background-color": "#007bff"},  # Cor de fundo das abas (azul)
            "icon": {"color": "white", "font-size": "20px"},  # Cor dos ícones
            "nav-link": {"font-size": "16px", "font-weight": "bold", "color": "white"},  # Estilo do texto do menu
            "nav-link-selected": {"background-color": "#0056b3", "color": "white"}  # Cor da aba selecionada
        }
    )

# Exemplo de conteúdo para cada aba
if selected == "Início":
    st.write("Bem-vindo à página inicial!")
elif selected == "Cadastro":
    st.write("Aqui você pode adicionar novos cadastros de pacientes.")
elif selected == "Relatórios":
    st.write("Visualize os relatórios aqui.")
elif selected == "Configurações":
    st.write("Ajuste as configurações do aplicativo aqui.")

# Abas no rodapé
with st.container():
    footer_selected = option_menu(
        menu_title=None,  # Título do menu
        options=["Ajuda", "Sobre", "Contato"],  # Opções de menu
        icons=["info-circle", "info", "envelope"],  # Ícones dos botões
        menu_icon="cast",  # Ícone do menu
        default_index=0,  # Aba padrão selecionada
        orientation="horizontal",  # Horizontal para o rodapé
        styles={
            "container": {"padding": "5px", "background-color": "#007bff"},  # Cor de fundo das abas (azul)
            "icon": {"color": "white", "font-size": "20px"},  # Cor dos ícones
            "nav-link": {"font-size": "16px", "font-weight": "bold", "color": "white"},  # Estilo do texto do menu
            "nav-link-selected": {"background-color": "#0056b3", "color": "white"}  # Cor da aba selecionada
        }
    )

# Exemplo de conteúdo para cada aba de rodapé
if footer_selected == "Ajuda":
    st.write("Página de ajuda!")
elif footer_selected == "Sobre":
    st.write("Informações sobre o aplicativo.")
elif footer_selected == "Contato":
    st.write("Informações de contato.")
