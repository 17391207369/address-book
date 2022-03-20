#电话录
people_list = [] #全局变量 数组

def main():#定义主方法
    while  True:
        menu()
        choice=(input("请选择"))
        if choice in ["0","1","2","3","4","5"]:
            if choice=="0":
                answer=input('你确定退出系统吗y/n')
                if answer=='y' or answer=='Y':
                    print('谢谢你的使用')
                    break
                else:
                    continue
            elif choice=="1":
                insert()
            elif choice=="2":
                search()
            elif choice=="3":
                delect()
            elif choice=="4":
                modify()
            elif choice=="5":
                select()
        else:
            menu()
def menu():#主程序
    print('---------------------------------学生信息管理系统------------------------------------------------')
    print('—————————————————————————————————————功能菜单——————————————————————————————————————————————————')
    print('\t\t\t\t1、录入联系人信息')
    print('\t\t\t\t2、查找联系人信息')
    print('\t\t\t\t3、删除联系人信息')
    print('\t\t\t\t4、修改联系人信息')
    print('\t\t\t\t5、查看通讯录')
    print('\t\t\t\t0、退出')
    print('--------------------------------请选择你要操作的功能---------------------------------------------')
    print('-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-')
def insert():#添加联系人
    while True:
        id = input('请输入ID（如1001）')
        if not id:
            break
        name =input('请输入姓名:')
        if not name:
            break

        try:
            number=int(input('请输入电话号码'))
            email=int(input('请输入邮箱地址'))
            dz=input('请输入地址')
        except:
            print('输入无效，请重新输入')
            continue
        students={'id':id,'name':name,'number':number,'email':email,'dz':dz}
        people_list.append(students)
        answer=input('是否继续添加y/n')
        if answer=='y'or answer=='Y':
            continue
        else:
            print("联系人信息录入完毕")
            break

def search():#查看联系人
    ID=input("请输入查看人的id")
    for a in people_list:
        if a["id"]==ID:
            print("ID：",a["id"])
            print("姓名：",a["name"])
            print("电话：", a["number"])
            print("邮箱：",a["email"])
            print("地址：",a["dz"])
def delect():#删除联系人
    item = []
    ID=(input("请输入要删除联系人id"))
    for a in people_list:
        id=a.get("id")
        name=a.get("name")
        number=a.get("number")
        email=a.get("email")
        dz=a.get("dz")
        if id==ID:
            continue
        sku={
            "id":id,
            "name":name,
            "number":number,
            "email":email,
            "dz":dz
        }
        item.append(sku)
    people_list.clear()
    for a in item:
        id = a.get("id")
        name = a.get("name")
        number = a.get("number")
        email = a.get("email")
        dz = a.get("dz")
        sku = {
            "id": id,
            "name": name,
            "number": number,
            "email": email,
            "dz": dz
        }
        people_list.append(sku)
    print("已删除")
def modify():#修改联系人
    while True:
        ID=input("请输入修改联系人id")
        for a in people_list:
            if a["id"] == ID:
                print("1、",a["id"])
                print("2、",a["name"])
                print("3、",a["number"])
                print("4、",a["email"])
                print("5、",a["dz"])
                im=int(input("请输入修改哪项信息"))
                im1 =(input("请输入修改内容"))
                if im==1:
                    a["id"]=int(im1)
                if im==2:
                    a["name"]=im1
                    print(im1)
                if im==3:
                    a["number"]=int(im1)
                if im==4:
                    a["email"]=im1
                if im==5:
                    a["dz"]=im1
                print("修改成功")
        answer=input('是否继续修改y/n')
        if answer == 'y' or answer == 'Y':
            continue
        else:
            break
def select():#查看所有人
    for a in people_list:
        print("*-*-*-*-*-*-*-*-*-*-*-*")
        print("ID：", a["id"])
        print("姓名：", a["name"])
        print("电话：", a["number"])
        print("邮箱：", a["email"])
        print("地址：", a["dz"])
        print("*-*-*-*-*-*-*-*-*-*-*-*")
if __name__ == '__main__':   #主程序运行
    main()
