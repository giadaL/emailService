# emailService

SMTP microservice. 
This is part of a python study project composed by two microservices : emailService , TemplateService.

EmailService sends an email to a receiver with message created from template provided.
Templates will be stored in a PostgreSQL database and will be managed by another microservice (TODO)

## Used technologies

* Python 3.10
* pip3
* FastApi
* smtplib
* postgres
* psycopg2
___
## Run application

Create directory called `config/` and into it create two JSON file: `smtp_config.json` and `postgres_config.json` 
like this:

* smtp_config.json:
```json
{
  "host": "hostname",
  "port": 587, 
  "userName": "my@email.com",
  "password": "myPassword"

}
```
The port number is the port of smtp host and protocol chosen. 

With gmail smtp server and the ssl protocol the port to use is 587.

__
* postgres_config.json:
```json
{
  "host": "hostname",
  "database": "databaseName",
  "user": "username",
  "password": "dbPassword"
}
```
__

Once you have the config files :
```commandline
> cd src/
> uvicorn main:app --reload
```
The server will start on port **8000** and it comunicate with a database on postrgres default port.

___

## Exposed API

### */send*
Method: POST

###### Request body
```json
{
  "to": "string",
  "template_name": "string"
}
```
___

*Author: Giada Legname*