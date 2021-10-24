import csv
import psycopg2

database_credentials = "dbname='415BigData' user='postgres' host='localhost' password='password'"

def parseAccessories():
    with open('Accessories.csv', mode='r') as file:
        csvFile = csv.reader(file)

        try:
            conn = psycopg2.connect(database_credentials)
        except:
            print('Unable to connect to the database!')
        cur = conn.cursor()

        count = 0
        lineNumber = 0
        for lines in csvFile:
            if count == 0:
                count = count + 1
                lineNumber = lineNumber + 1
                continue
            str1 = "INSERT INTO Accessories (name,variation,diy,buy,sell,color1,color2,uniquevalue,milesprice,source" \
                   ",sourcenotes,seasonalavailability,mannequinpiece,version,style,labelthemes,type,villagerequippable" \
                   ",catelog,filename,internalid,uniqueentryid) VALUES ("

            str2 = ""
            if "'" in lines[0]:
                newstr = lines[0].replace("'", "''")
                str2 += "'" + newstr + "',"
            else:
                str2 += "'" + str(lines[0]) + "',"

            str2 += "'" + str(lines[1]) + "',"
            if lines[2] == "No":
                str2 += "false,"
            else:
                str2 += "true,"
            str2 += "'" + str(lines[3]) + "',"
            str2 += str(lines[4]) + ","
            str2 += "'" + str(lines[5]) + "',"
            str2 += "'" + str(lines[6]) + "',"
            str2 += "'" + str(lines[7]) + "',"
            str2 += "'" + str(lines[8]) + "',"
            str2 += "'" + str(lines[9]) + "',"

            if "'" in lines[10]:
                newstr = lines[10].replace("'", "''")
                str2 += "'" + newstr + "',"
            else:
                str2 += "'" + str(lines[10]) + "',"

            str2 += "'" + str(lines[11]) + "',"

            if lines[12] == "No":
                str2 += "false,"
            else:
                str2 += "true,"

            str2 += "'" + str(lines[13]) + "',"
            str2 += "'" + str(lines[14]) + "',"
            str2 += "'" + str(lines[15]) + "',"
            str2 += "'" + str(lines[16]) + "',"

            if lines[17] == "No":
                str2 += "false,"
            else:
                str2 += "true,"

            if lines[18] == "Not for sale":
                str2 += "false,"
            else:
                str2 += "true,"
            str2 += "'" + str(lines[19]) + "',"
            str2 += str(lines[20]) + ","
            str2 += "'" + str(lines[21]) + "')"

            str3 = str1 + str2
            try:
                cur.execute(str3)
            except:
                print("Insert to accessories failed for: " + str(lineNumber) + " " + str3)

            conn.commit()
            lineNumber = lineNumber + 1

def parseAchievements():
    with open('achievements.csv', mode='r') as file:
        csvFile = csv.reader(file)

        try:
            conn = psycopg2.connect(database_credentials)
        except:
            print('Unable to connect to the database!')
        cur = conn.cursor()

        count = 0
        lineNumber = 0
        for lines in csvFile:
            if count == 0:
                count = count + 1
                lineNumber = lineNumber + 1
                continue
            str1 = "INSERT INTO Achievements (name,awardcriteria,number,internalid,internalname,internalcategory,numoftiers,tier1,tier2,tier3" \
                   ",tier4,tier5,rewardtier1,rewardtier2,rewardtier3,rewardtier4,rewardtier5,rewardtier6" \
                   ",sequential,version,uniqueentryid) VALUES ("

            str2 = ""
            if "'" in str(lines[0]):
                newstr = lines[0].replace("'", "''")
                str2 += "'" + newstr + "',"
            else:
                str2 += "'" + str(lines[0]) + "',"


            if "'" in str(lines[1]):
                newstr = lines[1].replace("'", "''")
                str2 += "'" + newstr + "',"
            else:
                str2 += "'" + str(lines[1]) + "',"

            str2 += str(lines[2]) + ","
            str2 += str(lines[3]) + ","
            str2 += "'" + str(lines[4]) + "',"
            str2 += "'" + str(lines[5]) + "',"
            str2 += str(lines[6]) + ","
            str2 += str(lines[7]) + ","
            str2 += str(lines[8]) + ","
            str2 += str(lines[9]) + ","
            str2 += str(lines[10]) + ","
            str2 += str(lines[11]) + ","
            str2 += str(lines[12]) + ","
            str2 += str(lines[13]) + ","
            str2 += str(lines[14]) + ","
            str2 += str(lines[15]) + ","
            str2 += str(lines[16]) + ","
            str2 += str(lines[17]) + ","
            if lines[18] == "Yes":
                str2 += "true,"
            else:
                str2 += "false,"

            str2 += "'" + str(lines[19]) + "',"
            str2 += "'" + str(lines[20]) + "')"


            str3 = str1 + str2
            try:
                cur.execute(str3)
            except:
                print("Insert to accessories failed for: " + str(lineNumber) + " " + str3)

            conn.commit()
            lineNumber = lineNumber + 1
    pass


        

        

