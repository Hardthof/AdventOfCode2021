import cProfile
from statistics import mean

def fuelCost2(seq, v):
    return sum([abs(v-e) for e in seq])

def fuelCost(seq, v):
    dis = [abs(v-e) for e in seq]
    s = [(n*n + n) / 2 for n in dis if n != 0]
    return sum(s)

if __name__ == '__main__':

    #f = "16,1,2,0,4,2,7,1,2,14"
    f = "1101,1,29,67,1102,0,1,65,1008,65,35,66,1005,66,28,1,67,65,20,4,0,1001,65,1,65,1106,0,8,99,35,67,101,99,105,32,110,39,101,115,116,32,112,97,115,32,117,110,101,32,105,110,116,99,111,100,101,32,112,114,111,103,114,97,109,10,841,69,1401,423,17,18,427,405,56,624,1657,333,194,691,31,130,951,165,1952,483,109,126,67,163,457,542,808,75,418,21,483,22,648,447,153,41,1267,114,1531,6,456,841,42,908,256,136,18,326,69,1300,626,28,943,326,225,53,1254,707,20,792,141,470,178,337,280,181,977,153,213,300,919,1540,1667,245,732,257,137,762,1637,968,511,409,605,402,456,0,1269,166,82,359,416,315,95,66,477,1375,816,255,2,1084,1396,84,343,173,215,128,314,856,696,210,350,1111,709,517,39,6,8,503,166,94,387,1254,281,231,515,125,618,267,316,682,684,1118,12,927,548,151,907,222,915,618,14,859,131,750,293,1067,857,248,750,161,466,101,263,44,9,21,612,201,13,51,989,281,30,119,521,36,21,1705,21,451,12,264,813,218,1097,640,154,421,386,395,359,706,313,215,615,502,0,15,20,665,379,524,164,419,872,1113,131,76,211,422,27,611,308,162,1125,879,68,661,154,166,556,279,1160,389,315,213,791,396,608,269,844,470,856,450,268,408,1817,1040,1574,423,868,43,132,886,37,43,109,19,485,1185,1251,1070,258,345,42,334,221,730,563,152,5,1326,97,551,139,1701,296,371,577,694,1152,191,1056,26,511,566,446,431,858,967,303,962,325,121,1660,26,928,156,320,51,328,998,466,809,22,1685,489,260,258,1005,330,243,241,1130,1143,607,549,69,276,20,175,91,1081,227,1219,1597,66,110,11,73,238,78,1299,814,1051,261,54,61,678,44,439,249,115,251,232,14,294,195,336,334,113,420,70,186,34,31,590,412,330,1182,310,316,426,235,485,303,561,961,121,171,59,132,513,239,1277,519,324,102,245,172,283,292,663,10,852,1132,434,1046,1671,1208,32,1249,221,176,13,80,730,354,743,308,662,1016,148,333,179,100,1698,719,157,392,329,400,790,368,437,174,1577,14,388,844,132,82,294,140,3,363,215,56,1330,481,171,539,1670,78,1590,757,1357,15,863,295,448,340,420,569,542,750,49,23,803,122,1079,489,1281,75,1055,938,245,137,221,664,254,1179,15,225,529,829,346,128,380,295,388,51,1038,1001,223,256,611,965,189,664,1676,825,282,417,394,202,434,513,529,2,395,797,1683,771,176,207,32,129,385,99,204,513,132,365,644,2,37,618,228,282,363,991,475,1476,91,843,1347,130,1683,737,53,684,501,323,274,88,214,558,6,858,190,129,38,1294,343,266,73,1379,179,190,290,506,37,163,832,46,407,474,920,136,1220,1305,113,208,514,917,93,125,82,1222,116,426,921,296,276,717,867,792,643,48,1326,233,550,385,638,672,184,1189,23,267,302,222,149,904,660,452,53,32,744,749,235,124,588,762,130,17,885,1464,1813,208,732,597,881,154,155,844,446,653,820,60,420,476,591,101,898,1124,100,750,20,554,699,1109,997,1093,1109,279,1020,246,62,46,1830,2,514,3,54,310,90,140,584,852,649,58,166,517,563,317,437,910,365,26,170,124,147,145,46,500,124,475,689,1277,227,116,570,965,524,6,250,327,39,365,1058,5,840,681,199,1070,29,840,148,290,189,93,265,1775,1244,374,210,85,61,460,36,1157,1019,1338,644,624,1101,927,228,413,18,1312,612,374,520,1801,362,656,569,593,165,38,76,9,912,149,36,386,280,1279,512,568,963,347,75,327,268,629,10,260,67,1299,963,932,245,452,890,953,1140,544,523,288,316,317,761,283,907,552,9,259,1270,722,129,362,81,571,222,33,362,542,111,107,50,285,213,304,421,362,1751,219,57,766,1096,1333,48,597,730,910,129,559,962,170,59,246,4,1094,328,733,105,65,837,213,174,3,133,757,148,26,558,309,636,40,1615,757,478,1080,9,499,499,1224,0,871,457,34,738,489,322,55,36,24,369,1056,232,217,196,169,204,114,1097,239,471,681,45,853,782,832,322,441,269,1413,1100,95,51,70,763,456,194,310,614,266,31,754,13,561,904,303,266,1567,34,1707,370,629,13,378,144,527,48,520,1348,322,401,454,423,528,29,619,430,916,974,74,1321,940,504,365,240,1801,1045,267,622,424,1481,1020,121,546,208,138,487,622,1557,379,249,148,500,51,828,447,260,1241,585,219,108,601,772,979,1774,12,20,356,405,342,558,19,334,161,235,328,55,233,644,201,645,149,230,201,1305,26,943,207,253,1477,559,120,1015,31,494,87,393,1740,315,195,328,2,472,101,995"
    seq = [int(n) for n in f.split(',')]
    #seq.sort()
    meanv = round(mean(seq))
    currentCost = (fuelCost(seq, meanv))

    costLeft = (fuelCost(seq, meanv-1))
    costRight = (fuelCost(seq, meanv+1))

    direction = 'r'
    newValue = costRight
    if costLeft < costRight: 
        direction = 'l'
        newValue = costLeft

    if direction == 'r': meanv += 1
    else: meanv -= 1

    while currentCost > newValue:
        if direction == 'r': meanv += 1
        else: meanv -= 1
        currentCost = newValue
        newValue = fuelCost(seq, meanv)

    if direction == 'r': meanv -= 1
    else: meanv += 1

    print(currentCost, meanv)