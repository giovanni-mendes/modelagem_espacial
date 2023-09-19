import streamlit as st
import webbrowser


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

btn = st.button('Acesse a Base de Dados')
if btn:
    webbrowser.open_new_tab('https://www.firjan.com.br/ifdm/')

st.write("## Autor")

st.markdown('Desenvolvido por Giovanni Mendes Lima')
btn_2 = st.button('Acesse meu GitHub')

if btn_2:
    webbrowser.open_new_tab('https://github.com/giovanni-mendes')

btn_3 = st.button('Notebook do Google Colab')
if btn_3:
    webbrowser.open_new_tab(
        'https://colab.research.google.com/drive/1ek8NBTldiTL33ycftvMLjusD5U_pYI3w?usp=sharing')

btn_4 = st.button(
    'Artigo aplicando os dados do IFDM em uma regressão linear múltipla')
if btn_4:
    webbrowser.open_new_tab(
        'https://publicacoes.unifal-mg.edu.br/revistas/index.php/cei/article/view/2159')


st.markdown('Turma Modelagem Espacial 2023-2 UNIFAL-MG Campus Varginha')

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
