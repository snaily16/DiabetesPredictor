# DiabetesPredictor [![](https://img.shields.io/github/license/mashape/apistatus.svg)](LICENSE)
DiabetesPredictor is a web app to predict whether a user has diabetes or not based on their inputs. 

## Overview 
I have used Logistic Regression algorithm in this project to train the model - [train.py](https://github.com/snaily16/DiabetesPredictor/blob/master/train.py). Here, I have used pickle to save the trained model which is then used in [main.py](https://github.com/snaily16/DiabetesPredictor/blob/master/main.py) to predict the result.

## Dependencies
* Numpy
* Pandas
* Sklearn
* Flask

## Usage
Run this command : ```python3 main.py```

To view the data analysis open [this](https://github.com/snaily16/DiabetesPredictor/blob/master/Diabetes.ipynb) jupyter notebook 
