import os

def rename_files_in_directory(directory):
    # List all files in the directory
    for filename in os.listdir(directory):
        # Construct the full file path
        old_file_path = os.path.join(directory, filename)
        
        # Check if it's a file (not a directory)
        if os.path.isfile(old_file_path):
            # Construct the new file name with the prefix
            new_filename = f"renamed_{filename}"
            new_file_path = os.path.join(directory, new_filename)
            
            # Rename the file
            os.rename(old_file_path, new_file_path)
            print(f"Renamed '{filename}' to '{new_filename}'")

# Specify the directory path
directory_path = 'path/to/your/directory'

# Call the function to rename files
rename_files_in_directory(directory_path)
