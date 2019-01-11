# FYSet

## Description
Flask project setup with prepared set of plugins, commands and logic. 
Based on flask restplus and sqlalchemy.  
All API logic separated to units - single model with all included logic 
(controllers, serializers, validators).

## Installation
- git clone ...
- ...
- PROFIT

## Included modules and logic
- REST API with flask-restplus
- Database models with flask-sqlalchemy and flask-migrate
- Default Werkzeug ProfilerMiddleware and sqltap for debug
- Authorization with pyjwt and custom plugin
- Asynchronous tasks with celery

## Commands
Any command has --help page.
- create:account - new account record creation
- create:unit - new project part
