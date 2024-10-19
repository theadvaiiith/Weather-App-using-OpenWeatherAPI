import tkinter as tk
from tkinter import messagebox
import requests

class WeatherApp:
    def __init__(self):
        self.api_key = 'd4c7d0ab38df3d0f45f417e963c8486a'  # Replace with your OpenWeather API key
        self.root = tk.Tk()
        self.root.title("Weather App")
        self.root.geometry("400x200")
        
        self.setup_ui()
    
    def setup_ui(self):
        self.city_label = tk.Label(self.root, text="Enter city:")
        self.city_label.pack()
        
        self.city_entry = tk.Entry(self.root)
        self.city_entry.pack()
        
        self.get_weather_button = tk.Button(self.root, text="Get Weather", command=self.get_weather)
        self.get_weather_button.pack()
        
        self.weather_info = tk.Label(self.root, text="")
        self.weather_info.pack()
        
        self.root.mainloop()
    
    def get_weather(self):
        city = self.city_entry.get()
        if city:
            weather = self.fetch_weather(city)
            if weather:
                self.weather_info.config(text=weather)
            else:
                messagebox.showerror("Error", "Failed to get weather data")
        else:
            messagebox.showerror("Error", "Please enter a city name")
    
    def fetch_weather(self, city):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather = (
                f"City: {data['name']}\n"
                f"Temperature: {data['main']['temp']}°C\n"
                f"Weather: {data['weather'][0]['description']}\n"
                f"Humidity: {data['main']['humidity']}%\n"
                f"Wind Speed: {data['wind']['speed']} m/s"
            )
            return weather
        return None

# Main entry point
if __name__ == "__main__":
    weather_app = WeatherApp()
