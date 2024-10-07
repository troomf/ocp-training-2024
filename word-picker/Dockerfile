FROM python:3.12
WORKDIR /code
RUN pip install flask
COPY word-picker.py /code/word-picker.py
ENV FLASK_APP=/code/word-picker.py
CMD ["flask", "run", "-h", "0.0.0.0"]