import unicodedata, random

random.seed()

def generate_book_data(inputfile):
    book=[]
    with open(inputfile, 'r', encoding="utf-8") as file:
        for line in file:
            book.append(line)
    return book
book = generate_book_data("sblgnt.txt")
# file = open('sblgnt.txt', 'r', encoding="utf-8")

# book = []

# for line in file:
#     book.append(line)

# file.close()

#done = False
practicelength = 1
startattempts = 2
versespracticed = 0
score = 0



def strip_accents(string):
    """Returns word with accents removed. Breathing marks, iota subscripts, and diareses remain"""
    accents = ['\u0300','\u0301','\u0302','͂']
    chars = [c for c in unicodedata.normalize('NFD', string) if c not in accents]
    return unicodedata.normalize('NFC', ''.join(chars))

def choose_verse(book, practicelength=1):
    verse = book[random.randrange(len(book))]
    reference = verse.split('\t')[0]        # In the SBL files, references are tab-separated from verse text
    text = verse.split('\t')[1].strip()
    words = text.split(' ')
    
    if len(words)<practicelength + 1:
        return choose_verse(book)
    else:
        return reference, text, words

def check_answer(correctanswer,attempts):
    if attempts == 0:
        print ("\nCorrect answer: ", correctanswer)
        return 0
    else:
        answer = input().strip()
        answer = unicodedata.normalize('NFD',answer)
        answer.replace('\u0302','͂').replace('\'','\ʼ').replace('’','\ʼ')    # Change circumflex and apostrophe to match SBL file   
        answer.replace('\'','ʼ')
        answer = unicodedata.normalize('NFC',answer)
        if answer == correctanswer:
            print("\nὈρθῶς ἀπεκρίθης!\n")
            return 1
        else:
            attempts -= 1
            print("Incorrect.", attempts, "attempt(s) remaining.")
            return check_answer(correctanswer, attempts)
            
    
while True:
    reference, text, words = choose_verse(book)
    attempts = startattempts
    startword = random.randrange(len(words)-practicelength+1)

    before = unicodedata.normalize('NFC',' '.join(words[0:startword]))
    after = unicodedata.normalize('NFC',' '.join(words[startword+practicelength:len(words)]))

    practicewords = []
    practicewordsstripped = []
    for word in range(practicelength):
        practicewords.append(words[startword + word])
        practicewordsstripped.append(strip_accents(words[startword + word]))

    print(before, '[[[',' '.join(practicewordsstripped),']]]',after,'\n',reference)
    print("\nType the bracketed portion with correct accents: ")
    correctanswer = unicodedata.normalize('NFC',' '.join(practicewords))

    score += check_answer(correctanswer, attempts)
    versespracticed += 1

    print(text)

    again = input("\nPress <enter> to continue. If you're done, type \"x\" or \"ξ\" to exit.\n").strip()
    if again in ['x','X','ξ','Ξ']:
        break
    else:
	    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

print("\nYour score this session: ", score, "/", versespracticed)
exit = input("\nPress <enter> to close program.")






    

