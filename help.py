flag = False
rawData = ''
while not flag:
    filepath = 'gff.txt '#input("Please enter Data directory: ")
    try:
        reader = open(filepath, 'r')
    except:
        print(filepath, "Not Found")
        continue
    rawData = reader.read()
    flag = True

dataMap = {
    'region': [],
    'gene': [],
    'CDS': [],
    'tRNA': [],
    'rRNA': [],
    'exon': [],
    'pseudogene': [],
    'RNase_P_RNA': [],
    'SRP_RNA': [],
    'tmRNA': []
}

rawDatalist = rawData.split('\n')

datalist = rawDatalist[9:-1:]

keylist = dataMap.keys()

for i in range(len(datalist)):
    rawfeatures = datalist[i].split('ID=')
    cutfeatures = str(rawfeatures[:-1])
    idFeatures = rawfeatures[-1]
    features = cutfeatures.split('\\t')
    #print(features)


    keycounter = 0
    for key in keylist:
        if key in features or key.lower() in features:
            dataMap[key] += [[features, idFeatures]]
            keycounter += 1
    if keycounter > 1:
        print(features)
math = 0
for key in keylist:
    math += len(dataMap[key])
    print("feature type: {0}, number of occurences: {1} ".format(key, len(dataMap[key])))

cds_Map = {

}

cds_data = dataMap['CDS']
cds_clean_data = []
print(cds_data[0][1])
for i in range(len(cds_data)):
    cds_clean_data.append([cds_data[i][1]])

for cds in cds_clean_data:
    for i in range(len(cds)):
        cds.find()