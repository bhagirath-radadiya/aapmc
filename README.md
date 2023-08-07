User Python3.10 for apmc.

Setup python 3.10.
```
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.10
python3.10 --version
```

Setup virtual environment.
Go to apmc directory.
```
# install virtual environment
python3.10 -m pip install virtualenv
python3.10 -m virtualenv venv

# activate environment.
source venv/bin/activate OR . venv/bin/activate
```

Install requirements package into virtual env.
```
pip install -r requirements.txt
```
