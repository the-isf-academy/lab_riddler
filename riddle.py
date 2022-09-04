from fuzzywuzzy import fuzz


class Riddle:
    def __init__(self,prompt,answer):
        self.prompt = prompt
        self.answer = answer


    def check_guess(self,guess):
        """Checks whether a guess is correct.
        Uses the fuzzywuzzy library to accept guesses which are close to the answer.
        """
        min_fuzz_ratio = 80
        similarity = fuzz.ratio(guess.lower(), self.answer.lower())
        
        if similarity >= min_fuzz_ratio:
            return True
        else:
            return False
    
 


riddles = [
    Riddle(
        'What has to be broken before you can use it?',
        'an egg'),
    Riddle(
        'What month of the year has 28 days?',
        'all of them'
    ),
    Riddle(
        'What goes up but never comes down?',
        'age'
    ),
    Riddle(
        'What gets wet while drying?',
        'a towel'
    )
]