try:
    import requests
    import tkinter as tk
    from tkinter import messagebox
    from datetime import datetime
    import pytz
    from tzlocal import get_localzone
    import logging
except ImportError:
    print("Error while importing dependencies!")

class WeatherApp:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"

        self.app = tk.Tk()
        self.app.title("Weather App")
        self.app.geometry("480x600")
        self.app.iconphoto(True, tk.PhotoImage(file='icon.png'))
        logging.basicConfig(filename='weather_app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

        self.create_widgets()

    def create_widgets(self):
        self.city_label = tk.Label(self.app, text="Enter City:")
        self.city_label.pack(pady=10)

        self.city_entry = tk.Entry(self.app)
        self.city_entry.pack(pady=10)
        self.city_entry.focus_set()  # Set focus on the city entry by default

        self.get_weather_button = tk.Button(self.app, text="Get Weather", command=self.get_weather_button_click)
        self.get_weather_button.pack(pady=10)

        self.result_label = tk.Label(self.app, text="")
        self.result_label.pack(pady=10)

    def get_weather(self, city):
        params = {
            'q': city,
            'appid': self.api_key,
            'units': 'metric'
        }

        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code
            data = response.json()
            self.display_weather(data)
        except requests.exceptions.RequestException as e:
            msg = f"Error fetching weather data: {str(e)}"
            messagebox.showerror('Error', msg)
            logging.error(msg + "\n")
        except ValueError as e:
            msg = f"Error decoding JSON: {str(e)}"
            messagebox.showerror('Error', msg)
            logging.error(msg + "\n")

    def get_weather_button_click(self):
        city = self.city_entry.get()
        if city:
            self.get_weather(city)
        else:
            msg = 'City name not entered!'
            messagebox.showwarning('Warning!', msg)
            logging.warning(msg + "\n")

    def display_weather(self, data):
        description = data['weather'][0]['description'].capitalize()
        temperature = data['main']['temp']
        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        wind_direction = data['wind']['deg']
        sunrise_utc = data['sys']['sunrise']
        sunset_utc = data['sys']['sunset']
        min_temp = data['main']['temp_min']
        max_temp = data['main']['temp_max']
        pressure = data['main']['pressure']

        # Detect local timezone automatically
        local_tz = get_localzone()
        sunrise_local = datetime.utcfromtimestamp(sunrise_utc).replace(tzinfo=pytz.utc).astimezone(local_tz)
        sunset_local = datetime.utcfromtimestamp(sunset_utc).replace(tzinfo=pytz.utc).astimezone(local_tz)

        result_text = f"""
Weather: {description}\n
Temperature: {temperature}°C\n
Feels Like: {feels_like}°C\n
Humidity: {humidity}%\n
Wind Speed: {wind_speed} m/s\n
Wind Direction: {wind_direction}°\n
Sunrise: {sunrise_local.strftime('%Y-%m-%d %H:%M:%S')}\n
Sunset: {sunset_local.strftime('%Y-%m-%d %H:%M:%S')}\n
Min. Temperature: {min_temp}°C\n
Max. Temperature: {max_temp}°C\n
Pressure: {pressure} hPa\n
        """
        logging.info("City: " + self.city_entry.get() + "\n" + result_text)
        self.result_label.config(text=result_text)

    def run(self):
        self.app.mainloop()

if __name__ == "__main__":
    api_key = "API_KEY" 
    weather_app = WeatherApp(api_key)
    weather_app.run()

