# Cyberoam CLI Client
Cyberoam login cli client written with python

## Prerequisites

- Python 2.7+
- [Virtualenv](https://virtualenv.pypa.io/en/latest/)


## Usage

- Install the dependencies
```
pip install -r requirements.txt
```

- Run with the python

```
python loginClient.py
```

- Set the cron (Using virtualenv)

```
* * * * * source <path-to-virtual-env>/bin/activate && python <path-to-client>/loginClient.py >><log-out-path> 2>><log-err-path>
* * * * * sleep 30 && source <path-to-virtual-env>/bin/activate && python <path-to-client>/loginClient.py >><log-out-path> 2>><log-err-path>
```

NOTE: If you have mutiple version multiple versions of python then make sure you give the correct path to the python where you installed the dependencies.
