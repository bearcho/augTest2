selloutData = pd.read_csv("../dataset/kopo_channel_seasonality_new.csv")




sortKey = ["REGIONID", "PRODUCT", "YEARWEEK"]

selloutData.sort_values(sortKey, inplace=True)

selloutData["MA"] = selloutData["QTY"].rolling(window=5, center=True, min_periods=1).mean()

selloutData.head()
 # 여기서 문제는 상품간 경계값에서 타상품의 QTY에 영향받을 수 있다







# 타 상품에 영향받지 않는 방법

selloutData = pd.read_csv("../dataset/kopo_channel_seasonality_new.csv")

groupKey = ["REGIONID", "PRODUCT"]




def rollingma(onegroup):

    #onegroup = groupData2.get_group( list(groupData2.groups)[793] )
     
     eachgroup = onegroup.reset_index(drop=True)
     eachgroup["MAG5"] = eachgroup["QTY"].rolling(window=5, center=True, min_periods=1).mean()

    return eachgroup




groupResult = selloutData.groupby(groupKey).apply(rollingma)
 groupResult.head()  
