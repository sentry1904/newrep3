FROM ubuntu:20.04

RUN apt-get update && \
    apt-get install -y python3 python3-pip git && \
    rm -rf /var/lib/apt/lists/*

# Clone repo
RUN git clone https://github.com/sentry1904/newrep3.git /app

# Set working directory to dock folder
WORKDIR /app/dock

# Run py1.py
CMD ["python3", "py1.py"]

