from flask import Flask, request, render_template
import requests
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk import pos_tag
import string
from apikey import CS_API_KEY, PROXYCURL_API_KEY

app = Flask(__name__)


def preprocess_text(text):
    stopwords_ = set(stopwords.words('english'))
    words = word_tokenize(text.lower())
    processed_text = [
        w for w in words if w not in string.punctuation and w not in stopwords_ and len(w) > 1]
    return processed_text


def extract_skills(resume_text):
    processed_text = preprocess_text(resume_text)
    pos_tags = pos_tag(processed_text)
    potential_skills = [word for word,
                        tag in pos_tags if tag in ["NN", "NNS", "NNP", "NNPS"]]
    return potential_skills


def process_coresignal_response(response_json):
    standardized_listings = []
    if isinstance(response_json, list):
        for item in response_json:
            if isinstance(item, dict):
                job = {
                    "title": item.get("title", "No title provided"),
                    "description": item.get("description", "No description provided"),
                    "company": item.get("company_name", "No company name provided"),
                    "location": item.get("location", "No location provided"),
                    "link": item.get("url", "No URL provided")
                }
                standardized_listings.append(job)
    return standardized_listings


def get_profile(profile_id):
    api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
    header_dic = {'Authorization': 'Bearer ' + PROXYCURL_API_KEY}
    params = {
        'url': f'https://www.linkedin.com/in/{profile_id}',
    }
    response = requests.get(api_endpoint,
                            params=params,
                            headers=header_dic)
    return response.json()


def proxy(PROXYCURL_API_KEY):
    # This sample was taken from the Nubela guide of how to use this API
    headers = {'Authorization': 'Bearer ' + PROXYCURL_API_KEY}
    api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin/company/job'
    params = {
        'job_type': 'anything',
        'experience_level': 'entry_level',
        'when': 'past-month',
        'flexibility': 'remote',
        'geo_id': '92000000',
        'keyword': 'software engineer',
        'search_id': '1035',
    }
    response = requests.get(api_endpoint, params=params, headers=headers)
    return response.json()


def process_proxycurl_response(response_json):
    standardized_listings = []
    for item in response_json:
        job = {
            "title": item.get("title"),
            "description": item.get("description"),
            "company": item.get("company"),
            "location": item.get("location"),
            "link": item.get("link")
        }
        standardized_listings.append(job)
    return standardized_listings


def process_greenhouse_response(response_json):
    standardized_listings = []
    for item in response_json['jobs']:
        job = {
            "title": item.get("title"),
            "description": item.get("content"),
            "company": "Your Company Name",
            "location": item.get("location"),
            "link": item.get("absolute_url")
        }
        standardized_listings.append(job)
    return standardized_listings


def get_job_listings(skills):
    job_listings = []
    for skill in skills:

        coresignal_url = "https://api.coresignal.com/cdapi/v1/linkedin/job/search/filter"
        headers = {
            'Authorization': f'Bearer {CS_API_KEY}',
            'Content-Type': 'application/json',
            'accept': 'application/json'
        }
        payload = {"title": skill}
        response = requests.post(coresignal_url, headers=headers, json=payload)
        if response.status_code == 200:
            job_listings.extend(process_coresignal_response(response.json()))

        proxycurl_url = "https://nubela.co/proxycurl/api/v2/linkedin/company/job"
        headers = {'Authorization': f'Bearer {PROXYCURL_API_KEY}',
                   'Content-Type': 'application/json'}
        payload = {"skill": skill}
        response = requests.post(proxycurl_url, headers=headers, json=payload)
        if response.status_code == 200:
            job_listings.extend(process_proxycurl_response(response.json()))

        greenhouse_url = "https://boards-api.greenhouse.io/v1/jobs"
        try:
            gh_response = requests.get(greenhouse_url)
            if gh_response.status_code == 200:
                job_listings.extend(
                    process_greenhouse_response(gh_response.json()))
        except requests.RequestException as e:
            print(f"Greenhouse API error: {e}")

    return job_listings


@app.route('/', methods=['GET', 'POST'])
def skill_input():
    if request.method == 'POST':
        resume_text = request.form.get('resume_text')
        extracted_skills = extract_skills(resume_text)
        listings = get_job_listings(extracted_skills)
        return render_template('listings.html', listings=listings, skills=extracted_skills)

    return render_template('upload.html')


if __name__ == '__main__':
    app.run(debug=True)
