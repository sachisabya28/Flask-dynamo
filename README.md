## _FLASK-DYNAMODB-LOCAL Integration_

We are trying here to integrate FLASK with Dynamodb Local(version)
useful to develop and test applications without accessing the DynamoDB Web Service

## IAM credentials
*** 
If you want to use a real AWS account, you'll need to set up your environment with the proper IAM credentials.
But here since we are using local Dynamodb version any fake credentials also works fine.
***

###### Setup AWS credentials locally using fake credentials . ######

```bash
aws configure
AWS Access Key ID [None]: AKIAIOSFODNN7EXAMPLE
AWS Secret Access Key [None]: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
Default region name [None]: us-west-2
Default output format [None]: json
```
###### Install dynamodb locally. ######

```bash
curl -O https://s3-us-west-2.amazonaws.com/dynamodb-local/dynamodb_local_latest.zip
$ unzip dynamodb_local_latest.zip
$ rm dynamodb_local_latest.zip
```
Then start your DynamoDB local instance:

```bash
$ java -Djava.library.path=./DynamoDBLocal_lib -jar DynamoDBLocal.jar -sharedDb

Initializing DynamoDB Local with the following configuration:
Port:	8000
InMemory:	false
DbPath:	null
SharedDb:	true
shouldDelayTransientStatuses:	false
CorsParams:	*
```

##### OR ####

##### Run DynamoDB using Docker ####
```bash
cd ./
docker-compose -f docker-compose.yaml up -d  
```
###### Install the devDependencies and start the server. ######

```bash
sh setup.sh
sh start_app.sh
```

###### Verify the deployment by navigating to your server address ######


```bash
http://127.0.0.1:5000/user/health
```

```bash
{
    "status": "healthy"
}
```
API endpoint (POST)

```bash
http://127.0.0.1:5000/user/token
```
POST BODY
```bash
{
    "username" :  "test@email.com"
}
```
Response 

```bash
{
    "message": "user created",
    "token": "5e977585cf9b4ea197fedee6de04f38a"
}
```

API endpoint (GET)

```bash
http://127.0.0.1:5000/user/token?username=test@email.com
```

Response 

```bash
{
    "credentails": {
        "token": "22b368e1403e498d9bce5bc61131560c",
        "username": "test@email.com"
    }
}
```

Data not present
```bash
{
    "message": "No user found"
}
```



## Technologies
***
A list of technologies used within the project:
Dynamodb - Database

Flask -  Web framework

BOTO3 : AWS SDK
***
