try:
    import psutil
except:
    print("psutil doesn't exist")
    import pip
    pip.main(["install", "psutil"])
    import psutil
    print("psutil installed!")

memory_percentage = psutil.virtual_memory()[2]
cpu_usage = psutil.cpu_percent(interval=1)
print (memory_percentage)
print (cpu_usage)
print (psutil.cpu_count())

print (psutil.disk_partitions())
print (psutil.disk_usage('/'))

print (psutil.net_if_addrs())

print (psutil.sensors_temperatures(fahrenheit=True))
