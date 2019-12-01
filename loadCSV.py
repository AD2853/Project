def importCsv(filePath):
    """Import vstupního CSV souboru - data načtena do slovníku 'd', kde klíče jsou názvy sloupců ze vstupního CSV. Funkce vrátí vytvoření slovník 'd'. """
    d = {}
    with open(filePath, newline='', encoding='utf-8-sig') as csvFile:
        reader = csv.reader(csvFile)
        for i in list(reader)[0]:
            d[i] = []    

    with open(filePath, newline='', encoding='utf-8-sig') as csvFile:
        reader2 = csv.DictReader(csvFile)
        for row in reader2:
            for key in row:
                d[key].append(row[key])
    return(d)
