FROM python:3.8-alphine

WORKDIR /lab1

COPY func.py main.py ./

CMD ["python","main.py"]