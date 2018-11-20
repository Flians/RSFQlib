*****************************************
* Begin .SUBCKT model                    *
* spice-sdb ver 4.28.2007                *
*                                        *
*		        Version: 1.1			 *
*										 *
* Modified 26 Oct 2018, L Schindler, SU  *
*   (Updated parameter values)	         *
* Last mod 20 Nov 2018, L Schindler, SU  *
******************************************
*                 IN   OUT
*$Ports          in_in out_out
.SUBCKT mitll_sfqdc 2 37
*********************************************************
*==============  Begin SPICE netlist of main design ============
B01        1          12         jmitll     area=1.96
B02        3          13         jmitll     area=1.96
B03        6          14         jmitll     area=1.96
B04        9          15         jmitll     area=1.44
B05        17         18         jmitll     area=1.44
B06        21         20         jmitll     area=2.33
B07        28         18         jmitll     area=2.56
B08        24         23         jmitll     area=1.32
B09        31         33         jmitll     area=1.32
IB01       0          42         pwl(0      0 5p 280u)
IB02       0          11         pwl(0      0 5p 176u)
IB03       0          10         pwl(0      0 5p 182u)
IB04       0          38         pwl(0      0 5p 148u)
IB05       0          32         pwl(0      0 5p 215u)
IB06       0          36         pwl(0      0 5p 456u)
L01        2          1          2.168p    
L02        4          3          3.429p    
L03        3          5          1.56p     
L04        5          6          1.563p    
L05        6          7          2.844p    
L06        7          8          0.234p    
L07        8          9          0.853p    
L08        17         8          1.557p    
L09        23         20         4.839p    
L10        18         26         5.278p    
L11        24         30         0.003p    
L12        30         31         0.143p    
L13        33         35         1.802p    
L14        35         0          0.702p    
L15        30         37         7.21p     
L16        15         20         0.494p    
L17        23         26         0.001p    
L20        1          4          0.2p      
LP01       0          12         0.172p    
LP02       0          13         0.153p    
LP03       0          14         0.109p    
LP06       21         0          0.837p    
LP07       28         0          0.855p    
LPR01      4          42         0.169p    
LPR02      5          11         0.192p    
LPR03      7          10         0.239p    
LPR04      15         38         0.078p    
LPR05      31         32         2.145p    
LPR06      35         36         0.013p    
LPR07      26         27         0.45p     
LRB01      12         39         1p        
LRB02      13         40         1p        
LRB03      14         41         1p        
LRB04      16         15         1p        
LRB05      19         18         1p        
LRB06      22         21         1p        
LRB07      29         28         1p        
LRB08      25         24         1p        
LRB09      34         33         1p        
R07        27         0          0.3       
RB01       39         1          5.765     
RB02       40         3          5.765     
RB03       41         6          5.765     
RB04       9          16         7.847     
RB05       17         19         7.847     
RB06       22         20         4.85      
RB07       29         18         4.414     
RB08       25         23         8.561     
RB09       31         34         8.561     
.model jmitll jj(rtype=1, vg=2.8mV, cap=0.07pF, r0=160, rn=16, icrit=0.1mA)
.ends mitll_sfqdc