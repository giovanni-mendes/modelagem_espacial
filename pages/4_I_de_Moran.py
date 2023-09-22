import streamlit as st
import pandas as pd
import plotly.express as px




st.set_page_config(
    page_title="Modelagem Espacial",
    page_icon="🗺️",
    layout="wide",
    initial_sidebar_state="expanded"
)

@st.cache_data
def gerar_df():
    df = pd.read_excel('datasets/IFDM_visualizacao.xlsx')
    return df

coluna = 'IFDM'

lista_condicoes =  [df[coluna] < 0.4,
                    df[coluna] < 0.6,
                    df[coluna] < 0.8,
                    df[coluna] <= 1]

lista_escolha =      ['Baixo',
                     'Regular',
                     'Moderado',
                     'Alto']

df['desenvolvimento'] = np.select(lista_condicoes, lista_escolha)

fig = px.pie(df, 'desenvolvimento')
fig.update_layout(title='Proporção de Desenvolvimento do Brasil')
st.plotly_chart(fig, use_container_width=True)

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
st.markdown('Intervalos de IFDM baseado nos Quantis')
st.image('imagens/ifdm_mun.png')

st.markdown('Intervalos homogêneos de IFDM')
st.image('imagens/ifdm_mun_h.png')


with st.expander("Veja a Interpretação"):
    st.write("""
        É possível observar que os municípios mais desenvolvidos se concentram nas regiões Centro-oeste, Sudeste e Sul.
    """)

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

        É possível observar que há vários clusters espaciais HH no Sul, Sudeste e Centro-oeste.

        Também há cluster espaciais do tipo LL no Norte do país.

        Por fim, há outliers espaciais do tipo HL no Norte do país. 
    """)

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
