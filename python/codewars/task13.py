def people_with_age_drink(age):
    match age:
        case x if x < 14:
            return 'drink toddy'
        case x if x < 18:
            return 'drink coke'
        case x if x < 21:
            return 'drink beer'
        case x if x >= 21:
            return 'drink whisky'
    return ''


print(people_with_age_drink(13))
print(people_with_age_drink(0))
print(people_with_age_drink(17))
print(people_with_age_drink(15))
print(people_with_age_drink(14))
print(people_with_age_drink(20))
print(people_with_age_drink(18))
print(people_with_age_drink(22))
print(people_with_age_drink(21))

