FROM 3.10-alpine
RUN mkdir -p /app
WORKDIR /app
RUN pip install pipenv
COPY Pipfile Pipfile.lock /app/
RUN pipenv install --system --deploy
COPY . /app/
EXPOSE 8000

CMD ["gunicorn", "-R", "-b", "0.0.0.0:8000", "-t", "2000", "--max-requests", "2000", "tasks_manager.wsgi"]
