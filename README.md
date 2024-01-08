GIS Alcohol Mapping Application with Django + Leafltet JS

STEPS GUIDE
-collect gps data(businesses,community amenity) using gps device and additional information from google
-clean and validate gps data into two (businesses, community amenities), store them in csv format. 
-create erd diagrams using mysql workbench.
-forward engineer the erd to produce mysql database tables and file. 
-install django and all its components(using pip).At the settings file set the parameters for installed apps,middleware,database(engine,name,user,password,host,port)
-use inspectdb command to generate the models from the sql file. 
-clean the models and add the geom attribute that will enable store spatial information 
-convert the csv to json in order to load the validated information into the database (businesses,community amenity) using geojson feature.
