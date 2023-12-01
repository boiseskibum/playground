# Main program
import os, sys
#from PyQt6.QtGui import QImage, QPixmap

######################################################################
# debuggging and logging
from share import jt_util as util

# logging configuration - the default level if not set is DEBUG
log = util.jt_logging()


log.msg(f'INFO - Valid logging levels are: {util.logging_levels}')
log.set_logging_level("WARNING")  # this will show errors but not files actually processed

log.msg(f'ending, thats all folks!\n')

image_path = 'jt.ico'
my_resources = 'resources/img/'

print(f'Old school way to deal with these')
if not os.path.exists(image_path):
    image_path = my_resources + image_path
    if not os.path.exists(image_path):
        print(f'   Could not find image_path for: {image_path}')
    else:
        print(f'   found image path: {image_path}')
#        image = QImage(image_path)

else:
    log.msg(f'found image path: {image_path}')
#    image = QImage(image_path)

#####################
print(f'\nCalculating basepath stuff')
def resource_path(relative_path):

    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    print(f'base_path: {base_path}, relative_path: {relative_path}')
    return os.path.join(base_path, relative_path)


    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

# Now use the function to get the path of your resource
icon_path = resource_path("resources/img/jt.ico")
if not os.path.exists(icon_path):
    print(f'    DID NOT find calculated path: {icon_path}')
else:
    print(f'    FOUND calculated path: {icon_path}')

