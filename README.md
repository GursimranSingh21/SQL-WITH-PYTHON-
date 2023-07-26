# SQL-WITH-PYTHON-
The script defines a record_move function to record the user's game moves into the MySQL database.
The revised Python script is a professional Hangman game with MySQL database integration. It allows users to play the classic Hangman game by guessing letters to reveal a hidden word. The game tracks the user's moves and stores them in a MySQL database for later retrieval and analysis.

Key Features:

Database Connection:
The script establishes a connection to a MySQL server running on localhost, using the username "****" and a specified password. If there is an error in connecting to the server, it will display an appropriate error message and exit gracefully.

Record Keeping:
The script defines a record_move function to record the user's game moves into the MySQL database. Each move, along with its move number, guessed letter, and result (correct/incorrect), is stored in a separate table named after the user's name. If there is an error in executing the SQL query, it handles the exception and rolls back the transaction to maintain data integrity.

User Interaction:
The game prompts users to enter their names. If the user enters "exit", the program terminates gracefully. Otherwise, the play_hangman function is called to initiate the Hangman game for that user.

Hangman Game:
The play_hangman function sets up the Hangman game for the user. It selects a random word from a predefined list and allows the user to guess letters. The game keeps track of the guessed letters, the number of tries remaining, and records each move using the record_move function. It also displays the game state after each move, informing the user if their guess is correct or incorrect.

Table Creation:
For each user, a unique table is generated using their name (with spaces replaced by underscores) followed by "_game_moves". This approach ensures each user's game moves are stored in a separate table for easy data management and analysis.

Error Handling:
The script handles potential errors gracefully by displaying appropriate error messages and rolling back transactions if necessary.
