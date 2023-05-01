n = int(input())
all_langs = set()
st_langs = []
for i in range(n):
    m = int(input())
    langs = set()
    for j in range(m):
        lang = input()
        langs.add(lang)
        all_langs.add(lang)
    st_langs.append(langs)


common_langs = set.intersection(*st_langs)
print(len(common_langs))
for lang in sorted(common_langs):
    print(lang)

any_langs = set.union(*st_langs)
print(len(any_langs))
for lang in sorted(any_langs):
    print(lang)
