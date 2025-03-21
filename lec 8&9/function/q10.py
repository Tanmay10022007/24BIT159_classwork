def frequency():
    string = input("Enter the string: ")  
    words = string.split()  
    freq_dict = {} 

    for word in words:
        freq_dict[word] = freq_dict.get(word, 0) + 1
    
    sorted_freq = dict(sorted(freq_dict.items()))

    return sorted_freq 


word_frequencies = frequency()
print("Word Frequencies:", word_frequencies)
#not completed
