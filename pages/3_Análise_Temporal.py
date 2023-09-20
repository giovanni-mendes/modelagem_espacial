import streamlit as st
import pandas as pd
import time
import plotly.express as px
from urllib.request import urlopen
import json

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

st.header('Análise Temporal')


with st.sidebar:
    indice = st.selectbox(
        'Selecione o Indicador:',
        options=['IFDM', 'Educação', 'Emprego e Renda', 'Saúde']
    )


fig_2 = px.line(df.pivot_table(indice, ['Ano'], 'Região'), markers=True)
fig_2.update_traces(textposition="bottom right")
fig_2.update_layout(title=f'Indicador {indice} para as Regiões do Brasil entre 2005 e 2016', plot_bgcolor='rgba(0,0,0,0)',
                    legend_title='Regiões')
fig_2.update_yaxes(title=f"Valor do indicador {indice}")
fig_2.update_xaxes(title="Ano")

st.plotly_chart(fig_2, use_container_width=True)

with urlopen('https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/brazil-states.geojson') as response:
    Brasil_geodata = json.load(response)

estados = []
siglas = []
for feature in Brasil_geodata['features']:
    estados.append(feature['properties']['name'])
    siglas.append(feature['properties']['sigla'])

df_estados = pd.DataFrame(estados)
df_estados['UF'] = siglas

for feature in Brasil_geodata['features']:
    feature['id'] = f"{feature['properties']['name']}"

df = pd.merge(df_estados, df, on='UF')
df.rename(columns={0: 'Estados'}, inplace=True)

df_medias = pd.DataFrame(df.groupby(['Estados', 'Ano'])[
                         ['IFDM', 'Educação', 'Saúde', 'Emprego e Renda']].mean()).reset_index()

with st.spinner('Espera um pouquinho que esse é pesado...'):
    fig_3 = px.choropleth(
        df_medias,
        locations="Estados",
        geojson=Brasil_geodata,
        color=indice,
        hover_name="Estados",
        hover_data=[indice],
        color_continuous_scale=px.colors.sequential.Oranges,
        range_color=[0, 1],
        animation_frame="Ano"
    )
    fig_3.update_geos(fitbounds="locations", visible=False)
    fig_3.update_layout(
        title=f'Indicador {indice} para os Estados do Brasil entre 2005 e 2016')
    st.plotly_chart(fig_3, use_container_width=True)
st.success('Ufa! Rodou.')

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
