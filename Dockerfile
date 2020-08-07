FROM python:3.6

WORKDIR /app

COPY requirements.txt ./requirements.txt


RUN pip install -r requirements.txt

EXPOSE 8502

COPY . /app

CMD ["streamlit", "run", "PGGAN_IG_data_app.py"]