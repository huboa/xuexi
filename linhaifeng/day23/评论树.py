commentList=[
    {"nid":1,"content":"111","pid":None,"childrenList":[]},
    {"nid":2,"content":"222","pid":None,"childrenList":[]},
    {"nid":3,"content":"333","pid":None,"childrenList":[]},
    {"nid":4,"content":"444","pid":1,"childrenList":[]},
    {"nid":5,"content":"555","pid":4,"childrenList":[]},
    {"nid":6,"content":"666","pid":1,"childrenList":[]},
    {"nid":7,"content":"777","pid":2,"childrenList":[]},
]

for comment_dict in commentList:
    comment_dict["childrenList"]=[]

    print(comment_dict["nid"])
    print(comment_dict["pid"])

    if comment_dict["pid"]==None:

        print(comment_dict)
    else:
        comment_dict["childrenList"].appent
#    if comment_dict["pid"] == comment_dict["nid"]:

