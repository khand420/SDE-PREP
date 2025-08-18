# data  = {'Id': ['00Q5g00000Rs0lYEAR', '00Q5g00000Rs0lZEAR', '00Q5g00000Rs0lbEAB', '00Q5g00000Rs0lcEAB', '00Q5g00000Rs0ldEAB'],
#   'Name': ['Bertha Boxer', 'Phyllis Cotton', 'Mike Braund', 'Patricia Feager', 'Brenda Mcclure'],
#     'Title': ['Director of Vendor Relations', 'CFO', 'VP, Technology', 'CEO', 'CFO'],
#       'State': ['FL', 'VA', 'MD', 'NC', 'IL'],
#         'Phone': ['(850) 644-4200', '(703) 757-1000', '(410) 381-2334', '(336) 777-1970', '(847) 262-5000'],
#         'Status': ['Working - Contacted', 'Open - Not Contacted', 'Open - Not Contacted', 'Working - Contacted', 'Working - Contacted']} 

# import pandas as pd


# df = pd.DataFrame(data)
# print(df[df['Title'] == 'CEO'])





# Your have SQL query and you need to use this query as input to the python function and
#  return only column names present in the string as a python list, Write program in python. 
# Example Input 
# SELECT Id, Name, Title, Email, State FROM Lead Where State = 'CT' 
  
# Example output: 
# [‘Id’, ‘Name’, ‘Title’, ‘Email’, ‘State’] 


# lst = [Id, Name, Title, Email, State]
# import regex as re
def findColumn(input):


    data = input.split(' ')
    s = data.index('SELECT')
    e = data.index('FROM')
    data = data[s+1:e].split(',')
    
     
     
    print(data)
# input = 'SELECT Id, Name, Title, Email, State FROM Lead Where State = CT' 
input = 'SELECT * FROM Lead Where State = CT' 

print(findColumn(input))





def extract_column_names(sql_query):
    # Split the query into parts
    parts = sql_query.split("FROM")[0]  # Get the part before 'FROM'
    columns = parts.replace("SELECT", "").strip()  # Remove 'SELECT' and strip whitespace
    column_names = [col.strip() for col in columns.split(",")]  # Split by comma and strip spaces
    return column_names

# Example Input
sql_query = "SELECT Id, Name, Title, Email, State FROM Lead Where State = 'CT'"

# Example Output
output = extract_column_names(sql_query)
print(output)  # Output: ['Id', 'Name', 'Title', 'Email', 'State']

