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

## Schema

```sql
CREATE TABLE members (name TEXT, email TEXT, phone TEXT, birthday TEXT, zipcode TEXT, level TEXT );
```

## REST Endpoints

Name                           | Method | Path
-------------------------------|--------|------------------
Retrieve members collection    | GET    | /restaurants
Retrieve members member        | GET    | /restaurants/*\<id\>*
Create members member          | POST   | /restaurants
Update members member          | PUT    | /restaurants/*\<id\>*
Delete members member          | DELETE | /restaurants/*\<id\>*
