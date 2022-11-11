'''Get the free space (GB) of a logical drive'''
import shutil

def get_drive_free_space(drive_letter):
    int_free_space = int(shutil.disk_usage(f"{drive_letter}:/")[2])
    int_free_space_GB = int_free_space * 9.31e-10
    str_free_space = '{:.2f}'.format(int_free_space_GB)
    str_return = f'Drive {str(drive_letter).upper()} free space: ' + str_free_space + ' GB'
    return str_return


def main():
    '''just for testing'''
    print(get_drive_free_space("c"))
    print(get_drive_free_space("d"))


if __name__ == '__main__':
    main()
