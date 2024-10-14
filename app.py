from flask import Flask, request, Response
import random
app = Flask(__name__)

@app.route("/")
def ComplexPassword():
    spacer = ' '
    if 'spacer' in request.args:
        spacer = request.args.get('spacer')
    sub_nouns = read_words('sub_nouns.txt')
    verbs = read_words('verbs.txt')
    adjectives = read_words('adjectives.txt')
    obj_nouns = read_words('obj_nouns.txt')
    adverbs = read_words('adverbs.txt')
    symbols = '-!"#$%&()*,./:;?@[]^_`{|}~+<=>'
    word_bank = [sub_nouns, adverbs, verbs, adjectives, obj_nouns]
    phrase_words = []
    for word_list in word_bank:
        random_word = random.SystemRandom().choice(word_list).title().strip()+spacer
        phrase_words.append(random_word)
    phrase_words.insert(3, str(random.randrange(10, 99))+spacer)
    random_index = random.randint(1, len(phrase_words)-1)
    phrase_words.insert(random_index, random.choice(symbols)+spacer)
    passphrase = ''.join(phrase_words).strip(spacer)+'s'
    return Response(passphrase, mimetype='text/plain')
    
def read_words(file_name):
    with open(file_name, 'r') as f:
        words = f.readlines()
    return words

if __name__ == "__main__":
    app.run()
