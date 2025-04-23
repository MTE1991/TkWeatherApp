# TkWeatherApp
**TkWeatherApp** is a desktop application built using Python's Tkinter library. It provides users with real-time weather information for any specified city. The application fetches data from a weather API and displays it in a user-friendly interface.

## Features
- **Real-Time Weather Data**: Fetches current weather information for user-specified cities.
- **User-Friendly Interface**: Simple and intuitive GUI built with Tkinter.
- **Error Handling**: Logs errors and exceptions to a log file for troubleshooting.
- **Custom Icon**: Includes a custom application icon (`icon.png`).

## Technologies Used
- **Programming Language**: Python
- **GUI Library**: Tkinter
- **API**: Weather data fetched from a public weather API (e.g., OpenWeatherMap).

## Getting Started

### Prerequisites
- Python 3.x installed on your system.
- Required Python libraries:
  - `requests`

### Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/MTE1991/TkWeatherApp.git
   ```
2. **Navigate to the Project Directory**:
   ```bash
   cd TkWeatherApp
   ```
3. **Install Required Libraries**:
   ```bash
   pip install requests
   ```
4. **Run the Application**:
   ```bash
   python main.py
   ```

## Usage
1. Launch the application.
2. Enter the name of the city you wish to get weather information for.
3. Click the "Get Weather" button.
4. The application will display the current weather details for the specified city.

## Project Structure
- `main.py`: Main application file containing the GUI and logic to fetch and display weather data.
- `icon.png`: Custom icon for the application window.
- `weather_app.log`: Log file that records errors and exceptions encountered during runtime.

## Contributing
Contributions are welcome! If you'd like to enhance the functionality or fix issues, please fork the repository and submit a pull request.

## License
This project is open-source and available under the [MIT License](LICENSE).
