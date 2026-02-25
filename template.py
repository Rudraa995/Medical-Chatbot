import os

# List of directories to create
directories = [
    "src",
    "research"
]

# List of files to create
files = [
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "setup.py",
    "app.py",
    "research/trials.ipynb",
    "requirements.txt"
]

# Create directories
for directory in directories:
    os.makedirs(directory, exist_ok=True)

# Create files
for file in files:
    # Create directory if not exists
    dir_name = os.path.dirname(file)
    if dir_name:
        os.makedirs(dir_name, exist_ok=True)

    # Create empty file
    with open(file, "w") as f:
        pass

print("Directory and files created successfully!")