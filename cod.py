import streamlit as st

st.set_page_config(page_title="Calculadora de Dosimetria Penal", page_icon="⚖️")

st.title("⚖️ Calculadora de Dosimetria Penal")
st.markdown("""
Este aplicativo segue as três fases da dosimetria de penas do **Código Penal Brasileiro**:
1. **Pena Base** (Art. 59 CP) - Critérios de dosimetria
2. **Circunstâncias** (Atenuantes/Agravantes) - Arts. 61 a 68 CP
3. **Causas de Aumento/Diminuição** (Arts. 69 e 70 CP)
""")

# Fase 1 - Pena Base
st.header("1️⃣ Fase 1 - Pena Base (Art. 59 CP)")
st.subheader("Critérios de dosimetria")

culpabilidade = st.slider("Culpabilidade", 0.0, 1.0, 0.5, help="Grau de reprovação da conduta")
antecedentes = st.slider("Antecedentes", 0.0, 1.0, 0.5, help="Histórico do agente")
conduta_social = st.slider("Conduta Social", 0.0, 1.0, 0.5, help="Comportamento em sociedade")
personalidade = st.slider("Personalidade do Agente", 0.0, 1.0, 0.5)
motivos = st.slider("Motivos do Crime", 0.0, 1.0, 0.5)
circunstancias = st.slider("Circunstâncias do Crime", 0.0, 1.0, 0.5)
comportamento_vitima = st.slider("Comportamento da Vítima", 0.0, 1.0, 0.5)

# Cálculo da pena base (exemplo simplificado)
pena_base = (culpabilidade + antecedentes + conduta_social + personalidade + 
             motivos + circunstancias + comportamento_vitima) / 7 * 12

st.metric("Pena Base Estimada", f"{pena_base:.2f} anos")

# Fase 2 - Circunstâncias
st.header("2️⃣ Fase 2 - Circunstâncias (Arts. 61-68 CP)")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Atenuantes")
    atenuante_menor = st.checkbox("Art. 65 - Agente menor de 21 anos")
    atenuante_maior = st.checkbox("Art. 65 - Agente maior de 70 anos")
    atenuante_arrependimento = st.checkbox("Art. 66 - Arrependimento")
    atenuante_confissao = st.checkbox("Confissão espontânea")

with col2:
    st.subheader("Agravantes")
    agravante_reincidente = st.checkbox("Art. 61 - Reincidência")
    agravante_ocultacao = st.checkbox("Art. 62 - Ocultação de autoria")
    agravante_motivo_futil = st.checkbox("Art. 63 - Motivo fútil")
    agravante_crueldade = st.checkbox("Art. 64 - Crueldade")

# Cálculo das circunstâncias
ajuste_circunstancias = 0
if atenuante_menor or atenuante_maior or atenuante_arrependimento or atenuante_confissao:
    ajuste_circunstancias -= 0.5  # Redução simplificada
if agravante_reincidente or agravante_ocultacao or agravante_motivo_futil or agravante_crueldade:
    ajuste_circunstancias += 0.5  # Aumento simplificado

pena_intermediaria = max(0, pena_base + ajuste_circunstancias)
st.metric("Pena Após Circunstâncias", f"{pena_intermediaria:.2f} anos")

# Fase 3 - Causas de Aumento/Diminuição
st.header("3️⃣ Fase 3 - Causas de Aumento/Diminuição (Arts. 69-70 CP)")

aumentos = st.number_input("Percentual de Aumento (%)", min_value=0, max_value=300, value=0)
diminuicoes = st.number_input("Percentual de Diminuição (%)", min_value=0, max_value=100, value=0)

# Cálculo final
pena_final = pena_intermediaria * (1 + aumentos/100) * (1 - diminuicoes/100)
pena_final = max(0, pena_final)  # Não permite pena negativa

st.metric("Pena Final Estimada", f"{pena_final:.2f} anos")

# Considerações finais
st.warning("""
**Atenção:** Esta calculadora é uma ferramenta auxiliar e não substitui 
a análise jurídica profissional. Consulte sempre um advogado especializado.
""")

st.info(""**
Referências legais:
- Arts. 59 a 70 do Código Penal
- Súmulas relevantes do STJ e STF
**")
