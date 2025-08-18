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
        
        # Check the response status code
        if response.status_code != 200:
            print(f"Error fetching the URL: {response.status_code} - {response.text}")
            return None
        
        # Parse the HTML content
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Extract specific information from div elements
        projects = soup.find_all('div', class_='col-lg-6 mb-4')
        
        # Check if projects are found
        if not projects:
            print("No projects found on the page.")
            return None
        
        print(f"Found {len(projects)} projects on the page.")
        
        for project in projects:
            name_tag = project.find('span', class_='font-lg fw-600')
            name = name_tag.text.strip() if name_tag else 'N/A'

            application_id_tag = project.find('a', class_='btn btn-primary btn-sm')
            if application_id_tag:
                application_id = application_id_tag['href'].split('=')[-1]
            else:
                application_id = 'N/A'

            description_tag = project.find('span', string='Development / Construction (Residential)')
            description = description_tag.text.strip() if description_tag else 'N/A'

            phone_tag = project.find('i', class_='fa fa-mobile-alt font-xxs fa-fw text-muted')
            phone = phone_tag.find_next_sibling('span').text.strip() if phone_tag else 'N/A'

            email_tag = project.find('i', class_='fa fa-at font-xxs fa-fw text-muted')
            email = email_tag.find_next_sibling('span').text.strip() if email_tag else 'N/A'

            address_tag = project.find('i', class_='fa fa-map-marker-alt font-xxs fa-fw text-muted')
            address = address_tag.find_next_sibling('span').text.strip() if address_tag else 'N/A'

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



# # Function to extract project details
# def extract_project_details(html):
#     projects = []
#     project_divs = html.split('<div class="col-lg-6">')
#     for project_div in project_divs[1:]:
#         project = {}
#         project['name'] = re.search(r'<span class="font-lg fw-600">(.*?)</span>', project_div).group(1)
#         project['id'] = re.search(r'<a href="javascript:void\(0\);" data-qs="(.*?)"', project_div).group(1)
#         project['type'] = re.search(r'<span>(.*?)</span>', project_div).group(1)
#         project['phone'] = re.search(r'<span class="ml-1">(.*?)</span>', project_div, re.DOTALL).group(1)
#         project['email'] = re.search(r'<span class="ml-1">(.*?)</span>', project_div, re.DOTALL).group(1)
#         project['address'] = re.search(r'<span class="ml-1">(.*?)</span>', project_div, re.DOTALL).group(1)
#         project['valid_upto'] = re.search(r'<span class="text-orange ml-1">\s*(.*?)\s*</span>', project_div).group(1)
#         projects.append(project)
#     return projects

# # Extract project details
# projects = extract_project_details(html_content)

# # Print the extracted project details
# for project in projects:
#     print("Project Name:", project['name'])
#     print("Project ID:", project['id'])
#     print("Project Type:", project['type'])
#     print("Phone:", project['phone'])
#     print("Email:", project['email'])
#     print("Address:", project['address'])
#     print("Valid Upto:", project['valid_upto'])
#     print()
