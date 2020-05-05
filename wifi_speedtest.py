'''
client Side:
    get ap_list array of (ssid, credential) from database
    for each ap in the ap_list:
        try to login
        if fail report to the backend server via API
        if success:
            speedtest
            write to file
            upload to the server via api in the format 

        testresult = {
            "secrete":"",
            "ssid": "",
            "ping": "",
            "download":"",
            "upload":""        
        }
        response = {
            "errorcode": 0,
            "message":""
        }

backend side:
    the api server will 
    1, as current data, write and update to the db each time get new data
    2, as history data, write and append into a file with filename. Categorized by ssid and date
    ssid_date.log, 
    e.g. ssid123_20200505.log, ssid123_20200506.log, ssid323_20200508.log

    the web server will use this file
     1, generate picture
     2, show current
    diaplay:
        ssid
        current status: ping , down, up
        history data as picture

API:
    get ssid/pwd and update the db.ap_list
    get the sampling period and update the db.config
'''


'''
get ap_list array of(ssid, credential) from database
for each ap in the ap_list:
    try to login
    if fail report to the backend server via API
    if success:
        speedtest
        upload to the server via api in the format        
    testresult = {
        "secrete": "",
        "ssid": "",
        "ping": "",
        "download": "",
        "upload": ""
    }
    
    response = {
        "errorcode": 0,
        "message": ""
    }
    # or
    response = {
        "errorcode": 1,
        "message": "error message"
    }
'''
def speedtest_sampling():
    # test data
    ap_list = ["ssid123","password123","ssid123","password123"]
    testresult = {
        "secrete": "",
        "ssid": "",
        "ping": "",
        "download": "",
        "upload": ""
    }

    ap_list= get_aplist()
    for ap in range(0, len(ap_list)):
        connection = connect(ap)
        if connection is True :
            testresult = get_test_data(connection)
            pass # upload to the server
        else: # connection fail
            # call the api to upload to the server the failure status
            pass
    pass


def get_test_data():
    pass


'''
Connect with the sside and password
ap = {ssid,pwd}
'''
def connect(ap):
    connect_success = True
    try:
        if connect_success is True
            return True
        else
            return False
    except:
        return False
    finally:
        # close connection
        pass


# get ap list from sqlite db
def get_aplist():
    pass


# write to the local file and upload to the server once a day
def writelog():
    pass


def main():
    # test1()
    speedtest_sampling()
if __name__ == '__main__':
    main()