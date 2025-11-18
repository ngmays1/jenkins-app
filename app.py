from datetime import datetime

app = Flask(__name__)

# Define the timezone for the timestamp
london_tz = pytz.timezone('Europe/London') # Or your preferred timezone

@app.route('/')
def hello():
    current_time = datetime.now(london_tz).strftime('%Y-%m-%d %H:%M:%S %Z%z')
    return f"<h1>Heading Update: Hello from Dockerized Jenkins CI/CD!</h1><p>The current time in London is: {current_time}</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
