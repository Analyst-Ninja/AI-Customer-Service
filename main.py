# importing the dependencies
import mongodb_conn
import voice_input
import os
from datetime import datetime
import chatGPT
# 800789001
if __name__ == '__main__':
    # Step 1 : ------------------------- Showing Customer Details--------------------------------

    # 1.1 Taking the Customer ID from the customer
    cust_id_onboard = int(input("Enter your cust_id: \n"))

    # 1.2 Calling the gam_conn from mongodb_conn file to fetch customer details
    customer_details = mongodb_conn.gam_conn_find(cust_id_onboard)
    print("Customer ID : ", customer_details['Customer ID'])
    print("Name : ", customer_details['Customer Name'])
    print("Mobile No. : ", customer_details['Mobile Number'])
    print("Account Number : ", customer_details['Account Number'])
    print("Account Type : ", customer_details['Scheme Type'])

    # Step 2 : ------------------------- Taking the Voice Input from customer -------------------
    remark, audio_file = voice_input.voice_in()

    # Step 3 : --------------------Processing the Query Type with the help of chatGPT------------

    interaction_type = chatGPT.interaction_type(remark) 

    # Step 4 : ---------------------------Populating the interaction data in Interaction Table ------

    now = datetime.now()

    insert_these = [{'Customer ID':customer_details['Customer ID'],
                     'Customer Name':customer_details['Customer Name'], 
                     'Mobile Number':customer_details['Mobile Number'],
                     'Email':customer_details['Email'],
                     'Interaction Type' : interaction_type,
                     'voice_text' : remark,
                     'binary_audio' : audio_file,
                     'etl_insert_date':now
                     }]

    mongodb_conn.interaction_collection.insert_many(insert_these)

    
    
