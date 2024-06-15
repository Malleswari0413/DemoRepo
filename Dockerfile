FROM python:3.8-slim

RUN pip install selenium

COPY test_script.py /test_script.py

CMD ["python", "/test_script.py"]
