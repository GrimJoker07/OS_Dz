def Zad4():
    import xml.etree.ElementTree as ET
    import os

    first_name = input("First name")
    last_name = input("Last name")
    city = input("City")

    items = [
        {"first_name": first_name, "last_name": last_name, "city": city},
    ]

    root = ET.Element('root')

    for i, item in enumerate(items, 1):
        person = ET.SubElement(root, 'person' + str(i))
        ET.SubElement(person, 'first_name').text = item['first_name']
        ET.SubElement(person, 'last_name').text = item['last_name']
        ET.SubElement(person, 'city').text = item['city']

    tree = ET.ElementTree(root)
    tree.write('xmlf.xml')

    with open('xmlf.xml') as f:
        print(f.read())

    os.remove('xmlf.xml')