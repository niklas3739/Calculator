FROM python:3.11-slim

# Copy requirements from root
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire app folder into the workspace
COPY . .

# Run from the workspace root
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
