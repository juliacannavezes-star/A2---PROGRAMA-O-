import streamlit as st

# ------------------------------
# GLOSSÁRIO JURÍDICO INTERATIVO
# ------------------------------

st.set_page_config(page_title="Glossário Jurídico Interativo", layout="centered")

st.title("📘 Glossário Jurídico Interativo")
st.write("Pesquise termos jurídicos, visualize suas definições e exemplos de uso prático.")

# Base simples de termos jurídicos (pode ser expandida facilmente)
glossario = {
    "Habeas Corpus": {
        "definicao": "Remédio constitucional que visa proteger o direito de locomoção quando alguém sofre ou está na iminência de sofrer violência ou coação ilegal.",
        "exemplo": "Um advogado impetrou Habeas Corpus para libertar um cliente preso sem mandado judicial."
    },
    "Ação Civil Pública": {
        "definicao": "Instrumento processual usado para proteger interesses difusos e coletivos, como o meio ambiente ou o patrimônio público.",
        "exemplo": "O Ministério Público ajuizou uma Ação Civil Pública contra uma empresa por poluição ambiental."
    },
    "Dolo": {
        "definicao": "Intenção de praticar um ato ilícito ou causar um resultado criminoso.",
        "exemplo": "O réu agiu com dolo ao planejar e executar o crime de furto."
    },
    "Culpa": {
        "definicao": "Conduta imprudente, negligente ou imperita, sem intenção de causar o resultado, mas que o produz.",
        "exemplo": "O motorista foi condenado por homicídio culposo após causar um acidente fatal."
    },
    "Prescrição": {
        "definicao": "Perda do direito de punir ou de exigir judicialmente um direito devido ao decurso do tempo.",
        "exemplo": "O juiz reconheceu a prescrição do crime, extinguindo a punibilidade do réu."
    },
}

# Campo de busca
busca = st.text_input("🔍 Buscar termo jurídico:")

# Se o usuário digitar algo, faz a busca
if busca:
    resultados = {termo: info for termo, info in glossario.items() if busca.lower() in termo.lower()}
    
    if resultados:
        for termo, info in resultados.items():
            st.subheader(f"📖 {termo}")
            st.write(f"**Definição:** {info['definicao']}")
            st.write(f"**Exemplo:** _{info['exemplo']}_")
            st.markdown("---")
    else:
        st.warning("Nenhum termo encontrado. Tente outra palavra-chave.")
else:
    st.info("Digite uma palavra-chave acima para buscar um termo jurídico.")

# Rodapé
st.markdown("<br><small>Desenvolvido em Streamlit • Versão 1.0</small>", unsafe_allow_html=True)
