# tensorFlow

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
