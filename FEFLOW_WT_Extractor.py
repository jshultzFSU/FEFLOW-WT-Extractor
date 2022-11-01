#create elevation of water table
import math
# Here we creating the new User Data for Free Surface Node Distribution
doc.createNodalRefDistr("Free Surface")
idND = doc.getNodalRefDistrIdByName("Free Surface")
NSlices = doc.getNumberOfSlices()# getting number of slices for model
Nodes = doc.getNumberOfNodesPerSlice()# getting number of nodes per slice

#find each layers nodes
layer1 = doc.findSelection(ifm.Enum.SEL_NODES, "S1")
layer2 = doc.findSelection(ifm.Enum.SEL_NODES, "S2")
layer3 = doc.findSelection(ifm.Enum.SEL_NODES, "S3")
layer4 = doc.findSelection(ifm.Enum.SEL_NODES, "S4")
layer5 = doc.findSelection(ifm.Enum.SEL_NODES, "S5")
layer6 = doc.findSelection(ifm.Enum.SEL_NODES, "S6")
layer7 = doc.findSelection(ifm.Enum.SEL_NODES, "S7")
#get nodes
Nl1=doc.getSelectionItems(ifm.Enum.SEL_NODES, layer1)
Nl2=doc.getSelectionItems(ifm.Enum.SEL_NODES, layer2)
Nl3=doc.getSelectionItems(ifm.Enum.SEL_NODES, layer3)
Nl4=doc.getSelectionItems(ifm.Enum.SEL_NODES, layer4)
Nl5=doc.getSelectionItems(ifm.Enum.SEL_NODES, layer5)
Nl6=doc.getSelectionItems(ifm.Enum.SEL_NODES, layer6)
Nl7=doc.getSelectionItems(ifm.Enum.SEL_NODES, layer7)
nodelist=[Nl1,Nl2,Nl3,Nl4,Nl5,Nl6,Nl7]#all nodes

#first layer
for i in range(0,doc.getNumberOfNodesPerSlice()):
    node = Nl1[i]
    p = doc.getResultsFlowPressureValue(node)
    if  (p>=0):
        doc.setNodalRefDistrValue(idND,i, doc.getResultsFlowHeadValue(node))

#loop each slice
for sl in range(1,NSlices):
    print('processing current slice:'+str(sl))
    #current node
    node=nodelist[sl]
    print('previous slice:'+str(sl-1))
    #previous node
    node_prev=nodelist[sl-1]
    #loop through each node
    for ND in range(0,len(nodelist[sl])):
        p = doc.getResultsFlowPressureValue(node[ND])  # current slice node pressure
        #print('node'+str(node[ND])+'pressure:'+str(p))
        p_prev = doc.getResultsFlowPressureValue(node_prev[ND])  # previous slice node pressure
        #if previous slice pressure < 0 and current slice pressure > 0 then we get the water table in current node
        if (p_prev < 0 and p >= 0):
            if (not math.isnan(doc.getResultsFlowHeadValue(node[ND]))):#is layer is active check?
                doc.setNodalRefDistrValue(idND,ND, doc.getResultsFlowHeadValue(node[ND]))