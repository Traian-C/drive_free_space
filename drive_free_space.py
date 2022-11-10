'''Get the free space (GB) of a logical drive'''
import subprocess #nosec(B404)

def get_drive_free_space(drive_letter):
    str_return = ''
    str_drive_path = 'dir ' + drive_letter + ':\\'
    fs_stdout, fs_stderr = subprocess.Popen(str(str_drive_path),
                                                text=True,
                                                stdout=subprocess.PIPE,
                                                stderr=subprocess.PIPE,
                                                shell=True).communicate() #nosec(B602)    
    if fs_stderr:
        str_return = 'Error!   ' + str(fs_stderr)
    else:
        str_free_space = fs_stdout[fs_stdout.find('Dir(s)')+len('Dir(s)'):].strip()
        str_free_space = str_free_space.removesuffix('bytes free')
        int_free_space = int(str_free_space.replace('.', ''))
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
