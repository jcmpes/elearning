FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/

ARG PUBLISHABLE_KEY
ARG KEY
ENV STRIPE_PUBLISHABLE_KEY=$PUBLISHABLE_KEY
ENV STRIPE_KEY=$KEY

ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]