import streamlit as st
import pandas as pd
import io

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

@st.cache_data
def gerar_df():
    df = pd.read_excel('datasets/IFDM_visualizacao.xlsx')
    return df


df = gerar_df()

df['Código'] = df['Código'].astype(str)
df['Ano'] = df['Ano'].astype(str)
df.replace('*', 0, inplace=True)
df.iloc[:, 5:-1].astype(float)

st.header('Análise Descritiva dos Dados')

st.markdown('df.head()')
st.write(df.head())

st.markdown('df.info()')
buffer = io.StringIO()
df.info(buf=buffer)
info = buffer.getvalue()
st.text(info)

st.markdown('df.isnull().sum()')
vazio = df.isnull().sum()
vazio.name = 'Quantidade de Nulos'
st.write(vazio)

st.markdown('df.describe()')
st.write(df.loc[(df.iloc[:, 5:] > 0).all(axis=1)].describe())

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
