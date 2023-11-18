import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np




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

st.write('# I de Moran para o Brasil')

st.markdown(
    'Para realizar a análise foi utilizado o IFDM dos municípios do ano de 2016')

st.image('imagens/interpreta_ifdm.png')

@st.cache_data
def gerar_df():
    df = pd.read_excel('datasets/IFDM_visualizacao.xlsx')
    return df

df = gerar_df()
df['Código'] = df['Código'].astype(str)
df['Ano'] = df['Ano'].astype(str)
df.replace('*', 0, inplace=True)
df.iloc[:, 5:-1].astype(float)

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


st.markdown(
    'Describe IFDM 2016 para o Brasil')
anos = list(df['Ano'].unique())
st.write(df['IFDM'].loc[(df['Ano'] == anos[-1]) & (df['IFDM'] > 0)].describe())

with st.expander("Veja a Interpretação"):
    st.write("""
        - Observações para cerca de 5.441 municípios (IFDM positivo);
        - A média do índice IFDM para o ano de 2016 foi de 0.6678, ou seja, em média, o desenvolvimento brasileiro é moderado;
        - O valor mínimo de desenvolvimento foi de 0.3214 do município de Ipixuna no Amazonas;
        - O valor máximo de desenvolvimento foi de 0.9006 do município de Louveira em São Paulo.
    """)

st.write('## Melhores municípios do Brasil')
st.write(df.loc[df['Ano'] == anos[-1]].sort_values(by='IFDM' ,ascending=False).head(5))

st.write('## Piores municípios do Brasil')
st.write(df.loc[(df['IFDM'] > 0) & (df['Ano'] == anos[-1])].sort_values(by='IFDM', ascending=True).head(5))

st.write('## Distribuição do IFDM em 2016')

df = df.loc[df['Ano'] ==  anos[-1]]
fig = px.histogram(df.loc[df['IFDM'] > 0], 
                   x="IFDM",
                   marginal="box",
                   color_discrete_sequence=['#0f9dd1'],
                   histnorm='probability density'
                   )

fig.update_yaxes(title='Densidade de Probabilidade', row=1, col=1)
fig.update_xaxes(title='IFDM', row=1, col=1)
st.plotly_chart(fig, use_container_width=True)


st.write('## Proporção de Desenvolvimento Municipal em 2016')

fig =  px.pie(df.loc[df['Ano'] == anos[-1]], 
       names='desenvolvimento',
       hole = 0.5,
       color='desenvolvimento',
        width=600,
        height=600,
       color_discrete_map={'Alto': 'green', 
                           'Moderado':'#04033d', 
                           'Regular': '#700270',
                           'Baixo':'red'})

fig.update_layout(annotations=[dict(text='Desenvolvimento', x=0.5, y=0.5, font_size=20, showarrow=False)])
st.plotly_chart(fig, use_container_width=True)


st.write('## IFDM para os municípios')
st.markdown('Intervalos de IFDM baseado nos Quantis')
st.image('imagens/ifdm_mun.png')


with st.expander("Veja a Interpretação"):
    st.write("""
        - Mínimo: 0
        - 1° Quartil: 0.6
        - 2° Quartil: 0.67
        - 3° Quartil: 0.74
        - Máximo: 0.9

        Cerca de 50% dos municípios brasileiros têm desenvolvimento abaixo de 0.67, isto é, pelo indicador IFDM, grande parte dos municípios pode ser classificado como regular/moderado.
    """)

st.markdown('Intervalos homogêneos de IFDM')
st.image('imagens/ifdm_mun_h.png')

st.markdown('Mapa Fisher Jenks')
st.image('imagens/ifdm_fisher_jenks_mun.png')


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

        Por fim, há outliers espaciais do tipo HL no Norte/Nordeste do país. 
    """)


st.write('# I de Moran para Minas Gerais')

def gerar_br():
    br = pd.read_csv('datasets/br.csv', encoding='latin-1', sep=',')
    return br
br = gerar_br()

mg = df.loc[df['UF'] == 'MG']
st.markdown(
    'Describe IFDM 2016 para Minas Gerais')

st.write(mg['IFDM'].loc[(mg['Ano'] == anos[-1]) & (mg['IFDM'] > 0)].describe())

with st.expander("Veja a Interpretação"):
    st.write("""
        - Observações para cerca de 839 municípios (IFDM positivo);
        - A média do índice IFDM para o ano de 2016 foi de 0.6679, ou seja, em média, o desenvolvimento mineiro é moderado;
        - O valor mínimo de desenvolvimento foi de 0.4568 do município Bertópolis;
        - O valor máximo de desenvolvimento foi de 0.8586 do município Patos de Minas.
        """)

st.write('## Melhores municípios de Minas Gerais em 2016')
st.write(mg.loc[(mg['Ano'] == anos[-1]) & (mg['IFDM'] > 0)].sort_values(by='IFDM', ascending=False).head())

st.write('## Piores municípios de Minas Gerais em 2016')
st.write(mg.loc[(mg['Ano'] == anos[-1]) & (mg['IFDM'] > 0)].sort_values(by='IFDM', ascending=True).head())

st.write('## Distribuição do IFDM em Minas Gerais para o ano de2016')
mg = mg.loc[mg['Ano'] ==  anos[-1]]
fig = px.histogram(mg.loc[mg['IFDM'] > 0], 
                   x="IFDM",
                   marginal="box",
                   color_discrete_sequence=['#0f9dd1'],
                   histnorm='probability density'
                   )

fig.update_yaxes(title='Densidade de Probabilidade', row=1, col=1)
fig.update_xaxes(title='IFDM', row=1, col=1)
st.plotly_chart(fig, use_container_width=True)


st.write('## Proporção de Desenvolvimento Municipal em Minas Gerais em 2016')

fig =  px.pie(mg.loc[df['Ano']=='2016'], 
       names='desenvolvimento',
       hole = 0.5,
       color='desenvolvimento',
        width=600,
        height=600,
       color_discrete_map={'Alto': 'green', 
                           'Moderado':'#04033d', 
                           'Regular': '#700270',
                           'Baixo':'red'})

fig.update_layout(annotations=[dict(text='Desenvolvimento', x=0.5, y=0.5, font_size=20, showarrow=False)])
st.plotly_chart(fig, use_container_width=True)

st.write('## Desenvolvimento médio por mesorregião mineira')
variavel= 'IFDM'
mg_2 = br.loc[br['UF'] == 'MG']
grupos = pd.DataFrame(mg_2.groupby('nome_meso')[variavel].mean().sort_values(ascending=False)).reset_index()
fig = px.bar(grupos, 
             x='nome_meso',
             y=variavel,
             text=grupos['IFDM'].apply(lambda x: '{:.2f}%'.format(x*100)),
             color='nome_meso')

fig.update_layout(xaxis={'categoryorder':'total descending'})
                 
fig.update_layout({
'plot_bgcolor': 'rgba(0, 0, 0, 0)',
})

fig.update_layout(
    autosize=False,
    width=600,
    height=600,
)

fig.update_traces(textfont_size=18, 
                  textangle=0, 
                  textposition="outside")

fig.update_yaxes(title='Percentual %')
fig.update_xaxes(title='IFDM médio')
st.plotly_chart(fig, use_container_width=True)


st.write('## IFDM para os municípios mineiros')
st.markdown('Intervalos de IFDM baseado nos Quantis')
st.image('imagens/mg_ifdm.png')

with st.expander("Veja a Interpretação"):
    st.write("""
        - Mínimo: 0
        - 1° Quartil: 0.63
        - 2° Quartil: 0.68
        - 3° Quartil: 0.72
        - Máximo: 0.86

        Cerca de 50% dos municípios mineiros têm desenvolvimento abaixo de 0.68, isto é, pelo indicador IFDM, grande parte dos municípios pode ser classificado como regular/moderado.
    """)

st.markdown('Intervalos homogêneos de IFDM')
st.image('imagens/mg_ifdm_h.png')

st.markdown('Mapa Fisher Jenks')
st.image('imagens/mg_fisher_jenks.png')


with st.expander("Veja a Interpretação"):
    st.write("""
        É possível observar que os municípios mais desenvolvidos se concentram nas regiões Centro-oeste, Sudeste e Sul.
    """)

st.write('## Estatística I de Moran para Minas Gerais')
st.markdown('Valor Encontrado: ')
i = pd.Series([0.19], name='I de Moran', index=['Estatística'])
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
st.image('imagens/mg_moran_d.png')

st.image('imagens/mg_moran_d2.png')

st.write('## Mapa Lisa Cluster')
st.image('imagens/mg_lisa_cluster.png')
with st.expander("Veja a Explicação"):
    st.write("""
        O mapa Lisa Cluster identifica os clusters e os outliers espaciais:
             
        - Cluesters espaciais (+): High-High (HH), Low-Low (LL)
        
        - Outliers espaciais  (-): High-Low (HL), Low-High (LH)
             
        - Não significativo (ns)

        É possível observar que há vários clusters espaciais HH no Sul e Centro-oeste do Estado.

        Também há cluster espaciais do tipo LL no Norte, Nordeste e Sudeste do Estado.

        Há outliers espaciais do tipo HL no Nordeste/Sudeste do Estado.

        Por fim, há outliers espaciais  do tipo LH no Oeste e Sul do Estado.
        
    """)


st.write('# I de Moran para as Microrregiões de Minas Gerais')
mg_micro = mg_2.groupby('nome_micro').mean().reset_index()
st.markdown(
    'Describe IFDM 2016 para as Microrregiões de Minas Gerais')
st.write(mg_micro.iloc[:, 2].describe())

with st.expander("Veja a Interpretação"):
    st.write("""
        - Observações para cerca de 66 microrregiões (IFDM positivo);
        - A média do índice IFDM para o ano de 2016 foi de 0.6733, ou seja, em média, o desenvolvimento das microrregiões é moderado;
        - O valor mínimo de desenvolvimento foi de 0.5678 da microrregião de Nanuque;
        - O valor máximo de desenvolvimento foi de 0.7704 da microrregião de Divinópolis.
    """)
    
st.write('## Distribuição do IFDM em Minas Gerais para o ano de2016')
fig = px.histogram(mg_micro.loc[mg['IFDM'] > 0], 
                   x="IFDM",
                   marginal="box",
                   color_discrete_sequence=['#0f9dd1'],
                   histnorm='probability density'
                   )

fig.update_yaxes(title='Densidade de Probabilidade', row=1, col=1)
fig.update_xaxes(title='IFDM', row=1, col=1)
st.plotly_chart(fig, use_container_width=True)



hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
