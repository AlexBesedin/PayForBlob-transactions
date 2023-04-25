FROM python:3.8.10
WORKDIR /app
COPY requirements.txt .

RUN python -m pip install --upgrade pip
RUN pip3 install -r /app/requirements.txt --no-cache-dir

COPY . .
CMD ["gunicorn", "project_name.wsgi:application", "--bind", "0:8000" ]