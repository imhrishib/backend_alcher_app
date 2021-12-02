# Base URL: `http://localhost:8000`

# Register
Registering a new user

```http
POST /auth/register
```

**Method** : `POST`

**Auth required** : NO

**Data constraints**

```json
{
    "email": "[valid email address]",
    "password": "[password in plain text]"
}
```

**Data example**

```json
{
    "email": "abcd@gmail.com",
    "password": "abcd1234"
}
```
**Response example**

```json
{
  "success": true
}
```



# Login


```http
POST /auth/login
```
**Method** : `POST`

**Auth required** : NO

**Data constraints**

```json
{
    "email": "[valid email address]",
    "password": "[password in plain text]"
}
```

**Data example**

```json
{
    "email": "abcd@example.com",
    "password": "abcd1234"
}
```

**Response example**

```json
{
  "success": true,
  "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiYjJiZTc1NWUtOGI0NS00MjNiLThmN2QtZDUyMTVjYzI4ZjU2IiwidXNlcm5hbWUiOiJzb3VtYWRpcGRhczE4QHlhaG9vLmNvbSIsImV4cCI6MTYzODE5Mzk1OCwiZW1haWwiOiJzb3VtYWRpcGRhczE4QHlhaG9vLmNvbSJ9.rd6PTgdrr67xo8I4YVVfAfsYJOY_Mc6zlIlil1kp7zw",
  "data": {
    "id": "b2be755e-8b45-423b-8f7d-d5215cc28f56",
    "password": "pbkdf2_sha256$216000$DbEeAE8pbt8q$JYdhgrbmqUGstIEJMcMzYZB/9rqMogvdtCozDN1xxcQ=",
    "last_login": "2021-11-29T13:47:38.580942Z",
    "is_superuser": true,
    "email": "abcd@example.com",
    "username": "superuser",
    "fullname": "",
    "phone": "",
    "date_joined": "2021-11-29T12:02:45.314870Z",
    "provider": "email",
    "about": "",
    "is_staff": true,
    "is_active": true,
    "groups": [],
    "user_permissions": []
  }
}
```




# Profile

### To get the profile details

```http
GET /auth/profile
```

**Method** : `GET`

**Auth required** : YES (include the bearer token in header of the request)

**Success Response example**

```json
{
  "success": true,
  "detail": "User profile fetched successfully",
  "data": {
    "id": "b2be755e-8b45-423b-8f7d-d5215cc28f56",
    "password": "pbkdf2_sha256$216000$DbEeAE8pbt8q$JYdhgrbmqUGstIEJMcMzYZB/9rqMogvdtCozDN1xxcQ=",
    "last_login": "2021-12-01T18:18:34.901759Z",
    "is_superuser": true,
    "email": "abcd@example.com",
    "username": "superuser",
    "fullname": "Abcd",
    "phone": "1234567890",
    "date_joined": "2021-11-29T12:02:45.314870Z",
    "provider": "email",
    "about": "",
    "is_staff": true,
    "is_active": true,
    "groups": [],
    "user_permissions": []
  }
}
```

**Error Response example**

```json
{
  "detail": "Authentication credentials were not provided."
}
```

### To update profile
#### Only full name, email and phone number can be updated with this API
```http
PUT /auth/profile
```
**Method** : `PUT`

**Auth required** : YES

**Data constraints**

```json
{
    "fullname": "[valid string]"
    "email": "[valid email address]",
    "phone": "[valid 10 charcter phone number]"
}
```

**Data example**

```json
{
    "fullname":"Abcd",
    "email":"abcd@example.com",
    "phone":"1234567890"
}
```

**Response example**

```json
{
  "success": true
}
```


