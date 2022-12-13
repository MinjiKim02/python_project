# Author : Minji Kim
# Class #2 Facility


# class Doctor:
# class Laboratory:
# class Patient:

fileFacilities = 'facilities.txt'
class Facility:
    def __init__(self, facilityName=''):
        if facilityName != '':
            self.facilityName = facilityName

    # read facilities file
    def readFacilitiesFile(self):
        file = open(fileFacilities, 'r')  # read = 'r'
        facilities_list = []
        for lines in file:
            facilities_list.append(lines.rstrip().split('_'))
        file.close()
        return facilities_list


    # adds and writes the facility to the file
    def addFacility(self):
        facilities_list = self.readFacilitiesFile()
        facility_add = input("Enter Facility name: \n")
        facilities_file = open(fileFacilities, 'a')  # add = 'a'
        facilities_file.write(facility_add)
        facilities_file.close()
        self.writeListOfFacilitiesToFile(facilities_list)



    # displays the list of facilities
    def displayFacilities(self):
        facilities_list = self.readFacilitiesFile()
        for lines in facilities_list:
            formatted = ''.join(lines)
            print(formatted)


    # writes the facilities list to facilities.txt
    def writeListOfFacilitiesToFile(self, facilities_list):
        facilities_list = self.readFacilitiesFile()
        facilities_file = open(fileFacilities, 'w')  # write = 'w'
        for lines in facilities_list:
            formatted = ''.join(lines)
            facilities_file.write(formatted)
            facilities_file.write('\n')
        facilities_file.close()


this_facility = Facility()

# print part
while True:
    print("Welcome to Alberta Hospital (AH) Management system \n"
          "Select from the following options, or select 0 to stop:\n"
          "1 - Doctors\n"
          "2 - Facilities\n"
          "3 - Laboratories\n"
          "4 - Patients")
    option = input()
    while option == '2':
        category = int(input("Facilities Menu:\n"
                             "1 - Display Facilities list\n"
                             "2 - Add Facility\n"
                             "3 - Back to the Main Menu\n"))
        if category == 1:
            this_facility.displayFacilities()
            print("\nBack to the previous Menu")

        elif category == 2:
            this_facility.addFacility()
            print("\nBack to the previous Menu")

        elif category == 3:
            print("Welcome to Alberta Hospital (AH) Management system \n"
                  "Select from the following options, or select 0 to stop:\n"
                  "1 - Doctors\n"
                  "2 - Facilities\n"
                  "3 - Laboratories\n"
                  "4 - Patients")
            option = input()
            continue
    else:
        break

