FROM ubuntu
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
# Avoiding tzdata installation stuckness
ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=America/Sao_Paulo
# Installing python3, pip3, venv3, apache and mod_wsgi
RUN apt-get update
RUN apt install python3 -y
RUN apt install pip -y
RUN pip install poetry -y

# Defining working directory
WORKDIR /application

# Updating poetry
RUN poetry update

# Creating virtual environment
RUN poetry shell
