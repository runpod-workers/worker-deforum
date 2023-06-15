# Base image
FROM python:3.10-slim

# Use bash shell with pipefail option
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# Set the working directory
WORKDIR /

# Update and upgrade the system packages (Worker Template)
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install git ffmpeg libgl1-mesa-glx libglib2.0-0 -y &&\
    apt-get autoremove -y && \
    apt-get clean -y && \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies (Worker Template)
COPY builder/requirements.txt /requirements.txt
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install --upgrade pip && \
    pip install --upgrade -r /requirements.txt --no-cache-dir && \
    rm /requirements.txt

# Add src files (Worker Template)
RUN git clone https://github.com/deforum-art/deforum-stable-diffusion.git
WORKDIR /deforum-stable-diffusion
ADD src .

# Cache Models
COPY builder/cache_models.py /cache_models.py
RUN python /cache_models.py
RUN rm /cache_models.py

# Cleanup section (Worker Template)
RUN apt-get autoremove -y && \
    apt-get clean -y && \
    rm -rf /var/lib/apt/lists/*

CMD python -u /rp_handler.py
