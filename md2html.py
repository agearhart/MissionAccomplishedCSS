import markdown
import os, sys


output = """<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <style type="text/css">
"""
script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "Dossier/MissionAccomplished.css"
abs_file_path = os.path.join(script_dir, rel_path)
cssin = open(abs_file_path, "r")
output += cssin.read()

output += """
    </style>
</head>

<body>
"""

rel_path = "Dossier/Dossier.md"
abs_file_path = os.path.join(script_dir, rel_path)
mkin = open(abs_file_path, "r")
output += markdown.markdown(mkin.read())

output += """</body>

</html>
"""

outfile = open("Dossier.html", "w")
outfile.write(output)
outfile.close()