class str662:


    def dictt(list1,list2):
        # Это функция поможет создать словарь из двух литов
        # This function will help create a dictionary from two litas
        dic = {}
        for i in range(len(list1)):
            dic.update({list1[i]:list2[i]})
        return dic
    