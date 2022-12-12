## Intro

The main purpose of this repo is to make a module that can simplify the mechanism of getting dynamic backup from redis and store them in the storage

# Dependencies
1. Install [Python](https://www.python.org/downloads/)
2. Install [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or [Anaconda](https://www.anaconda.com/products/individual)
3. Clone/pull the project
```sh
git pull
```
4. Create [new environment](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) by conda if you didn't:
```sh
conda create --name redis-backup python=3.9
```
5. Activate the environment: [Need help](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#activating-an-environment)
```sh
conda activate redis-backup
```
6. Install [pip](https://pip.pypa.io/en/stable/installation/) if your environment doesnt have it:

7. Install the other requirements and package
```sh
pip install -r requirements.txt
```
8. Smile

# Pre commit
1. For linting your code base
```sh
make lint
```

# How to run
1. Prepare the configs
2. Create .env file and fill "..." ones:
```sh
cp .env.example .env
```
3. Run the redis-backup container
```sh
make start
```
1. How to stop
```sh
make stop
```
---

# How to redis example
1. Run Redis docker and set env vars
2. Go to example folder
```sh
cd examples
```
3. Run redis listener:
```sh
python test_listener.py
```
4. send message to redis
```sh
python test_producer.py --m your_message
```
---