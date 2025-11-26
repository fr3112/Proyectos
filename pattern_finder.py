#Search for substrings or sublists using slicing + sequence operators.
print("\n*****Patter finder: Give a text or list of items and the pattern you are looking for within the text or list. And this program will find the pattern and tell you where it is.*****\n")

data = input("Place your text or list of things here (if it's a list, separate the items with \',\'): ")

if ',' in data:
    data = data.split(',')

pattern = input("\nInsert the pattern you want to find (if it's a list, separate the items with \',\'): ")

if ',' in pattern:
    pattern = pattern.split(',')

leng_p = len(pattern)

for i in range(len(data) - (leng_p-1)):
    if data[i:i+leng_p] == pattern:
        print("The pattern is in the index", i)