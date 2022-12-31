
def split_data(data,train_ratio,val_ratio):
    l=len(data)
    train_size=int(l*train_ratio)
    val_size=int(l*val_ratio)
    test_size=l-train_size-val_size
    train_data=data[:train_size]
    val_data=data[train_size:-test_size]
    test_data=data[-test_size:]
    return train_data,val_data,test_data