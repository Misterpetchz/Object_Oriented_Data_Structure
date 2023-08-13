def extractQuote(text, idx=0, result=None):
    if result is None:
        result = []
    
    first = text.find("'", idx)
    second = text.find("'", first + 1)

    if first == -1 or second == -1:
        return result
    
    str = text[first + 1: second]
    result.append(str)

    return extractQuote(text, second +  1, result)

# def segment(text, word_list):
#     if not text:
#         return True

#     if not word_list:
#         return False
    
#     word = word_list[0]
#     if word in text:
#         remaining_text = text.replace(word, '', 1)
#         if segment(remaining_text, word_list):
#             return True
    
#     return segment(text, word_list[1:])

def segment(text, word_list):
    if not text:
        return True

    if not word_list:
        return False

    word = word_list[0]
    if word and word in text:
        remaining_text = text.replace(word, '', 1)
        if segment(remaining_text, word_list) or segment(text, word_list[1:]):
            return True

    return segment(text, word_list[1:])


inp = extractQuote(input('Enter list[str]: '))
text, language = inp[0], inp[1:]

print(f"text: str = '{text}'")
print(f'lang: list[str] = {language}')
print(f"segment(text, lang) -> {segment(text, language)}")