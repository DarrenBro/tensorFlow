# tensorFlow

TensorFlow is a framework of machine learning using data flow graphs. TensorFlow offers APIs binding to Python, C++ and Java. Operations in TensorFlow with Python API often requires the installation of NumPy, among others.

What is the core of Machine Learning and the path to Artificial Intelligence?
All examples written using python.

Problem
Teaching a Computer to reconcile what it sees and learn the same way a human does.

Traditional Programming
Data example - feed from a webcam.
The rules we write will act in the data to give us an answer.

**Quick Note to setting up your IDE
Installing TensorFlow
mkdir tensorFlow
cd tensorFlow

Create a virtualenv

python3.7 -m venv .

sudo easy_install pip 

or pip install --upgrade pip (if you have pip already, my version at this time is pip version 19.1.1)

pip3 install tensorflow
check => pip3 show tensorflow



# TroubleShooting

Errors I got but we can continue on until we need matplotlib
A library for creating static, animated, and interactive visuals

ERROR: matplotlib 1.3.1 requires nose, which is not installed.
ERROR: matplotlib 1.3.1 requires tornado, which is not installed.

Issue with below
/usr/local/bin/python3.7: can't find '__main__' module in '/Users/dir/tensorFlow'
ImportError: No module named tensorflow

Solution
run test-tf.py to check if TensorFlow is imported correctly.
python3.7 test-tf.py








Flipping the diagram
Now we answers going in with the data and let the computer figure out the rules.
That’s machine learning.



Now we let the model figure out the ‘patterns’ as to what each image is.




So the core of building something that uses ML;
1. You get data that has patterns inherent in it.
2. Your neural network learns what those patterns are.

**Quick Note to setting up your IDE
Installing TensorFlow
mkdir TensorFlow
cd tensorFlow

// Create a virtualenv
python3.7 -m venv .

sudo easy_install pip 
or pip install --upgrade pip (if you have pip already, my version at this time is pip version 19.1.1)
pip3 install tensorflow

Errors I got but we can continue on until we need matplotlib
// A library for creating static, animated, and interactive visuals
ERROR: matplotlib 1.3.1 requires nose, which is not installed.
ERROR: matplotlib 1.3.1 requires tornado, which is not installed.

Setup On PyCharm CE IDE


Got this error when trying to import tensor flow in PyCharm

Fix
// Turn off z-scaler and run below off pycharm terminal
pip install tensorflow

Test With this small code snippet, make a new py file ’test.py’ in project root.
https://stackoverflow.com/questions/36998018/installing-tensorflow-on-pycharm-mac
import tensorflow as tf

node1 = tf.constant(3.0, tf.float32)
node2 = tf.constant(4.0)

print(node1, node2)
Add this run config

Run and I got below


EXAMPLE 1 - Y = 2X - 1
WHITEBOARD - Draw Keras Sequential Model
https://app.ziteboard.com/


Basically, an artificial neural network consists of an input layer where it receives inputs and output layer where it outputs. The hidden layer is a layer which is hidden in between input and output layers since the output of one layer is the input of another layer.

The number of hidden neurons should be between the size of the input layer and the size of the output layer. The number of hidden neurons should be 2/3 the size of the input layer, plus the size of the output layer. The number of hidden neurons should be less than twice the size of the input layer.


TensorBoard

Activate tensorFlow
source ~/tensorFlow/bin/activate
python --version
pip show tensorflow
pip install tensorboard
tensorboard --logdir=/Users/n0237580/tensorFlow/logs

TroubleShoot
cd /Users/n0237580/tensorFlow/lib/python3.7/site-packages
cd tensorboard
python main.py --logdir=/Users/n0237580/tensorFlow/logs






