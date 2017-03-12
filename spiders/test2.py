headers = ['Model', 'Year', 'Kilometers', 'Price', 'Address','Transmission', 'Body Type' ,'Colour' ,'No. of Doors', 'Drivetrain', 'Fuel Type' , 'Description' , 'Url', 'For Sale By','Trim']
attrs = [1,5,8,9,5]


possible_header = set(['Date Listed', 'Make' ,'Model', 'Year', 'Kilometers', 'Price', 'Address','Transmission', 'Body Type' ,'Colour' ,'No. of Doors', 'Drivetrain', 'Fuel Type' , 'Description' , 'Url', 'For Sale By','Trim'])
actual_header = set(headers)
to_add = list(possible_header-actual_header)
all_headers = headers + to_add


print(to_add)
print(all_headers)


for sve in range(len(to_add)):
    attrs.append('')

zipano = zip(all_headers,attrs)




print (zipano)