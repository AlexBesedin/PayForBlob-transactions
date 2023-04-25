# PayForBlob-transactions-V1.0

## About the project:

This utility allows you to send a PayForBlob transaction in blockchain Celestia using the UI.


# Preparing for installation:
### Make sure you have the apt-transport-https package installed on your machine and add the Docker GPG key:

```sh
sudo apt-get update
sudo apt-get install apt-transport-https ca-certificates curl gnupg lsb-release
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
```

###  Add the Docker repository to your system:

```sh
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```
###  Update the package index and install Docker:

```sh
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io
```

###  Download the latest version of Docker Compose:


```sh
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```
###  Add permissions to execute the file:

```sh
sudo chmod +x /usr/local/bin/docker-compose
```
###  Verify that Docker Compose is successfully installed by running the command:

```sh
docker-compose --version
```

###  Clone the repository: 

```sh
git clone git@github.com:AlexBesedin/PayForBlob-transactions.git
```
###  Create a file containing virtual environment variables (.env):

```sh
cd PayForBlob-transactions
touch .env
```

###  Generate Django Secret Key here: https://djecrety.ir/

```sh
SECRET_KEY=#el+4fri51pvz%=5h1cc!e($jca^y9e@fh(%rx$tl%u&^u7sv=
```

###  Run the application in containers from the infra/ directory

```sh
sudo docker-compose up -d --build
```

### Collect static:
```sh
sudo docker-compose exec backend python3 manage.py collectstatic --no-input
```

### Try this tools here:

DEMO: http://94.131.14.53/submit_pfb/

![Название картинки](https://github.com/AlexBesedin/PayForBlob-transactions-V1.0/blob/de6d738377b172185b5ec20bedcc6bba0e2c483c/1.PNG)
