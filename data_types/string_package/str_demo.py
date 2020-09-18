# single line initialization
name:str = 'Sundar'

# multiple line initialization
about_me:str = ''' I am software developer with 7+ years experience in enterprise application development.
I have good knowledge in Core Java, Java8, Spring Framework, RESTful service, maven, GIT verison control, 
Sonar integration, Cassandra, AWS Neptune, AWS Dynamo and other AWS web services.'''

# print name and about_me
print('Name :',name)
print('\nAbout me :',about_me)

# access string using indexing. String is array of bytes representing unicode characters. It can be accessed using
# square brackets.
print('\nPrint first character from name :',name[0],' #Index start with 0')

# Slicing - return range of characters specify slice syntax.
# Start index - included (Should be less than end index)
# End index - not included.
print('\n## Slicing')
print(name[0:2],' Desxription: If start and end index having proper value, then result will be proper.')
print(name[2:2],' Description: If start and end index represent same value, then result will be empty.')
print(name[2:0],' Description: If start index value greater than end index, then result will be empty.')
print(name[0:8],' Description: If end index value greter than string length, then it will not throw any error')

# Negative Indexing
print('\nNegative Indexing')
print('Input-',name,'|Length-',len(name))
print(name[-3:-1])

# Length of the String variable
print('\nLength of the String variable')
print("Name:",name,"and it's length", len(name))

# Capitalize - Converts the first character to upper case
lastname:str='thambidurai'
print('Input-',lastname,'| Capitalize lastname-',lastname.capitalize())

# Count - No of times specified character occurs in a string.
print('Input-',lastname,'| Find character - a and count-',lastname.count('a'))


