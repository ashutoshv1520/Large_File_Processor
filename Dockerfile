FROM python:3.7

ADD large_file_processor.py .

RUN pip install pymysql

CMD ["python", "./large_file_processor.py"]