import maya.cmds as cmds
import re

def rename_transforms_from_shapes():
    for shape in cmds.ls(type="mesh"):
        transform = cmds.listRelatives(shape, parent=True, fullPath=True)[0]
        short_transform = transform.split('|')[-1]
        short_shape = shape.split('|')[-1]

        # Try to extract the tile ID from the shape name using regex
        match = re.match(r"Tile_(\d+)_Shape", short_shape)
        if match:
            tile_id = match.group(1)
            new_transform_name = f"Tile_{tile_id}_Render_Geo"

            # Rename transform if it doesn't already match the target
            if short_transform != new_transform_name:
                if not cmds.objExists(new_transform_name):
                    try:
                        cmds.rename(transform, new_transform_name)
                        print(f"Renamed transform: {short_transform} ? {new_transform_name}")
                    except Exception as e:
                        print(f"Failed to rename {short_transform}: {e}")
                else:
                    print(f"Skipped {short_transform}, name {new_transform_name} already exists.")
            else:
                print(f"Transform already named {new_transform_name}, skipping.")
        else:
            print(f"Skipped shape {short_shape}: does not match pattern 'Tile_XXXX_Shape'.")

rename_transforms_from_shapes()
