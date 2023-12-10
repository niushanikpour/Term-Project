# Job Search Tool made by Niusha Nikpour

## Table of Content
- [Job Search Tool made by Niusha Nikpour](#job-search-tool-made-by-niusha-nikpour)
  - [Table of Content](#table-of-content)
    - [Disclaimer](#disclaimer)
    - [Introduction](#introduction)
    - [Installation](#installation)
    - [Usage](#usage)
    - [Implementation Information](#implementation-information)
    - [Results](#results)
    - [Project Evolution/Narrative](#project-evolutionnarrative)
    - [Attribution](#attribution)

### Disclaimer 

My first file, named `draft_app.py`, was an attempt at my original proposal: to have users input their resume into the webpage, which would then return applicable job listings. Unfortunately, despite extensive research and testing, I couldn't make it fully functional. The APIs I explored were not user-friendly and quite expensive. I included this file to demonstrate my thought process. In this version, I successfully implemented NLP, but the job listing functionality didn't work as intended.

Instead, I created a new file named `final_app.py`, which showcases a working version of my software. This file will focus on my final product.

### Introduction

I developed a tool that allows users to look up any company name and a keyword, returning a refined list of job listings with links to LinkedIn applications. This tool simplifies the job search by directly finding relevant opportunities from company profiles on LinkedIn, tailored to specific interests and preferences. As a senior at Babson, constantly applying to jobs, I thought building this tool would be practical and enjoyable for both me and other students. I wanted to create something connected to a topic I'm genuinely passionate about and improve my skills with APIs and Flask.

### Installation
You will need:
- Python 3.x
- Flask
- Requests library

### Usage
- Enter a company name in the first text box.
- Enter a keyword (such as 'engineer', 'analyst', 'software', etc.) that you would like to see in job titles.

### Implementation Information
The code creates a web application that lets users search for jobs by company name and keyword. It uses Flask, a Python framework, for handling web requests. When a user submits a company name and keyword, the `fetch_company_search_id` function generates a URL for LinkedIn's company profile and retrieves its unique search ID using the Proxycurl API. The `request_proxycurl_jobs` function then uses this ID to fetch job listings matching the keyword. The retrieved jobs are formatted in the `process_proxycurl_response` function, creating a user-friendly list of job opportunities displayed on the webpage.

### Results
1. Base Look of Form Before Submitting:
![Step 1](<Screenshot (133).png>)
When you first access the Flask application, you're presented with a simple form. This is the initial state of your web page, where users can enter their inputs.
The form likely includes two text fields: one for the company name and another for a keyword related to the job they're searching for.

2. Typing in the Company Name and Keyword:
 ![Step 2](<Screenshot (135).png>)
In this step, users type in the name of the company they're interested in and a keyword that represents the type of job they're looking for.
For example, a user might enter "Google" as the company and "engineer" as the keyword.

3. Result of Job Listings:
![Step 3](<Screenshot (137).png>)
After submitting the form, the Flask application processes the request. It fetches job listings from LinkedIn that match the entered company name and keyword.
The user is then presented with a list of job listings. Each listing typically includes the job title, company name, location, date of the listing, and a link to the job posting on LinkedIn.

4. Clicking the Link of One of the Job Listings:
![Step 4](<Screenshot (138).png>)
Users can click on a job title in the list, which redirects them to the actual job posting on LinkedIn.
This step allows users to view detailed information about the job and apply for it directly on LinkedIn.

### Project Evolution/Narrative

Like I mentioned in my disclaimer, my original idea was different from my final outcome. My code went through many changes because of this. I spent a majority of my time researching the different APIs offered (free and paid).

Initially, the goal was to develop a tool that could analyze resumes and match them with job listings. This required extensive exploration of various APIs for job listings and natural language processing (NLP) libraries. I experimented with different methods for extracting relevant data from resumes and matching them to job descriptions. However, this proved to be a complex challenge, particularly in accurately parsing and interpreting the diverse formats and content of resumes.

Throughout this process, I encountered limitations with the available APIs, both in terms of functionality and cost. While I managed to implement NLP successfully, integrating it effectively with the job listing function was a significant hurdle. I realized that achieving the level of accuracy and functionality I envisioned was beyond the scope of the available resources and the project timeline.

Consequently, I pivoted my approach to focus on a more achievable goal: creating a tool that allows users to search for jobs based on company names and keywords. This shift required adapting the existing codebase to a new purpose, refining the user interface, and ensuring seamless integration with the Proxycurl API for fetching LinkedIn job listings.

The final product, while different from my initial vision, is a testament to the iterative nature of software development. It reflects the adaptability and problem-solving skills required in this field, as well as my personal growth as a developer. Despite the challenges, the project has been a rewarding journey that has enhanced my technical skills and understanding of the complexities of software development.

### Attribution
- https://github.com/nubelaco/linkedin-api-python3-examples/tree/master
- https://dev.to/heymich/scraping-linkedin-data-with-proxycurl-jobs-api-2jgb#fetching-listed-jobs
- https://nubela.co/blog/ultimate-guide-to-linkedin-api_people-profile-api_with-python-examples/
- https://nubela.co/proxycurl/linkedin
- https://nubela.co/proxycurl/docs#jobs-api-job-search-endpoint
- https://developers.greenhouse.io/job-board.html#retrieve-a-job



  
