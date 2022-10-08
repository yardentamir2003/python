def sort_anagrams(list_of_strings):
    sorted_list_of_anagrams = []
    while not list_of_strings == []:
        anagrams = []
        word = list_of_strings[0]
        for i in list_of_strings:
            if sorted(i) == sorted(word):
                anagrams.append(i)
        for anagram in anagrams:
            list_of_strings.remove(anagram)
        sorted_list_of_anagrams.append(anagrams)
    return sorted_list_of_anagrams


list_of_strings = ['deltas', 'retainers', 'desalt', 'pants', 'slated', 'generating', 'ternaries', 'smelters',
                   'termless', 'staled', 'greatening', 'lasted', 'resmelts']
print(sort_anagrams(list_of_strings))
