FROM python:3.13

WORKDIR /app
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
# Expose port 8000 to allow communication to/from server
EXPOSE 8000
# Run the API with uvicorn
# --host 0.0.0.0 makes the server accessible from outside the container
CMD ["uvicorn", "IronLog.api:app", "--host", "0.0.0.0", "--port", "8000"]