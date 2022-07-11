
import numpy as np
import pandas as pd

def rewrite_css(filepath: str, viewportpx: tuple, vw, output_filepath: str):

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

    print (values)


    newvalues = []  

    if vw == 'vw': 
        for value in values:
            if value.endswith(vw):
                partstring = value.partition(vw)
                newvwvalue = str(round((float(partstring[0])/viewportpx)*100, 3))
                newvalues.append(str(newvwvalue + 'vw'))
            else:
                newvalues.append(value)
            
    
    
    elif vw == 'vh':
        for value in values:
            if value.endswith(vw):
                partstring = value.partition(vw)
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

def get_numbers(x: str):
    
    y = ''
    for i in list(x):
        if i.isdecimal() or i.isnumeric() or i == ".":
            y += i
        
    return y


    

def replace_css(filepath: str, viewportpx: tuple, target_unit: str, output_filepath: str):

    with open(filepath) as f:
        lines = f.read()
        lines = lines.split(" ")
    
    print (lines)
    if target_unit == 'vh':
        opp_lines = []
        for i in lines:
            if 'vw' in i:
                x = i.split('vw')[0]
                opp_lines.append(get_numbers(x))
            else:
                opp_lines.append('')

    if target_unit == 'vw':
        opp_lines = []
        for i in lines:
            if 'vh' in i:
                x = i.split('vh')[0]
                opp_lines.append(get_numbers(x))
            else:
                opp_lines.append('')
    
    num_lines = []

    if target_unit == 'vh':
        for i in opp_lines:
            try:
                num_lines.append((((float(i)/100)*viewportpx[0])/viewportpx[1])*100)
            except:
                num_lines.append('')

    if target_unit == 'vw':
        for i in opp_lines:
            try:
                num_lines.append((((float(i)/100)*viewportpx[1])/viewportpx[0])*100)
            except:
                num_lines.append('')
    
    final_lines = []

    for i in num_lines:
        try:
            final_lines.append(str(round(float(i), 2)))  
        except:
            final_lines.append('')
            
    print (final_lines)
    


    
    # with open(output_filepath, "w") as f:
    #     f.write(output_string)


replace_css(r"C:\", (414,896),'vh', r"C:\")