# imu-data
IMU dataset(s) 

00 - phone in jacket front pocket
01 - phone in trouser pocket, IMU on helmet, IMU on bike

## Set 00

GPS and IMU data from mobile phone. Phone in jacket front pocket (substantially vertically oriented, upright, screen facing to the rear).
 
## Set 01

GPS data from phone. Phone in trouser pocket (substantially diagonally oriented, screen down and to the rear).
IMU data from IMU unit on helmet (Y upwards, tilted back)
IMU data from IMU unit on bike (Z upwards, tilted back)


![orientations](./img/set01.jpg)

At the very end of the data set, there are two periods of temporary parking with the rider looking straight ahead. The last one is on an almost flat road, and could be used for finding the stationary position of the IMU units on the helmet and bike.

The files have been approximately aligned in time, however it may be necessary to look for vertical accelerations in common between the helmet and bike IMU arising from pot-holes in the road to check/adjust the alignment. The sample rate in all three files is different. 

### Issues

The timestamps in the IMU data appear to have an issue, where it seems the data points are out of order - but I think this is a formatting error in the routine in the IMU that created the time string. For example, 00:16:31.18 should be 00:16:31:018. This can be fixed by implementing a search for times with 2 decimal places in the fraction, and adding a leading zero. 

```
80    00:16:30.818    -0.018    0.187    0.970    -39.185    23.926    -64.514    1.02    5.66    135.74    2220    -352    -734    47    0.000000    0.000000    0    0    0
80    00:16:30.918    -0.366    0.214    0.929    0.488    -27.771    -61.707    -0.16    5.06    134.76    2219    -359    -712    56    0.000000    0.000000    0    0    0
80    00:16:31.18    0.089    0.296    0.665    2.319    -69.336    -147.827    -1.05    1.88    127.12    2224    -406    -710    61    0.000000    0.000000    0    0    0
80    00:16:31.118    0.529    0.154    0.884    31.006    -6.836    -31.921    2.84    -3.27    122.05    2214    -481    -730    65    0.000000    0.000000    0    0    0
80    00:16:31.218    0.259    0.305    0.987    32.898    33.569    49.866    6.95    -1.32    128.80    2221    -489    -755    60    0.000000    0.000000    0    0    0
```

### Trimming

`sed` was be used to trim lines from the data files to achieve alignment in time.

e.g. for removing the first unnneded lines, but keeping the header:

```
sed -i 2,4128d bike.csv
```

and for removing the last unneeded lines

```
tac bike.csv | sed '1,4764d' | tac  > bike.csv
```

## Set 02

GPS and IMU data from a [racebox micro](https://www.racebox.pro/products/racebox-micro) mounted on a bike running at a track. This is an example of the data available from this device, for consideration of whether it could be helmet mounted.

