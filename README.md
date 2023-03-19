## Environment Setup

**db.sqlite** for now


## Project Details

- Frontend: Vue + Bootstrap.
- Backend : Django + Django Rest Framework + Djoser





### Frontend
go to wiki_frontend and do

```
npm install
```

to install all the packages.

After installing the package, do 

```
npm run serve
```

to start the website.

**Important**: 

Once starting the server, visit

```python
127.0.0.1:8000 # IMPORTANT
```

instead of `localhost:8000` (This will have some cross-origin problem).

### Backend
The .config folder is ignored because it contains my personal data for sending the email.
You should create a .config/settings.json and put things like 
```json
{
    "email_useranme":"xxx",
    "email_password":"xxx",
    "email_host":"xxx"
}

```

Also, see the email part for more information if you want to change sth.


- Database : mysql
- **db.sqlite** for now, will use mysql in the future

#### Databases:

- Users
- Entry

User (1) -> Entry (M)
