# NeatSankey

Here is the source code for the NeatSankey

You can find the layout algorithm in two folders, "NeatSankeyNodeOrdering" and "LineBundling"

at the same time, all the example html files can be found in "attachment" folder

and all the dataset used in the CaseStudy can be found in the "dataset" folder

as for the four evaluating methods, they all exist in the folder "evaluating"

## What we have done?

### A brand new layout algorithm

#### input: 
 
A json file like the data in "dataset" folder

#### output:

our layout algorithm will generate an output file with three lists: links, level, result

+ links is a single-dimensional array which contains all the edges info in current chart
+ level is a two-dimensional array which contains the nodes name and size info
+ result is a two-dimensional array which describes the order of nodes in every layer

example:

```js
var links = [{"source": "USA", "target": "gold", "value": "39"}, {"source": "USA", "target": "silver", "value": "41"}, {"source": "USA", "target": "brown", "value": "33"}, {"source": "China", "target": "gold", "value": "38"}, {"source": "China", "target": "silver", "value": "32"}, {"source": "China", "target": "brown", "value": "18"}, {"source": "Japan", "target": "gold", "value": "27"}, {"source": "Japan", "target": "silver", "value": "14"}, {"source": "Japan", "target": "brown", "value": "17"}, {"source": "ROC", "target": "gold", "value": "20"}, {"source": "ROC", "target": "silver", "value": "28"}, {"source": "ROC", "target": "brown", "value": "23"}]

var level = [[{"name": "ROC", "size": 71.0}, {"name": "Japan", "size": 58.0}, {"name": "China", "size": 88.0}, {"name": "USA", "size": 113.0}], [{"name": "brown", "size": 91.0}, {"name": "silver", "size": 115.0}, {"name": "gold", "size": 124.0}]]

let result = [[1, 4, 2, 3], [1, 2, 3]]
```

### An ambiguity-free edge bundling algorithm

this algorithm is so easy to use that what we should do is just import the script file at the end of a file like

```js
<script src="LineBundling/sankeyEdgesBundling.js"></script>
```

you can see more details in the script