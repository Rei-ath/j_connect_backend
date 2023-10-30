# Use the Python 3.11.4 base image from Docker Hub.
FROM python:3.11.4

# Copy the contents of the current directory (where the Dockerfile is located)
# into the /app directory in the image.
COPY . /app

# Upgrade pip to the latest version.
RUN python3 -m pip install --upgrade pip

# Set the working directory to /app in the image.
WORKDIR /app

# Install Python packages listed in the requirements.txt file.
RUN pip3 install -r requirements.txt

# Change the working directory to /app/src in the image.
WORKDIR /app/src

# Define the command to run when a container is started.
# In this case, it runs the Python script process.py.
CMD [ "python3", "-u", "image_processing/process.py" ]
