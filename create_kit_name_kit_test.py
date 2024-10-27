from sender_stand_request import
import sender_stand_request
import data

# Generate an account
def create_an_account_with_authoken():
  use_response = 
  sender_stand_request.post_new_user(data.user_body)
  return user_response.json()["authToken"]

  
