#-*- coding:utf-8 -*-
import math
def ComputeEuclideanDistance(x1,y1,x2,y2):
    d = math.sqrt(math.pow(x1-x2,2) + math.pow(y1-y2,2))
    return d

d_ag = ComputeEuclideanDistance(3,104,18,90)
d_bg = ComputeEuclideanDistance(2,100,18,90)
d_cg = ComputeEuclideanDistance(1,81,18,90)
d_dg = ComputeEuclideanDistance(101,10,18,90)
d_eg = ComputeEuclideanDistance(99,5,18,90)
d_fg = ComputeEuclideanDistance(98,2,18,90)

print "ag两点的距离:", d_ag
print "bg两点的距离:", d_bg
print "cg两点的距离:", d_cg
print "dg两点的距离:", d_dg
print "eg两点的距离:", d_eg
print "fg两点的距离:", d_fg