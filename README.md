# Cyberoam CLI Client
Opensource Cyberoam login cli client written with python. Cross compatible with Operating Systems.

## Prerequisites

- Python 2.7+
- [Virtualenv](https://virtualenv.pypa.io/en/latest/) (Optional)


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

OR (If source does not work)

```
* * * * * . <path-to-virtual-env>/bin/activate && python <path-to-client>/loginClient.py >><log-out-path> 2>><log-err-path>
* * * * * sleep 30 && . <path-to-virtual-env>/bin/activate && python <path-to-client>/loginClient.py >><log-out-path> 2>><log-err-path>
```

NOTE: If you have mutiple version multiple versions of python then make sure you give the correct path to the python where you installed the dependencies.
