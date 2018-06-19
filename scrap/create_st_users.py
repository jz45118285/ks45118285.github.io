# Script to read account list from a csv file and create appropriate users in the portal.
# Using Star Trek as basis of users. 

import csv
from arcgis.gis import *
import argparse

try:
    #region read cmd line args
    parser = argparse.ArgumentParser()
    parser.add_argument('url', help='Portal url of the form: https://portalname.domain.com/webadaptor')
    parser.add_argument('-u','--user', help='Administrator username', default='admin')
    parser.add_argument('-p','--password', help='Administrator password', default='x]984<ngb3!')
    parser.add_argument('-l', '--log', help='Path to log file', default='python_process.log')

    args = parser.parse_args()
    #endregion

    # Read the log file in append mode
    log_file = open(args.log, 'a')

    log_file.write("\n")
    log_file.write("=====================================================================\n")
    log_file.write("CREATING USER ACCOUNTS")

    # Connect to the GIS
    gis = GIS(args.url, args.user, args.password)

    # loop through and create users
    # default to 'org_viewer'
    RoleManager=gis.users.roles
    with open("users_trek.csv", 'r') as users_csv:
        users = csv.DictReader(users_csv)
        for user in users:
            try:
                log_file.write("\nCreating user: " + user['username'] + " " + user['role'] + " ## ")
                result = gis.users.create(username=user['username'],
                                          password=user['password'],
                                          firstname=user['Firstname'],
                                          lastname=user['Lastname'],
                                          email=user['email'],
                                          role='org_user')
                                          #role =user['role'])
                if result:
                    log_file.write("success  ##\n")
                    ## Assign custom role
                    log_file.write("\t Assigning role:  "+ user['role']+" ## ")
                    for r in RoleManager.all():
                        try:
                            if r.name == user['role']:
                                result.update_role(r)
                        except Exception as role_ex:
                            log_file.write("\n \t Cannot assign role to user", r.name, str(role_ex))

                    log_file.write("\t Adding to groups:  # ")
                    groups = user['groups']
                    group_list = groups.split(",")

                    # Search for the group
                    for g in group_list:
                        group_search = gis.groups.search(g)
                        if len(group_search) > 0:
                            try:
                                group = group_search[0]
                                groups_result = group.add_users([user['username']])
                                if len(groups_result['notAdded']) == 0:
                                    log_file.write(g + " # ")

                            except Exception as groups_ex:
                                log_file.write("\n \t Cannot add user to group ", g, str(groups_ex))
            except Exception as add_ex:
                log_file.write("\nCannot create user: " + user['username'])
                log_file.write("\n")
                log_file.write(str(add_ex))

    log_file.close()
    print("0")
except:
    print("1")
