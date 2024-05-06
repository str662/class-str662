class str662:

    def dictt(list1,list2):
        dic = {}
        for i in range(len(list1)):
            dic.update({list1[i]:list2[i]})
        return dic
    