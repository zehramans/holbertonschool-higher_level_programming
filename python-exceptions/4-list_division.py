#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    final_list = []
    for i in range(list_length):
        try:
            final_list.append(my_list_1[i]/my_list_2[i])
        except ZeroDivisionError:
            print("division by 0")
            final_list.append(0)
        except TypeError:
            print("wrong type")
            final_list.append(0)
        except IndexError:
            print("out of range")
            final_list.append(0)
        finally:
            pass
    return final_list
