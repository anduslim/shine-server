========================
Shine-Backend-Server-project
========================


This application is developed for ShineSeniors project. It is based off Django 1.6.10 and two-scoops of django template.

Key Objectives
==============
1. Demulplex data (which includes sensor readings, logs & statistics) from MQTT broker
2. REST API layer

Setup
=====
In your bashrc file, add the following environmental settings as needed 

```
## For production
export DJANGO_SETTINGS_MODULE=data_server.settings.production
export SECRET_KEY=dsfdf32#@$#43242$#d34fdsgfsd%#@*323rdcsc

## For local
export DJANGO_SETTINGS_MODULE=data_server.settings.local
export SECRET_KEY=dsf132sf24$&4fdsgfsd%#@*323rdcsc
```

Run command
===========
*Run REST API server*
  In your shine-server folder, run ``./manage.py runserver 0.0.0.0:80`` to run in local machine with port 80.

*Run demux service*
  In your shine-server folder, run ``./manage.py demux``.
  
Usage
=====

