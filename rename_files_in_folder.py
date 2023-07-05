import os

source_folder = r''

for item in os.listdir(source_folder):
    # Check if an item is file or not
    if os.path.isfile(os.path.join(source_folder,item)):
        if item.endswith('.mp4'):
            try:
                # renaming a file
                os.rename(
                    os.path.join(source_folder,item),
                    os.path.join(source_folder, item[:-17]+'-RexPorn-'+item[-8:])
                )
            except PermissionError:
                print('Permission Error')
                continue
            except Exception as e:
                raise Exception(e)
        else: print(f'{item} does not end with .mp4')
    else:
        print(f'item is not a file')
