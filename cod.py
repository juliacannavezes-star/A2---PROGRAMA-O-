import streamlit as st

st.set_page_config(page_title="Mapa Interativo do Direito", layout="wide")

st.title("⚖️ Mapa Interativo do Direito")
st.markdown("Escolha uma disciplina para explorar os conceitos essenciais do Direito Brasileiro.")

# Sidebar de seleção
materia = st.sidebar.selectbox(
    "📘 Escolha uma disciplina",
    ["Direito Penal", "Direito Civil", "Direito Constitucional "]
)


conteudo = {

    "Direito Penal": {
        "Conceitos-chave": {
            "Crime": "Infração penal a que a lei comina pena de reclusão ou detenção.",
            "Dolo e Culpa": "Dolo: intenção de cometer o crime. Culpa: ausência de intenção, mas com imprudência/negligência.",
            "Princípio da Legalidade": "Não há crime sem lei anterior que o defina (art. 1º do CP)."
        },
        "Artigos Relevantes": [
            "Art. 121 - Homicídio",
            "Art. 213 - Estupro",
            "Art. 5º, XXXIX da CF - Legalidade Penal"
        ],
        "Aplicações Práticas": [
            "Julgamento de homicídios dolosos pelo Tribunal do Júri.",
            "Redução de pena por arrependimento posterior."
        ]
    },

    "Direito Civil": {
        "Conceitos-chave": {
            "Pessoa Natural": "Todo ser humano, titular de direitos e deveres (art. 1º CC).",
            "Capacidade Civil": "Aptidão para exercer direitos e deveres. Pode ser plena ou relativa.",
            "Domicílio": "Residência habitual com ânimo definitivo (art. 70 CC)."
        },
        "Artigos Relevantes": [
            "Art. 1º ao 4º - Das Pessoas Naturais",
            "Art. 70 - Domicílio",
            "Art. 11 ao 21 - Direitos da personalidade"
        ],
        "Aplicações Práticas": [
            "Registro de nascimento em cartório.",
            "Interdição de pessoa incapaz por deficiência mental."
        ]
    },

    "Direito Constitucional": {
        "Conceitos-chave": {
            "Constituição": "Norma superior que organiza o Estado e garante direitos fundamentais.",
            "Poder Constituinte": "Capacidade de criar ou modificar a Constituição.",
            "Direitos Fundamentais": "Liberdade, igualdade, dignidade e garantias individuais (art. 5º)."
        },
        "Artigos Relevantes": [
            "Art. 1º ao 5º - Princípios fundamentais e direitos individuais",
            "Art. 60 - Cláusulas pétreas",
            "Art. 37 - Princípios da Administração Pública"
        ],
        "Aplicações Práticas": [
            "Controle de constitucionalidade de leis pelo STF.",
            "Proteção contra censura e liberdade de expressão."
        ]
    }
}

dados = conteudo[materia]

st.header(f"📚 {materia}")

col1, col2 = st.columns(2)

with col1:
    st.subheader("🔑 Conceitos-Chave")
    for titulo, explicacao in dados["Conceitos-chave"].items():
        st.markdown(f"**{titulo}**: {explicacao}")

with col2:
    st.subheader("📜 Artigos Relevantes")
    for artigo in dados["Artigos Relevantes"]:
        st.markdown(f"- {artigo}")

st.markdown("---")
st.subheader("⚖️ Aplicações Práticas")
for exemplo in dados["Aplicações Práticas"]:
    st.markdown(f"- {exemplo}")
