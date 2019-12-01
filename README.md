# ICEBOX MEMBERSHIP REWARDS PROGRAM

## Resource

**Members**

Attributes:

* name (string)
* email (string)
* phone (string)
* birthday (string) ( for now )
* zipcode (string)
* rewards level (string)

**Users**

Attributes:

* first name (string)
* last name (string)
* email (sqlite email format)
* password (string)

## Schema

```sql
CREATE TABLE members (name TEXT, email EMAIL, phone TEXT, birthday TEXT, zipcode TEXT, level TEXT );
```
```sql
CREATE TABLE users (fname TEXT, lname TEXT, email EMAIL, crypto TEXT);
```


## REST Endpoints

Name                           | Method | Path
-------------------------------|--------|------------------
Retrieve members collection    | GET    | /members
Retrieve members member        | GET    | /members/*\<id\>*
Create members member          | POST   | /members
Update members member          | PUT    | /members/*\<id\>*
Delete members member          | DELETE | /members/*\<id\>*


Name                           | Method | Path
-------------------------------|--------|------------------
Create users user              | POST   | /users
Login users user               | PUT    | /users/*\<id\>*
