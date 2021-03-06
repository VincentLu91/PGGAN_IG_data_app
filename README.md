# PGGAN_IG_data_app

## About The Project

Instagram is the biggest platform for building a brand. Over 90 million Instagram posts are uploaded per day. Millions of influencers are on the platform to sell products and promote brands. There are tremendous opportunities for businesses to build audiences and customer base. However, bootstrapped business owners with limited time or money do not have the resources to grow audiences the way their fledgling competitors do. Some founders are starting out with a side hustle. Others have a small capacity to allocate resources to other necessary functions.

Due to the frustration of growing a brand in a space where social content is crowded, I decided to build an Instagram content generator to help businesses grow audiences at scale, regardless of budget or limited amount of time spent at marketing.

I have written up a blog post on the IG Content Generator in great detail here: https://vincentlu91.github.io/2020/04/18/Attempt_IG_Generator.html

You can also find the data app demonstration in the following YouTube video: https://youtu.be/OAgeJVUTXyw

## How to access the data app

### You can set up a Docker container to run the application

You can pull the docker image from the Docker Hub repository:
https://hub.docker.com/r/vincelu299/pggan_ig_data_app_stapp

Then in the folder where you pulled the image, run:
```
docker run -p 8501:8501 pggan_ig_data_app_stapp:v1
```

You may see the suggested Network and External URLs. Ignore those - go to the browser and enter:
```http://localhost:8501/```

You should be able to view the containerized application.

### Alternatively, you can access the application in development environment

Libraries and their versions are included in requirements.txt. To install the virtual environment, run the following:

```
python3 -m venv env # or python -m venv env
source env/bin/activate
pip3 install -r requirements.txt # or pip install -r requirements.txt
```

At this point the environment should be set up with required libraries to run the application. 

Make sure you download the checkpoint folder [tree_run1](https://drive.google.com/file/d/1vFYnH91yQeEeRASPhOAEnjccHGE48Ywl/view) and place it within the `checkpoint` directory.

To run the app, enter:

```
streamlit run PGGAN_IG_data_app.py
```
Then in the browser, enter ```localhost:8501/```.

## How to use the data app

Once you started the application (container or your local environment), you should now see the data application run, generating 5 Instagram posts:

![martymcfly](https://user-images.githubusercontent.com/3411100/89596643-c2b12400-d825-11ea-979b-92649fb4f340.png)

## Pre-trained models used.

PGGAN: https://github.com/MSC-BUAA/Keras-progressive_growing_of_gans

GPT-2: https://github.com/minimaxir/gpt-2-simple

## Slides included in the repo

IG_Content_Generator_Slides.pptx
