import mysql.connector

# Establish a connection to the MySQL server
db = mysql.connector.connect(
    host="localhost",
    user="****",
    password="*********",
    database="hello"
)

# Create a cursor object to execute SQL queries
cursor = db.cursor()

# Function to record game moves in the database
def record_move(table_name, move_number, move_input, input_result):
    insert_query = f"""
        INSERT INTO {table_name} (move_number, move_input, input_result)
        VALUES (%s, %s, %s)
    """
    cursor.execute(insert_query, (move_number, move_input, input_result))
    db.commit()

# Function to play Hangman game
def play_hangman(name):
    words = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grapefruit', 'honeydew']
    import random

    def Random_word():
        return random.choice(words)

    def display_word(word, guessed_letters):
        for letter in word:
            if letter in guessed_letters:
                print(letter, end=' ')
            else:
                print('_', end=' ')
        print()

    def HANGMAN():
        word = Random_word()
        guessed_letters = []
        tries = 6
        move_number = 1

        # Generate a unique table name using the user's name
        table_name = f"{name.replace(' ', '_')}_game_moves"

        # Create a table to store the game moves
        create_table_query = f"""
            CREATE TABLE IF NOT EXISTS {table_name} (
                move_number INT AUTO_INCREMENT PRIMARY KEY,
                move_input VARCHAR(255),
                input_result VARCHAR(20)
            )
        """
        cursor.execute(create_table_query)

        while tries > 0:
            display_word(word, guessed_letters)
            guess = input('Enter a letter: ').lower()
            if guess in guessed_letters:
                print('You already guessed that letter.')
                continue

            guessed_letters.append(guess)

            if guess in word:
                print('Correct guess!')
                input_result = 'Correct'
            else:
                print('Incorrect guess!')
                tries -= 1
                print('Tries left:', tries)
                input_result = 'Incorrect'

            record_move(table_name, move_number, guess, input_result)
            move_number += 1

            if all(letter in guessed_letters for letter in word):
                print('Congratulations! You guessed the word:', word)
                break

        if tries == 0:
            print('You lost! The word was:', word)

    HANGMAN()

# Main loop to play Hangman for multiple users
while True:
    # Prompt the user to enter their name
    name = input("Enter your name (or 'exit' to quit): ")
    if name.lower() == "exit":
        print("Exiting the program.")
        break

    play_hangman(name)

# Close the cursor and database connection
cursor.close()
db.close()
