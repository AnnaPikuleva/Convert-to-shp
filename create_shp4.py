import arcpy
import os
#выбрать рабочее пространство 
workspace = arcpy.GetParameterAsText(0)
#задаем рабочее пространство 
arcpy.env.workspace = workspace 
#папка для сохранения shp
myfolder=arcpy.GetParameterAsText(1)
#список всех dataset
datasetList = arcpy.ListDatasets(feature_type='feature')
#список всех fc
only_fcList = arcpy.ListFeatureClasses()
#объединим списки 
ListFeatureClasses=datasetList+ only_fcList
for i in ListFeatureClasses:
     if i in datasetList:
         #для каждого dataset создали папку
         arcpy.management.CreateFolder(myfolder,i)
         #список всех fc
         fcList = arcpy.ListFeatureClasses(feature_dataset=i)
         for fc in fcList:             
 	    #конвертируем каждый fc в shp
             path = os.path.join(myfolder,i)
             arcpy.conversion.FeatureClassToShapefile(fc,path)
     elif i in only_fcList:      
         #конвертируем каждый fc в shp
         path = os.path.join(myfolder)
         arcpy.conversion.FeatureClassToShapefile(i,myfolder)
     else:
         break
