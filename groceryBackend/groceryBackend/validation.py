def validate(data,mandatory):
    not_present = []
    for X in mandatory:
        if X not in data:
            not_present.append(X)
            return (f"{X} Is Not Present")
        else :
            if data[X]=="":
                not_present.append(X)
                return (f"{X} Cannot use as Null")
            else:pass
        if len(not_present)==0:
            return True
        else:
            pass
        
        