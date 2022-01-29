﻿import arcpy
#выбрать рабочее пространство 
workspace = arcpy.GetParameterAsText(0)
#задаем рабочее пространство 
arcpy.env.workspace = workspace 
#папка для сохранения shp
myfolder=arcpy.GetParameterAsText(1)
#список всех dataset
datasetList = arcpy.ListDatasets(feature_type='feature')
for dataset in datasetList:
    #для каждого dataset создали папку 
    arcpy.management.CreateFolder(myfolder,dataset)
    #список всех fc
    fcList = arcpy.ListFeatureClasses(feature_dataset=dataset)
    for fc in fcList:             
	#конвертируем каждый fc в shp
        path = os.path.join(myfolder,'my_folder')
        arcpy.conversion.FeatureClassToShapefile(fc,path)
        
