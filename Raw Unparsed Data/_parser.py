import csv
import psycopg2

database_credentials = "dbname='415BigData' user='postgres' host='localhost' password='password'"

def parseAccessories():
    with open('Accessories.csv', mode='r', encoding="utf8") as file:
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
    with open('achievements.csv', mode='r', encoding="utf8") as file:
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

def parseArt():
    with open('art.csv', mode='r', encoding="utf8") as file:
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
            str1 = "INSERT INTO Art (name,Genuine,category,buy,sell,color1,color2,size,realartworktitle" \
                   ",artist,MuseumDescription,Source,SourceNotes,Version,HHAConcept1,HHAConcept2,HHASeries" \
                   ",HHASet,Interact,Tag,SpeakerType,LightingType,Catalog,Filename,InternalID,UniqueEntryID) VALUES ("

            str2 = ""
            str2 += "'" + str(lines[0]) + "',"
            if "No" in str(lines[1]):
                str2 += "false" + ","
            else:
                str2 += "true" + ","
            str2 += "'" + str(lines[2]) + "',"
            str2 += "'" + str(lines[3]) + "',"
            str2 += str(lines[4]) + ","
            str2 += "'" + str(lines[5]) + "',"
            str2 += "'" + str(lines[6]) + "',"
            str2 += "'" + str(lines[7]) + "',"
            str2 += "'" + str(lines[8]) + "',"
            str2 += "'" + str(lines[9]) + "',"

            if "'" in str(lines[10]):
                newstr = lines[10].replace("'", "''")
                str2 += "'" + newstr + "',"
            else:
                str2 += "'" + str(lines[10]) + "',"

            if "'" in str(lines[11]):
                newstr = lines[11].replace("'", "''")
                str2 += "'" + newstr + "',"
            else:
                str2 += "'" + str(lines[11]) + "',"

            if "'" in str(lines[12]):
                newstr = lines[12].replace("'", "''")
                str2 += "'" + newstr + "',"
            else:
                str2 += "'" + str(lines[12]) + "',"

            str2 += "'" + str(lines[13]) + "',"
            str2 += "'" + str(lines[14]) + "',"
            str2 += "'" + str(lines[15]) + "',"
            str2 += "'" + str(lines[16]) + "',"
            str2 += "'" + str(lines[17]) + "',"

            if "No" in str(lines[1]):
                str2 += "false" + ","
            else:
                str2 += "true" + ","

            str2 += "'" + str(lines[19]) + "',"
            str2 += "'" + str(lines[20]) + "',"
            str2 += "'" + str(lines[21]) + "',"
            str2 += "'" + str(lines[22]) + "',"
            str2 += "'" + str(lines[23]) + "',"
            str2 += str(lines[24]) + ","
            str2 += "'" + str(lines[25]) + "')"



            str3 = str1 + str2
            try:
                cur.execute(str3)
            except:
                print("Insert to accessories failed for: " + str(lineNumber) + " " + str3)

            conn.commit()
            lineNumber = lineNumber + 1
    pass



def parseBags():
    with open('bags.csv', mode='r', encoding="utf8") as file:
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
            str1 = "INSERT INTO Bags (name,Variation,DIY,buy,sell,color1,color2,size,MilesPrice,Source" \
                   ",SourceNotes,SeasonalAvailability,Version,Style,LabelThemes,VillagerEquippable,Catalog,Filename" \
                   ",InternalID,UniqueEntryID) VALUES ("

            str2 = ""

            if "'" in str(lines[0]):
                newstr = lines[0].replace("'", "''")
                str2 += "'" + newstr + "',"
            else:
                str2 += "'" + str(lines[0]) + "',"
            str2 += "'" + str(lines[1]) + "',"

            if "Yes" in str(lines[2]):
                str2 += "true" + ","
            else:
                str2 += "false" + ","


            str2 += "'" + str(lines[3]) + "',"
            str2 += str(lines[4]) + ","
            str2 += "'" + str(lines[5]) + "',"
            str2 += "'" + str(lines[6]) + "',"
            str2 += "'" + str(lines[7]) + "',"
            str2 += "'" + str(lines[8]) + "',"
            str2 += "'" + str(lines[9]) + "',"
            str2 += "'" + str(lines[10]) + "',"
            str2 += "'" + str(lines[11]) + "',"
            str2 += "'" + str(lines[12]) + "',"
            str2 += "'" + str(lines[13]) + "',"
            str2 += "'" + str(lines[14]) + "',"

            if "No" in str(lines[15]):
                str2 += "false" + ","
            else:
                str2 += "true" + ","

            str2 += "'" + str(lines[16]) + "',"
            str2 += "'" + str(lines[17]) + "',"
            str2 += str(lines[18]) + ","
            str2 += "'" + str(lines[19]) + "')"


            str3 = str1 + str2
            try:
                cur.execute(str3)
            except:
                print("Insert to accessories failed for: " + str(lineNumber) + " " + str3)

            conn.commit()
            lineNumber = lineNumber + 1
    pass

def parseBottoms():
    with open('bottoms.csv', mode='r', encoding="utf8") as file:
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
            str1 = "INSERT INTO Bottoms (name,Variation,DIY,buy,sell,color1,color2,size,Source" \
                   ",SourceNotes,SeasonalAvailability,MannequinPiece,Version,Style,LabelThemes,VillagerEquippable,Catalog,Filename" \
                   ",InternalID,UniqueEntryID) VALUES ("

            str2 = ""
            if "'" in str(lines[0]):
                newstr = lines[0].replace("'", "''")
                str2 += "'" + newstr + "',"
            else:
                str2 += "'" + str(lines[0]) + "',"
            str2 += "'" + str(lines[1]) + "',"

            if "Yes" in str(lines[2]):
                str2 += "true" + ","
            else:
                str2 += "false" + ","


            str2 += "'" + str(lines[3]) + "',"
            str2 += str(lines[4]) + ","
            str2 += "'" + str(lines[5]) + "',"
            str2 += "'" + str(lines[6]) + "',"
            str2 += "'" + str(lines[7]) + "',"
            str2 += "'" + str(lines[8]) + "',"

            if "'" in str(lines[9]):
                newstr = lines[9].replace("'", "''")
                str2 += "'" + newstr + "',"
            else:
                str2 += "'" + str(lines[9]) + "',"

            str2 += "'" + str(lines[10]) + "',"
            str2 += "'" + str(lines[11]) + "',"
            str2 += "'" + str(lines[12]) + "',"
            str2 += "'" + str(lines[13]) + "',"
            str2 += "'" + str(lines[14]) + "',"
            str2 += "'" + str(lines[15]) + "',"
            str2 += "'" + str(lines[16]) + "',"

            if "No" in str(lines[17]):
                str2 += "false" + ","
            else:
                str2 += "true" + ","

            str2 += "'" + str(lines[18]) + "',"
            str2 += "'" + str(lines[19]) + "')"

            str3 = str1 + str2
            try:
                cur.execute(str3)
            except:
                print("Insert to accessories failed for: " + str(lineNumber) + " " + str3)

            conn.commit()
            lineNumber = lineNumber + 1
    pass

def parseConstruction():
    with open('construction.csv', mode='r', encoding="utf8") as file:
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
            str1 = "INSERT INTO Construction (name,buy,catalog,Source" \
                   ",filename,version,UniqueEntryID) VALUES ("

            str2 = ""

            str2  += "'" + str(lines[0]) + "',"
            str2 += str(lines[1]) + ","
            str2 += "'" + str(lines[2]) + "',"
            str2 += "'" + str(lines[3]) + "',"
            str2 += "'" + str(lines[4]) + "',"
            str2 += "'" + str(lines[5]) + "',"
            str2 += "'" + str(lines[6]) + "')"

            str3 = str1 + str2
            try:
                cur.execute(str3)
            except:
                print("Insert to accessories failed for: " + str(lineNumber) + " " + str3)

            conn.commit()
            lineNumber = lineNumber + 1
    pass

def parseDressUp():
    with open('dress-up.csv', mode='r', encoding="utf8") as file:
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
            str1 = "INSERT INTO DressUp (name,Variation,DIY,Buy" \
                   ",Sell,Color1,Color2,Size,Source,SourceNotes,SeasonalAvailability" \
                   ",MannequinPiece,Version,Style,LabelThemes,VillagerEquippable,Catalog" \
                   ",PrimaryShape,SecondaryShape,Filename,InternalID,UniqueEntryID) VALUES ("

            str2 = ""

            if "'" in str(lines[0]):
                newstr = lines[0].replace("'", "''")
                str2 += "'" + newstr + "',"
            else:
                str2 += "'" + str(lines[0]) + "',"
            str2 += "'" + str(lines[1]) + "',"
            str2 += "'" + str(lines[2]) + "'," #bool
            str2 += "'" + str(lines[3]) + "',"
            str2 += "'" + str(lines[4]) + "'," #int
            str2 += "'" + str(lines[5]) + "',"
            str2 += "'" + str(lines[6]) + "',"
            str2 += "'" + str(lines[7]) + "',"
            str2 += "'" + str(lines[8]) + "',"

            if "'" in str(lines[9]):
                newstr = lines[9].replace("'", "''")
                str2 += "'" + newstr + "',"
            else:
                str2 += "'" + str(lines[9]) + "',"

            str2 += "'" + str(lines[10]) + "',"
            str2 += "'" + str(lines[11]) + "'," #bool
            str2 += "'" + str(lines[12]) + "',"
            str2 += "'" + str(lines[13]) + "',"
            str2 += "'" + str(lines[14]) + "',"
            str2 += "'" + str(lines[15]) + "'," #bool
            str2 += "'" + str(lines[16]) + "',"
            str2 += "'" + str(lines[17]) + "',"
            str2 += "'" + str(lines[18]) + "',"
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
    pass

def parseFencing():
    with open('fencing.csv', mode='r', encoding="utf8") as file:
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
            str1 = "INSERT INTO Fencing (name,DIY,StackSize,Buy" \
                   ",Sell,Source,SourceNotes,Version,Filename,InternalID,UniqueEntryID) VALUES ("

            str2 = ""
            str2 += "'" + str(lines[0]) + "',"

            if "Yes" in str(lines[1]):
                str2 += "true" + ","
            else:
                str2 += "false" + ","

            str2 += str(lines[2]) + ","
            str2 += "'" + str(lines[3]) + "',"
            str2 += str(lines[4]) + ","
            str2 += "'" + str(lines[5]) + "',"
            str2 += "'" + str(lines[6]) + "',"
            str2 += "'" + str(lines[7]) + "',"
            str2 += "'" + str(lines[8]) + "',"
            str2 += str(lines[9]) + ","
            str2 += "'" + str(lines[10]) + "')"



            str3 = str1 + str2
            try:
                cur.execute(str3)
            except:
                print("Insert to accessories failed for: " + str(lineNumber) + " " + str3)

            conn.commit()
            lineNumber = lineNumber + 1
    pass

def parseFish():
    with open('fish.csv', mode='r', encoding="utf8") as file:
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
            str1 = "INSERT INTO Fish (Number,Name,Sell,Where_" \
                   ",Shadow,TotalCatchesToUnlock,SpawnRates,RainSnow,NHJan,NHFeb,NHMar" \
                   ",NHApr,NHMay,NHJun,NHJul,NHAug,NHSep,NHOct,NHNov,NHDec,SHJan,SHFeb" \
                   ",SHMar,SHApr,SHMay,SHJun,SHJul,SHAug,SHSep,SHOct,SHNov,SHDec,Color1" \
                   ",Color2,Size,LightingType,IconFileName,CritterpediaFilename,Furniture" \
                   ",InternalID,UniqueEntryID) VALUES ("

            str2 = ""
            str2 += str(lines[0]) + ","
            str2 += "'" + str(lines[1]) + "',"
            str2 += str(lines[2]) + ","
            str2 += "'" + str(lines[3]) + "',"
            str2 += "'" + str(lines[4]) + "',"
            str2 += str(lines[5]) + ","
            str2 += "'" + str(lines[6]) + "',"
            str2 += "'" + str(lines[7]) + "'," #bool
            str2 += "'" + str(lines[8]) + "',"
            str2 += "'" + str(lines[9]) + "',"
            str2 += "'" + str(lines[10]) + "',"
            str2 += "'" + str(lines[11]) + "',"
            str2 += "'" + str(lines[12]) + "',"
            str2 += "'" + str(lines[13]) + "',"
            str2 += "'" + str(lines[14]) + "',"
            str2 += "'" + str(lines[15]) + "',"
            str2 += "'" + str(lines[16]) + "',"
            str2 += "'" + str(lines[17]) + "',"
            str2 += "'" + str(lines[18]) + "',"
            str2 += "'" + str(lines[19]) + "',"
            str2 += "'" + str(lines[20]) + "',"
            str2 += "'" + str(lines[21]) + "',"
            str2 += "'" + str(lines[22]) + "',"
            str2 += "'" + str(lines[23]) + "',"
            str2 += "'" + str(lines[24]) + "',"
            str2 += "'" + str(lines[25]) + "',"
            str2 += "'" + str(lines[26]) + "',"
            str2 += "'" + str(lines[27]) + "',"
            str2 += "'" + str(lines[28]) + "',"
            str2 += "'" + str(lines[29]) + "',"
            str2 += "'" + str(lines[30]) + "',"
            str2 += "'" + str(lines[31]) + "',"
            str2 += "'" + str(lines[32]) + "',"
            str2 += "'" + str(lines[33]) + "',"
            str2 += "'" + str(lines[34]) + "',"
            str2 += "'" + str(lines[35]) + "',"
            str2 += "'" + str(lines[36]) + "',"
            str2 += "'" + str(lines[37]) + "',"
            str2 += "'" + str(lines[38]) + "',"
            str2 += str(lines[39]) + ","
            str2 += "'" + str(lines[40]) + "')"

            str3 = str1 + str2
            try:
                cur.execute(str3)
            except:
                print("Insert to accessories failed for: " + str(lineNumber) + " " + str3)

            conn.commit()
            lineNumber = lineNumber + 1
    pass

def parseFloors():
    with open('floors.csv', mode='r', encoding="utf8") as file:
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
            str1 = "INSERT INTO Floors (Name,VFX,DIY,Buy,Sell,Color1,Color2,MilesPrice,Source" \
                   ",SourceNotes,Version,HHAConcept1,HHAConcept2,HHASeries,Tag,Catalog,Filename" \
                   ",InternalID,UniqueEntryID)" \
                   "VALUES ("

            str2 = ""

            if "'" in str(lines[0]):
                newstr = lines[0].replace("'", "''")
                str2 += "'" + newstr + "',"
            else:
                str2 += "'" + str(lines[0]) + "',"

            if "No" in str(lines[1]):
                str2 += "false" + ","
            else:
                str2 += "true" + ","

            if "No" in str(lines[2]):
                str2 += "false" + ","
            else:
                str2 += "true" + ","

            str2 += "'" + str(lines[3]) + "',"
            str2 += str(lines[4]) + ","
            str2 += "'" + str(lines[5]) + "',"
            str2 += "'" + str(lines[6]) + "',"
            str2 += "'" + str(lines[7]) + "',"

            if "'" in str(lines[8]):
                newstr = lines[8].replace("'", "''")
                str2 += "'" + newstr + "',"
            else:
                str2 += "'" + str(lines[8]) + "',"

            str2 += "'" + str(lines[9]) + "',"
            str2 += "'" + str(lines[10]) + "',"
            if "'" in str(lines[11]):
                newstr = lines[11].replace("'", "''")
                str2 += "'" + newstr + "',"
            else:
                str2 += "'" + str(lines[11]) + "',"

            if "'" in str(lines[12]):
                newstr = lines[12].replace("'", "''")
                str2 += "'" + newstr + "',"
            else:
                str2 += "'" + str(lines[12]) + "',"

            if "'" in str(lines[13]):
                newstr = lines[13].replace("'", "''")
                str2 += "'" + newstr + "',"
            else:
                str2 += "'" + str(lines[13]) + "',"

            str2 += "'" + str(lines[14]) + "',"
            str2 += "'" + str(lines[15]) + "',"
            str2 += "'" + str(lines[16]) + "',"
            str2 += str(lines[17]) + ","
            str2 += "'" + str(lines[18]) + "')"

            str3 = str1 + str2
            try:
                cur.execute(str3)
            except:
                print("Insert to accessories failed for: " + str(lineNumber) + " " + str3)

            conn.commit()
            lineNumber = lineNumber + 1
    pass

def parseFossils():
    with open('fossils.csv', mode='r', encoding="utf8") as file:
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
            str1 = "INSERT INTO Fossils (Name,Buy,Sell,Color1,Color2,Size,Source,Museum,Version" \
                   ",Interact,Catalog,Filename,InternalID,UniqueEntryID) VALUES ("

            str2 = ""
            str2 += "'" + str(lines[0]) + "',"
            str2 += "'" + str(lines[1]) + "',"
            str2 += str(lines[2]) + ","
            str2 += "'" + str(lines[3]) + "',"
            str2 += "'" + str(lines[4]) + "',"
            str2 += "'" + str(lines[5]) + "',"
            str2 += "'" + str(lines[6]) + "',"
            str2 += "'" + str(lines[7]) + "',"
            str2 += "'" + str(lines[8]) + "',"

            if "No" in str(lines[9]):
                str2 += "false" + ","
            else:
                str2 += "true" + ","

            str2 += "'" + str(lines[10]) + "',"
            str2 += "'" + str(lines[11]) + "',"
            str2 += str(lines[12]) + ","
            str2 += "'" + str(lines[13]) + "')"



            str3 = str1 + str2
            try:
                cur.execute(str3)
            except:
                print("Insert to accessories failed for: " + str(lineNumber) + " " + str3)

            conn.commit()
            lineNumber = lineNumber + 1
    pass

def parseHeadwear():
    with open('headwear.csv', mode='r', encoding="utf8") as file:
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
            str1 = "INSERT INTO Headwear (Name,Variation,DIY,Buy,Sell,Color1,Color2,Size,MilesPrice" \
                   ",Source,SourceNotes,SeasonalAvailability,MannequinPiece,Version,Style" \
                   ",LabelThemes,Type,VillagerEquippable,Catalog,Filename,InternalID,UniqueEntryID) VALUES ("

            str2 = ""

            if "'" in str(lines[0]):
                newstr = lines[0].replace("'", "''")
                str2 += "'" + newstr + "',"
            else:
                str2 += "'" + str(lines[0]) + "',"

            str2 += "'" + str(lines[1]) + "',"

            if "No" in str(lines[2]):
                str2 += "false" + ","
            else:
                str2 += "true" + ","

            str2 += "'" + str(lines[3]) + "',"
            str2 += str(lines[4]) + ","
            str2 += "'" + str(lines[5]) + "',"
            str2 += "'" + str(lines[6]) + "',"
            str2 += "'" + str(lines[7]) + "',"
            str2 += "'" + str(lines[8]) + "',"

            if "'" in str(lines[9]):
                newstr = lines[9].replace("'", "''")
                str2 += "'" + newstr + "',"
            else:
                str2 += "'" + str(lines[9]) + "',"

            if "'" in str(lines[10]):
                newstr = lines[10].replace("'", "''")
                str2 += "'" + newstr + "',"
            else:
                str2 += "'" + str(lines[10]) + "',"

            str2 += "'" + str(lines[11]) + "',"

            if "No" in str(lines[12]):
                str2 += "false" + ","
            else:
                str2 += "true" + ","

            str2 += "'" + str(lines[13]) + "',"
            str2 += "'" + str(lines[14]) + "',"
            str2 += "'" + str(lines[15]) + "',"
            str2 += "'" + str(lines[16]) + "',"

            if "No" in str(lines[17]):
                str2 += "false" + ","
            else:
                str2 += "true" + ","

            str2 += "'" + str(lines[18]) + "',"
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
    pass

def parseHousewares():
    with open('housewares.csv', mode='r', encoding="utf8") as file:
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
            str1 = "INSERT INTO Housewares (Name,Variation,BodyTitle,Pattern,PatternTitle,DIY" \
                   ",BodyCustomize,PatternCustomize,KitCost,Buy,Sell,Color1,Color2,Size,MilesPrice" \
                   ",Source,SourceNotes,Version,HHAConcept1,HHAConcept2,HHASeries,HHASet,Interact" \
                   ",Tag,Outdoor,SpeakerType,LightingType,Catalog,Filename,VariantID,InternalID" \
                   ",UniqueEntryID) VALUES ("

            str2 = ""
            if "'" in str(lines[0]):
                newstr = lines[0].replace("'", "''")
                str2 += "'" + newstr + "',"
            else:
                str2 += "'" + str(lines[0]) + "',"

            str2 += "'" + str(lines[1]) + "',"
            str2 += "'" + str(lines[2]) + "',"
            str2 += "'" + str(lines[3]) + "',"
            str2 += "'" + str(lines[4]) + "',"
            if "No" in str(lines[5]):
                str2 += "false" + ","
            else:
                str2 += "true" + ","

            if "No" in str(lines[6]):
                str2 += "false" + ","
            else:
                str2 += "true" + ","

            if "No" in str(lines[7]):
                str2 += "false" + ","
            else:
                str2 += "true" + ","

            str2 += "'" + str(lines[8]) + "',"
            str2 += "'" + str(lines[9]) + "',"
            str2 += str(lines[10]) + ","
            str2 += "'" + str(lines[11]) + "',"
            str2 += "'" + str(lines[12]) + "',"
            str2 += "'" + str(lines[13]) + "',"
            str2 += "'" + str(lines[14]) + "',"

            if "'" in str(lines[15]):
                newstr = lines[15].replace("'", "''")
                str2 += "'" + newstr + "',"
            else:
                str2 += "'" + str(lines[15]) + "',"

            if "'" in str(lines[16]):
                newstr = lines[16].replace("'", "''")
                str2 += "'" + newstr + "',"
            else:
                str2 += "'" + str(lines[16]) + "',"

            str2 += "'" + str(lines[17]) + "',"

            if "'" in str(lines[18]):
                newstr = lines[18].replace("'", "''")
                str2 += "'" + newstr + "',"
            else:
                str2 += "'" + str(lines[18]) + "',"

            if "'" in str(lines[19]):
                newstr = lines[19].replace("'", "''")
                str2 += "'" + newstr + "',"
            else:
                str2 += "'" + str(lines[19]) + "',"

            if "'" in str(lines[20]):
                newstr = lines[20].replace("'", "''")
                str2 += "'" + newstr + "',"
            else:
                str2 += "'" + str(lines[20]) + "',"

            str2 += "'" + str(lines[21]) + "',"

            if "No" in str(lines[22]):
                str2 += "false" + ","
            else:
                str2 += "true" + ","

            str2 += "'" + str(lines[23]) + "',"

            if "No" in str(lines[24]):
                str2 += "false" + ","
            else:
                str2 += "true" + ","

            str2 += "'" + str(lines[25]) + "',"
            str2 += "'" + str(lines[26]) + "',"
            str2 += "'" + str(lines[27]) + "',"
            str2 += "'" + str(lines[28]) + "',"
            str2 += "'" + str(lines[29]) + "',"
            str2 += str(lines[30]) + ","
            str2 += "'" + str(lines[31]) + "')"


            str3 = str1 + str2
            try:
                cur.execute(str3)
            except:
                print("Insert to accessories failed for: " + str(lineNumber) + " " + str3)

            conn.commit()
            lineNumber = lineNumber + 1
    pass

def parseInsects():
    with open('insects.csv', mode='r', encoding="utf8") as file:
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
            str1 = "INSERT INTO Insects (Number,Name,Sell,Where_" \
                   ",Weather,TotalCatchesToUnlock,SpawnRates,NHJan,NHFeb,NHMar" \
                   ",NHApr,NHMay,NHJun,NHJul,NHAug,NHSep,NHOct,NHNov,NHDec,SHJan,SHFeb" \
                   ",SHMar,SHApr,SHMay,SHJun,SHJul,SHAug,SHSep,SHOct,SHNov,SHDec,Color1" \
                   ",Color2,IconFileName,CritterpediaFilename,Furniture,InternalID,UniqueEntryID) " \
                   " VALUES ("

            str2 = ""
            str2 += str(lines[0]) + ","

            if "'" in str(lines[1]):
                newstr = lines[1].replace("'", "''")
                str2 += "'" + newstr + "',"
            else:
                str2 += "'" + str(lines[1]) + "',"

            str2 += str(lines[2]) + ","
            str2 += "'" + str(lines[3]) + "',"
            str2 += "'" + str(lines[4]) + "',"
            str2 += str(lines[5]) + ","
            str2 += "'" + str(lines[6]) + "',"
            str2 += "'" + str(lines[7]) + "',"  # bool
            str2 += "'" + str(lines[8]) + "',"
            str2 += "'" + str(lines[9]) + "',"
            str2 += "'" + str(lines[10]) + "',"
            str2 += "'" + str(lines[11]) + "',"
            str2 += "'" + str(lines[12]) + "',"
            str2 += "'" + str(lines[13]) + "',"
            str2 += "'" + str(lines[14]) + "',"
            str2 += "'" + str(lines[15]) + "',"
            str2 += "'" + str(lines[16]) + "',"
            str2 += "'" + str(lines[17]) + "',"
            str2 += "'" + str(lines[18]) + "',"
            str2 += "'" + str(lines[19]) + "',"
            str2 += "'" + str(lines[20]) + "',"
            str2 += "'" + str(lines[21]) + "',"
            str2 += "'" + str(lines[22]) + "',"
            str2 += "'" + str(lines[23]) + "',"
            str2 += "'" + str(lines[24]) + "',"
            str2 += "'" + str(lines[25]) + "',"
            str2 += "'" + str(lines[26]) + "',"
            str2 += "'" + str(lines[27]) + "',"
            str2 += "'" + str(lines[28]) + "',"
            str2 += "'" + str(lines[29]) + "',"
            str2 += "'" + str(lines[30]) + "',"
            str2 += "'" + str(lines[31]) + "',"
            str2 += "'" + str(lines[32]) + "',"
            str2 += "'" + str(lines[33]) + "',"
            str2 += "'" + str(lines[34]) + "',"
            str2 += "'" + str(lines[35]) + "',"
            str2 += str(lines[36]) + ","
            str2 += "'" + str(lines[37]) + "')"


            str3 = str1 + str2
            try:
                cur.execute(str3)
            except:
                print("Insert to accessories failed for: " + str(lineNumber) + " " + str3)

            conn.commit()
            lineNumber = lineNumber + 1
    pass

def parseMiscellaneous():
    with open('miscellaneous.csv', mode='r', encoding="utf8") as file:
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
            str1 = "INSERT INTO Miscellaneous (Name,Variation,BodyTitle,Pattern" \
                   ",PatternTitle,DIY,BodyCustomize,PatternCustomize,KitCost,Buy" \
                   ",Sell,Color1,Color2,Size,Source,SourceNotes,Version,HHAConcept1,HHAConcept2,HHASeries,HHASet" \
                   ",Interact,Tag,Outdoor,SpeakerType,LightingType,Filename,VariantID,InternalID" \
                   ",UniqueEntryID)" \
                   " VALUES ("

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

            str2 += "'" + str(lines[2]) + "',"
            str2 += "'" + str(lines[3]) + "',"
            str2 += "'" + str(lines[4]) + "',"
            if "No" in str(lines[5]):
                str2 += "false" + ","
            else:
                str2 += "true" + ","
            if "No" in str(lines[6]):
                str2 += "false" + ","
            else:
                str2 += "true" + ","
            if "No" in str(lines[7]):
                str2 += "false" + ","
            else:
                str2 += "true" + ","
            str2 += "'" + str(lines[8]) + "',"
            str2 += "'" + str(lines[9]) + "',"
            str2 += str(lines[10]) + ","
            str2 += "'" + str(lines[11]) + "',"
            str2 += "'" + str(lines[12]) + "',"
            str2 += "'" + str(lines[13]) + "',"
            if "'" in str(lines[14]):
                newstr = lines[14].replace("'", "''")
                str2 += "'" + newstr + "',"
            else:
                str2 += "'" + str(lines[14]) + "',"
            if "'" in str(lines[15]):
                newstr = lines[15].replace("'", "''")
                str2 += "'" + newstr + "',"
            else:
                str2 += "'" + str(lines[15]) + "',"
            str2 += "'" + str(lines[16]) + "',"

            if "'" in str(lines[17]):
                newstr = lines[17].replace("'", "''")
                str2 += "'" + newstr + "',"
            else:
                str2 += "'" + str(lines[17]) + "',"


            if "'" in str(lines[18]):
                newstr = lines[18].replace("'", "''")
                str2 += "'" + newstr + "',"
            else:
                str2 += "'" + str(lines[18]) + "',"

            if "'" in str(lines[19]):
                newstr = lines[19].replace("'", "''")
                str2 += "'" + newstr + "',"
            else:
                str2 += "'" + str(lines[19]) + "',"

            str2 += "'" + str(lines[20]) + "',"

            if "No" in str(lines[21]):
                str2 += "false" + ","
            else:
                str2 += "true" + ","

            str2 += "'" + str(lines[22]) + "',"

            if "No" in str(lines[23]):
                str2 += "false" + ","
            else:
                str2 += "true" + ","

            str2 += "'" + str(lines[24]) + "',"
            str2 += "'" + str(lines[25]) + "',"
            str2 += "'" + str(lines[26]) + "',"
            str2 += "'" + str(lines[27]) + "',"
            str2 += "'" + str(lines[28]) + "',"
            str2 += "'" + str(lines[29]) + "')"






            str3 = str1 + str2
            try:
                cur.execute(str3)
            except:
                print("Insert to accessories failed for: " + str(lineNumber) + " " + str3)

            conn.commit()
            lineNumber = lineNumber + 1
    pass

def parseMusic():
    with open('music.csv', mode='r', encoding="utf8") as file:
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
            str1 = "INSERT INTO Music (Name,Buy,Sell,Color1" \
                   ",Color2,Size,Source,SourceNotes,Version,Catalog" \
                   ",Filename,InternalID,UniqueEntryID)" \
                   " VALUES ("

            str2 = ""

            if "'" in str(lines[0]):
                newstr = lines[0].replace("'", "''")
                str2 += "'" + newstr + "',"
            else:
                str2 += "'" + str(lines[0]) + "',"

            str2 += "'" + str(lines[1]) + "',"
            str2 += str(lines[2]) + ","
            str2 += "'" + str(lines[3]) + "',"
            str2 += "'" + str(lines[4]) + "',"
            str2 += "'" + str(lines[5]) + "',"

            if "'" in str(lines[6]):
                newstr = lines[6].replace("'", "''")
                str2 += "'" + newstr + "',"
            else:
                str2 += "'" + str(lines[6]) + "',"


            if "'" in str(lines[7]):
                newstr = lines[7].replace("'", "''")
                str2 += "'" + newstr + "',"
            else:
                str2 += "'" + str(lines[7]) + "',"

            str2 += "'" + str(lines[8]) + "',"
            str2 += "'" + str(lines[9]) + "',"
            str2 += "'" + str(lines[10]) + "',"
            str2 += str(lines[11]) + ","
            str2 += "'" + str(lines[12]) + "')"

            str3 = str1 + str2
            try:
                cur.execute(str3)
            except:
                print("Insert to accessories failed for: " + str(lineNumber) + " " + str3)

            conn.commit()
            lineNumber = lineNumber + 1
    pass


def parseOther():
    with open('other.csv', mode='r', encoding="utf8") as file:
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
            str1 = "INSERT INTO Other (Name,DIY,StackSize,Buy" \
                   ",Sell,MilesPrice,Source,SourceNotes,Tag,Color1" \
                   ",Color2,Version,Filename,InternalID,UniqueEntryID)" \
                   " VALUES ("

            str2 = ""
            if "'" in str(lines[0]):
                newstr = lines[0].replace("'", "''")
                str2 += "'" + newstr + "',"
            else:
                str2 += "'" + str(lines[0]) + "',"

            if "No" in str(lines[1]):
                str2 += "false" + ","
            else:
                str2 += "true" + ","

            str2 += str(lines[2]) + ","
            str2 += "'" + str(lines[3]) + "',"
            str2 += "'" + str(lines[4]) + "',"
            str2 += "'" + str(lines[5]) + "',"

            if "'" in str(lines[6]):
                newstr = lines[6].replace("'", "''")
                str2 += "'" + newstr + "',"
            else:
                str2 += "'" + str(lines[6]) + "',"

            if "'" in str(lines[7]):
                newstr = lines[7].replace("'", "''")
                str2 += "'" + newstr + "',"
            else:
                str2 += "'" + str(lines[7]) + "',"

            str2 += "'" + str(lines[8]) + "',"
            str2 += "'" + str(lines[9]) + "',"
            str2 += "'" + str(lines[10]) + "',"
            str2 += "'" + str(lines[11]) + "',"
            str2 += "'" + str(lines[12]) + "',"
            str2 += str(lines[13]) + ","
            str2 += "'" + str(lines[14]) + "')"

            str3 = str1 + str2
            try:
                cur.execute(str3)
            except:
                print("Insert to accessories failed for: " + str(lineNumber) + " " + str3)

            conn.commit()
            lineNumber = lineNumber + 1
    pass

def parsePhotos():
    with open('photos.csv', mode='r', encoding="utf8") as file:
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
            str1 = "INSERT INTO Photos (Name,Variation,BodyTitle,Pattern" \
                   ",PatternTitle,DIY,Customize,KitCost,Buy,Sell" \
                   ",Color1,Color2,Size,Source,Version,Catalog" \
                   ",Filename,VariantID,InternalID,UniqueEntryID)" \
                   " VALUES ("

            str2 = ""

            if "'" in str(lines[0]):
                newstr = lines[0].replace("'", "''")
                str2 += "'" + newstr + "',"
            else:
                str2 += "'" + str(lines[0]) + "',"


            str2 += "'" + str(lines[1]) + "',"
            str2 += "'" + str(lines[2]) + "',"
            str2 += "'" + str(lines[3]) + "',"
            str2 += "'" + str(lines[4]) + "',"
            str2 += "'" + str(lines[5]) + "',"
            str2 += "'" + str(lines[6]) + "',"
            str2 += "'" + str(lines[7]) + "',"
            str2 += "'" + str(lines[8]) + "',"
            str2 += "'" + str(lines[9]) + "',"
            str2 += "'" + str(lines[10]) + "',"
            str2 += "'" + str(lines[11]) + "',"
            str2 += "'" + str(lines[12]) + "',"
            str2 += "'" + str(lines[13]) + "',"
            str2 += "'" + str(lines[14]) + "',"
            str2 += "'" + str(lines[15]) + "',"
            str2 += "'" + str(lines[16]) + "',"
            str2 += "'" + str(lines[17]) + "',"
            str2 += "'" + str(lines[18]) + "',"
            str2 += "'" + str(lines[19]) + "')"

            str3 = str1 + str2
            try:
                cur.execute(str3)
            except:
                print("Insert to accessories failed for: " + str(lineNumber) + " " + str3)

            conn.commit()
            lineNumber = lineNumber + 1
    pass

def parsePosters():
    with open('posters.csv', mode='r', encoding="utf8") as file:
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
            str1 = "INSERT INTO Posters (Name,Buy,Sell,Color1" \
                   ",Color2,Size,Source,SourceNotes,Version,Catalog" \
                   ",Filename,InternalID,UniqueEntryID)" \
                   " VALUES ("

            str2 = ""

            if "'" in str(lines[0]):
                newstr = lines[0].replace("'", "''")
                str2 += "'" + newstr + "',"
            else:
                str2 += "'" + str(lines[0]) + "',"

            str2 += str(lines[1]) + ","
            str2 += str(lines[2]) + ","
            str2 += "'" + str(lines[3]) + "',"
            str2 += "'" + str(lines[4]) + "',"
            str2 += "'" + str(lines[5]) + "',"

            if "'" in str(lines[6]):
                newstr = lines[6].replace("'", "''")
                str2 += "'" + newstr + "',"
            else:
                str2 += "'" + str(lines[6]) + "',"

            if "'" in str(lines[7]):
                newstr = lines[7].replace("'", "''")
                str2 += "'" + newstr + "',"
            else:
                str2 += "'" + str(lines[7]) + "',"

            str2 += "'" + str(lines[8]) + "',"
            str2 += "'" + str(lines[9]) + "',"
            str2 += "'" + str(lines[10]) + "',"
            str2 += str(lines[11]) + ","
            str2 += "'" + str(lines[12]) + "')"

            str3 = str1 + str2
            try:
                cur.execute(str3)
            except:
                print("Insert to accessories failed for: " + str(lineNumber) + " " + str3)

            conn.commit()
            lineNumber = lineNumber + 1
    pass

def parseReactions():
    with open('reactions.csv', mode='r', encoding="utf8") as file:
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
            str1 = "INSERT INTO Reactions (Name,Source,SourceNotes,InternalID" \
                   ",UniqueEntryID)" \
                   " VALUES ("

            str2 = ""

            str2 += "'" + str(lines[0]) + "',"
            str2 += "'" + str(lines[1]) + "',"
            str2 += "'" + str(lines[2]) + "',"
            str2 += "'" + str(lines[3]) + "',"
            str2 += "'" + str(lines[4]) + "')"

            str3 = str1 + str2
            try:
                cur.execute(str3)
            except:
                print("Insert to accessories failed for: " + str(lineNumber) + " " + str3)

            conn.commit()
            lineNumber = lineNumber + 1
    pass

def parseRecipes():
    with open('recipes.csv', mode='r', encoding="utf8") as file:
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
            str1 = "INSERT INTO Recipes (Name,Number1,Material1,Number2,Material2,Number3" \
                   ",Material3,Number4,Material4,Number5,Material5,Number6,Material6,Buy" \
                   ",Sell,MilesPrice,Source,SourceNotes,NumberOfRecipesToUnlock,Version" \
                   ",Category,SerialID,InternalID,UniqueEntryID)" \
                   " VALUES ("

            str2 = ""

            if "'" in str(lines[0]):
                newstr = lines[0].replace("'", "''")
                str2 += "'" + newstr + "',"
            else:
                str2 += "'" + str(lines[0]) + "',"

            str2 += "'" + str(lines[1]) + "',"
            str2 += "'" + str(lines[2]) + "',"
            str2 += "'" + str(lines[3]) + "',"
            str2 += "'" + str(lines[4]) + "',"
            str2 += "'" + str(lines[5]) + "',"
            str2 += "'" + str(lines[6]) + "',"
            str2 += "'" + str(lines[7]) + "',"
            str2 += "'" + str(lines[8]) + "',"
            str2 += "'" + str(lines[9]) + "',"
            str2 += "'" + str(lines[10]) + "',"
            str2 += "'" + str(lines[11]) + "',"
            str2 += "'" + str(lines[12]) + "',"
            str2 += "'" + str(lines[13]) + "',"
            str2 += str(lines[14]) + ","
            str2 += "'" + str(lines[15]) + "',"

            if "'" in str(lines[16]):
                newstr = lines[16].replace("'", "''")
                str2 += "'" + newstr + "',"
            else:
                str2 += "'" + str(lines[16]) + "',"

            if "'" in str(lines[17]):
                newstr = lines[17].replace("'", "''")
                str2 += "'" + newstr + "',"
            else:
                str2 += "'" + str(lines[17]) + "',"

            str2 += str(lines[18]) + ","
            str2 += "'" + str(lines[19]) + "',"
            str2 += "'" + str(lines[20]) + "',"
            str2 += str(lines[21]) + ","
            str2 += str(lines[22]) + ","
            str2 += "'" + str(lines[23]) + "')"

            str3 = str1 + str2
            try:
                cur.execute(str3)
            except:
                print("Insert to accessories failed for: " + str(lineNumber) + " " + str3)

            conn.commit()
            lineNumber = lineNumber + 1
    pass

def parseRugs():
    with open('rugs.csv', mode='r', encoding="utf8") as file:
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
            str1 = "INSERT INTO Rugs (Name,DIY,Buy,Sell,Color1,Color2" \
                   ",Size,MilesPrice,Source,SourceNotes,Version,HHAConcept1,HHAConcept2,HHASeries" \
                   ",Tag,Catalog,Filename,InternalID,UniqueEntryID)" \
                   " VALUES ("

            str2 = ""

            if "'" in str(lines[0]):
                newstr = lines[0].replace("'", "''")
                str2 += "'" + newstr + "',"
            else:
                str2 += "'" + str(lines[0]) + "',"

            if "No" in str(lines[1]):
                str2 += "false" + ","
            else:
                str2 += "true" + ","

            str2 += "'" + str(lines[2]) + "',"
            str2 += str(lines[3]) + ","
            str2 += "'" + str(lines[4]) + "',"
            str2 += "'" + str(lines[5]) + "',"
            str2 += "'" + str(lines[6]) + "',"
            str2 += "'" + str(lines[7]) + "',"
            str2 += "'" + str(lines[8]) + "',"
            str2 += "'" + str(lines[9]) + "',"
            str2 += "'" + str(lines[10]) + "',"

            if "'" in str(lines[11]):
                newstr = lines[11].replace("'", "''")
                str2 += "'" + newstr + "',"
            else:
                str2 += "'" + str(lines[11]) + "',"

            if "'" in str(lines[12]):
                newstr = lines[12].replace("'", "''")
                str2 += "'" + newstr + "',"
            else:
                str2 += "'" + str(lines[12]) + "',"

            str2 += "'" + str(lines[13]) + "',"
            str2 += "'" + str(lines[14]) + "',"
            str2 += "'" + str(lines[15]) + "',"
            str2 += "'" + str(lines[16]) + "',"
            str2 += str(lines[17]) + ","
            str2 += "'" + str(lines[18]) + "')"

            str3 = str1 + str2
            try:
                cur.execute(str3)
            except:
                print("Insert to accessories failed for: " + str(lineNumber) + " " + str3)

            conn.commit()
            lineNumber = lineNumber + 1
    pass

def parseShoes():
    with open('shoes.csv', mode='r', encoding="utf8") as file:
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
            str1 = "INSERT INTO Shoes (Name,Variation,DIY,Buy,Sell,Color1" \
                   ",Color2,Size,MilesPrice,Source,SourceNotes,SeasonalAvailability" \
                   ",MannequinPiece,Version,Style,LabelThemes" \
                   ",VillagerEquippable,Catalog,Filename,InternalID,UniqueEntryID)" \
                   " VALUES ("

            str2 = ""

            if "'" in str(lines[0]):
                newstr = lines[0].replace("'", "''")
                str2 += "'" + newstr + "',"
            else:
                str2 += "'" + str(lines[0]) + "',"

            str2 += "'" + str(lines[1]) + "',"

            if "No" in str(lines[2]):
                str2 += "false" + ","
            else:
                str2 += "true" + ","

            str2 += "'" + str(lines[3]) + "',"
            str2 += str(lines[4]) + ","
            str2 += "'" + str(lines[5]) + "',"
            str2 += "'" + str(lines[6]) + "',"
            str2 += "'" + str(lines[7]) + "',"
            str2 += "'" + str(lines[8]) + "',"

            if "'" in str(lines[9]):
                newstr = lines[9].replace("'", "''")
                str2 += "'" + newstr + "',"
            else:
                str2 += "'" + str(lines[9]) + "',"

            if "'" in str(lines[10]):
                newstr = lines[10].replace("'", "''")
                str2 += "'" + newstr + "',"
            else:
                str2 += "'" + str(lines[10]) + "',"

            str2 += "'" + str(lines[11]) + "',"

            if "No" in str(lines[12]):
                str2 += "false" + ","
            else:
                str2 += "true" + ","

            str2 += "'" + str(lines[13]) + "',"
            str2 += "'" + str(lines[14]) + "',"
            str2 += "'" + str(lines[15]) + "',"

            if "No" in str(lines[16]):
                str2 += "false" + ","
            else:
                str2 += "true" + ","

            str2 += "'" + str(lines[17]) + "',"
            str2 += "'" + str(lines[18]) + "',"
            str2 += str(lines[19]) + ","
            str2 += "'" + str(lines[20]) + "')"

            str3 = str1 + str2
            try:
                cur.execute(str3)
            except:
                print("Insert to accessories failed for: " + str(lineNumber) + " " + str3)

            conn.commit()
            lineNumber = lineNumber + 1
    pass

def parseSocks():
    with open('socks.csv', mode='r', encoding="utf8") as file:
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
            str1 = "INSERT INTO Socks (Name,Variation,DIY,Buy,Sell,Color1" \
                   ",Color2,Size,MilesPrice,Source,SourceNotes,SeasonalAvailability" \
                   ",MannequinPiece,Version,Style,LabelThemes" \
                   ",VillagerEquippable,Catalog,Filename,InternalID,UniqueEntryID)" \
                   " VALUES ("

            str2 = ""

            if "'" in str(lines[0]):
                newstr = lines[0].replace("'", "''")
                str2 += "'" + newstr + "',"
            else:
                str2 += "'" + str(lines[0]) + "',"

            str2 += "'" + str(lines[1]) + "',"

            if "No" in str(lines[2]):
                str2 += "false" + ","
            else:
                str2 += "true" + ","

            str2 += "'" + str(lines[3]) + "',"
            str2 += str(lines[4]) + ","
            str2 += "'" + str(lines[5]) + "',"
            str2 += "'" + str(lines[6]) + "',"
            str2 += "'" + str(lines[7]) + "',"
            str2 += "'" + str(lines[8]) + "',"

            if "'" in str(lines[9]):
                newstr = lines[9].replace("'", "''")
                str2 += "'" + newstr + "',"
            else:
                str2 += "'" + str(lines[9]) + "',"

            if "'" in str(lines[10]):
                newstr = lines[10].replace("'", "''")
                str2 += "'" + newstr + "',"
            else:
                str2 += "'" + str(lines[10]) + "',"

            str2 += "'" + str(lines[11]) + "',"

            if "No" in str(lines[12]):
                str2 += "false" + ","
            else:
                str2 += "true" + ","

            str2 += "'" + str(lines[13]) + "',"
            str2 += "'" + str(lines[14]) + "',"
            str2 += "'" + str(lines[15]) + "',"

            if "No" in str(lines[16]):
                str2 += "false" + ","
            else:
                str2 += "true" + ","

            str2 += "'" + str(lines[17]) + "',"
            str2 += "'" + str(lines[18]) + "',"
            str2 += str(lines[19]) + ","
            str2 += "'" + str(lines[20]) + "')"

            str3 = str1 + str2
            try:
                cur.execute(str3)
            except:
                print("Insert to accessories failed for: " + str(lineNumber) + " " + str3)

            conn.commit()
            lineNumber = lineNumber + 1
    pass

def parseTools():
    with open('tools.csv', mode='r', encoding="utf8") as file:
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
            str1 = "INSERT INTO Tools (Name,Variation,BodyTitle,DIY,Customize,KitCost" \
                   ",Uses,StackSize,Buy,Sell,Color1,Color2,Size,Set,MilesPrice" \
                   ",Source,SourceNotes,Version,Filename" \
                   ",VariantID,InternalID,UniqueEntryID)" \
                   " VALUES ("

            str2 = ""
            str2 += "'" + str(lines[0]) + "',"
            str2 += "'" + str(lines[1]) + "',"
            str2 += "'" + str(lines[2]) + "',"

            if "No" in str(lines[3]):
                str2 += "false" + ","
            else:
                str2 += "true" + ","

            if "No" in str(lines[4]):
                str2 += "false" + ","
            else:
                str2 += "true" + ","

            str2 += "'" + str(lines[5]) + "',"
            str2 += "'" + str(lines[6]) + "',"
            str2 += str(lines[7]) + ","
            str2 += "'" + str(lines[8]) + "',"
            str2 += str(lines[9]) + ","
            str2 += "'" + str(lines[10]) + "',"
            str2 += "'" + str(lines[11]) + "',"
            str2 += "'" + str(lines[12]) + "',"
            str2 += "'" + str(lines[13]) + "',"
            str2 += "'" + str(lines[14]) + "',"

            if "'" in str(lines[15]):
                newstr = lines[15].replace("'", "''")
                str2 += "'" + newstr + "',"
            else:
                str2 += "'" + str(lines[15]) + "',"

            if "'" in str(lines[16]):
                newstr = lines[16].replace("'", "''")
                str2 += "'" + newstr + "',"
            else:
                str2 += "'" + str(lines[16]) + "',"

            str2 += "'" + str(lines[17]) + "',"
            str2 += "'" + str(lines[18]) + "',"
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
    pass


def parseTops():
    with open('tops.csv', mode='r', encoding="utf8") as file:
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
            str1 = "INSERT INTO Tops (Name,Variation,DIY,Buy,Sell,Color1" \
                   ",Color2,Size,MilesPrice,Source,SourceNotes,SeasonalAvailability" \
                   ",MannequinPiece,Version,Style,LabelThemes,VillagerEquippable" \
                   ",Catalog,Filename,InternalID,UniqueEntryID)" \
                   " VALUES ("

            str2 = ""

            if "'" in str(lines[0]):
                newstr = lines[0].replace("'", "''")
                str2 += "'" + newstr + "',"
            else:
                str2 += "'" + str(lines[0]) + "',"
            str2 += "'" + str(lines[1]) + "',"
            str2 += "'" + str(lines[2]) + "',"
            str2 += "'" + str(lines[3]) + "',"
            str2 += str(lines[4]) + ","
            str2 += "'" + str(lines[5]) + "',"
            str2 += "'" + str(lines[6]) + "',"
            str2 += "'" + str(lines[7]) + "',"
            str2 += "'" + str(lines[8]) + "',"

            if "'" in str(lines[9]):
                newstr = lines[9].replace("'", "''")
                str2 += "'" + newstr + "',"
            else:
                str2 += "'" + str(lines[9]) + "',"

            if "'" in str(lines[10]):
                newstr = lines[10].replace("'", "''")
                str2 += "'" + newstr + "',"
            else:
                str2 += "'" + str(lines[10]) + "',"

            str2 += "'" + str(lines[11]) + "',"
            str2 += "'" + str(lines[12]) + "',"
            str2 += "'" + str(lines[13]) + "',"
            str2 += "'" + str(lines[14]) + "',"
            str2 += "'" + str(lines[15]) + "',"
            str2 += "'" + str(lines[16]) + "',"
            str2 += "'" + str(lines[17]) + "',"
            str2 += "'" + str(lines[18]) + "',"
            str2 += str(lines[19]) + ","
            str2 += "'" + str(lines[20]) + "')"


            str3 = str1 + str2
            try:
                cur.execute(str3)
            except:
                print("Insert to accessories failed for: " + str(lineNumber) + " " + str3)

            conn.commit()
            lineNumber = lineNumber + 1
    pass

def parseUmbrellas():
    with open('umbrellas.csv', mode='r', encoding="utf8") as file:
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
            str1 = "INSERT INTO Umbrellas (Name,DIY,Buy,Sell,Color1" \
                   ",Color2,Size,MilesPrice,Source,SourceNotes" \
                   ",Version,VillagerEquippable" \
                   ",Catalog,Filename,InternalID,UniqueEntryID)" \
                   " VALUES ("

            str2 = ""

            if "'" in str(lines[0]):
                newstr = lines[0].replace("'", "''")
                str2 += "'" + newstr + "',"
            else:
                str2 += "'" + str(lines[0]) + "',"
            str2 += "'" + str(lines[1]) + "',"
            str2 += "'" + str(lines[2]) + "',"
            str2 += str(lines[3]) + ","
            str2 += "'" + str(lines[4]) + "',"
            str2 += "'" + str(lines[5]) + "',"
            str2 += "'" + str(lines[6]) + "',"
            str2 += "'" + str(lines[7]) + "',"

            if "'" in str(lines[8]):
                newstr = lines[8].replace("'", "''")
                str2 += "'" + newstr + "',"
            else:
                str2 += "'" + str(lines[8]) + "',"

            if "'" in str(lines[9]):
                newstr = lines[9].replace("'", "''")
                str2 += "'" + newstr + "',"
            else:
                str2 += "'" + str(lines[9]) + "',"

            str2 += "'" + str(lines[10]) + "',"
            str2 += "'" + str(lines[11]) + "',"
            str2 += "'" + str(lines[12]) + "',"
            str2 += "'" + str(lines[13]) + "',"
            str2 += str(lines[14]) + ","
            str2 += "'" + str(lines[15]) + "')"



            str3 = str1 + str2
            try:
                cur.execute(str3)
            except:
                print("Insert to accessories failed for: " + str(lineNumber) + " " + str3)

            conn.commit()
            lineNumber = lineNumber + 1
    pass

def parseVillagers():
    with open('villagers.csv', mode='r', encoding="utf8") as file:
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
            str1 = "INSERT INTO Villagers (Name,Species,Gender,Personality,Hobby" \
                   ",Birthday,Catchphrase,FavoriteSong,Style1,Style2" \
                   ",Color1,Color2,Wallpaper,Flooring" \
                   ",FurnitureList,Filename,UniqueEntryID)" \
                   " VALUES ("

            str2 = ""

            if "'" in str(lines[0]):
                newstr = lines[0].replace("'", "''")
                str2 += "'" + newstr + "',"
            else:
                str2 += "'" + str(lines[0]) + "',"

            str2 += "'" + str(lines[1]) + "',"
            str2 += "'" + str(lines[2]) + "',"
            str2 += "'" + str(lines[3]) + "',"
            str2 += "'" + str(lines[4]) + "',"
            str2 += "'" + str(lines[5]) + "',"

            if "'" in str(lines[6]):
                newstr = lines[6].replace("'", "''")
                str2 += "'" + newstr + "',"
            else:
                str2 += "'" + str(lines[6]) + "',"

            if "'" in str(lines[7]):
                newstr = lines[7].replace("'", "''")
                str2 += "'" + newstr + "',"
            else:
                str2 += "'" + str(lines[7]) + "',"

            str2 += "'" + str(lines[8]) + "',"
            str2 += "'" + str(lines[9]) + "',"
            str2 += "'" + str(lines[10]) + "',"
            str2 += "'" + str(lines[11]) + "',"
            str2 += "'" + str(lines[12]) + "',"

            if "'" in str(lines[13]):
                newstr = lines[13].replace("'", "''")
                str2 += "'" + newstr + "',"
            else:
                str2 += "'" + str(lines[13]) + "',"

            str2 += "'" + str(lines[14]) + "',"
            str2 += "'" + str(lines[15]) + "',"
            str2 += "'" + str(lines[16]) + "')"

            str3 = str1 + str2
            try:
                cur.execute(str3)
            except:
                print("Insert to accessories failed for: " + str(lineNumber) + " " + str3)

            conn.commit()
            lineNumber = lineNumber + 1
    pass

def parseWallMounted():
    with open('wall-mounted.csv', mode='r', encoding="utf8") as file:
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
            if lineNumber == 459:
                break
            str1 = "INSERT INTO WallMounted (Name,Variation,BodyTitle,Pattern,PatternTitle" \
                   ",DIY,BodyCustomize,PatternCustomize,KitCost,buy" \
                   ",Sell,Color1,Color2,Size,Source,SourceNotes,Version,HHAConcept1,HHAConcept2" \
                   ",HHASeries,HHASet,Interact,Tag,Outdoor,LightingType,DoorDeco,Catalog,Filename" \
                   ",VariantID,InternalID,UniqueEntryID)" \
                   " VALUES ("

            str2 = ""
            if "'" in str(lines[0]):
                newstr = lines[0].replace("'", "''")
                str2 += "'" + newstr + "',"
            else:
                str2 += "'" + str(lines[0]) + "',"

            str2 += "'" + str(lines[1]) + "',"
            str2 += "'" + str(lines[2]) + "',"

            if "'" in str(lines[3]):
                newstr = lines[3].replace("'", "''")
                str2 += "'" + newstr + "',"
            else:
                str2 += "'" + str(lines[3]) + "',"

            str2 += "'" + str(lines[4]) + "',"
            str2 += "'" + str(lines[5]) + "',"
            str2 += "'" + str(lines[6]) + "',"
            str2 += "'" + str(lines[7]) + "',"
            str2 += "'" + str(lines[8]) + "',"
            str2 += "'" + str(lines[9]) + "',"
            str2 += str(lines[10]) + ","
            str2 += "'" + str(lines[11]) + "',"
            str2 += "'" + str(lines[12]) + "',"
            str2 += "'" + str(lines[13]) + "',"

            if "'" in str(lines[14]):
                newstr = lines[14].replace("'", "''")
                str2 += "'" + newstr + "',"
            else:
                str2 += "'" + str(lines[14]) + "',"
            if "'" in str(lines[15]):
                newstr = lines[15].replace("'", "''")
                str2 += "'" + newstr + "',"
            else:
                str2 += "'" + str(lines[15]) + "',"

            str2 += "'" + str(lines[16]) + "',"

            if "'" in str(lines[17]):
                newstr = lines[17].replace("'", "''")
                str2 += "'" + newstr + "',"
            else:
                str2 += "'" + str(lines[17]) + "',"

            if "'" in str(lines[18]):
                newstr = lines[18].replace("'", "''")
                str2 += "'" + newstr + "',"
            else:
                str2 += "'" + str(lines[18]) + "',"

            if "'" in str(lines[19]):
                newstr = lines[19].replace("'", "''")
                str2 += "'" + newstr + "',"
            else:
                str2 += "'" + str(lines[19]) + "',"
            if "'" in str(lines[20]):
                newstr = lines[20].replace("'", "''")
                str2 += "'" + newstr + "',"
            else:
                str2 += "'" + str(lines[20]) + "',"

            str2 += "'" + str(lines[21]) + "',"
            str2 += "'" + str(lines[22]) + "',"
            str2 += "'" + str(lines[23]) + "',"
            str2 += "'" + str(lines[24]) + "',"
            str2 += "'" + str(lines[25]) + "',"
            str2 += "'" + str(lines[26]) + "',"
            str2 += "'" + str(lines[27]) + "',"
            str2 += "'" + str(lines[27]) + "',"
            str2 += str(lines[29]) + ","
            str2 += "'" + str(lines[30]) + "')"



            str3 = str1 + str2
            try:
                cur.execute(str3)
            except:
                print("Insert to accessories failed for: " + str(lineNumber) + " " + str3)

            conn.commit()
            lineNumber = lineNumber + 1
    pass

def parseWallpaper():
    with open('wallpaper.csv', mode='r', encoding="utf8") as file:
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
            if lineNumber == 459:
                break
            str1 = "INSERT INTO Wallpaper (Name,VFX,VFXType,DIY,Buy,Sell,Color1,Color2" \
                   ",MilesPrice,Source,SourceNotes,Catalog,WindowType,WindowColor,Panetype" \
                   ",CurtainType,CurtainColor,CeilingType,HHAConcept1,HHAConcept2,HHASeries" \
                   ",Tag,Version,Filename,InternalID,UniqueEntryID)" \
                   " VALUES ("

            str2 = ""

            str2 += "'" + str(lines[0]) + "',"
            str2 += "'" + str(lines[1]) + "',"
            str2 += "'" + str(lines[2]) + "',"
            str2 += "'" + str(lines[3]) + "',"
            str2 += "'" + str(lines[4]) + "',"
            str2 += str(lines[5]) + ","
            str2 += "'" + str(lines[6]) + "',"
            str2 += "'" + str(lines[7]) + "',"
            str2 += "'" + str(lines[8]) + "',"

            if "'" in str(lines[9]):
                newstr = lines[9].replace("'", "''")
                str2 += "'" + newstr + "',"
            else:
                str2 += "'" + str(lines[9]) + "',"

            str2 += "'" + str(lines[10]) + "',"
            str2 += "'" + str(lines[11]) + "',"
            str2 += "'" + str(lines[12]) + "',"
            str2 += "'" + str(lines[13]) + "',"
            str2 += "'" + str(lines[14]) + "',"
            str2 += "'" + str(lines[15]) + "',"
            str2 += "'" + str(lines[16]) + "',"
            str2 += "'" + str(lines[17]) + "',"

            if "'" in str(lines[18]):
                newstr = lines[18].replace("'", "''")
                str2 += "'" + newstr + "',"
            else:
                str2 += "'" + str(lines[18]) + "',"

            if "'" in str(lines[19]):
                newstr = lines[19].replace("'", "''")
                str2 += "'" + newstr + "',"
            else:
                str2 += "'" + str(lines[19]) + "',"

            if "'" in str(lines[20]):
                newstr = lines[20].replace("'", "''")
                str2 += "'" + newstr + "',"
            else:
                str2 += "'" + str(lines[20]) + "',"

            str2 += "'" + str(lines[21]) + "',"
            str2 += "'" + str(lines[22]) + "',"
            str2 += "'" + str(lines[23]) + "',"
            str2 += str(lines[24]) + ","
            str2 += "'" + str(lines[25]) + "')"



            str3 = str1 + str2
            try:
                cur.execute(str3)
            except:
                print("Insert to accessories failed for: " + str(lineNumber) + " " + str3)

            conn.commit()
            lineNumber = lineNumber + 1
    pass


