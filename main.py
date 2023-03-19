# importing the dependencies
import mongodb_conn
import voice_input
import os
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
    
    # Step 3 : 
    
