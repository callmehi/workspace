# 方法1
# import os
# dirPath = r"D:/temp/Test_folder/archive"
# result = [f for f in os.listdir(dirPath) if os.path.isfile(os.path.join(dirPath, f))]
# print(result)

# 方法2
# import os
# dirPath = r"D:/temp/Test_folder/archive"
# result = next(os.walk(dirPath))[1]
# print(result)

# 方法3
import glob
dirPathPattern = r"D:/temp/Test_folder/archive/*"
result = glob.glob(dirPathPattern)
print(result)