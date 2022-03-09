
import numpy as np
import pandas as pd

def rewrite_css(filepath: str, viewportpx: int, vw, output_filepath: str):

    with open(filepath) as f:
        lines = f.read()
        lines = lines.split(";")
    
    itemlist = []
    for item in lines[:-1]:
        split_items = item.split(":")
        prop = split_items[0]
        val = split_items[1]
        itemlist.append((prop, val))
    
    values = []
    for line in itemlist:
        value = line[-1]
        values.append(value)


    newvalues = []   
    for value in values:
        if value.endswith('px'):
            partstring = value.partition("px")
            if vw == True:
                newvwvalue = str(round((float(partstring[0])/viewportpx)*100, 3))
                newvalues.append(str(newvwvalue + 'vw'))
            elif vw == False:
                newvhvalue = str(round((float(partstring[0])/viewportpx)*100, 3))
                newvalues.append(str(newvhvalue + 'vh'))
        else:
            newvalues.append(value)

    df = pd.DataFrame(np.array(itemlist))
    df['newvals'] = newvalues

    output_string = ''

    for i, row in df.iterrows():
        output_string += row[0]
        output_string += ": "
        output_string += row["newvals"]
        output_string += " ;"
    
    with open(output_filepath, "w") as f:
        f.write(output_string)





#     Use the rewrite_css function like so
#     rewrite_css(r"C:\Users\path\to\your\existingcss.css", 1720, True, r"C:\Users\path\to\your\newcss.css")

