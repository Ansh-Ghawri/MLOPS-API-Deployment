# 1. Use an official Python runtime as a parent image
FROM python:3.9-slim

# 2. Set the working directory in the container
WORKDIR /app

# 3. Copy the requirements file into the container at /app
COPY requirements.txt .

# 4. Install any needed packages specified in requirements.txt
#    --no-cache-dir reduces image size
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of the application code and the model file into the container at /app
COPY . .

# 6. Make port 5000 available to the world outside this container
EXPOSE 5000

# 7. Define environment variable (optional but good practice)
ENV FLASK_APP=app.py

# 8. Run app.py when the container launches
#    Use the production server gunicorn if you were going live, but flask run is fine for this project
#    CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"] # Production way
# Simpler way for now (uses Flask's dev server)
CMD ["python", "app.py"] 