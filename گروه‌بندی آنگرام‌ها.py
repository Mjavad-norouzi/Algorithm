def group_anagrams(arr):
    anagrams = {}

    for text in arr:
        sorted_text = ''.join(sorted(text))

        if sorted_text not in anagrams:
            anagrams[sorted_text] = []

        anagrams[sorted_text].append(text)

    return list(anagrams.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

result = group_anagrams(strs)
print(result)
