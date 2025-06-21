# VFX_Scripts
Niche scripts for use in Maya and Houdini (python and mel).



Maya (Mel)

ABC_Cleanup
- Cleans up alembic cache meshes by deleting specific Input attributes; time1 and AlembicNode.

MeshOutlinerSelect
- Selects all meshes within the Outliner, no matter if inside a group or other hierarchy setup.

StaticMeshBakeLocator
- After using MeshOutlinerSelect, use this script to create a locator for each selected static mesh and bakes their transform, rotation and scale values.


Maya (Python)

meshDisplayAttributeCreate_MetaHumanAdvancedSkeletonRig
- Creates the meshDisplay attribute with enums; Ultra, High, Medium and Low. Ideal use is for the selected Advanced Skeleton rig Main controller to switch between lod mesh groups when using MetaHuman NameMatcher template.

meshDisplaySwitch_MetaHumanAdvancedSkeletonRig
- Assigns the default MetaHuman lod mesh groups (lod0-lod3) with the meshDisplay attribute and a different enum (Ultra, High, Medium and Low) for the Advanced Skeleton rig Main controller. Use after running the meshDisplayAttributeCreate script with the Main controller selected. Then go to the Channel Box and use the MeshDisplay switch.



Houdini (Python)

BakeParentedCamera
- Bake parented camera animation, whether it's constrained with null locators or other methods.

StereoBakeCameras
- Bake left and right stereo camera channels from the selected Stereo Camera node.
