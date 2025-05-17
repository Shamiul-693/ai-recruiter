import streamlit as st
from utils import get_reports
from datetime import datetime

def app():
    st.title("📊 Interview Reports")

    if st.button("Fetch Reports"):
        reports_data = get_reports()

        if "error" in reports_data:
            st.error(f"Error fetching reports: {reports_data['error']}")
            return
        
        reports = reports_data.get("data", [])
        if not reports:
            st.info("No reports found.")
            return

        for i, report in enumerate(reports, start=1):
            with st.container():
                st.markdown(f"## {i}. Candidate: {report.get('candidate_name', 'N/A')}  ")
                st.markdown(f"**Email:** {report.get('candidate_email_id', 'N/A')}")
                st.markdown(f"**Interview:** {report.get('interview_name', 'N/A')}")
                report_date = report.get("report_date")
                if report_date:
                    dt = datetime.fromisoformat(report_date)
                    st.markdown(f"**Date:** {dt.strftime('%b %d, %Y %H:%M:%S')}")

                # Metrics side-by-side
                col1, col2, col3 = st.columns(3)
                col1.metric("Proctoring Score", f"{report.get('proctoring_score', 'N/A')}%")
                col2.metric("AI Match Score", report.get("ai_match_score", "N/A"))
                coding_rating = report.get("coding_skills_evaluation", {}).get("rating", "N/A")
                col3.metric("Coding Skill Rating", coding_rating)

                # Links side-by-side
                col1, col2 = st.columns(2)
                report_url = report.get("report_url")
                if report_url:
                    col1.markdown(f"[📄 View Full Report]({report_url})")
                recording_url = report.get("interview_recording_url")
                if recording_url:
                    col2.markdown(f"[🎥 Interview Recording]({recording_url})")

                # Technical Skills
                tech_skills = report.get("technical_skills_evaluation", [])
                if tech_skills:
                    with st.expander("🛠️ Technical Skills Evaluation", expanded=False):
                        for tech in tech_skills:
                            skill = tech.get("skill", "N/A")
                            rating = tech.get("ai_evaluation", {}).get("rating", "N/A")
                            feedback = tech.get("ai_evaluation", {}).get("feedback", "N/A")
                            st.markdown(f"**{skill}** - Rating: *{rating}*")
                            st.write(feedback)
                            st.markdown("---")

                # Soft Skills
                soft_skills = report.get("soft_skills_evaluation", [])
                if soft_skills:
                    with st.expander("🗣️ Soft Skills Evaluation", expanded=False):
                        for soft in soft_skills:
                            skill = soft.get("skill", "N/A")
                            rating = soft.get("ai_evaluation", {}).get("rating", "N/A")
                            feedback = soft.get("ai_evaluation", {}).get("feedback", "N/A")
                            st.markdown(f"**{skill}** - Rating: *{rating}*")
                            st.write(feedback)
                            st.markdown("---")

                # Proctoring Violations
                violations = report.get("proctoring_violations", [])
                if violations:
                    with st.expander("🚨 Proctoring Violations", expanded=False):
                        for violation in violations:
                            desc = violation.get("description", "")
                            val = violation.get("value", "")
                            st.write(f"- {desc} ({val})")

                # Interview Transcript
                transcript = report.get("interview_transcript", [])
                if transcript:
                    with st.expander("📜 Interview Transcript", expanded=False):
                        for entry in transcript:
                            role = entry.get("role", "N/A").capitalize()
                            content = entry.get("content", "")
                            timestamp = entry.get("timestamp", 0)
                            mins, secs = divmod(timestamp, 60)
                            st.markdown(f"**{role} [{int(mins)}:{int(secs):02d}]**")
                            st.write(content)

                st.markdown("---")
