## GCP Create a Portfolio Template
A simple portfolio template, that allows you to deploy onto the Google Cloud Platform with App Engine, for free.

[View Presentation](https://docs.google.com/presentation/d/1IUf3iY52FM8xrJGTGlLyq_ar2ltO3PJ4fKuhz7CzCog/edit?usp=sharing)
[View Demo](https://createportfolio-215022.appspot.com/)
## Screenshots
![](https://github.com/robeartoe/GCPCreatePortfolio/tree/master/images/myPortfolio.png)
## Getting Started
Setup an account for the Google Cloud Platform [here](https://cloud.google.com/free/). It's free, and you can get $300 of free credit for 12 months.
## Prerequisites
* Python must be installed on your system.
* Virtualenv is **highly** recommended though not required.
## Installing
It is best to either git clone, or download this project as a zip file, and extract to a location of your choice on your system. Then open a terminal in the folder location.
```bash
#Optional: If virualenv is installed
virtualenv NAME_OF_VENV
source NAME_OF_VENV/bin/activate 

pip install -r requirements.txt
```
## Local Development:
Local development is ready to go right out of the box. Any changes that is made will be updated every time the page is refreshed.
```bash
python main.py
```
## Deployment
* Setup GCP SDK: Information can be found [here](https://cloud.google.com/sdk/docs/downloads-interactive#linux).

    ```bash
    #Install GCP SDK
    curl https://sdk.cloud.google.com | bash
    
    #Restart Terminal:
    exec -l $SHELL
    
    #Initialize GCP:
    gcloud init
    
    #Create Project
    gcloud projects create PICK_A_NAME
    
    #Create an App Engine
    gcloud app create
    
    #Deploy App Engine
    gcloud app deploy
    ```

## Built With
Google App Engine, Flask, HTML, CSS, Materialize