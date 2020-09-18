# This example will demonstrate how Python data types can be initialized.

# str - (String) Sequence of characters such as 'Sundar', "Suganya"
# int - (Integer) Whole numbers such as 3, 300
# float - (Float) Numbers with decimal points such as 1.0, 125.89
# list - (List) Insertion ordered and changeable collection. Allow duplicates
# dict - (Dictionaries) Unordered, changeable and indexed key:value pairs and don't allow duplicates based on key value.
# tuple - (Tuple) Insertion ordered and unchangeable collection. Allow duplicates
# Set - (Set) Unordered collection and Hold only unique values.
# bool - (Boolean) Logical value True or False

name: str = 'Sundar'
age: int = 30
height: float = 172.3
family_members: list = ['Sundar', 'Suganya', 'Mithran']
family_hierarchy: dict = {'Dad': 'Sundar', 'Mom': 'Suganya', 'Son': 'Mithran'}
dob: tuple = ('09-Mar-1991', '19-Feb-1991', '17-Nov-2018')
grand_parents: set = {'Thambidurai', 'Murugeswari'}
is_happy: bool = True

print('Name ::', name, ' #String')
print('Age :: ', age, '#Integer')
print('Height :: ', height, '#Float')
print('Family Members :: ', family_members, '#List')
print('Family Hierarchy :: ', family_hierarchy, '#Dictionary')
print('DOB :: ', dob, '#Tuple')
print('Grand Parents :: ', grand_parents, ' #Set')
print('Happy :: ', is_happy, '#Boolean')
