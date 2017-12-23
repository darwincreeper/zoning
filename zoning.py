# imports
import time
import csv

# Objects
class alias:
    def __init__(self, kind, name, wwn):
        self.kind = kind
        self.name = name
        self.wwn = wwn

class zone:
    def __init__(self, name, members):
        self.name = name
        self.members = members

# Variables
aliases = []

# Fonctions
def add_alias_manually():
    kind = input("\n\tAlias kind (i for initiator, t for target): ")
    name = input("\tAlias name: ")
    wwn = input("\tAlias wwn (xx:xx:xx:xx:xx:xx:xx:xx): ")
    print("\n\tAlias added successfully!\n")
    new_alias = alias(kind, name, wwn)
    aliases.append(new_alias)
    time.sleep(1)

def import_aliases_from_csv(file_path):
    while True:
        try:
            with open(file_path,'r') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    kind = row[0]
                    name = row[1]
                    wwn = row[2]
                    new_alias = alias(kind, name, wwn)
                    aliases.append(new_alias)
                print("\n\tImport Successfull!\n")
            break
        except (FileNotFoundError, IOError):
            print("\n\tImport failed. Path does not exist!\n")
            break
    time.sleep(1)

def list_aliases(aliases):
    if aliases:
        print("\nKind, Name, WWN")
        print("------------------")
        for alias in aliases:
            print(alias.kind + ", " + alias.name + ", " + alias.wwn)
        print("\n")   
    else:
        print("\nList of aliases is empty! Please add an alias manually or use a CSV file.\n")
    time.sleep(1)

def export_aliases_to_csv(aliases, file_name):
    with open(file_name,'w+', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for alias in aliases:
            writer.writerow([alias.kind,alias.name,alias.wwn])
        print("\n\tExport Successfull!\n")

def generate_alicreate_commands(aliases):
    if aliases:
        print("\n")
        for alias in aliases:
            print("alicreate \"" + alias.name + "\", \"" + alias.wwn + "\"")
        print("\n")
    else:
        print("\nList of aliases is empty! Please add an alias manually or use a CSV file.\n")
    time.sleep(1)

def generate_alidelete_commands(aliases):
    if aliases:
        print("\n")
        for alias in aliases:
            print("alidelete \"" + alias.name + "\"")
        print("\n")
    else:
        print("\nList of aliases is empty! Please add an alias manually or use a CSV file.\n")
    time.sleep(1)

def remove_alias(name):
    exist = False
    for alias in aliases:
        if name == alias.name:
            exist = True
            aliases.remove(alias)
            print("\n\tAlias deleted!\n")
            
    if not exist:
        print("\n\tAlias doesn't exist.\n")
    time.sleep(1)

# Welcome
print("""
WELCOME TO ZONGEN 0.2 - Zoning made easy!
Gonzalez I. - 22.12.2017
""")

# Main Menu 
menu = {}
menu['1'] = "Add an Alias Manually"
menu['2'] = "Import Aliases from CSV"
menu['3'] = "List Aliases"
menu['4'] = "Export Aliases to CSV"
menu['5'] = "Generate alicreate Commands"
menu['6'] = "Generate alidelete Commands"
menu['7'] = "Remove an Alias"
menu['90'] = "Quit"

while True:
    options = menu.keys()
    
    for entry in options:
        print(entry, menu[entry])

    selection = input("\nPlease Select: ")

    if selection == '1':
        add_alias_manually()
    elif selection == '2':
        file_path = input("\n\tCSV file path: ")
        import_aliases_from_csv(file_path)
    elif selection == '3':
        list_aliases(aliases)
    elif selection == '4':
        file_name = input("\n\tFile Name: ")
        export_aliases_to_csv(aliases,file_name)
    elif selection == '5':
        generate_alicreate_commands(aliases)
    elif selection == '6':
        generate_alidelete_commands(aliases)
    elif selection == '7':
        name = input("\n\tName of the alias to remove: ")
        remove_alias(name)
    elif selection == '90':
        print("\nGoodbye!\n")
        break
    else:
        print("\nUnknow Option Selected!\n")
        time.sleep(1)