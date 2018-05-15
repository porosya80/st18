import random


def word_gen():
    words = ['new', 'book', 'adjustment', 'airplane', "hello"]
    word = random.choice(words)
    answer = [x.lower() for x in word]

    hidden_word = ["*" for i in range(len(word))]

    tries = len(word) + 2
    return tries, hidden_word, answer



def draw(tries, hidden_word):
    print('Количество попыток : ', tries)
    print('Слово : ' + "".join(hidden_word))


def check(answer,hidden_word,tries):
    chr = input("Введите букву: ")[0].lower()
    if chr in answer:
        for i, ch in enumerate(answer):
            if ch == chr:
                hidden_word[i] = chr
    else:
        tries -= 1
    return tries, hidden_word


def main():
    tries, hidden_word, answer = word_gen()
    while '*' in hidden_word and tries > 0:
        draw(tries, hidden_word)
        tries, hidden_word = check(answer, hidden_word, tries)
    print( "You Lose") if tries == 0 else print("You win")


if __name__ == '__main__':
    main()