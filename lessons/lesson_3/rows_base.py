one_line_v1: str = ('Це одинарний рядок. Він використовується для того щоб написати тут якийсь текст в одну лінію.'
                    ' уоцршграшгршгрцушгршгргашршгуощшмнгисч')
one_line_v2: str = ("Це подвійний "
                    "рядок.")
print(one_line_v1)
print(one_line_v2)
# ---------------------------------
three_line_v1: str = ''' Це
    трьохкратний
  рядок.''' # тут три фізичних лінії, проте лише одна логічна лінія

three_line_v2: str = """Це
            трьохкратний
 рядок.""" # тут три фізичних лінії, проте лише одна логічна лінія

print(three_line_v1)

print(three_line_v2)

# docstring
def test_some_func():
    """
    This test is checking some function.
    Description of func is ...
    """
    pass

# ------------------------------------

bio: str = 'I\'m Bohdan. \nI like testing and AQA'
bio_v2: str = "I'm Bohdan. I like testing and AQA"

print(bio)
print(bio_v2)


string_v1 = 'Name of our company is "Hillel"'
string_v2 = "Name of our company is \"Hillel\""
string_v3 = '''Name of our company is "Hillel"'''
string_v4 = """Name of our 
company is 
'Hillel'"""


print(string_v1)
print(string_v2)
print(string_v3)
print(string_v4)

user_id = 123456789
actual_status_code = 401
json_response = {"error": "Unauthorized",
                 "msg": "User is not authorized",
                 "status_code": actual_status_code,
                 "user_id": user_id,
                }
log_payment = f'I\'m Making payment operation for user {user_id}. \nExpected status_code: 200 \nActual status_code: {actual_status_code} \nResponse_body: {json_response}'
print(log_payment)


descr = "\\n is symbol for new line"
print(descr)