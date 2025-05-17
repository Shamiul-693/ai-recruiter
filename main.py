import streamlit as st
from utils import create_interview, invite_candidate

st.title("🧠 AI Recruiter")

st.header("📋 Create Interview")
interview_name = st.text_input("Interview Name")
skill = st.text_input("Skill Name")
desc = st.text_input("Skill Description")
coding_language = st.selectbox("Coding Language", ["python", "javascript", "java"])

if st.button("Create Interview"):
    if not (interview_name and skill and desc):
        st.error("Please fill in all the fields!")
    else:
        payload = {
            "interview_name": interview_name,
            "skills": [{"name": skill, "description": desc}],
            "interview_language": "en",
            "is_coding_round_required": True,
            "selected_coding_language": coding_language,
            "is_proctoring_required": True
        }
        result = create_interview(payload)
        
        if "error" in result:
            st.error(f"Error creating interview: {result['error']}")
        else:
            st.success(f"Interview created successfully! Interview ID: {result.get('interview_id')}")
            st.json(result)

st.header("✉️ Invite Candidate")
interview_id = st.text_input("Interview ID")
candidate_name = st.text_input("Candidate Name")
candidate_email = st.text_input("Candidate Email")

if st.button("Send Invite"):
    if not (interview_id and candidate_name and candidate_email):
        st.error("Please fill in all the invite fields!")
    else:
        invite_result = invite_candidate(interview_id, candidate_name, candidate_email)
        if "error" in invite_result:
            st.error(f"Error sending invite: {invite_result['error']}")
        else:
            st.success(f"Invitation sent to {candidate_email}")
            st.json(invite_result)
