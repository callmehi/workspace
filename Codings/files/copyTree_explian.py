# Python program to explain shutil.copytree() method
# importing os module
import os
# importing shutil module
import shutil
from time import time
# path
path = 'D:/temp/Test_folder/archive'
# List files and directories

# in 'D:/temp/Test_folder/archive'

print("Before copying file:")
print(os.listdir(path))

# Source path
src = 'D:/temp/Test_folder/archive/source'

# Destination path
dest = 'D:/temp/Test_try'

# Copy the content of
# source to destination
destination = shutil.copytree(src, dest)

# List files and directories

# in "D:/temp/Test_folder/archive/"
print("After copying file:")
print(os.listdir(path))

# Print path of newly
# created file
print("Destination path:", destination)
