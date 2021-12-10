
def main():
    header = ['Username', 'Department', 'Classroom']
    username = list()
    dept = list()
    classroom = list()
    registres = int(input("Quants registres vols afegir? "))

    for i in range(registres):
        username.append(input("Introdueix el nom d'usuari: "))
        dept.append(input("Introdueix el departament: "))
        classroom.append(int(input("Introdueix la classe: ")))

    regs = {
        "username": username,
        "department": dept,
        "classroom": classroom
    }
    for i in header:
        print(i, end ='\t|')
    print()

    for i in range(registres):
        print(regs['username'][i] + '\t\t| '+ regs['department'][i] + '\t\t| ' + str(regs['classroom'][i])+ '\t\t| ')
if __name__ == '__main__':
    main()


