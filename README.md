# FEFLOW-WT-Extractor
Extract water tabel surface from FEFLOW model (Richards equation)

This code was modified from Ivan Rastorguev
https://www.researchgate.net/publication/334167217_Python_script_for_Feflow_71_to_view_water_table_elevation_the_same_option_like_in_Visual_Modflow

**This code was ran inside FEFLOWs scripting tool**

To use code (1) create selections in your FEFLOW model (2) modify selection section of code

When you want to calculate free surface run the script this will cycle through each layer and if pressure is > 0 in the current layer and p<0 in the layer above the current layer water table will be assigned to curent layer. With the exception of layer 1 which is checked for instances where pressure exceeds 0

**This is a rudimentary attempt to extract the water table elevation any comments or suggestions are welcome**
