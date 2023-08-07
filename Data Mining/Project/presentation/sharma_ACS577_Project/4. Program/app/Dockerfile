# Use the official Python image as the base image
FROM python:3.9
EXPOSE 8080

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application files to the container
COPY . .

# Set the command to run your Streamlit app
# CMD ["streamlit", "run", "app.py"]

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8080", "--server.address=0.0.0.0"]
# stock-prediction

# docker run -p 8080:8080 stock-prediction 