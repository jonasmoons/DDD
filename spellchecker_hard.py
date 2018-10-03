words_wrong = ["stupid", "yes", "no", "right", "wrong", "frituurpan"]
words_right = ["fun", "no", "yes", "wrong", "right", "koekenpan"]
zin = input("Schrijf hier je zin ")
words = zin.split()
index = 0

for word in words:
	if word in words_wrong:
		right_word_index = words_wrong.index(word)
		words[index] = words_right[right_word_index]
	index = index+1
words = " ".join(words)
print(words)