import json, boto3
from boto3.dynamodb.conditions import Key

### GET LAMBDA FUNCTION

def lambda_handler(event, context):
    # TODO implement
    
    TableName = "CustomerDetails"
    Primary_Column_Name = 'EmailID'
    Primary_Key = 'rr.k@gmail.com'
    
    DB =     boto3.resource('dynamodb')
    table = DB.Table(TableName)
    p_k = event.get('EmailID', None)

    if p_k is not None:
        response = table.get_item(
                    Key={
                        Primary_Column_Name:p_k
                    }
                )
    
        print(response["Item"])
    
    if len(response["Item"])>0:
        return response["Item"]
    
    return event

### POST LAMBDA FUNCTION

def lambda_handler(event, context):
    # TODO implement
    
    TableName = "CustomerDetails"
    Primary_Column_Name = 'EmailID'
    columns=["EmailID","FN", "LN"]
    
    DB =     boto3.resource('dynamodb')
    table = DB.Table(TableName)
    p_k = event.get('EmailID', None)
    f_n = event.get('FN', None)
    l_n = event.get('LN', None)
    
    
    response = table.put_item(
    Item={
        Primary_Column_Name:p_k,
        columns[1] :f_n,
        columns[2]: l_n
            }
        )
        
    print(response["ResponseMetadata"]["HTTPStatusCode"])
    return response["ResponseMetadata"]["HTTPStatusCode"]
