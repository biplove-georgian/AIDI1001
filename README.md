
# Flask Webhook for Dialogflow Integration

This project is a Flask-based webhook designed to integrate with Dialogflow and provide real-time weather information. The webhook is deployed using **Render** and utilizes the **OpenWeatherMap API** to fetch weather data based on user input.

## Features
- Provides real-time weather information for any specified city.
- Includes two routes:
  - `/` - Returns student number in JSON format.
  - `/webhook` - Handles Dialogflow webhook requests and returns weather data.
- Deployed on **Render** for reliable hosting.

---

## Folder Structure
```
flask-webhook/
│
├── app.py                # Main Flask application
├── requirements.txt      # Python dependencies
├── render.yaml           # Configuration file for Render
```

---

## Setup Instructions

### 1. Prerequisites
- Python 3.7 or later installed on your system.
- A [Render](https://render.com/) account.
- An [OpenWeatherMap API Key](https://openweathermap.org/api).

---

### 2. Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/AIDI1002.git
   cd AIDI1002
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv env
   source env/bin/activate   # For Windows: env\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Add your **OpenWeatherMap API Key** to `app.py`:
   Replace `your_openweather_api_key` with your actual API key in the code:
   ```python
   API_KEY = "your_openweather_api_key"
   ```

5. Run the application locally:
   ```bash
   python app.py
   ```

6. Test the endpoints:
   - Visit `http://127.0.0.1:5000/` to verify the `/` route.
   - Use Postman or cURL to send a POST request to `http://127.0.0.1:5001/webhook` with a payload:
     ```json
     {
       "queryResult": {
         "parameters": {
           "geo-city": "Toronto"
         }
       }
     }
     ```

---

### 3. Deployment on Render

1. **Sign up** for a free [Render](https://render.com/) account.
2. **Create a new Web Service**:
   - Connect your GitHub repository.
   - Set the **Start Command** as:
     ```bash
     gunicorn app:app
     ```
3. **Deploy the service** and note the provided URL (e.g., `https://flask-webhook.onrender.com`).

4. **Test the deployed application**:
   - Visit `https://flask-webhook.onrender.com/` to verify the `/` route.
   - Use the `/webhook` endpoint to fetch weather data.

---

### 4. Dialogflow Integration

1. Go to your **Dialogflow Console**.
2. Create a new intent (e.g., `Weather Inquiry`):
   - **Training Phrases**:
     - "What's the weather in [city]?"
     - "Tell me the weather in [Toronto]."
   - **Parameter**:
     - Name: `geo-city`
     - Entity: `@sys.geo-city` (built-in Dialogflow entity).
   - **Enable Fulfillment** for this intent.

3. Add your Render webhook URL to the **Fulfillment** tab in Dialogflow:
   - Example: `https://flask-webhook.onrender.com/webhook`.

4. Save and test your agent by asking:
   - "What's the weather in Toronto?"

---

## Example Responses

### `/` Route
**Request**:
```
GET / HTTP/1.1
Host: flask-webhook.onrender.com
```

**Response**:
```json
{
    "student_number": "200572872"
}
```

---

### `/webhook` Route
**Request**:
```json
{
    "queryResult": {
        "parameters": {
            "geo-city": "Toronto"
        }
    }
}
```

**Response**:
```json
{
    "fulfillmentText": "The current weather in Toronto is 15°C with clear sky."
}
```

---

## Dependencies
- Flask
- Requests
- Gunicorn

To install dependencies, run:
```bash
pip install -r requirements.txt
```

---

## License
This project is licensed under the MIT License.

---

## Acknowledgments
- [Dialogflow](https://dialogflow.cloud.google.com/) for providing conversational AI capabilities.
- [Render](https://render.com/) for hosting the Flask application.
- [OpenWeatherMap API](https://openweathermap.org/api) for real-time weather data.
