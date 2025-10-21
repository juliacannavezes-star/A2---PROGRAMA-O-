import streamlit as st

st.title("Calculadora de Dosimetria Penal")
st.subheader("Baseada nas três fases do Código Penal Brasileiro")

# Fase 1 - Pena Base
st.header("Fase 1: Fixação da Pena-Base (Art. 59 CP)")
st.write("Avalie os seguintes elementos:")

culpabilidade = st.slider("Culpabilidade", 0.0, 1.0, 0.5)
antecedentes = st.slider("Antecedentes", 0.0, 1.0, 0.5)
conduta_social = st.slider("Conduta Social", 0.0, 1.0, 0.5)
personalidade = st.slider("Personalidade do Agente", 0.0, 1.0, 0.5)
motivos = st.slider("Motivos do Crime", 0.0, 1.0, 0.5)
circunstancias = st.slider("Circunstâncias do Crime", 0.0, 1.0, 0.5)
consequencias = st.slider("Consequências do Crime", 0.0, 1.0, 0.5)
comportamento_vitima = st.slider("Comportamento da Vítima", 0.0, 1.0, 0.5)

# Cálculo da pena base (exemplo simplificado)
pena_base = (culpabilidade + antecedentes + conduta_social + personalidade + 
             motivos + circunstancias + consequencias + comportamento_vitima) / 8

st.metric("Intensidade da Pena-Base", f"{pena_base:.1%}")

# Fase 2 - Atenuantes e Agravantes
st.header("Fase 2: Atenuantes e Agravantes (Arts. 61-68 CP)")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Atenuantes")
    atenuante_generica = st.checkbox("Atenuante genérica (Art. 65)")
    atenuante_especifica = st.number_input("Nº de atenuantes específicas", 0, 10, 0)

with col2:
    st.subheader("Agravantes")
    agravante_generica = st.checkbox("Agravante genérica (Art. 61)")
    agravante_especifica = st.number_input("Nº de agravantes específicas", 0, 10, 0)

# Cálculo de ajustes
ajuste_atenuantes = (atenuante_generica * 0.1) + (atenuante_especifica * 0.05)
ajuste_agravantes = (agravante_generica * 0.1) + (agravante_especifica * 0.05)

pena_intermediaria = pena_base + ajuste_agravantes - ajuste_atenuantes
pena_intermediaria = max(0.0, min(1.0, pena_intermediaria))  # Limita entre 0% e 100%

st.metric("Pena Após Atenuantes/Agravantes", f"{pena_intermediaria:.1%}")

# Fase 3 - Causas de Aumento e Diminuição
st.header("Fase 3: Causas de Aumento e Diminuição (Arts. 69-70 CP)")

col3, col4 = st.columns(2)

with col3:
    causas_aumento = st.number_input("Nº de causas de aumento", 0, 5, 0)
    
with col4:
    causas_diminuicao = st.number_input("Nº de causas de diminuição", 0, 5, 0)

# Cálculo final
ajuste_final = (causas_aumento * 0.1) - (causas_diminuicao * 0.1)
pena_final = pena_intermediaria + ajuste_final
pena_final = max(0.0, min(1.0, pena_final))  # Limita entre 0% e 100%

st.metric("Pena Final Calculada", f"{pena_final:.1%}")

# Conversão para anos (exemplo)
st.header("Resultado Final")
pena_anos = pena_final * 30  # Supondo pena máxima de 30 anos
st.write(f"Pena estimada: **{pena_anos:.1f} anos** (baseado em pena máxima de 30 anos)")

st.markdown("---")
st.caption("""
**Nota:** Esta calculadora é uma simplificação didática. 
A dosimetria real deve considerar a análise detalhada de cada caso concreto 
e a aplicação integral da legislação penal.
""")
