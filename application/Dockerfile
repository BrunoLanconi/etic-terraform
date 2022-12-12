FROM ubuntu
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
# Avoiding tzdata installation stuckness
ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=America/Sao_Paulo
# Installing python3, pip and poetry
RUN apt-get update
RUN apt install python3 -y
RUN apt install pip -y
RUN pip install poetry
# Copying content
COPY . /application
# Defining working directory
WORKDIR /application
# Updating poetry
RUN poetry update
# Making migrations
RUN poetry run python api/manage.py makemigrations
RUN poetry run python api/manage.py migrate
# Running server
CMD ["poetry", "run", "python", "api/manage.py", "runserver", "80"]
