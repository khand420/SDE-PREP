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
        
        # Check if projects are found
        if not projects:
            print("No projects found on the page.")
            return None
        
        project_data = []
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

            project_data.append({
                "Name": name,
                "Application ID": application_id,
                "Description": description,
                "Phone": phone,
                "Email": email,
                "Address": address,
                "Valid Upto": valid_upto
            })

        return project_data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return None

project_data = extract_information()
if project_data:
    for project in project_data:
        print(project)



# from bs4 import BeautifulSoup

# html_content = """
# <div class="col-lg-6">
#     <div class="shadow py-3 px-3 font-sm radius-3 mb-2">
#         <div class="">
#             <span class="font-lg fw-600">KAISVILLE COUNTRY HOMES</span><br>
#             <a href="javascript:void(0);" data-qs="f3fIU7vFXK1A7oBz+wkjSvkyuy1IqgT00EZbp3WMSVgpSER8U2dHmU+BdTran0RzkwtPFe8C8EcL6xOjHUmvw2OI4Wp5LyNWq0r2CrvITeUP5rRrwb//A20DISThXIUm" title="View Application" onclick="tab_project_main_ApplicationPreview($(this));">RERAHPKUP01180019</a>
#             <br>
#             <span>Development / Construction (Residential)</span>
#             <div class="mt-1">
#                 <i class="fa fa-mobile-alt font-xxs fa-fw text-muted"></i> : <span class="ml-1">9811285650</span><br>
#                 <i class="fa fa-at font-xxs fa-fw text-muted"></i> : <span class="ml-1">pradeepmalik101@yahoo.com</span><br>
#                 <i class="fa fa-map-marker-alt font-xxs fa-fw text-muted"></i> : <span class="ml-1">Vill. Kais Kullu (175101)</span>
#             </div>
#             <div class="text-right font-xxs">
#                 Valid Upto : <span class="text-orange ml-1">23/01/2029</span>
#             </div>
#         </div>
#     </div>
# </div>
# """

# soup = BeautifulSoup(html_content, 'html.parser')

# # Find all the div elements with the class 'col-lg-6'
# col_lg_6_divs = soup.find_all('div', class_='col-lg-6')

# # Extract the data from each 'col-lg-6' div
# for col_lg_6_div in col_lg_6_divs:
#     project_name = col_lg_6_div.find('span', class_='font-lg fw-600').text.strip() if col_lg_6_div.find('span', class_='font-lg fw-600') else 'N/A'
#     application_id = col_lg_6_div.find('a').text.strip() if col_lg_6_div.find('a') else 'N/A'
#     project_type = col_lg_6_div.find('span', text='Development / Construction (Residential)').text.strip() if col_lg_6_div.find('span', text='Development / Construction (Residential)') else 'N/A'
    
#     phone_tag = col_lg_6_div.find('i', class_='fa fa-mobile-alt font-xxs fa-fw text-muted')
#     phone = phone_tag.find_next_sibling('span').text.strip() if phone_tag else 'N/A'

#     email_tag = col_lg_6_div.find('i', class_='fa fa-at font-xxs fa-fw text-muted')
#     email = email_tag.find_next_sibling('span').text.strip() if email_tag else 'N/A'

#     address_tag = col_lg_6_div.find('i', class_='fa fa-map-marker-alt font-xxs fa-fw text-muted')
#     address = address_tag.find_next_sibling('span').text.strip() if address_tag else 'N/A'

#     valid_upto_tag = col_lg_6_div.find('span', class_='text-orange ml-1')
#     valid_upto = valid_upto_tag.text.strip() if valid_upto_tag else 'N/A'

#     print(f"Name: {project_name}")
#     print(f"Application ID: {application_id}")
#     print(f"Description: {project_type}")
#     print(f"Phone: {phone}")
#     print(f"Email: {email}")
#     print(f"Address: {address}")
#     print(f"Valid Upto: {valid_upto}")
#     print()





# from bs4 import BeautifulSoup

# html_content = """
# <div class="col-lg-6">
#     <div class="shadow py-3 px-3 font-sm radius-3 mb-2">
#         <div class="">
#             <span class="font-lg fw-600">KAISVILLE COUNTRY HOMES</span><br>
#             <a href="javascript:void(0);" data-qs="f3fIU7vFXK1A7oBz+wkjSvkyuy1IqgT00EZbp3WMSVgpSER8U2dHmU+BdTran0RzkwtPFe8C8EcL6xOjHUmvw2OI4Wp5LyNWq0r2CrvITeUP5rRrwb//A20DISThXIUm" title="View Application" onclick="tab_project_main_ApplicationPreview($(this));">RERAHPKUP01180019</a>
#             <br>
#             <span>Development / Construction (Residential)</span>
#             <div class="mt-1">
#                 <i class="fa fa-mobile-alt font-xxs fa-fw text-muted"></i> : <span class="ml-1">9811285650</span><br>
#                 <i class="fa fa-at font-xxs fa-fw text-muted"></i> : <span class="ml-1">pradeepmalik101@yahoo.com</span><br>
#                 <i class="fa fa-map-marker-alt font-xxs fa-fw text-muted"></i> : <span class="ml-1">Vill. Kais Kullu (175101)</span>
#             </div>
#             <div class="text-right font-xxs">
#                 Valid Upto : <span class="text-orange ml-1">23/01/2029</span>
#             </div>
#         </div>
#     </div>
# </div>
# """

# soup = BeautifulSoup(html_content, 'html.parser')

# # Find all the div elements with the class 'col-lg-6'
# col_lg_6_divs = soup.find_all('div', class_='col-lg-6')

# # Extract the data from each 'col-lg-6' div
# for col_lg_6_div in col_lg_6_divs:
#     project_name = col_lg_6_div.find('span', class_='font-lg fw-600').text.strip()
#     application_id = col_lg_6_div.find('a').text.strip()
#     project_type = col_lg_6_div.find('span', text='Development / Construction (Residential)').text.strip()
#     phone = col_lg_6_div.find('span', text=lambda t: 'fa-mobile-alt' in t).text.strip()
#     email = col_lg_6_div.find('span', text=lambda t: 'fa-at' in t).text.strip()
#     address = col_lg_6_div.find('span', text=lambda t: 'fa-map-marker-alt' in t).text.strip()
#     valid_upto = col_lg_6_div.find('span', class_='text-orange').text.strip()

#     print(f"Name: {project_name}")
#     print(f"Application ID: {application_id}")
#     print(f"Description: {project_type}")
#     print(f"Phone: {phone}")
#     print(f"Email: {email}")
#     print(f"Address: {address}")
#     print(f"Valid Upto: {valid_upto}")
#     print()
