FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install OS dependencies
RUN apt-get update && apt-get install -y \
	wget \
	unzip \
	curl \
	gnupg \
	fonts-liberation \
	libnss3 \
	libgconf-2-4 \
	libxi6 \
	libxcursor1 \
	libxrandr2 \
	libxcomposite1 \
	libasound2 \
	libatk1.0-0 \
	libgtk-3-0 \
	chromium-driver \
	chromium \
	xvfb \
	--no-install-recommends && \
	apt-get clean && \
	rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy files
COPY . /app

# Install Python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Expose the port Flask runs on
EXPOSE 5000

# Start the app
CMD ["flask", "run", "--host=0.0.0.0"]

# CMD ["flas", "scraperk.py"]

