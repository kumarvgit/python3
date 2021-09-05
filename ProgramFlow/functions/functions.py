def multiply():
    result = 10.5 * 4
    return result


def is_palindrome(string: str) -> bool:
    # reverse a string
    backwards = string[::-1]
    return backwards.casefold() == string.casefold()


def palindrome_sentence(sentence) -> bool:
    sentence = sentence.casefold()
    extracted = ''
    for char in sentence:
        if char.isalnum():
            sentence += char
    # return extracted[::-1] == sentence
    return is_palindrome(extracted)


def fibonacci(n: int) -> int:
    """
    Returns the sum of fibonacci series until positive `n` th

    :param n: the positive number
    :return: a sum of fibonacci series
    """

    if 0 <= n <= 1:
        return n
    if n < 0:
        return None

    n_minus_1 = 1
    n_minus_2 = 0
    result = None
    for i in range(n - 1):
        result = n_minus_2 + n_minus_1
        n_minus_2 = n_minus_1
        n_minus_1 = result
    return result


answer = multiply()
print(answer)

word = input("Enter a word to check for palindrome: ")
if is_palindrome(word):
    print('{} ia palindrome'.format(word))
else:
    print('{} is not a palindrome'.format(word))

sentence = input("Enter a sentence to check for palindrome: ")
if palindrome_sentence(sentence):
    print('{} ia palindrome'.format(sentence))
else:
    print('{} is not a palindrome'.format(sentence))


for i in range(36):
    print(i, fibonacci(i))

is_palindrome('as')
