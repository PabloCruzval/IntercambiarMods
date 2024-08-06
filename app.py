from functions import *

ACTIVEFOLDER = Path('Test packs/Active Folder')
OTHERFOLDERS = Path('Test packs/Other Folders')

active_pack = create_pack(ACTIVEFOLDER)
other_packs = get_other_packs(OTHERFOLDERS, active_pack)

print_packs(active_pack, other_packs)

while True:
    active_pack = create_pack(ACTIVEFOLDER)
    other_packs = get_other_packs(OTHERFOLDERS, active_pack)
    print_menu()

    option = select_option(5)
    if option == 1:
        if active_pack['name'] != 'none' and active_pack['status'] == 'SJ':
            move_files(ACTIVEFOLDER, OTHERFOLDERS / active_pack['name'])
            print('Mods guardados')
            wait()
        elif active_pack['name'] == 'none' and active_pack['status'] == 'J':
            print('Los mods actuales no tienen nombre.')
            new_name = rename_pack(input('$'), active_pack)

        elif not os.listdir(ACTIVEFOLDER):
            clear_console()
            print('No hay ningún archivo en el directorio activo.')
            wait()

    elif option == 2:
        clear_console()
        if active_pack['name'] != 'none' and active_pack['status'] != 'N':
            print('Hay un pack activo')
            wait()
        else:
            print_packs(active_pack, other_packs, 1)
            option = select_option(len(other_packs) - 1)
            move_files(other_packs[option]['dir'], ACTIVEFOLDER)
            print('Mods puestos')
            wait()

    elif option == 3:
        clear_console()
        if active_pack['name'] == 'none' and active_pack['status'] == 'N':
            print('No hay un pack activo')
            wait()
        else:
            print_packs(active_pack, other_packs, 1)
            option = select_option(len(other_packs) - 1)
            move_files(ACTIVEFOLDER, OTHERFOLDERS / active_pack['name'])
            move_files(other_packs[option]['dir'], ACTIVEFOLDER)
            print('Mods puestos')
            wait()

    elif option == 4:
        clear_console()
        name = input('Ingrese un nuevo nombre:')
        rename_pack(name, active_pack, OTHERFOLDERS)
        print('Se ha cambiado correctamente el nombre')
        wait()

    elif option == 5:
        clear_console()
        print_packs(active_pack, other_packs)

    elif option == 0:
        break
