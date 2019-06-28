def packer(**kwargs):
    print(kwargs)

#def packer(name=None, **kwargs):
#    print(kwargs)

def unpacker(first_name= None, last_name= None):
    if first_name and last_name:
        print("hi {} {}".format(first_name, last_name))
    else:
        print("hi no name")

packer(name= 'rik', num=21, indian_inquisition= None)
unpacker(**{'last_name': 'mukherjee', 'first_name': 'rik'})
