import requests

API_KEY = "228bf5c8f011845bba52dd0f4907cd5e4c7fb2fa15f09d988e5066a02105499c8231fad389adca13c2eb4a17a179a42cca52a51ca69d4a1b77669d00f1da5b63"
BASE_URL = "https://public.api.micro1.ai"

HEADERS = {
    "Content-Type": "application/json",
    "x-api-key": API_KEY
}

def create_interview(payload):
    url = f"{BASE_URL}/interview"
    try:
        response = requests.post(url, json=payload, headers=HEADERS)
        data = response.json()
        if response.status_code == 200 and data.get("status", False):
            return data
        else:
            error_message = data.get("message", "Unknown error occurred")
            return {"error": error_message}
    except Exception as e:
        return {"error": str(e)}

def invite_candidate(interview_id, name, email):
    url = f"{BASE_URL}/interview/invite"
    data = {
        "interview_id": interview_id,
        "candidate_name": name,
        "candidate_email": email
    }
    try:
        response = requests.post(url, json=data, headers=HEADERS)
        resp_data = response.json()
        if response.status_code == 200 and resp_data.get("status", False):
            return resp_data
        else:
            error_message = resp_data.get("message", "Unknown error occurred")
            return {"error": error_message}
    except Exception as e:
        return {"error": str(e)}

def get_reports():
    url = f"{BASE_URL}/interview/reports"
    try:
        response = requests.get(url, headers=HEADERS)
        data = response.json()
        if response.status_code == 200 and data.get("status", False):
            return data
        else:
            error_message = data.get("message", "Unknown error occurred")
            return {"error": error_message}
    except Exception as e:
        return {"error": str(e)}

