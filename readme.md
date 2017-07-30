### About
This is a very simple python script which fetches the first 1000 users from keycloak using the Admin API http://www.keycloak.org/docs-api/3.1/rest-api/index.html

### Usage

##### Set env variables

```
export SSO_SERVER=sso.osio.org
export SSO_ADMIN_API_TOKEN=eyJhbGciOiJSU__TOKEN___n1jd32kA
```


##### Run the script using python2.7

```
pip install -r requirements.txt
python get_approved_users.py
```

##### Sample output

```
$ python get_approved_users.py 
Fetching data from keycloak, this will take a while.....
Server returned response code 200
Creating list of approved users..
Total approved users : 268
```

### Drawbacks
The Users' API doesn't give the meta info of total number of users, 
that's why we get a `max` of 1000 users now which works for us since there are about 700+ users in the system now.
There is no upper limit for `max` users that I know of


