from twilio.rest import Client 
 
account_sid = 'ACc5e14469f00335894b1cc750542e9414' 
auth_token = '5ca1e043d3d0ed76bf9617522f82f435' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='+16787862764',  
                              body='heyy!!! this is crazy',      
                              to='+919481306259' 
                          ) 
 
print(message.sid)