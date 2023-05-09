FROM python:3.9

WORKDIR /backend
COPY ./requirements.txt /backend/

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . /backend/

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python3","manage.py","runserver", "0.0.0.0:8000"]