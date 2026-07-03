config = "host=localhost;port=5432;user=admin"


separator = ","

config_normalized = config.replace(";", separator, 1)

print(config_normalized)