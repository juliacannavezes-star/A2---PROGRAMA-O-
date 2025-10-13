import streamlit as st

st.set_page_config(page_title="JurisCenários: Simulador Jurídico", layout="wide")

st.title("⚖️ JurisCenários")
st.markdown("Explore como o Direito Penal, Civil e Constitucional se aplicam em situações reais e hipotéticas.")

cenarios = {
    "🚔 Fui abordado pela polícia sem motivo aparente": {
        "Área do Direito": "Constitucional & Penal",
        "Fundamento Legal": [
            "Art. 5º, II da CF - 'ninguém será obrigado a fazer ou deixar de fazer alguma coisa senão em virtude de lei'",
            "Lei de Abuso de Autoridade (Lei 13.869/2019)",
            "Direito à liberdade e à dignidade da pessoa humana"
        ],
        "Análise Jurídica": """
        A abordagem policial deve ter fundamento em suspeita razoável. Caso contrário, pode configurar abuso de autoridade. A Constituição garante a liberdade de ir e vir e a proteção contra ações arbitrárias do Estado.
        """,
        "Desdobramentos Possíveis": [
            "Representação contra o agente público",
            "Pedido de indenização por danos morais",
            "Habeas corpus preventivo, em casos de repetição"
        ]
    },

    "🏠 O locador invadiu meu imóvel alugado sem autorização": {
        "Área do Direito": "Civil",
        "Fundamento Legal": [
            "Art.  invasion of privacy and peaceful possession.",
            "Lei do Inquilinato (Lei 8.245/91), art. 5º e seguintes",
            "Art.  invasion of property — Art.  invasion of possession"
        ],
        "Análise Jurídica": """
        O locador perde o direito de posse direta ao alugar o imóvel. A entrada sem autorização configura violação à posse, podendo inclusive gerar responsabilização civil e penal (violação de domicílio - art.  invasion of home).
        """,
        "Desdobramentos Possíveis": [
            "Ação de indenização por danos morais e materiais",
            "Possibilidade de denúncia penal (violação de domicílio)",
            "Rescisão do contrato por justa causa"
        ]
    },

    "💬 Fui ofendido em rede social por uma figura pública": {
        "Área do Direito": "Civil & Penal",
        "Fundamento Legal": [
            "Código Civil - Art. 186 e 927 (responsabilidade civil)",
            "Código Penal - Art. 139 (difamação), 140 (injúria)",
            "Marco Civil da Internet (Lei 12.965/14)"
        ],
        "Análise Jurídica": """
        Ofensas em ambiente digital têm o mesmo valor jurídico que na vida real. Há possibilidade de ação por danos morais e processo criminal, dependendo da gravidade e da intencionalidade da conduta.
        """,
        "Desdobramentos Possíveis": [
            "Pedido judicial de remoção de conteúdo e identificação do autor",
            "Ação de indenização por dano moral",
            "Queixa-crime por difamação ou injúria"
        ]
    },

    "👨‍⚖️ Um projeto de lei quer restringir liberdade de expressão de jornalistas": {
        "Área do Direito": "Constitucional",
        "Fundamento Legal": [
            "Art. 5º, IX da CF - liberdade de expressão",
            "Art. 220 da CF - liberdade de imprensa",
            "Cláusulas pétreas (Art. 60, §4º, IV - CF)"
        ],
        "Análise Jurídica": """
        Qualquer tentativa de limitar a liberdade de imprensa ou expressão fere cláusulas pétreas da Constituição. Tais propostas são inconstitucionais por violar direitos fundamentais.
        """,
        "Desdobramentos Possíveis": [
            "Ação Direta de Inconstitucionalidade (ADI)",
            "Manifestação de órgãos de classe (OAB, ABI, etc)",
            "Judicialização antes da sanção"
        ]
    },

    "🔐 Empresa compartilhou meus dados pessoais sem consentimento": {
        "Área do Direito": "Civil & Constitucional",
        "Fundamento Legal": [
            "Lei Geral de Proteção de Dados (LGPD - Lei 13.709/18)",
            "Art. 5º, X e XII da CF - intimidade e sigilo de dados",
            "CDC - relação de consumo e boa-fé objetiva"
        ],
        "Análise Jurídica": """
        A empresa violou seu direito à privacidade. A LGPD exige consentimento claro e informado para o tratamento e compartilhamento de dados pessoais.
        """,
        "Desdobramentos Possíveis": [
            "Denúncia à ANPD (Autoridade Nacional de Proteção de Dados)",
            "Ação judicial por danos morais",
            "Multa administrativa à empresa"
        ]
    }
}

# Interface de seleção
cenario_escolhido = st.selectbox("🧩 Escolha um cenário jurídico:", list(cenarios.keys()))

dados = cenarios[cenario_escolhido]

st.header(f"📌 Situação: {cenario_escolhido}")
st.markdown(f"**📚 Área do Direito Envolvida:** {dados['Área do Direito']}")

st.subheader("🔎 Fundamento Legal")
for artigo in dados["Fundamento Legal"]:
    st.markdown(f"- {artigo}")

st.subheader("📖 Análise Jurídica")
st.markdown(dados["Análise Jurídica"])

st.subheader("⚖️ Desdobramentos Possíveis")
for desdobramento in dados["Desdobramentos Possíveis"]:
    st.markdown(f"- {desdobramento}")
