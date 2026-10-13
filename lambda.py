is_passing = lambda marks: marks>40
print(is_passing(60))

List_of_words = ["Python", "Javascript", "Java", "C", "C++","ReactJS","NodeJS"]

Max_words = max(List_of_words, key= lambda size: len(size))
print(Max_words)