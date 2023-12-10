from flask import Flask, request, render_template
import requests
from apikey import PROXYCURL_API_KEY

app = Flask(__name__)


def fetch_company_search_id(company_url):
    api_endpoint = 'https://nubela.co/proxycurl/api/linkedin/company'
    params = {'url': company_url}
    headers = {'Authorization': 'Bearer ' + PROXYCURL_API_KEY}
    response = requests.get(api_endpoint, params=params, headers=headers)
    if response.status_code == 200:
        return response.json().get('search_id')
    return None


def request_proxycurl_jobs(search_id, keyword):
    url = "https://nubela.co/proxycurl/api/v2/linkedin/company/job"
    headers = {'Authorization': f'Bearer {PROXYCURL_API_KEY}'}
    params = {'search_id': search_id, 'keyword': keyword}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json().get('job', [])
    return []


def process_proxycurl_response(job_list):
    standardized_listings = []
    for item in job_list:
        job = {
            "title": item.get("job_title"),
            "company": item.get("company"),
            "location": item.get("location"),
            "link": item.get("job_url"),
            "list_date": item.get("list_date")
        }
        standardized_listings.append(job)
    return standardized_listings


@app.route('/', methods=['GET', 'POST'])
def job_search():
    if request.method == 'POST':
        company_name = request.form.get(
            'company_name').replace(" ", "-").lower()
        keyword = request.form.get('keyword')

        company_url = f"https://www.linkedin.com/company/{company_name}/"
        search_id = fetch_company_search_id(company_url)

        if search_id:
            job_list = request_proxycurl_jobs(search_id, keyword)
            listings = process_proxycurl_response(job_list)
            return render_template('listings.html', listings=listings)
        else:
            error_message = "Company not found or invalid URL."
            return render_template('upload.html', error=error_message)
    return render_template('upload.html')


if __name__ == '__main__':
    app.run(debug=True)
