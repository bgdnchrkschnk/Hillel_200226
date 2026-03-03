csv_row = "id123;Bohdan;QA Engineer;Odesa"


list_of_values: list[str] = csv_row.split(";") # розрізаю по роздільнику

print(list_of_values)


text_line = (" На цьому занятті викладач пояснює важливість систем контролю версій, зокрема Git, "
             "у процесі розробки програмного забезпечення.")

list_of_words: list[str] = text_line.split()
list_of_words_v2: list[str] = text_line.split(" ")

print(list_of_words)
print(list_of_words_v2)


text_lines = ("На цьому занятті викладач пояснює важливість систем контролю версій, зокрема Git, у процесі розробки програмного забезпечення. "
              "Він роз'яснює, що Git дозволяє організувати роботу в команді, ведучи контроль над змінами в коді, що включає в себе історію версій, можливість огляду та відкату змін. "
              "Викладач розглядає різні типи систем контролю версій, такі як локальні, централізовані та розподілені системи, "
              "зосереджуючись на перевагах використання Git, який є найпоширенішим у середовищі розробників.")


text_sentences: list[str] = text_lines.split(". ")

print(text_sentences)


#-------------------------------- split - розрізати строчку -> list[str]

# -------------------------------------------------- .join() - з колекції зклеїти елементи в одну строчку


new_joined_text = " ".join(list_of_words)
print(new_joined_text)



my_name = "Bohdan"
my_age = 29
my_friends = ["Oleg", "Ivan", "Mykola"]

my_friends_str = ", ".join(my_friends)


my_biography = f"My name is {my_name}, I am {my_age} years old, and my friends are {my_friends_str}"

print(my_biography)