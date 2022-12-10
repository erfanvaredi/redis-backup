# 
FROM python:3.9.15-bullseye

# 
WORKDIR /redis-backup

# 
COPY requirements.txt /redis-backup/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /redis-backup/requirements.txt

# 
COPY . .

# 
CMD ["uvicorn", "api_runner:app", "--host", "0.0.0.0", "--port", "6561"]