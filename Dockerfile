FROM python:3.11-alpine
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
RUN python -m compileall .
CMD ["python", "-c", "print('Auction service is running')"]
