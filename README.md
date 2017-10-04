# EngineP
Power the smart computation behind SmartP

# Install
Install using pip
```
pip install -r requirements.txt
```
# Run

Build cache:
```
python finfo.py
```
This will pre-load all price history to disk. For production there should be another module for caching.
```
python SmartP.py
```
# Deploy
Using gunicorn
http://gunicorn.org/
