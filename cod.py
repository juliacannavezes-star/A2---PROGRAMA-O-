import streamlit as st

st.set_page_config(page_title="Simulador de Multas e Penas de Trânsito 🚦", page_icon="🚗", layout="centered")

st.title("🚦 Simulador de Multas e Penas de Trânsito")
st.write("Selecione as infrações abaixo para ver as penalidades correspondentes conforme o **Código de Trânsito Brasileiro (CTB)**:")

# Dicionário com infrações
infracoes = {
    "🚗 Excesso de velocidade até 20% acima do limite": {
        "artigo": "Art. 218, I - CTB",
        "multa": "R$ 130,16",
        "pontos": "4 pontos (infração média)",
        "consequencias": "Pode gerar aumento no seguro e suspensão em caso de reincidência."
    },
    "🚙 Excesso de velocidade acima de 50% do limite": {
        "artigo": "Art. 218, III - CTB",
        "multa": "R$ 880,41 (multa triplicada)",
        "pontos": "7 pontos (gravíssima)",
        "consequencias": "Suspensão imediata do direito de dirigir e apreensão do veículo."
    },
    "🍺 Dirigir sob influência de álcool": {
        "artigo": "Art. 165 - CTB",
        "multa": "R$ 2.934,70",
        "pontos": "7 pontos (gravíssima)",
        "consequencias": "Suspensão do direito de dirigir por 12 meses e retenção do veículo."
    },
    "📵 Usar celular ao volante": {
        "artigo": "Art. 252, VI - CTB",
        "multa": "R$ 293,47",
        "pontos": "7 pontos (gravíssima)",
        "consequencias": "Pode agravar responsabilidade em caso de acidente."
    },
    "🚫 Avançar sinal vermelho": {
        "artigo": "Art. 208 - CTB",
        "multa": "R$ 293,47",
        "pontos": "7 pontos (gravíssima)",
        "consequencias": "Pode gerar multa adicional se causar acidente."
    },
    "💺 Não usar cinto de segurança": {
        "artigo": "Art. 167 - CTB",
        "multa": "R$ 195,23",
        "pontos": "5 pontos (grave)",
        "consequencias": "Condutor pode ser multado por cada passageiro sem cinto."
    }
}

# Exibição interativa
selecionadas = st.multiselect("Escolha uma ou mais infrações:", list(infracoes.keys()))

if selecionadas:
    for item in selecionadas:
        dados = infracoes[item]
        st.subheader(item)
        st.write(f"**Artigo:** {dados['artigo']}")
        st.write(f"**Valor da multa:** {dados['multa']}")
        st.write(f"**Pontuação:** {dados['pontos']}")
        st.write(f"**Consequências:** {dados['consequencias']}")
        st.markdown("---")
else:
    st.info("⬆️ Selecione uma infração acima para visualizar as penalidades correspondentes.")
