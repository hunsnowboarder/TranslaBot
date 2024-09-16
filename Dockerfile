FROM python:3.11.10-slim

EXPOSE 8501

ENV POETRY_VIRTUALENVS_CREATE=false

WORKDIR /app

RUN pip install poetry

COPY pyproject.toml poetry.lock /app/

RUN poetry install

COPY . /app/

CMD ["streamlit", "run", "app.py"]