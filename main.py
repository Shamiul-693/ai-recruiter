import streamlit as st
from utils import create_interview, invite_candidate

st.title("🧠 AI Recruiter")

st.header("📋 Create Interview")
interview_name = st.text_input("Interview Name")
skill = st.text_input("Skill Name")
desc = st.text_input("Skill Description")
coding_language = st.selectbox("Coding Language", ["python", "javascript", "java"])
if st.button("Create Interview"):
    payload = {
        "interview_name": interview_name,
        "skills": [{"name": skill, "description": desc}],
        "interview_language": "en",
        "is_coding_round_required": True,
        "selected_coding_language": coding_language,
        "is_proctoring_required": True
    }
    result = create_interview(payload)
    st.success(f"Interview created: {result.get('interview_id')}")

st.header("✉️ Invite Candidate")
interview_id = st.text_input("Interview ID")
candidate_name = st.text_input("Candidate Name")
candidate_email = st.text_input("Candidate Email")

if st.button("Send Invite"):
    invite_result = invite_candidate(interview_id, candidate_name, candidate_email)
    st.success(f"Invitation sent to {candidate_email}")
