import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# Configuração da página
st.set_page_config(
    page_title="Dashboard Interativo",
    page_icon="📊",
    layout="wide"
)

# Título do aplicativo
st.title("📊 Dashboard de Dados Governamentais")
st.markdown("---")

# Carregamento de dados (substitua pela URL direta do arquivo)
@st.cache_data
def load_data():
    # Converta o link do SharePoint para URL de download direto:
    # Substitua toda a parte após "personal/" por "_layouts/15/download.aspx?share=..."
    url = "https://gvmail-my.sharepoint.com/:x:/g/personal/c3007596_fgv_edu_br/ERkvqr-gd-lBlzJPUMarJ1cBo2IP_j0kCzea6SrFKD_oIg?e=24OG7j"
    
    try:
        df = pd.read_excel(url)
        return df
    except Exception as e:
        st.error(f"Erro ao carregar dados: {e}")
        return None

df = load_data()

if df is not None:
    # Sidebar para filtros
    st.sidebar.header("Filtros")
    
    # Exemplo de filtros (adaptar conforme colunas do seu dataset)
    if 'categoria' in df.columns:
        categorias = st.sidebar.multiselect(
            "Selecione as categorias:",
            options=df['categoria'].unique(),
            default=df['categoria'].unique()
        )
        df = df[df['categoria'].isin(categorias)]
    
    if 'data' in df.columns:
        data_min = df['data'].min()
        data_max = df['data'].max()
        data_range = st.sidebar.date_input(
            "Selecione o período:",
            value=(data_min, data_max),
            min_value=data_min,
            max_value=data_max
        )
        if len(data_range) == 2:
            df = df[(df['data'] >= data_range[0]) & (df['data'] <= data_range[1])]

    # Métricas principais
    st.header("Principais Indicadores")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if 'valor' in df.columns:
            total = df['valor'].sum()
            st.metric("Valor Total", f"R$ {total:,.2f}")
    
    with col2:
        if 'processos' in df.columns:
            processos = df['processos'].count()
            st.metric("Total de Processos", processos)
    
    with col3:
        if 'tempo_medio' in df.columns:
            tempo = df['tempo_medio'].mean()
            st.metric("Tempo Médio (dias)", f"{tempo:.1f}")
    
    with col4:
        if 'eficiencia' in df.columns:
            eficiencia = df['eficiencia'].mean()
            st.metric("Eficiência Geral", f"{eficiencia:.2%}")

    # Gráficos interativos
    st.markdown("---")
    st.header("Visualizações Interativas")

    col1, col2 = st.columns(2)
    
    with col1:
        if all(x in df.columns for x in ['categoria', 'valor']):
            fig_bar = px.bar(
                df,
                x='categoria',
                y='valor',
                title="Valores por Categoria",
                color='categoria'
            )
            st.plotly_chart(fig_bar, use_container_width=True)
        
        if 'data' in df.columns and 'valor' in df.columns:
            fig_line = px.line(
                df,
                x='data',
                y='valor',
                title="Evolução Temporal",
                color='categoria' if 'categoria' in df.columns else None
            )
            st.plotly_chart(fig_line, use_container_width=True)

    with col2:
        if all(x in df.columns for x in ['status', 'valor']):
            fig_pie = px.pie(
                df,
                values='valor',
                names='status',
                title="Distribuição por Status"
            )
            st.plotly_chart(fig_pie, use_container_width=True)
        
        if all(x in df.columns for x in ['regiao', 'valor']):
            fig_map = px.scatter_geo(
                df,
                locations='regiao',
                locationmode='country names',
                size='valor',
                title="Distribuição Geográfica",
                projection='natural earth'
            )
            st.plotly_chart(fig_map, use_container_width=True)

    # Tabela interativa
    st.markdown("---")
    st.header("Tabela de Dados")
    st.dataframe(df, use_container_width=True)

else:
    st.error("""
    Não foi possível carregar os dados. Verifique:
    1. O link de download direto do arquivo
    2. A estrutura do dataframe
    3. As permissões de acesso ao arquivo
    """)
