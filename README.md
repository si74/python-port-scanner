# python-port-scanner
Creating a port scanner in Python! 

# Create virtual environment and activate it

```
python3 -mvenv --prompt scanner .venv
.venv/bin/pip -q install -U pip setuptools wheel
.venv/bin/pip -q install -r requirements.txt

TODO(sneha): has no setup.py
.venv/bin/pip -q install -e ~/sites/python-port-scanner

source /Users/singuva/sites/python-port-scanner/.venv/bin/activate
```

# To run as a console script 

# Next steps (TODO)

1. Get this working as a package CLI tool in python - https://pybit.es/articles/how-to-package-and-deploy-cli-apps/

## References

Socket Programming: 
- http://pymotw.com/2/socket/tcp.html
- https://blog.cloudflare.com/how-to-stop-running-out-of-ephemeral-ports-and-start-to-love-long-lived-connections/

Configuring packages: 
- 