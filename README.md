# pxtovw
Turn CSS pixel units (px) to viewport width and viewport height (vw or vh) using a simple python function

To update your CSS px values to vw values (viewport width units)  and save to a new file specify the viewport width (for example 1720) and use True in the 3rd argument like this:

  rewrite_css(r"C:\Users\path\to\your\existingcss.css", 1720, True, r"C:\Users\path\to\your\newcss.css")
  
To update your CSS px values to vw values (viewport width units)  and save to a new file specify the viewport height (for example 1110) and use True in the 3rd argument like this:

  rewrite_css(r"C:\Users\path\to\your\existingcss.css", 1720, False, r"C:\Users\path\to\your\newcss.css")
