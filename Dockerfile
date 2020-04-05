# Use the latest Ubuntu LTS image
FROM ubuntu:latest

# Install Flask to run the server
RUN pip install Flask

# Copy the files for the model and the server
COPY app.py app.py
COPY rf_model_1.pickle rf_model_1.pickle
COPY rf_model_2.pickle rf_model_2.pickle
COPY rf_model_3.pickle rf_model_3.pickle

# Expose port 5000 for the Flask server
EXPOSE 5000

# Run the Flask server on container start
CMD ["python", "app.py"]
