# tensorFlow (python) - Beginner example models

TensorFlow is a framework of machine learning using data flow graphs. TensorFlow offers APIs binding to Python, C++ and Java. Operations in TensorFlow with Python API often requires the installation of NumPy, among others.

What is the core of Machine Learning and the path to Artificial Intelligence?
All examples written using python.

Problem
Teaching a Computer to reconcile what it sees and learn the same way a human does.

Traditional Programming
Data example - feed from a webcam.
The rules we write will act in the data to give us an answer.

So the core of building something that uses ML;
1. You get data that has patterns inherent in it.
2. Your neural network learns what those patterns are.

# Git clone or fork this project, cd into root and create a virtual envirnoment, (suggest using python3)
If you don't have python3 or not sure run the below.
<br/>Check -> "brew list | grep python"
<br/>Install -> "brew install python3"
<br/>`On your IDE check your python interpreter is set to python3 or higher`

Now you can run the following-> python3 -m venv .

# Running above command creates the target directory (creating any parent directories that don’t exist already) and places a pyvenv.cfg file in it with a home key pointing to the Python installation from which the command was run (a common name for the target directory is .venv).
You can read more about it here https://docs.python.org/3/library/venv.html

# Then activate this virtual environment

source bin/activate

# Install pip to install dependencies(tensorflow)

<br/>sudo easy_install pip 
<br/>(my version at this time is pip version 19.1.1)
<br/>"pip3 install tensorflow"
<br/>check => "pip3 show tensorflow"

# TroubleShooting

Errors I got but we can continue on until we need matplotlib which is library for creating static, animated, and interactive visuals.

<br/>ERROR: matplotlib 1.3.1 requires nose, which is not installed.
<br/>ERROR: matplotlib 1.3.1 requires tornado, which is not installed.

Issue with below
/usr/local/bin/python3.7: can't find '__main__' module in '/Users/dir/tensorFlow'
ImportError: No module named tensorflow

# Solution
run test-tf.py to check if TensorFlow is imported correctly.

python3 test-tf.py

# TensorBoard

Activate tensorFlow

source ~/tensorFlow/bin/activate

python --version

pip show tensorflow

pip install tensorboard

tensorboard --logdir=/Users/n0237580/tensorFlow/logs

# TroubleShoot
cd /Users/n0237580/tensorFlow/lib/python3.7/site-packages

cd tensorboard

python main.py --logdir=/Users/n0237580/tensorFlow/logs
