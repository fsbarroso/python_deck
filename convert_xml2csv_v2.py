from xml.etree import ElementTree
import csv

# PARSE XML
xml = ElementTree.parse(".\sample_response.txt")

row_fields = [  "race_id",
                "name",
                "description",
                "url",
                "external_race_url",
                "fb_page_id",
                "last_date",
                "last_end_date",
                "next_date",
                "next_end_date",
                "is_draft_race",
                "is_private_race",
                "is_registration_open",
                "created",
                "last_modified",
                "./address/street",
                "./address/street2",
                "./address/city",
                "./address/state",
                "./address/zipcode",
                "./address/country_code",
                "timezone",
                "real_time_notifications_enabled"]


# CREATE CSV FILE
csvfile = open("data.csv",'w',newline='',encoding='utf-8')
csvfile_writer = csv.writer(csvfile)

# creating the header to csv file
csvfile_writer.writerow(row_fields)

# for each RACE
for race in xml.findall("race"):

    line_data = []

    if(race):
        # extract RACE details

        for race_field in row_fields:
            tmp_field = race.find(race_field)
            if tmp_field is not None :
                if tmp_field.text is not None :
                    tmp_field = tmp_field.text
                    tmp_field = tmp_field.replace('\n',"")
                    tmp_field = tmp_field.replace('\t',"")
                    tmp_field = tmp_field.replace(';',"")
                else:
                    tmp_field = "\"\""
            else :
                tmp_field = "(field not present)"
            line_data.append(tmp_field)

        # add new row to csv file
    csvfile_writer.writerow(line_data)

csvfile.close()
