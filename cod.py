import streamlit as st

# Dicionário simulando crimes e suas penas mínimas (em meses)
CODIGO_PENAL = {
    "Furto simples": 4,
    "Roubo": 8,
    "Homicídio doloso": 12,
    "Estelionato": 3,
    "Receptação": 3
}

def main():
    st.title("Calculadora de Dosimetria Penal")
    st.subheader("Baseada nas 3 fases do Código Penal")
    
    # Fase 1 - Pena Base
    st.header("Fase 1: Pena Base")
    crime = st.selectbox("Selecione o tipo de crime:", list(CODIGO_PENAL.keys()))
    circunstancias = st.number_input("Número de circunstâncias agravantes:", min_value=0, step=1)
    
    pena_minima = CODIGO_PENAL[crime]
    pena_base = pena_minima * (1 + circunstancias * 1/8)
    
    st.write(f"Pena mínima: {pena_minima} meses")
    st.write(f"Pena base após fase 1: {pena_base:.2f} meses")
    
    # Fase 2 - Circunstâncias
    st.header("Fase 2: Circunstâncias")
    agravantes = st.number_input("Número de agravantes:", min_value=0, step=1)
    atenuantes = st.number_input("Número de atenuantes:", min_value=0, step=1)
    
    pena_fase2 = pena_base * (1 + agravantes * 1/6) * (1 - atenuantes * 1/6)
    st.write(f"Pena após fase 2: {pena_fase2:.2f} meses")
    
    # Fase 3 - Majorantes/Minorantes
    st.header("Fase 3: Causas de aumento/diminução")
    majorantes = st.number_input("Percentual de majorantes (%):", min_value=0.0, step=1.0)
    minorantes = st.number_input("Percentual de minorantes (%):", min_value=0.0, step=1.0)
    
    pena_final = pena_fase2 * (1 + majorantes/100) * (1 - minorantes/100)
    
    st.header("Resultado Final")
    st.success(f"Pena final calculada: {pena_final:.2f} meses")
    
    # Conversão para anos/meses
    anos = int(pena_final // 12)
    meses = int(pena_final % 12)
    st.info(f"Equivalente a: {anos} anos e {meses} meses")

if __name__ == "__main__":
    main()
