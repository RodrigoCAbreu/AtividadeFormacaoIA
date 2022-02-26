import pycuda.driver as drv 

drv.init() 

print ("%d Dispositivo(s) encontrados." % drv.Device.count())

for ordinal in range(drv.Device.count()): 
       dev = drv.Device(ordinal) 
       print ("Dispositivo #%d: %s" % (ordinal, dev.name())) 
       print (" Compute Capability: %d.%d" % dev.compute_capability())     
       print (" Total Memory: %s KB" % (dev.total_memory()//(1024))) 