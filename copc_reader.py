import json
import pdal
import numpy as np

# copc url 
url = "https://storage.sbg.cloud.ovh.net/v1/AUTH_63234f509d6048bca3c9fd7928720ca1/ppk-lidar/LS/LHD_FXX_0714_6149_PTS_C_LAMB93_IGN69.copc.laz"

# pdal pipeline, filter based on aread and classification building
pipeline_json = {
    "pipeline": [
        url,
        {
            "type": "filters.range",
            "limits": "Classification[6:6],X[714066.1682:714247.1574],Y[6148282.8360:6148669.0890]"
        }
    ]
}

pipeline = pdal.Pipeline(json.dumps(pipeline_json))
count = pipeline.execute()

arrays = pipeline.arrays
print(f"Arrays: {len(arrays)}")
points = arrays[0]

# Voorbeeld: toegang tot X, Y, Z
x = points['X']
y = points['Y']
z = points['Z']
c = points['Classification']

print(f"Totaal aantal punten: {count}")
print("Eerste 5 punten:")
for i in range(5):
    print(x[i], y[i], z[i], c[i])