# 
FROM python:3.9.15-bullseye

# 
WORKDIR /api

# 
COPY requirements.txt /api/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /api/requirements.txt

# 
COPY . .

# 
CMD ["uvicorn", "api_runner:app", "--host", "0.0.0.0", "--port", "6561"]