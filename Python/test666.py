import csv
from typing import Dict, Any

import phonenumbers
from phonenumbers import geocoder
from phonenumbers.phonenumberutil import (
    region_code_for_country_code,
    region_code_for_number,
)
import pycountry

with open("Equant_MSK.csv", mode='r', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    for line in csv_reader:  # type: Dict[Any, Any]
        code = line["CODE"]  # type: str
        print(code)

        x = phonenumbers.parse(code, "EN")
        print(x)

#        y = geocoder.country_name_for_number(x, "en")
#        print(y)
        z=region_code_for_country_code(x.country_code)
        print(z)

        country = pycountry.countries.get(alpha_2=str(z))
        print(country.name)