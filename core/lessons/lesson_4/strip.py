filename = "    /var/usrbin/logs/test_log.log/     "

print(
    filename.strip() # прибирає зайві пробіли зліва та справа
)

print(
    filename.lstrip() # прибирає зайві пробіли зліва
)

print(
    filename.rstrip() # прибирає зайві пробіли справа
)


filename = "//var/usrbin/logs/test_log.log//"


print(
    filename.strip("/")
)