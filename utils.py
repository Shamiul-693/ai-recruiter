import requests

API_KEY = "228bf5c8f011845bba52dd0f4907cd5e4c7fb2fa15f09d988e5066a02105499c8231fad389adca13c2eb4a17a179a42cca52a51ca69d4a1b77669d00f1da5b63"
BASE_URL = "https://public.api.micro1.ai"

HEADERS = {
    "Content-Type": "application/json",
    "x-api-key": API_KEY
}

def create_interview(payload):
    url = f"{BASE_URL}/interview"
    response = requests.post(url, json=payload, headers=HEADERS)
    return response.json()

def invite_candidate(interview_id, name, email):
    url = f"{BASE_URL}/interview/invite"
    data = {
        "interview_id": interview_id,
        "candidate_name": name,
        "candidate_email": email
    }
    response = requests.post(url, json=data, headers=HEADERS)
    return response.json()

def get_reports():
    url = f"{BASE_URL}/interview/reports"
    response = requests.get(url, headers=HEADERS)
    return response.json()

