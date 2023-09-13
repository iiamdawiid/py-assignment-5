# Exercise 1 
words = ['this' , 'is', 'a', 'sentence', '.']

def reverse_strings(string_list):
    string_list.reverse()
    for index in range(len(string_list)):
        string_list[index] = string_list[index][::-1]
    return " ".join(string_list)
    
print(reverse_strings(words))



# Exercise 2 
def word_counter(some_string):
    word_tracker = {}
    clean_string = ""
    for char in some_string:
        if char not in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~":
            clean_string += char
    word_split = clean_string.split()
    for word in word_split:
        word_tracker[word.lower()] = word_tracker.get(word.lower(), 0) + 1
    return word_tracker


a_text = 'In computing, a hash table hash map is a data structure which implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index into an array of buckets or slots from which the desired value can be found'
tracked_words = word_counter(a_text)
# formats the output so that if 'key' is shorter than max_key_width it will be padded until it reaches max_key_width
max_key_width = max(len(key) for key in tracked_words.keys())
for key, value in tracked_words.items():
    print(f"{key:{max_key_width}} : {value}")



# Exercise 3 
import random

def linear_search(some_list, target):
    if target not in some_list:
        return "Number is not in the list."
    else:
        i = 0
        for number in some_list:
            if target == number:
                return f"The number {target} was found at index {i}."
            else:
                i += 1

# generates list of 100 random numbers ranging from 1-100    
nums = [random.randint(1, 101) for _ in range(100)]
print(linear_search(nums, 8))
# the time complexity of a linear search algorithm is O(n)
# meaning run-time increases linearly as size of input increases