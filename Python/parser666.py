import phonenumbers
import pycountry
from phonenumbers.phonenumberutil import PhoneMetadata
from phonenumbers import geocoder
from phonenumbers.phonenumberutil import (
    region_code_for_country_code,
    region_code_for_number,
    national_significant_number
)
from phonenumbers import carrier
from phonenumbers import timezone

text = '+16473612505'
text1 = '+73812332308'

x=phonenumbers.parse(text1, None)
print(x)

y=str(geocoder.country_name_for_number(x, "en"))
print(y)

z=str(geocoder.description_for_number(x, "en"))
print(z)

code=region_code_for_country_code(x.country_code)
print(code)

country = pycountry.countries.get(alpha_2=str(code))
print(country)

#short = national_significant_number(text1)
short1= PhoneMetadata.short_metadata_for_region(code)
print(short1)