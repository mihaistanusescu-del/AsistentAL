import streamlit as st
from pypdf import PdfReader
import re

st.title("⚡ Verificator Autorizație")

st.write("Încarcă autorizația în format PDF.")

fisier = st.file_uploader("Încarcă PDF", type=["pdf"])

if fisier is not None:
    reader = PdfReader(fisier)

    text = ""

    for pagina in reader.pages:
        continut = pagina.extract_text()
        if continut:
            text += continut + "\n"

    # Caută date de forma 28.08.2026, 28/08/2026 sau 28-08-2026
    date_gasite = re.findall(
        r"\b(?:0?[1-9]|[12][0-9]|3[01])[./-](?:0?[1-9]|1[0-2])[./-](?:19|20)\d{2}\b",
        text
    )

    if date_gasite:
        st.success("✅ DATA A FOST GĂSITĂ")
        st.write("Data/datele identificate:")
        for data in sorted(set(date_gasite)):
            st.write("📅", data)
    else:
        st.error("❌ DATA NU A FOST GĂSITĂ")

    with st.expander("Vezi textul citit din PDF"):
        st.text(text)
