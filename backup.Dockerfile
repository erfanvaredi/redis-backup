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
CMD ["python", "backup_runner.py"]