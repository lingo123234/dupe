from flask import Flask, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

myclient = MongoClient("mongodb+srv://mysteriouscoder:mysteriouscoder@cluster0.agkearu.mongodb.net/?retryWrites=true&w=majority")
db = myclient["DUDP"]
Collection = db["Repo"]


# Filtering the Quantities greater

@app.route('/search', methods=['GET', 'POST'])
def search():
    firstname = ""
    lastname = ""
    email = ""
    cntno = ""




    if (request.method == 'GET'):
        args = request.args
        first = args.get('firstname')
        last = args.get('lastname')
        emails = args.get('email')
        allcontact = args.get('allcontact')


        if first != None:
            firstname = {'$regex': first, '$options': 'i'}

        else:
            ns = "None"
            firstname = None if ns == 'None' else ns

        if last != None:
            lastname = {'$regex': last, '$options': 'i'}
        else:
            ns = "None"
            lastname = None if ns == 'None' else ns

        if emails != None:
            email = {'$regex': emails, '$options': 'i'}
        else:
            ns = "None"
            email = None if ns == 'None' else ns

        if allcontact != None:
            cntno = {'$regex': allcontact, '$options': 'i'}
        else:
            ns = "None"
            cntno = None if ns == 'None' else ns

        cursor = Collection.find({'$or': [{"FIRST_NAME": firstname}, {"LAST_NAME": lastname}, {"EMAIL":  email},
                                          {"HOME_PHONE": cntno}, {"CONTACT_NO": cntno},
                                          {"MOBILE_NO": cntno}, {"WORK_PHONE": cntno}]})
        #cursor = Collection.find({'$or': [{"FIRST_NAME": firstname}, {"LAST_NAME": lastname}, {"EMAIL":  email},
        #                                  {"HOME_PHONE": home_phone}, {"CONTACT_NO": contact_no},
        #                                  {"MOBILE_NO": mobile_no}, {"WORK_PHONE": work_phone}]}).explain()['executionStats']

        #return jsonify(cursor)

        First_Name = []
        Last_Name = []
        Emailss = []
        Home_phone = []
        Contact_No = []
        Mobile_No = []
        Work_Phone = []

        worth = len(list(cursor.clone()))
        print(worth)
        for record in cursor:
            print(record)
            getfirstname = record['FIRST_NAME']
            First_Name.append(getfirstname)
            getlastname = record['LAST_NAME']
            Last_Name.append(getlastname)
            getemail = record['EMAIL']
            Emailss.append(getemail)
            gethomephone = record['HOME_PHONE']
            if gethomephone != "":
                Home_phone.append(gethomephone)
            getcontactno = record['CONTACT_NO']
            if getcontactno != "":
                Contact_No.append(getcontactno)
            getmobileno = record['MOBILE_NO']
            if getmobileno != "":
                Mobile_No.append(getmobileno)
            getworkphone = record['WORK_PHONE']
            if getworkphone != "":
                Work_Phone.append(getworkphone)


        my_dict1 = {i: First_Name.count(i) for i in First_Name}
        print(my_dict1)
        my_dict2 = {i: Last_Name.count(i) for i in Last_Name}
        print(my_dict2)
        my_dict3 = {i: Emailss.count(i) for i in Emailss}
        print(my_dict3)
        my_dict4 = {i: Home_phone.count(i) for i in Home_phone}
        print(my_dict4)
        my_dict5 = {i: Contact_No.count(i) for i in Contact_No}
        print(my_dict5)
        my_dict6 = {i: Mobile_No.count(i) for i in Mobile_No}
        print(my_dict6)
        my_dict7 = {i: Work_Phone.count(i) for i in Work_Phone}
        print(my_dict7)

        if first != None:
            try:
                firstcount = my_dict1[first]
                firstpercentage = firstcount / worth * 100
                finalcount = str(firstcount)+ " " +str(firstpercentage)+"%"
            except:
                finalcount = 0
        else:
            finalcount = 0

        if last != None:
            try:
                lastcount = my_dict2[last]
                lastpercentage = lastcount / worth * 100
                lastcount = str(lastcount) + " " + str(lastpercentage) + "%"

            except:
                lastcount = 0
        else:
            lastcount = 0

        if emails != None:
            try:
                emailcount = my_dict3[emails]
                emailpercentage = emailcount / worth * 100
                emailcount = str(emailcount) + " " + str(emailpercentage) + "%"

            except:
                emailcount = 0
        else:
            emailcount = 0

        if cntno != None:
            try:
                homenocount = my_dict4[allcontact]
                homephonepercentage = homenocount / worth * 100
                homenocount = str(homenocount) + " " + str(homephonepercentage) + "%"

            except:
                homenocount = 0
        else:
            homenocount = 0


        if cntno != None:
            try:
                contactnocount = my_dict5[allcontact]
                contactnopercentage = contactnocount / worth * 100
                contactnocount = str(homenocount) + " " + str(homephonepercentage) + "%"

            except:
                contactnocount = 0
        else:
            contactnocount = 0

        if cntno != None:
            try:
                mobilenocount = my_dict6[allcontact]
                mobilenopercentage = mobilenocount / worth * 100
                mobilenocount = str(mobilenocount) + " " + str(mobilenopercentage) + "%"
                print(mobilenopercentage)
            except:
                mobilenocount = 0
        else:
            mobilenocount = 0


        if cntno != None:
            try:
                worknocount = my_dict7[allcontact]
                worknopercentage = worknocount / worth * 100
                mobilenocount = str(worknocount) + " " + str(worknopercentage) + "%"

            except:
                mobilenocount = 0
        else:
            mobilenocount = 0





        return jsonify([{"First_Name_Match": finalcount},{"Last_Name_Match": lastcount},
                        {"EmailID_Match": emailcount},{"HOME_PHONE_Match": homenocount}, {"CONTACT_NO_Match": contactnocount},
                        {"MOBILE_NO_Match": mobilenocount},{"WORK_PHONE_Match": mobilenocount} ,{"Total Records Found": worth}])

# driver function
if __name__ == '__main__':
    app.run()
