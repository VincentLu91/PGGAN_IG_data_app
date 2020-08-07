# PGGAN_IG_data_app

Update (July 15 2020): since having uploaded the repository, the app does not work again after cloning the code, as the app now complains about an incorrect number of weights or layers used, even though the code and weight files are untouched.

The best way to view the application in action is to watch the YouTube demo as alluded to below.

Update (August 6 2020): the data application now finally works, but the checkpoint files are too large to upload to the repository. Also, the git-LFS service has exhausted its quota and it is not possible to upload them to the repository. To circumvent this, I created a google downloadable link to the checkpoint files: https://drive.google.com/file/d/1vFYnH91yQeEeRASPhOAEnjccHGE48Ywl/view

## About The Project

Instagram is the biggest platform for building a brand. Over 90 million Instagram posts are uploaded per day. Millions of influencers are on the platform to sell products and promote brands. There are tremendous opportunities for businesses to build audiences and customer base. However, bootstrapped business owners with limited time or money do not have the resources to grow audiences the way their fledgling competitors do. Some founders are starting out with a side hustle. Others have a small capacity to allocate resources to other necessary functions.

Due to the frustration of growing a brand in a space where social content is crowded, I decided to build an Instagram content generator to help businesses grow audiences at scale, regardless of budget or limited amount of time spent at marketing.

I have written up a blog post on the IG Content Generator in great detail here: https://vincentlu91.github.io/2020/04/18/Attempt_IG_Generator.html

You can also find the data app demonstration in the following YouTube video: https://youtu.be/OAgeJVUTXyw

## How to access the data app

### You can set up a Docker container to run the application

After cloning the repo, download the `tree_run1.zip`: https://drive.google.com/file/d/1vFYnH91yQeEeRASPhOAEnjccHGE48Ywl/view

Once downloaded, unzip `tree_run1.zip` and place the `tree_run1` folder in the `checkpoint` folder in the root directory
![martymcfly](https://user-images.githubusercontent.com/3411100/89595437-803a1800-d822-11ea-851e-7a6b77641cf7.png)

Cd to the repo and run:

```
docker build -t pggan_ig_data_app_stapp:v1 .
```

Then:
```
docker run -p 8501:8501 pggan_ig_data_app_stapp:v1
```

You may see the suggested Network and External URLs. Ignore those - go to the browser and enter:
```http://localhost:8501/```

You should be able to view the containerized application.

### Alternatively, you can access the application in development environment

Dependencies are included in requirements.txt. To install the virtual environment, run the following:

```
python3 -m venv env # or python -m venv env
source env/bin/activate
pip3 install -r requirements.txt # or pip install -r requirements.txt
```

At this point the environment should be set up with required libraries to run the application. 

Download the `tree_run1.zip`: https://drive.google.com/file/d/1vFYnH91yQeEeRASPhOAEnjccHGE48Ywl/view

Once downloaded, unzip `tree_run1.zip` and place the `tree_run1` folder in the `checkpoint` folder in the root directory.

If you don't have streamlit installed on your machine, run:

```
pip install streamlit
```

Then to run the app, cd to the project folder and enter:

```
streamlit run PGGAN_IG_data_app.py
```

In the terminal, you should see the following right after the command:

```
  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.2.28:8501
```

This will load up the data app and open a new browser tab. If the app does not open in the browser, open a new tab and enter the URL from your run.

## How to use the data app

Once you started the application (container or your local environment), you should now see the data application run, generating 5 Instagram posts:

![martymcfly](https://user-images.githubusercontent.com/3411100/89596643-c2b12400-d825-11ea-979b-92649fb4f340.png)

If you use a local environment, you will notice that a `124M` folder is downloaded into the `models` folder. This is the 124M GPT-2 pre-trained model that will be used to generate captions.

## Pre-trained models used.

PGGAN: https://github.com/MSC-BUAA/Keras-progressive_growing_of_gans

GPT-2: https://github.com/minimaxir/gpt-2-simple

## Slides included in the repo

IG_Content_Generator_Slides.pptx
