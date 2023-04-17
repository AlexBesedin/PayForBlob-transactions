# PayForBlob-transactions-V1.0

## About the project:

This tool allows you to send a PayForBlob transaction in blockhain Celestia using the UI.


## Preparing for installation:
```sh
sudo apt install python3-pip python3-venv git -y
```
```sh
sudo apt-get update
sudo apt-get install iptables
```
## This command is used to add a rule to the INPUT chain of the iptables table that allows incoming TCP connections on port 8000.

```sh
sudo iptables -A INPUT -p tcp --dport 8000 -j ACCEPT
```

## Clone the repository: 

```sh
git clone git@github.com:AlexBesedin/PayForBlob-transactions-V1.0.git
```
## Go to the directory with the project. Activate the virtual environment and install the packages from requirements.txt

```sh
cd payforblob/
python3 -m venv venv
. venv/bin/activate
python -m pip install -r requirements.txt 
```
## Navigate to the folder where the file manage.py is located and run the project:
```sh
python manage.py runserver 0.0.0.0:8000
```

## Try this tools here:

- http://94.131.14.53:8000/submit_pfb/

![Название картинки](https://github.com/AlexBesedin/PayForBlob-transactions-V1.0/blob/de6d738377b172185b5ec20bedcc6bba0e2c483c/1.PNG)
