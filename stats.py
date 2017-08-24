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
    @staticmethod
    def usage():
        #return str(psutil.cpu_percent(interval=1)) + "%"
        psutil.cpu_percent(interval=1)
        return psutil.cpu_times_percent(interval=1)

    def cores():
        return psutil.cpu_count()

    def uptime():
        epoch = psutil.boot_time()
        return datetime.datetime.fromtimestamp(epoch)

class MEMORY(object):
    @staticmethod
    def usage():
        return psutil.virtual_memory()[2]

#print (memory_percentage)
print (CPU.usage())
print (CPU.cores())
print (CPU.uptime())
#print (psutil.cpu_stats())

#print (psutil.disk_partitions())
#print (psutil.disk_usage('/'))
#print (psutil.users())

