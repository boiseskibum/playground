import subprocess
import re

def get_webcam_info():
    # Use system profiler to get webcam information
    command = 'system_profiler SPUSBDataType'
    output = subprocess.check_output(command, shell=True).decode('utf-8')

    # Extract webcam make and model information using regular expressions
    pattern = r'(?<=Camera Manufacturer:\s)(.*)(?=\n)'
    make = re.search(pattern, output)
    if make:
        make = make.group(0).strip()

    pattern = r'(?<=Camera Model:\s)(.*)(?=\n)'
    model = re.search(pattern, output)
    if model:
        model = model.group(0).strip()

    return make, model

# Get webcam information
webcam_make, webcam_model = get_webcam_info()

# Print webcam make and model
print("Webcam Make:", webcam_make)
print("Webcam Model:", webcam_model)
