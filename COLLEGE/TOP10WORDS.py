inp = input("ENTER THE FILE TO BE OPENED:")
handle = open(inp)
count = dict()
for lines in handle:
    words = lines.split()
    for word in words:
        count[word] = count.get(word, 0)+1
lang = list()
for k, v in count.items():
    lang.append((v, k))
word_list = sorted(lang, reverse=True)
print(f"COUNTING...."
	  f"\n TOP 10 WORDS OF THE GIVEN FILE ARE AS FOLLOWS")
print(word_list[:10])
