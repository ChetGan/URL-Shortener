FROM python:3.9.2

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY test_cases.py /app

ENV FLASK_APP=app.py

COPY . .
#Running Test Cases. Comment out for production builds.
RUN python3 test_cases.py

EXPOSE 5001

CMD ["flask", "run", "-h", "0.0.0.0", "-p", "5001"]