def percent_change(series):
    """
    Compute the fractional change between consecutive values.
    """
    # Write code here
    res=[]
    x=series
    for i in range(1,len(series)):
        if(x[i-1]==0):
            res.append(0.0)
            continue
        res.append((x[i]-x[i-1])/x[i-1])
    return res
