import requests

API_KEY = "5f165b29614698c16d6efd5dc0bf7f23ac1f98c4c30865b8ed11efab486682029f6f5357bfa463acde32eee54f98615659ff83a98848cc49b0726d80dc0cb135"
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

