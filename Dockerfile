# Dockerfile

FROM python:3.11.4

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Upgrade pip and install python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Copy the application code to the container
COPY . .


# Command to run the application using gunicorn
CMD ["gunicorn", "--config", "gunicorn-cfg.py", "PROJECT.wsgi"]
