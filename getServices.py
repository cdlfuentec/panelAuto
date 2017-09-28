#!/usr/bin/python
import psycopg2
from configparser import ConfigParser
from configDB import config
import mysql.connector
import os
import shutil
import random
import commands
import re #Para sacar las iniciales
import random
import string
#Excel
import xlwt


def getServices():
    i = 1
    serviceID = []
    serviceName = []
    # read connection parameters
    params = config('database.ini','mysql')
    cnx = mysql.connector.connect(**params)
    #cnx = mysql.connector.connect(host= '10.254.254.112', user='root', passwd='t1l2cm3r', db='radius')
    cursor = cnx.cursor()


    servicesq = ("SELECT srvid,srvname FROM rm_services")

    cursor.execute(servicesq)
    wb = xlwt.Workbook()
    ws = wb.add_sheet('servicios',cell_overwrite_ok=True)

    for (srvid, srvname) in cursor:
       serviceID += [srvid]
       serviceName += [srvname]
       ws.write(i,1,srvid)
       ws.write(i,2,srvname)
       i += 1

    wb.save('services.xls')
    cursor.close()
    cnx.close()
    


if __name__ == '__main__':
    getServices()
