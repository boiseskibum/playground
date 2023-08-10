import os

cwd = os.getcwd()
target_dir = 'pycharm code'
while not os.path.isdir(target_dir):
    target_dir = '../' + target_dir
    print(f"   temp: {target_dir}")

target_dir = os.path.abspath(os.path.join(target_dir, 'scratch_files'))
print (target_dir)