config_db: str = "host=localhost;port=5432;user=admin;password=secret"

host_index = config_db.find("host=") # index = 0
port_index = config_db.find("port=") # -> int (index)
user_index = config_db.find("user=")
password_index = config_db.find("password=")

host_value_index_start = host_index + 5
host_value = config_db[host_value_index_start:port_index - 1]

print(host_value)
# ----------------------------
log_data = """
INFO: Service started
CRITICAL: Database connection failed 
CRITICAL: Timeout occurred
WARNING: High memory usage
"""

first_critical_index = log_data.find("CRITICAL") # -> index
error_message_index_start = first_critical_index + 10

second_critical_index = log_data.find("CRITICAL", first_critical_index +1) # - (text_fragment, start_from)


print(second_critical_index)

print(
    log_data.find("ERROR")
)



# ----------------------------------

critical_messages = log_data.count("ERROR")
print(critical_messages)






