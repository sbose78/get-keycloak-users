import os
import json
import requests

SSO_SERVER = "https://" + os.environ['SSO_SERVER'] # sso.osio.org
SSO_TOKEN = os.environ['SSO_ADMIN_API_TOKEN'] # without the 'bearer '
APPROVED_USERS_FILE = "approved_users.json"

SSO_URL = SSO_SERVER + "/auth/admin/realms/fabric8/users?max=1000&search=redhat.com"
# A max value of 1000 is fine now, there are about 700 approved users now.
# unfortunately there is no api which returns a count :(

print "Fetching data from keycloak, this will take a while....."
RESPONSE = requests.get(SSO_URL, headers={'Authorization': "bearer %s"%(SSO_TOKEN)})
print "Server returned response code %d"%(RESPONSE.status_code)

if RESPONSE.status_code == 200:
    APPROVED_USERS = []
    print "Creating list of approved users.."
    JSON_USERS = json.loads(RESPONSE.text)
    for user in JSON_USERS:
        if 'attributes' in user.keys()  and 'approved' in user['attributes'].keys():
            APPROVED_USERS.append(user)

    print "Total approved users : %d"%(len(APPROVED_USERS))
    with open(APPROVED_USERS_FILE, 'w') as outfile:
        json.dump(APPROVED_USERS, outfile, sort_keys=True, indent=4, encoding='utf-8')
    print "Approved users' info written to %s "%(APPROVED_USERS_FILE)
