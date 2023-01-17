import json 
import os 
import mercadopago  
 
 
def lambda_handler(event, context): 
    sdk= mercadopago.SDK(os.environ["ACCESS_TOKEN"]) 
    bodyGet = event 
    
    payment_response = sdk.payment().create(bodyGet) 
    payment = payment_response["response"] 
     
   
 
    return { 
        'statusCode': 200, 
        'body': json.dumps(payment) 
    }