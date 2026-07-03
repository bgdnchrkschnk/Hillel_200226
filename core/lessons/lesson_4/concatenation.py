# cancatenation (+)

error_message: str = "ValueError"
details_error: str = "Invalid input data"

log_message_fstring = f"ERROR: {error_message} - {details_error}"

print(log_message_fstring)


log_message_conc: str = "ERROR: " + error_message + " - " + details_error
print(log_message_conc)


print(
    "Bohdan" + " - " + "Cherkashchenko"
)