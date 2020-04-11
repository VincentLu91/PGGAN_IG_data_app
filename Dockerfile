FROM python:3

#WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
CMD [ "pip3" ,"install", "--upgrade" "https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-1.4.0-py3-none-any.whl"]

#COPY . .

#CMD [ "python", "./your-daemon-or-script.py" ]
# run a container or just put a command for python train.py!? need some clarity