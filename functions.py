from pathlib import Path
import os
import shutil
import time


mods_file_extension = ('.jar', '.esp', '.test')


def get_name(dir_: Path):
    """ Obtener el nombre del archivo 'pack.sav' en el directorio"""
    files = os.listdir(dir_)
    for file_ in files:
        if file_ == 'pack.sav':
            with open(dir_ / file_, 'r') as file_name:
                return file_name.read()
    return 'none'


def get_status(dir_: Path):
    """ Se comprueba si el directorio tiene el archivo 'pack.sav' y/o mods """
    files = os.listdir(dir_)
    has_sav = any(file_.endswith('.sav') for file_ in files)
    has_jar = any(file_.endswith(mods_file_extension) for file_ in files)
    if not has_sav and not has_jar:
        return 'N'
    return ('S' if has_sav else '') + ('J' if has_jar else '')


def get_mods(dir_: Path):
    """ Se obtiene una lista con los mods en el directorio """
    mods = []
    for file_ in os.listdir(dir_):
        if file_.split('.')[-1] != 'sav':
            mods.append(file_)
    return mods


def move_files(from_dir: Path, to_dir: Path):
    """ Se mueven los archivos de un directorio a otro """
    for file_ in os.listdir(from_dir):
        if to_dir.exists():
            shutil.move(from_dir / file_, to_dir)
        else:
            to_dir.mkdir()
            shutil.move(from_dir / file_, to_dir)


def rename_pack(new_name, pack: dict, other_packs):
    """ Se renombra el pack seleccionado """
    old_name = pack['name']
    old_other_dir = Path(other_packs / old_name)
    if old_other_dir.exists():
        old_other_dir.rename(other_packs / new_name)
    pack['name'] = new_name
    with open(pack['dir'] / 'pack.sav', 'w') as save:
        save.write(new_name)


def create_pack(dir_: Path):
    """ Crea un diccionario representando un pack con su nombre, estado, mods y directorio """
    return {
        'name': get_name(dir_),
        'status': get_status(dir_),
        'mods': get_mods(dir_),
        'dir': dir_
    }


def get_other_packs(dir_: Path, active_pack):
    """ Se obtiene la lista de los packs que no sean el activo """
    packs = []
    for pack in os.listdir(dir_):
        if pack != active_pack['name']:
            packs.append(create_pack(dir_ / pack))
    return packs


def print_menu():
    print('Tus opciones son:')
    print('1: Guardar Mods')
    print('2: Poner Mods')
    print('3: Intercambiar Mods (si hay uno activo)')
    print('4: Cambiar nombre pack activo')
    print('5: Mostrar todos los packs')
    print('0: Salir')


def wait():
    """ Una espera de pocos segundos con un indicador visual """
    for i in range(3):
        print('.', end='', flush=True)
        time.sleep(1.2)
    clear_console()


def clear_console():
    """ Limpia la consola dependiendo del sistema operativo """
    os.system('clear' if os.name == 'posix' else 'cls')


def print_packs(active_pack, other_packs, packs: int = 2):
    """ Se imprime el pack actual y los otros packs"""
    if packs == 0 or packs == 2:
        print(f'Tu pack actual:\n{active_pack['name']}\n')
    if packs == 1 or packs == 2:
        print('Tus otros packs:')
        for pack in other_packs:
            print(f'{other_packs.index(pack)}: {pack['name']}')
        print('')


def select_option(max_):
    """ Un input al usuario en un rango de enteros """
    while True:
        try:
            option = int(input('Ingresa una opción: '))
            if 0 <= option <= max_:
                return option
            else:
                print('Opción no valida, ingrese un numero dentro de las opciones.')
        except ValueError:
            print('Entrada no valida')
