def palindrome(word):
    return word == word[::-1]

def main():
    word = input("Input: ")
    if(palindrome(word)): print(word + " é um palindromo") 
    else: print(word + "Não é um palindromo")
        
main()