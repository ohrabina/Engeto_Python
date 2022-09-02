import random
def main(words):

    word = random.choice(words)
    guesses_available = int(len(word)*2)
    status = ['_'] * len(word)
    print('Myslím si slovo, co to je?')

    while True:
        letter = get_letter(status, guesses_available)
        replace_letters(letter, word, status)
        guesses_available -= 1

        if '_' not in status:
            print('\nVyhrál si!\n')
            break

        if not guesses_available:
            print('\nProhrál si :-( Slovo bylo:\n' + word)
            break
def get_letter(status,guesses_available):

    print(' '.join(status))
    letter = input('Hádej písmeno | počet pokusů: '+ str(guesses_available) + '\n')
    return letter

def replace_letters(letter, word, status):
    count_replaced = 0

    for i,char in enumerate(word):
        if char == letter:
            status[i] = letter
            count_replaced += 1

    if count_replaced:
        print("Počet uhádnutých písmen: " + str(count_replaced))

    else:
        print('Písmeno ' + letter + ' ve slově není')

words = ['Hangman', 'available', 'increase']

main(words)