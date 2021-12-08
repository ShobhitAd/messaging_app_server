# Messaging app

## Setup

### Requirements

#### pip

```bash
sudo apt-get install python3-pip
```

#### virtualenv

```bash
sudo apt-get install python3-venv
```

#### sqlite3
```bash
sudo apt-get install sqlite3
```

### Setting up the virtual environment

#### Create virtual environment
```bash
python3 -m venv venv
```

#### Activate virtual environment
```bash
source venv/bin/activate
```

#### Install required packages
```bash
pip3 install --upgrade pip
pip3 install -r requirements.txt
```

### Creating/Reseting the database
```bash
sqlite3 < setupDB.sql
```

## Starting the server

#### Activate virtual environment
```bash
source venv/bin/activate
```

#### Start flask app(debug mode)
```bash
python3 app.py
```

#### Start flask app
```bash
gunicorn --worker-class eventlet -w 1 -b <hostname>:<port> -D app:flaskApp
```

<!-- ## [Optional] Setting up Auto Start on the Pi
Start the server when the pi starts -->

<!-- ```bash
# AUTO START SERVER  
cd ~/spur-server  
source venv/bin/activate  
   
who am i | grep tty  
LOCAL_LOGIN=$?
if [ $LOCAL_LOGIN -eq 0 ]; then # Not logged in using ssh  
   ./server_manager.py start  
fi
``` -->