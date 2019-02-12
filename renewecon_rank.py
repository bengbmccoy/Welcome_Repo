'''
Author: Ben McCoy
Date started: 2019-02-12

This is the third script of the Renewecon project, this script will be the
so called "ranker" script.

This script will do the following:
- Take arguemnts from the command line as to what to do --> DONE
- Allow the user to rank an article through command line args --> DONE
- Accept or ammend an articles rank --> DONE

'''

import argparse
import pandas as pd
import numpy as np
import sys

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('id', type=int,
                        help='input the ID of an article to be ranked')
    parser.add_argument('rank', type=int,
                        help='input the rank of the article')
    args = parser.parse_args()

    url_database = fetch_url_database()
    # print url_database
    print "url_database collected"

    check, err_message = run_checks(args.id, args.rank, url_database)
    if check == True:
        pass
    else:
        print 'failed checks'
        print err_message
        sys.exit(1)

    for i in range(len(url_database.index)):
        if str(url_database.at[i,'Title'][-5:]) == str(args.id):
            url_database.at[i, 'Rank'] = args.rank
            print url_database.at[i,'Title'] + ' rank updated to ' + str(args.rank)

    # print url_database

def run_checks(argid, argrank, url_database):


    err_message = ''
    check = True
    if argid <= 0:
        check = False
        err_message = 'article id is below 0'
        return check, err_message
    if argrank < 0:
        check = False
        err_message = 'article rank is below 0'
        return check, err_message
    if argrank > 10:
        check = False
        err_message = 'article rank is above 10'
        return check, err_message

    check = False
    err_message = 'article does not exist'

    for i in range(len(url_database.index)):
        if str(url_database.at[i,'Title'][-5:]) == str(argid):
            check = True
            err_message = ''

    return check, err_message

def fetch_url_database():
    # fetches 'url_database.csv' as read and write and returns pandas db
    url_database = pd.read_csv('url_database.csv')
    return url_database

main()
