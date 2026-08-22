# 0. lightning round de longitudes de strings
a = ""
length_a = len(a)

b = "it's ok"
length_b = len(b)

c = 'it\'s ok'
length_c = len(c)

e = '\n'
length_e = len(e)

# 1. validar codigo postal (5 digitos)
def is_valid_zip(zip_code):
    """Devuelve si el string es un codigo postal valido (5 digitos)."""
    return len(zip_code) == 5 and zip_code.isdigit()

# 2. buscar palabra completa dentro de una lista de documentos
def word_search(doc_list, keyword):
    indices = []
    for i, doc in enumerate(doc_list):
        tokens = doc.lower().replace(",", "").replace(".", "").split()
        if keyword.lower() in tokens:
            indices.append(i)
    return indices

# 3. buscar varias palabras clave
def multi_word_search(doc_list, keywords):
    result = {}
    for keyword in keywords:
        result[keyword] = word_search(doc_list, keyword)
    return result

if __name__ == "__main__":
    print(length_a, length_b, length_c, length_e)
    print(is_valid_zip("12345"))
    print(is_valid_zip("1234a"))

    doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
    print(word_search(doc_list, "casino"))
    print(multi_word_search(doc_list, ["casino", "they"]))
