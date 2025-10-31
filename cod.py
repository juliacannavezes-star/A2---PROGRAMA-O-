import streamlit as st
from bs4 import BeautifulSoup
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Explorador do Código Penal", layout="wide")

# --- Carregar o arquivo HTML ---
with open("data/codigo_penal.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

# Extrair artigos (linhas que começam com "Art.")
artigos = []
for p in soup.find_all("p"):
    texto = p.get_text().strip()
    if texto.startswith("Art."):
        num = texto.split(" ")[1].split("º")[0].replace("-", "")
        artigos.append({"Artigo": f"Art. {num}", "Texto": texto})

df = pd.DataFrame(artigos)

# --- Interface do App ---
st.title("⚖️ Explorador do Código Penal Brasileiro")
st.write("Pesquise artigos e visualize o Código Penal de forma interativa.")

aba = st.sidebar.radio("Menu", ["Pesquisar", "Gráficos", "Sobre"])

if aba == "Pesquisar":
    termo = st.text_input("Digite número ou palavra-chave do artigo:")
    if termo:
        resultados = df[df["Texto"].str.contains(termo, case=False, na=False)]
        if len(resultados) > 0:
            st.success(f"{len(resultados)} artigo(s) encontrado(s):")
            for _, row in resultados.iterrows():
                st.markdown(f"### {row['Artigo']}")
                st.write(row['Texto'])
        else:
            st.warning("Nenhum artigo encontrado.")

elif aba == "Gráficos":
    st.subheader("Distribuição dos Artigos")
    df["Número"] = df["Artigo"].str.extract(r"(\d+)").astype(int)
    bins = [0, 50, 100, 200, 300, 400]
    labels = ["1-50", "51-100", "101-200", "201-300", "301-400"]
    df["Faixa"] = pd.cut(df["Número"], bins=bins, labels=labels)
    graf = df["Faixa"].value_counts().sort_index().reset_index()
    graf.columns = ["Faixa de Artigos", "Quantidade"]

    fig = px.bar(graf, x="Faixa de Artigos", y="Quantidade", title="Quantidade de Artigos por Faixa Numérica")
    st.plotly_chart(fig, use_container_width=True)

else:
    st.info("""
    App criado para explorar o **Código Penal Brasileiro (Decreto-Lei nº 2.848/1940)**.
    
    - Busca rápida por artigos
    - Visualização analítica por gráfico
    - Design simples e moderno

    📚 Fonte: [Planalto.gov.br](https://www.planalto.gov.br/ccivil_03/decreto-lei/del2848compilado.htm)
    """)
