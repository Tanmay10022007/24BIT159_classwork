d = {
    "dept1":{1:20000,2:65800,3:45760},
    "dept2":{1:10000,2:85800,3:95760},
    "dept3":{1:40000,2:25800,3:35760}
}
for i in d:
    print("Department:",i)
    print("Minimum salary:",min(d[i].values()))
    print("Maximum salary:",max(d[i].values()))
    
    print()