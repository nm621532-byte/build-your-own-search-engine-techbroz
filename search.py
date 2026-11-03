docs = {1: "python seekho free mein",
        2: "javascript se website banao",
        3: "python se website aur AI"}

index = {}
for i, text in docs.items():
    for word in text.split():
        index.setdefault(word, set()).add(i)

def search(q):
    ids = [index.get(w, set())
           for w in q.split()]
    return sorted(set.intersection(*ids))

print("python ->", index["python"])
print("python website ->",
      search("python website"))
