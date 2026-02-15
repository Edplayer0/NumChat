# NumChat: Chat Analyzer

NumChat is a Python-based application designed to analyze chat data from exported JSON files. It provides insights into chat history, including message trends, participant activity, and more, through an interactive and user-friendly graphical interface.

## Features

- **Interactive Dashboard**: Visualize chat data with charts and graphs.
- **Participant Analysis**: View message statistics for individual participants.
- **Time-Based Insights**: Analyze messages by day, week, month, or year.
- **Customizable Views**: Filter and explore data with ease.
- **Support for Telegram Chats**: Currently supports JSON exports from Telegram.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Edplayer0/NumChat.git
   cd NumChat
   ```

2. Install dependencies:
   ```bash
   pip install poetry
   poetry install --no-root
   ```

3. Run the application:
   ```bash
   poetry run python src/main.py
   ```

## Usage

1. Launch the application.
2. Select a JSON file exported from Telegram.
3. Explore the dashboard to analyze your chat data.

## Requirements

- Python 3.14 or higher
- Dependencies listed in `pyproject.toml`

## Project Structure

- `src/`: Contains the source code for the application.
  - `app/`: Application entry point.
  - `core/`: Core logic for parsing and analyzing chat data.
  - `ui/`: User interface components.
  - `models/`: Data models and constants.
  - `style/`: Application styles.
- `tests/`: Placeholder for unit tests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## Author

- **Edgar Ayuso Martínez**  
  Email: [edgarayusodev@proton.me](mailto:edgarayusodev@proton.me)