import pandas as pd

# Sample data for students
data = {
    'Name': [
        'John Doe', 'Jane Smith', 'Alice Brown', 'Bob Johnson', 
        'Charlie Davis', 'Emily Clark', 'Frank Moore', 'Grace Lee', 
        'Henry White', 'Ivy Wilson', 'Jack Taylor', 'Kelly Brown', 
        'Liam Martin', 'Mia Thompson', 'Noah Scott'
    ],
    'Subjects': [
        'Physics Chemistry Math', 'Biology Chemistry Hindi', 
        'Math Physics Computer Science', 'Hindi Biology Chemistry', 
        'Math Chemistry Physics', 'Biology Math Computer Science', 
        'Physics Computer Science Biology', 'Hindi Chemistry Math', 
        'Computer Science Math Physics', 'Biology Chemistry Physics', 
        'Hindi Math Biology', 'Physics Computer Science Hindi', 
        'Math Chemistry Biology', 'Computer Science Physics Math', 
        'Hindi Biology Chemistry'
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Check the DataFrame structure
print("Columns in DataFrame:", df.columns)
print(df.head())

# Split the 'Subjects' column into lists
df['Subjects'] = df['Subjects'].str.split()

# a) Filter for students with 'Math' in their subjects
students_with_math = df[df['Subjects'].apply(lambda x: 'Math' in x)]
print("\nStudents with Math:")
print(students_with_math)

# b) Find out the students who have Hindi as a subject
students_with_hindi = df[df['Subjects'].apply(lambda x: 'Hindi' in x)]
print("\nStudents with Hindi:")
print(students_with_hindi)

# c) Find out the number of students who have Computer Science as a subject
students_with_cs = df[df['Subjects'].apply(lambda x: 'Computer Science' in x)]
print("\nStudents with Computer Science:")
print(students_with_cs)

# Dates processing
dates = [
    '2012-12-31 08:45', 
    '2019-1-1 12:30', 
    '2008-02-2 10:30',
    '2010-1-1 09:25', 
    '2019-12-31 00:00'
]

# Convert the list of dates into a Pandas DataFrame
dates_df = pd.DataFrame(dates, columns=['Date'])

# Convert the 'Date' column to datetime format
dates_df['Date'] = pd.to_datetime(dates_df['Date'])

# Extract the day names
dates_df['Day'] = dates_df['Date'].dt.day_name()

# Output the days in the specified format
print("\nDays from dates:")
for i, day in enumerate(dates_df['Day'], start=1):
    print(f"Day{i} {day}")
