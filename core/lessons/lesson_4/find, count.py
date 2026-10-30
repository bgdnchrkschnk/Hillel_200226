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

first_critical = log_data.find("CRITICAL:")
second_critical = log_data.find("CRITICAL:", first_critical + 1)

start_first = first_critical + len("CRITICAL: ")
start_second = second_critical + len("CRITICAL: ")

end_first = log_data.find("\n", start_first)
end_second = log_data.find("\n", start_second)

print(log_data[start_first:end_first])
print(log_data[start_second:end_second])

# ----------------------------------

critical_messages = log_data.count("ERROR")
print(critical_messages)






