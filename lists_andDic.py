import json
def run ():
    my_list=[1,"Hello",True,4.5]
    my_Dic={"firname":"Roberto", "lastname":"Mendoza"}

    super_list=[
        {"firname":"Jose", "lastname":"Mendoza"},
        {"firname":"Mario", "lastname":"Mendez"},
        {"firname":"Fermin", "lastname":"flores"},
    ]

    super_dic={
        "natural_nums":[1,2,3,4,5],
        "integer_nums":[-2,-1,0,1,2],
        "floating_nums":[2.0,3.3,4.3,5.9]
    }

    for key,value in super_dic.items():
        print(key," - ", value)

    for value in super_list:
        print(json.dumps(value, sort_keys=False, indent=1))

if __name__=="__main__":
    run()