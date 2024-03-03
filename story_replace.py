
filename = input("Enter the name of the file: ")

with open(filename, 'r') as f:
    story = f.read()

target_start = "<"
target_end = ">"
start_of_word = -1
words = set()

for i, ch in enumerate(story):
    if ch == target_start:
        start_of_word = i

    if ch == target_end and start_of_word != -1:
        word = story[start_of_word: i + 1]
        words.add(word)
        start_of_word = -1


answers = {}

for word in words:
    answer = input("Enter a word for " + word + ": ")
    answers[word] = answer


for word in words:
    story = story.replace(word, answers[word])


print(story)
