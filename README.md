# Demonstration
https://www.youtube.com/watch?v=GL6F0wNYZys

# Setup

## Virtual Environment and Libraries
Make sure you have Python installed on your computer! First, make a virtual environment for this project that will hold all the necessary packages and libraries needed. You can learn more about how to create and activate a virtual environment here:
https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/

Once you have your virtual environment running, make sure to install all the right packages and libraries for the project. You can do this by navigating to the github repo on a command line or terminal and entering the following command:
`python -m pip install -r requirements-cuda.txt`
or alternatively if you do NOT have cuda installed on your computer (or if you do not own a computer with a NVIDIA GPU):
`python -m pip install -r requirements.txt`

## Dataset and Models
The dataset is too big to be stored on Github (it is 7GB!), so you need to download the dataset locally yourself. The dataset can be found here:
https://www.kaggle.com/datasets/ubitquitin/geolocation-geoguessr-images-50k

Make sure you have a Kaggle account in order to download the dataset. Once you download the dataset, you should get an `archive.zip` file. In your local git repo, create a `data` folder and unzip the contents of the `archive.zip` into this `data` directory. Make sure that the data is structured like this: `data/archive/compressed_dataset` where folders containing country images are found in the `compressed_dataset` directory.

The trained model weights can be found in the Google Drive. Make sure to create a `models` folder inside the github repo and store all your trained models in that folder.
