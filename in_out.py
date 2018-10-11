import numpy as np
import matplotlib.pyplot as plt
import h5py as h5
import time


def plainSave( arr, filename ):

    f = open( filename, "w" )

    for row in arr:
        line = " ".join([str(x) for x in row ])
        line += "\n"
        f.write(line)

    f.close()

def plainLoad( filename ):

    f = open( filename, "r" )

    arr = []
    for line in f:
        words = line.split()
        row = [float(x) for x in words]
        arr.append(row)

    f.close()
    return np.array( arr )

def numpySave( arr, filename ):
    np.savetxt( filename, arr )

def numpyLoad( filename ):
    return np.loadtxt( filename )

def hdf5Save( arr, filename ):

    f = h5.File( filename, "w" )

    dset = f.create_dataset("array", arr.shape, dtype=np.float )
    dset[...] = arr

    f.close()

def hdf5Load( filename ):

    f = h5.File( filename, "r" )

    arr = f['array'][...]

    f.close()
    return arr

def makeArray( shape ):
    return np.random.rand( *shape )

if __name__=="__main__":

   shape = (1000, 1000)
   a = makeArray( shape )

   t1 = time.time()
   plainSave( a, "plain.txt" )
   b = plainLoad( "plain.txt" )
   t2 = time.time()

   t3 = time.time()
   numpySave( a, 'numpy.txt' )
   c = numpyLoad( 'numpy.txt' )
   t4 = time.time()

   t5 = time.time()
   hdf5Save( a, 'data.h5' )
   d = hdf5Load('data.h5' )
   t6 = time.time()

   print "\nFileTest\n"
   print "size: ", a.shape
   print

   print "Python time: ", t2-t1
   print "      err: ", np.abs(b-a).sum()
   print "Numpy time ", t4-t3
   print "      err: ", np.abs(c-a).sum()
   print "HDF5 time ", t6-t5
   print "      err: ", np.abs(d-a).sum()




