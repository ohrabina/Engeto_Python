def all_anagrams(*args) -> bool:
    vzor = sorted(args[0])
    for slovo in args:
        if sorted(slovo) != vzor:
            return False
    else:
        return True
print(
    all_anagrams("ship", "low"),
    all_anagrams("ship", "duck"),
    sep="\n"
)


