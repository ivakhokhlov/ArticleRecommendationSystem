FROM python:3.12 

WORKDIR /home/app/web/

RUN pip3 install poetry

RUN poetry config virtualenvs.create false

WORKDIR /home/app/web/
COPY ./pyproject.toml ./pyproject.toml

COPY ./src ./src
COPY ./main.py ./main.py 
EXPOSE 8000

RUN poetry install

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
