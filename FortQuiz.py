# dictionary that stores questions and answers
quiz = {
    'Question1': {
        'Question':'What is the capital of France?',
        'Answer': 'Paris'    
    },
    'Question2': {
        'Question':'What is the capital of Germany?',
        'Answer': 'Berlin'    
    },
    'Question3': {
        'Question':'What is the capital of Italy?',
        'Answer': 'Rome'    
    },
    'Question4': {
        'Question':'What is the capital of Spain?',
        'Answer': 'Madrid'    
    },
    'Question5': {
        'Question':'What is the capital of Portugal?',
        'Answer': 'Lisbon'    
    },
    'Question6': {
        'Question':'What is the capital of SwitzerLand?',
        'Answer': 'Bern'    
    },
    'Question7': {
        'Question':'What is the capital of China?',
        'Answer': 'Beijing'    
    },
}

Score = 0
# have a variable that track the score of the player
#  loop through the dictionary using the key values pairs
for key, value in quiz.items():
    print(value['Question'])
    answer = input('Answer?')

    if answer.lower() == value['Answer'].lower():
        print('Correct')
        Score = Score + 1
        print('Your score is :' + str(Score))
        print('')

    else:
        print('Wrong!')
        print('The answer is :' + value['Answer'])  
        print('Your score is :' + str(Score))  
        print('')
# displays each questions to the user and allow them to answer
# show the final result in percentage when the quiz is completed using 
print('You got ' + str(Score) + ' out of 7 questions correctly')
print('Your pecentage is ' + str(int(Score/7 * 100)) + '%')