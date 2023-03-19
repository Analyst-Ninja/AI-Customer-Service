import pymongo

# making a connection to mongoDB
client = pymongo.MongoClient("mongodb://localhost:27017")
db = client['AICS_data']
gam_collection = db.collection['gen_acct_mast_table']
# function for showing the customer demographic details

# def gam_conn(cust_id):
#     gam_collection = db.collection['gen_acct_mast_table']
#     a=gam_collection.find_one({'Customer ID': cust_id})
#     return a

# object_id - mongo object_id
# id - cust_id 
# name - cust_name
# dob - cust_DOB
# email - cust_Email
# mob - cust_mobile
# acct_num - account number
# acct_type = acct_type
# acct_sub_type = acct_sub_type
# acct_bal = Account Balance
# address = Address
# etl_insert_date = insert date


def gam_conn(field,param):
    if param == 'id':
        field_name = 'Customer ID'
    elif param == 'name' :
        field_name = 'Customer Name'
    elif param == 'dob' :
        field_name = 'Customer DOB'
    elif param == 'email' :
        field_name = 'Email'
    elif param == 'mob' :
        field_name = 'Mobile Number'
    elif param == 'acct_num' :
        field_name = 'Account Number'
    elif param == 'acct_type' :
        field_name = 'Scheme Type'
    elif param == 'acct_sub_type' :
        field_name = 'Scheme Code'
    elif param == 'acct_bal' :
        field_name = 'Account Balance'
    elif param == 'address' :
        field_name = 'Address'
    elif param == 'etl_insert_date' :
        field_name = 'insert date'
    elif param == 'object_id' :
        field_name = '_id'
    a=gam_collection.find_one({ field_name : field})
    return a


def gam_conn_find(a):
    b=gam_collection.find_one({'Customer ID':a})
    return b



    
