import streamlit as st

# Configurações da página
st.set_page_config(page_title="Simulador de Multas e Penas de Trânsito 🚗", page_icon="🚦", layout="centered")

# Cabeçalho
st.title("🚦 Simulador de Multas e Penas de Trânsito")
st.markdown("Selecione as infrações abaixo para visualizar as penalidades correspondentes segundo o **Código de Trânsito Brasileiro (CTB)**.")

# Dicionário com dados das infrações
infracoes = {
    "🚗 Excesso de velocidade até 20% acima do limite": {
        # "artigo": "Art. 218, I - CTB:  Transitar em velocidade superior à máxima permitida para o local, medida por instrumento ou equipamento hábil, em rodovias, vias de trânsito rápido, vias arteriais e demais vias:
I - quando a velocidade for superior à máxima em até 20% (vinte por cento)",
        "multa": "R$ 130,16",
        "pontos": "4 pontos (infração média)",
        "consequencias": "Pode gerar aumento no valor do seguro e suspensão em caso de reincidência."
    },
    "🚙 Excesso de velocidade acima de 50% do limite": {
        "artigo": "Art. 218, III - CTB: Transitar em velocidade superior à máxima permitida para o local, medida por instrumento ou equipamento hábil, em rodovias, vias de trânsito rápido, vias arteriais e demais vias:quando a velocidade for superior à máxima em mais de 50% (cinqüenta por cento): (Incluído pela Lei nº 11.334, de 2006)",
        "multa": "R$ 880,41 (multa triplicada)",
        "pontos": "7 pontos (gravíssima)",
        "consequencias": "Suspensão imediata do direito de dirigir e apreensão do veículo."
    },
    "🍺 Dirigir sob influência de álcool": {
        "artigo": "Art. 165 - CTB: Dirigir sob a influência de álcool ou de qualquer outra substância psicoativa que determine dependência",
        "multa": "R$ 2.934,70",
        "pontos": "7 pontos (gravíssima)",
        "consequencias": "Suspensão do direito de dirigir por 12 meses e retenção do veículo."
    },
    "📵 Usar celular ao volante": {
        "artigo": "Art. 252, VI - CTB: Dirigir o veículo:  utilizando-se de fones nos ouvidos conectados a aparelhagem sonora ou de telefone celular; ",
        "multa": "R$ 293,47",
        "pontos": "7 pontos (gravíssima)",
        "consequencias": "Pode agravar a responsabilidade do condutor em caso de acidente."
    },
    "🚫 Avançar sinal vermelho": {
        "artigo": "Art. 208 - CTB: Avançar o sinal vermelho do semáforo ou o de parada obrigatória, exceto onde houver sinalização que permita a livre conversão à direita prevista no art. 44-A deste Código",
        "multa": "R$ 293,47",
        "pontos": "7 pontos (gravíssima)",
        "consequencias": "Pode gerar multa adicional se causar acidente."
    },
    "💺 Não usar cinto de segurança": {
        # "artigo": "Art. 167 - CTB: Deixar o condutor ou passageiro de usar o cinto de segurança, conforme previsto no art. 65:",
        "multa": "R$ 195,23",
        "pontos": "5 pontos (grave)",
        "consequencias": "Condutor pode ser multado por cada passageiro sem cinto."
    }
}

# Checklist de seleção
st.subheader("✅ Escolha as infrações cometidas:")
selecionadas = st.multiselect("", list(infracoes.keys()))

# Exibição dos resultados
if selecionadas:
    for item in selecionadas:
        dados = infracoes[item]
        st.markdown("---")
        st.header(item)

        with st.expander("📜 Clique aqui para ver o artigo do CTB"):
            st.write(f"**{dados['artigo']}**")

        with st.expander("💰 Clique aqui para ver o valor da multa"):
            st.write(f"**{dados['multa']}**")

        with st.expander("⚠️ Clique aqui para ver a pontuação na CNH"):
            st.write(f"**{dados['pontos']}**")

        with st.expander("🚫 Clique aqui para ver as consequências"):
            st.write(f"**{dados['consequencias']}**")

else:
    st.info("⬆️ Selecione uma ou mais infrações acima para visualizar as informações detalhadas.")

# Rodapé
st.markdown("---")
st.caption("Desenvolvido em Python com ❤️ no Streamlit | Dados baseados no Código de Trânsito Brasileiro (CTB)")
