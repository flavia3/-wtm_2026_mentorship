# 6. Remove Duplicate Values
numbers = [1, 2, 3, 4, 2, 5, 3, 6, 1]
converted_numbers = list(set(numbers))

print(f"The list has been converted to a set: {converted_numbers}")

# A set stores unique values only. When the list is converted into a set, duplicate values are automatically removed. Therefore, the repeated numbers 1, 2, and 3 appear only once in the resulting set.


# 7. Unique Programming Languages 
languages = ["Python", "Java", "Python", "C++", "JavaScript", "Python"]
unique_languages = set(languages)
print(f"The unique languages are: {unique_languages}")

unique_languages.add("Django")
print(f"After adding a new language, the unique languages are: {unique_languages}")