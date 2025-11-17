## Who Wants To Be A Millionaire

AIM - Develop a version of the game using:

- classes to structure our code
- question bank stored within files
- tests to validate the game code

### Define Class Structures

`Question` class

#### Attributes

 - Question Text
 - Difficulty
 - Option A
 - Option B
 - Option C
 - Option D

Each option is dict with text and boolean correct/incorrect

##### Methods

initialise it from a , correct ans and three wrong ans

.randomise() shuffle answers randomly
.fiftyfifty() remove two wrong answers at random
.check_answer(user_ans) # return "correct" "wrong" "invalid"

`GameBoard` Class

#### Attributes

- money ladder
- player level (money)
- question_set
- lifelines left (number of 50:50s)
- player names
- final_answer_locked


##### Methods

- initialisation(question_bank_file)
- start_game()
- play_round()