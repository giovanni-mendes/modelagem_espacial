import streamlit as st
import pandas as pd

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

st.write('# I de Moran para o Brasil')

st.markdown(
    'Para realizar a análise foi utilizado o IFDM dos municípios do ano de 2016')

st.write('## IFDM para os municípios')
st.markdown('Intervalos desiguais')
st.image('imagens/ifdm_mun.png')

st.markdown('Intervalos homogêneos')
st.image('imagens/ifdm_mun_h.png')

st.write('## Estatística I de Moran para o Brasil')
st.markdown('Valor Encontrado: ')
i = pd.Series([0.47], name='I de Moran', index=['Estatística'])
st.write(i)

st.markdown('P-valor:')
p = pd.Series([0.001], name='P-valor', index=['Estatística'])
st.write(p)

with st.expander("Veja a Interpretação"):
    st.write("""
        A estatística de I de Moran foi positiva, indicando clusters espaciais.
             
        Além disso, como o p-valor é inferior a 0.05, constata-se que é uma estatística significativa.
    """)

st.markdown('Diagrama de Dispersão de Moran')
st.image('imagens/moran_d.png')

st.image('imagens/moran_d_2.png')


st.write('## Mapa Lisa Cluster')
st.image('imagens/lisa_cluster.png')
with st.expander("Veja a Explicação"):
    st.write("""
        O mapa Lisa Cluster identifica os clusters e os outliers espaciais:
             
        - Cluesters espaciais (+): High-High (HH), Low-Low (LL)
        
        - Outliers espaciais  (-): High-Low (HL), Low-High (LH)
             
        - Não significativo (ns)
    """)

hide_st_style = """
            <style>
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

