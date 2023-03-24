import mongodb_conn
from datetime import datetime

def cust_onboard():
    print('''\n
            ----------------------- customer onboarding -----------------------------\n
            ----------------------- Submit your details -----------------------------\n''')
    onboarding_cust_name = input("Enter Name: ")
    onboarding_cust_dob = input("Enter DOB: ")
    onboarding_cust_mob = input("Enter Mobile number: ")
    onboarding_cust_email = input("Enter Email: ")
    onboarding_cust_address = input("Enter Address: ")
    onboarding_cust_acct_type = input("Enter account type (SBA/CAA/TDA): ")
    onboarding_cust_acct_sub_type = input("Enter account sub type (SBAP/CAAP/TDAP/SBAN/CAAN/TDAN): ")

    acct_num = mongodb_conn.gam_collection.find().sort("Account Number", -1).limit(1)[0]["Account Number"] + 1
    cust_id = mongodb_conn.gam_collection.find().sort("Customer ID", 1).limit(1)[0]["Customer ID"] - 1
    now = datetime.now()

    insert_these = [{'Customer Name':onboarding_cust_name,
                     'Customer DOB':onboarding_cust_dob,
                     'Account Number':acct_num, 
                     'Scheme Type':onboarding_cust_acct_type,
                     'Scheme Code': onboarding_cust_acct_sub_type,
                     'Mobile Number':onboarding_cust_mob,
                     'Email':onboarding_cust_email,
                     'Address':onboarding_cust_address,
                     'insert date':now,
                     'Customer ID':cust_id}]

    mongodb_conn.gam_collection.insert_many(insert_these)

cust_onboard()


    
    # return onboarding_cust_name, onboarding_cust_dob, onboarding_cust_mob, onboarding_cust_email, onboarding_cust_address, onboarding_cust_acct_type, onboarding_cust_acct_sub_type