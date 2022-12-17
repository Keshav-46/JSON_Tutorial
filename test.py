import json
text = """
{
    "name": "Techview",
    "yearofstart": 2017,
    "verified" : true,
    "bestvideo" : ["abc","vfv"],
    "camerainfo": {
        "type":"DSLR",
        "resolution":"12mp",
        "lens": "50mm"
    }
}
"""

obj=json.loads(text)
# print(obj["name"])
# print(obj["yearofstart"])
print(obj["bestvideo"][0])


# YOU can try on inception

"""
text = `{
    "name": "Techview",
    "yearofstart": 2017,
    "verified" : true,
    "bestvideo" : ["abc","vfv"],
    "camerainfo": {
        "type":"DSLR",
        "resolution":"12mp",
        "lens": "50mm"
    }
}`"""

# and try this code
# obj= JSON.parse(text)
# obj.name
# obj.camerainfo['1'] // yasle vitrako value lai pani dinx
