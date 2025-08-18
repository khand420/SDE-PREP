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
        
        # Extract specific information from div elements
        projects = soup.find_all('div', class_='col-lg-6')
        print('-----------------', projects)

# col_lg_6_divs = soup.find_all('div', class_='col-lg-6')        
        # Check if projects are found
        if not projects:
            print("No projects found on the page.")
            return None
        
        for project in projects:
            name_tag = project.find('span', class_='font-lg fw-600')
            name = name_tag.text.strip() if name_tag else 'N/A'

            application_id_tag = project.find('a')
            application_id = application_id_tag.text.strip() if application_id_tag else 'N/A'

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









# import requests
# from bs4 import BeautifulSoup
# from retry import retry
# import warnings

# # Suppress only the InsecureRequestWarning from urllib3
# from requests.packages.urllib3.exceptions import InsecureRequestWarning
# requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# @retry(requests.exceptions.ConnectionError, tries=3, delay=2)
# def fetch_url(url, headers):
#     return requests.get(url, headers=headers, verify=False)

# def extract_information():
#     URL = 'https://hprera.nic.in/PublicDashboard/'
#     # Define headers with a User-Agent
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
#     }
    
#     try:
#         # Get the page content from the URL with retry mechanism
#         response = fetch_url(URL, headers)
        
#         # Parse the HTML content
#         soup = BeautifulSoup(response.text, "html.parser")
        
#         # Print the parsed HTML content (for debugging)
#         # print(soup.prettify())
        
#         # Extract specific information from div elements
#         projects = soup.find_all('div', class_='col-lg-6')
#         for project in projects:
#             name = project.find('span', class_='font-lg fw-600').text.strip()
#             application_id = project.find('a').text.strip()
#             description = project.find_all('span')[2].text.strip()
#             phone = project.find_all('span')[3].text.strip()
#             email = project.find_all('span')[4].text.strip()
#             address = project.find_all('span')[5].text.strip()
#             valid_upto = project.find('span', class_='text-orange ml-1').text.strip()
            
#             print(f"Name: {name}")
#             print(f"Application ID: {application_id}")
#             print(f"Description: {description}")
#             print(f"Phone: {phone}")
#             print(f"Email: {email}")
#             print(f"Address: {address}")
#             print(f"Valid Upto: {valid_upto}")
#             print("\n")
        
#         return response
#     except requests.exceptions.RequestException as e:
#         print(f"Error fetching the URL: {e}")
#         return None

# extract_information()
