FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -U pip
RUN pip install -r requirements.txt
COPY . .
CMD ["pytest", "--browser", "chrome"]
