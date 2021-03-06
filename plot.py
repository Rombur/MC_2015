#! /usr/bin/env python
#----------------------------------------------------------------------------#
# Python code
# Author: Bruno Turcksin
# Date: 2014-10-15 16:40:20.728361
#----------------------------------------------------------------------------#

import pylab
import numpy as np

iteration = np.array([1.,1.5,2.,2.5,3.,3.5,4.,4.5,5.,5.5,6.,6.5,7.,7.5,8.,8.5,
    9.,9.5,10.,10.5,11.,11.5,12.,12.5,13.,13.5,14.,14.5,15.,15.5,16.,16.5,17.,
    17.5,18.,18.5,19.,19.5,20.])

central_148_1 = np.array([262.,246.,242.,242.,238.,238.,238.,238.,238.,238.,
    238.,238.,238.,238.,238.,238.,238.,238.,238.,238.,238.,238.,238.,238.,
    238.,238.,238.,238.,238.,238.,238.,238.,238.,238.,238.,238.,238.,238.,
    238.])
central_148_2 = np.array([269.,254.,250.,250.,250.,253.,250.,253.,250.,253.,
    250.,253.,250.,253.,250.,253.,250.,253.,250.,253.,250.,253.,250.,253.,
    250.,253.,250.,253.,250.,253.,250.,253.,250.,253.,250.,253.,250.,253.,
    250.])
central_148_3 = np.array([267.,259.,253.,249.,250.,247.,244.,247.,244.,246.,
    246.,247.,244.,246.,244.,246.,244.,246.,244.,246.,244.,246.,244.,246.,
    244.,246.,244.,246.,244.,246.,244.,246.,244.,246.,244.,246.,244.,246.,
    244.])
central_148_4 = np.array([279.,260.,259.,253.,256.,252.,257.,252.,252.,252.,
    252.,252.,252.,252.,252.,252.,252.,252.,252.,252.,252.,252.,252.,252.,
    252.,252.,252.,252.,252.,252.,252.,252.,252.,252.,252.,252.,252.,252.,
    252.])
                                         
pylab.figure(1)
pylab.plot(iteration,central_148_1,color='blue',linewidth=2.,linestyle='-',marker='D',markersize=7)
pylab.plot(iteration,central_148_2,color='red',linewidth=2.,linestyle='-',marker='D',markersize=7)
pylab.plot(iteration,central_148_3,color='green',linewidth=2.,linestyle='-',marker='D',markersize=7)
pylab.plot(iteration,central_148_4,color='black',linewidth=2.,linestyle='-',marker='D',markersize=7)
pylab.xlim(1,20)
pylab.xlabel('Number of iterations')
pylab.ylabel('Number of stages')
pylab.legend(['serial','random1','random2','iDFDS'])
pylab.xticks(np.linspace(1,20,20,endpoint=True))
pylab.savefig('convergence_central_148.png')

#----------------------------------------------------------------------------#

central_592_1 = np.array([360.,344.,336.,332.,332.,332.,332.,332.,332.,332.,
    332.,332.,332.,332.,332.,332.,332.,332.,332.,332.,332.,332.,332.,332.,
    332.,332.,332.,332.,332.,332.,332.,332.,332.,332.,332.,332.,332.,332.,
    332.])
central_592_2 = np.array([386.,375.,366.,363.,355.,355.,351.,355.,351.,351.,
    350.,347.,344.,346.,340.,338.,339.,338.,336.,342.,335.,341.,338.,338.,
    338.,338.,338.,337.,338.,337.,338.,337.,338.,337.,338.,337.,338.,337.,
    338.])
central_592_3 = np.array([387.,368.,359.,352.,348.,347.,343.,342.,342.,337.,
    340.,337.,340.,336.,336.,332.,337.,332.,337.,332.,337.,332.,337.,332.,
    337.,332.,337.,332.,337.,332.,337.,332.,337.,332.,337.,332.,337.,332.,
    337.])
central_592_4 = np.array([552.,475.,379.,365.,363.,349.,352.,348.,352.,348.,
    352.,348.,352.,348.,352.,348.,352.,348.,352.,348.,352.,348.,352.,348.,
    352.,348.,352.,348.,352.,348.,352.,348.,352.,348.,352.,348.,352.,348.,
    352.])

pylab.figure(2)
pylab.plot(iteration,central_592_1,color='blue',linewidth=2.,linestyle='-',marker='D',markersize=7)
pylab.plot(iteration,central_592_2,color='red',linewidth=2.,linestyle='-',marker='D',markersize=7)
pylab.plot(iteration,central_592_3,color='green',linewidth=2.,linestyle='-',marker='D',markersize=7)
pylab.plot(iteration,central_592_4,color='black',linewidth=2.,linestyle='-',marker='D',markersize=7)
pylab.xlim(1,20)
pylab.ylim(320,410)
pylab.xlabel('Number of iterations')
pylab.ylabel('Number of stages')
pylab.legend(['serial','random1','random2','iDFDS'])
pylab.xticks(np.linspace(1,20,20,endpoint=True))
pylab.savefig('convergence_central_592.png')

#----------------------------------------------------------------------------#

band_20_20_1 = np.array([593.,564.,559.,546.,543.,541.,533.,534.,531.,530.,
    530.,531.,530.,530.,526.,527.,525.,527.,525.,526.,522.,526.,524.,526.,
    523.,526.,523.,526.,523.,526.,523.,526.,523.,526.,523.,526.,523.,526.,
    523.])
band_20_20_2 = np.array([739.,698.,675.,638.,611.,612.,596.,599.,589.,589.,
    579.,587.,584.,580.,574.,579.,569.,568.,566.,563.,565.,559.,555.,556.,
    552.,554.,554.,547.,547.,548.,539.,542.,542.,543.,543.,543.,539.,544.,
    540.])
band_20_20_3 = np.array([733.,684.,669.,634.,631.,617.,608.,594.,601.,595.,
    579.,578.,578.,577.,568.,568.,565.,569.,560.,561.,555.,556.,548.,547.,
    548.,549.,545.,542.,541.,545.,541.,549.,544.,542.,544.,542.,543.,542.,
    536.])
band_20_20_4 = np.array([1161.,1125.,1113.,1109.,1062.,1063.,991.,968.,972.,
    964.,932.,920.,920.,910.,899.,850.,837.,776.,732.,688.,633.,612.,607.,
    571.,572.,565.,563.,561.,561.,562.,562.,565.,561.,558.,555.,556.,553.,
    557.,553.])

pylab.figure(3)                
pylab.plot(iteration,band_20_20_1,color='blue',linewidth=2.,linestyle='-',marker='D',markersize=7)
pylab.plot(iteration,band_20_20_2,color='red',linewidth=2.,linestyle='-',marker='D',markersize=7)
pylab.plot(iteration,band_20_20_3,color='green',linewidth=2.,linestyle='-',marker='D',markersize=7)
pylab.plot(iteration,band_20_20_4,color='black',linewidth=2.,linestyle='-',marker='D',markersize=7)
pylab.xlim(1,20)
pylab.ylim(520,620)
pylab.xlabel('Number of iterations')
pylab.ylabel('Number of stages')
pylab.legend(['serial','random1','random2','iDFDS'])
pylab.xticks(np.linspace(1,20,20,endpoint=True))
pylab.savefig('convergence_band_20_20.png')

#----------------------------------------------------------------------------#

band_40_40_1 = np.array([885.,887.,884.,884.,884.,884.,884.,884.,884.,884.,
    884.,884.,884.,884.,884.,884.,884.,884.,884.,884.,884.,884.,884.,884.,
    884.,884.,884.,884.,884.,884.,884.,884.,884.,884.,884.,884.,884.,884.,
    884.])
band_40_40_2 = np.array([1175.,1109.,1030.,1014.,989.,959.,938.,930.,937.,926.,
    936.,923.,934.,925.,934.,925.,934.,922.,934.,922.,934.,925.,937.,925.,
    934.,925.,934.,925.,937.,925.,937.,925.,934.,925.,937.,925.,937.,925.,
    934.])
band_40_40_3 = np.array([1103.,1040.,1008.,982.,964.,945.,934.,929.,909.,913.,
    905.,907.,905.,907.,905.,907.,906.,907.,905.,907.,905.,907.,905.,907.,
    906.,907.,906.,907.,906.,907.,906.,907.,906.,907.,906.,907.,905.,907.,
    905.])
band_40_40_4 = np.array([2112.,1975.,1851.,1757.,1767.,1576.,1554.,1526.,1380.,
    1336.,1326.,1271.,1244.,1208.,1152.,1119.,1076.,1013.,986.,984.,948.,934.,
    903.,899.,899.,898.,899.,898.,899.,898.,899.,898.,899.,898.,899.,898.,
    899.,898.,899.])

pylab.figure(4)                
pylab.plot(iteration,band_40_40_1,color='blue',linewidth=2.,linestyle='-',marker='D',markersize=7)
pylab.plot(iteration,band_40_40_2,color='red',linewidth=2.,linestyle='-',marker='D',markersize=7)
pylab.plot(iteration,band_40_40_3,color='green',linewidth=2.,linestyle='-',marker='D',markersize=7)
pylab.plot(iteration,band_40_40_4,color='black',linewidth=2.,linestyle='-',marker='D',markersize=7)
pylab.xlim(1,20)
pylab.ylim(880,980)
pylab.xlabel('Number of iterations')
pylab.ylabel('Number of stages')
pylab.legend(['serial','random1','random2','iDFDS'])
pylab.xticks(np.linspace(1,20,20,endpoint=True))
pylab.savefig('convergence_band_40_40.png')
