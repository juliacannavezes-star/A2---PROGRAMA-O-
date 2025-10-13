import streamlit as st

st.set_page_config(page_title="📔 Diário de Direitos", layout="wide")

st.title("📔 Diário de Direitos")
st.markdown("Explore situações do dia a dia sob a ótica do **Direito Penal, Civil e Constitucional**. Aprenda como os direitos se manifestam na prática.")

# Lista de casos cotidianos
casos = {
    "1. Uma briga de trânsito com agressão física": {
        "Área do Direito": ["Penal", "Civil"],
        "Descrição": "Durante uma discussão no trânsito, um dos motoristas agride fisicamente o outro, resultando em lesões leves.",
        "Direitos Envolvidos": [
            "Direito à integridade física",
            "Responsabilidade civil por dano",
            "Dever de reparação",
            "Sanção penal"
        ],
        "Artigos Relevantes": [
            "CP, Art. 129 - Lesão corporal",
            "CC, Art. 186 e 927 - Responsabilidade civil por ato ilícito",
            "CF, Art. 5º, V - Direito à indenização por dano moral"
        ],
        "Atores Jurídicos": ["Delegado de polícia", "Promotor de justiça", "Juiz criminal", "Juiz cível"],
        "Consequências": [
            "Ação penal pública incondicionada (lesão)",
            "Possível prisão em flagrante",
            "Indenização por danos morais e materiais"
        ]
    },

    "2. Uma escola pública nega matrícula a uma criança com deficiência": {
        "Área do Direito": ["Constitucional", "Civil"],
        "Descrição": "Uma mãe tenta matricular seu filho com deficiência em uma escola pública, mas é informada que não há 'estrutura adequada'.",
        "Direitos Envolvidos": [
            "Direito à educação",
            "Princípio da igualdade",
            "Acesso universal a serviços públicos"
        ],
        "Artigos Relevantes": [
            "CF, Art. 205 - Direito à educação",
            "CF, Art. 5º, caput e I - Igualdade",
            "Lei Brasileira de Inclusão - Lei 13.146/15"
        ],
        "Atores Jurídicos": ["Defensoria Pública", "Ministério Público", "Juiz de Direito"],
        "Consequências": [
            "Mandado de segurança para garantir matrícula",
            "Ação civil pública",
            "Multa e responsabilização da administração"
        ]
    },

    "3. Um político bloqueia um cidadão nas redes sociais públicas": {
        "Área do Direito": ["Constitucional", "Civil"],
        "Descrição": "Um vereador, usando rede social institucional, bloqueia um cidadão crítico ao seu mandato.",
        "Direitos Envolvidos": [
            "Liberdade de expressão",
            "Acesso à informação pública",
            "Transparência administrativa"
        ],
        "Artigos Relevantes": [
            "CF, Art. 5º, IV e XIV - Liberdade de expressão e acesso à informação",
            "CF, Art. 37 - Princípios da Administração Pública",
            "Jurisprudência do STF sobre redes institucionais"
        ],
        "Atores Jurídicos": ["Juiz Federal", "Advogado constitucionalista", "Ministério Público"],
        "Consequências": [
            "Obrigação de desbloquear o cidadão",
            "Ação de indenização",
            "Precedente constitucional aplicado"
        ]
    },

    "4. Um banco vaza os dados de um cliente na internet": {
        "Área do Direito": ["Civil", "Constitucional"],
        "Descrição": "Dados bancários de um cliente são indevidamente compartilhados por uma fintech, sem autorização.",
        "Direitos Envolvidos": [
            "Direito à privacidade",
            "Sigilo bancário",
            "Proteção de dados pessoais"
        ],
        "Artigos Relevantes": [
            "LGPD - Lei 13.709/18",
            "CF, Art. 5º, X e XII - Privacidade e sigilo de dados",
            "CC, Art. 927 - Responsabilidade civil objetiva"
        ],
        "Atores Jurídicos": ["Advogado cível", "Autoridade Nacional de Proteção de Dados", "Juiz cível"],
        "Consequências": [
            "Multa administrativa à empresa",
            "Ação de danos morais",
            "Obrigação de retratação e correção"
        ]
    }
}

# Interface
caso_escolhido = st.selectbox("📖 Escolha um caso para explorar:", list(casos.keys()))
dados = casos[caso_escolhido]

st.header(f"🔍 {caso_escolhido}")
st.markdown(f"**📘 Descrição do caso:** {dados['Descrição']}")

col1, col2 = st.columns(2)

with col1:
    st.subheader("⚖️ Área(s) do Direito Envolvida(s)")
    for area in dados["Área do Direito"]:
        st.markdown(f"- {area}")

    st.subheader("📚 Direitos Envolvidos")
    for d in dados["Direitos Envolvidos"]:
        st.markdown(f"- {d}")

    st.subheader("👥 Atores Jurídicos Típicos")
    for a in dados["Atores Jurídicos"]:
        st.markdown(f"- {a}")

with col2:
    st.subheader("📜 Artigos e Leis Relacionadas")
    for artigo in dados["Artigos Relevantes"]:
        st.markdown(f"- {artigo}")

    st.subheader("🧾 Possíveis Consequências Jurídicas")
    for c in dados["Consequências"]:
        st.markdown(f"- {c}")

st.markdown("---")
st.info("💡 Este modelo ajuda a entender como o Direito se aplica a situações reais, conectando teoria e prática.")

