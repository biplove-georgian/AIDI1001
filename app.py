import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# My OpenWeatherMap API key
API_KEY = "ac7b8306ddb9a4ede8dbc073be32946f"

@app.route("/", methods=["GET"])
def home():
    return jsonify({"Student_Number": "200572872"})  # Student Number Provided

@app.route("/webhook", methods=["POST"])
def webhook():
    req = request.get_json()

    # Extract location from Dialogflow request
    location = req.get("queryResult").get("parameters").get("geo-city")

    if not location:
        response_text = "I'm sorry, I couldn't find the location. Can you please specify a city?"
    else:
        # Call the OpenWeatherMap API
        weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=metric"
        weather_response = requests.get(weather_url)

        if weather_response.status_code == 200:
            weather_data = weather_response.json()
            # Extract weather details
            temp = weather_data["main"]["temp"]
            description = weather_data["weather"][0]["description"]
            response_text = f"The current weather in {location} is {temp}°C with {description}."
        else:
            response_text = f"I couldn't fetch the weather for {location}. Please make sure the city name is correct."

    # Respond back to Dialogflow
    return jsonify({
        "fulfillmentText": response_text
    })

if __name__ == "__main__":
    app.run(debug=True, port=5001)