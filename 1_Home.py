import streamlit as st


st.set_page_config(
    page_title="Modelagem Espacial",
    page_icon="🗺️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"]::before {
                content: "Páginas";
                margin-left: 20px;
                margin-top: 20px;
                font-size: 30px;
                position: relative;
                top: 100px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

st.write("# Análise do Geoespacial do IFDM")

st.write("## Objetivo")
st.markdown("""O objetivo deste trabalho é realizar uma análise temporal do IFDM e seus componentes, como também,
            calcular o I de Moran para os municípios brasileiros utilizando os dados do IFDM do ano de 2016.
            """)


st.write("## O IFDM")

st.image('imagens/IFDM.png')

st.markdown(
    """
    O IFDM – Índice FIRJAN de Desenvolvimento Municipal – é um estudo do Sistema FIRJAN que acompanha anualmente o desenvolvimento socioeconômico de todos os mais de 5 mil municípios brasileiros em três áreas de atuação: 
    Emprego & renda, Educação e Saúde. Criado em 2008, ele é feito, exclusivamente, com base em estatísticas públicas oficiais, disponibilizadas pelos ministérios do Trabalho, Educação e Saúde.

"""
)

st.video('https://www.youtube.com/watch?v=IxisjjHDn7A&embeds_referring_euri=https%3A%2F%2Fwww.firjan.com.br%2F&source_ve_path=MjM4NTE&feature=emb_title&ab_channel=Firjan',  start_time=0)

st.markdown(
    f'<a href="{"https://www.firjan.com.br/ifdm/"}" style="display: inline-block; padding: 12px 20px; background-color: #4CAF50; color: white; text-align: center; text-decoration: none; font-size: 16px; border-radius: 4px;">Acesse a Base de Dados</a>',
    unsafe_allow_html=True
)


st.write("## Autor")

st.markdown('Desenvolvido por Giovanni Mendes Lima')
st.markdown(
    f'<a href="{"https://github.com/giovanni-mendes"}" style="display: inline-block; padding: 12px 20px; background-color: #4CAF50; color: white; text-align: center; text-decoration: none; font-size: 16px; border-radius: 4px;">Acesse meu GitHub</a>',
    unsafe_allow_html=True
)

st.markdown(
    f'<a href="{"https://colab.research.google.com/drive/1ek8NBTldiTL33ycftvMLjusD5U_pYI3w?usp=sharing"}" style="display: inline-block; padding: 12px 20px; background-color: #4CAF50; color: white; text-align: center; text-decoration: none; font-size: 16px; border-radius: 4px;">Notebook do Google Colab</a>',
    unsafe_allow_html=True
)

st.markdown(
    f'<a href="{"https://publicacoes.unifal-mg.edu.br/revistas/index.php/cei/article/view/2159"}" style="display: inline-block; padding: 12px 20px; background-color: #4CAF50; color: white; text-align: center; text-decoration: none; font-size: 16px; border-radius: 4px;">Artigo aplicando os dados do IFDM em uma regressão linear múltipla</a>',
    unsafe_allow_html=True

)

st.markdown('Turma Modelagem Espacial 2023-2 UNIFAL-MG Campus Varginha')

y = st.slider('Teste', min_value = 2005, max_value=2016, step=1)

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)


