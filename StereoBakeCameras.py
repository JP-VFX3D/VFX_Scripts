import hou

# Select the stereo camera HDA
stereoRig = hou.selectedNodes()[0]

# Define internal camera names
leftCam = stereoRig.node('left_camera')
rightCam = stereoRig.node('right_camera')

if not leftCam or not rightCam:
    raise Exception("Could not find 'left_camera' and 'right_camera' inside the stereo rig HDA.")

# Create baked camera nodes in /obj
leftBake = hou.node('/obj').createNode('cam', stereoRig.name() + '_left_bake')
rightBake = hou.node('/obj').createNode('cam', stereoRig.name() + '_right_bake')

# Get frame range
startFrame, endFrame = map(int, hou.playbar.playbackRange())

# Bake helper
def bake_camera(source_cam, target_cam):
    for f in range(startFrame, endFrame + 1):
        hou.setFrame(f)

        # Copy transform
        target_cam.setWorldTransform(source_cam.worldTransform())
        for parm in ['tx', 'ty', 'tz', 'rx', 'ry', 'rz']:
            val = target_cam.parm(parm).eval()
            target_cam.parm(parm).setKeyframe(hou.Keyframe(val))

        # Copy common camera settings
        for parm_name in [
            'focal', 'aperture', 'near', 'far',
            'resx', 'resy', 'winsizex', 'winsizey',
            'shutter', 'aspect', 'winx', 'winy'
        ]:
            if source_cam.parm(parm_name) and target_cam.parm(parm_name):
                val = source_cam.parm(parm_name).eval()
                target_cam.parm(parm_name).setKeyframe(hou.Keyframe(val))

# Bake both cameras
bake_camera(leftCam, leftBake)
bake_camera(rightCam, rightBake)