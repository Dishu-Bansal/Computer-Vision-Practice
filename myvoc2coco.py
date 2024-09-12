import os

# Define the directory containing the files
directory_path = 'FaceMask/annotations'

# Define the path for the output text file
output_file_path = 'FaceMask/xmllist.txt'

# Get a list of all files and directories in the specified directory
file_names = os.listdir(directory_path)

# Filter out directories, only keep files
file_names = [f for f in file_names if os.path.isfile(os.path.join(directory_path, f))]

# Write the file names to the text file
with open(output_file_path, 'w') as file:
    for name in file_names:
        file.write(name + '\n')

print(f"File names have been written to {output_file_path}")
