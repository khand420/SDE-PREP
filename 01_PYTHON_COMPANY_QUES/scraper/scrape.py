import requests
from bs4 import BeautifulSoup
from retry import retry
import warnings

# Suppress only the InsecureRequestWarning from urllib3
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

@retry(requests.exceptions.ConnectionError, tries=3, delay=2)
def fetch_url(url, headers):
    return requests.get(url, headers=headers, verify=False)

def extract_information():
    URL = 'https://hprera.nic.in/PublicDashboard/'
    # Define headers with a User-Agent
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    
    try:
        # Get the page content from the URL with retry mechanism
        response = fetch_url(URL, headers)
        
        # Parse the HTML content
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Uncomment to print the prettified HTML (for debugging)
        # print(soup.prettify())
        
        # Extract specific information from div elements
        projects = soup.find_all('div', class_='col-lg-6')
        
        # Check if projects are found
        if not projects:
            print("No projects found on the page.")
            return None
        
        for project in projects:
            name_tag = project.find('span', class_='font-lg fw-600')
            name = name_tag.text.strip() if name_tag else 'N/A'

            application_id_tag = project.find('a')
            application_id = application_id_tag.text.strip() if application_id_tag else 'N/A'

            shadow_div = project.find('div', class_='shadow py-3 px-3 font-sm radius-3 mb-2')
            if shadow_div:
                span_tags = shadow_div.find_all('span')
                description = span_tags[1].text.strip() if len(span_tags) > 1 else 'N/A'
                phone = span_tags[2].text.strip() if len(span_tags) > 2 else 'N/A'
                email = span_tags[3].text.strip() if len(span_tags) > 3 else 'N/A'
                address = span_tags[4].text.strip() if len(span_tags) > 4 else 'N/A'
            else:
                description = 'N/A'
                phone = 'N/A'
                email = 'N/A'
                address = 'N/A'

            valid_upto_tag = project.find('span', class_='text-orange ml-1')
            valid_upto = valid_upto_tag.text.strip() if valid_upto_tag else 'N/A'

            print(f"Name: {name}")
            print(f"Application ID: {application_id}")
            print(f"Description: {description}")
            print(f"Phone: {phone}")
            print(f"Email: {email}")
            print(f"Address: {address}")
            print(f"Valid Upto: {valid_upto}")
            print("\n")
        
        return response
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return None

extract_information()
