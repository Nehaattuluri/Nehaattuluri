# # Use an official Python runtime as a parent image
# FROM python:3.9-alpine

# # Set the working directory in the container
# WORKDIR /app

# # Copy the current directory contents into the container at /app
# COPY . /app

# # RUN pip install uv
# # RUN ./venv/scripts/activate
# # Install any needed packages specified in requirements.txt
# RUN pip install streamlit

# # Make port 8501 available to the world outside this container
# EXPOSE 8501

# # Run the Streamlit app
# CMD ["streamlit", "run", "energy_estimation_app.py"]


FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

# RUN git clone https://github.com/streamlit/streamlit-example.git .
COPY . /app

RUN pip3 install -r requirements.txt

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]