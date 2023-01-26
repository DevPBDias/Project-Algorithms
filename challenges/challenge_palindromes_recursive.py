def is_palindrome_recursive(word, low_index, high_index):
    if word == "":
        return False
    # se o valor do indice for diferente, entao nao é palindromo
    if word[low_index] != word[high_index]:
        return False
    #se for len() for par: low_index > high_index
    #se for len() for impar: low_index == high_index
    if low_index >= high_index:
        return True
    # chamada de recursividade
    else:
       return is_palindrome_recursive(word, low_index + 1, high_index - 1)


# print(is_palindrome_recursive("ANA", 0, 2))
# print(is_palindrome_recursive("JOAO", 0, 3))
