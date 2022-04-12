# emailService

SMTP microservice. 
This is a python study project composed by two microservices : emailService , TemplateService.

This emailService sends an email to a receiver with message created from template provided.
Templates are stored in a PostgreSQL database and are managed by an other microservice.
(TODO)

## Used technologies

* Python3
* pip3
* FastApi
* smtplib
___
## Run application
```commandline
> cd src/
> uvicorn main:app --reload
```
The server will start on port **8000** and it comunicate with a database on postrgres default port.

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