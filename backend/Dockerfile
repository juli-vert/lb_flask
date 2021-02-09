FROM python:3.9.1-slim
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY backend.py .
CMD ["5000"]
ENTRYPOINT [ "python3", "backend.py" ]