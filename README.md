# Karls Lotterie

Welcome to Karls Lotterie! This is a simple web application built with Flask that allows users to participate in a lottery game and see their winnings. The application also provides an admin page to view all the recorded winnings and the total accumulated winnings.

## Installation and Setup

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/Lo10Th/Karls-Lotterie
   cd lottery-app
   ```

2. Install the required dependencies using pip:

   ```bash
   pip install Flask
   ```

3. Run the Flask application:

   ```bash
   python main.py
   ```

4. Access the application in your web browser at `http://localhost:5500/`.

## Features

### Play the Lottery

- To participate in the lottery, enter your desired bet amount and click the "Los kaufen" button on the homepage.
- The lottery game has three possible outcomes, each associated with a different prize amount.

### Winning Outcomes

1. **won4.html**: If you win with a 1 in 3 chance, you will receive a 1.33 times return on your bet amount.
2. **won6.html**: If you win with a 1 in 3 chance, you will receive a 2 times return on your bet amount.
3. **won8.html**: If you win with a 1 in 3 chance, you will receive a 2.66 times return on your bet amount.

### Losing Outcome

- **lost.html**: If you lose the lottery, you will lose your bet amount.

### Admin Page

- Access the admin page at `/admin` to view all recorded winnings and the total accumulated winnings.

## Technical Details

The application uses a SQLite database to store the lottery data. Each time a user participates in the lottery, their bet amount and the outcome are recorded in the database.

## Contributions

Contributions to improve the application are welcome! Feel free to create pull requests for bug fixes, enhancements, or new features.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.