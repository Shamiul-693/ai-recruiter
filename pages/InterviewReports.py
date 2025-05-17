import streamlit as st
from utils import get_reports

st.title("📊 Interview Reports")

if st.button("Fetch Reports"):
    reports = get_reports()
    for report in reports.get("data", []):
        st.subheader(report.get("candidate_name", "Unnamed"))
        st.write(f"Email: {report.get('candidate_email')}")
        st.json(report)
