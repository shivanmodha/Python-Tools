''' Statistic script, enabling access to computer usage stats '''
import datetime
try:
    import psutil
except:
    print("psutil doesn't exist")
    import pip
    pip.main(["install", "psutil"])
    import psutil
    print("psutil installed!")

class CPU(object):
    def usage():
        psutil.cpu_percent(interval=1)
        return psutil.cpu_percent(interval=1)
    def cores():
        return psutil.cpu_count()
    def uptime():
        epoch = psutil.boot_time()
        return datetime.datetime.fromtimestamp(epoch)

class MEMORY(object):
    def usage():
        return psutil.virtual_memory()[2]

class DISK(object):
    def partitions():
        obj = {}
        partitions = psutil.disk_partitions()
        for i in range(0, len(partitions)):
            usage = "Unknown"
            try:
                usage = psutil.disk_usage(partitions[i][1])[3]
            except:
                pass
            obj[partitions[i][0]] = { "Mount Point": partitions[i][1], "Type": partitions[i][2], "Attributes": partitions[i][3], "Usage": usage }
        return obj

class SYSTEM(object):
    def users():
        obj = {}
        users = psutil.users()
        for i in range(0, len(users)):
            epoch = datetime.datetime.fromtimestamp(users[i][3]).strftime("%Y-%m-%d %H:%M:%S")
            obj[users[i][0]] = { "Started": epoch }
        print (users)
        return obj

print ("CPU Usage: " + str(CPU.usage()))
print ("CPU Cores: " + str(CPU.cores()))
print ("CPU Uptime: " + str(CPU.uptime()))
print ("MEMORY Usage: " + str(MEMORY.usage()))
print ("DISK Partitions: " + str(DISK.partitions()))
print ("Users: " + str(SYSTEM.users()))
