FROM python:3.6

WORKDIR /app

COPY requirements.txt ./requirements.txt


RUN pip install -r requirements.txt

RUN pip install streamlit

RUN pip install tensorflow==1.13.1

RUN pip install gpt_2_simple

EXPOSE 8502

COPY . /app

CMD ["streamlit", "run", "PGGAN_IG_data_app.py"]