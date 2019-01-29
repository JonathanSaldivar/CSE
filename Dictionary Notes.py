states = {
    'CA': 'California',
    'NJ': 'New Jersey',
    'WI': 'Wisconsin',
    'NY': 'New York'
}

print(states['CA'])
print(states['WI'])

nested_dictionary = {
    'CA': {
        'NAME': 'California',
        'POPULATION': 39500000  # 39,500,000
    },
    'NJ': {
        'NAME': 'New Jersey',
        'POPULATION': 9000000  # 9,000,000
    },
    'WI': {
        'NAME': 'Wisconsin',
        'POPULATION': 5800000  # 5,800,000
    },
    'NY': {
        'NAME': 'New York',
        'POPULATION': 19500000  # 19,500,000
    }
}

print(nested_dictionary['CA'])
print(nested_dictionary['CA']['POPULATION'])

complex_dictionary = {
    'CA': {
        'NAME': 'CALIFORNIA',
        'POPULATION': 39500000,
        'CITIES': [
            'FRESNO',
            'SAN FRANCISCO',
            'Los Angeles'
        ]
    },
    'NY': {
        'NAME': 'New York',
        'POPULATION': 19500000,  # 19,500,000
        'CITIES': [
            'New York City',
            'Rockester',
            'Buffalo'
        ]
    }
