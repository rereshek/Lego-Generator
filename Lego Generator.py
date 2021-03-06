import maya.cmds as cmds
import random as rnd

if 'myWin' in globals():
    if cmds.window(myWin, exists=True):
        cmds.deleteUI(myWin, window=True)

# Window Title       
myWin = cmds.window(title="Lego Blocks", menuBar=True)

# Collapsible Menu with options to create New Scene and Delete Selected
cmds.menu(label="Basic Options")
cmds.menuItem(label="New Scene", command=('cmds.file(new=True, force=True)'))
cmds.menuItem(label="Delete Selected", command=('cmds.delete()'))

#          UI: adjust and create a Standard Block               #
#################################################################
cmds.frameLayout(collapsable=True, label="Standard Block", width=475, height=140)

cmds.columnLayout()

cmds.intSliderGrp('height',l="Height", f=True, min=1, max=20, value=3)
cmds.intSliderGrp('blockWidth', l="Width", f=True, min=1, max=20, value=2)
cmds.intSliderGrp('blockLength', l="Length", f=True, min=1, max=20, value=8)
cmds.colorSliderGrp('blockColour', label="Colour", hsv=(120, 1, 1))

cmds.columnLayout()
cmds.button(label="Create Basic Block", command=('basicBlock()'))

# Level Up in Hierarchy
cmds.setParent( '..' )
cmds.setParent( '..' )
cmds.setParent( '..' )

#      UI: adjust and create a Standard Block With Holes        #
#################################################################
cmds.frameLayout(collapsable=True, label="Standard Block with Holes", width=475, height=90)

cmds.columnLayout()

cmds.intSliderGrp('blockWithHolesLength', l="Length", f=True, min=1, max=20, value=8)
cmds.colorSliderGrp('blockWithHolesColour', label="Colour", hsv=(120, 1, 1))

cmds.columnLayout()
cmds.button(label="Create Basic Block With Holes", command=('basicBlockWithHoles()'))

# Level Up in Hierarchy
cmds.setParent( '..' )
cmds.setParent( '..' )
cmds.setParent( '..' )

#       UI: adjust and create a Rounded Block With Holes        #
#################################################################
cmds.frameLayout(collapsable=True, label="Rounded Block with Holes")

cmds.columnLayout()

cmds.intSliderGrp('roundedBlockWithHolesLength', l="Length", f=True, min=1, max=20, value=8)
cmds.colorSliderGrp('roundedBlockWithHolesColour', label="Colour", hsv=(11.5, 1, 1))

cmds.columnLayout()
cmds.button(label="Create Rounded Block With Holes", command=('roundedBlockWithHoles()'))

# Level Up in Hierarchy
cmds.setParent( '..' )
cmds.setParent( '..' )
cmds.setParent( '..' )

#   UI: adjust and create a Rounded Block With Holes and Angle  #
#################################################################
#function for synching UI 
def checkBend60deg(isOn):
    if(isOn):
      # disable adjusting length feauture for bend at 60 deg (had little time left)
      bendLength = cmds.intSliderGrp('roundedBlockWithHolesAngleBendLength', edit=True, en=False)
      length = cmds.intSliderGrp('roundedBlockWithHolesAngleLength', edit=True, en=False)
    else:
        bendLength = cmds.intSliderGrp('roundedBlockWithHolesAngleBendLength', edit=True, en=True)
        length = cmds.intSliderGrp('roundedBlockWithHolesAngleLength', edit=True, en=True)

cmds.frameLayout(collapsable=True, label="Rounded Block with Holes and Angle")

cmds.columnLayout()

cmds.intSliderGrp('roundedBlockWithHolesAngleLength', l="Base Part Length", f=True, min=1, max=20, value=4)
cmds.intSliderGrp('roundedBlockWithHolesAngleBendLength', l="Bended Part Length", f=True, min=2, max=20, value=3)
cmds.radioButtonGrp('roundedBlockWithHolesBendAngle', label="Bend Angle", labelArray2=["90 deg", "60 deg"], numberOfRadioButtons=2, sl=1,cc2=checkBend60deg)
#cmds.radioButton( label='roundedBlockWithHolesBendAngle90', label="Bend at 90 degrees")
#cmds.radioButton( label='roundedBlockWithHolesBendAngle60', label="Bend at 60 degrees")
cmds.colorSliderGrp('roundedBlockWithHolesAngleColour', label="Colour", hsv=(120, 0, 0.4))

cmds.columnLayout()
cmds.button(label="Create Rounded Block With Holes and Angle", command=('roundedBlockWithHolesAngle()'))

# Level Up in Hierarchy
cmds.setParent( '..' )
cmds.setParent( '..' )
cmds.setParent( '..' )

#              UI:  create a Wheels and Hubs                    #
#################################################################
cmds.frameLayout(collapsable=True, label="Wheels and Hubs")

cmds.columnLayout()

cmds.radioButtonGrp('wheelTire', label="Tire", labelArray2=["yes", "no"], numberOfRadioButtons=2, sl=1)
cmds.colorSliderGrp('tireColour', label="Tire's colour", hsv=(217, 0, 0.007))
cmds.radioButtonGrp('wheelHub', label="Hub", labelArray2=["yes", "no"], numberOfRadioButtons=2, sl=1)
cmds.colorSliderGrp('hubColour', label="Hub's colour", hsv=(360, 0, 0.852))

cmds.columnLayout()
cmds.button(label="Create a Wheel", command=('createWheel()'))

# Level Up in Hierarchy
cmds.setParent( '..' )
cmds.setParent( '..' )
cmds.setParent( '..' )

#                 UI:  create Gears and Racks                   #
#################################################################
cmds.frameLayout(collapsable=True, label="Gears and Racks")

cmds.columnLayout()

cmds.colorSliderGrp('gearColour', label="Gear's colour", hsv=(240, 0.8, 0.852))
cmds.button(label="Create a Gear", command=('createGear()'))

cmds.colorSliderGrp('rackColour', label="Rack's colour", hsv=(360, 0.99, 0.99))
cmds.button(label="Create a Rack", command=('createRack()'))

# show UI window
cmds.showWindow( myWin )

#################################################################
#               Basic Block Without Holes                       #
#################################################################
def basicBlock():
    # query values from UI sliders
    height = cmds.intSliderGrp('height', q=True, v=True)
    width = cmds.intSliderGrp('blockWidth', q=True, v=True)
    length = cmds.intSliderGrp('blockLength', q=True, v=True)   
    rgb = cmds.colorSliderGrp('blockColour', q=True, rgbValue=True)
    
    # name
    nsTmp = "Block" + str(rnd.randint(1000,9999))
    
    cmds.select(clear=True)
    cmds.namespace(add=nsTmp)
    cmds.namespace(set=nsTmp)
    
    # define a cube's size
    cubeSizeX = width * 0.8
    cubeSizeZ = length * 0.8
    cubeSizeY = height * 0.32
    
    # create a cube
    cmds.polyCube(h=cubeSizeY, w=cubeSizeX, d=cubeSizeZ)
    
    # move block half size up on Y axis
    cmds.move((cubeSizeY/2.0), moveY=True)
    
    # loop through width and length (in bumps)
    for i in range(width):
        for j in range(length):
            # create cylinder
            cmds.polyCylinder(r=0.25, h=0.20)
            # move it on Y axis
            cmds.move((cubeSizeY + 0.10), moveY=True, a=True)
            # move it on X axis
            cmds.move(((i * 0.8) - (cubeSizeX/2.0) + 0.4), moveX=True, a=True)
            # move it on Z axis
            cmds.move(((j * 0.8) - (cubeSizeZ/2.0) + 0.4), moveZ=True, a=True)
    
    # add material        
    myShader = cmds.shadingNode('lambert', asShader=True, name="blckMat")
    cmds.setAttr(nsTmp+":blckMat.color",rgb[0],rgb[1],rgb[2], type='double3')
    
    cmds.polyUnite((nsTmp+":*"), n=nsTmp, ch=False)
    cmds.delete(ch=True)
    
    cmds.hyperShade(assign=(nsTmp+":blckMat"))
    cmds.namespace(removeNamespace=":"+nsTmp,mergeNamespaceWithParent=True)
    
#################################################################
#                    Basic Block With Holes                     #
#################################################################
def basicBlockWithHoles():
    # set up block dimensions
    height = 3
    width = 1 #bump
    length = cmds.intSliderGrp('blockWithHolesLength', q=True, v=True)
    rgb = cmds.colorSliderGrp('blockWithHolesColour', q=True, rgbValue=True)
    
    # name
    nsTmp = "BlockWithHoles" + str(rnd.randint(1000,9999))
    
    cmds.select(clear=True)
    cmds.namespace(add=nsTmp)
    cmds.namespace(set=nsTmp)
    
    # define cube's size 
    cubeSizeX = width * 0.8
    cubeSizeZ = length * 0.8
    cubeSizeY = height * 0.32
    
    # create a cube
    cube = cmds.polyCube(h=cubeSizeY, w=cubeSizeX, d=cubeSizeZ)
    
    # move it up
    cmds.move((cubeSizeY/2.0), moveY=True)
    
    # create bumps
    for i in range(width):
        for j in range(length):
            # create cylinder
            cmds.polyCylinder(r=0.25, h=0.20)
            # move it
            cmds.move((cubeSizeY + 0.10), moveY=True, a=True)
            cmds.move(((i * 0.8) - (cubeSizeX/2.0) + 0.4), moveX=True, a=True)
            cmds.move(((j * 0.8) - (cubeSizeZ/2.0) + 0.4), moveZ=True, a=True)
            
    # create holes
    for i in range(width):
        for j in range(length):
            # create cylinder in the place of a hole
            hole = cmds.polyCylinder(r=0.25, h=height/2.0)
            
            # rotate and position it
            cmds.rotate(90, rotateX=True, a=True)
            cmds.rotate(90, rotateY=True, a=True)
            
            cmds.move((cubeSizeY/2.0), moveY=True, a=True)
            cmds.move(((i * 0.8) - (cubeSizeX/2.0) + 0.4), moveX=True, a=True)
            cmds.move(((j * 0.8) - (cubeSizeZ/2.0) + 0.4), moveZ=True, a=True)
            
            # remove it from the base block
            cube = cmds.polyCBoolOp(cube, hole, op=2, caching=False, ch=False)
    
    # add material        
    myShader = cmds.shadingNode('lambert', asShader=True, name="blckMat")
    cmds.setAttr(nsTmp+":blckMat.color",rgb[0],rgb[1],rgb[2], type='double3')
    
    cmds.polyUnite((nsTmp+":*"), n=nsTmp, ch=False)
    cmds.delete(ch=True)
    
    cmds.hyperShade(assign=(nsTmp+":blckMat"))  
    cmds.namespace(removeNamespace=":"+nsTmp,mergeNamespaceWithParent=True)
    
#################################################################
#                Rounded Block  With Holes                      #
#################################################################
def roundedBlockWithHoles():
    # set up block dimensions
    height = 3
    width = 1 #bump
    length = cmds.intSliderGrp('roundedBlockWithHolesLength', q=True, v=True)
    rgb = cmds.colorSliderGrp('roundedBlockWithHolesColour', q=True, rgbValue=True)
    
    # name
    nsTmp = "RoundedBlockWithHoles" + str(rnd.randint(1000,9999))
    
    cmds.select(clear=True)
    cmds.namespace(add=nsTmp)
    cmds.namespace(set=nsTmp)
    
    # define cube's size 
    cubeSizeX = width * 0.8
    cubeSizeZ = length * 0.8
    cubeSizeY = height * 0.32
    
    # create a cube
    cube = cmds.polyCube(h=cubeSizeY, w=cubeSizeX, d=cubeSizeZ)
    
    # move it up 
    cmds.move((cubeSizeY/2.0), moveY=True)
    
    # create holes
    for i in range(width):
        for j in range(length):
            # create cylinder in the place of a hole
            hole = cmds.polyCylinder(r=0.25, h=height/2.0)
            
            # rotate and position it
            cmds.rotate(90, rotateX=True, a=True)
            cmds.rotate(90, rotateY=True, a=True)
            
            cmds.move((cubeSizeY/2.0), moveY=True, a=True)
            cmds.move(((i * 0.8) - (cubeSizeX/2.0) + 0.4), moveX=True, a=True) 
            cmds.move(((j * 0.8) - (cubeSizeZ/2.0)), moveZ=True, a=True)
            
            # remove it from the base block
            cube = cmds.polyCBoolOp(cube, hole, op=2, caching=False, ch=False)    
    
    # add cylinders to round corners
    # right side 
    rCylind = cmds.polyCylinder(r=cubeSizeY*0.5, h=cubeSizeX)
    cmds.rotate(90, rotateX=True, a=True)
    cmds.rotate(90, rotateY=True, a=True)
    cmds.move((cubeSizeX/2.0 + 0.079), moveY=True, a=True)
    cmds.move((-cubeSizeZ * 0.5), moveZ=True, a=True) 
    # create a hole in it 
    rHole = cmds.polyCylinder(r=0.25, h=height/2.0)
    cmds.rotate(90, rotateX=True, a=True)
    cmds.rotate(90, rotateY=True, a=True)       
    cmds.move((cubeSizeY/2.0), moveY=True, a=True)
    cmds.move(((0 * 0.8) - (cubeSizeX/2.0) + 0.4), moveX=True, a=True) 
    cmds.move(((0 * 0.8) - (cubeSizeZ/2.0)), moveZ=True, a=True)
    rCylind = cmds.polyCBoolOp(rCylind, rHole, op=2, caching=False, ch=False)
    
    # left side 
    lCylind = cmds.polyCylinder(r=cubeSizeY*0.5, h=cubeSizeX)
    cmds.rotate(90, rotateX=True, a=True)
    cmds.rotate(90, rotateY=True, a=True)
    cmds.move((cubeSizeX/2.0 + 0.079), moveY=True, a=True)
    cmds.move((cubeSizeZ * 0.5), moveZ=True, a=True)
    # create a hole in it 
    lHole = cmds.polyCylinder(r=0.25, h=height/2.0)
    cmds.rotate(90, rotateX=True, a=True)
    cmds.rotate(90, rotateY=True, a=True)       
    cmds.move((cubeSizeY/2.0), moveY=True, a=True)
    cmds.move(((width * 0.8) - cubeSizeX), moveX=True, a=True) 
    cmds.move(((length * 0.8) - (cubeSizeZ/2.0)), moveZ=True, a=True)
    lCylind = cmds.polyCBoolOp(lCylind, lHole, op=2, caching=False, ch=False)
    
    # subtract a cylinder from left side of the cube
    lCubeHole = cmds.polyCylinder(r=0.25, h=height/2.0)
    cmds.rotate(90, rotateX=True, a=True)
    cmds.rotate(90, rotateY=True, a=True)       
    cmds.move((cubeSizeY/2.0), moveY=True, a=True)
    cmds.move(((width * 0.8) - cubeSizeX), moveX=True, a=True) 
    cmds.move(((length * 0.8) - (cubeSizeZ/2.0)), moveZ=True, a=True)
    cube = cmds.polyCBoolOp(cube, lCubeHole, op=2, caching=False, ch=False)
    
    # add material        
    myShader = cmds.shadingNode('lambert', asShader=True, name="blckMat")
    cmds.setAttr(nsTmp+":blckMat.color",rgb[0],rgb[1],rgb[2], type='double3')
    
    cmds.polyUnite((nsTmp+":*"), n=nsTmp, ch=False)
    cmds.delete(ch=True)
    
    cmds.hyperShade(assign=(nsTmp+":blckMat"))  
    cmds.namespace(removeNamespace=":"+nsTmp,mergeNamespaceWithParent=True)
    
#################################################################
#             Rounded Block With Holes and Angle                #
#################################################################
def roundedBlockWithHolesAngle():
    # set up block dimensions
    height = 3
    width = 1 #bump
    bendAngle = cmds.radioButtonGrp('roundedBlockWithHolesBendAngle', q=True, sl=True)
    if(bendAngle == 1):
        length = cmds.intSliderGrp('roundedBlockWithHolesAngleLength', q=True, v=True)
        bendLength = cmds.intSliderGrp('roundedBlockWithHolesAngleBendLength', q=True, v=True)
    if(bendAngle == 2):
        length = 4
        bendLength = 3
    rgb = cmds.colorSliderGrp('roundedBlockWithHolesAngleColour', q=True, rgbValue=True)
    
    # name
    nsTmp = "RoundedBlockWithHolesAngle" + str(rnd.randint(1000,9999))
    
    cmds.select(clear=True)
    cmds.namespace(add=nsTmp)
    cmds.namespace(set=nsTmp)
    
    # define cubes size 
    cubeSizeX = width * 0.8
    cubeSizeZ = length * 0.8
    cubeSizeY = height * 0.32
    bendSizeZ = bendLength * 0.8
    
    # create a cube
    cube = cmds.polyCube(h=cubeSizeY, w=cubeSizeX, d=cubeSizeZ)
    
    # move it up 
    cmds.move((cubeSizeY/2.0), moveY=True) 
    
    # create holes
    for i in range(width):
        for j in range(length):
            # create cylinder in the place of a hole
            hole = cmds.polyCylinder(r=0.25, h=height/2.0)
    
            # rotate and position it
            cmds.rotate(90, rotateX=True, a=True)
            cmds.rotate(90, rotateY=True, a=True)
            
            cmds.move((cubeSizeY/2.0), moveY=True, a=True)
            cmds.move(((i * 0.8) - (cubeSizeX/2.0) + 0.4), moveX=True, a=True) 
            cmds.move(((j * 0.8) - (cubeSizeZ/2.0)), moveZ=True, a=True)
            
            # remove it from the base block
            cube = cmds.polyCBoolOp(cube, hole, op=2, caching=False, ch=False)     
    
    # add cylinders to round corners
    # right side 
    rCylind = cmds.polyCylinder(r=cubeSizeY*0.5, h=cubeSizeX)
    cmds.rotate(90, rotateX=True, a=True)
    cmds.rotate(90, rotateY=True, a=True)
    cmds.move((cubeSizeX/2.0 + 0.079), moveY=True, a=True)
    cmds.move((-cubeSizeZ * 0.5), moveZ=True, a=True)
    # merge right cylinder with cube
    cube = cmds.polyCBoolOp(cube, rCylind, op=1, caching=False, ch=False)
    # add a hole
    rHole = cmds.polyCylinder(r=0.25, h=height/2.0)
    cmds.rotate(90, rotateX=True, a=True)
    cmds.rotate(90, rotateY=True, a=True)       
    cmds.move((cubeSizeY/2.0), moveY=True, a=True)
    cmds.move(((0 * 0.8) - (cubeSizeX/2.0) + 0.4), moveX=True, a=True) 
    cmds.move(((0 * 0.8) - (cubeSizeZ/2.0)), moveZ=True, a=True)
    cube = cmds.polyCBoolOp(cube, rHole, op=2, caching=False, ch=False)
    
    # left side 
    lCylind = cmds.polyCylinder(r=cubeSizeY*0.5, h=cubeSizeX)
    cmds.rotate(90, rotateX=True, a=True)
    cmds.rotate(90, rotateY=True, a=True)
    cmds.move((cubeSizeX/2.0 + 0.079), moveY=True, a=True)
    cmds.move((cubeSizeZ * 0.5), moveZ=True, a=True)
    # merge left cylinder with cube
    cube = cmds.polyCBoolOp(cube, lCylind, op=1, caching=False, ch=False)
    # create a hole 
    lHole = cmds.polyCylinder(r=0.25, h=height/2.0)
    cmds.rotate(90, rotateX=True, a=True)
    cmds.rotate(90, rotateY=True, a=True)       
    cmds.move((cubeSizeY/2.0), moveY=True, a=True)
    cmds.move(((width * 0.8) - cubeSizeX), moveX=True, a=True) 
    cmds.move(((length * 0.8) - (cubeSizeZ/2.0)), moveZ=True, a=True)
    cube = cmds.polyCBoolOp(cube, lHole, op=2, caching=False, ch=False)
    
    # create a second cube for bend 
    if(bendAngle == 1): # at 90 degrees
        cubeBend = cmds.polyCube(h=cubeSizeY, w=cubeSizeX, d=bendSizeZ)
        cmds.rotate(90, rotateX=True, a=True)
        
        # move it up 
        cmds.move((bendSizeZ/2.0), moveY=True)
        
        # add cylinder to its end
        endCylind = cmds.polyCylinder(r=cubeSizeY*0.5, h=cubeSizeX)
        cmds.rotate(90, rotateX=True, a=True)
        cmds.rotate(90, rotateY=True, a=True)
        cmds.move((bendSizeZ), moveY=True, a=True)    
         
        # merge cube with cylinder 
        cubeBend = cmds.polyCBoolOp(cubeBend, endCylind, op=1, caching=False, ch=False)
        
        # move bended cube to cube's end
        cmds.move((-cubeSizeZ/2), moveZ=True, a=True)
        
        # move it up a bit
        cmds.move(0.5, moveY=True)
        
        # add holes to bended part
        # create holes
        for i in range(width):
            for j in range(bendLength):
                # create cylinder in the place of a hole
                bHole = cmds.polyCylinder(r=0.25, h=height/2.0)        
                # rotate and position it
                cmds.rotate(90, rotateX=True, a=True)
                cmds.rotate(90, rotateY=True, a=True)
                cmds.move((cubeSizeY/2.0), moveY=True, a=True)
                cmds.move(((0 * 0.8) - (cubeSizeZ/2.0)), moveZ=True, a=True)
                cmds.move(((0 * 0.8) - (cubeSizeX/2.0) + 0.4), moveX=True, a=True) 
                cmds.move(((j * 0.8) + (cubeSizeY/2.0)), moveY=True, a=True)
                # remove it from the base block
                cubeBend = cmds.polyCBoolOp(cubeBend, bHole, op=2, caching=False, ch=False)     
        
        # create the last hole
        endHole = cmds.polyCylinder(r=0.25, h=height/2.0)
        # rotate and position it
        cmds.rotate(90, rotateX=True, a=True)
        cmds.rotate(90, rotateY=True, a=True)
        cmds.move((cubeSizeY/2.0), moveY=True, a=True)
        cmds.move(((0 * 0.8) - (cubeSizeZ/2.0)), moveZ=True, a=True)
        cmds.move((((bendLength) * 0.8) + (cubeSizeY/2.0)), moveY=True, a=True)
        # remove it from end cylinder
        cubeBend = cmds.polyCBoolOp(cubeBend, endHole, op=2, caching=False, ch=False) 
        
    if(bendAngle == 2):    # bend at 60 degrees 
        # create a cube for bend
        cubeBend = cmds.polyCube(h=cubeSizeY, w=cubeSizeX, d=bendSizeZ)
        # move & rotate
        cmds.move((cubeSizeY), moveY=True)
        cmds.rotate(60, rotateX=True, a=True)
        cmds.move(( 0 -(cubeSizeZ/2.0) + 1.04), moveZ=True, a=True)   
            
        # add cylinder to its end
        endCylind = cmds.polyCylinder(r=cubeSizeY*0.5+0.01, h=cubeSizeX)
        cmds.rotate(90, rotateX=True, a=True)
        cmds.rotate(90, rotateY=True, a=True)
        cmds.move((bendSizeZ - 0.4), moveY=True, a=True) 
        cmds.move((-bendSizeZ/2 + 0.04), moveZ=True, a=True)    
         
        # merge cube with cylinder 
        cubeBend = cmds.polyCBoolOp(cubeBend, endCylind, op=1, caching=False, ch=False)
        
        # move bended cube to cube's end
        cmds.move((-cubeSizeZ/2), moveZ=True, a=True)
        
        # move it up a bit
        cmds.move(0.5, moveY=True)
        
        # add holes to bended part
        # create holes  
        # HOLE ONE (from bottom)
        hole1 = cmds.polyCylinder(r=0.25, h=height/2.0)        
        # rotate and position it
        cmds.rotate(90, rotateX=True, a=True)
        cmds.rotate(90, rotateY=True, a=True)
        cmds.move(cubeSizeY/2, moveY=True, a=True)
        cmds.move(-cubeSizeZ/2.0, moveZ=True, a=True)
        cmds.move(((0 * 0.8) - (cubeSizeX*0.5) + 0.4), moveX=True, a=True) 
        # remove it from the base block
        cubeBend = cmds.polyCBoolOp(cubeBend, hole1, op=2, caching=False, ch=False)  
        
        # HOLE TWO
        hole2 = cmds.polyCylinder(r=0.25, h=height/2.0)
        # rotate and position it
        cmds.rotate(90, rotateX=True, a=True)
        cmds.rotate(90, rotateY=True, a=True)
        cmds.move(1.129, moveY=True, a=True)
        cmds.move(-1.994, moveZ=True, a=True)
        # remove it from the base block
        cubeBend = cmds.polyCBoolOp(cubeBend, hole2, op=2, caching=False, ch=False)  
          
        # HOLE THREE 
        hole3 = cmds.polyCylinder(r=0.25, h=height/2.0)
        # rotate and position it
        cmds.rotate(90, rotateX=True, a=True)
        cmds.rotate(90, rotateY=True, a=True) 
        cmds.move(1.834, moveY=True, a=True)
        cmds.move(-2.363, moveZ=True, a=True) 
        # remove it from the base block
        cubeBend = cmds.polyCBoolOp(cubeBend, hole3, op=2, caching=False, ch=False)  
        
        # HOLE FOUR
        endHole = cmds.polyCylinder(r=0.25, h=height/2.0)
        # rotate and position it
        cmds.rotate(90, rotateX=True, a=True)
        cmds.rotate(90, rotateY=True, a=True)
        cmds.move(-2.741, moveZ=True, a=True)
        cmds.move(2.49, moveY=True, a=True)
        # remove it from end cylinder
        cubeBend = cmds.polyCBoolOp(cubeBend, endHole, op=2, caching=False, ch=False)    
       
    # add material       
    myShader = cmds.shadingNode('lambert', asShader=True, name="blckMat")
    cmds.setAttr(nsTmp+":blckMat.color",rgb[0],rgb[1],rgb[2], type='double3')
    
    cmds.polyUnite((nsTmp+":*"), n=nsTmp, ch=False)
    cmds.delete(ch=True)
    
    cmds.hyperShade(assign=(nsTmp+":blckMat"))  
    cmds.namespace(removeNamespace=":"+nsTmp,mergeNamespaceWithParent=True)
    
#################################################################
#                       Wheel and Hub                           #
#################################################################
def createWheel():
    # query UI choice
    createTire = cmds.radioButtonGrp('wheelTire', q=True, sl=True)
    createHub = cmds.radioButtonGrp('wheelHub', q=True, sl=True)
    
    # create a tire 
    if(createTire == 1):
        # name
        nsTmp = "Tire" + str(rnd.randint(1000,9999))
        cmds.select(clear=True)
        cmds.namespace(add=nsTmp)
        cmds.namespace(set=nsTmp)
        # query colour from UI
        rgb = cmds.colorSliderGrp('tireColour', q=True, rgbValue=True)
        # create cylinder for the base
        tire = cmds.polyCylinder(r=3.5, h=3.5, sx=36)
        # add a smaller sphere to round up the tire
        tmp = cmds.polySphere(r=3.35, sy=15, sx=36)
        cmds.scale(1.1, scaleY=True)
        # remove non intersecting parts 
        tire = cmds.polyCBoolOp(tire, tmp, op=3, ch=False)
        # Add texture:
        # create cylinder as the base for texture at 1 side 
        texture1 = cmds.polyCylinder(r=2.8, h=1.75, sx=36)
        # move it up 
        cmds.move(1.75/2, moveY=True, a=True)
        # in range of subdivisions 
        for i in range(35):
             #for all even numbers
             if(i % 2 == 0):
                 cmds.select(texture1[0] + ".f[" + str(i) + "]")
                 # local translate on Z and scale x 
                 cmds.polyExtrudeFacet(ltz=1, lsx=1.35)
        # duplicate texture 1 for the 2nd side
        texture2 = cmds.duplicate(texture1)
        cmds.select(texture2)
        cmds.move(-1.75/2, moveY=True, a=True) 
        cmds.rotate(10, rotateY=True, a=True)
        # combine textures 1 and 2
        texture = cmds.polyCBoolOp(texture1, texture2, op=1, ch=False)
        # add a smaller sphere to round up the texture
        tmp = cmds.polySphere(r=3.7, sy=13, sx=36)
        # remove non intersecting parts 
        texture = cmds.polyCBoolOp(texture, tmp, op=3, ch=False)
        cmds.polyMergeVertex(d=0.05, ch=False)
        # create another cylinder for the hole
        tmp = cmds.polyCylinder(r=2, h=3.5)
        # remove it
        tire = cmds.polyCBoolOp(tire, tmp, op=2, ch=False)
        tmp = cmds.polyCylinder(r=2, h=3.5)
        texture = cmds.polyCBoolOp(texture, tmp, op=2, ch=False)
        
        # add material       
        myShader = cmds.shadingNode('lambert', asShader=True, name="blckMat")
        cmds.setAttr(nsTmp+":blckMat.color",rgb[0],rgb[1],rgb[2], type='double3')
        cmds.polyUnite((nsTmp+":*"), n=nsTmp, ch=False)
        cmds.rotate(90, rotateX=True, a=True)
        cmds.rotate(90, rotateY=True, a=True)
        cmds.move(3.466, moveY=True, a=True)
        
        cmds.delete(ch=True)
        
        cmds.hyperShade(assign=(nsTmp+":blckMat"))  
        cmds.namespace(removeNamespace=":"+nsTmp,mergeNamespaceWithParent=True)

    # create a hub
    if (createHub == 1):
        # name
        nsTmp = "Hub" + str(rnd.randint(1000,9999))
        cmds.select(clear=True)
        cmds.namespace(add=nsTmp)
        cmds.namespace(set=nsTmp)
        # query colour from UI
        rgb = cmds.colorSliderGrp('hubColour', q=True, rgbValue=True)
        
        # base 
        hub = cmds.polyCylinder(r=2.1, h=2.8)
        # outline
        tmp = cmds.polyCylinder(r=1.6, h=2.8)
        hub = cmds.polyCBoolOp(hub, tmp, op=2, ch=False)
        # inner part of the hub
        hubIn = cmds.polyCylinder(r=1.6, h=1.8)
        # center 
        hubCenter = cmds.polyCylinder(r=0.3, h=2.4)
        hubIn = cmds.polyCBoolOp(hubIn, hubCenter, op=2, ch=False)
        
        # decor parts
        d1 = cmds.polyCylinder(r=0.4, h=2.8)
        cmds.move(-0.85, moveX=True, a=True)
        cmds.move(-0.03, moveZ=True, a=True)
        hubIn = cmds.polyCBoolOp(hubIn, d1, op=1, ch=False)
        # subtract smaller cylinder inside 
        d1c = cmds.polyCylinder(r=0.3, h=2.9)
        cmds.move(-0.85, moveX=True, a=True)
        cmds.move(-0.03, moveZ=True, a=True)
        hubIn = cmds.polyCBoolOp(hubIn, d1c, op=2, ch=False)

        d3 = cmds.polyCylinder(r=0.4, h=2.8) 
        cmds.move(-0.422, moveX=True, a=True)
        cmds.move(0.648, moveZ=True, a=True)
        hubIn = cmds.polyCBoolOp(hubIn, d3, op=1, ch=False)
        # subtract smaller cylinder inside 
        d3c = cmds.polyCylinder(r=0.3, h=2.9)
        cmds.move(-0.422, moveX=True, a=True)
        cmds.move(0.648, moveZ=True, a=True)
        hubIn = cmds.polyCBoolOp(hubIn, d3c, op=2, ch=False)

        d4 = cmds.polyCylinder(r=0.4, h=2.8)
        cmds.move(0.416, moveX=True, a=True)
        cmds.move(0.627, moveZ=True, a=True)
        hubIn = cmds.polyCBoolOp(hubIn, d4, op=1, ch=False)
        # subtract smaller cylinder inside 
        d4c = cmds.polyCylinder(r=0.3, h=2.9)
        cmds.move(0.416, moveX=True, a=True)
        cmds.move(0.627, moveZ=True, a=True)
        hubIn = cmds.polyCBoolOp(hubIn, d4c, op=2, ch=False)
        
        d5 = cmds.polyCylinder(r=0.4, h=2.8)
        cmds.move(0.835, moveX=True, a=True)
        cmds.move(-0.049, moveZ=True, a=True)
        hubIn = cmds.polyCBoolOp(hubIn, d5, op=1, ch=False)
        # subtract smaller cylinder inside 
        d5c = cmds.polyCylinder(r=0.3, h=2.9)
        cmds.move(0.835, moveX=True, a=True)
        cmds.move(-0.049, moveZ=True, a=True)
        hubIn = cmds.polyCBoolOp(hubIn, d5c, op=2, ch=False)
        
        d6 = cmds.polyCylinder(r=0.4, h=2.8)
        cmds.move(0.431, moveX=True, a=True)
        cmds.move(-0.692, moveZ=True, a=True)
        hubIn = cmds.polyCBoolOp(hubIn, d6, op=1, ch=False)
        # subtract smaller cylinder inside 
        d6c = cmds.polyCylinder(r=0.3, h=2.9)
        cmds.move(0.431, moveX=True, a=True)
        cmds.move(-0.692, moveZ=True, a=True)
        hubIn = cmds.polyCBoolOp(hubIn, d6c, op=2, ch=False)
        
        d7 = cmds.polyCylinder(r=0.4, h=2.8)
        cmds.move(-0.384, moveX=True, a=True)
        cmds.move(-0.734, moveZ=True, a=True)
        hubIn = cmds.polyCBoolOp(hubIn, d7, op=1, ch=False)
        # subtract smaller cylinder inside 
        d7c = cmds.polyCylinder(r=0.3, h=2.9)
        cmds.move(-0.384, moveX=True, a=True)
        cmds.move(-0.734, moveZ=True, a=True)
        hubIn = cmds.polyCBoolOp(hubIn, d7c, op=2, ch=False)
        
        # add material       
        myShader = cmds.shadingNode('lambert', asShader=True, name="blckMat")
        cmds.setAttr(nsTmp+":blckMat.color",rgb[0],rgb[1],rgb[2], type='double3')
        
        cmds.polyUnite((nsTmp+":*"), n=nsTmp, ch=False)
        cmds.rotate(90, rotateX=True, a=True)
        cmds.rotate(90, rotateY=True, a=True)
        cmds.move(3.466, moveY=True, a=True)
        cmds.delete(ch=True)
        
        cmds.hyperShade(assign=(nsTmp+":blckMat"))  
        cmds.namespace(removeNamespace=":"+nsTmp,mergeNamespaceWithParent=True)
        
              
#################################################################
#                             Gear                              #  
#################################################################   
def createGear(): 
    teeth = 16
    teethLength = 0.2
    
    # name
    nsTmp = "Gear" + str(rnd.randint(1000,9999))
    cmds.select(clear=True)
    cmds.namespace(add=nsTmp)
    cmds.namespace(set=nsTmp)
    # query colour from UI
    rgb = cmds.colorSliderGrp('gearColour', q=True, rgbValue=True)
    
    # base
    gear = cmds.polyCylinder(r=0.7, h=0.4, sx=32) 
    
    # extrude teeth
    for i in range(31):
        if(i % 2 == 0):
            cmds.select(gear[0] + ".f[" + str(i) + "]")
            cmds.polyExtrudeFacet(ltz=0.1)
            cmds.polyExtrudeFacet(ltz=0.1)
            cmds.polyMoveFacet(lsx=0.5)
    
    # decor 
    tmp = cmds.polyCylinder(r=0.6, h=0.2)
    cmds.move(0.2, moveY=True, a=True)
    gear = cmds.polyCBoolOp(gear, tmp, op=2, ch=False)
    tmp = cmds.polyCylinder(r=0.6, h=0.2)
    cmds.move(-0.2, moveY=True, a=True)
    gear = cmds.polyCBoolOp(gear, tmp, op=2, ch=False)
    # center 
    cylind = cmds.polyCylinder(r=0.3, h=0.6)
    #create x shape
    x = cmds.polyCube(w=0.5, h=0.6, d=0.2)
    tmp = cmds.polyCube(w=0.2, h=0.6, d=0.5)
    #combine them
    x = cmds.polyCBoolOp(x, tmp, op=1)
    x2 = cmds.duplicate(x)
    # remove from center
    cylind = cmds.polyCBoolOp(cylind, x, op=2)
    # remove from base 
    gear = cmds.polyCBoolOp(gear, x2, op=2)
    
    # add material       
    myShader = cmds.shadingNode('lambert', asShader=True, name="blckMat")
    cmds.setAttr(nsTmp+":blckMat.color",rgb[0],rgb[1],rgb[2], type='double3')
        
    cmds.polyUnite((nsTmp+":*"), n=nsTmp, ch=False)
    cmds.move(0.3, moveY=True, a=True)
    cmds.delete(ch=True)
        
    cmds.hyperShade(assign=(nsTmp+":blckMat"))  
    cmds.namespace(removeNamespace=":"+nsTmp,mergeNamespaceWithParent=True) 

#################################################################
#                             Rack                              #  
#################################################################   
def createRack():
    rgb = cmds.colorSliderGrp('rackColour', q=True, rgbValue=True)
    
    # name
    nsTmp = "Rack" + str(rnd.randint(1000,9999))
    
    cmds.select(clear=True)
    cmds.namespace(add=nsTmp)
    cmds.namespace(set=nsTmp)
    
    # base
    rack = cmds.polyCube(h=0.6, w=1.5, d=6, sz=24)
    
    # extrude teeth
    for i in range(24):
        if(i % 2 == 1):
            cmds.select(rack[0] + ".f[" + str(i) + "]")
            cmds.polyExtrudeFacet(ltz=0.3)
            cmds.polyExtrudeFacet(ltz=0.3)
            cmds.polyMoveFacet(lsx=0.1)
            
    tmp = cmds.polyCube(h=0.6, w=1.5, d=2)
    cmds.move(-3.753, moveZ = True)
    rack = cmds.polyCBoolOp(rack, tmp, op=2)
    tmp = cmds.polyCube(h=0.6, w=1.5, d=2)
            
    # add material       
    myShader = cmds.shadingNode('lambert', asShader=True, name="blckMat")
    cmds.setAttr(nsTmp+":blckMat.color",rgb[0],rgb[1],rgb[2], type='double3')
        
    cmds.polyUnite((nsTmp+":*"), n=nsTmp, ch=False)
    cmds.move(0.4, moveY=True, a=True)
    cmds.delete(ch=True)
        
    cmds.hyperShade(assign=(nsTmp+":blckMat"))  
    cmds.namespace(removeNamespace=":"+nsTmp,mergeNamespaceWithParent=True) 

