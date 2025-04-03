import streamlit as st
import streamlit.components.v1 as components

def main():
    st.markdown(
        """
        <style>
            /* Ajustando espaçamentos para melhor visualização em telas menores */
            .main .block-container {
                padding: 0.5rem 0.5rem;
            }
            h1, h2 {
                margin-bottom: 0.3rem;
            }
            .stButton>button {
                width: 100%;
                padding: 0.4rem 0.8rem;
                font-size: 0.9rem;
            }
            .stMarkdown {
                margin-bottom: 0.5rem;
            }
            .footer {
                position: fixed;
                bottom: 0;
                left: 0;
                width: 100%;
                background: #007bff;
                color: white;
                text-align: center;
                padding: 0.5rem;
                font-size: 0.8rem;
            }
            .header {
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                background: #007bff;
                color: white;
                text-align: center;
                padding: 0.5rem;
                font-size: 1.2rem;
                font-weight: bold;
                z-index: 1000;
            }
            .container {
                padding-top: 2.5rem; /* Para compensar o header fixo */
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div class="header">ACS Micro Área</div>', unsafe_allow_html=True)

    st.markdown("## Bem-vindo, Ataide!")
    st.markdown("### Cadastros")
    
    st.button("🏠 Domicílios")
    st.button("👨‍👩‍👧‍👦 Famílias")
    st.button("🧑 Cidadãos")
    
    st.markdown("### Análises e Relatórios")
    
    st.button("📊 Relatórios")
    st.button("📈 Resumo de Produção")
    st.button("👶⚰️ Nascimentos e Óbitos")
    
    st.markdown("<div class='footer'>Desenvolvido para ACS</div>", unsafe_allow_html=True)
    
if __name__ == "__main__":
    main()
