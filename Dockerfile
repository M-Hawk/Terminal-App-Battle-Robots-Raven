# Use a lightweight Alpine Linux image with Python 3.12 pre-installed
FROM python:3.12-alpine3.22

# Set the working directory inside the container to /app
WORKDIR /app

# Copy only the requirements.txt file from your host into the container's /app folder, needs to do this to install the dependencies before copying the rest of the files
COPY requirements.txt .

# Install necessary system packages:
# - build-base: basic build tools (gcc, make, etc.) needed for compiling Python packages with native extensions
# - bash: install bash shell (some scripts might require it)
# - ncurses: provides terminal handling libraries, needed for terminal-based UI packages
RUN apk add --no-cache build-base bash ncurses

# Use pip to install Python dependencies listed in requirements.txt
# --no-cache-dir prevents caching to reduce image size
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire current directory (source code, scripts, etc.) into the container’s /app directory
COPY . .

# Set an environment variable so Python includes /app in its module search path
# This allows imports like "from src.module import Class" to work correctly
ENV PYTHONPATH=/app

# Specify the default command to run when the container starts:
# runs the main.py Python script using Python 3
CMD ["python3", "src/main.py"]