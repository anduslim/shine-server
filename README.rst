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

*For Production*
     export DJANGO_SETTINGS_MODULE=data_server.settings.production
     export SECRET_KEY=dsfdf32#@$#43242$#d34fdsgfsd%#@*323rdcsc


*For Local*
     export DJANGO_SETTINGS_MODULE=data_server.settings.local
     export SECRET_KEY=dsf132sf24$&4fdsgfsd%#@*323rdcsc


Run command
===========
*Run REST API server*
  In your shine-server folder, run ``./manage.py runserver 0.0.0.0:80`` to run in local machine with port 80.

*Run demux service*
  In your shine-server folder, run ``./manage.py demux``.
  
Usage
=====
*Access REST APIs*
  
  To access the browsable API interface, go to your browser and open http://localhost/.

  You should see a list of API end-points.

A list of url end-points is listed below:
  1. ``/node/`` & ``/node/<node_id>``
  2. ``/deployment/`` & ``/deployment/<deployment_id>``
  3. ``/confseq/`` & ``/confseq/<confseq_id>``
  4. ``/sensormap/`` & ``/sensormap/<sensormap_id>``
  5. ``/sensor/`` & ``/sensor/<sensor_id>``
  6. ``/reading/`` & ``/reading/<reading_id>``
  7. ``/statistics/`` & ``/statistics/<statistics_id>``

  For each of the API end-point, the standard ``GET, POST, PUT, DELETE`` HTTP verbs apply.

*Admin panel access*

  You can access Django default admin panel through http://localhost/admin. Through the panel, you can interact with the database.

