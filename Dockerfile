# Select a base image
FROM python:3.11-slim

# Select working directory
WORKDIR /usr/app

#Copy the required files
COPY  . .,

RUN pip install -r requirements.txt

COPY . .

# Add user to run it as a non-root user
RUN useradd app
USER app

# Add commands
CMD [ "python", "app.py" ]