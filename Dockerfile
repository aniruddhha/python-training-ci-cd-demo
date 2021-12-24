FROM python:latest

RUN pip3 install pipenv

ENV PROJECT_DIR /rest-api-cicd

WORKDIR ${PROJECT_DIR}

COPY Pipfile .

COPY Pipfile.lock .

COPY . .

RUN pipenv install --deploy 

EXPOSE 80

CMD ["pipenv", "run", "python", "api.py"]