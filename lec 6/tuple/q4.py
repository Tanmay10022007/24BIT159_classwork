import operator
lst=[("pizza",300),("burger",180),("cola",75)]

print (sorted(lst, key = operator.itemgetter(1),reverse=True))
