from PyMultiDictionary import MultiDictionary

dictionary = MultiDictionary()
print("Welcome to pocket dictionary app")
query=input("what you want to search in this dictionary : ")
meaning = dictionary.meaning('en', query)
print(meaning)
