def search4letters(phrase: str = "", letters: str = "eiru,!") -> set:
    return {i for i in phrase if i in letters}

