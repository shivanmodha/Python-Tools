try:
    import psutil
except:
    print("psutil doesn't exist")
    import pip
    pip.main(["install", "psutil"])
    import psutil
    print("psutil installed!")

print(psutil.virtual_memory()[2])
