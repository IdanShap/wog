FROM python:alpine
WORKDIR /app
COPY games /app
RUN pip install -r requirements.txt
RUN python MainScores.py
EXPOSE 8080
CMD python MainGame.py