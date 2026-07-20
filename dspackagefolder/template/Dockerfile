# Dockerfile
FROM python:3.12-slim

WORKDIR /app

# Install uv and Jupyter
RUN pip install --no-cache-dir uv jupyterlab notebook

CMD ["bash"]


## Build the Docker image
# Run the following command from the folder containing this Dockerfile:
# docker build -t my-dev-env .

## Run the container (mount your local project directory)
# Linux/macOS:
# docker run -it -p 8888:8888 -v $(pwd):/app my-dev-env bash
#
# Windows (Command Prompt):
# docker run -it -p 8888:8888 -v %cd%:/app my-dev-env cmd

## Start Jupyter Notebook inside the container
# jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root
#
# Then open your browser and go to:
# http://localhost:8888

## Restart an existing container
# docker restart <container_name_or_id>

## Reconnect to a running container
# docker exec -it <container_name_or_id> bash
