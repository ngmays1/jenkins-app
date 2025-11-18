# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# coy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy the remaining application code to /app
COPY . /app

# expose port 5000 to outside world
EXPOSE 5000

# run app when container launches
CMD ["python", "app.py"]
