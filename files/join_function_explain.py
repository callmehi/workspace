import os 


# Python Ops join(os.path.join) 取得資料夾絕對路徑
# 如何透過os.path.join取得資料夾絕對路徑呢？可以用在哪裡？
# 當你學會方法後，要是在別人的電腦或是server只要對方提供一個根目錄，後面就不需要跟改了！可以參考下面的作法。
# PS:如果你是想指定資料夾裡面的所有檔案，記得後面要搭配 “”
print("//////////////////////////////////////////////////////")
print("//////////////////////////////////////////////////////")

print("Python Ops join(os.path.join) 取得資料夾絕對路徑//////////////////////////////////////////////////////")

path = "/Users/mark"
print(os.path.join(path, "Desktop", "TEST_Folder", "")) # /Users/mark/Desktop/TEST_Folder/
print(os.path.join(path, "Desktop", "TEST_Folder"))     # /Users/mark/Desktop/TEST_Folder

print("Python join() method dict(字典)//////////////////////////////////////////////////////")

# Python join() method dict(字典)
# 透過join()搭配dict，dict是一個字典也就是必須要有一個key對應一個value，才能是字典，但是我們透過join()來取得新的字串，只能用key值。
test_dict = {'A':1, 'B':2, 'C':3}
print(''.join(test_dict))  # ABC
print(':'.join(test_dict)) # A:B:C
print('*'.join(test_dict)) # A*B*C

print("Python join() method tuple(元組)//////////////////////////////////////////////////////")

# Python join() method tuple(元組)
# 元組可以透過join()重新取得新的字串。
test_tuple = ('A','B','C')
print(''.join(test_tuple))  # ABC
print(':'.join(test_tuple)) # A:B:C
print('$'.join(test_tuple)) # A$B$C

print("Python join() method str(字串)//////////////////////////////////////////////////////")

# Python join() method str(字串)
# 字串當然也是可以轉成新的字串，主要是透過連接字符來串接起來。
test_str = 'ABC'
print(''.join(test_str))    # ABC
print(':'.join(test_str))   # A:B:C
print('! '.join(test_str))  # A! B! C

print("Python join() method list(串列) //////////////////////////////////////////////////////")

# Python join() method list(串列)
# join() list 是非常常用的功能，不論在寫爬蟲、自動化測試、數據分析、AI我都覺得滿重要的！
# 主要可以幫你轉成 str，在看你要用在哪些地方，實用性高！
test_list = ['A', 'B', 'C']
print('-'.join(test_list)) # A-B-C
print('#'.join(test_list)) # A#B#C
print(' '.join(test_list)) # A B C

print("//////////////////////////////////////////////////////")
print("//////////////////////////////////////////////////////")
print("//////////////////////////////////////////////////////")