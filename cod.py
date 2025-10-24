# app.py
import re
import io
from typing import List, Tuple, Optional, Dict
import streamlit as st

# PDF parsing
try:
    from PyPDF2 import PdfReader
except Exception:
    PdfReader = None

# ---- Helper functions ----
ARTICLE_REGEX = re.compile(r'(?:Art\.|Artigo)\s*\.?\s*(\d+)\s*[ºº\w\.,\s-]*\s*(?:[^\n]*\n){0,2}', re.IGNORECASE)
# Pattern to capture typical penalty phrases like "reclusão, de 1 a 4 anos" or "detenção, de 6 meses a 2 anos"
PENALTY_REGEX = re.compile(
    r'(?P<tipo>reclus[aã]o|deten[cç][aã]o|multa|penas?[^.,;\n]*)[^\n,.;]*?(?:de\s+)?(?:(?P<min>\d+(?:[.,]\d+)?)\s*(?:anos|ano|meses|m[eê]s|dias|dia))\s*(?:a|até|-)\s*(?P<max>\d+(?:[.,]\d+)?)\s*(?:anos|ano|meses|m[eê]s|dias|dia)',
    re.IGNORECASE
)

def extract_text_from_pdf(file_bytes: bytes) -> str:
    if PdfReader is None:
        raise RuntimeError("PyPDF2 não está instalado. Veja requirements.txt.")
    reader = PdfReader(io.BytesIO(file_bytes))
    text = []
    for page in reader.pages:
        try:
            text.append(page.extract_text() or "")
        except Exception:
            continue
    return "\n".join(text)

def extract_articles_and_penalties(text: str) -> Dict[str, Dict]:
    """
    Tenta extrair artigos e, a partir do parágrafo, localizar penalidades.
    Retorna dicionário {article_number: {"text": snippet, "penalty": (tipo,min,max,unit) or None}}
    """
    results = {}
    # find indices of "Art." occurrences to split
    art_positions = [(m.start(), m.group(1)) for m in re.finditer(r'(?:Art\.|Artigo)\s*\.?\s*(\d+)', text, re.IGNORECASE)]
    # append end
    art_positions.append((len(text), None))
    for i in range(len(art_positions)-1):
        start_idx, art_num = art_positions[i]
        end_idx = art_positions[i+1][0]
        snippet = text[start_idx:end_idx].strip()
        # find penalty inside snippet
        p = PENALTY_REGEX.search(snippet)
        penalty = None
        if p:
            min_raw = p.group('min').replace(',', '.')
            max_raw = p.group('max').replace(',', '.')
            # unit detection (years/months/days) naive:
            unit_match = re.search(r'(anos|ano|meses|m[eê]s|dias|dia)', snippet, re.IGNORECASE)
            unit = unit_match.group(1) if unit_match else 'anos'
            try:
                min_v = float(min_raw)
                max_v = float(max_raw)
                # if unit in months/days convert to years as decimal (approx)
                if re.search(r'm(e|ê)s', unit, re.IGNORECASE):
                    min_v = min_v / 12.0
                    max_v = max_v / 12.0
                elif re.search(r'dia', unit, re.IGNORECASE):
                    min_v = min_v / 365.0
                    max_v = max_v / 365.0
                penalty = {"tipo": p.group('tipo').strip(), "min": min_v, "max": max_v, "raw_unit": unit}
            except:
                penalty = None
        results[art_num] = {"text": snippet, "penalty": penalty}
    return results

def parse_uploaded_code(file) -> str:
    content_type = file.type
    data = file.read()
    text = ""
    if 'pdf' in content_type:
        text = extract_text_from_pdf(data)
    else:
        try:
            text = data.decode('utf-8')
        except Exception:
            text = data.decode('latin-1')
    return text

def compute_base_penalty(min_y: float, max_y: float, percentile: float) -> float:
    """
    percentile between 0 and 100: 50 = midpoint
    """
    return min_y + (max_y - min_y) * (percentile / 100.0)

def apply_adjustments(penalty_years: float, adjustments: List[float]) -> float:
    """
    adjustments: list of additive percents (e.g., 0.20 for +20, -0.10 for -10)
    we apply multiplicatively: final = penalty * prod(1 + adj)
    """
    result = penalty_years
    prod = 1.0
    for a in adjustments:
        prod *= (1 + a)
    return result * prod

def years_to_days(years: float) -> int:
    return int(round(years * 365))

# ---- Streamlit UI ----
st.set_page_config(page_title="Dosimetria da Pena (trifásica)", layout="wide")
st.title("App de Dosimetria da Pena — Sistema Trifásico (art. 59, 61, 65, etc.)")
st.markdown(
    """
    Este app **não substitui o trabalho do juiz**: é uma ferramenta de apoio que automatiza cálculos
    e organiza raciocínio. Configure percentuais quando a norma for específica. Consulte sempre a legislação.
    """
)

with st.expander("Referências legais rápidas (consultadas)"):
    st.write("Art. 59 (circunstâncias judiciais), arts. 61 (agravantes) e 65 (atenuantes) do Código Penal; art. 68 (sistema trifásico).")

# Upload Código Penal
st.header("1) Carregue o texto do Código Penal (PDF ou TXT)")
uploaded = st.file_uploader("Arquivo do Código Penal (PDF/TXT). Se não fizer upload, é possível inserir texto manualmente.", type=["pdf", "txt"])

extracted = ""
if uploaded:
    try:
        with st.spinner("Lendo documento..."):
            extracted = parse_uploaded_code(uploaded)
        st.success("Documento lido.")
    except Exception as e:
        st.error(f"Erro ao ler arquivo: {e}")

if not extracted:
    extracted = st.text_area("Ou cole aqui o texto do Código (ou trechos)", height=250)

if extracted:
    art_map = extract_articles_and_penalties(extracted)
    st.subheader("Artigos encontrados (amostra)")
    sample_keys = list(art_map.keys())[:30]
    for k in sample_keys:
        pen = art_map[k]["penalty"]
        if pen:
            st.write(f"Art. {k} — pena abstrata: {pen['tipo']} de {pen['min']} a {pen['max']} anos (unidade original: {pen['raw_unit']})")
        else:
            st.write(f"Art. {k} — pena não identificada automaticamente.")

    st.markdown("---")
    st.header("2) Escolha o artigo/fatos do caso")
    art_choice = st.selectbox("Selecione o artigo (número)", options=list(art_map.keys()))
    art_data = art_map[art_choice]
    st.markdown("**Texto do artigo (trecho):**")
    st.write(art_data["text"][:1000] + ("..." if len(art_data["text"])>1000 else ""))

    # If no penalty detected, allow manual input
    if not art_data["penalty"]:
        st.warning("Não foi possível extrair automaticamente a pena abstrata desse artigo. Insira-a manualmente abaixo.")
        tipo_manual = st.text_input("Tipo de pena (ex: reclusão/detenção/multa)", value="reclusão")
        min_manual = st.number_input("Pena mínima (anos)", min_value=0.0, value=1.0, step=0.5)
        max_manual = st.number_input("Pena máxima (anos)", min_value=0.0, value=4.0, step=0.5)
        penalty = {"tipo": tipo_manual, "min": min_manual, "max": max_manual, "raw_unit": "anos"}
    else:
        penalty = art_data["penalty"]

    st.markdown("**Pena abstrata identificada:**")
    st.write(penalty)

    st.header("3) Fase 1 — Pena-base (art. 59)")
    st.write("Marque as circunstâncias judiciais que influenciam a pena-base (estas servem para o juiz fixar a pena entre o mínimo e o máximo abstrato).")
    st.write("Observação: o app aplica um *peso* configurável para cada item; trate isso como auxílio — a valoração é discricionária.")
    culpabilidade = st.slider("Culpabilidade (quanto maior, maior a pena-base)", 0.0, 2.0, 1.0, 0.1)
    antecedentes = st.checkbox("Antecedentes (p.ex. antecedentes criminais)")
    conduta_social = st.checkbox("Conduta social")
    personalidade = st.checkbox("Personalidade do agente")
    motivos = st.checkbox("Motivos do crime (p.ex. fútil/torpe)")
    circunstancias = st.checkbox("Circunstâncias do crime (p.ex. traição, emboscada...)")
    consequencias = st.checkbox("Consequências do crime (lesões, morte...)")
    comportamento_vitima = st.checkbox("Comportamento da vítima")

    percentile = st.slider("Escolha posição entre mínimo e máximo abstrato (0% = mínimo, 50% = meio, 100% = máximo) — valor sugerido pela valoração do juiz",
                           0, 100, 50)

    # compute preliminary base using percentile
    base = compute_base_penalty(penalty['min'], penalty['max'], percentile)
    # crude influence of 'culpabilidade' scale: multiply by culpabilidade/1.0 (so 1 = neutral)
    base = base * (culpabilidade)

    st.write(f"Pena-base estimada (anos): **{base:.3f}** (base preliminar antes de agravantes/atenuantes)")

    st.header("4) Fase 2 — Agravantes e Atenuantes (arts. 61 / 65)")
    st.write("Marque os fatores aplicáveis. O app sugere percentuais padrão, mas você pode ajustar cada um.")
    # Example list (not exhaustive). We show common items; user can add custom.
    agr_items = {
        "reincidência (art.63)": 0.20,
        "motivo fútil/torpe (art.61 II a)": 0.15,
        "uso de violência/emboscada (art.61 II c)": 0.20,
        "abuso de poder (art.61 II g)": 0.20
    }
    aten_items = {
        "menor de 21 / maior de 70 (art.65 I)": -0.20,
        "arrependimento/regular reparação (art.65 III b)": -0.20,
        "confissão espontânea (art.65 III d)": -0.10,
        "coação/violenta emoção (art.65 III c)": -0.15
    }

    st.subheader("Agravantes (selecione as que ocorreram)")
    selected_agr = []
    agr_adjustments = []
    for k, default in agr_items.items():
        if st.checkbox(k, key=f"agr_{k}"):
            pct = st.number_input(f"Percentual para '{k}' (ex: 0.20 = +20%)", value=float(default), step=0.01, key=f"agr_pct_{k}")
            selected_agr.append(k)
            agr_adjustments.append(float(pct))

    st.subheader("Atenuantes (selecione as que ocorreram)")
    selected_aten = []
    aten_adjustments = []
    for k, default in aten_items.items():
        if st.checkbox(k, key=f"aten_{k}"):
            pct = st.number_input(f"Percentual para '{k}' (ex: -0.20 = -20%)", value=float(default), step=0.01, key=f"aten_pct_{k}")
            selected_aten.append(k)
            aten_adjustments.append(float(pct))

    # compute after phase 2
    adjustments_phase2 = agr_adjustments + aten_adjustments
    pena_provisoria = apply_adjustments(base, adjustments_phase2)
    st.write(f"Pena provisória (após agravantes/atenuantes) em anos: **{pena_provisoria:.3f}**")

    st.header("5) Fase 3 — Causas de aumento / diminuição (majorantes / minorantes)")
    st.write("Aqui entram causas especiais do Código (ex.: majorantes específicos do crime, tentativa, concurso de crimes, causa que aumenta para 1/3 etc.). Configure percentuais conforme a norma aplicável.")
    st.markdown("**Adicione causas específicas**:")
    custom_causes = st.text_area("Liste causas separadas por linha no formato: Nome|percentual (ex: 'Uso de arma|0.50' para +50% ; 'Arrependimento eficaz|-0.50')", height=120)
    causes = []
    cause_adjustments = []
    if custom_causes.strip():
        for line in custom_causes.strip().splitlines():
            if '|' in line:
                name, pct = line.split('|', 1)
                try:
                    p = float(pct.strip())
                    causes.append(name.strip())
                    cause_adjustments.append(p)
                except:
                    st.warning(f"Não entendi a linha: {line}")

    st.write("Causas adicionais aplicadas:", causes)
    pena_definitiva = apply_adjustments(pena_provisoria, cause_adjustments)
    st.write(f"**Pena definitiva (anos): {pena_definitiva:.3f}** — equivalente a {years_to_days(pena_definitiva)} dias (aprox.)")

    st.markdown("---")
    st.header("Relatório / Exportação")
    report = {
        "artigo": art_choice,
        "pena_abstrata": penalty,
        "percentile_base": percentile,
        "base_anos": round(base, 4),
        "agravantes": selected_agr,
        "atenuantes": selected_aten,
        "causas_3fase": causes,
        "pena_definitiva_anos": round(pena_definitiva, 4),
        "pena_definitiva_dias": years_to_days(pena_definitiva)
    }
    st.json(report)

    st.markdown("### Observações importantes")
    st.write("""
    - O app **até tenta extrair** a pena abstrata do texto do Código Penal, mas essa extração é heurística; confirme sempre manualmente.
    - Muitos majorantes/minorantes são **específicos** (ex.: § de artigo da Parte Especial) e trazem frações/intervalos próprios — prefira então inserir o percentual correto na terceira fase.
    - A valoração das circunstâncias judiciais (art. 59) é discricionária e aqui é simulada via slider/pesos; o juiz fundamenta.
    - Esta ferramenta serve como **apoio de cálculo e organização**; não substitui pesquisa doutrinária/jurisprudencial nem decisão judicial.
    """)
