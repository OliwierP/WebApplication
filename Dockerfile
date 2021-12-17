FROM python:latest
             
COPY WebApp myapp13

# UZUPELNIJ POLECENIA (patrz README aplikacji WebApp, nie używaj srodowiska wirtualnego)
WORKDIR /myapp13

RUN pip install -r requirements.txt
RUN export FLASK_APP=app.py
RUN export FLASK_ENV=development
RUN export FLASK_RUN_HOST=localhost
RUN export FLASK_RUN_PORT=5000

ENTRYPOINT ["python", "-m", "flask", "run"]
