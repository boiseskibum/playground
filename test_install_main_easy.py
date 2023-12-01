import os, sys

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    if hasattr(sys, '_MEIPASS'):
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")

    full_path = os.path.join(base_path, relative_path)
    print(f'Full path: {full_path}')
    return full_path

# Now use the function to get the path of your resource
icon_path = resource_path("resources/img/jt.ico")
if not os.path.exists(image_path):
    print(f'    DID NOT find calculated path: {icon_path}')
else:
    print(f'    FOUND calculated path: {icon_path}')
