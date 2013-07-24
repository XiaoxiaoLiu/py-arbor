#!/usr/bin/python

from  vtk import *

#read in  a tree
treeReader = vtkNewickTreeReader()
treeReader.SetFileName('/home/xiaoxiao/work/data/Arbor/anolis.phy')
treeReader.Update()
tr = treeReader.GetOutput()
print(tr.GetNumberOfVertices())

#read in  a table
tableReader = vtkDelimitedTextReader()
tableReader.SetFileName('/home/xiaoxiao/work/data/Arbor/anolisDataAppended.csv')
tableReader.Update()
table = tableReader.GetOutput()


#play with the heatmap vis
treeHeatmapItem = vtkTreeHeatmapItem()
treeHeatmapItem.SetTree(tr);
treeHeatmapItem.SetTable(table);

# setup the window
view = vtkContextView()
view.GetRenderer().SetBackground(1,1,1)
view.GetRenderWindow().SetSize(800,600)

iren = view.GetInteractor()
iren.SetRenderWindow(view.GetRenderWindow())

transformItem = vtkContextTransform()
transformItem.AddItem(treeHeatmapItem)
transformItem.SetInteractive(1)

view.GetScene().AddItem(transformItem)
view.GetRenderWindow().SetMultiSamples(0)

iren.Initialize()
view.GetRenderWindow().Render()
iren.Start()





