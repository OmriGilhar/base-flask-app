# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ADD . .
# Expose port
EXPOSE 5000
# start the app
CMD ["gunicorn", "wsgi:app"]