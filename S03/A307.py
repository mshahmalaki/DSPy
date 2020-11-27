person = {'Name': 'Pouriya',
          'Birth': 1362,
          'Code': 510}
this_year = 1399
if (this_year - person['Birth']) > 30:
    print('Middle age')
    person['Status'] = 'Middle age'
    print(person)
