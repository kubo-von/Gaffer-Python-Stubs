
def ALLOCATION_LG2 (*args):
      '''

'''      
    ...

def ALLOCATION_UNIFORM (*args):
      '''

'''      
    ...

def ALLOCATION_UNKNOWN (*args):
      '''

'''      
    ...

def Allocation (*args):
      '''

'''      
    ...

class Allocation:
    def ALLOCATION_LG2 (self, *args, **kwargs):
      '''

Members:

  ALLOCATION_UNKNOWN : 

  ALLOCATION_UNIFORM : 

  ALLOCATION_LG2 : '''
    ...
    def ALLOCATION_UNIFORM (self, *args, **kwargs):
      '''

Members:

  ALLOCATION_UNKNOWN : 

  ALLOCATION_UNIFORM : 

  ALLOCATION_LG2 : '''
    ...
    def ALLOCATION_UNKNOWN (self, *args, **kwargs):
      '''

Members:

  ALLOCATION_UNKNOWN : 

  ALLOCATION_UNIFORM : 

  ALLOCATION_LG2 : '''
    ...
    def name (self, *args, **kwargs):
      '''name(self: handle) -> str
'''
    ...
    def value (self, *args, **kwargs):
      ''''''
    ...

def AllocationFromString (*args):
      '''

'''      
    ...

def AllocationToString (*args):
      '''

'''      
    ...

def AllocationTransform (*args):
      '''

'''      
    ...

class AllocationTransform:
    def getAllocation (self, *args, **kwargs):
      '''getAllocation(self: PyOpenColorIO.AllocationTransform) -> PyOpenColorIO.Allocation
'''
    ...
    def getDirection (self, *args, **kwargs):
      '''getDirection(self: PyOpenColorIO.Transform) -> PyOpenColorIO.TransformDirection
'''
    ...
    def getTransformType (self, *args, **kwargs):
      '''getTransformType(self: PyOpenColorIO.Transform) -> PyOpenColorIO.TransformType
'''
    ...
    def getVars (self, *args, **kwargs):
      '''getVars(self: PyOpenColorIO.AllocationTransform) -> List[float]
'''
    ...
    def setAllocation (self, *args, **kwargs):
      '''setAllocation(self: PyOpenColorIO.AllocationTransform, allocation: PyOpenColorIO.Allocation) -> None
'''
    ...
    def setDirection (self, *args, **kwargs):
      '''setDirection(self: PyOpenColorIO.Transform, direction: PyOpenColorIO.TransformDirection) -> None
'''
    ...
    def setVars (self, *args, **kwargs):
      '''setVars(self: PyOpenColorIO.AllocationTransform, vars: List[float]) -> None
'''
    ...
    def validate (self, *args, **kwargs):
      '''validate(self: PyOpenColorIO.Transform) -> None
'''
    ...

def AutoStride (*args):
      '''

'''      
    ...

def BIT_DEPTH_F16 (*args):
      '''

'''      
    ...

def BIT_DEPTH_F32 (*args):
      '''

'''      
    ...

def BIT_DEPTH_UINT10 (*args):
      '''

'''      
    ...

def BIT_DEPTH_UINT12 (*args):
      '''

'''      
    ...

def BIT_DEPTH_UINT14 (*args):
      '''

'''      
    ...

def BIT_DEPTH_UINT16 (*args):
      '''

'''      
    ...

def BIT_DEPTH_UINT32 (*args):
      '''

'''      
    ...

def BIT_DEPTH_UINT8 (*args):
      '''

'''      
    ...

def BIT_DEPTH_UNKNOWN (*args):
      '''

'''      
    ...

def Baker (*args):
      '''

'''      
    ...

class Baker:
    def FormatIterator (self, *args, **kwargs):
      '''
Iterator on LUT baker Formats.

Each item is a tuple containing format name and format extension.
'''
    ...
    def bake (self, *args, **kwargs):
      '''bake(*args, **kwargs)
Overloaded function.

1. bake(self: PyOpenColorIO.Baker, fileName: str) -> None

2. bake(self: PyOpenColorIO.Baker) -> str
'''
    ...
    def getConfig (self, *args, **kwargs):
      '''getConfig(self: PyOpenColorIO.Baker) -> PyOpenColorIO.Config
'''
    ...
    def getCubeSize (self, *args, **kwargs):
      '''getCubeSize(self: PyOpenColorIO.Baker) -> int
'''
    ...
    def getDisplay (self, *args, **kwargs):
      '''getDisplay(self: PyOpenColorIO.Baker) -> str
'''
    ...
    def getFormat (self, *args, **kwargs):
      '''getFormat(self: PyOpenColorIO.Baker) -> str
'''
    ...
    def getFormatMetadata (self, *args, **kwargs):
      '''getFormatMetadata(self: PyOpenColorIO.Baker) -> PyOpenColorIO.FormatMetadata
'''
    ...
    def getFormats (self, *args, **kwargs):
      '''getFormats() -> PyOpenColorIO.Baker.FormatIterator
'''
    ...
    def getInputSpace (self, *args, **kwargs):
      '''getInputSpace(self: PyOpenColorIO.Baker) -> str
'''
    ...
    def getLooks (self, *args, **kwargs):
      '''getLooks(self: PyOpenColorIO.Baker) -> str
'''
    ...
    def getShaperSize (self, *args, **kwargs):
      '''getShaperSize(self: PyOpenColorIO.Baker) -> int
'''
    ...
    def getShaperSpace (self, *args, **kwargs):
      '''getShaperSpace(self: PyOpenColorIO.Baker) -> str
'''
    ...
    def getTargetSpace (self, *args, **kwargs):
      '''getTargetSpace(self: PyOpenColorIO.Baker) -> str
'''
    ...
    def getView (self, *args, **kwargs):
      '''getView(self: PyOpenColorIO.Baker) -> str
'''
    ...
    def setConfig (self, *args, **kwargs):
      '''setConfig(self: PyOpenColorIO.Baker, config: PyOpenColorIO.Config) -> None
'''
    ...
    def setCubeSize (self, *args, **kwargs):
      '''setCubeSize(self: PyOpenColorIO.Baker, cubeSize: int) -> None
'''
    ...
    def setDisplayView (self, *args, **kwargs):
      '''setDisplayView(self: PyOpenColorIO.Baker, display: str, view: str) -> None
'''
    ...
    def setFormat (self, *args, **kwargs):
      '''setFormat(self: PyOpenColorIO.Baker, formatName: str) -> None
'''
    ...
    def setInputSpace (self, *args, **kwargs):
      '''setInputSpace(self: PyOpenColorIO.Baker, inputSpace: str) -> None
'''
    ...
    def setLooks (self, *args, **kwargs):
      '''setLooks(self: PyOpenColorIO.Baker, looks: str) -> None
'''
    ...
    def setShaperSize (self, *args, **kwargs):
      '''setShaperSize(self: PyOpenColorIO.Baker, shaperSize: int) -> None
'''
    ...
    def setShaperSpace (self, *args, **kwargs):
      '''setShaperSpace(self: PyOpenColorIO.Baker, shaperSpace: str) -> None
'''
    ...
    def setTargetSpace (self, *args, **kwargs):
      '''setTargetSpace(self: PyOpenColorIO.Baker, targetSpace: str) -> None
'''
    ...

def BitDepth (*args):
      '''

'''      
    ...

class BitDepth:
    def BIT_DEPTH_F16 (self, *args, **kwargs):
      '''

Members:

  BIT_DEPTH_UNKNOWN : 

  BIT_DEPTH_UINT8 : 

  BIT_DEPTH_UINT10 : 

  BIT_DEPTH_UINT12 : 

  BIT_DEPTH_UINT14 : 

  BIT_DEPTH_UINT16 : 

  BIT_DEPTH_UINT32 : 

  BIT_DEPTH_F16 : 

  BIT_DEPTH_F32 : '''
    ...
    def BIT_DEPTH_F32 (self, *args, **kwargs):
      '''

Members:

  BIT_DEPTH_UNKNOWN : 

  BIT_DEPTH_UINT8 : 

  BIT_DEPTH_UINT10 : 

  BIT_DEPTH_UINT12 : 

  BIT_DEPTH_UINT14 : 

  BIT_DEPTH_UINT16 : 

  BIT_DEPTH_UINT32 : 

  BIT_DEPTH_F16 : 

  BIT_DEPTH_F32 : '''
    ...
    def BIT_DEPTH_UINT10 (self, *args, **kwargs):
      '''

Members:

  BIT_DEPTH_UNKNOWN : 

  BIT_DEPTH_UINT8 : 

  BIT_DEPTH_UINT10 : 

  BIT_DEPTH_UINT12 : 

  BIT_DEPTH_UINT14 : 

  BIT_DEPTH_UINT16 : 

  BIT_DEPTH_UINT32 : 

  BIT_DEPTH_F16 : 

  BIT_DEPTH_F32 : '''
    ...
    def BIT_DEPTH_UINT12 (self, *args, **kwargs):
      '''

Members:

  BIT_DEPTH_UNKNOWN : 

  BIT_DEPTH_UINT8 : 

  BIT_DEPTH_UINT10 : 

  BIT_DEPTH_UINT12 : 

  BIT_DEPTH_UINT14 : 

  BIT_DEPTH_UINT16 : 

  BIT_DEPTH_UINT32 : 

  BIT_DEPTH_F16 : 

  BIT_DEPTH_F32 : '''
    ...
    def BIT_DEPTH_UINT14 (self, *args, **kwargs):
      '''

Members:

  BIT_DEPTH_UNKNOWN : 

  BIT_DEPTH_UINT8 : 

  BIT_DEPTH_UINT10 : 

  BIT_DEPTH_UINT12 : 

  BIT_DEPTH_UINT14 : 

  BIT_DEPTH_UINT16 : 

  BIT_DEPTH_UINT32 : 

  BIT_DEPTH_F16 : 

  BIT_DEPTH_F32 : '''
    ...
    def BIT_DEPTH_UINT16 (self, *args, **kwargs):
      '''

Members:

  BIT_DEPTH_UNKNOWN : 

  BIT_DEPTH_UINT8 : 

  BIT_DEPTH_UINT10 : 

  BIT_DEPTH_UINT12 : 

  BIT_DEPTH_UINT14 : 

  BIT_DEPTH_UINT16 : 

  BIT_DEPTH_UINT32 : 

  BIT_DEPTH_F16 : 

  BIT_DEPTH_F32 : '''
    ...
    def BIT_DEPTH_UINT32 (self, *args, **kwargs):
      '''

Members:

  BIT_DEPTH_UNKNOWN : 

  BIT_DEPTH_UINT8 : 

  BIT_DEPTH_UINT10 : 

  BIT_DEPTH_UINT12 : 

  BIT_DEPTH_UINT14 : 

  BIT_DEPTH_UINT16 : 

  BIT_DEPTH_UINT32 : 

  BIT_DEPTH_F16 : 

  BIT_DEPTH_F32 : '''
    ...
    def BIT_DEPTH_UINT8 (self, *args, **kwargs):
      '''

Members:

  BIT_DEPTH_UNKNOWN : 

  BIT_DEPTH_UINT8 : 

  BIT_DEPTH_UINT10 : 

  BIT_DEPTH_UINT12 : 

  BIT_DEPTH_UINT14 : 

  BIT_DEPTH_UINT16 : 

  BIT_DEPTH_UINT32 : 

  BIT_DEPTH_F16 : 

  BIT_DEPTH_F32 : '''
    ...
    def BIT_DEPTH_UNKNOWN (self, *args, **kwargs):
      '''

Members:

  BIT_DEPTH_UNKNOWN : 

  BIT_DEPTH_UINT8 : 

  BIT_DEPTH_UINT10 : 

  BIT_DEPTH_UINT12 : 

  BIT_DEPTH_UINT14 : 

  BIT_DEPTH_UINT16 : 

  BIT_DEPTH_UINT32 : 

  BIT_DEPTH_F16 : 

  BIT_DEPTH_F32 : '''
    ...
    def name (self, *args, **kwargs):
      '''name(self: handle) -> str
'''
    ...
    def value (self, *args, **kwargs):
      ''''''
    ...

def BitDepthFromString (*args):
      '''

'''      
    ...

def BitDepthIsFloat (*args):
      '''

'''      
    ...

def BitDepthToInt (*args):
      '''

'''      
    ...

def BitDepthToString (*args):
      '''

'''      
    ...

def BoolFromString (*args):
      '''

'''      
    ...

def BoolToString (*args):
      '''

'''      
    ...

def BuiltinConfigRegistry (*args):
      '''

'''      
    ...

class BuiltinConfigRegistry:
    def BuiltinConfigIterator (self, *args, **kwargs):
      '''None'''
    ...
    def BuiltinConfigNameIterator (self, *args, **kwargs):
      '''None'''
    ...
    def getBuiltinConfigs (self, *args, **kwargs):
      '''getBuiltinConfigs(self: PyOpenColorIO.BuiltinConfigRegistry) -> PyOpenColorIO.BuiltinConfigRegistry.BuiltinConfigIterator
'''
    ...
    def getDefaultBuiltinConfigName (self, *args, **kwargs):
      '''getDefaultBuiltinConfigName(self: PyOpenColorIO.BuiltinConfigRegistry) -> str
'''
    ...

def BuiltinTransform (*args):
      '''

'''      
    ...

class BuiltinTransform:
    def getDescription (self, *args, **kwargs):
      '''getDescription(self: PyOpenColorIO.BuiltinTransform) -> str
'''
    ...
    def getDirection (self, *args, **kwargs):
      '''getDirection(self: PyOpenColorIO.Transform) -> PyOpenColorIO.TransformDirection
'''
    ...
    def getStyle (self, *args, **kwargs):
      '''getStyle(self: PyOpenColorIO.BuiltinTransform) -> str
'''
    ...
    def getTransformType (self, *args, **kwargs):
      '''getTransformType(self: PyOpenColorIO.Transform) -> PyOpenColorIO.TransformType
'''
    ...
    def setDirection (self, *args, **kwargs):
      '''setDirection(self: PyOpenColorIO.Transform, direction: PyOpenColorIO.TransformDirection) -> None
'''
    ...
    def setStyle (self, *args, **kwargs):
      '''setStyle(self: PyOpenColorIO.BuiltinTransform, style: str) -> None
'''
    ...
    def validate (self, *args, **kwargs):
      '''validate(self: PyOpenColorIO.Transform) -> None
'''
    ...

def BuiltinTransformRegistry (*args):
      '''

'''      
    ...

class BuiltinTransformRegistry:
    def BuiltinIterator (self, *args, **kwargs):
      '''None'''
    ...
    def BuiltinStyleIterator (self, *args, **kwargs):
      '''None'''
    ...
    def getBuiltins (self, *args, **kwargs):
      '''getBuiltins(self: PyOpenColorIO.BuiltinTransformRegistry) -> PyOpenColorIO.BuiltinTransformRegistry.BuiltinIterator
'''
    ...

def CDLStyle (*args):
      '''

'''      
    ...

class CDLStyle:
    def CDL_ASC (self, *args, **kwargs):
      '''

Members:

  CDL_ASC : 

  CDL_NO_CLAMP : 

  CDL_TRANSFORM_DEFAULT : '''
    ...
    def CDL_NO_CLAMP (self, *args, **kwargs):
      '''

Members:

  CDL_ASC : 

  CDL_NO_CLAMP : 

  CDL_TRANSFORM_DEFAULT : '''
    ...
    def CDL_TRANSFORM_DEFAULT (self, *args, **kwargs):
      '''

Members:

  CDL_ASC : 

  CDL_NO_CLAMP : 

  CDL_TRANSFORM_DEFAULT : '''
    ...
    def name (self, *args, **kwargs):
      '''name(self: handle) -> str
'''
    ...
    def value (self, *args, **kwargs):
      ''''''
    ...

def CDLStyleFromString (*args):
      '''

'''      
    ...

def CDLStyleToString (*args):
      '''

'''      
    ...

def CDLTransform (*args):
      '''

'''      
    ...

class CDLTransform:
    def CreateFromFile (self, *args, **kwargs):
      '''CreateFromFile(src: str, id: str) -> PyOpenColorIO.CDLTransform
'''
    ...
    def CreateGroupFromFile (self, *args, **kwargs):
      '''CreateGroupFromFile(src: str) -> PyOpenColorIO.GroupTransform
'''
    ...
    def equals (self, *args, **kwargs):
      '''equals(self: PyOpenColorIO.CDLTransform, other: PyOpenColorIO.CDLTransform) -> bool
'''
    ...
    def getDirection (self, *args, **kwargs):
      '''getDirection(self: PyOpenColorIO.Transform) -> PyOpenColorIO.TransformDirection
'''
    ...
    def getFirstSOPDescription (self, *args, **kwargs):
      '''getFirstSOPDescription(self: PyOpenColorIO.CDLTransform) -> str
'''
    ...
    def getFormatMetadata (self, *args, **kwargs):
      '''getFormatMetadata(self: PyOpenColorIO.CDLTransform) -> PyOpenColorIO.FormatMetadata
'''
    ...
    def getID (self, *args, **kwargs):
      '''getID(self: PyOpenColorIO.CDLTransform) -> str
'''
    ...
    def getOffset (self, *args, **kwargs):
      '''getOffset(self: PyOpenColorIO.CDLTransform) -> List[float[3]]
'''
    ...
    def getPower (self, *args, **kwargs):
      '''getPower(self: PyOpenColorIO.CDLTransform) -> List[float[3]]
'''
    ...
    def getSOP (self, *args, **kwargs):
      '''getSOP(self: PyOpenColorIO.CDLTransform) -> List[float[9]]
'''
    ...
    def getSat (self, *args, **kwargs):
      '''getSat(self: PyOpenColorIO.CDLTransform) -> float
'''
    ...
    def getSatLumaCoefs (self, *args, **kwargs):
      '''getSatLumaCoefs(self: PyOpenColorIO.CDLTransform) -> List[float[3]]
'''
    ...
    def getSlope (self, *args, **kwargs):
      '''getSlope(self: PyOpenColorIO.CDLTransform) -> List[float[3]]
'''
    ...
    def getStyle (self, *args, **kwargs):
      '''getStyle(self: PyOpenColorIO.CDLTransform) -> PyOpenColorIO.CDLStyle
'''
    ...
    def getTransformType (self, *args, **kwargs):
      '''getTransformType(self: PyOpenColorIO.Transform) -> PyOpenColorIO.TransformType
'''
    ...
    def setDirection (self, *args, **kwargs):
      '''setDirection(self: PyOpenColorIO.Transform, direction: PyOpenColorIO.TransformDirection) -> None
'''
    ...
    def setFirstSOPDescription (self, *args, **kwargs):
      '''setFirstSOPDescription(self: PyOpenColorIO.CDLTransform, description: str) -> None
'''
    ...
    def setID (self, *args, **kwargs):
      '''setID(self: PyOpenColorIO.CDLTransform, id: str) -> None
'''
    ...
    def setOffset (self, *args, **kwargs):
      '''setOffset(self: PyOpenColorIO.CDLTransform, rgb: List[float[3]]) -> None
'''
    ...
    def setPower (self, *args, **kwargs):
      '''setPower(self: PyOpenColorIO.CDLTransform, rgb: List[float[3]]) -> None
'''
    ...
    def setSOP (self, *args, **kwargs):
      '''setSOP(self: PyOpenColorIO.CDLTransform, vec9: List[float[9]]) -> None
'''
    ...
    def setSat (self, *args, **kwargs):
      '''setSat(self: PyOpenColorIO.CDLTransform, sat: float) -> None
'''
    ...
    def setSlope (self, *args, **kwargs):
      '''setSlope(self: PyOpenColorIO.CDLTransform, rgb: List[float[3]]) -> None
'''
    ...
    def setStyle (self, *args, **kwargs):
      '''setStyle(self: PyOpenColorIO.CDLTransform, style: PyOpenColorIO.CDLStyle) -> None
'''
    ...
    def validate (self, *args, **kwargs):
      '''validate(self: PyOpenColorIO.Transform) -> None
'''
    ...

def CDL_ASC (*args):
      '''

'''      
    ...

def CDL_NO_CLAMP (*args):
      '''

'''      
    ...

def CDL_TRANSFORM_DEFAULT (*args):
      '''

'''      
    ...

def CHANNEL_ORDERING_ABGR (*args):
      '''

'''      
    ...

def CHANNEL_ORDERING_BGR (*args):
      '''

'''      
    ...

def CHANNEL_ORDERING_BGRA (*args):
      '''

'''      
    ...

def CHANNEL_ORDERING_RGB (*args):
      '''

'''      
    ...

def CHANNEL_ORDERING_RGBA (*args):
      '''

'''      
    ...

def COLORSPACE_ACTIVE (*args):
      '''

'''      
    ...

def COLORSPACE_ALL (*args):
      '''

'''      
    ...

def COLORSPACE_DIR_FROM_REFERENCE (*args):
      '''

'''      
    ...

def COLORSPACE_DIR_TO_REFERENCE (*args):
      '''

'''      
    ...

def COLORSPACE_INACTIVE (*args):
      '''

'''      
    ...

def CPUProcessor (*args):
      '''

'''      
    ...

class CPUProcessor:
    def apply (self, *args, **kwargs):
      '''apply(*args, **kwargs)
Overloaded function.

1. apply(self: PyOpenColorIO.CPUProcessor, imgDesc: PyOpenColorIO.ImageDesc) -> None


Apply to an image with any kind of channel ordering while respecting 
the input and output bit-depths. Image values are modified in place.

.. note::
    The GIL is released during processing, freeing up Python to execute 
    other threads concurrently.

.. note::
    For large images, ``applyRGB`` or ``applyRGBA`` are preferred for 
    processing a NumPy array. The Python ``ImageDesc`` implementation 
    requires copying all values (once) in order to own the underlying 
    pointer. The dedicated packed ``apply*`` methods utilize 
    ``ImageDesc`` on the C++ side so avoid the copy.



2. apply(self: PyOpenColorIO.CPUProcessor, srcImgDesc: PyOpenColorIO.ImageDesc, dstImgDesc: PyOpenColorIO.ImageDesc) -> None


Apply to an image with any kind of channel ordering while respecting 
the input and output bit-depths. Modified srcImgDesc image values are
written to the dstImgDesc image, leaving srcImgDesc unchanged.

.. note::
    The GIL is released during processing, freeing up Python to execute 
    other threads concurrently.

.. note::
    For large images, ``applyRGB`` or ``applyRGBA`` are preferred for 
    processing a NumPy array. The Python ``ImageDesc`` implementation 
    requires copying all values (once) in order to own the underlying 
    pointer. The dedicated packed ``apply*`` methods utilize 
    ``ImageDesc`` on the C++ side so avoid the copy.


'''
    ...
    def applyRGB (self, *args, **kwargs):
      '''applyRGB(*args, **kwargs)
Overloaded function.

1. applyRGB(self: PyOpenColorIO.CPUProcessor, data: buffer) -> None


Apply to a packed RGB array adhering to the Python buffer protocol. 
This will typically be a NumPy array. Input and output bit-depths are
respected but must match. Any array size or shape is supported as long
as the flattened array size is divisible by 3. Array values are 
modified in place.

.. note::
    This differs from the C++ implementation which only applies to a 
    single pixel. This method uses a ``PackedImageDesc`` under the 
    hood to apply to an entire image at once. The GIL is released 
    during processing, freeing up Python to execute other threads 
    concurrently.



2. applyRGB(self: PyOpenColorIO.CPUProcessor, data: List[float]) -> List[float]


Apply to a packed RGB list of float values. Any size is supported as 
long as the list length is divisible by 3. A new list with processed
float values is returned, leaving the input list unchanged.

.. note::
    This differs from the C++ implementation which only applies to a 
    single pixel. This method uses a ``PackedImageDesc`` under the 
    hood to apply to an entire image at once. The GIL is released 
    during processing, freeing up Python to execute other threads 
    concurrently.

.. note::
    For large images, a NumPy array should be preferred over a list.
    List values are copied on input and output, where an array is 
    modified in place.


'''
    ...
    def applyRGBA (self, *args, **kwargs):
      '''applyRGBA(*args, **kwargs)
Overloaded function.

1. applyRGBA(self: PyOpenColorIO.CPUProcessor, data: buffer) -> None


Apply to a packed RGBA array adhering to the Python buffer protocol. 
This will typically be a NumPy array. Input and output bit-depths are
respected but must match. Any array size or shape is supported as long
as the flattened array size is divisible by 4. Array values are 
modified in place.

.. note::
    This differs from the C++ implementation which only applies to a 
    single pixel. This method uses a ``PackedImageDesc`` under the 
    hood to apply to an entire image at once. The GIL is released 
    during processing, freeing up Python to execute other threads 
    concurrently.



2. applyRGBA(self: PyOpenColorIO.CPUProcessor, data: List[float]) -> List[float]


Apply to a packed RGBA list of float values. Any size is supported as 
long as the list length is divisible by 4. A new list with processed
float values is returned, leaving the input list unchanged.

.. note::
    This differs from the C++ implementation which only applies to a 
    single pixel. This method uses a ``PackedImageDesc`` under the 
    hood to apply to an entire image at once. The GIL is released 
    during processing, freeing up Python to execute other threads 
    concurrently.

.. note::
    For large images, a NumPy array should be preferred over a list.
    List values are copied on input and output, where an array is 
    modified in place.


'''
    ...
    def getCacheID (self, *args, **kwargs):
      '''getCacheID(self: PyOpenColorIO.CPUProcessor) -> str
'''
    ...
    def getDynamicProperty (self, *args, **kwargs):
      '''getDynamicProperty(self: PyOpenColorIO.CPUProcessor, type: PyOpenColorIO.DynamicPropertyType) -> PyOpenColorIO.DynamicProperty
'''
    ...
    def getInputBitDepth (self, *args, **kwargs):
      '''getInputBitDepth(self: PyOpenColorIO.CPUProcessor) -> PyOpenColorIO.BitDepth
'''
    ...
    def getOutputBitDepth (self, *args, **kwargs):
      '''getOutputBitDepth(self: PyOpenColorIO.CPUProcessor) -> PyOpenColorIO.BitDepth
'''
    ...
    def hasChannelCrosstalk (self, *args, **kwargs):
      '''hasChannelCrosstalk(self: PyOpenColorIO.CPUProcessor) -> bool
'''
    ...
    def isIdentity (self, *args, **kwargs):
      '''isIdentity(self: PyOpenColorIO.CPUProcessor) -> bool
'''
    ...
    def isNoOp (self, *args, **kwargs):
      '''isNoOp(self: PyOpenColorIO.CPUProcessor) -> bool
'''
    ...

def ChannelOrdering (*args):
      '''

'''      
    ...

class ChannelOrdering:
    def CHANNEL_ORDERING_ABGR (self, *args, **kwargs):
      '''

Members:

  CHANNEL_ORDERING_RGBA : 

  CHANNEL_ORDERING_BGRA : 

  CHANNEL_ORDERING_ABGR : 

  CHANNEL_ORDERING_RGB : 

  CHANNEL_ORDERING_BGR : '''
    ...
    def CHANNEL_ORDERING_BGR (self, *args, **kwargs):
      '''

Members:

  CHANNEL_ORDERING_RGBA : 

  CHANNEL_ORDERING_BGRA : 

  CHANNEL_ORDERING_ABGR : 

  CHANNEL_ORDERING_RGB : 

  CHANNEL_ORDERING_BGR : '''
    ...
    def CHANNEL_ORDERING_BGRA (self, *args, **kwargs):
      '''

Members:

  CHANNEL_ORDERING_RGBA : 

  CHANNEL_ORDERING_BGRA : 

  CHANNEL_ORDERING_ABGR : 

  CHANNEL_ORDERING_RGB : 

  CHANNEL_ORDERING_BGR : '''
    ...
    def CHANNEL_ORDERING_RGB (self, *args, **kwargs):
      '''

Members:

  CHANNEL_ORDERING_RGBA : 

  CHANNEL_ORDERING_BGRA : 

  CHANNEL_ORDERING_ABGR : 

  CHANNEL_ORDERING_RGB : 

  CHANNEL_ORDERING_BGR : '''
    ...
    def CHANNEL_ORDERING_RGBA (self, *args, **kwargs):
      '''

Members:

  CHANNEL_ORDERING_RGBA : 

  CHANNEL_ORDERING_BGRA : 

  CHANNEL_ORDERING_ABGR : 

  CHANNEL_ORDERING_RGB : 

  CHANNEL_ORDERING_BGR : '''
    ...
    def name (self, *args, **kwargs):
      '''name(self: handle) -> str
'''
    ...
    def value (self, *args, **kwargs):
      ''''''
    ...

def ClearAllCaches (*args):
      '''

'''      
    ...

def ColorSpace (*args):
      '''

'''      
    ...

class ColorSpace:
    def ColorSpaceAliasIterator (self, *args, **kwargs):
      '''None'''
    ...
    def ColorSpaceCategoryIterator (self, *args, **kwargs):
      '''None'''
    ...
    def addAlias (self, *args, **kwargs):
      '''addAlias(self: PyOpenColorIO.ColorSpace, alias: str) -> None
'''
    ...
    def addCategory (self, *args, **kwargs):
      '''addCategory(self: PyOpenColorIO.ColorSpace, category: str) -> None
'''
    ...
    def clearAliases (self, *args, **kwargs):
      '''clearAliases(self: PyOpenColorIO.ColorSpace) -> None
'''
    ...
    def clearCategories (self, *args, **kwargs):
      '''clearCategories(self: PyOpenColorIO.ColorSpace) -> None
'''
    ...
    def getAliases (self, *args, **kwargs):
      '''getAliases(self: PyOpenColorIO.ColorSpace) -> PyOpenColorIO.ColorSpace.ColorSpaceAliasIterator
'''
    ...
    def getAllocation (self, *args, **kwargs):
      '''getAllocation(self: PyOpenColorIO.ColorSpace) -> PyOpenColorIO.Allocation
'''
    ...
    def getAllocationVars (self, *args, **kwargs):
      '''getAllocationVars(self: PyOpenColorIO.ColorSpace) -> List[float]
'''
    ...
    def getBitDepth (self, *args, **kwargs):
      '''getBitDepth(self: PyOpenColorIO.ColorSpace) -> PyOpenColorIO.BitDepth
'''
    ...
    def getCategories (self, *args, **kwargs):
      '''getCategories(self: PyOpenColorIO.ColorSpace) -> PyOpenColorIO.ColorSpace.ColorSpaceCategoryIterator
'''
    ...
    def getDescription (self, *args, **kwargs):
      '''getDescription(self: PyOpenColorIO.ColorSpace) -> str
'''
    ...
    def getEncoding (self, *args, **kwargs):
      '''getEncoding(self: PyOpenColorIO.ColorSpace) -> str
'''
    ...
    def getEqualityGroup (self, *args, **kwargs):
      '''getEqualityGroup(self: PyOpenColorIO.ColorSpace) -> str
'''
    ...
    def getFamily (self, *args, **kwargs):
      '''getFamily(self: PyOpenColorIO.ColorSpace) -> str
'''
    ...
    def getName (self, *args, **kwargs):
      '''getName(self: PyOpenColorIO.ColorSpace) -> str
'''
    ...
    def getReferenceSpaceType (self, *args, **kwargs):
      '''getReferenceSpaceType(self: PyOpenColorIO.ColorSpace) -> PyOpenColorIO.ReferenceSpaceType
'''
    ...
    def getTransform (self, *args, **kwargs):
      '''getTransform(self: PyOpenColorIO.ColorSpace, direction: PyOpenColorIO.ColorSpaceDirection) -> PyOpenColorIO.Transform
'''
    ...
    def hasCategory (self, *args, **kwargs):
      '''hasCategory(self: PyOpenColorIO.ColorSpace, category: str) -> bool
'''
    ...
    def isData (self, *args, **kwargs):
      '''isData(self: PyOpenColorIO.ColorSpace) -> bool
'''
    ...
    def removeAlias (self, *args, **kwargs):
      '''removeAlias(self: PyOpenColorIO.ColorSpace, alias: str) -> None
'''
    ...
    def removeCategory (self, *args, **kwargs):
      '''removeCategory(self: PyOpenColorIO.ColorSpace, category: str) -> None
'''
    ...
    def setAllocation (self, *args, **kwargs):
      '''setAllocation(self: PyOpenColorIO.ColorSpace, allocation: PyOpenColorIO.Allocation) -> None
'''
    ...
    def setAllocationVars (self, *args, **kwargs):
      '''setAllocationVars(self: PyOpenColorIO.ColorSpace, vars: List[float]) -> None
'''
    ...
    def setBitDepth (self, *args, **kwargs):
      '''setBitDepth(self: PyOpenColorIO.ColorSpace, bitDepth: PyOpenColorIO.BitDepth) -> None
'''
    ...
    def setDescription (self, *args, **kwargs):
      '''setDescription(self: PyOpenColorIO.ColorSpace, description: str) -> None
'''
    ...
    def setEncoding (self, *args, **kwargs):
      '''setEncoding(self: PyOpenColorIO.ColorSpace, encoding: str) -> None
'''
    ...
    def setEqualityGroup (self, *args, **kwargs):
      '''setEqualityGroup(self: PyOpenColorIO.ColorSpace, equalityGroup: str) -> None
'''
    ...
    def setFamily (self, *args, **kwargs):
      '''setFamily(self: PyOpenColorIO.ColorSpace, family: str) -> None
'''
    ...
    def setIsData (self, *args, **kwargs):
      '''setIsData(self: PyOpenColorIO.ColorSpace, isData: bool) -> None
'''
    ...
    def setName (self, *args, **kwargs):
      '''setName(self: PyOpenColorIO.ColorSpace, name: str) -> None
'''
    ...
    def setTransform (self, *args, **kwargs):
      '''setTransform(self: PyOpenColorIO.ColorSpace, transform: PyOpenColorIO.Transform, direction: PyOpenColorIO.ColorSpaceDirection) -> None
'''
    ...

def ColorSpaceDirection (*args):
      '''

'''      
    ...

class ColorSpaceDirection:
    def COLORSPACE_DIR_FROM_REFERENCE (self, *args, **kwargs):
      '''

Members:

  COLORSPACE_DIR_TO_REFERENCE : 

  COLORSPACE_DIR_FROM_REFERENCE : '''
    ...
    def COLORSPACE_DIR_TO_REFERENCE (self, *args, **kwargs):
      '''

Members:

  COLORSPACE_DIR_TO_REFERENCE : 

  COLORSPACE_DIR_FROM_REFERENCE : '''
    ...
    def name (self, *args, **kwargs):
      '''name(self: handle) -> str
'''
    ...
    def value (self, *args, **kwargs):
      ''''''
    ...

def ColorSpaceHelpers (*args):
      '''

'''      
    ...

def ColorSpaceMenuHelper (*args):
      '''

'''      
    ...

class ColorSpaceMenuHelper:
    def ColorSpaceLevelIterator (self, *args, **kwargs):
      '''None'''
    ...
    def getDescription (self, *args, **kwargs):
      '''getDescription(self: PyOpenColorIO.ColorSpaceMenuHelper, index: int) -> str
'''
    ...
    def getFamily (self, *args, **kwargs):
      '''getFamily(self: PyOpenColorIO.ColorSpaceMenuHelper, index: int) -> str
'''
    ...
    def getHierarchyLevels (self, *args, **kwargs):
      '''getHierarchyLevels(self: PyOpenColorIO.ColorSpaceMenuHelper, index: int) -> PyOpenColorIO.ColorSpaceMenuHelper.ColorSpaceLevelIterator
'''
    ...
    def getIndexFromName (self, *args, **kwargs):
      '''getIndexFromName(self: PyOpenColorIO.ColorSpaceMenuHelper, name: str) -> int
'''
    ...
    def getIndexFromUIName (self, *args, **kwargs):
      '''getIndexFromUIName(self: PyOpenColorIO.ColorSpaceMenuHelper, name: str) -> int
'''
    ...
    def getName (self, *args, **kwargs):
      '''getName(self: PyOpenColorIO.ColorSpaceMenuHelper, index: int) -> str
'''
    ...
    def getNameFromUIName (self, *args, **kwargs):
      '''getNameFromUIName(self: PyOpenColorIO.ColorSpaceMenuHelper, name: str) -> str
'''
    ...
    def getNumColorSpaces (self, *args, **kwargs):
      '''getNumColorSpaces(self: PyOpenColorIO.ColorSpaceMenuHelper) -> int
'''
    ...
    def getUIName (self, *args, **kwargs):
      '''getUIName(self: PyOpenColorIO.ColorSpaceMenuHelper, index: int) -> str
'''
    ...
    def getUINameFromName (self, *args, **kwargs):
      '''getUINameFromName(self: PyOpenColorIO.ColorSpaceMenuHelper, name: str) -> str
'''
    ...

def ColorSpaceMenuParameters (*args):
      '''

'''      
    ...

class ColorSpaceMenuParameters:
    def AddedColorSpaceIterator (self, *args, **kwargs):
      '''None'''
    ...
    def addColorSpace (self, *args, **kwargs):
      '''addColorSpace(self: PyOpenColorIO.ColorSpaceMenuParameters, colorSpace: str) -> None
'''
    ...
    def clearAddedColorSpaces (self, *args, **kwargs):
      '''clearAddedColorSpaces(self: PyOpenColorIO.ColorSpaceMenuParameters) -> None
'''
    ...
    def getAddedColorSpaces (self, *args, **kwargs):
      '''getAddedColorSpaces(self: PyOpenColorIO.ColorSpaceMenuParameters) -> PyOpenColorIO.ColorSpaceMenuParameters.AddedColorSpaceIterator
'''
    ...
    def getAppCategories (self, *args, **kwargs):
      '''getAppCategories(self: PyOpenColorIO.ColorSpaceMenuParameters) -> str
'''
    ...
    def getConfig (self, *args, **kwargs):
      '''getConfig(self: PyOpenColorIO.ColorSpaceMenuParameters) -> PyOpenColorIO.Config
'''
    ...
    def getEncodings (self, *args, **kwargs):
      '''getEncodings(self: PyOpenColorIO.ColorSpaceMenuParameters) -> str
'''
    ...
    def getIncludeColorSpaces (self, *args, **kwargs):
      '''getIncludeColorSpaces(self: PyOpenColorIO.ColorSpaceMenuParameters) -> bool
'''
    ...
    def getIncludeNamedTransforms (self, *args, **kwargs):
      '''getIncludeNamedTransforms(self: PyOpenColorIO.ColorSpaceMenuParameters) -> bool
'''
    ...
    def getIncludeRoles (self, *args, **kwargs):
      '''getIncludeRoles(self: PyOpenColorIO.ColorSpaceMenuParameters) -> bool
'''
    ...
    def getRole (self, *args, **kwargs):
      '''getRole(self: PyOpenColorIO.ColorSpaceMenuParameters) -> str
'''
    ...
    def getSearchReferenceSpaceType (self, *args, **kwargs):
      '''getSearchReferenceSpaceType(self: PyOpenColorIO.ColorSpaceMenuParameters) -> PyOpenColorIO.SearchReferenceSpaceType
'''
    ...
    def getUserCategories (self, *args, **kwargs):
      '''getUserCategories(self: PyOpenColorIO.ColorSpaceMenuParameters) -> str
'''
    ...
    def setAppCategories (self, *args, **kwargs):
      '''setAppCategories(self: PyOpenColorIO.ColorSpaceMenuParameters, appCategories: str) -> None
'''
    ...
    def setConfig (self, *args, **kwargs):
      '''setConfig(self: PyOpenColorIO.ColorSpaceMenuParameters, config: PyOpenColorIO.Config) -> None
'''
    ...
    def setEncodings (self, *args, **kwargs):
      '''setEncodings(self: PyOpenColorIO.ColorSpaceMenuParameters, encodings: str) -> None
'''
    ...
    def setIncludeColorSpaces (self, *args, **kwargs):
      '''setIncludeColorSpaces(self: PyOpenColorIO.ColorSpaceMenuParameters, includeColorSpaces: bool = True) -> None
'''
    ...
    def setIncludeNamedTransforms (self, *args, **kwargs):
      '''setIncludeNamedTransforms(self: PyOpenColorIO.ColorSpaceMenuParameters, includeNamedTransforms: bool = True) -> None
'''
    ...
    def setIncludeRoles (self, *args, **kwargs):
      '''setIncludeRoles(self: PyOpenColorIO.ColorSpaceMenuParameters, includeRoles: bool = True) -> None
'''
    ...
    def setRole (self, *args, **kwargs):
      '''setRole(self: PyOpenColorIO.ColorSpaceMenuParameters, role: str) -> None
'''
    ...
    def setSearchReferenceSpaceType (self, *args, **kwargs):
      '''setSearchReferenceSpaceType(self: PyOpenColorIO.ColorSpaceMenuParameters, searchReferenceSpaceType: PyOpenColorIO.SearchReferenceSpaceType) -> None
'''
    ...
    def setUserCategories (self, *args, **kwargs):
      '''setUserCategories(self: PyOpenColorIO.ColorSpaceMenuParameters, categories: str) -> None
'''
    ...

def ColorSpaceSet (*args):
      '''

'''      
    ...

class ColorSpaceSet:
    def ColorSpaceIterator (self, *args, **kwargs):
      '''None'''
    ...
    def ColorSpaceNameIterator (self, *args, **kwargs):
      '''None'''
    ...
    def addColorSpace (self, *args, **kwargs):
      '''addColorSpace(self: PyOpenColorIO.ColorSpaceSet, colorSpace: PyOpenColorIO.ColorSpace) -> None
'''
    ...
    def addColorSpaces (self, *args, **kwargs):
      '''addColorSpaces(self: PyOpenColorIO.ColorSpaceSet, colorSpaces: PyOpenColorIO.ColorSpaceSet) -> None
'''
    ...
    def clearColorSpaces (self, *args, **kwargs):
      '''clearColorSpaces(self: PyOpenColorIO.ColorSpaceSet) -> None
'''
    ...
    def getColorSpace (self, *args, **kwargs):
      '''getColorSpace(self: PyOpenColorIO.ColorSpaceSet, name: str) -> PyOpenColorIO.ColorSpace
'''
    ...
    def getColorSpaceNames (self, *args, **kwargs):
      '''getColorSpaceNames(self: PyOpenColorIO.ColorSpaceSet) -> PyOpenColorIO.ColorSpaceSet.ColorSpaceNameIterator
'''
    ...
    def getColorSpaces (self, *args, **kwargs):
      '''getColorSpaces(self: PyOpenColorIO.ColorSpaceSet) -> PyOpenColorIO.ColorSpaceSet.ColorSpaceIterator
'''
    ...
    def removeColorSpace (self, *args, **kwargs):
      '''removeColorSpace(self: PyOpenColorIO.ColorSpaceSet, colorSpace: str) -> None
'''
    ...
    def removeColorSpaces (self, *args, **kwargs):
      '''removeColorSpaces(self: PyOpenColorIO.ColorSpaceSet, colorSpaces: PyOpenColorIO.ColorSpaceSet) -> None
'''
    ...

def ColorSpaceTransform (*args):
      '''

'''      
    ...

class ColorSpaceTransform:
    def getDataBypass (self, *args, **kwargs):
      '''getDataBypass(self: PyOpenColorIO.ColorSpaceTransform) -> bool
'''
    ...
    def getDirection (self, *args, **kwargs):
      '''getDirection(self: PyOpenColorIO.Transform) -> PyOpenColorIO.TransformDirection
'''
    ...
    def getDst (self, *args, **kwargs):
      '''getDst(self: PyOpenColorIO.ColorSpaceTransform) -> str
'''
    ...
    def getSrc (self, *args, **kwargs):
      '''getSrc(self: PyOpenColorIO.ColorSpaceTransform) -> str
'''
    ...
    def getTransformType (self, *args, **kwargs):
      '''getTransformType(self: PyOpenColorIO.Transform) -> PyOpenColorIO.TransformType
'''
    ...
    def setDataBypass (self, *args, **kwargs):
      '''setDataBypass(self: PyOpenColorIO.ColorSpaceTransform, dataBypass: bool) -> None
'''
    ...
    def setDirection (self, *args, **kwargs):
      '''setDirection(self: PyOpenColorIO.Transform, direction: PyOpenColorIO.TransformDirection) -> None
'''
    ...
    def setDst (self, *args, **kwargs):
      '''setDst(self: PyOpenColorIO.ColorSpaceTransform, dst: str) -> None
'''
    ...
    def setSrc (self, *args, **kwargs):
      '''setSrc(self: PyOpenColorIO.ColorSpaceTransform, src: str) -> None
'''
    ...
    def validate (self, *args, **kwargs):
      '''validate(self: PyOpenColorIO.Transform) -> None
'''
    ...

def ColorSpaceVisibility (*args):
      '''

'''      
    ...

class ColorSpaceVisibility:
    def COLORSPACE_ACTIVE (self, *args, **kwargs):
      '''

Members:

  COLORSPACE_ACTIVE : 

  COLORSPACE_INACTIVE : 

  COLORSPACE_ALL : '''
    ...
    def COLORSPACE_ALL (self, *args, **kwargs):
      '''

Members:

  COLORSPACE_ACTIVE : 

  COLORSPACE_INACTIVE : 

  COLORSPACE_ALL : '''
    ...
    def COLORSPACE_INACTIVE (self, *args, **kwargs):
      '''

Members:

  COLORSPACE_ACTIVE : 

  COLORSPACE_INACTIVE : 

  COLORSPACE_ALL : '''
    ...
    def name (self, *args, **kwargs):
      '''name(self: handle) -> str
'''
    ...
    def value (self, *args, **kwargs):
      ''''''
    ...

def CombineTransformDirections (*args):
      '''

'''      
    ...

def Config (*args):
      '''

'''      
    ...

class Config:
    def ActiveColorSpaceIterator (self, *args, **kwargs):
      '''None'''
    ...
    def ActiveColorSpaceNameIterator (self, *args, **kwargs):
      '''None'''
    ...
    def ActiveNamedTransformIterator (self, *args, **kwargs):
      '''None'''
    ...
    def ActiveNamedTransformNameIterator (self, *args, **kwargs):
      '''None'''
    ...
    def ColorSpaceIterator (self, *args, **kwargs):
      '''None'''
    ...
    def ColorSpaceNameIterator (self, *args, **kwargs):
      '''None'''
    ...
    def CreateFromBuiltinConfig (self, *args, **kwargs):
      '''CreateFromBuiltinConfig(arg0: str) -> PyOpenColorIO.Config
'''
    ...
    def CreateFromConfigIOProxy (self, *args, **kwargs):
      '''CreateFromConfigIOProxy(arg0: OpenColorIO_v2_2::ConfigIOProxy) -> PyOpenColorIO.Config
'''
    ...
    def CreateFromEnv (self, *args, **kwargs):
      '''CreateFromEnv() -> PyOpenColorIO.Config
'''
    ...
    def CreateFromFile (self, *args, **kwargs):
      '''CreateFromFile(fileName: str) -> PyOpenColorIO.Config
'''
    ...
    def CreateFromStream (self, *args, **kwargs):
      '''CreateFromStream(str: str) -> PyOpenColorIO.Config
'''
    ...
    def CreateRaw (self, *args, **kwargs):
      '''CreateRaw() -> PyOpenColorIO.Config
'''
    ...
    def DisplayAllIterator (self, *args, **kwargs):
      '''None'''
    ...
    def DisplayIterator (self, *args, **kwargs):
      '''None'''
    ...
    def EnvironmentVarNameIterator (self, *args, **kwargs):
      '''None'''
    ...
    def GetProcessorFromBuiltinColorSpace (self, *args, **kwargs):
      '''GetProcessorFromBuiltinColorSpace(builtinColorSpaceName: str, srcConfig: PyOpenColorIO.Config, srcColorSpaceName: str) -> PyOpenColorIO.Processor
'''
    ...
    def GetProcessorFromConfigs (self, *args, **kwargs):
      '''GetProcessorFromConfigs(*args, **kwargs)
Overloaded function.

1. GetProcessorFromConfigs(srcConfig: PyOpenColorIO.Config, srcColorSpaceName: str, dstConfig: PyOpenColorIO.Config, dstColorSpaceName: str) -> PyOpenColorIO.Processor

2. GetProcessorFromConfigs(srcContext: PyOpenColorIO.Context, srcConfig: PyOpenColorIO.Config, srcColorSpaceName: str, dstContext: PyOpenColorIO.Context, dstConfig: PyOpenColorIO.Config, dstColorSpaceName: str) -> PyOpenColorIO.Processor

3. GetProcessorFromConfigs(srcConfig: PyOpenColorIO.Config, srcColorSpaceName: str, srcInterchangeName: str, dstConfig: PyOpenColorIO.Config, dstColorSpaceName: str, dstInterchangeName: str) -> PyOpenColorIO.Processor

4. GetProcessorFromConfigs(srcContext: PyOpenColorIO.Context, srcConfig: PyOpenColorIO.Config, srcColorSpaceName: str, srcInterchangeName: str, dstContext: PyOpenColorIO.Context, dstConfig: PyOpenColorIO.Config, dstColorSpaceName: str, dstInterchangeName: str) -> PyOpenColorIO.Processor
'''
    ...
    def GetProcessorToBuiltinColorSpace (self, *args, **kwargs):
      '''GetProcessorToBuiltinColorSpace(srcConfig: PyOpenColorIO.Config, srcColorSpaceName: str, builtinColorSpaceName: str) -> PyOpenColorIO.Processor
'''
    ...
    def LookIterator (self, *args, **kwargs):
      '''None'''
    ...
    def LookNameIterator (self, *args, **kwargs):
      '''None'''
    ...
    def NamedTransformIterator (self, *args, **kwargs):
      '''None'''
    ...
    def NamedTransformNameIterator (self, *args, **kwargs):
      '''None'''
    ...
    def RoleColorSpaceIterator (self, *args, **kwargs):
      '''None'''
    ...
    def RoleNameIterator (self, *args, **kwargs):
      '''None'''
    ...
    def SearchPathIterator (self, *args, **kwargs):
      '''None'''
    ...
    def SharedViewIterator (self, *args, **kwargs):
      '''None'''
    ...
    def ViewForColorSpaceIterator (self, *args, **kwargs):
      '''None'''
    ...
    def ViewForViewTypeIterator (self, *args, **kwargs):
      '''None'''
    ...
    def ViewIterator (self, *args, **kwargs):
      '''None'''
    ...
    def ViewTransformIterator (self, *args, **kwargs):
      '''None'''
    ...
    def ViewTransformNameIterator (self, *args, **kwargs):
      '''None'''
    ...
    def VirtualViewIterator (self, *args, **kwargs):
      '''None'''
    ...
    def addColorSpace (self, *args, **kwargs):
      '''addColorSpace(self: PyOpenColorIO.Config, colorSpace: PyOpenColorIO.ColorSpace) -> None
'''
    ...
    def addDisplaySharedView (self, *args, **kwargs):
      '''addDisplaySharedView(self: PyOpenColorIO.Config, display: str, view: str) -> None
'''
    ...
    def addDisplayView (self, *args, **kwargs):
      '''addDisplayView(*args, **kwargs)
Overloaded function.

1. addDisplayView(self: PyOpenColorIO.Config, display: str, view: str, colorSpaceName: str, looks: str = '') -> None

2. addDisplayView(self: PyOpenColorIO.Config, display: str, view: str, viewTransform: str, displayColorSpaceName: str, looks: str = '', ruleName: str = '', description: str = '') -> None
'''
    ...
    def addEnvironmentVar (self, *args, **kwargs):
      '''addEnvironmentVar(self: PyOpenColorIO.Config, name: str, defaultValue: str) -> None
'''
    ...
    def addLook (self, *args, **kwargs):
      '''addLook(self: PyOpenColorIO.Config, look: PyOpenColorIO.Look) -> None
'''
    ...
    def addNamedTransform (self, *args, **kwargs):
      '''addNamedTransform(self: PyOpenColorIO.Config, namedTransform: PyOpenColorIO.NamedTransform) -> None
'''
    ...
    def addSearchPath (self, *args, **kwargs):
      '''addSearchPath(self: PyOpenColorIO.Config, path: str) -> None
'''
    ...
    def addSharedView (self, *args, **kwargs):
      '''addSharedView(self: PyOpenColorIO.Config, view: str, viewTransformName: str, colorSpaceName: str, looks: str = '', ruleName: str = '', description: str = '') -> None
'''
    ...
    def addViewTransform (self, *args, **kwargs):
      '''addViewTransform(self: PyOpenColorIO.Config, viewTransform: PyOpenColorIO.ViewTransform) -> None
'''
    ...
    def addVirtualDisplaySharedView (self, *args, **kwargs):
      '''addVirtualDisplaySharedView(self: PyOpenColorIO.Config, sharedView: str) -> None
'''
    ...
    def addVirtualDisplayView (self, *args, **kwargs):
      '''addVirtualDisplayView(self: PyOpenColorIO.Config, view: str, viewTransformName: str, colorSpaceName: str, looks: str = '', ruleName: str = '', description: str = '') -> None
'''
    ...
    def archive (self, *args, **kwargs):
      '''archive(self: PyOpenColorIO.Config, arg0: str) -> None
'''
    ...
    def clearColorSpaces (self, *args, **kwargs):
      '''clearColorSpaces(self: PyOpenColorIO.Config) -> None
'''
    ...
    def clearDisplays (self, *args, **kwargs):
      '''clearDisplays(self: PyOpenColorIO.Config) -> None
'''
    ...
    def clearEnvironmentVars (self, *args, **kwargs):
      '''clearEnvironmentVars(self: PyOpenColorIO.Config) -> None
'''
    ...
    def clearLooks (self, *args, **kwargs):
      '''clearLooks(self: PyOpenColorIO.Config) -> None
'''
    ...
    def clearNamedTransforms (self, *args, **kwargs):
      '''clearNamedTransforms(self: PyOpenColorIO.Config) -> None
'''
    ...
    def clearSearchPaths (self, *args, **kwargs):
      '''clearSearchPaths(self: PyOpenColorIO.Config) -> None
'''
    ...
    def clearViewTransforms (self, *args, **kwargs):
      '''clearViewTransforms(self: PyOpenColorIO.Config) -> None
'''
    ...
    def clearVirtualDisplay (self, *args, **kwargs):
      '''clearVirtualDisplay(self: PyOpenColorIO.Config) -> None
'''
    ...
    def filepathOnlyMatchesDefaultRule (self, *args, **kwargs):
      '''filepathOnlyMatchesDefaultRule(self: PyOpenColorIO.Config, filePath: str) -> bool
'''
    ...
    def getActiveDisplays (self, *args, **kwargs):
      '''getActiveDisplays(self: PyOpenColorIO.Config) -> str
'''
    ...
    def getActiveViews (self, *args, **kwargs):
      '''getActiveViews(self: PyOpenColorIO.Config) -> str
'''
    ...
    def getCacheID (self, *args, **kwargs):
      '''getCacheID(*args, **kwargs)
Overloaded function.

1. getCacheID(self: PyOpenColorIO.Config) -> str

2. getCacheID(self: PyOpenColorIO.Config, context: PyOpenColorIO.Context) -> str
'''
    ...
    def getCanonicalName (self, *args, **kwargs):
      '''getCanonicalName(self: PyOpenColorIO.Config, name: str) -> str
'''
    ...
    def getColorSpace (self, *args, **kwargs):
      '''getColorSpace(self: PyOpenColorIO.Config, name: str) -> PyOpenColorIO.ColorSpace
'''
    ...
    def getColorSpaceFromFilepath (self, *args, **kwargs):
      '''getColorSpaceFromFilepath(self: PyOpenColorIO.Config, filePath: str) -> tuple
'''
    ...
    def getColorSpaceNames (self, *args, **kwargs):
      '''getColorSpaceNames(*args, **kwargs)
Overloaded function.

1. getColorSpaceNames(self: PyOpenColorIO.Config, searchReferenceType: PyOpenColorIO.SearchReferenceSpaceType, visibility: PyOpenColorIO.ColorSpaceVisibility) -> PyOpenColorIO.Config.ColorSpaceNameIterator

2. getColorSpaceNames(self: PyOpenColorIO.Config) -> PyOpenColorIO.Config.ActiveColorSpaceNameIterator
'''
    ...
    def getColorSpaces (self, *args, **kwargs):
      '''getColorSpaces(*args, **kwargs)
Overloaded function.

1. getColorSpaces(self: PyOpenColorIO.Config, category: str) -> PyOpenColorIO.ColorSpaceSet

2. getColorSpaces(self: PyOpenColorIO.Config, searchReferenceType: PyOpenColorIO.SearchReferenceSpaceType, visibility: PyOpenColorIO.ColorSpaceVisibility) -> PyOpenColorIO.Config.ColorSpaceIterator

3. getColorSpaces(self: PyOpenColorIO.Config) -> PyOpenColorIO.Config.ActiveColorSpaceIterator
'''
    ...
    def getCurrentContext (self, *args, **kwargs):
      '''getCurrentContext(self: PyOpenColorIO.Config) -> PyOpenColorIO.Context
'''
    ...
    def getDefaultDisplay (self, *args, **kwargs):
      '''getDefaultDisplay(self: PyOpenColorIO.Config) -> str
'''
    ...
    def getDefaultLumaCoefs (self, *args, **kwargs):
      '''getDefaultLumaCoefs(self: PyOpenColorIO.Config) -> List[float[3]]
'''
    ...
    def getDefaultSceneToDisplayViewTransform (self, *args, **kwargs):
      '''getDefaultSceneToDisplayViewTransform(self: PyOpenColorIO.Config) -> PyOpenColorIO.ViewTransform
'''
    ...
    def getDefaultView (self, *args, **kwargs):
      '''getDefaultView(*args, **kwargs)
Overloaded function.

1. getDefaultView(self: PyOpenColorIO.Config, display: str) -> str

2. getDefaultView(self: PyOpenColorIO.Config, display: str, colorSpacename: str) -> str
'''
    ...
    def getDefaultViewTransformName (self, *args, **kwargs):
      '''getDefaultViewTransformName(self: PyOpenColorIO.Config) -> str
'''
    ...
    def getDescription (self, *args, **kwargs):
      '''getDescription(self: PyOpenColorIO.Config) -> str
'''
    ...
    def getDisplayViewColorSpaceName (self, *args, **kwargs):
      '''getDisplayViewColorSpaceName(self: PyOpenColorIO.Config, display: str, view: str) -> str
'''
    ...
    def getDisplayViewDescription (self, *args, **kwargs):
      '''getDisplayViewDescription(self: PyOpenColorIO.Config, display: str, view: str) -> str
'''
    ...
    def getDisplayViewLooks (self, *args, **kwargs):
      '''getDisplayViewLooks(self: PyOpenColorIO.Config, display: str, view: str) -> str
'''
    ...
    def getDisplayViewRule (self, *args, **kwargs):
      '''getDisplayViewRule(self: PyOpenColorIO.Config, display: str, view: str) -> str
'''
    ...
    def getDisplayViewTransformName (self, *args, **kwargs):
      '''getDisplayViewTransformName(self: PyOpenColorIO.Config, display: str, view: str) -> str
'''
    ...
    def getDisplays (self, *args, **kwargs):
      '''getDisplays(self: PyOpenColorIO.Config) -> PyOpenColorIO.Config.DisplayIterator
'''
    ...
    def getDisplaysAll (self, *args, **kwargs):
      '''getDisplaysAll(self: PyOpenColorIO.Config) -> PyOpenColorIO.Config.DisplayAllIterator
'''
    ...
    def getEnvironmentMode (self, *args, **kwargs):
      '''getEnvironmentMode(self: PyOpenColorIO.Config) -> PyOpenColorIO.EnvironmentMode
'''
    ...
    def getEnvironmentVarDefault (self, *args, **kwargs):
      '''getEnvironmentVarDefault(self: PyOpenColorIO.Config, name: str) -> str
'''
    ...
    def getEnvironmentVarNames (self, *args, **kwargs):
      '''getEnvironmentVarNames(self: PyOpenColorIO.Config) -> PyOpenColorIO.Config.EnvironmentVarNameIterator
'''
    ...
    def getFamilySeparator (self, *args, **kwargs):
      '''getFamilySeparator(self: PyOpenColorIO.Config) -> str
'''
    ...
    def getFileRules (self, *args, **kwargs):
      '''getFileRules(self: PyOpenColorIO.Config) -> PyOpenColorIO.FileRules
'''
    ...
    def getInactiveColorSpaces (self, *args, **kwargs):
      '''getInactiveColorSpaces(self: PyOpenColorIO.Config) -> str
'''
    ...
    def getLook (self, *args, **kwargs):
      '''getLook(self: PyOpenColorIO.Config, name: str) -> PyOpenColorIO.Look
'''
    ...
    def getLookNames (self, *args, **kwargs):
      '''getLookNames(self: PyOpenColorIO.Config) -> PyOpenColorIO.Config.LookNameIterator
'''
    ...
    def getLooks (self, *args, **kwargs):
      '''getLooks(self: PyOpenColorIO.Config) -> PyOpenColorIO.Config.LookIterator
'''
    ...
    def getMajorVersion (self, *args, **kwargs):
      '''getMajorVersion(self: PyOpenColorIO.Config) -> int
'''
    ...
    def getMinorVersion (self, *args, **kwargs):
      '''getMinorVersion(self: PyOpenColorIO.Config) -> int
'''
    ...
    def getName (self, *args, **kwargs):
      '''getName(self: PyOpenColorIO.Config) -> str
'''
    ...
    def getNamedTransform (self, *args, **kwargs):
      '''getNamedTransform(self: PyOpenColorIO.Config, name: str) -> PyOpenColorIO.NamedTransform
'''
    ...
    def getNamedTransformNames (self, *args, **kwargs):
      '''getNamedTransformNames(*args, **kwargs)
Overloaded function.

1. getNamedTransformNames(self: PyOpenColorIO.Config, visibility: PyOpenColorIO.NamedTransformVisibility) -> PyOpenColorIO.Config.NamedTransformNameIterator

2. getNamedTransformNames(self: PyOpenColorIO.Config) -> PyOpenColorIO.Config.ActiveNamedTransformNameIterator
'''
    ...
    def getNamedTransforms (self, *args, **kwargs):
      '''getNamedTransforms(*args, **kwargs)
Overloaded function.

1. getNamedTransforms(self: PyOpenColorIO.Config, visibility: PyOpenColorIO.NamedTransformVisibility) -> PyOpenColorIO.Config.NamedTransformIterator

2. getNamedTransforms(self: PyOpenColorIO.Config) -> PyOpenColorIO.Config.ActiveNamedTransformIterator
'''
    ...
    def getProcessor (self, *args, **kwargs):
      '''getProcessor(*args, **kwargs)
Overloaded function.

1. getProcessor(self: PyOpenColorIO.Config, srcColorSpace: PyOpenColorIO.ColorSpace, dstColorSpace: PyOpenColorIO.ColorSpace) -> PyOpenColorIO.Processor

2. getProcessor(self: PyOpenColorIO.Config, context: PyOpenColorIO.Context, srcColorSpace: PyOpenColorIO.ColorSpace, dstColorSpace: PyOpenColorIO.ColorSpace) -> PyOpenColorIO.Processor

3. getProcessor(self: PyOpenColorIO.Config, srcColorSpaceName: str, dstColorSpaceName: str) -> PyOpenColorIO.Processor

4. getProcessor(self: PyOpenColorIO.Config, context: PyOpenColorIO.Context, srcColorSpaceName: str, dstColorSpaceName: str) -> PyOpenColorIO.Processor

5. getProcessor(self: PyOpenColorIO.Config, srcColorSpaceName: str, display: str, view: str, direction: PyOpenColorIO.TransformDirection) -> PyOpenColorIO.Processor

6. getProcessor(self: PyOpenColorIO.Config, context: PyOpenColorIO.Context, srcColorSpaceName: str, display: str, view: str, direction: PyOpenColorIO.TransformDirection) -> PyOpenColorIO.Processor

7. getProcessor(self: PyOpenColorIO.Config, namedTransform: PyOpenColorIO.NamedTransform, direction: PyOpenColorIO.TransformDirection) -> PyOpenColorIO.Processor

8. getProcessor(self: PyOpenColorIO.Config, context: PyOpenColorIO.Context, namedTransform: PyOpenColorIO.NamedTransform, direction: PyOpenColorIO.TransformDirection) -> PyOpenColorIO.Processor

9. getProcessor(self: PyOpenColorIO.Config, namedTransformName: str, direction: PyOpenColorIO.TransformDirection) -> PyOpenColorIO.Processor

10. getProcessor(self: PyOpenColorIO.Config, context: PyOpenColorIO.Context, namedTransformName: str, direction: PyOpenColorIO.TransformDirection) -> PyOpenColorIO.Processor

11. getProcessor(self: PyOpenColorIO.Config, transform: PyOpenColorIO.Transform) -> PyOpenColorIO.Processor

12. getProcessor(self: PyOpenColorIO.Config, transform: PyOpenColorIO.Transform, direction: PyOpenColorIO.TransformDirection) -> PyOpenColorIO.Processor

13. getProcessor(self: PyOpenColorIO.Config, context: PyOpenColorIO.Context, transform: PyOpenColorIO.Transform, direction: PyOpenColorIO.TransformDirection) -> PyOpenColorIO.Processor
'''
    ...
    def getRoleNames (self, *args, **kwargs):
      '''getRoleNames(self: PyOpenColorIO.Config) -> PyOpenColorIO.Config.RoleNameIterator
'''
    ...
    def getRoles (self, *args, **kwargs):
      '''getRoles(self: PyOpenColorIO.Config) -> PyOpenColorIO.Config.RoleColorSpaceIterator
'''
    ...
    def getSearchPath (self, *args, **kwargs):
      '''getSearchPath(self: PyOpenColorIO.Config) -> str
'''
    ...
    def getSearchPaths (self, *args, **kwargs):
      '''getSearchPaths(self: PyOpenColorIO.Config) -> PyOpenColorIO.Config.SearchPathIterator
'''
    ...
    def getSharedViews (self, *args, **kwargs):
      '''getSharedViews(self: PyOpenColorIO.Config) -> PyOpenColorIO.Config.SharedViewIterator
'''
    ...
    def getViewTransform (self, *args, **kwargs):
      '''getViewTransform(self: PyOpenColorIO.Config, name: str) -> PyOpenColorIO.ViewTransform
'''
    ...
    def getViewTransformNames (self, *args, **kwargs):
      '''getViewTransformNames(self: PyOpenColorIO.Config) -> PyOpenColorIO.Config.ViewTransformNameIterator
'''
    ...
    def getViewTransforms (self, *args, **kwargs):
      '''getViewTransforms(self: PyOpenColorIO.Config) -> PyOpenColorIO.Config.ViewTransformIterator
'''
    ...
    def getViewingRules (self, *args, **kwargs):
      '''getViewingRules(self: PyOpenColorIO.Config) -> PyOpenColorIO.ViewingRules
'''
    ...
    def getViews (self, *args, **kwargs):
      '''getViews(*args, **kwargs)
Overloaded function.

1. getViews(self: PyOpenColorIO.Config, display: str) -> PyOpenColorIO.Config.ViewIterator

2. getViews(self: PyOpenColorIO.Config, type: PyOpenColorIO.ViewType, display: str) -> PyOpenColorIO.Config.ViewForViewTypeIterator

3. getViews(self: PyOpenColorIO.Config, display: str, colorSpaceName: str) -> PyOpenColorIO.Config.ViewForColorSpaceIterator
'''
    ...
    def getVirtualDisplayViewColorSpaceName (self, *args, **kwargs):
      '''getVirtualDisplayViewColorSpaceName(self: PyOpenColorIO.Config, view: str) -> str
'''
    ...
    def getVirtualDisplayViewDescription (self, *args, **kwargs):
      '''getVirtualDisplayViewDescription(self: PyOpenColorIO.Config, view: str) -> str
'''
    ...
    def getVirtualDisplayViewLooks (self, *args, **kwargs):
      '''getVirtualDisplayViewLooks(self: PyOpenColorIO.Config, view: str) -> str
'''
    ...
    def getVirtualDisplayViewRule (self, *args, **kwargs):
      '''getVirtualDisplayViewRule(self: PyOpenColorIO.Config, view: str) -> str
'''
    ...
    def getVirtualDisplayViewTransformName (self, *args, **kwargs):
      '''getVirtualDisplayViewTransformName(self: PyOpenColorIO.Config, view: str) -> str
'''
    ...
    def getVirtualDisplayViews (self, *args, **kwargs):
      '''getVirtualDisplayViews(self: PyOpenColorIO.Config, display: PyOpenColorIO.ViewType) -> PyOpenColorIO.Config.VirtualViewIterator
'''
    ...
    def getWorkingDir (self, *args, **kwargs):
      '''getWorkingDir(self: PyOpenColorIO.Config) -> str
'''
    ...
    def hasRole (self, *args, **kwargs):
      '''hasRole(self: PyOpenColorIO.Config, role: str) -> bool
'''
    ...
    def instantiateDisplayFromICCProfile (self, *args, **kwargs):
      '''instantiateDisplayFromICCProfile(self: PyOpenColorIO.Config, ICCProfileFilepath: str) -> int
'''
    ...
    def instantiateDisplayFromMonitorName (self, *args, **kwargs):
      '''instantiateDisplayFromMonitorName(self: PyOpenColorIO.Config, monitorName: str) -> int
'''
    ...
    def isArchivable (self, *args, **kwargs):
      '''isArchivable(self: PyOpenColorIO.Config) -> bool
'''
    ...
    def isColorSpaceLinear (self, *args, **kwargs):
      '''isColorSpaceLinear(self: PyOpenColorIO.Config, colorSpace: str, referenceSpaceType: PyOpenColorIO.ReferenceSpaceType) -> bool
'''
    ...
    def isColorSpaceUsed (self, *args, **kwargs):
      '''isColorSpaceUsed(self: PyOpenColorIO.Config, name: str) -> bool
'''
    ...
    def isDisplayTemporary (self, *args, **kwargs):
      '''isDisplayTemporary(self: PyOpenColorIO.Config, display: str) -> bool
'''
    ...
    def isStrictParsingEnabled (self, *args, **kwargs):
      '''isStrictParsingEnabled(self: PyOpenColorIO.Config) -> bool
'''
    ...
    def loadEnvironment (self, *args, **kwargs):
      '''loadEnvironment(self: PyOpenColorIO.Config) -> None
'''
    ...
    def parseColorSpaceFromString (self, *args, **kwargs):
      '''parseColorSpaceFromString(self: PyOpenColorIO.Config, str: str) -> str
'''
    ...
    def removeColorSpace (self, *args, **kwargs):
      '''removeColorSpace(self: PyOpenColorIO.Config, name: str) -> None
'''
    ...
    def removeDisplayView (self, *args, **kwargs):
      '''removeDisplayView(self: PyOpenColorIO.Config, display: str, view: str) -> None
'''
    ...
    def removeSharedView (self, *args, **kwargs):
      '''removeSharedView(self: PyOpenColorIO.Config, view: str) -> None
'''
    ...
    def removeVirtualDisplayView (self, *args, **kwargs):
      '''removeVirtualDisplayView(self: PyOpenColorIO.Config, view: str) -> None
'''
    ...
    def serialize (self, *args, **kwargs):
      '''serialize(*args, **kwargs)
Overloaded function.

1. serialize(self: PyOpenColorIO.Config, fileName: str) -> None

2. serialize(self: PyOpenColorIO.Config) -> str
'''
    ...
    def setActiveDisplays (self, *args, **kwargs):
      '''setActiveDisplays(self: PyOpenColorIO.Config, displays: str) -> None
'''
    ...
    def setActiveViews (self, *args, **kwargs):
      '''setActiveViews(self: PyOpenColorIO.Config, views: str) -> None
'''
    ...
    def setDefaultLumaCoefs (self, *args, **kwargs):
      '''setDefaultLumaCoefs(self: PyOpenColorIO.Config, rgb: List[float[3]]) -> None
'''
    ...
    def setDefaultViewTransformName (self, *args, **kwargs):
      '''setDefaultViewTransformName(self: PyOpenColorIO.Config, name: str) -> None
'''
    ...
    def setDescription (self, *args, **kwargs):
      '''setDescription(self: PyOpenColorIO.Config, description: str) -> None
'''
    ...
    def setEnvironmentMode (self, *args, **kwargs):
      '''setEnvironmentMode(self: PyOpenColorIO.Config, mode: PyOpenColorIO.EnvironmentMode) -> None
'''
    ...
    def setFamilySeparator (self, *args, **kwargs):
      '''setFamilySeparator(self: PyOpenColorIO.Config, separator: str) -> None
'''
    ...
    def setFileRules (self, *args, **kwargs):
      '''setFileRules(self: PyOpenColorIO.Config, fileRules: PyOpenColorIO.FileRules) -> None
'''
    ...
    def setInactiveColorSpaces (self, *args, **kwargs):
      '''setInactiveColorSpaces(self: PyOpenColorIO.Config, inactiveColorSpaces: str) -> None
'''
    ...
    def setMajorVersion (self, *args, **kwargs):
      '''setMajorVersion(self: PyOpenColorIO.Config, major: int) -> None
'''
    ...
    def setMinorVersion (self, *args, **kwargs):
      '''setMinorVersion(self: PyOpenColorIO.Config, minor: int) -> None
'''
    ...
    def setName (self, *args, **kwargs):
      '''setName(self: PyOpenColorIO.Config, name: str) -> None
'''
    ...
    def setProcessorCacheFlags (self, *args, **kwargs):
      '''setProcessorCacheFlags(self: PyOpenColorIO.Config, flags: PyOpenColorIO.ProcessorCacheFlags) -> None
'''
    ...
    def setRole (self, *args, **kwargs):
      '''setRole(self: PyOpenColorIO.Config, role: str, colorSpaceName: str) -> None
'''
    ...
    def setSearchPath (self, *args, **kwargs):
      '''setSearchPath(self: PyOpenColorIO.Config, path: str) -> None
'''
    ...
    def setStrictParsingEnabled (self, *args, **kwargs):
      '''setStrictParsingEnabled(self: PyOpenColorIO.Config, enabled: bool) -> None
'''
    ...
    def setVersion (self, *args, **kwargs):
      '''setVersion(self: PyOpenColorIO.Config, major: int, minor: int) -> None
'''
    ...
    def setViewingRules (self, *args, **kwargs):
      '''setViewingRules(self: PyOpenColorIO.Config, ViewingRules: PyOpenColorIO.ViewingRules) -> None
'''
    ...
    def setWorkingDir (self, *args, **kwargs):
      '''setWorkingDir(self: PyOpenColorIO.Config, dirName: str) -> None
'''
    ...
    def upgradeToLatestVersion (self, *args, **kwargs):
      '''upgradeToLatestVersion(self: PyOpenColorIO.Config) -> None
'''
    ...
    def validate (self, *args, **kwargs):
      '''validate(self: PyOpenColorIO.Config) -> None
'''
    ...

def Context (*args):
      '''

'''      
    ...

class Context:
    def SearchPathIterator (self, *args, **kwargs):
      '''None'''
    ...
    def StringVarIterator (self, *args, **kwargs):
      '''None'''
    ...
    def StringVarNameIterator (self, *args, **kwargs):
      '''None'''
    ...
    def addSearchPath (self, *args, **kwargs):
      '''addSearchPath(self: PyOpenColorIO.Context, path: str) -> None
'''
    ...
    def clearSearchPaths (self, *args, **kwargs):
      '''clearSearchPaths(self: PyOpenColorIO.Context) -> None
'''
    ...
    def clearStringVars (self, *args, **kwargs):
      '''clearStringVars(self: PyOpenColorIO.Context) -> None
'''
    ...
    def getCacheID (self, *args, **kwargs):
      '''getCacheID(self: PyOpenColorIO.Context) -> str
'''
    ...
    def getEnvironmentMode (self, *args, **kwargs):
      '''getEnvironmentMode(self: PyOpenColorIO.Context) -> PyOpenColorIO.EnvironmentMode
'''
    ...
    def getSearchPath (self, *args, **kwargs):
      '''getSearchPath(self: PyOpenColorIO.Context) -> str
'''
    ...
    def getSearchPaths (self, *args, **kwargs):
      '''getSearchPaths(self: PyOpenColorIO.Context) -> PyOpenColorIO.Context.SearchPathIterator
'''
    ...
    def getStringVars (self, *args, **kwargs):
      '''getStringVars(self: PyOpenColorIO.Context) -> PyOpenColorIO.Context.StringVarIterator
'''
    ...
    def getWorkingDir (self, *args, **kwargs):
      '''getWorkingDir(self: PyOpenColorIO.Context) -> str
'''
    ...
    def loadEnvironment (self, *args, **kwargs):
      '''loadEnvironment(self: PyOpenColorIO.Context) -> None
'''
    ...
    def resolveFileLocation (self, *args, **kwargs):
      '''resolveFileLocation(*args, **kwargs)
Overloaded function.

1. resolveFileLocation(self: PyOpenColorIO.Context, filename: str) -> str

2. resolveFileLocation(self: PyOpenColorIO.Context, filename: str, usedContextVars: PyOpenColorIO.Context) -> str
'''
    ...
    def resolveStringVar (self, *args, **kwargs):
      '''resolveStringVar(*args, **kwargs)
Overloaded function.

1. resolveStringVar(self: PyOpenColorIO.Context, string: str) -> str

2. resolveStringVar(self: PyOpenColorIO.Context, string: str, usedContextVars: PyOpenColorIO.Context) -> str
'''
    ...
    def setEnvironmentMode (self, *args, **kwargs):
      '''setEnvironmentMode(self: PyOpenColorIO.Context, mode: PyOpenColorIO.EnvironmentMode) -> None
'''
    ...
    def setSearchPath (self, *args, **kwargs):
      '''setSearchPath(self: PyOpenColorIO.Context, path: str) -> None
'''
    ...
    def setWorkingDir (self, *args, **kwargs):
      '''setWorkingDir(self: PyOpenColorIO.Context, dirName: str) -> None
'''
    ...

def DEFAULT_RULE_NAME (*args):
      '''

'''      
    ...

def DYNAMIC_PROPERTY_CONTRAST (*args):
      '''

'''      
    ...

def DYNAMIC_PROPERTY_EXPOSURE (*args):
      '''

'''      
    ...

def DYNAMIC_PROPERTY_GAMMA (*args):
      '''

'''      
    ...

def DYNAMIC_PROPERTY_GRADING_PRIMARY (*args):
      '''

'''      
    ...

def DYNAMIC_PROPERTY_GRADING_RGBCURVE (*args):
      '''

'''      
    ...

def DYNAMIC_PROPERTY_GRADING_TONE (*args):
      '''

'''      
    ...

def DisplayViewHelpers (*args):
      '''

'''      
    ...

def DisplayViewTransform (*args):
      '''

'''      
    ...

class DisplayViewTransform:
    def getDataBypass (self, *args, **kwargs):
      '''getDataBypass(self: PyOpenColorIO.DisplayViewTransform) -> bool
'''
    ...
    def getDirection (self, *args, **kwargs):
      '''getDirection(self: PyOpenColorIO.Transform) -> PyOpenColorIO.TransformDirection
'''
    ...
    def getDisplay (self, *args, **kwargs):
      '''getDisplay(self: PyOpenColorIO.DisplayViewTransform) -> str
'''
    ...
    def getLooksBypass (self, *args, **kwargs):
      '''getLooksBypass(self: PyOpenColorIO.DisplayViewTransform) -> bool
'''
    ...
    def getSrc (self, *args, **kwargs):
      '''getSrc(self: PyOpenColorIO.DisplayViewTransform) -> str
'''
    ...
    def getTransformType (self, *args, **kwargs):
      '''getTransformType(self: PyOpenColorIO.Transform) -> PyOpenColorIO.TransformType
'''
    ...
    def getView (self, *args, **kwargs):
      '''getView(self: PyOpenColorIO.DisplayViewTransform) -> str
'''
    ...
    def setDataBypass (self, *args, **kwargs):
      '''setDataBypass(self: PyOpenColorIO.DisplayViewTransform, dataBypass: bool) -> None
'''
    ...
    def setDirection (self, *args, **kwargs):
      '''setDirection(self: PyOpenColorIO.Transform, direction: PyOpenColorIO.TransformDirection) -> None
'''
    ...
    def setDisplay (self, *args, **kwargs):
      '''setDisplay(self: PyOpenColorIO.DisplayViewTransform, display: str) -> None
'''
    ...
    def setLooksBypass (self, *args, **kwargs):
      '''setLooksBypass(self: PyOpenColorIO.DisplayViewTransform, looksBypass: bool) -> None
'''
    ...
    def setSrc (self, *args, **kwargs):
      '''setSrc(self: PyOpenColorIO.DisplayViewTransform, src: str) -> None
'''
    ...
    def setView (self, *args, **kwargs):
      '''setView(self: PyOpenColorIO.DisplayViewTransform, view: str) -> None
'''
    ...
    def validate (self, *args, **kwargs):
      '''validate(self: PyOpenColorIO.Transform) -> None
'''
    ...

def DynamicProperty (*args):
      '''

'''      
    ...

class DynamicProperty:
    def getDouble (self, *args, **kwargs):
      '''getDouble(self: PyOpenColorIO.DynamicProperty) -> float
'''
    ...
    def getGradingPrimary (self, *args, **kwargs):
      '''getGradingPrimary(self: PyOpenColorIO.DynamicProperty) -> PyOpenColorIO.GradingPrimary
'''
    ...
    def getGradingRGBCurve (self, *args, **kwargs):
      '''getGradingRGBCurve(self: PyOpenColorIO.DynamicProperty) -> PyOpenColorIO.GradingRGBCurve
'''
    ...
    def getGradingTone (self, *args, **kwargs):
      '''getGradingTone(self: PyOpenColorIO.DynamicProperty) -> PyOpenColorIO.GradingTone
'''
    ...
    def getType (self, *args, **kwargs):
      '''getType(self: PyOpenColorIO.DynamicProperty) -> PyOpenColorIO.DynamicPropertyType
'''
    ...
    def setDouble (self, *args, **kwargs):
      '''setDouble(self: PyOpenColorIO.DynamicProperty, val: float) -> None
'''
    ...
    def setGradingPrimary (self, *args, **kwargs):
      '''setGradingPrimary(self: PyOpenColorIO.DynamicProperty, val: PyOpenColorIO.GradingPrimary) -> None
'''
    ...
    def setGradingRGBCurve (self, *args, **kwargs):
      '''setGradingRGBCurve(self: PyOpenColorIO.DynamicProperty, val: PyOpenColorIO.GradingRGBCurve) -> None
'''
    ...
    def setGradingTone (self, *args, **kwargs):
      '''setGradingTone(self: PyOpenColorIO.DynamicProperty, val: PyOpenColorIO.GradingTone) -> None
'''
    ...

def DynamicPropertyType (*args):
      '''

'''      
    ...

class DynamicPropertyType:
    def DYNAMIC_PROPERTY_CONTRAST (self, *args, **kwargs):
      '''

Members:

  DYNAMIC_PROPERTY_EXPOSURE : 

  DYNAMIC_PROPERTY_CONTRAST : 

  DYNAMIC_PROPERTY_GAMMA : 

  DYNAMIC_PROPERTY_GRADING_PRIMARY : 

  DYNAMIC_PROPERTY_GRADING_RGBCURVE : 

  DYNAMIC_PROPERTY_GRADING_TONE : '''
    ...
    def DYNAMIC_PROPERTY_EXPOSURE (self, *args, **kwargs):
      '''

Members:

  DYNAMIC_PROPERTY_EXPOSURE : 

  DYNAMIC_PROPERTY_CONTRAST : 

  DYNAMIC_PROPERTY_GAMMA : 

  DYNAMIC_PROPERTY_GRADING_PRIMARY : 

  DYNAMIC_PROPERTY_GRADING_RGBCURVE : 

  DYNAMIC_PROPERTY_GRADING_TONE : '''
    ...
    def DYNAMIC_PROPERTY_GAMMA (self, *args, **kwargs):
      '''

Members:

  DYNAMIC_PROPERTY_EXPOSURE : 

  DYNAMIC_PROPERTY_CONTRAST : 

  DYNAMIC_PROPERTY_GAMMA : 

  DYNAMIC_PROPERTY_GRADING_PRIMARY : 

  DYNAMIC_PROPERTY_GRADING_RGBCURVE : 

  DYNAMIC_PROPERTY_GRADING_TONE : '''
    ...
    def DYNAMIC_PROPERTY_GRADING_PRIMARY (self, *args, **kwargs):
      '''

Members:

  DYNAMIC_PROPERTY_EXPOSURE : 

  DYNAMIC_PROPERTY_CONTRAST : 

  DYNAMIC_PROPERTY_GAMMA : 

  DYNAMIC_PROPERTY_GRADING_PRIMARY : 

  DYNAMIC_PROPERTY_GRADING_RGBCURVE : 

  DYNAMIC_PROPERTY_GRADING_TONE : '''
    ...
    def DYNAMIC_PROPERTY_GRADING_RGBCURVE (self, *args, **kwargs):
      '''

Members:

  DYNAMIC_PROPERTY_EXPOSURE : 

  DYNAMIC_PROPERTY_CONTRAST : 

  DYNAMIC_PROPERTY_GAMMA : 

  DYNAMIC_PROPERTY_GRADING_PRIMARY : 

  DYNAMIC_PROPERTY_GRADING_RGBCURVE : 

  DYNAMIC_PROPERTY_GRADING_TONE : '''
    ...
    def DYNAMIC_PROPERTY_GRADING_TONE (self, *args, **kwargs):
      '''

Members:

  DYNAMIC_PROPERTY_EXPOSURE : 

  DYNAMIC_PROPERTY_CONTRAST : 

  DYNAMIC_PROPERTY_GAMMA : 

  DYNAMIC_PROPERTY_GRADING_PRIMARY : 

  DYNAMIC_PROPERTY_GRADING_RGBCURVE : 

  DYNAMIC_PROPERTY_GRADING_TONE : '''
    ...
    def name (self, *args, **kwargs):
      '''name(self: handle) -> str
'''
    ...
    def value (self, *args, **kwargs):
      ''''''
    ...

def ENV_ENVIRONMENT_LOAD_ALL (*args):
      '''

'''      
    ...

def ENV_ENVIRONMENT_LOAD_PREDEFINED (*args):
      '''

'''      
    ...

def ENV_ENVIRONMENT_UNKNOWN (*args):
      '''

'''      
    ...

def EXPOSURE_CONTRAST_LINEAR (*args):
      '''

'''      
    ...

def EXPOSURE_CONTRAST_LOGARITHMIC (*args):
      '''

'''      
    ...

def EXPOSURE_CONTRAST_VIDEO (*args):
      '''

'''      
    ...

def EnvironmentMode (*args):
      '''

'''      
    ...

class EnvironmentMode:
    def ENV_ENVIRONMENT_LOAD_ALL (self, *args, **kwargs):
      '''

Members:

  ENV_ENVIRONMENT_UNKNOWN : 

  ENV_ENVIRONMENT_LOAD_PREDEFINED : 

  ENV_ENVIRONMENT_LOAD_ALL : '''
    ...
    def ENV_ENVIRONMENT_LOAD_PREDEFINED (self, *args, **kwargs):
      '''

Members:

  ENV_ENVIRONMENT_UNKNOWN : 

  ENV_ENVIRONMENT_LOAD_PREDEFINED : 

  ENV_ENVIRONMENT_LOAD_ALL : '''
    ...
    def ENV_ENVIRONMENT_UNKNOWN (self, *args, **kwargs):
      '''

Members:

  ENV_ENVIRONMENT_UNKNOWN : 

  ENV_ENVIRONMENT_LOAD_PREDEFINED : 

  ENV_ENVIRONMENT_LOAD_ALL : '''
    ...
    def name (self, *args, **kwargs):
      '''name(self: handle) -> str
'''
    ...
    def value (self, *args, **kwargs):
      ''''''
    ...

def EnvironmentModeFromString (*args):
      '''

'''      
    ...

def EnvironmentModeToString (*args):
      '''

'''      
    ...

def Exception (*args):
      '''

'''      
    ...

class Exception:
    def args (self, *args, **kwargs):
      '''None'''
    ...
    def with_traceback (self, *args, **kwargs):
      '''Exception.with_traceback(tb) --
    set self.__traceback__ to tb and return self.'''
    ...

def ExceptionMissingFile (*args):
      '''

'''      
    ...

class ExceptionMissingFile:
    def args (self, *args, **kwargs):
      '''None'''
    ...
    def with_traceback (self, *args, **kwargs):
      '''Exception.with_traceback(tb) --
    set self.__traceback__ to tb and return self.'''
    ...

def ExponentTransform (*args):
      '''

'''      
    ...

class ExponentTransform:
    def equals (self, *args, **kwargs):
      '''equals(self: PyOpenColorIO.ExponentTransform, other: PyOpenColorIO.ExponentTransform) -> bool
'''
    ...
    def getDirection (self, *args, **kwargs):
      '''getDirection(self: PyOpenColorIO.Transform) -> PyOpenColorIO.TransformDirection
'''
    ...
    def getFormatMetadata (self, *args, **kwargs):
      '''getFormatMetadata(self: PyOpenColorIO.ExponentTransform) -> PyOpenColorIO.FormatMetadata
'''
    ...
    def getNegativeStyle (self, *args, **kwargs):
      '''getNegativeStyle(self: PyOpenColorIO.ExponentTransform) -> PyOpenColorIO.NegativeStyle
'''
    ...
    def getTransformType (self, *args, **kwargs):
      '''getTransformType(self: PyOpenColorIO.Transform) -> PyOpenColorIO.TransformType
'''
    ...
    def getValue (self, *args, **kwargs):
      '''getValue(self: PyOpenColorIO.ExponentTransform) -> List[float[4]]
'''
    ...
    def setDirection (self, *args, **kwargs):
      '''setDirection(self: PyOpenColorIO.Transform, direction: PyOpenColorIO.TransformDirection) -> None
'''
    ...
    def setNegativeStyle (self, *args, **kwargs):
      '''setNegativeStyle(self: PyOpenColorIO.ExponentTransform, style: PyOpenColorIO.NegativeStyle) -> None
'''
    ...
    def setValue (self, *args, **kwargs):
      '''setValue(self: PyOpenColorIO.ExponentTransform, value: List[float[4]]) -> None
'''
    ...
    def validate (self, *args, **kwargs):
      '''validate(self: PyOpenColorIO.Transform) -> None
'''
    ...

def ExponentWithLinearTransform (*args):
      '''

'''      
    ...

class ExponentWithLinearTransform:
    def equals (self, *args, **kwargs):
      '''equals(self: PyOpenColorIO.ExponentWithLinearTransform, other: PyOpenColorIO.ExponentWithLinearTransform) -> bool
'''
    ...
    def getDirection (self, *args, **kwargs):
      '''getDirection(self: PyOpenColorIO.Transform) -> PyOpenColorIO.TransformDirection
'''
    ...
    def getFormatMetadata (self, *args, **kwargs):
      '''getFormatMetadata(self: PyOpenColorIO.ExponentWithLinearTransform) -> PyOpenColorIO.FormatMetadata
'''
    ...
    def getGamma (self, *args, **kwargs):
      '''getGamma(self: PyOpenColorIO.ExponentWithLinearTransform) -> List[float[4]]
'''
    ...
    def getNegativeStyle (self, *args, **kwargs):
      '''getNegativeStyle(self: PyOpenColorIO.ExponentWithLinearTransform) -> PyOpenColorIO.NegativeStyle
'''
    ...
    def getOffset (self, *args, **kwargs):
      '''getOffset(self: PyOpenColorIO.ExponentWithLinearTransform) -> List[float[4]]
'''
    ...
    def getTransformType (self, *args, **kwargs):
      '''getTransformType(self: PyOpenColorIO.Transform) -> PyOpenColorIO.TransformType
'''
    ...
    def setDirection (self, *args, **kwargs):
      '''setDirection(self: PyOpenColorIO.Transform, direction: PyOpenColorIO.TransformDirection) -> None
'''
    ...
    def setGamma (self, *args, **kwargs):
      '''setGamma(self: PyOpenColorIO.ExponentWithLinearTransform, values: List[float[4]]) -> None
'''
    ...
    def setNegativeStyle (self, *args, **kwargs):
      '''setNegativeStyle(self: PyOpenColorIO.ExponentWithLinearTransform, style: PyOpenColorIO.NegativeStyle) -> None
'''
    ...
    def setOffset (self, *args, **kwargs):
      '''setOffset(self: PyOpenColorIO.ExponentWithLinearTransform, values: List[float[4]]) -> None
'''
    ...
    def validate (self, *args, **kwargs):
      '''validate(self: PyOpenColorIO.Transform) -> None
'''
    ...

def ExposureContrastStyle (*args):
      '''

'''      
    ...

class ExposureContrastStyle:
    def EXPOSURE_CONTRAST_LINEAR (self, *args, **kwargs):
      '''

Members:

  EXPOSURE_CONTRAST_LINEAR : 

  EXPOSURE_CONTRAST_VIDEO : 

  EXPOSURE_CONTRAST_LOGARITHMIC : '''
    ...
    def EXPOSURE_CONTRAST_LOGARITHMIC (self, *args, **kwargs):
      '''

Members:

  EXPOSURE_CONTRAST_LINEAR : 

  EXPOSURE_CONTRAST_VIDEO : 

  EXPOSURE_CONTRAST_LOGARITHMIC : '''
    ...
    def EXPOSURE_CONTRAST_VIDEO (self, *args, **kwargs):
      '''

Members:

  EXPOSURE_CONTRAST_LINEAR : 

  EXPOSURE_CONTRAST_VIDEO : 

  EXPOSURE_CONTRAST_LOGARITHMIC : '''
    ...
    def name (self, *args, **kwargs):
      '''name(self: handle) -> str
'''
    ...
    def value (self, *args, **kwargs):
      ''''''
    ...

def ExposureContrastStyleFromString (*args):
      '''

'''      
    ...

def ExposureContrastStyleToString (*args):
      '''

'''      
    ...

def ExposureContrastTransform (*args):
      '''

'''      
    ...

class ExposureContrastTransform:
    def equals (self, *args, **kwargs):
      '''equals(self: PyOpenColorIO.ExposureContrastTransform, other: PyOpenColorIO.ExposureContrastTransform) -> bool
'''
    ...
    def getContrast (self, *args, **kwargs):
      '''getContrast(self: PyOpenColorIO.ExposureContrastTransform) -> float
'''
    ...
    def getDirection (self, *args, **kwargs):
      '''getDirection(self: PyOpenColorIO.Transform) -> PyOpenColorIO.TransformDirection
'''
    ...
    def getExposure (self, *args, **kwargs):
      '''getExposure(self: PyOpenColorIO.ExposureContrastTransform) -> float
'''
    ...
    def getFormatMetadata (self, *args, **kwargs):
      '''getFormatMetadata(self: PyOpenColorIO.ExposureContrastTransform) -> PyOpenColorIO.FormatMetadata
'''
    ...
    def getGamma (self, *args, **kwargs):
      '''getGamma(self: PyOpenColorIO.ExposureContrastTransform) -> float
'''
    ...
    def getLogExposureStep (self, *args, **kwargs):
      '''getLogExposureStep(self: PyOpenColorIO.ExposureContrastTransform) -> float
'''
    ...
    def getLogMidGray (self, *args, **kwargs):
      '''getLogMidGray(self: PyOpenColorIO.ExposureContrastTransform) -> float
'''
    ...
    def getPivot (self, *args, **kwargs):
      '''getPivot(self: PyOpenColorIO.ExposureContrastTransform) -> float
'''
    ...
    def getStyle (self, *args, **kwargs):
      '''getStyle(self: PyOpenColorIO.ExposureContrastTransform) -> PyOpenColorIO.ExposureContrastStyle
'''
    ...
    def getTransformType (self, *args, **kwargs):
      '''getTransformType(self: PyOpenColorIO.Transform) -> PyOpenColorIO.TransformType
'''
    ...
    def isContrastDynamic (self, *args, **kwargs):
      '''isContrastDynamic(self: PyOpenColorIO.ExposureContrastTransform) -> bool
'''
    ...
    def isExposureDynamic (self, *args, **kwargs):
      '''isExposureDynamic(self: PyOpenColorIO.ExposureContrastTransform) -> bool
'''
    ...
    def isGammaDynamic (self, *args, **kwargs):
      '''isGammaDynamic(self: PyOpenColorIO.ExposureContrastTransform) -> bool
'''
    ...
    def makeContrastDynamic (self, *args, **kwargs):
      '''makeContrastDynamic(self: PyOpenColorIO.ExposureContrastTransform) -> None
'''
    ...
    def makeContrastNonDynamic (self, *args, **kwargs):
      '''makeContrastNonDynamic(self: PyOpenColorIO.ExposureContrastTransform) -> None
'''
    ...
    def makeExposureDynamic (self, *args, **kwargs):
      '''makeExposureDynamic(self: PyOpenColorIO.ExposureContrastTransform) -> None
'''
    ...
    def makeExposureNonDynamic (self, *args, **kwargs):
      '''makeExposureNonDynamic(self: PyOpenColorIO.ExposureContrastTransform) -> None
'''
    ...
    def makeGammaDynamic (self, *args, **kwargs):
      '''makeGammaDynamic(self: PyOpenColorIO.ExposureContrastTransform) -> None
'''
    ...
    def makeGammaNonDynamic (self, *args, **kwargs):
      '''makeGammaNonDynamic(self: PyOpenColorIO.ExposureContrastTransform) -> None
'''
    ...
    def setContrast (self, *args, **kwargs):
      '''setContrast(self: PyOpenColorIO.ExposureContrastTransform, contrast: float) -> None
'''
    ...
    def setDirection (self, *args, **kwargs):
      '''setDirection(self: PyOpenColorIO.Transform, direction: PyOpenColorIO.TransformDirection) -> None
'''
    ...
    def setExposure (self, *args, **kwargs):
      '''setExposure(self: PyOpenColorIO.ExposureContrastTransform, exposure: float) -> None
'''
    ...
    def setGamma (self, *args, **kwargs):
      '''setGamma(self: PyOpenColorIO.ExposureContrastTransform, gamma: float) -> None
'''
    ...
    def setLogExposureStep (self, *args, **kwargs):
      '''setLogExposureStep(self: PyOpenColorIO.ExposureContrastTransform, logExposureStep: float) -> None
'''
    ...
    def setLogMidGray (self, *args, **kwargs):
      '''setLogMidGray(self: PyOpenColorIO.ExposureContrastTransform, logMidGray: float) -> None
'''
    ...
    def setPivot (self, *args, **kwargs):
      '''setPivot(self: PyOpenColorIO.ExposureContrastTransform, pivot: float) -> None
'''
    ...
    def setStyle (self, *args, **kwargs):
      '''setStyle(self: PyOpenColorIO.ExposureContrastTransform, style: PyOpenColorIO.ExposureContrastStyle) -> None
'''
    ...
    def validate (self, *args, **kwargs):
      '''validate(self: PyOpenColorIO.Transform) -> None
'''
    ...

def ExtractOCIOZArchive (*args):
      '''

'''      
    ...

def FILE_PATH_SEARCH_RULE_NAME (*args):
      '''

'''      
    ...

def FIXED_FUNCTION_ACES_DARK_TO_DIM_10 (*args):
      '''

'''      
    ...

def FIXED_FUNCTION_ACES_GAMUTMAP_02 (*args):
      '''

'''      
    ...

def FIXED_FUNCTION_ACES_GAMUTMAP_07 (*args):
      '''

'''      
    ...

def FIXED_FUNCTION_ACES_GAMUT_COMP_13 (*args):
      '''

'''      
    ...

def FIXED_FUNCTION_ACES_GLOW_03 (*args):
      '''

'''      
    ...

def FIXED_FUNCTION_ACES_GLOW_10 (*args):
      '''

'''      
    ...

def FIXED_FUNCTION_ACES_RED_MOD_03 (*args):
      '''

'''      
    ...

def FIXED_FUNCTION_ACES_RED_MOD_10 (*args):
      '''

'''      
    ...

def FIXED_FUNCTION_REC2100_SURROUND (*args):
      '''

'''      
    ...

def FIXED_FUNCTION_RGB_TO_HSV (*args):
      '''

'''      
    ...

def FIXED_FUNCTION_XYZ_TO_LUV (*args):
      '''

'''      
    ...

def FIXED_FUNCTION_XYZ_TO_uvY (*args):
      '''

'''      
    ...

def FIXED_FUNCTION_XYZ_TO_xyY (*args):
      '''

'''      
    ...

def FileRules (*args):
      '''

'''      
    ...

class FileRules:
    def decreaseRulePriority (self, *args, **kwargs):
      '''decreaseRulePriority(self: PyOpenColorIO.FileRules, ruleIndex: int) -> None
'''
    ...
    def getColorSpace (self, *args, **kwargs):
      '''getColorSpace(self: PyOpenColorIO.FileRules, ruleIndex: int) -> str
'''
    ...
    def getCustomKeyName (self, *args, **kwargs):
      '''getCustomKeyName(self: PyOpenColorIO.FileRules, ruleIndex: int, key: int) -> str
'''
    ...
    def getCustomKeyValue (self, *args, **kwargs):
      '''getCustomKeyValue(self: PyOpenColorIO.FileRules, ruleIndex: int, key: int) -> str
'''
    ...
    def getExtension (self, *args, **kwargs):
      '''getExtension(self: PyOpenColorIO.FileRules, ruleIndex: int) -> str
'''
    ...
    def getIndexForRule (self, *args, **kwargs):
      '''getIndexForRule(self: PyOpenColorIO.FileRules, ruleName: str) -> int
'''
    ...
    def getName (self, *args, **kwargs):
      '''getName(self: PyOpenColorIO.FileRules, ruleIndex: int) -> str
'''
    ...
    def getNumCustomKeys (self, *args, **kwargs):
      '''getNumCustomKeys(self: PyOpenColorIO.FileRules, ruleIndex: int) -> int
'''
    ...
    def getNumEntries (self, *args, **kwargs):
      '''getNumEntries(self: PyOpenColorIO.FileRules) -> int
'''
    ...
    def getPattern (self, *args, **kwargs):
      '''getPattern(self: PyOpenColorIO.FileRules, ruleIndex: int) -> str
'''
    ...
    def getRegex (self, *args, **kwargs):
      '''getRegex(self: PyOpenColorIO.FileRules, ruleIndex: int) -> str
'''
    ...
    def increaseRulePriority (self, *args, **kwargs):
      '''increaseRulePriority(self: PyOpenColorIO.FileRules, ruleIndex: int) -> None
'''
    ...
    def insertPathSearchRule (self, *args, **kwargs):
      '''insertPathSearchRule(self: PyOpenColorIO.FileRules, ruleIndex: int) -> None
'''
    ...
    def insertRule (self, *args, **kwargs):
      '''insertRule(*args, **kwargs)
Overloaded function.

1. insertRule(self: PyOpenColorIO.FileRules, ruleIndex: int, name: str, colorSpace: str, pattern: str, extension: str) -> None

2. insertRule(self: PyOpenColorIO.FileRules, ruleIndex: int, name: str, colorSpace: str, regex: str) -> None
'''
    ...
    def isDefault (self, *args, **kwargs):
      '''isDefault(self: PyOpenColorIO.FileRules) -> bool
'''
    ...
    def removeRule (self, *args, **kwargs):
      '''removeRule(self: PyOpenColorIO.FileRules, ruleIndex: int) -> None
'''
    ...
    def setColorSpace (self, *args, **kwargs):
      '''setColorSpace(self: PyOpenColorIO.FileRules, ruleIndex: int, colorSpace: str) -> None
'''
    ...
    def setCustomKey (self, *args, **kwargs):
      '''setCustomKey(self: PyOpenColorIO.FileRules, ruleIndex: int, key: str, value: str) -> None
'''
    ...
    def setDefaultRuleColorSpace (self, *args, **kwargs):
      '''setDefaultRuleColorSpace(self: PyOpenColorIO.FileRules, colorSpace: str) -> None
'''
    ...
    def setExtension (self, *args, **kwargs):
      '''setExtension(self: PyOpenColorIO.FileRules, ruleIndex: int, extension: str) -> None
'''
    ...
    def setPattern (self, *args, **kwargs):
      '''setPattern(self: PyOpenColorIO.FileRules, ruleIndex: int, pattern: str) -> None
'''
    ...
    def setRegex (self, *args, **kwargs):
      '''setRegex(self: PyOpenColorIO.FileRules, ruleIndex: int, regex: str) -> None
'''
    ...

def FileTransform (*args):
      '''

'''      
    ...

class FileTransform:
    def FormatIterator (self, *args, **kwargs):
      '''None'''
    ...
    def getCCCId (self, *args, **kwargs):
      '''getCCCId(self: PyOpenColorIO.FileTransform) -> str
'''
    ...
    def getCDLStyle (self, *args, **kwargs):
      '''getCDLStyle(self: PyOpenColorIO.FileTransform) -> PyOpenColorIO.CDLStyle
'''
    ...
    def getDirection (self, *args, **kwargs):
      '''getDirection(self: PyOpenColorIO.Transform) -> PyOpenColorIO.TransformDirection
'''
    ...
    def getFormats (self, *args, **kwargs):
      '''getFormats() -> PyOpenColorIO.FileTransform.FormatIterator
'''
    ...
    def getInterpolation (self, *args, **kwargs):
      '''getInterpolation(self: PyOpenColorIO.FileTransform) -> PyOpenColorIO.Interpolation
'''
    ...
    def getSrc (self, *args, **kwargs):
      '''getSrc(self: PyOpenColorIO.FileTransform) -> str
'''
    ...
    def getTransformType (self, *args, **kwargs):
      '''getTransformType(self: PyOpenColorIO.Transform) -> PyOpenColorIO.TransformType
'''
    ...
    def setCCCId (self, *args, **kwargs):
      '''setCCCId(self: PyOpenColorIO.FileTransform, cccId: str) -> None
'''
    ...
    def setCDLStyle (self, *args, **kwargs):
      '''setCDLStyle(self: PyOpenColorIO.FileTransform, style: PyOpenColorIO.CDLStyle) -> None
'''
    ...
    def setDirection (self, *args, **kwargs):
      '''setDirection(self: PyOpenColorIO.Transform, direction: PyOpenColorIO.TransformDirection) -> None
'''
    ...
    def setInterpolation (self, *args, **kwargs):
      '''setInterpolation(self: PyOpenColorIO.FileTransform, interpolation: PyOpenColorIO.Interpolation) -> None
'''
    ...
    def setSrc (self, *args, **kwargs):
      '''setSrc(self: PyOpenColorIO.FileTransform, src: str) -> None
'''
    ...
    def validate (self, *args, **kwargs):
      '''validate(self: PyOpenColorIO.Transform) -> None
'''
    ...

def FixedFunctionStyle (*args):
      '''

'''      
    ...

class FixedFunctionStyle:
    def FIXED_FUNCTION_ACES_DARK_TO_DIM_10 (self, *args, **kwargs):
      '''

Members:

  FIXED_FUNCTION_ACES_RED_MOD_03 : 

  FIXED_FUNCTION_ACES_RED_MOD_10 : 

  FIXED_FUNCTION_ACES_GLOW_03 : 

  FIXED_FUNCTION_ACES_GLOW_10 : 

  FIXED_FUNCTION_ACES_DARK_TO_DIM_10 : 

  FIXED_FUNCTION_REC2100_SURROUND : 

  FIXED_FUNCTION_RGB_TO_HSV : 

  FIXED_FUNCTION_XYZ_TO_xyY : 

  FIXED_FUNCTION_XYZ_TO_uvY : 

  FIXED_FUNCTION_XYZ_TO_LUV : 

  FIXED_FUNCTION_ACES_GAMUTMAP_02 : 

  FIXED_FUNCTION_ACES_GAMUTMAP_07 : 

  FIXED_FUNCTION_ACES_GAMUT_COMP_13 : '''
    ...
    def FIXED_FUNCTION_ACES_GAMUTMAP_02 (self, *args, **kwargs):
      '''

Members:

  FIXED_FUNCTION_ACES_RED_MOD_03 : 

  FIXED_FUNCTION_ACES_RED_MOD_10 : 

  FIXED_FUNCTION_ACES_GLOW_03 : 

  FIXED_FUNCTION_ACES_GLOW_10 : 

  FIXED_FUNCTION_ACES_DARK_TO_DIM_10 : 

  FIXED_FUNCTION_REC2100_SURROUND : 

  FIXED_FUNCTION_RGB_TO_HSV : 

  FIXED_FUNCTION_XYZ_TO_xyY : 

  FIXED_FUNCTION_XYZ_TO_uvY : 

  FIXED_FUNCTION_XYZ_TO_LUV : 

  FIXED_FUNCTION_ACES_GAMUTMAP_02 : 

  FIXED_FUNCTION_ACES_GAMUTMAP_07 : 

  FIXED_FUNCTION_ACES_GAMUT_COMP_13 : '''
    ...
    def FIXED_FUNCTION_ACES_GAMUTMAP_07 (self, *args, **kwargs):
      '''

Members:

  FIXED_FUNCTION_ACES_RED_MOD_03 : 

  FIXED_FUNCTION_ACES_RED_MOD_10 : 

  FIXED_FUNCTION_ACES_GLOW_03 : 

  FIXED_FUNCTION_ACES_GLOW_10 : 

  FIXED_FUNCTION_ACES_DARK_TO_DIM_10 : 

  FIXED_FUNCTION_REC2100_SURROUND : 

  FIXED_FUNCTION_RGB_TO_HSV : 

  FIXED_FUNCTION_XYZ_TO_xyY : 

  FIXED_FUNCTION_XYZ_TO_uvY : 

  FIXED_FUNCTION_XYZ_TO_LUV : 

  FIXED_FUNCTION_ACES_GAMUTMAP_02 : 

  FIXED_FUNCTION_ACES_GAMUTMAP_07 : 

  FIXED_FUNCTION_ACES_GAMUT_COMP_13 : '''
    ...
    def FIXED_FUNCTION_ACES_GAMUT_COMP_13 (self, *args, **kwargs):
      '''

Members:

  FIXED_FUNCTION_ACES_RED_MOD_03 : 

  FIXED_FUNCTION_ACES_RED_MOD_10 : 

  FIXED_FUNCTION_ACES_GLOW_03 : 

  FIXED_FUNCTION_ACES_GLOW_10 : 

  FIXED_FUNCTION_ACES_DARK_TO_DIM_10 : 

  FIXED_FUNCTION_REC2100_SURROUND : 

  FIXED_FUNCTION_RGB_TO_HSV : 

  FIXED_FUNCTION_XYZ_TO_xyY : 

  FIXED_FUNCTION_XYZ_TO_uvY : 

  FIXED_FUNCTION_XYZ_TO_LUV : 

  FIXED_FUNCTION_ACES_GAMUTMAP_02 : 

  FIXED_FUNCTION_ACES_GAMUTMAP_07 : 

  FIXED_FUNCTION_ACES_GAMUT_COMP_13 : '''
    ...
    def FIXED_FUNCTION_ACES_GLOW_03 (self, *args, **kwargs):
      '''

Members:

  FIXED_FUNCTION_ACES_RED_MOD_03 : 

  FIXED_FUNCTION_ACES_RED_MOD_10 : 

  FIXED_FUNCTION_ACES_GLOW_03 : 

  FIXED_FUNCTION_ACES_GLOW_10 : 

  FIXED_FUNCTION_ACES_DARK_TO_DIM_10 : 

  FIXED_FUNCTION_REC2100_SURROUND : 

  FIXED_FUNCTION_RGB_TO_HSV : 

  FIXED_FUNCTION_XYZ_TO_xyY : 

  FIXED_FUNCTION_XYZ_TO_uvY : 

  FIXED_FUNCTION_XYZ_TO_LUV : 

  FIXED_FUNCTION_ACES_GAMUTMAP_02 : 

  FIXED_FUNCTION_ACES_GAMUTMAP_07 : 

  FIXED_FUNCTION_ACES_GAMUT_COMP_13 : '''
    ...
    def FIXED_FUNCTION_ACES_GLOW_10 (self, *args, **kwargs):
      '''

Members:

  FIXED_FUNCTION_ACES_RED_MOD_03 : 

  FIXED_FUNCTION_ACES_RED_MOD_10 : 

  FIXED_FUNCTION_ACES_GLOW_03 : 

  FIXED_FUNCTION_ACES_GLOW_10 : 

  FIXED_FUNCTION_ACES_DARK_TO_DIM_10 : 

  FIXED_FUNCTION_REC2100_SURROUND : 

  FIXED_FUNCTION_RGB_TO_HSV : 

  FIXED_FUNCTION_XYZ_TO_xyY : 

  FIXED_FUNCTION_XYZ_TO_uvY : 

  FIXED_FUNCTION_XYZ_TO_LUV : 

  FIXED_FUNCTION_ACES_GAMUTMAP_02 : 

  FIXED_FUNCTION_ACES_GAMUTMAP_07 : 

  FIXED_FUNCTION_ACES_GAMUT_COMP_13 : '''
    ...
    def FIXED_FUNCTION_ACES_RED_MOD_03 (self, *args, **kwargs):
      '''

Members:

  FIXED_FUNCTION_ACES_RED_MOD_03 : 

  FIXED_FUNCTION_ACES_RED_MOD_10 : 

  FIXED_FUNCTION_ACES_GLOW_03 : 

  FIXED_FUNCTION_ACES_GLOW_10 : 

  FIXED_FUNCTION_ACES_DARK_TO_DIM_10 : 

  FIXED_FUNCTION_REC2100_SURROUND : 

  FIXED_FUNCTION_RGB_TO_HSV : 

  FIXED_FUNCTION_XYZ_TO_xyY : 

  FIXED_FUNCTION_XYZ_TO_uvY : 

  FIXED_FUNCTION_XYZ_TO_LUV : 

  FIXED_FUNCTION_ACES_GAMUTMAP_02 : 

  FIXED_FUNCTION_ACES_GAMUTMAP_07 : 

  FIXED_FUNCTION_ACES_GAMUT_COMP_13 : '''
    ...
    def FIXED_FUNCTION_ACES_RED_MOD_10 (self, *args, **kwargs):
      '''

Members:

  FIXED_FUNCTION_ACES_RED_MOD_03 : 

  FIXED_FUNCTION_ACES_RED_MOD_10 : 

  FIXED_FUNCTION_ACES_GLOW_03 : 

  FIXED_FUNCTION_ACES_GLOW_10 : 

  FIXED_FUNCTION_ACES_DARK_TO_DIM_10 : 

  FIXED_FUNCTION_REC2100_SURROUND : 

  FIXED_FUNCTION_RGB_TO_HSV : 

  FIXED_FUNCTION_XYZ_TO_xyY : 

  FIXED_FUNCTION_XYZ_TO_uvY : 

  FIXED_FUNCTION_XYZ_TO_LUV : 

  FIXED_FUNCTION_ACES_GAMUTMAP_02 : 

  FIXED_FUNCTION_ACES_GAMUTMAP_07 : 

  FIXED_FUNCTION_ACES_GAMUT_COMP_13 : '''
    ...
    def FIXED_FUNCTION_REC2100_SURROUND (self, *args, **kwargs):
      '''

Members:

  FIXED_FUNCTION_ACES_RED_MOD_03 : 

  FIXED_FUNCTION_ACES_RED_MOD_10 : 

  FIXED_FUNCTION_ACES_GLOW_03 : 

  FIXED_FUNCTION_ACES_GLOW_10 : 

  FIXED_FUNCTION_ACES_DARK_TO_DIM_10 : 

  FIXED_FUNCTION_REC2100_SURROUND : 

  FIXED_FUNCTION_RGB_TO_HSV : 

  FIXED_FUNCTION_XYZ_TO_xyY : 

  FIXED_FUNCTION_XYZ_TO_uvY : 

  FIXED_FUNCTION_XYZ_TO_LUV : 

  FIXED_FUNCTION_ACES_GAMUTMAP_02 : 

  FIXED_FUNCTION_ACES_GAMUTMAP_07 : 

  FIXED_FUNCTION_ACES_GAMUT_COMP_13 : '''
    ...
    def FIXED_FUNCTION_RGB_TO_HSV (self, *args, **kwargs):
      '''

Members:

  FIXED_FUNCTION_ACES_RED_MOD_03 : 

  FIXED_FUNCTION_ACES_RED_MOD_10 : 

  FIXED_FUNCTION_ACES_GLOW_03 : 

  FIXED_FUNCTION_ACES_GLOW_10 : 

  FIXED_FUNCTION_ACES_DARK_TO_DIM_10 : 

  FIXED_FUNCTION_REC2100_SURROUND : 

  FIXED_FUNCTION_RGB_TO_HSV : 

  FIXED_FUNCTION_XYZ_TO_xyY : 

  FIXED_FUNCTION_XYZ_TO_uvY : 

  FIXED_FUNCTION_XYZ_TO_LUV : 

  FIXED_FUNCTION_ACES_GAMUTMAP_02 : 

  FIXED_FUNCTION_ACES_GAMUTMAP_07 : 

  FIXED_FUNCTION_ACES_GAMUT_COMP_13 : '''
    ...
    def FIXED_FUNCTION_XYZ_TO_LUV (self, *args, **kwargs):
      '''

Members:

  FIXED_FUNCTION_ACES_RED_MOD_03 : 

  FIXED_FUNCTION_ACES_RED_MOD_10 : 

  FIXED_FUNCTION_ACES_GLOW_03 : 

  FIXED_FUNCTION_ACES_GLOW_10 : 

  FIXED_FUNCTION_ACES_DARK_TO_DIM_10 : 

  FIXED_FUNCTION_REC2100_SURROUND : 

  FIXED_FUNCTION_RGB_TO_HSV : 

  FIXED_FUNCTION_XYZ_TO_xyY : 

  FIXED_FUNCTION_XYZ_TO_uvY : 

  FIXED_FUNCTION_XYZ_TO_LUV : 

  FIXED_FUNCTION_ACES_GAMUTMAP_02 : 

  FIXED_FUNCTION_ACES_GAMUTMAP_07 : 

  FIXED_FUNCTION_ACES_GAMUT_COMP_13 : '''
    ...
    def FIXED_FUNCTION_XYZ_TO_uvY (self, *args, **kwargs):
      '''

Members:

  FIXED_FUNCTION_ACES_RED_MOD_03 : 

  FIXED_FUNCTION_ACES_RED_MOD_10 : 

  FIXED_FUNCTION_ACES_GLOW_03 : 

  FIXED_FUNCTION_ACES_GLOW_10 : 

  FIXED_FUNCTION_ACES_DARK_TO_DIM_10 : 

  FIXED_FUNCTION_REC2100_SURROUND : 

  FIXED_FUNCTION_RGB_TO_HSV : 

  FIXED_FUNCTION_XYZ_TO_xyY : 

  FIXED_FUNCTION_XYZ_TO_uvY : 

  FIXED_FUNCTION_XYZ_TO_LUV : 

  FIXED_FUNCTION_ACES_GAMUTMAP_02 : 

  FIXED_FUNCTION_ACES_GAMUTMAP_07 : 

  FIXED_FUNCTION_ACES_GAMUT_COMP_13 : '''
    ...
    def FIXED_FUNCTION_XYZ_TO_xyY (self, *args, **kwargs):
      '''

Members:

  FIXED_FUNCTION_ACES_RED_MOD_03 : 

  FIXED_FUNCTION_ACES_RED_MOD_10 : 

  FIXED_FUNCTION_ACES_GLOW_03 : 

  FIXED_FUNCTION_ACES_GLOW_10 : 

  FIXED_FUNCTION_ACES_DARK_TO_DIM_10 : 

  FIXED_FUNCTION_REC2100_SURROUND : 

  FIXED_FUNCTION_RGB_TO_HSV : 

  FIXED_FUNCTION_XYZ_TO_xyY : 

  FIXED_FUNCTION_XYZ_TO_uvY : 

  FIXED_FUNCTION_XYZ_TO_LUV : 

  FIXED_FUNCTION_ACES_GAMUTMAP_02 : 

  FIXED_FUNCTION_ACES_GAMUTMAP_07 : 

  FIXED_FUNCTION_ACES_GAMUT_COMP_13 : '''
    ...
    def name (self, *args, **kwargs):
      '''name(self: handle) -> str
'''
    ...
    def value (self, *args, **kwargs):
      ''''''
    ...

def FixedFunctionStyleFromString (*args):
      '''

'''      
    ...

def FixedFunctionStyleToString (*args):
      '''

'''      
    ...

def FixedFunctionTransform (*args):
      '''

'''      
    ...

class FixedFunctionTransform:
    def equals (self, *args, **kwargs):
      '''equals(self: PyOpenColorIO.FixedFunctionTransform, other: PyOpenColorIO.FixedFunctionTransform) -> bool
'''
    ...
    def getDirection (self, *args, **kwargs):
      '''getDirection(self: PyOpenColorIO.Transform) -> PyOpenColorIO.TransformDirection
'''
    ...
    def getFormatMetadata (self, *args, **kwargs):
      '''getFormatMetadata(self: PyOpenColorIO.FixedFunctionTransform) -> PyOpenColorIO.FormatMetadata
'''
    ...
    def getParams (self, *args, **kwargs):
      '''getParams(self: PyOpenColorIO.FixedFunctionTransform) -> List[float]
'''
    ...
    def getStyle (self, *args, **kwargs):
      '''getStyle(self: PyOpenColorIO.FixedFunctionTransform) -> PyOpenColorIO.FixedFunctionStyle
'''
    ...
    def getTransformType (self, *args, **kwargs):
      '''getTransformType(self: PyOpenColorIO.Transform) -> PyOpenColorIO.TransformType
'''
    ...
    def setDirection (self, *args, **kwargs):
      '''setDirection(self: PyOpenColorIO.Transform, direction: PyOpenColorIO.TransformDirection) -> None
'''
    ...
    def setParams (self, *args, **kwargs):
      '''setParams(self: PyOpenColorIO.FixedFunctionTransform, params: List[float]) -> None
'''
    ...
    def setStyle (self, *args, **kwargs):
      '''setStyle(self: PyOpenColorIO.FixedFunctionTransform, style: PyOpenColorIO.FixedFunctionStyle) -> None
'''
    ...
    def validate (self, *args, **kwargs):
      '''validate(self: PyOpenColorIO.Transform) -> None
'''
    ...

def FormatMetadata (*args):
      '''

'''      
    ...

class FormatMetadata:
    def AttributeIterator (self, *args, **kwargs):
      '''None'''
    ...
    def AttributeNameIterator (self, *args, **kwargs):
      '''None'''
    ...
    def ChildElementIterator (self, *args, **kwargs):
      '''None'''
    ...
    def ConstChildElementIterator (self, *args, **kwargs):
      '''None'''
    ...
    def addChildElement (self, *args, **kwargs):
      '''addChildElement(self: PyOpenColorIO.FormatMetadata, name: str, value: str) -> None
'''
    ...
    def clear (self, *args, **kwargs):
      '''clear(self: PyOpenColorIO.FormatMetadata) -> None
'''
    ...
    def getAttributes (self, *args, **kwargs):
      '''getAttributes(self: PyOpenColorIO.FormatMetadata) -> PyOpenColorIO.FormatMetadata.AttributeIterator
'''
    ...
    def getChildElements (self, *args, **kwargs):
      '''getChildElements(self: PyOpenColorIO.FormatMetadata) -> PyOpenColorIO.FormatMetadata.ChildElementIterator
'''
    ...
    def getElementName (self, *args, **kwargs):
      '''getElementName(self: PyOpenColorIO.FormatMetadata) -> str
'''
    ...
    def getElementValue (self, *args, **kwargs):
      '''getElementValue(self: PyOpenColorIO.FormatMetadata) -> str
'''
    ...
    def getID (self, *args, **kwargs):
      '''getID(self: PyOpenColorIO.FormatMetadata) -> str
'''
    ...
    def getName (self, *args, **kwargs):
      '''getName(self: PyOpenColorIO.FormatMetadata) -> str
'''
    ...
    def setElementName (self, *args, **kwargs):
      '''setElementName(self: PyOpenColorIO.FormatMetadata, name: str) -> None
'''
    ...
    def setElementValue (self, *args, **kwargs):
      '''setElementValue(self: PyOpenColorIO.FormatMetadata, value: str) -> None
'''
    ...
    def setID (self, *args, **kwargs):
      '''setID(self: PyOpenColorIO.FormatMetadata, id: str) -> None
'''
    ...
    def setName (self, *args, **kwargs):
      '''setName(self: PyOpenColorIO.FormatMetadata, name: str) -> None
'''
    ...

def GPUProcessor (*args):
      '''

'''      
    ...

class GPUProcessor:
    def extractGpuShaderInfo (self, *args, **kwargs):
      '''extractGpuShaderInfo(self: PyOpenColorIO.GPUProcessor, shaderDesc: PyOpenColorIO.GpuShaderDesc) -> None
'''
    ...
    def getCacheID (self, *args, **kwargs):
      '''getCacheID(self: PyOpenColorIO.GPUProcessor) -> str
'''
    ...
    def hasChannelCrosstalk (self, *args, **kwargs):
      '''hasChannelCrosstalk(self: PyOpenColorIO.GPUProcessor) -> bool
'''
    ...
    def isNoOp (self, *args, **kwargs):
      '''isNoOp(self: PyOpenColorIO.GPUProcessor) -> bool
'''
    ...

def GPU_LANGUAGE_CG (*args):
      '''

'''      
    ...

def GPU_LANGUAGE_GLSL_1_2 (*args):
      '''

'''      
    ...

def GPU_LANGUAGE_GLSL_1_3 (*args):
      '''

'''      
    ...

def GPU_LANGUAGE_GLSL_4_0 (*args):
      '''

'''      
    ...

def GPU_LANGUAGE_GLSL_ES_1_0 (*args):
      '''

'''      
    ...

def GPU_LANGUAGE_GLSL_ES_3_0 (*args):
      '''

'''      
    ...

def GPU_LANGUAGE_HLSL_DX11 (*args):
      '''

'''      
    ...

def GPU_LANGUAGE_MSL_2_0 (*args):
      '''

'''      
    ...

def GRADING_LIN (*args):
      '''

'''      
    ...

def GRADING_LOG (*args):
      '''

'''      
    ...

def GRADING_VIDEO (*args):
      '''

'''      
    ...

def GetCurrentConfig (*args):
      '''

'''      
    ...

def GetEnvVariable (*args):
      '''

'''      
    ...

def GetInverseTransformDirection (*args):
      '''

'''      
    ...

def GetLoggingLevel (*args):
      '''

'''      
    ...

def GetVersion (*args):
      '''

'''      
    ...

def GetVersionHex (*args):
      '''

'''      
    ...

def GpuLanguage (*args):
      '''

'''      
    ...

class GpuLanguage:
    def GPU_LANGUAGE_CG (self, *args, **kwargs):
      '''

Members:

  GPU_LANGUAGE_CG : 

  GPU_LANGUAGE_GLSL_1_2 : 

  GPU_LANGUAGE_GLSL_1_3 : 

  GPU_LANGUAGE_GLSL_4_0 : 

  GPU_LANGUAGE_GLSL_ES_1_0 : 

  GPU_LANGUAGE_GLSL_ES_3_0 : 

  GPU_LANGUAGE_HLSL_DX11 : 

  GPU_LANGUAGE_MSL_2_0 : '''
    ...
    def GPU_LANGUAGE_GLSL_1_2 (self, *args, **kwargs):
      '''

Members:

  GPU_LANGUAGE_CG : 

  GPU_LANGUAGE_GLSL_1_2 : 

  GPU_LANGUAGE_GLSL_1_3 : 

  GPU_LANGUAGE_GLSL_4_0 : 

  GPU_LANGUAGE_GLSL_ES_1_0 : 

  GPU_LANGUAGE_GLSL_ES_3_0 : 

  GPU_LANGUAGE_HLSL_DX11 : 

  GPU_LANGUAGE_MSL_2_0 : '''
    ...
    def GPU_LANGUAGE_GLSL_1_3 (self, *args, **kwargs):
      '''

Members:

  GPU_LANGUAGE_CG : 

  GPU_LANGUAGE_GLSL_1_2 : 

  GPU_LANGUAGE_GLSL_1_3 : 

  GPU_LANGUAGE_GLSL_4_0 : 

  GPU_LANGUAGE_GLSL_ES_1_0 : 

  GPU_LANGUAGE_GLSL_ES_3_0 : 

  GPU_LANGUAGE_HLSL_DX11 : 

  GPU_LANGUAGE_MSL_2_0 : '''
    ...
    def GPU_LANGUAGE_GLSL_4_0 (self, *args, **kwargs):
      '''

Members:

  GPU_LANGUAGE_CG : 

  GPU_LANGUAGE_GLSL_1_2 : 

  GPU_LANGUAGE_GLSL_1_3 : 

  GPU_LANGUAGE_GLSL_4_0 : 

  GPU_LANGUAGE_GLSL_ES_1_0 : 

  GPU_LANGUAGE_GLSL_ES_3_0 : 

  GPU_LANGUAGE_HLSL_DX11 : 

  GPU_LANGUAGE_MSL_2_0 : '''
    ...
    def GPU_LANGUAGE_GLSL_ES_1_0 (self, *args, **kwargs):
      '''

Members:

  GPU_LANGUAGE_CG : 

  GPU_LANGUAGE_GLSL_1_2 : 

  GPU_LANGUAGE_GLSL_1_3 : 

  GPU_LANGUAGE_GLSL_4_0 : 

  GPU_LANGUAGE_GLSL_ES_1_0 : 

  GPU_LANGUAGE_GLSL_ES_3_0 : 

  GPU_LANGUAGE_HLSL_DX11 : 

  GPU_LANGUAGE_MSL_2_0 : '''
    ...
    def GPU_LANGUAGE_GLSL_ES_3_0 (self, *args, **kwargs):
      '''

Members:

  GPU_LANGUAGE_CG : 

  GPU_LANGUAGE_GLSL_1_2 : 

  GPU_LANGUAGE_GLSL_1_3 : 

  GPU_LANGUAGE_GLSL_4_0 : 

  GPU_LANGUAGE_GLSL_ES_1_0 : 

  GPU_LANGUAGE_GLSL_ES_3_0 : 

  GPU_LANGUAGE_HLSL_DX11 : 

  GPU_LANGUAGE_MSL_2_0 : '''
    ...
    def GPU_LANGUAGE_HLSL_DX11 (self, *args, **kwargs):
      '''

Members:

  GPU_LANGUAGE_CG : 

  GPU_LANGUAGE_GLSL_1_2 : 

  GPU_LANGUAGE_GLSL_1_3 : 

  GPU_LANGUAGE_GLSL_4_0 : 

  GPU_LANGUAGE_GLSL_ES_1_0 : 

  GPU_LANGUAGE_GLSL_ES_3_0 : 

  GPU_LANGUAGE_HLSL_DX11 : 

  GPU_LANGUAGE_MSL_2_0 : '''
    ...
    def GPU_LANGUAGE_MSL_2_0 (self, *args, **kwargs):
      '''

Members:

  GPU_LANGUAGE_CG : 

  GPU_LANGUAGE_GLSL_1_2 : 

  GPU_LANGUAGE_GLSL_1_3 : 

  GPU_LANGUAGE_GLSL_4_0 : 

  GPU_LANGUAGE_GLSL_ES_1_0 : 

  GPU_LANGUAGE_GLSL_ES_3_0 : 

  GPU_LANGUAGE_HLSL_DX11 : 

  GPU_LANGUAGE_MSL_2_0 : '''
    ...
    def name (self, *args, **kwargs):
      '''name(self: handle) -> str
'''
    ...
    def value (self, *args, **kwargs):
      ''''''
    ...

def GpuLanguageFromString (*args):
      '''

'''      
    ...

def GpuLanguageToString (*args):
      '''

'''      
    ...

def GpuShaderCreator (*args):
      '''

'''      
    ...

class GpuShaderCreator:
    def DynamicPropertyIterator (self, *args, **kwargs):
      '''None'''
    ...
    def TEXTURE_RED_CHANNEL (self, *args, **kwargs):
      '''

Members:

  TEXTURE_RED_CHANNEL

  TEXTURE_RGB_CHANNEL'''
    ...
    def TEXTURE_RGB_CHANNEL (self, *args, **kwargs):
      '''

Members:

  TEXTURE_RED_CHANNEL

  TEXTURE_RGB_CHANNEL'''
    ...
    def TextureType (self, *args, **kwargs):
      '''

Members:

  TEXTURE_RED_CHANNEL

  TEXTURE_RGB_CHANNEL'''
    ...
    def addToDeclareShaderCode (self, *args, **kwargs):
      '''addToDeclareShaderCode(self: PyOpenColorIO.GpuShaderCreator, shaderCode: str) -> None
'''
    ...
    def addToFunctionFooterShaderCode (self, *args, **kwargs):
      '''addToFunctionFooterShaderCode(self: PyOpenColorIO.GpuShaderCreator, shaderCode: str) -> None
'''
    ...
    def addToFunctionHeaderShaderCode (self, *args, **kwargs):
      '''addToFunctionHeaderShaderCode(self: PyOpenColorIO.GpuShaderCreator, shaderCode: str) -> None
'''
    ...
    def addToFunctionShaderCode (self, *args, **kwargs):
      '''addToFunctionShaderCode(self: PyOpenColorIO.GpuShaderCreator, shaderCode: str) -> None
'''
    ...
    def addToHelperShaderCode (self, *args, **kwargs):
      '''addToHelperShaderCode(self: PyOpenColorIO.GpuShaderCreator, shaderCode: str) -> None
'''
    ...
    def begin (self, *args, **kwargs):
      '''begin(self: PyOpenColorIO.GpuShaderCreator, uid: str) -> None
'''
    ...
    def clone (self, *args, **kwargs):
      '''clone(self: PyOpenColorIO.GpuShaderCreator) -> PyOpenColorIO.GpuShaderCreator
'''
    ...
    def createShaderText (self, *args, **kwargs):
      '''createShaderText(self: PyOpenColorIO.GpuShaderCreator, shaderDeclarations: str, shaderHelperMethods: str, shaderFunctionHeader: str, shaderFunctionBody: str, shaderFunctionFooter: str) -> None
'''
    ...
    def end (self, *args, **kwargs):
      '''end(self: PyOpenColorIO.GpuShaderCreator) -> None
'''
    ...
    def finalize (self, *args, **kwargs):
      '''finalize(self: PyOpenColorIO.GpuShaderCreator) -> None
'''
    ...
    def getCacheID (self, *args, **kwargs):
      '''getCacheID(self: PyOpenColorIO.GpuShaderCreator) -> str
'''
    ...
    def getDynamicProperties (self, *args, **kwargs):
      '''getDynamicProperties(self: PyOpenColorIO.GpuShaderCreator) -> PyOpenColorIO.GpuShaderCreator.DynamicPropertyIterator
'''
    ...
    def getDynamicProperty (self, *args, **kwargs):
      '''getDynamicProperty(self: PyOpenColorIO.GpuShaderCreator, type: PyOpenColorIO.DynamicPropertyType) -> PyOpenColorIO.DynamicProperty
'''
    ...
    def getFunctionName (self, *args, **kwargs):
      '''getFunctionName(self: PyOpenColorIO.GpuShaderCreator) -> str
'''
    ...
    def getLanguage (self, *args, **kwargs):
      '''getLanguage(self: PyOpenColorIO.GpuShaderCreator) -> PyOpenColorIO.GpuLanguage
'''
    ...
    def getNextResourceIndex (self, *args, **kwargs):
      '''getNextResourceIndex(self: PyOpenColorIO.GpuShaderCreator) -> int
'''
    ...
    def getPixelName (self, *args, **kwargs):
      '''getPixelName(self: PyOpenColorIO.GpuShaderCreator) -> str
'''
    ...
    def getResourcePrefix (self, *args, **kwargs):
      '''getResourcePrefix(self: PyOpenColorIO.GpuShaderCreator) -> str
'''
    ...
    def getTextureMaxWidth (self, *args, **kwargs):
      '''getTextureMaxWidth(self: PyOpenColorIO.GpuShaderCreator) -> int
'''
    ...
    def getUniqueID (self, *args, **kwargs):
      '''getUniqueID(self: PyOpenColorIO.GpuShaderCreator) -> str
'''
    ...
    def hasDynamicProperty (self, *args, **kwargs):
      '''hasDynamicProperty(self: PyOpenColorIO.GpuShaderCreator, type: PyOpenColorIO.DynamicPropertyType) -> bool
'''
    ...
    def setFunctionName (self, *args, **kwargs):
      '''setFunctionName(self: PyOpenColorIO.GpuShaderCreator, name: str) -> None
'''
    ...
    def setLanguage (self, *args, **kwargs):
      '''setLanguage(self: PyOpenColorIO.GpuShaderCreator, language: PyOpenColorIO.GpuLanguage) -> None
'''
    ...
    def setPixelName (self, *args, **kwargs):
      '''setPixelName(self: PyOpenColorIO.GpuShaderCreator, name: str) -> None
'''
    ...
    def setResourcePrefix (self, *args, **kwargs):
      '''setResourcePrefix(self: PyOpenColorIO.GpuShaderCreator, prefix: str) -> None
'''
    ...
    def setTextureMaxWidth (self, *args, **kwargs):
      '''setTextureMaxWidth(self: PyOpenColorIO.GpuShaderCreator, maxWidth: int) -> None
'''
    ...
    def setUniqueID (self, *args, **kwargs):
      '''setUniqueID(self: PyOpenColorIO.GpuShaderCreator, uid: str) -> None
'''
    ...

def GpuShaderDesc (*args):
      '''

'''      
    ...

class GpuShaderDesc:
    def CreateShaderDesc (self, *args, **kwargs):
      '''CreateShaderDesc(language: PyOpenColorIO.GpuLanguage = <GpuLanguage.GPU_LANGUAGE_GLSL_1_2: 1>, functionName: str = 'OCIOMain', pixelName: str = 'outColor', resourcePrefix: str = 'ocio', uid: str = '') -> PyOpenColorIO.GpuShaderDesc
'''
    ...
    def DynamicPropertyIterator (self, *args, **kwargs):
      '''None'''
    ...
    def TEXTURE_RED_CHANNEL (self, *args, **kwargs):
      '''

Members:

  TEXTURE_RED_CHANNEL

  TEXTURE_RGB_CHANNEL'''
    ...
    def TEXTURE_RGB_CHANNEL (self, *args, **kwargs):
      '''

Members:

  TEXTURE_RED_CHANNEL

  TEXTURE_RGB_CHANNEL'''
    ...
    def Texture (self, *args, **kwargs):
      '''None'''
    ...
    def Texture3D (self, *args, **kwargs):
      '''None'''
    ...
    def Texture3DIterator (self, *args, **kwargs):
      '''None'''
    ...
    def TextureIterator (self, *args, **kwargs):
      '''None'''
    ...
    def TextureType (self, *args, **kwargs):
      '''

Members:

  TEXTURE_RED_CHANNEL

  TEXTURE_RGB_CHANNEL'''
    ...
    def UniformData (self, *args, **kwargs):
      '''None'''
    ...
    def UniformIterator (self, *args, **kwargs):
      '''None'''
    ...
    def add3DTexture (self, *args, **kwargs):
      '''add3DTexture(self: PyOpenColorIO.GpuShaderDesc, textureName: str, samplerName: str, edgeLen: int, interpolation: PyOpenColorIO.Interpolation, values: buffer) -> None
'''
    ...
    def addTexture (self, *args, **kwargs):
      '''addTexture(self: PyOpenColorIO.GpuShaderDesc, textureName: str, samplerName: str, width: int, height: int, channel: PyOpenColorIO.GpuShaderCreator.TextureType, interpolation: PyOpenColorIO.Interpolation, values: buffer) -> None
'''
    ...
    def addToDeclareShaderCode (self, *args, **kwargs):
      '''addToDeclareShaderCode(self: PyOpenColorIO.GpuShaderCreator, shaderCode: str) -> None
'''
    ...
    def addToFunctionFooterShaderCode (self, *args, **kwargs):
      '''addToFunctionFooterShaderCode(self: PyOpenColorIO.GpuShaderCreator, shaderCode: str) -> None
'''
    ...
    def addToFunctionHeaderShaderCode (self, *args, **kwargs):
      '''addToFunctionHeaderShaderCode(self: PyOpenColorIO.GpuShaderCreator, shaderCode: str) -> None
'''
    ...
    def addToFunctionShaderCode (self, *args, **kwargs):
      '''addToFunctionShaderCode(self: PyOpenColorIO.GpuShaderCreator, shaderCode: str) -> None
'''
    ...
    def addToHelperShaderCode (self, *args, **kwargs):
      '''addToHelperShaderCode(self: PyOpenColorIO.GpuShaderCreator, shaderCode: str) -> None
'''
    ...
    def begin (self, *args, **kwargs):
      '''begin(self: PyOpenColorIO.GpuShaderCreator, uid: str) -> None
'''
    ...
    def clone (self, *args, **kwargs):
      '''clone(self: PyOpenColorIO.GpuShaderDesc) -> PyOpenColorIO.GpuShaderCreator
'''
    ...
    def createShaderText (self, *args, **kwargs):
      '''createShaderText(self: PyOpenColorIO.GpuShaderCreator, shaderDeclarations: str, shaderHelperMethods: str, shaderFunctionHeader: str, shaderFunctionBody: str, shaderFunctionFooter: str) -> None
'''
    ...
    def end (self, *args, **kwargs):
      '''end(self: PyOpenColorIO.GpuShaderCreator) -> None
'''
    ...
    def finalize (self, *args, **kwargs):
      '''finalize(self: PyOpenColorIO.GpuShaderCreator) -> None
'''
    ...
    def get3DTextures (self, *args, **kwargs):
      '''get3DTextures(self: PyOpenColorIO.GpuShaderDesc) -> PyOpenColorIO.GpuShaderDesc.Texture3DIterator
'''
    ...
    def getCacheID (self, *args, **kwargs):
      '''getCacheID(self: PyOpenColorIO.GpuShaderCreator) -> str
'''
    ...
    def getDynamicProperties (self, *args, **kwargs):
      '''getDynamicProperties(self: PyOpenColorIO.GpuShaderCreator) -> PyOpenColorIO.GpuShaderCreator.DynamicPropertyIterator
'''
    ...
    def getDynamicProperty (self, *args, **kwargs):
      '''getDynamicProperty(self: PyOpenColorIO.GpuShaderCreator, type: PyOpenColorIO.DynamicPropertyType) -> PyOpenColorIO.DynamicProperty
'''
    ...
    def getFunctionName (self, *args, **kwargs):
      '''getFunctionName(self: PyOpenColorIO.GpuShaderCreator) -> str
'''
    ...
    def getLanguage (self, *args, **kwargs):
      '''getLanguage(self: PyOpenColorIO.GpuShaderCreator) -> PyOpenColorIO.GpuLanguage
'''
    ...
    def getNextResourceIndex (self, *args, **kwargs):
      '''getNextResourceIndex(self: PyOpenColorIO.GpuShaderCreator) -> int
'''
    ...
    def getPixelName (self, *args, **kwargs):
      '''getPixelName(self: PyOpenColorIO.GpuShaderCreator) -> str
'''
    ...
    def getResourcePrefix (self, *args, **kwargs):
      '''getResourcePrefix(self: PyOpenColorIO.GpuShaderCreator) -> str
'''
    ...
    def getShaderText (self, *args, **kwargs):
      '''getShaderText(self: PyOpenColorIO.GpuShaderDesc) -> str
'''
    ...
    def getTextureMaxWidth (self, *args, **kwargs):
      '''getTextureMaxWidth(self: PyOpenColorIO.GpuShaderCreator) -> int
'''
    ...
    def getTextures (self, *args, **kwargs):
      '''getTextures(self: PyOpenColorIO.GpuShaderDesc) -> PyOpenColorIO.GpuShaderDesc.TextureIterator
'''
    ...
    def getUniforms (self, *args, **kwargs):
      '''getUniforms(self: PyOpenColorIO.GpuShaderDesc) -> PyOpenColorIO.GpuShaderDesc.UniformIterator
'''
    ...
    def getUniqueID (self, *args, **kwargs):
      '''getUniqueID(self: PyOpenColorIO.GpuShaderCreator) -> str
'''
    ...
    def hasDynamicProperty (self, *args, **kwargs):
      '''hasDynamicProperty(self: PyOpenColorIO.GpuShaderCreator, type: PyOpenColorIO.DynamicPropertyType) -> bool
'''
    ...
    def setFunctionName (self, *args, **kwargs):
      '''setFunctionName(self: PyOpenColorIO.GpuShaderCreator, name: str) -> None
'''
    ...
    def setLanguage (self, *args, **kwargs):
      '''setLanguage(self: PyOpenColorIO.GpuShaderCreator, language: PyOpenColorIO.GpuLanguage) -> None
'''
    ...
    def setPixelName (self, *args, **kwargs):
      '''setPixelName(self: PyOpenColorIO.GpuShaderCreator, name: str) -> None
'''
    ...
    def setResourcePrefix (self, *args, **kwargs):
      '''setResourcePrefix(self: PyOpenColorIO.GpuShaderCreator, prefix: str) -> None
'''
    ...
    def setTextureMaxWidth (self, *args, **kwargs):
      '''setTextureMaxWidth(self: PyOpenColorIO.GpuShaderCreator, maxWidth: int) -> None
'''
    ...
    def setUniqueID (self, *args, **kwargs):
      '''setUniqueID(self: PyOpenColorIO.GpuShaderCreator, uid: str) -> None
'''
    ...

def GradingBSplineCurve (*args):
      '''

'''      
    ...

class GradingBSplineCurve:
    def GradingControlPointIterator (self, *args, **kwargs):
      '''None'''
    ...
    def getControlPoints (self, *args, **kwargs):
      '''getControlPoints(self: PyOpenColorIO.GradingBSplineCurve) -> PyOpenColorIO.GradingBSplineCurve.GradingControlPointIterator
'''
    ...
    def setNumControlPoints (self, *args, **kwargs):
      '''setNumControlPoints(self: PyOpenColorIO.GradingBSplineCurve, size: int) -> None
'''
    ...
    def validate (self, *args, **kwargs):
      '''validate(self: PyOpenColorIO.GradingBSplineCurve) -> None
'''
    ...

def GradingControlPoint (*args):
      '''

'''      
    ...

class GradingControlPoint:
    def x (self, *args, **kwargs):
      ''''''
    ...
    def y (self, *args, **kwargs):
      ''''''
    ...

def GradingPrimary (*args):
      '''

'''      
    ...

class GradingPrimary:
    def NoClampBlack (self, *args, **kwargs):
      '''Convert a string or number to a floating point number, if possible.'''
    ...
    def NoClampWhite (self, *args, **kwargs):
      '''Convert a string or number to a floating point number, if possible.'''
    ...
    def brightness (self, *args, **kwargs):
      ''''''
    ...
    def clampBlack (self, *args, **kwargs):
      ''''''
    ...
    def clampWhite (self, *args, **kwargs):
      ''''''
    ...
    def contrast (self, *args, **kwargs):
      ''''''
    ...
    def exposure (self, *args, **kwargs):
      ''''''
    ...
    def gain (self, *args, **kwargs):
      ''''''
    ...
    def gamma (self, *args, **kwargs):
      ''''''
    ...
    def lift (self, *args, **kwargs):
      ''''''
    ...
    def offset (self, *args, **kwargs):
      ''''''
    ...
    def pivot (self, *args, **kwargs):
      ''''''
    ...
    def pivotBlack (self, *args, **kwargs):
      ''''''
    ...
    def pivotWhite (self, *args, **kwargs):
      ''''''
    ...
    def saturation (self, *args, **kwargs):
      ''''''
    ...
    def validate (self, *args, **kwargs):
      '''validate(self: PyOpenColorIO.GradingPrimary, arg0: PyOpenColorIO.GradingStyle) -> None
'''
    ...

def GradingPrimaryTransform (*args):
      '''

'''      
    ...

class GradingPrimaryTransform:
    def getDirection (self, *args, **kwargs):
      '''getDirection(self: PyOpenColorIO.Transform) -> PyOpenColorIO.TransformDirection
'''
    ...
    def getFormatMetadata (self, *args, **kwargs):
      '''getFormatMetadata(self: PyOpenColorIO.GradingPrimaryTransform) -> PyOpenColorIO.FormatMetadata
'''
    ...
    def getStyle (self, *args, **kwargs):
      '''getStyle(self: PyOpenColorIO.GradingPrimaryTransform) -> PyOpenColorIO.GradingStyle
'''
    ...
    def getTransformType (self, *args, **kwargs):
      '''getTransformType(self: PyOpenColorIO.Transform) -> PyOpenColorIO.TransformType
'''
    ...
    def getValue (self, *args, **kwargs):
      '''getValue(self: PyOpenColorIO.GradingPrimaryTransform) -> PyOpenColorIO.GradingPrimary
'''
    ...
    def isDynamic (self, *args, **kwargs):
      '''isDynamic(self: PyOpenColorIO.GradingPrimaryTransform) -> bool
'''
    ...
    def makeDynamic (self, *args, **kwargs):
      '''makeDynamic(self: PyOpenColorIO.GradingPrimaryTransform) -> None
'''
    ...
    def makeNonDynamic (self, *args, **kwargs):
      '''makeNonDynamic(self: PyOpenColorIO.GradingPrimaryTransform) -> None
'''
    ...
    def setDirection (self, *args, **kwargs):
      '''setDirection(self: PyOpenColorIO.Transform, direction: PyOpenColorIO.TransformDirection) -> None
'''
    ...
    def setStyle (self, *args, **kwargs):
      '''setStyle(self: PyOpenColorIO.GradingPrimaryTransform, style: PyOpenColorIO.GradingStyle) -> None
'''
    ...
    def setValue (self, *args, **kwargs):
      '''setValue(self: PyOpenColorIO.GradingPrimaryTransform, values: PyOpenColorIO.GradingPrimary) -> None
'''
    ...
    def validate (self, *args, **kwargs):
      '''validate(self: PyOpenColorIO.Transform) -> None
'''
    ...

def GradingRGBCurve (*args):
      '''

'''      
    ...

class GradingRGBCurve:
    def blue (self, *args, **kwargs):
      ''''''
    ...
    def green (self, *args, **kwargs):
      ''''''
    ...
    def master (self, *args, **kwargs):
      ''''''
    ...
    def red (self, *args, **kwargs):
      ''''''
    ...

def GradingRGBCurveTransform (*args):
      '''

'''      
    ...

class GradingRGBCurveTransform:
    def getBypassLinToLog (self, *args, **kwargs):
      '''getBypassLinToLog(self: PyOpenColorIO.GradingRGBCurveTransform) -> bool
'''
    ...
    def getDirection (self, *args, **kwargs):
      '''getDirection(self: PyOpenColorIO.Transform) -> PyOpenColorIO.TransformDirection
'''
    ...
    def getFormatMetadata (self, *args, **kwargs):
      '''getFormatMetadata(self: PyOpenColorIO.GradingRGBCurveTransform) -> PyOpenColorIO.FormatMetadata
'''
    ...
    def getSlope (self, *args, **kwargs):
      '''getSlope(self: PyOpenColorIO.GradingRGBCurveTransform, channel: PyOpenColorIO.RGBCurveType, index: int) -> float
'''
    ...
    def getStyle (self, *args, **kwargs):
      '''getStyle(self: PyOpenColorIO.GradingRGBCurveTransform) -> PyOpenColorIO.GradingStyle
'''
    ...
    def getTransformType (self, *args, **kwargs):
      '''getTransformType(self: PyOpenColorIO.Transform) -> PyOpenColorIO.TransformType
'''
    ...
    def getValue (self, *args, **kwargs):
      '''getValue(self: PyOpenColorIO.GradingRGBCurveTransform) -> PyOpenColorIO.GradingRGBCurve
'''
    ...
    def isDynamic (self, *args, **kwargs):
      '''isDynamic(self: PyOpenColorIO.GradingRGBCurveTransform) -> bool
'''
    ...
    def makeDynamic (self, *args, **kwargs):
      '''makeDynamic(self: PyOpenColorIO.GradingRGBCurveTransform) -> None
'''
    ...
    def makeNonDynamic (self, *args, **kwargs):
      '''makeNonDynamic(self: PyOpenColorIO.GradingRGBCurveTransform) -> None
'''
    ...
    def setBypassLinToLog (self, *args, **kwargs):
      '''setBypassLinToLog(self: PyOpenColorIO.GradingRGBCurveTransform, bypass: bool) -> None
'''
    ...
    def setDirection (self, *args, **kwargs):
      '''setDirection(self: PyOpenColorIO.Transform, direction: PyOpenColorIO.TransformDirection) -> None
'''
    ...
    def setSlope (self, *args, **kwargs):
      '''setSlope(self: PyOpenColorIO.GradingRGBCurveTransform, channel: PyOpenColorIO.RGBCurveType, index: int, slope: float) -> None
'''
    ...
    def setStyle (self, *args, **kwargs):
      '''setStyle(self: PyOpenColorIO.GradingRGBCurveTransform, style: PyOpenColorIO.GradingStyle) -> None
'''
    ...
    def setValue (self, *args, **kwargs):
      '''setValue(self: PyOpenColorIO.GradingRGBCurveTransform, values: PyOpenColorIO.GradingRGBCurve) -> None
'''
    ...
    def slopesAreDefault (self, *args, **kwargs):
      '''slopesAreDefault(self: PyOpenColorIO.GradingRGBCurveTransform, channel: PyOpenColorIO.RGBCurveType) -> bool
'''
    ...
    def validate (self, *args, **kwargs):
      '''validate(self: PyOpenColorIO.Transform) -> None
'''
    ...

def GradingRGBM (*args):
      '''

'''      
    ...

class GradingRGBM:
    def blue (self, *args, **kwargs):
      ''''''
    ...
    def green (self, *args, **kwargs):
      ''''''
    ...
    def master (self, *args, **kwargs):
      ''''''
    ...
    def red (self, *args, **kwargs):
      ''''''
    ...

def GradingRGBMSW (*args):
      '''

'''      
    ...

class GradingRGBMSW:
    def blue (self, *args, **kwargs):
      ''''''
    ...
    def green (self, *args, **kwargs):
      ''''''
    ...
    def master (self, *args, **kwargs):
      ''''''
    ...
    def red (self, *args, **kwargs):
      ''''''
    ...
    def start (self, *args, **kwargs):
      ''''''
    ...
    def width (self, *args, **kwargs):
      ''''''
    ...

def GradingStyle (*args):
      '''

'''      
    ...

class GradingStyle:
    def GRADING_LIN (self, *args, **kwargs):
      '''

Members:

  GRADING_LOG : 

  GRADING_LIN : 

  GRADING_VIDEO : '''
    ...
    def GRADING_LOG (self, *args, **kwargs):
      '''

Members:

  GRADING_LOG : 

  GRADING_LIN : 

  GRADING_VIDEO : '''
    ...
    def GRADING_VIDEO (self, *args, **kwargs):
      '''

Members:

  GRADING_LOG : 

  GRADING_LIN : 

  GRADING_VIDEO : '''
    ...
    def name (self, *args, **kwargs):
      '''name(self: handle) -> str
'''
    ...
    def value (self, *args, **kwargs):
      ''''''
    ...

def GradingStyleFromString (*args):
      '''

'''      
    ...

def GradingStyleToString (*args):
      '''

'''      
    ...

def GradingTone (*args):
      '''

'''      
    ...

class GradingTone:
    def blacks (self, *args, **kwargs):
      ''''''
    ...
    def highlights (self, *args, **kwargs):
      ''''''
    ...
    def midtones (self, *args, **kwargs):
      ''''''
    ...
    def scontrast (self, *args, **kwargs):
      ''''''
    ...
    def shadows (self, *args, **kwargs):
      ''''''
    ...
    def validate (self, *args, **kwargs):
      '''validate(self: PyOpenColorIO.GradingTone) -> None
'''
    ...
    def whites (self, *args, **kwargs):
      ''''''
    ...

def GradingToneTransform (*args):
      '''

'''      
    ...

class GradingToneTransform:
    def getDirection (self, *args, **kwargs):
      '''getDirection(self: PyOpenColorIO.Transform) -> PyOpenColorIO.TransformDirection
'''
    ...
    def getFormatMetadata (self, *args, **kwargs):
      '''getFormatMetadata(self: PyOpenColorIO.GradingToneTransform) -> PyOpenColorIO.FormatMetadata
'''
    ...
    def getStyle (self, *args, **kwargs):
      '''getStyle(self: PyOpenColorIO.GradingToneTransform) -> PyOpenColorIO.GradingStyle
'''
    ...
    def getTransformType (self, *args, **kwargs):
      '''getTransformType(self: PyOpenColorIO.Transform) -> PyOpenColorIO.TransformType
'''
    ...
    def getValue (self, *args, **kwargs):
      '''getValue(self: PyOpenColorIO.GradingToneTransform) -> PyOpenColorIO.GradingTone
'''
    ...
    def isDynamic (self, *args, **kwargs):
      '''isDynamic(self: PyOpenColorIO.GradingToneTransform) -> bool
'''
    ...
    def makeDynamic (self, *args, **kwargs):
      '''makeDynamic(self: PyOpenColorIO.GradingToneTransform) -> None
'''
    ...
    def makeNonDynamic (self, *args, **kwargs):
      '''makeNonDynamic(self: PyOpenColorIO.GradingToneTransform) -> None
'''
    ...
    def setDirection (self, *args, **kwargs):
      '''setDirection(self: PyOpenColorIO.Transform, direction: PyOpenColorIO.TransformDirection) -> None
'''
    ...
    def setStyle (self, *args, **kwargs):
      '''setStyle(self: PyOpenColorIO.GradingToneTransform, style: PyOpenColorIO.GradingStyle) -> None
'''
    ...
    def setValue (self, *args, **kwargs):
      '''setValue(self: PyOpenColorIO.GradingToneTransform, values: PyOpenColorIO.GradingTone) -> None
'''
    ...
    def validate (self, *args, **kwargs):
      '''validate(self: PyOpenColorIO.Transform) -> None
'''
    ...

def GroupTransform (*args):
      '''

'''      
    ...

class GroupTransform:
    def GetWriteFormats (self, *args, **kwargs):
      '''GetWriteFormats() -> PyOpenColorIO.GroupTransform.WriteFormatIterator
'''
    ...
    def TransformIterator (self, *args, **kwargs):
      '''None'''
    ...
    def WriteFormatIterator (self, *args, **kwargs):
      '''None'''
    ...
    def appendTransform (self, *args, **kwargs):
      '''appendTransform(self: PyOpenColorIO.GroupTransform, transform: PyOpenColorIO.Transform) -> None
'''
    ...
    def getDirection (self, *args, **kwargs):
      '''getDirection(self: PyOpenColorIO.Transform) -> PyOpenColorIO.TransformDirection
'''
    ...
    def getFormatMetadata (self, *args, **kwargs):
      '''getFormatMetadata(self: PyOpenColorIO.GroupTransform) -> PyOpenColorIO.FormatMetadata
'''
    ...
    def getTransformType (self, *args, **kwargs):
      '''getTransformType(self: PyOpenColorIO.Transform) -> PyOpenColorIO.TransformType
'''
    ...
    def prependTransform (self, *args, **kwargs):
      '''prependTransform(self: PyOpenColorIO.GroupTransform, transform: PyOpenColorIO.Transform) -> None
'''
    ...
    def setDirection (self, *args, **kwargs):
      '''setDirection(self: PyOpenColorIO.Transform, direction: PyOpenColorIO.TransformDirection) -> None
'''
    ...
    def validate (self, *args, **kwargs):
      '''validate(self: PyOpenColorIO.Transform) -> None
'''
    ...
    def write (self, *args, **kwargs):
      '''write(*args, **kwargs)
Overloaded function.

1. write(self: PyOpenColorIO.GroupTransform, formatName: str, fileName: str, config: PyOpenColorIO.Config = None) -> None

2. write(self: PyOpenColorIO.GroupTransform, formatName: str, config: PyOpenColorIO.Config = None) -> str
'''
    ...

def HUE_DW3 (*args):
      '''

'''      
    ...

def HUE_NONE (*args):
      '''

'''      
    ...

def HUE_WYPN (*args):
      '''

'''      
    ...

def INTERP_BEST (*args):
      '''

'''      
    ...

def INTERP_CUBIC (*args):
      '''

'''      
    ...

def INTERP_DEFAULT (*args):
      '''

'''      
    ...

def INTERP_LINEAR (*args):
      '''

'''      
    ...

def INTERP_NEAREST (*args):
      '''

'''      
    ...

def INTERP_TETRAHEDRAL (*args):
      '''

'''      
    ...

def INTERP_UNKNOWN (*args):
      '''

'''      
    ...

def ImageDesc (*args):
      '''

'''      
    ...

class ImageDesc:
    def getBitDepth (self, *args, **kwargs):
      '''getBitDepth(self: PyOpenColorIO.ImageDesc) -> PyOpenColorIO.BitDepth
'''
    ...
    def getHeight (self, *args, **kwargs):
      '''getHeight(self: PyOpenColorIO.ImageDesc) -> int
'''
    ...
    def getWidth (self, *args, **kwargs):
      '''getWidth(self: PyOpenColorIO.ImageDesc) -> int
'''
    ...
    def getXStrideBytes (self, *args, **kwargs):
      '''getXStrideBytes(self: PyOpenColorIO.ImageDesc) -> int
'''
    ...
    def getYStrideBytes (self, *args, **kwargs):
      '''getYStrideBytes(self: PyOpenColorIO.ImageDesc) -> int
'''
    ...
    def isFloat (self, *args, **kwargs):
      '''isFloat(self: PyOpenColorIO.ImageDesc) -> bool
'''
    ...
    def isRGBAPacked (self, *args, **kwargs):
      '''isRGBAPacked(self: PyOpenColorIO.ImageDesc) -> bool
'''
    ...

def Interpolation (*args):
      '''

'''      
    ...

class Interpolation:
    def INTERP_BEST (self, *args, **kwargs):
      '''

Members:

  INTERP_UNKNOWN : 

  INTERP_NEAREST : 

  INTERP_LINEAR : 

  INTERP_TETRAHEDRAL : 

  INTERP_CUBIC : 

  INTERP_DEFAULT : 

  INTERP_BEST : '''
    ...
    def INTERP_CUBIC (self, *args, **kwargs):
      '''

Members:

  INTERP_UNKNOWN : 

  INTERP_NEAREST : 

  INTERP_LINEAR : 

  INTERP_TETRAHEDRAL : 

  INTERP_CUBIC : 

  INTERP_DEFAULT : 

  INTERP_BEST : '''
    ...
    def INTERP_DEFAULT (self, *args, **kwargs):
      '''

Members:

  INTERP_UNKNOWN : 

  INTERP_NEAREST : 

  INTERP_LINEAR : 

  INTERP_TETRAHEDRAL : 

  INTERP_CUBIC : 

  INTERP_DEFAULT : 

  INTERP_BEST : '''
    ...
    def INTERP_LINEAR (self, *args, **kwargs):
      '''

Members:

  INTERP_UNKNOWN : 

  INTERP_NEAREST : 

  INTERP_LINEAR : 

  INTERP_TETRAHEDRAL : 

  INTERP_CUBIC : 

  INTERP_DEFAULT : 

  INTERP_BEST : '''
    ...
    def INTERP_NEAREST (self, *args, **kwargs):
      '''

Members:

  INTERP_UNKNOWN : 

  INTERP_NEAREST : 

  INTERP_LINEAR : 

  INTERP_TETRAHEDRAL : 

  INTERP_CUBIC : 

  INTERP_DEFAULT : 

  INTERP_BEST : '''
    ...
    def INTERP_TETRAHEDRAL (self, *args, **kwargs):
      '''

Members:

  INTERP_UNKNOWN : 

  INTERP_NEAREST : 

  INTERP_LINEAR : 

  INTERP_TETRAHEDRAL : 

  INTERP_CUBIC : 

  INTERP_DEFAULT : 

  INTERP_BEST : '''
    ...
    def INTERP_UNKNOWN (self, *args, **kwargs):
      '''

Members:

  INTERP_UNKNOWN : 

  INTERP_NEAREST : 

  INTERP_LINEAR : 

  INTERP_TETRAHEDRAL : 

  INTERP_CUBIC : 

  INTERP_DEFAULT : 

  INTERP_BEST : '''
    ...
    def name (self, *args, **kwargs):
      '''name(self: handle) -> str
'''
    ...
    def value (self, *args, **kwargs):
      ''''''
    ...

def InterpolationFromString (*args):
      '''

'''      
    ...

def InterpolationToString (*args):
      '''

'''      
    ...

def IsEnvVariablePresent (*args):
      '''

'''      
    ...

def LOGGING_LEVEL_DEBUG (*args):
      '''

'''      
    ...

def LOGGING_LEVEL_INFO (*args):
      '''

'''      
    ...

def LOGGING_LEVEL_NONE (*args):
      '''

'''      
    ...

def LOGGING_LEVEL_UNKNOWN (*args):
      '''

'''      
    ...

def LOGGING_LEVEL_WARNING (*args):
      '''

'''      
    ...

def LegacyViewingPipeline (*args):
      '''

'''      
    ...

class LegacyViewingPipeline:
    def getChannelView (self, *args, **kwargs):
      '''getChannelView(self: PyOpenColorIO.LegacyViewingPipeline) -> PyOpenColorIO.Transform
'''
    ...
    def getColorTimingCC (self, *args, **kwargs):
      '''getColorTimingCC(self: PyOpenColorIO.LegacyViewingPipeline) -> PyOpenColorIO.Transform
'''
    ...
    def getDisplayCC (self, *args, **kwargs):
      '''getDisplayCC(self: PyOpenColorIO.LegacyViewingPipeline) -> PyOpenColorIO.Transform
'''
    ...
    def getDisplayViewTransform (self, *args, **kwargs):
      '''getDisplayViewTransform(self: PyOpenColorIO.LegacyViewingPipeline) -> PyOpenColorIO.DisplayViewTransform
'''
    ...
    def getLinearCC (self, *args, **kwargs):
      '''getLinearCC(self: PyOpenColorIO.LegacyViewingPipeline) -> PyOpenColorIO.Transform
'''
    ...
    def getLooksOverride (self, *args, **kwargs):
      '''getLooksOverride(self: PyOpenColorIO.LegacyViewingPipeline) -> str
'''
    ...
    def getLooksOverrideEnabled (self, *args, **kwargs):
      '''getLooksOverrideEnabled(self: PyOpenColorIO.LegacyViewingPipeline) -> bool
'''
    ...
    def getProcessor (self, *args, **kwargs):
      '''getProcessor(self: PyOpenColorIO.LegacyViewingPipeline, config: PyOpenColorIO.Config, context: PyOpenColorIO.Context = None) -> PyOpenColorIO.Processor
'''
    ...
    def setChannelView (self, *args, **kwargs):
      '''setChannelView(self: PyOpenColorIO.LegacyViewingPipeline, arg0: PyOpenColorIO.Transform) -> None
'''
    ...
    def setColorTimingCC (self, *args, **kwargs):
      '''setColorTimingCC(self: PyOpenColorIO.LegacyViewingPipeline, arg0: PyOpenColorIO.Transform) -> None
'''
    ...
    def setDisplayCC (self, *args, **kwargs):
      '''setDisplayCC(self: PyOpenColorIO.LegacyViewingPipeline, arg0: PyOpenColorIO.Transform) -> None
'''
    ...
    def setDisplayViewTransform (self, *args, **kwargs):
      '''setDisplayViewTransform(self: PyOpenColorIO.LegacyViewingPipeline, arg0: PyOpenColorIO.DisplayViewTransform) -> None
'''
    ...
    def setLinearCC (self, *args, **kwargs):
      '''setLinearCC(self: PyOpenColorIO.LegacyViewingPipeline, arg0: PyOpenColorIO.Transform) -> None
'''
    ...
    def setLooksOverride (self, *args, **kwargs):
      '''setLooksOverride(self: PyOpenColorIO.LegacyViewingPipeline, looks: str) -> None
'''
    ...
    def setLooksOverrideEnabled (self, *args, **kwargs):
      '''setLooksOverrideEnabled(self: PyOpenColorIO.LegacyViewingPipeline, arg0: bool) -> None
'''
    ...

def LogAffineTransform (*args):
      '''

'''      
    ...

class LogAffineTransform:
    def equals (self, *args, **kwargs):
      '''equals(self: PyOpenColorIO.LogAffineTransform, other: PyOpenColorIO.LogAffineTransform) -> bool
'''
    ...
    def getBase (self, *args, **kwargs):
      '''getBase(self: PyOpenColorIO.LogAffineTransform) -> float
'''
    ...
    def getDirection (self, *args, **kwargs):
      '''getDirection(self: PyOpenColorIO.Transform) -> PyOpenColorIO.TransformDirection
'''
    ...
    def getFormatMetadata (self, *args, **kwargs):
      '''getFormatMetadata(self: PyOpenColorIO.LogAffineTransform) -> PyOpenColorIO.FormatMetadata
'''
    ...
    def getLinSideOffsetValue (self, *args, **kwargs):
      '''getLinSideOffsetValue(self: PyOpenColorIO.LogAffineTransform) -> List[float[3]]
'''
    ...
    def getLinSideSlopeValue (self, *args, **kwargs):
      '''getLinSideSlopeValue(self: PyOpenColorIO.LogAffineTransform) -> List[float[3]]
'''
    ...
    def getLogSideOffsetValue (self, *args, **kwargs):
      '''getLogSideOffsetValue(self: PyOpenColorIO.LogAffineTransform) -> List[float[3]]
'''
    ...
    def getLogSideSlopeValue (self, *args, **kwargs):
      '''getLogSideSlopeValue(self: PyOpenColorIO.LogAffineTransform) -> List[float[3]]
'''
    ...
    def getTransformType (self, *args, **kwargs):
      '''getTransformType(self: PyOpenColorIO.Transform) -> PyOpenColorIO.TransformType
'''
    ...
    def setBase (self, *args, **kwargs):
      '''setBase(self: PyOpenColorIO.LogAffineTransform, base: float) -> None
'''
    ...
    def setDirection (self, *args, **kwargs):
      '''setDirection(self: PyOpenColorIO.Transform, direction: PyOpenColorIO.TransformDirection) -> None
'''
    ...
    def setLinSideOffsetValue (self, *args, **kwargs):
      '''setLinSideOffsetValue(self: PyOpenColorIO.LogAffineTransform, values: List[float[3]]) -> None
'''
    ...
    def setLinSideSlopeValue (self, *args, **kwargs):
      '''setLinSideSlopeValue(self: PyOpenColorIO.LogAffineTransform, values: List[float[3]]) -> None
'''
    ...
    def setLogSideOffsetValue (self, *args, **kwargs):
      '''setLogSideOffsetValue(self: PyOpenColorIO.LogAffineTransform, values: List[float[3]]) -> None
'''
    ...
    def setLogSideSlopeValue (self, *args, **kwargs):
      '''setLogSideSlopeValue(self: PyOpenColorIO.LogAffineTransform, values: List[float[3]]) -> None
'''
    ...
    def validate (self, *args, **kwargs):
      '''validate(self: PyOpenColorIO.Transform) -> None
'''
    ...

def LogCameraTransform (*args):
      '''

'''      
    ...

class LogCameraTransform:
    def equals (self, *args, **kwargs):
      '''equals(self: PyOpenColorIO.LogCameraTransform, other: PyOpenColorIO.LogCameraTransform) -> bool
'''
    ...
    def getBase (self, *args, **kwargs):
      '''getBase(self: PyOpenColorIO.LogCameraTransform) -> float
'''
    ...
    def getDirection (self, *args, **kwargs):
      '''getDirection(self: PyOpenColorIO.Transform) -> PyOpenColorIO.TransformDirection
'''
    ...
    def getFormatMetadata (self, *args, **kwargs):
      '''getFormatMetadata(self: PyOpenColorIO.LogCameraTransform) -> PyOpenColorIO.FormatMetadata
'''
    ...
    def getLinSideBreakValue (self, *args, **kwargs):
      '''getLinSideBreakValue(self: PyOpenColorIO.LogCameraTransform) -> List[float[3]]
'''
    ...
    def getLinSideOffsetValue (self, *args, **kwargs):
      '''getLinSideOffsetValue(self: PyOpenColorIO.LogCameraTransform) -> List[float[3]]
'''
    ...
    def getLinSideSlopeValue (self, *args, **kwargs):
      '''getLinSideSlopeValue(self: PyOpenColorIO.LogCameraTransform) -> List[float[3]]
'''
    ...
    def getLinearSlopeValue (self, *args, **kwargs):
      '''getLinearSlopeValue(self: PyOpenColorIO.LogCameraTransform) -> List[float[3]]


Return LinearSlope or 3 qnan values if not defined.

'''
    ...
    def getLogSideOffsetValue (self, *args, **kwargs):
      '''getLogSideOffsetValue(self: PyOpenColorIO.LogCameraTransform) -> List[float[3]]
'''
    ...
    def getLogSideSlopeValue (self, *args, **kwargs):
      '''getLogSideSlopeValue(self: PyOpenColorIO.LogCameraTransform) -> List[float[3]]
'''
    ...
    def getTransformType (self, *args, **kwargs):
      '''getTransformType(self: PyOpenColorIO.Transform) -> PyOpenColorIO.TransformType
'''
    ...
    def isLinearSlopeValueSet (self, *args, **kwargs):
      '''isLinearSlopeValueSet(self: PyOpenColorIO.LogCameraTransform) -> bool
'''
    ...
    def setBase (self, *args, **kwargs):
      '''setBase(self: PyOpenColorIO.LogCameraTransform, base: float) -> None
'''
    ...
    def setDirection (self, *args, **kwargs):
      '''setDirection(self: PyOpenColorIO.Transform, direction: PyOpenColorIO.TransformDirection) -> None
'''
    ...
    def setLinSideBreakValue (self, *args, **kwargs):
      '''setLinSideBreakValue(self: PyOpenColorIO.LogCameraTransform, values: List[float[3]]) -> None
'''
    ...
    def setLinSideOffsetValue (self, *args, **kwargs):
      '''setLinSideOffsetValue(self: PyOpenColorIO.LogCameraTransform, values: List[float[3]]) -> None
'''
    ...
    def setLinSideSlopeValue (self, *args, **kwargs):
      '''setLinSideSlopeValue(self: PyOpenColorIO.LogCameraTransform, values: List[float[3]]) -> None
'''
    ...
    def setLinearSlopeValue (self, *args, **kwargs):
      '''setLinearSlopeValue(self: PyOpenColorIO.LogCameraTransform, values: List[float[3]]) -> None
'''
    ...
    def setLogSideOffsetValue (self, *args, **kwargs):
      '''setLogSideOffsetValue(self: PyOpenColorIO.LogCameraTransform, values: List[float[3]]) -> None
'''
    ...
    def setLogSideSlopeValue (self, *args, **kwargs):
      '''setLogSideSlopeValue(self: PyOpenColorIO.LogCameraTransform, values: List[float[3]]) -> None
'''
    ...
    def unsetLinearSlopeValue (self, *args, **kwargs):
      '''unsetLinearSlopeValue(self: PyOpenColorIO.LogCameraTransform) -> None
'''
    ...
    def validate (self, *args, **kwargs):
      '''validate(self: PyOpenColorIO.Transform) -> None
'''
    ...

def LogMessage (*args):
      '''

'''      
    ...

def LogTransform (*args):
      '''

'''      
    ...

class LogTransform:
    def equals (self, *args, **kwargs):
      '''equals(self: PyOpenColorIO.LogTransform, other: PyOpenColorIO.LogTransform) -> bool
'''
    ...
    def getBase (self, *args, **kwargs):
      '''getBase(self: PyOpenColorIO.LogTransform) -> float
'''
    ...
    def getDirection (self, *args, **kwargs):
      '''getDirection(self: PyOpenColorIO.Transform) -> PyOpenColorIO.TransformDirection
'''
    ...
    def getFormatMetadata (self, *args, **kwargs):
      '''getFormatMetadata(self: PyOpenColorIO.LogTransform) -> PyOpenColorIO.FormatMetadata
'''
    ...
    def getTransformType (self, *args, **kwargs):
      '''getTransformType(self: PyOpenColorIO.Transform) -> PyOpenColorIO.TransformType
'''
    ...
    def setBase (self, *args, **kwargs):
      '''setBase(self: PyOpenColorIO.LogTransform, base: float) -> None
'''
    ...
    def setDirection (self, *args, **kwargs):
      '''setDirection(self: PyOpenColorIO.Transform, direction: PyOpenColorIO.TransformDirection) -> None
'''
    ...
    def validate (self, *args, **kwargs):
      '''validate(self: PyOpenColorIO.Transform) -> None
'''
    ...

def LoggingLevel (*args):
      '''

'''      
    ...

class LoggingLevel:
    def LOGGING_LEVEL_DEBUG (self, *args, **kwargs):
      '''

Members:

  LOGGING_LEVEL_NONE : 

  LOGGING_LEVEL_WARNING : 

  LOGGING_LEVEL_INFO : 

  LOGGING_LEVEL_DEBUG : 

  LOGGING_LEVEL_UNKNOWN : '''
    ...
    def LOGGING_LEVEL_INFO (self, *args, **kwargs):
      '''

Members:

  LOGGING_LEVEL_NONE : 

  LOGGING_LEVEL_WARNING : 

  LOGGING_LEVEL_INFO : 

  LOGGING_LEVEL_DEBUG : 

  LOGGING_LEVEL_UNKNOWN : '''
    ...
    def LOGGING_LEVEL_NONE (self, *args, **kwargs):
      '''

Members:

  LOGGING_LEVEL_NONE : 

  LOGGING_LEVEL_WARNING : 

  LOGGING_LEVEL_INFO : 

  LOGGING_LEVEL_DEBUG : 

  LOGGING_LEVEL_UNKNOWN : '''
    ...
    def LOGGING_LEVEL_UNKNOWN (self, *args, **kwargs):
      '''

Members:

  LOGGING_LEVEL_NONE : 

  LOGGING_LEVEL_WARNING : 

  LOGGING_LEVEL_INFO : 

  LOGGING_LEVEL_DEBUG : 

  LOGGING_LEVEL_UNKNOWN : '''
    ...
    def LOGGING_LEVEL_WARNING (self, *args, **kwargs):
      '''

Members:

  LOGGING_LEVEL_NONE : 

  LOGGING_LEVEL_WARNING : 

  LOGGING_LEVEL_INFO : 

  LOGGING_LEVEL_DEBUG : 

  LOGGING_LEVEL_UNKNOWN : '''
    ...
    def name (self, *args, **kwargs):
      '''name(self: handle) -> str
'''
    ...
    def value (self, *args, **kwargs):
      ''''''
    ...

def LoggingLevelFromString (*args):
      '''

'''      
    ...

def LoggingLevelToString (*args):
      '''

'''      
    ...

def Look (*args):
      '''

'''      
    ...

class Look:
    def getDescription (self, *args, **kwargs):
      '''getDescription(self: PyOpenColorIO.Look) -> str
'''
    ...
    def getInverseTransform (self, *args, **kwargs):
      '''getInverseTransform(self: PyOpenColorIO.Look) -> PyOpenColorIO.Transform
'''
    ...
    def getName (self, *args, **kwargs):
      '''getName(self: PyOpenColorIO.Look) -> str
'''
    ...
    def getProcessSpace (self, *args, **kwargs):
      '''getProcessSpace(self: PyOpenColorIO.Look) -> str
'''
    ...
    def getTransform (self, *args, **kwargs):
      '''getTransform(self: PyOpenColorIO.Look) -> PyOpenColorIO.Transform
'''
    ...
    def setDescription (self, *args, **kwargs):
      '''setDescription(self: PyOpenColorIO.Look, description: str) -> None
'''
    ...
    def setInverseTransform (self, *args, **kwargs):
      '''setInverseTransform(self: PyOpenColorIO.Look, transform: PyOpenColorIO.Transform) -> None
'''
    ...
    def setName (self, *args, **kwargs):
      '''setName(self: PyOpenColorIO.Look, name: str) -> None
'''
    ...
    def setProcessSpace (self, *args, **kwargs):
      '''setProcessSpace(self: PyOpenColorIO.Look, processSpace: str) -> None
'''
    ...
    def setTransform (self, *args, **kwargs):
      '''setTransform(self: PyOpenColorIO.Look, transform: PyOpenColorIO.Transform) -> None
'''
    ...

def LookTransform (*args):
      '''

'''      
    ...

class LookTransform:
    def getDirection (self, *args, **kwargs):
      '''getDirection(self: PyOpenColorIO.Transform) -> PyOpenColorIO.TransformDirection
'''
    ...
    def getDst (self, *args, **kwargs):
      '''getDst(self: PyOpenColorIO.LookTransform) -> str
'''
    ...
    def getLooks (self, *args, **kwargs):
      '''getLooks(self: PyOpenColorIO.LookTransform) -> str
'''
    ...
    def getSkipColorSpaceConversion (self, *args, **kwargs):
      '''getSkipColorSpaceConversion(self: PyOpenColorIO.LookTransform) -> bool
'''
    ...
    def getSrc (self, *args, **kwargs):
      '''getSrc(self: PyOpenColorIO.LookTransform) -> str
'''
    ...
    def getTransformType (self, *args, **kwargs):
      '''getTransformType(self: PyOpenColorIO.Transform) -> PyOpenColorIO.TransformType
'''
    ...
    def setDirection (self, *args, **kwargs):
      '''setDirection(self: PyOpenColorIO.Transform, direction: PyOpenColorIO.TransformDirection) -> None
'''
    ...
    def setDst (self, *args, **kwargs):
      '''setDst(self: PyOpenColorIO.LookTransform, dst: str) -> None
'''
    ...
    def setLooks (self, *args, **kwargs):
      '''setLooks(self: PyOpenColorIO.LookTransform, looks: str) -> None
'''
    ...
    def setSkipColorSpaceConversion (self, *args, **kwargs):
      '''setSkipColorSpaceConversion(self: PyOpenColorIO.LookTransform, skipColorSpaceConversion: bool) -> None
'''
    ...
    def setSrc (self, *args, **kwargs):
      '''setSrc(self: PyOpenColorIO.LookTransform, src: str) -> None
'''
    ...
    def validate (self, *args, **kwargs):
      '''validate(self: PyOpenColorIO.Transform) -> None
'''
    ...

def Lut1DHueAdjust (*args):
      '''

'''      
    ...

class Lut1DHueAdjust:
    def HUE_DW3 (self, *args, **kwargs):
      '''

Members:

  HUE_NONE : 

  HUE_DW3 : 

  HUE_WYPN : '''
    ...
    def HUE_NONE (self, *args, **kwargs):
      '''

Members:

  HUE_NONE : 

  HUE_DW3 : 

  HUE_WYPN : '''
    ...
    def HUE_WYPN (self, *args, **kwargs):
      '''

Members:

  HUE_NONE : 

  HUE_DW3 : 

  HUE_WYPN : '''
    ...
    def name (self, *args, **kwargs):
      '''name(self: handle) -> str
'''
    ...
    def value (self, *args, **kwargs):
      ''''''
    ...

def Lut1DTransform (*args):
      '''

'''      
    ...

class Lut1DTransform:
    def equals (self, *args, **kwargs):
      '''equals(self: PyOpenColorIO.Lut1DTransform, other: PyOpenColorIO.Lut1DTransform) -> bool
'''
    ...
    def getData (self, *args, **kwargs):
      '''getData(self: PyOpenColorIO.Lut1DTransform) -> numpy.ndarray
'''
    ...
    def getDirection (self, *args, **kwargs):
      '''getDirection(self: PyOpenColorIO.Transform) -> PyOpenColorIO.TransformDirection
'''
    ...
    def getFileOutputBitDepth (self, *args, **kwargs):
      '''getFileOutputBitDepth(self: PyOpenColorIO.Lut1DTransform) -> PyOpenColorIO.BitDepth
'''
    ...
    def getFormatMetadata (self, *args, **kwargs):
      '''getFormatMetadata(self: PyOpenColorIO.Lut1DTransform) -> PyOpenColorIO.FormatMetadata
'''
    ...
    def getHueAdjust (self, *args, **kwargs):
      '''getHueAdjust(self: PyOpenColorIO.Lut1DTransform) -> PyOpenColorIO.Lut1DHueAdjust
'''
    ...
    def getInputHalfDomain (self, *args, **kwargs):
      '''getInputHalfDomain(self: PyOpenColorIO.Lut1DTransform) -> bool
'''
    ...
    def getInterpolation (self, *args, **kwargs):
      '''getInterpolation(self: PyOpenColorIO.Lut1DTransform) -> PyOpenColorIO.Interpolation
'''
    ...
    def getLength (self, *args, **kwargs):
      '''getLength(self: PyOpenColorIO.Lut1DTransform) -> int
'''
    ...
    def getOutputRawHalfs (self, *args, **kwargs):
      '''getOutputRawHalfs(self: PyOpenColorIO.Lut1DTransform) -> bool
'''
    ...
    def getTransformType (self, *args, **kwargs):
      '''getTransformType(self: PyOpenColorIO.Transform) -> PyOpenColorIO.TransformType
'''
    ...
    def getValue (self, *args, **kwargs):
      '''getValue(self: PyOpenColorIO.Lut1DTransform, index: int) -> tuple
'''
    ...
    def setData (self, *args, **kwargs):
      '''setData(self: PyOpenColorIO.Lut1DTransform, data: buffer) -> None
'''
    ...
    def setDirection (self, *args, **kwargs):
      '''setDirection(self: PyOpenColorIO.Transform, direction: PyOpenColorIO.TransformDirection) -> None
'''
    ...
    def setFileOutputBitDepth (self, *args, **kwargs):
      '''setFileOutputBitDepth(self: PyOpenColorIO.Lut1DTransform, bitDepth: PyOpenColorIO.BitDepth) -> None
'''
    ...
    def setHueAdjust (self, *args, **kwargs):
      '''setHueAdjust(self: PyOpenColorIO.Lut1DTransform, hueAdjust: PyOpenColorIO.Lut1DHueAdjust) -> None
'''
    ...
    def setInputHalfDomain (self, *args, **kwargs):
      '''setInputHalfDomain(self: PyOpenColorIO.Lut1DTransform, isHalfDomain: bool) -> None
'''
    ...
    def setInterpolation (self, *args, **kwargs):
      '''setInterpolation(self: PyOpenColorIO.Lut1DTransform, interpolation: PyOpenColorIO.Interpolation) -> None
'''
    ...
    def setLength (self, *args, **kwargs):
      '''setLength(self: PyOpenColorIO.Lut1DTransform, length: int) -> None
'''
    ...
    def setOutputRawHalfs (self, *args, **kwargs):
      '''setOutputRawHalfs(self: PyOpenColorIO.Lut1DTransform, isRawHalfs: bool) -> None
'''
    ...
    def setValue (self, *args, **kwargs):
      '''setValue(self: PyOpenColorIO.Lut1DTransform, index: int, r: float, g: float, b: float) -> None
'''
    ...
    def validate (self, *args, **kwargs):
      '''validate(self: PyOpenColorIO.Transform) -> None
'''
    ...

def Lut3DTransform (*args):
      '''

'''      
    ...

class Lut3DTransform:
    def equals (self, *args, **kwargs):
      '''equals(self: PyOpenColorIO.Lut3DTransform, other: PyOpenColorIO.Lut3DTransform) -> bool
'''
    ...
    def getData (self, *args, **kwargs):
      '''getData(self: PyOpenColorIO.Lut3DTransform) -> numpy.ndarray
'''
    ...
    def getDirection (self, *args, **kwargs):
      '''getDirection(self: PyOpenColorIO.Transform) -> PyOpenColorIO.TransformDirection
'''
    ...
    def getFileOutputBitDepth (self, *args, **kwargs):
      '''getFileOutputBitDepth(self: PyOpenColorIO.Lut3DTransform) -> PyOpenColorIO.BitDepth
'''
    ...
    def getFormatMetadata (self, *args, **kwargs):
      '''getFormatMetadata(self: PyOpenColorIO.Lut3DTransform) -> PyOpenColorIO.FormatMetadata
'''
    ...
    def getGridSize (self, *args, **kwargs):
      '''getGridSize(self: PyOpenColorIO.Lut3DTransform) -> int
'''
    ...
    def getInterpolation (self, *args, **kwargs):
      '''getInterpolation(self: PyOpenColorIO.Lut3DTransform) -> PyOpenColorIO.Interpolation
'''
    ...
    def getTransformType (self, *args, **kwargs):
      '''getTransformType(self: PyOpenColorIO.Transform) -> PyOpenColorIO.TransformType
'''
    ...
    def getValue (self, *args, **kwargs):
      '''getValue(self: PyOpenColorIO.Lut3DTransform, indexR: int, indexG: int, indexB: int) -> tuple
'''
    ...
    def setData (self, *args, **kwargs):
      '''setData(self: PyOpenColorIO.Lut3DTransform, data: buffer) -> None
'''
    ...
    def setDirection (self, *args, **kwargs):
      '''setDirection(self: PyOpenColorIO.Transform, direction: PyOpenColorIO.TransformDirection) -> None
'''
    ...
    def setFileOutputBitDepth (self, *args, **kwargs):
      '''setFileOutputBitDepth(self: PyOpenColorIO.Lut3DTransform, bitDepth: PyOpenColorIO.BitDepth) -> None
'''
    ...
    def setGridSize (self, *args, **kwargs):
      '''setGridSize(self: PyOpenColorIO.Lut3DTransform, gridSize: int) -> None
'''
    ...
    def setInterpolation (self, *args, **kwargs):
      '''setInterpolation(self: PyOpenColorIO.Lut3DTransform, interpolation: PyOpenColorIO.Interpolation) -> None
'''
    ...
    def setValue (self, *args, **kwargs):
      '''setValue(self: PyOpenColorIO.Lut3DTransform, indexR: int, indexG: int, indexB: int, r: float, g: float, b: float) -> None
'''
    ...
    def validate (self, *args, **kwargs):
      '''validate(self: PyOpenColorIO.Transform) -> None
'''
    ...

def METADATA_DESCRIPTION (*args):
      '''

'''      
    ...

def METADATA_ID (*args):
      '''

'''      
    ...

def METADATA_INFO (*args):
      '''

'''      
    ...

def METADATA_INPUT_DESCRIPTOR (*args):
      '''

'''      
    ...

def METADATA_NAME (*args):
      '''

'''      
    ...

def METADATA_OUTPUT_DESCRIPTOR (*args):
      '''

'''      
    ...

def MatrixTransform (*args):
      '''

'''      
    ...

class MatrixTransform:
    def Fit (self, *args, **kwargs):
      '''Fit(oldMin: List[float[4]] = [0.0, 0.0, 0.0, 0.0], oldMax: List[float[4]] = [1.0, 1.0, 1.0, 1.0], newMin: List[float[4]] = [0.0, 0.0, 0.0, 0.0], newMax: List[float[4]] = [1.0, 1.0, 1.0, 1.0]) -> PyOpenColorIO.MatrixTransform
'''
    ...
    def Identity (self, *args, **kwargs):
      '''Identity() -> PyOpenColorIO.MatrixTransform
'''
    ...
    def Sat (self, *args, **kwargs):
      '''Sat(sat: float, lumaCoef: List[float[3]]) -> PyOpenColorIO.MatrixTransform
'''
    ...
    def Scale (self, *args, **kwargs):
      '''Scale(scale: List[float[4]]) -> PyOpenColorIO.MatrixTransform
'''
    ...
    def View (self, *args, **kwargs):
      '''View(channelHot: List[int[4]], lumaCoef: List[float[3]]) -> PyOpenColorIO.MatrixTransform
'''
    ...
    def equals (self, *args, **kwargs):
      '''equals(self: PyOpenColorIO.MatrixTransform, other: PyOpenColorIO.MatrixTransform) -> bool
'''
    ...
    def getDirection (self, *args, **kwargs):
      '''getDirection(self: PyOpenColorIO.Transform) -> PyOpenColorIO.TransformDirection
'''
    ...
    def getFileInputBitDepth (self, *args, **kwargs):
      '''getFileInputBitDepth(self: PyOpenColorIO.MatrixTransform) -> PyOpenColorIO.BitDepth
'''
    ...
    def getFileOutputBitDepth (self, *args, **kwargs):
      '''getFileOutputBitDepth(self: PyOpenColorIO.MatrixTransform) -> PyOpenColorIO.BitDepth
'''
    ...
    def getFormatMetadata (self, *args, **kwargs):
      '''getFormatMetadata(self: PyOpenColorIO.MatrixTransform) -> PyOpenColorIO.FormatMetadata
'''
    ...
    def getMatrix (self, *args, **kwargs):
      '''getMatrix(self: PyOpenColorIO.MatrixTransform) -> List[float[16]]
'''
    ...
    def getOffset (self, *args, **kwargs):
      '''getOffset(self: PyOpenColorIO.MatrixTransform) -> List[float[4]]
'''
    ...
    def getTransformType (self, *args, **kwargs):
      '''getTransformType(self: PyOpenColorIO.Transform) -> PyOpenColorIO.TransformType
'''
    ...
    def setDirection (self, *args, **kwargs):
      '''setDirection(self: PyOpenColorIO.Transform, direction: PyOpenColorIO.TransformDirection) -> None
'''
    ...
    def setFileInputBitDepth (self, *args, **kwargs):
      '''setFileInputBitDepth(self: PyOpenColorIO.MatrixTransform, bitDepth: PyOpenColorIO.BitDepth) -> None
'''
    ...
    def setFileOutputBitDepth (self, *args, **kwargs):
      '''setFileOutputBitDepth(self: PyOpenColorIO.MatrixTransform, bitDepth: PyOpenColorIO.BitDepth) -> None
'''
    ...
    def setMatrix (self, *args, **kwargs):
      '''setMatrix(self: PyOpenColorIO.MatrixTransform, matrix: List[float[16]]) -> None
'''
    ...
    def setOffset (self, *args, **kwargs):
      '''setOffset(self: PyOpenColorIO.MatrixTransform, offset: List[float[4]]) -> None
'''
    ...
    def validate (self, *args, **kwargs):
      '''validate(self: PyOpenColorIO.Transform) -> None
'''
    ...

def MixingColorSpaceManager (*args):
      '''

'''      
    ...

class MixingColorSpaceManager:
    def MixingEncodingIterator (self, *args, **kwargs):
      '''None'''
    ...
    def MixingSpaceIterator (self, *args, **kwargs):
      '''None'''
    ...
    def getMixingEncodings (self, *args, **kwargs):
      '''getMixingEncodings(self: PyOpenColorIO.MixingColorSpaceManager) -> PyOpenColorIO.MixingColorSpaceManager.MixingEncodingIterator
'''
    ...
    def getMixingSpaces (self, *args, **kwargs):
      '''getMixingSpaces(self: PyOpenColorIO.MixingColorSpaceManager) -> PyOpenColorIO.MixingColorSpaceManager.MixingSpaceIterator
'''
    ...
    def getProcessor (self, *args, **kwargs):
      '''getProcessor(self: PyOpenColorIO.MixingColorSpaceManager, workingSpaceName: str, displayName: str, viewName: str, direction: PyOpenColorIO.TransformDirection = <TransformDirection.TRANSFORM_DIR_FORWARD: 0>) -> PyOpenColorIO.Processor
'''
    ...
    def getSelectedMixingEncodingIdx (self, *args, **kwargs):
      '''getSelectedMixingEncodingIdx(self: PyOpenColorIO.MixingColorSpaceManager) -> int
'''
    ...
    def getSelectedMixingSpaceIdx (self, *args, **kwargs):
      '''getSelectedMixingSpaceIdx(self: PyOpenColorIO.MixingColorSpaceManager) -> int
'''
    ...
    def getSlider (self, *args, **kwargs):
      '''getSlider(*args, **kwargs)
Overloaded function.

1. getSlider(self: PyOpenColorIO.MixingColorSpaceManager) -> PyOpenColorIO.MixingSlider

2. getSlider(self: PyOpenColorIO.MixingColorSpaceManager, sliderMixingMinEdge: float, sliderMixingMaxEdge: float) -> PyOpenColorIO.MixingSlider
'''
    ...
    def isPerceptuallyUniform (self, *args, **kwargs):
      '''isPerceptuallyUniform(self: PyOpenColorIO.MixingColorSpaceManager) -> bool
'''
    ...
    def refresh (self, *args, **kwargs):
      '''refresh(self: PyOpenColorIO.MixingColorSpaceManager, config: PyOpenColorIO.Config) -> None
'''
    ...
    def setSelectedMixingEncoding (self, *args, **kwargs):
      '''setSelectedMixingEncoding(self: PyOpenColorIO.MixingColorSpaceManager, mixingEncoding: str) -> None
'''
    ...
    def setSelectedMixingEncodingIdx (self, *args, **kwargs):
      '''setSelectedMixingEncodingIdx(self: PyOpenColorIO.MixingColorSpaceManager, arg0: int) -> None
'''
    ...
    def setSelectedMixingSpace (self, *args, **kwargs):
      '''setSelectedMixingSpace(self: PyOpenColorIO.MixingColorSpaceManager, mixingSpace: str) -> None
'''
    ...
    def setSelectedMixingSpaceIdx (self, *args, **kwargs):
      '''setSelectedMixingSpaceIdx(self: PyOpenColorIO.MixingColorSpaceManager, arg0: int) -> None
'''
    ...

def MixingSlider (*args):
      '''

'''      
    ...

class MixingSlider:
    def getSliderMaxEdge (self, *args, **kwargs):
      '''getSliderMaxEdge(self: PyOpenColorIO.MixingSlider) -> float
'''
    ...
    def getSliderMinEdge (self, *args, **kwargs):
      '''getSliderMinEdge(self: PyOpenColorIO.MixingSlider) -> float
'''
    ...
    def mixingToSlider (self, *args, **kwargs):
      '''mixingToSlider(self: PyOpenColorIO.MixingSlider, mixingUnits: float) -> float
'''
    ...
    def setSliderMaxEdge (self, *args, **kwargs):
      '''setSliderMaxEdge(self: PyOpenColorIO.MixingSlider, arg0: float) -> None
'''
    ...
    def setSliderMinEdge (self, *args, **kwargs):
      '''setSliderMinEdge(self: PyOpenColorIO.MixingSlider, arg0: float) -> None
'''
    ...
    def sliderToMixing (self, *args, **kwargs):
      '''sliderToMixing(self: PyOpenColorIO.MixingSlider, sliderUnits: float) -> float
'''
    ...

def NAMEDTRANSFORM_ACTIVE (*args):
      '''

'''      
    ...

def NAMEDTRANSFORM_ALL (*args):
      '''

'''      
    ...

def NAMEDTRANSFORM_INACTIVE (*args):
      '''

'''      
    ...

def NEGATIVE_CLAMP (*args):
      '''

'''      
    ...

def NEGATIVE_LINEAR (*args):
      '''

'''      
    ...

def NEGATIVE_MIRROR (*args):
      '''

'''      
    ...

def NEGATIVE_PASS_THRU (*args):
      '''

'''      
    ...

def NamedTransform (*args):
      '''

'''      
    ...

class NamedTransform:
    def GetTransform (self, *args, **kwargs):
      '''GetTransform(transform: PyOpenColorIO.NamedTransform, direction: PyOpenColorIO.TransformDirection) -> PyOpenColorIO.Transform
'''
    ...
    def NamedTransformAliasIterator (self, *args, **kwargs):
      '''None'''
    ...
    def NamedTransformCategoryIterator (self, *args, **kwargs):
      '''None'''
    ...
    def addAlias (self, *args, **kwargs):
      '''addAlias(self: PyOpenColorIO.NamedTransform, alias: str) -> None
'''
    ...
    def addCategory (self, *args, **kwargs):
      '''addCategory(self: PyOpenColorIO.NamedTransform, category: str) -> None
'''
    ...
    def clearAliases (self, *args, **kwargs):
      '''clearAliases(self: PyOpenColorIO.NamedTransform) -> None
'''
    ...
    def clearCategories (self, *args, **kwargs):
      '''clearCategories(self: PyOpenColorIO.NamedTransform) -> None
'''
    ...
    def getAliases (self, *args, **kwargs):
      '''getAliases(self: PyOpenColorIO.NamedTransform) -> PyOpenColorIO.NamedTransform.NamedTransformAliasIterator
'''
    ...
    def getCategories (self, *args, **kwargs):
      '''getCategories(self: PyOpenColorIO.NamedTransform) -> PyOpenColorIO.NamedTransform.NamedTransformCategoryIterator
'''
    ...
    def getDescription (self, *args, **kwargs):
      '''getDescription(self: PyOpenColorIO.NamedTransform) -> str
'''
    ...
    def getEncoding (self, *args, **kwargs):
      '''getEncoding(self: PyOpenColorIO.NamedTransform) -> str
'''
    ...
    def getFamily (self, *args, **kwargs):
      '''getFamily(self: PyOpenColorIO.NamedTransform) -> str
'''
    ...
    def getName (self, *args, **kwargs):
      '''getName(self: PyOpenColorIO.NamedTransform) -> str
'''
    ...
    def getTransform (self, *args, **kwargs):
      '''getTransform(self: PyOpenColorIO.NamedTransform, direction: PyOpenColorIO.TransformDirection) -> PyOpenColorIO.Transform
'''
    ...
    def hasCategory (self, *args, **kwargs):
      '''hasCategory(self: PyOpenColorIO.NamedTransform, category: str) -> bool
'''
    ...
    def removeAlias (self, *args, **kwargs):
      '''removeAlias(self: PyOpenColorIO.NamedTransform, alias: str) -> None
'''
    ...
    def removeCategory (self, *args, **kwargs):
      '''removeCategory(self: PyOpenColorIO.NamedTransform, category: str) -> None
'''
    ...
    def setDescription (self, *args, **kwargs):
      '''setDescription(self: PyOpenColorIO.NamedTransform, description: str) -> None
'''
    ...
    def setEncoding (self, *args, **kwargs):
      '''setEncoding(self: PyOpenColorIO.NamedTransform, encoding: str) -> None
'''
    ...
    def setFamily (self, *args, **kwargs):
      '''setFamily(self: PyOpenColorIO.NamedTransform, family: str) -> None
'''
    ...
    def setName (self, *args, **kwargs):
      '''setName(self: PyOpenColorIO.NamedTransform, name: str) -> None
'''
    ...
    def setTransform (self, *args, **kwargs):
      '''setTransform(self: PyOpenColorIO.NamedTransform, transform: PyOpenColorIO.Transform, direction: PyOpenColorIO.TransformDirection) -> None
'''
    ...

def NamedTransformVisibility (*args):
      '''

'''      
    ...

class NamedTransformVisibility:
    def NAMEDTRANSFORM_ACTIVE (self, *args, **kwargs):
      '''

Members:

  NAMEDTRANSFORM_ACTIVE : 

  NAMEDTRANSFORM_INACTIVE : 

  NAMEDTRANSFORM_ALL : '''
    ...
    def NAMEDTRANSFORM_ALL (self, *args, **kwargs):
      '''

Members:

  NAMEDTRANSFORM_ACTIVE : 

  NAMEDTRANSFORM_INACTIVE : 

  NAMEDTRANSFORM_ALL : '''
    ...
    def NAMEDTRANSFORM_INACTIVE (self, *args, **kwargs):
      '''

Members:

  NAMEDTRANSFORM_ACTIVE : 

  NAMEDTRANSFORM_INACTIVE : 

  NAMEDTRANSFORM_ALL : '''
    ...
    def name (self, *args, **kwargs):
      '''name(self: handle) -> str
'''
    ...
    def value (self, *args, **kwargs):
      ''''''
    ...

def NegativeStyle (*args):
      '''

'''      
    ...

class NegativeStyle:
    def NEGATIVE_CLAMP (self, *args, **kwargs):
      '''

Members:

  NEGATIVE_CLAMP : 

  NEGATIVE_MIRROR : 

  NEGATIVE_PASS_THRU : 

  NEGATIVE_LINEAR : '''
    ...
    def NEGATIVE_LINEAR (self, *args, **kwargs):
      '''

Members:

  NEGATIVE_CLAMP : 

  NEGATIVE_MIRROR : 

  NEGATIVE_PASS_THRU : 

  NEGATIVE_LINEAR : '''
    ...
    def NEGATIVE_MIRROR (self, *args, **kwargs):
      '''

Members:

  NEGATIVE_CLAMP : 

  NEGATIVE_MIRROR : 

  NEGATIVE_PASS_THRU : 

  NEGATIVE_LINEAR : '''
    ...
    def NEGATIVE_PASS_THRU (self, *args, **kwargs):
      '''

Members:

  NEGATIVE_CLAMP : 

  NEGATIVE_MIRROR : 

  NEGATIVE_PASS_THRU : 

  NEGATIVE_LINEAR : '''
    ...
    def name (self, *args, **kwargs):
      '''name(self: handle) -> str
'''
    ...
    def value (self, *args, **kwargs):
      ''''''
    ...

def NegativeStyleFromString (*args):
      '''

'''      
    ...

def NegativeStyleToString (*args):
      '''

'''      
    ...

def OCIO_ACTIVE_DISPLAYS_ENVVAR (*args):
      '''

'''      
    ...

def OCIO_ACTIVE_VIEWS_ENVVAR (*args):
      '''

'''      
    ...

def OCIO_CONFIG_ENVVAR (*args):
      '''

'''      
    ...

def OCIO_DISABLE_ALL_CACHES (*args):
      '''

'''      
    ...

def OCIO_DISABLE_CACHE_FALLBACK (*args):
      '''

'''      
    ...

def OCIO_DISABLE_PROCESSOR_CACHES (*args):
      '''

'''      
    ...

def OCIO_INACTIVE_COLORSPACES_ENVVAR (*args):
      '''

'''      
    ...

def OCIO_OPTIMIZATION_FLAGS_ENVVAR (*args):
      '''

'''      
    ...

def OCIO_USER_CATEGORIES_ENVVAR (*args):
      '''

'''      
    ...

def OCIO_VIEW_USE_DISPLAY_NAME (*args):
      '''

'''      
    ...

def OPTIMIZATION_ALL (*args):
      '''

'''      
    ...

def OPTIMIZATION_COMP_EXPONENT (*args):
      '''

'''      
    ...

def OPTIMIZATION_COMP_GAMMA (*args):
      '''

'''      
    ...

def OPTIMIZATION_COMP_LUT1D (*args):
      '''

'''      
    ...

def OPTIMIZATION_COMP_LUT3D (*args):
      '''

'''      
    ...

def OPTIMIZATION_COMP_MATRIX (*args):
      '''

'''      
    ...

def OPTIMIZATION_COMP_RANGE (*args):
      '''

'''      
    ...

def OPTIMIZATION_COMP_SEPARABLE_PREFIX (*args):
      '''

'''      
    ...

def OPTIMIZATION_DEFAULT (*args):
      '''

'''      
    ...

def OPTIMIZATION_DRAFT (*args):
      '''

'''      
    ...

def OPTIMIZATION_FAST_LOG_EXP_POW (*args):
      '''

'''      
    ...

def OPTIMIZATION_GOOD (*args):
      '''

'''      
    ...

def OPTIMIZATION_IDENTITY (*args):
      '''

'''      
    ...

def OPTIMIZATION_IDENTITY_GAMMA (*args):
      '''

'''      
    ...

def OPTIMIZATION_LOSSLESS (*args):
      '''

'''      
    ...

def OPTIMIZATION_LUT_INV_FAST (*args):
      '''

'''      
    ...

def OPTIMIZATION_NONE (*args):
      '''

'''      
    ...

def OPTIMIZATION_NO_DYNAMIC_PROPERTIES (*args):
      '''

'''      
    ...

def OPTIMIZATION_PAIR_IDENTITY_CDL (*args):
      '''

'''      
    ...

def OPTIMIZATION_PAIR_IDENTITY_EXPOSURE_CONTRAST (*args):
      '''

'''      
    ...

def OPTIMIZATION_PAIR_IDENTITY_FIXED_FUNCTION (*args):
      '''

'''      
    ...

def OPTIMIZATION_PAIR_IDENTITY_GAMMA (*args):
      '''

'''      
    ...

def OPTIMIZATION_PAIR_IDENTITY_GRADING (*args):
      '''

'''      
    ...

def OPTIMIZATION_PAIR_IDENTITY_LOG (*args):
      '''

'''      
    ...

def OPTIMIZATION_PAIR_IDENTITY_LUT1D (*args):
      '''

'''      
    ...

def OPTIMIZATION_PAIR_IDENTITY_LUT3D (*args):
      '''

'''      
    ...

def OPTIMIZATION_SIMPLIFY_OPS (*args):
      '''

'''      
    ...

def OPTIMIZATION_VERY_GOOD (*args):
      '''

'''      
    ...

def OptimizationFlags (*args):
      '''

'''      
    ...

class OptimizationFlags:
    def OPTIMIZATION_ALL (self, *args, **kwargs):
      '''

Members:

  OPTIMIZATION_NONE : 

  OPTIMIZATION_IDENTITY : 

  OPTIMIZATION_IDENTITY_GAMMA : 

  OPTIMIZATION_PAIR_IDENTITY_CDL : 

  OPTIMIZATION_PAIR_IDENTITY_EXPOSURE_CONTRAST : 

  OPTIMIZATION_PAIR_IDENTITY_FIXED_FUNCTION : 

  OPTIMIZATION_PAIR_IDENTITY_GAMMA : 

  OPTIMIZATION_PAIR_IDENTITY_LUT1D : 

  OPTIMIZATION_PAIR_IDENTITY_LUT3D : 

  OPTIMIZATION_PAIR_IDENTITY_LOG : 

  OPTIMIZATION_PAIR_IDENTITY_GRADING : 

  OPTIMIZATION_COMP_EXPONENT : 

  OPTIMIZATION_COMP_GAMMA : 

  OPTIMIZATION_COMP_MATRIX : 

  OPTIMIZATION_COMP_LUT1D : 

  OPTIMIZATION_COMP_LUT3D : 

  OPTIMIZATION_COMP_RANGE : 

  OPTIMIZATION_COMP_SEPARABLE_PREFIX : 

  OPTIMIZATION_LUT_INV_FAST : 

  OPTIMIZATION_FAST_LOG_EXP_POW : 

  OPTIMIZATION_SIMPLIFY_OPS : 

  OPTIMIZATION_NO_DYNAMIC_PROPERTIES : 

  OPTIMIZATION_ALL : 

  OPTIMIZATION_LOSSLESS : 

  OPTIMIZATION_VERY_GOOD : 

  OPTIMIZATION_GOOD : 

  OPTIMIZATION_DRAFT : 

  OPTIMIZATION_DEFAULT : '''
    ...
    def OPTIMIZATION_COMP_EXPONENT (self, *args, **kwargs):
      '''

Members:

  OPTIMIZATION_NONE : 

  OPTIMIZATION_IDENTITY : 

  OPTIMIZATION_IDENTITY_GAMMA : 

  OPTIMIZATION_PAIR_IDENTITY_CDL : 

  OPTIMIZATION_PAIR_IDENTITY_EXPOSURE_CONTRAST : 

  OPTIMIZATION_PAIR_IDENTITY_FIXED_FUNCTION : 

  OPTIMIZATION_PAIR_IDENTITY_GAMMA : 

  OPTIMIZATION_PAIR_IDENTITY_LUT1D : 

  OPTIMIZATION_PAIR_IDENTITY_LUT3D : 

  OPTIMIZATION_PAIR_IDENTITY_LOG : 

  OPTIMIZATION_PAIR_IDENTITY_GRADING : 

  OPTIMIZATION_COMP_EXPONENT : 

  OPTIMIZATION_COMP_GAMMA : 

  OPTIMIZATION_COMP_MATRIX : 

  OPTIMIZATION_COMP_LUT1D : 

  OPTIMIZATION_COMP_LUT3D : 

  OPTIMIZATION_COMP_RANGE : 

  OPTIMIZATION_COMP_SEPARABLE_PREFIX : 

  OPTIMIZATION_LUT_INV_FAST : 

  OPTIMIZATION_FAST_LOG_EXP_POW : 

  OPTIMIZATION_SIMPLIFY_OPS : 

  OPTIMIZATION_NO_DYNAMIC_PROPERTIES : 

  OPTIMIZATION_ALL : 

  OPTIMIZATION_LOSSLESS : 

  OPTIMIZATION_VERY_GOOD : 

  OPTIMIZATION_GOOD : 

  OPTIMIZATION_DRAFT : 

  OPTIMIZATION_DEFAULT : '''
    ...
    def OPTIMIZATION_COMP_GAMMA (self, *args, **kwargs):
      '''

Members:

  OPTIMIZATION_NONE : 

  OPTIMIZATION_IDENTITY : 

  OPTIMIZATION_IDENTITY_GAMMA : 

  OPTIMIZATION_PAIR_IDENTITY_CDL : 

  OPTIMIZATION_PAIR_IDENTITY_EXPOSURE_CONTRAST : 

  OPTIMIZATION_PAIR_IDENTITY_FIXED_FUNCTION : 

  OPTIMIZATION_PAIR_IDENTITY_GAMMA : 

  OPTIMIZATION_PAIR_IDENTITY_LUT1D : 

  OPTIMIZATION_PAIR_IDENTITY_LUT3D : 

  OPTIMIZATION_PAIR_IDENTITY_LOG : 

  OPTIMIZATION_PAIR_IDENTITY_GRADING : 

  OPTIMIZATION_COMP_EXPONENT : 

  OPTIMIZATION_COMP_GAMMA : 

  OPTIMIZATION_COMP_MATRIX : 

  OPTIMIZATION_COMP_LUT1D : 

  OPTIMIZATION_COMP_LUT3D : 

  OPTIMIZATION_COMP_RANGE : 

  OPTIMIZATION_COMP_SEPARABLE_PREFIX : 

  OPTIMIZATION_LUT_INV_FAST : 

  OPTIMIZATION_FAST_LOG_EXP_POW : 

  OPTIMIZATION_SIMPLIFY_OPS : 

  OPTIMIZATION_NO_DYNAMIC_PROPERTIES : 

  OPTIMIZATION_ALL : 

  OPTIMIZATION_LOSSLESS : 

  OPTIMIZATION_VERY_GOOD : 

  OPTIMIZATION_GOOD : 

  OPTIMIZATION_DRAFT : 

  OPTIMIZATION_DEFAULT : '''
    ...
    def OPTIMIZATION_COMP_LUT1D (self, *args, **kwargs):
      '''

Members:

  OPTIMIZATION_NONE : 

  OPTIMIZATION_IDENTITY : 

  OPTIMIZATION_IDENTITY_GAMMA : 

  OPTIMIZATION_PAIR_IDENTITY_CDL : 

  OPTIMIZATION_PAIR_IDENTITY_EXPOSURE_CONTRAST : 

  OPTIMIZATION_PAIR_IDENTITY_FIXED_FUNCTION : 

  OPTIMIZATION_PAIR_IDENTITY_GAMMA : 

  OPTIMIZATION_PAIR_IDENTITY_LUT1D : 

  OPTIMIZATION_PAIR_IDENTITY_LUT3D : 

  OPTIMIZATION_PAIR_IDENTITY_LOG : 

  OPTIMIZATION_PAIR_IDENTITY_GRADING : 

  OPTIMIZATION_COMP_EXPONENT : 

  OPTIMIZATION_COMP_GAMMA : 

  OPTIMIZATION_COMP_MATRIX : 

  OPTIMIZATION_COMP_LUT1D : 

  OPTIMIZATION_COMP_LUT3D : 

  OPTIMIZATION_COMP_RANGE : 

  OPTIMIZATION_COMP_SEPARABLE_PREFIX : 

  OPTIMIZATION_LUT_INV_FAST : 

  OPTIMIZATION_FAST_LOG_EXP_POW : 

  OPTIMIZATION_SIMPLIFY_OPS : 

  OPTIMIZATION_NO_DYNAMIC_PROPERTIES : 

  OPTIMIZATION_ALL : 

  OPTIMIZATION_LOSSLESS : 

  OPTIMIZATION_VERY_GOOD : 

  OPTIMIZATION_GOOD : 

  OPTIMIZATION_DRAFT : 

  OPTIMIZATION_DEFAULT : '''
    ...
    def OPTIMIZATION_COMP_LUT3D (self, *args, **kwargs):
      '''

Members:

  OPTIMIZATION_NONE : 

  OPTIMIZATION_IDENTITY : 

  OPTIMIZATION_IDENTITY_GAMMA : 

  OPTIMIZATION_PAIR_IDENTITY_CDL : 

  OPTIMIZATION_PAIR_IDENTITY_EXPOSURE_CONTRAST : 

  OPTIMIZATION_PAIR_IDENTITY_FIXED_FUNCTION : 

  OPTIMIZATION_PAIR_IDENTITY_GAMMA : 

  OPTIMIZATION_PAIR_IDENTITY_LUT1D : 

  OPTIMIZATION_PAIR_IDENTITY_LUT3D : 

  OPTIMIZATION_PAIR_IDENTITY_LOG : 

  OPTIMIZATION_PAIR_IDENTITY_GRADING : 

  OPTIMIZATION_COMP_EXPONENT : 

  OPTIMIZATION_COMP_GAMMA : 

  OPTIMIZATION_COMP_MATRIX : 

  OPTIMIZATION_COMP_LUT1D : 

  OPTIMIZATION_COMP_LUT3D : 

  OPTIMIZATION_COMP_RANGE : 

  OPTIMIZATION_COMP_SEPARABLE_PREFIX : 

  OPTIMIZATION_LUT_INV_FAST : 

  OPTIMIZATION_FAST_LOG_EXP_POW : 

  OPTIMIZATION_SIMPLIFY_OPS : 

  OPTIMIZATION_NO_DYNAMIC_PROPERTIES : 

  OPTIMIZATION_ALL : 

  OPTIMIZATION_LOSSLESS : 

  OPTIMIZATION_VERY_GOOD : 

  OPTIMIZATION_GOOD : 

  OPTIMIZATION_DRAFT : 

  OPTIMIZATION_DEFAULT : '''
    ...
    def OPTIMIZATION_COMP_MATRIX (self, *args, **kwargs):
      '''

Members:

  OPTIMIZATION_NONE : 

  OPTIMIZATION_IDENTITY : 

  OPTIMIZATION_IDENTITY_GAMMA : 

  OPTIMIZATION_PAIR_IDENTITY_CDL : 

  OPTIMIZATION_PAIR_IDENTITY_EXPOSURE_CONTRAST : 

  OPTIMIZATION_PAIR_IDENTITY_FIXED_FUNCTION : 

  OPTIMIZATION_PAIR_IDENTITY_GAMMA : 

  OPTIMIZATION_PAIR_IDENTITY_LUT1D : 

  OPTIMIZATION_PAIR_IDENTITY_LUT3D : 

  OPTIMIZATION_PAIR_IDENTITY_LOG : 

  OPTIMIZATION_PAIR_IDENTITY_GRADING : 

  OPTIMIZATION_COMP_EXPONENT : 

  OPTIMIZATION_COMP_GAMMA : 

  OPTIMIZATION_COMP_MATRIX : 

  OPTIMIZATION_COMP_LUT1D : 

  OPTIMIZATION_COMP_LUT3D : 

  OPTIMIZATION_COMP_RANGE : 

  OPTIMIZATION_COMP_SEPARABLE_PREFIX : 

  OPTIMIZATION_LUT_INV_FAST : 

  OPTIMIZATION_FAST_LOG_EXP_POW : 

  OPTIMIZATION_SIMPLIFY_OPS : 

  OPTIMIZATION_NO_DYNAMIC_PROPERTIES : 

  OPTIMIZATION_ALL : 

  OPTIMIZATION_LOSSLESS : 

  OPTIMIZATION_VERY_GOOD : 

  OPTIMIZATION_GOOD : 

  OPTIMIZATION_DRAFT : 

  OPTIMIZATION_DEFAULT : '''
    ...
    def OPTIMIZATION_COMP_RANGE (self, *args, **kwargs):
      '''

Members:

  OPTIMIZATION_NONE : 

  OPTIMIZATION_IDENTITY : 

  OPTIMIZATION_IDENTITY_GAMMA : 

  OPTIMIZATION_PAIR_IDENTITY_CDL : 

  OPTIMIZATION_PAIR_IDENTITY_EXPOSURE_CONTRAST : 

  OPTIMIZATION_PAIR_IDENTITY_FIXED_FUNCTION : 

  OPTIMIZATION_PAIR_IDENTITY_GAMMA : 

  OPTIMIZATION_PAIR_IDENTITY_LUT1D : 

  OPTIMIZATION_PAIR_IDENTITY_LUT3D : 

  OPTIMIZATION_PAIR_IDENTITY_LOG : 

  OPTIMIZATION_PAIR_IDENTITY_GRADING : 

  OPTIMIZATION_COMP_EXPONENT : 

  OPTIMIZATION_COMP_GAMMA : 

  OPTIMIZATION_COMP_MATRIX : 

  OPTIMIZATION_COMP_LUT1D : 

  OPTIMIZATION_COMP_LUT3D : 

  OPTIMIZATION_COMP_RANGE : 

  OPTIMIZATION_COMP_SEPARABLE_PREFIX : 

  OPTIMIZATION_LUT_INV_FAST : 

  OPTIMIZATION_FAST_LOG_EXP_POW : 

  OPTIMIZATION_SIMPLIFY_OPS : 

  OPTIMIZATION_NO_DYNAMIC_PROPERTIES : 

  OPTIMIZATION_ALL : 

  OPTIMIZATION_LOSSLESS : 

  OPTIMIZATION_VERY_GOOD : 

  OPTIMIZATION_GOOD : 

  OPTIMIZATION_DRAFT : 

  OPTIMIZATION_DEFAULT : '''
    ...
    def OPTIMIZATION_COMP_SEPARABLE_PREFIX (self, *args, **kwargs):
      '''

Members:

  OPTIMIZATION_NONE : 

  OPTIMIZATION_IDENTITY : 

  OPTIMIZATION_IDENTITY_GAMMA : 

  OPTIMIZATION_PAIR_IDENTITY_CDL : 

  OPTIMIZATION_PAIR_IDENTITY_EXPOSURE_CONTRAST : 

  OPTIMIZATION_PAIR_IDENTITY_FIXED_FUNCTION : 

  OPTIMIZATION_PAIR_IDENTITY_GAMMA : 

  OPTIMIZATION_PAIR_IDENTITY_LUT1D : 

  OPTIMIZATION_PAIR_IDENTITY_LUT3D : 

  OPTIMIZATION_PAIR_IDENTITY_LOG : 

  OPTIMIZATION_PAIR_IDENTITY_GRADING : 

  OPTIMIZATION_COMP_EXPONENT : 

  OPTIMIZATION_COMP_GAMMA : 

  OPTIMIZATION_COMP_MATRIX : 

  OPTIMIZATION_COMP_LUT1D : 

  OPTIMIZATION_COMP_LUT3D : 

  OPTIMIZATION_COMP_RANGE : 

  OPTIMIZATION_COMP_SEPARABLE_PREFIX : 

  OPTIMIZATION_LUT_INV_FAST : 

  OPTIMIZATION_FAST_LOG_EXP_POW : 

  OPTIMIZATION_SIMPLIFY_OPS : 

  OPTIMIZATION_NO_DYNAMIC_PROPERTIES : 

  OPTIMIZATION_ALL : 

  OPTIMIZATION_LOSSLESS : 

  OPTIMIZATION_VERY_GOOD : 

  OPTIMIZATION_GOOD : 

  OPTIMIZATION_DRAFT : 

  OPTIMIZATION_DEFAULT : '''
    ...
    def OPTIMIZATION_DEFAULT (self, *args, **kwargs):
      '''

Members:

  OPTIMIZATION_NONE : 

  OPTIMIZATION_IDENTITY : 

  OPTIMIZATION_IDENTITY_GAMMA : 

  OPTIMIZATION_PAIR_IDENTITY_CDL : 

  OPTIMIZATION_PAIR_IDENTITY_EXPOSURE_CONTRAST : 

  OPTIMIZATION_PAIR_IDENTITY_FIXED_FUNCTION : 

  OPTIMIZATION_PAIR_IDENTITY_GAMMA : 

  OPTIMIZATION_PAIR_IDENTITY_LUT1D : 

  OPTIMIZATION_PAIR_IDENTITY_LUT3D : 

  OPTIMIZATION_PAIR_IDENTITY_LOG : 

  OPTIMIZATION_PAIR_IDENTITY_GRADING : 

  OPTIMIZATION_COMP_EXPONENT : 

  OPTIMIZATION_COMP_GAMMA : 

  OPTIMIZATION_COMP_MATRIX : 

  OPTIMIZATION_COMP_LUT1D : 

  OPTIMIZATION_COMP_LUT3D : 

  OPTIMIZATION_COMP_RANGE : 

  OPTIMIZATION_COMP_SEPARABLE_PREFIX : 

  OPTIMIZATION_LUT_INV_FAST : 

  OPTIMIZATION_FAST_LOG_EXP_POW : 

  OPTIMIZATION_SIMPLIFY_OPS : 

  OPTIMIZATION_NO_DYNAMIC_PROPERTIES : 

  OPTIMIZATION_ALL : 

  OPTIMIZATION_LOSSLESS : 

  OPTIMIZATION_VERY_GOOD : 

  OPTIMIZATION_GOOD : 

  OPTIMIZATION_DRAFT : 

  OPTIMIZATION_DEFAULT : '''
    ...
    def OPTIMIZATION_DRAFT (self, *args, **kwargs):
      '''

Members:

  OPTIMIZATION_NONE : 

  OPTIMIZATION_IDENTITY : 

  OPTIMIZATION_IDENTITY_GAMMA : 

  OPTIMIZATION_PAIR_IDENTITY_CDL : 

  OPTIMIZATION_PAIR_IDENTITY_EXPOSURE_CONTRAST : 

  OPTIMIZATION_PAIR_IDENTITY_FIXED_FUNCTION : 

  OPTIMIZATION_PAIR_IDENTITY_GAMMA : 

  OPTIMIZATION_PAIR_IDENTITY_LUT1D : 

  OPTIMIZATION_PAIR_IDENTITY_LUT3D : 

  OPTIMIZATION_PAIR_IDENTITY_LOG : 

  OPTIMIZATION_PAIR_IDENTITY_GRADING : 

  OPTIMIZATION_COMP_EXPONENT : 

  OPTIMIZATION_COMP_GAMMA : 

  OPTIMIZATION_COMP_MATRIX : 

  OPTIMIZATION_COMP_LUT1D : 

  OPTIMIZATION_COMP_LUT3D : 

  OPTIMIZATION_COMP_RANGE : 

  OPTIMIZATION_COMP_SEPARABLE_PREFIX : 

  OPTIMIZATION_LUT_INV_FAST : 

  OPTIMIZATION_FAST_LOG_EXP_POW : 

  OPTIMIZATION_SIMPLIFY_OPS : 

  OPTIMIZATION_NO_DYNAMIC_PROPERTIES : 

  OPTIMIZATION_ALL : 

  OPTIMIZATION_LOSSLESS : 

  OPTIMIZATION_VERY_GOOD : 

  OPTIMIZATION_GOOD : 

  OPTIMIZATION_DRAFT : 

  OPTIMIZATION_DEFAULT : '''
    ...
    def OPTIMIZATION_FAST_LOG_EXP_POW (self, *args, **kwargs):
      '''

Members:

  OPTIMIZATION_NONE : 

  OPTIMIZATION_IDENTITY : 

  OPTIMIZATION_IDENTITY_GAMMA : 

  OPTIMIZATION_PAIR_IDENTITY_CDL : 

  OPTIMIZATION_PAIR_IDENTITY_EXPOSURE_CONTRAST : 

  OPTIMIZATION_PAIR_IDENTITY_FIXED_FUNCTION : 

  OPTIMIZATION_PAIR_IDENTITY_GAMMA : 

  OPTIMIZATION_PAIR_IDENTITY_LUT1D : 

  OPTIMIZATION_PAIR_IDENTITY_LUT3D : 

  OPTIMIZATION_PAIR_IDENTITY_LOG : 

  OPTIMIZATION_PAIR_IDENTITY_GRADING : 

  OPTIMIZATION_COMP_EXPONENT : 

  OPTIMIZATION_COMP_GAMMA : 

  OPTIMIZATION_COMP_MATRIX : 

  OPTIMIZATION_COMP_LUT1D : 

  OPTIMIZATION_COMP_LUT3D : 

  OPTIMIZATION_COMP_RANGE : 

  OPTIMIZATION_COMP_SEPARABLE_PREFIX : 

  OPTIMIZATION_LUT_INV_FAST : 

  OPTIMIZATION_FAST_LOG_EXP_POW : 

  OPTIMIZATION_SIMPLIFY_OPS : 

  OPTIMIZATION_NO_DYNAMIC_PROPERTIES : 

  OPTIMIZATION_ALL : 

  OPTIMIZATION_LOSSLESS : 

  OPTIMIZATION_VERY_GOOD : 

  OPTIMIZATION_GOOD : 

  OPTIMIZATION_DRAFT : 

  OPTIMIZATION_DEFAULT : '''
    ...
    def OPTIMIZATION_GOOD (self, *args, **kwargs):
      '''

Members:

  OPTIMIZATION_NONE : 

  OPTIMIZATION_IDENTITY : 

  OPTIMIZATION_IDENTITY_GAMMA : 

  OPTIMIZATION_PAIR_IDENTITY_CDL : 

  OPTIMIZATION_PAIR_IDENTITY_EXPOSURE_CONTRAST : 

  OPTIMIZATION_PAIR_IDENTITY_FIXED_FUNCTION : 

  OPTIMIZATION_PAIR_IDENTITY_GAMMA : 

  OPTIMIZATION_PAIR_IDENTITY_LUT1D : 

  OPTIMIZATION_PAIR_IDENTITY_LUT3D : 

  OPTIMIZATION_PAIR_IDENTITY_LOG : 

  OPTIMIZATION_PAIR_IDENTITY_GRADING : 

  OPTIMIZATION_COMP_EXPONENT : 

  OPTIMIZATION_COMP_GAMMA : 

  OPTIMIZATION_COMP_MATRIX : 

  OPTIMIZATION_COMP_LUT1D : 

  OPTIMIZATION_COMP_LUT3D : 

  OPTIMIZATION_COMP_RANGE : 

  OPTIMIZATION_COMP_SEPARABLE_PREFIX : 

  OPTIMIZATION_LUT_INV_FAST : 

  OPTIMIZATION_FAST_LOG_EXP_POW : 

  OPTIMIZATION_SIMPLIFY_OPS : 

  OPTIMIZATION_NO_DYNAMIC_PROPERTIES : 

  OPTIMIZATION_ALL : 

  OPTIMIZATION_LOSSLESS : 

  OPTIMIZATION_VERY_GOOD : 

  OPTIMIZATION_GOOD : 

  OPTIMIZATION_DRAFT : 

  OPTIMIZATION_DEFAULT : '''
    ...
    def OPTIMIZATION_IDENTITY (self, *args, **kwargs):
      '''

Members:

  OPTIMIZATION_NONE : 

  OPTIMIZATION_IDENTITY : 

  OPTIMIZATION_IDENTITY_GAMMA : 

  OPTIMIZATION_PAIR_IDENTITY_CDL : 

  OPTIMIZATION_PAIR_IDENTITY_EXPOSURE_CONTRAST : 

  OPTIMIZATION_PAIR_IDENTITY_FIXED_FUNCTION : 

  OPTIMIZATION_PAIR_IDENTITY_GAMMA : 

  OPTIMIZATION_PAIR_IDENTITY_LUT1D : 

  OPTIMIZATION_PAIR_IDENTITY_LUT3D : 

  OPTIMIZATION_PAIR_IDENTITY_LOG : 

  OPTIMIZATION_PAIR_IDENTITY_GRADING : 

  OPTIMIZATION_COMP_EXPONENT : 

  OPTIMIZATION_COMP_GAMMA : 

  OPTIMIZATION_COMP_MATRIX : 

  OPTIMIZATION_COMP_LUT1D : 

  OPTIMIZATION_COMP_LUT3D : 

  OPTIMIZATION_COMP_RANGE : 

  OPTIMIZATION_COMP_SEPARABLE_PREFIX : 

  OPTIMIZATION_LUT_INV_FAST : 

  OPTIMIZATION_FAST_LOG_EXP_POW : 

  OPTIMIZATION_SIMPLIFY_OPS : 

  OPTIMIZATION_NO_DYNAMIC_PROPERTIES : 

  OPTIMIZATION_ALL : 

  OPTIMIZATION_LOSSLESS : 

  OPTIMIZATION_VERY_GOOD : 

  OPTIMIZATION_GOOD : 

  OPTIMIZATION_DRAFT : 

  OPTIMIZATION_DEFAULT : '''
    ...
    def OPTIMIZATION_IDENTITY_GAMMA (self, *args, **kwargs):
      '''

Members:

  OPTIMIZATION_NONE : 

  OPTIMIZATION_IDENTITY : 

  OPTIMIZATION_IDENTITY_GAMMA : 

  OPTIMIZATION_PAIR_IDENTITY_CDL : 

  OPTIMIZATION_PAIR_IDENTITY_EXPOSURE_CONTRAST : 

  OPTIMIZATION_PAIR_IDENTITY_FIXED_FUNCTION : 

  OPTIMIZATION_PAIR_IDENTITY_GAMMA : 

  OPTIMIZATION_PAIR_IDENTITY_LUT1D : 

  OPTIMIZATION_PAIR_IDENTITY_LUT3D : 

  OPTIMIZATION_PAIR_IDENTITY_LOG : 

  OPTIMIZATION_PAIR_IDENTITY_GRADING : 

  OPTIMIZATION_COMP_EXPONENT : 

  OPTIMIZATION_COMP_GAMMA : 

  OPTIMIZATION_COMP_MATRIX : 

  OPTIMIZATION_COMP_LUT1D : 

  OPTIMIZATION_COMP_LUT3D : 

  OPTIMIZATION_COMP_RANGE : 

  OPTIMIZATION_COMP_SEPARABLE_PREFIX : 

  OPTIMIZATION_LUT_INV_FAST : 

  OPTIMIZATION_FAST_LOG_EXP_POW : 

  OPTIMIZATION_SIMPLIFY_OPS : 

  OPTIMIZATION_NO_DYNAMIC_PROPERTIES : 

  OPTIMIZATION_ALL : 

  OPTIMIZATION_LOSSLESS : 

  OPTIMIZATION_VERY_GOOD : 

  OPTIMIZATION_GOOD : 

  OPTIMIZATION_DRAFT : 

  OPTIMIZATION_DEFAULT : '''
    ...
    def OPTIMIZATION_LOSSLESS (self, *args, **kwargs):
      '''

Members:

  OPTIMIZATION_NONE : 

  OPTIMIZATION_IDENTITY : 

  OPTIMIZATION_IDENTITY_GAMMA : 

  OPTIMIZATION_PAIR_IDENTITY_CDL : 

  OPTIMIZATION_PAIR_IDENTITY_EXPOSURE_CONTRAST : 

  OPTIMIZATION_PAIR_IDENTITY_FIXED_FUNCTION : 

  OPTIMIZATION_PAIR_IDENTITY_GAMMA : 

  OPTIMIZATION_PAIR_IDENTITY_LUT1D : 

  OPTIMIZATION_PAIR_IDENTITY_LUT3D : 

  OPTIMIZATION_PAIR_IDENTITY_LOG : 

  OPTIMIZATION_PAIR_IDENTITY_GRADING : 

  OPTIMIZATION_COMP_EXPONENT : 

  OPTIMIZATION_COMP_GAMMA : 

  OPTIMIZATION_COMP_MATRIX : 

  OPTIMIZATION_COMP_LUT1D : 

  OPTIMIZATION_COMP_LUT3D : 

  OPTIMIZATION_COMP_RANGE : 

  OPTIMIZATION_COMP_SEPARABLE_PREFIX : 

  OPTIMIZATION_LUT_INV_FAST : 

  OPTIMIZATION_FAST_LOG_EXP_POW : 

  OPTIMIZATION_SIMPLIFY_OPS : 

  OPTIMIZATION_NO_DYNAMIC_PROPERTIES : 

  OPTIMIZATION_ALL : 

  OPTIMIZATION_LOSSLESS : 

  OPTIMIZATION_VERY_GOOD : 

  OPTIMIZATION_GOOD : 

  OPTIMIZATION_DRAFT : 

  OPTIMIZATION_DEFAULT : '''
    ...
    def OPTIMIZATION_LUT_INV_FAST (self, *args, **kwargs):
      '''

Members:

  OPTIMIZATION_NONE : 

  OPTIMIZATION_IDENTITY : 

  OPTIMIZATION_IDENTITY_GAMMA : 

  OPTIMIZATION_PAIR_IDENTITY_CDL : 

  OPTIMIZATION_PAIR_IDENTITY_EXPOSURE_CONTRAST : 

  OPTIMIZATION_PAIR_IDENTITY_FIXED_FUNCTION : 

  OPTIMIZATION_PAIR_IDENTITY_GAMMA : 

  OPTIMIZATION_PAIR_IDENTITY_LUT1D : 

  OPTIMIZATION_PAIR_IDENTITY_LUT3D : 

  OPTIMIZATION_PAIR_IDENTITY_LOG : 

  OPTIMIZATION_PAIR_IDENTITY_GRADING : 

  OPTIMIZATION_COMP_EXPONENT : 

  OPTIMIZATION_COMP_GAMMA : 

  OPTIMIZATION_COMP_MATRIX : 

  OPTIMIZATION_COMP_LUT1D : 

  OPTIMIZATION_COMP_LUT3D : 

  OPTIMIZATION_COMP_RANGE : 

  OPTIMIZATION_COMP_SEPARABLE_PREFIX : 

  OPTIMIZATION_LUT_INV_FAST : 

  OPTIMIZATION_FAST_LOG_EXP_POW : 

  OPTIMIZATION_SIMPLIFY_OPS : 

  OPTIMIZATION_NO_DYNAMIC_PROPERTIES : 

  OPTIMIZATION_ALL : 

  OPTIMIZATION_LOSSLESS : 

  OPTIMIZATION_VERY_GOOD : 

  OPTIMIZATION_GOOD : 

  OPTIMIZATION_DRAFT : 

  OPTIMIZATION_DEFAULT : '''
    ...
    def OPTIMIZATION_NONE (self, *args, **kwargs):
      '''

Members:

  OPTIMIZATION_NONE : 

  OPTIMIZATION_IDENTITY : 

  OPTIMIZATION_IDENTITY_GAMMA : 

  OPTIMIZATION_PAIR_IDENTITY_CDL : 

  OPTIMIZATION_PAIR_IDENTITY_EXPOSURE_CONTRAST : 

  OPTIMIZATION_PAIR_IDENTITY_FIXED_FUNCTION : 

  OPTIMIZATION_PAIR_IDENTITY_GAMMA : 

  OPTIMIZATION_PAIR_IDENTITY_LUT1D : 

  OPTIMIZATION_PAIR_IDENTITY_LUT3D : 

  OPTIMIZATION_PAIR_IDENTITY_LOG : 

  OPTIMIZATION_PAIR_IDENTITY_GRADING : 

  OPTIMIZATION_COMP_EXPONENT : 

  OPTIMIZATION_COMP_GAMMA : 

  OPTIMIZATION_COMP_MATRIX : 

  OPTIMIZATION_COMP_LUT1D : 

  OPTIMIZATION_COMP_LUT3D : 

  OPTIMIZATION_COMP_RANGE : 

  OPTIMIZATION_COMP_SEPARABLE_PREFIX : 

  OPTIMIZATION_LUT_INV_FAST : 

  OPTIMIZATION_FAST_LOG_EXP_POW : 

  OPTIMIZATION_SIMPLIFY_OPS : 

  OPTIMIZATION_NO_DYNAMIC_PROPERTIES : 

  OPTIMIZATION_ALL : 

  OPTIMIZATION_LOSSLESS : 

  OPTIMIZATION_VERY_GOOD : 

  OPTIMIZATION_GOOD : 

  OPTIMIZATION_DRAFT : 

  OPTIMIZATION_DEFAULT : '''
    ...
    def OPTIMIZATION_NO_DYNAMIC_PROPERTIES (self, *args, **kwargs):
      '''

Members:

  OPTIMIZATION_NONE : 

  OPTIMIZATION_IDENTITY : 

  OPTIMIZATION_IDENTITY_GAMMA : 

  OPTIMIZATION_PAIR_IDENTITY_CDL : 

  OPTIMIZATION_PAIR_IDENTITY_EXPOSURE_CONTRAST : 

  OPTIMIZATION_PAIR_IDENTITY_FIXED_FUNCTION : 

  OPTIMIZATION_PAIR_IDENTITY_GAMMA : 

  OPTIMIZATION_PAIR_IDENTITY_LUT1D : 

  OPTIMIZATION_PAIR_IDENTITY_LUT3D : 

  OPTIMIZATION_PAIR_IDENTITY_LOG : 

  OPTIMIZATION_PAIR_IDENTITY_GRADING : 

  OPTIMIZATION_COMP_EXPONENT : 

  OPTIMIZATION_COMP_GAMMA : 

  OPTIMIZATION_COMP_MATRIX : 

  OPTIMIZATION_COMP_LUT1D : 

  OPTIMIZATION_COMP_LUT3D : 

  OPTIMIZATION_COMP_RANGE : 

  OPTIMIZATION_COMP_SEPARABLE_PREFIX : 

  OPTIMIZATION_LUT_INV_FAST : 

  OPTIMIZATION_FAST_LOG_EXP_POW : 

  OPTIMIZATION_SIMPLIFY_OPS : 

  OPTIMIZATION_NO_DYNAMIC_PROPERTIES : 

  OPTIMIZATION_ALL : 

  OPTIMIZATION_LOSSLESS : 

  OPTIMIZATION_VERY_GOOD : 

  OPTIMIZATION_GOOD : 

  OPTIMIZATION_DRAFT : 

  OPTIMIZATION_DEFAULT : '''
    ...
    def OPTIMIZATION_PAIR_IDENTITY_CDL (self, *args, **kwargs):
      '''

Members:

  OPTIMIZATION_NONE : 

  OPTIMIZATION_IDENTITY : 

  OPTIMIZATION_IDENTITY_GAMMA : 

  OPTIMIZATION_PAIR_IDENTITY_CDL : 

  OPTIMIZATION_PAIR_IDENTITY_EXPOSURE_CONTRAST : 

  OPTIMIZATION_PAIR_IDENTITY_FIXED_FUNCTION : 

  OPTIMIZATION_PAIR_IDENTITY_GAMMA : 

  OPTIMIZATION_PAIR_IDENTITY_LUT1D : 

  OPTIMIZATION_PAIR_IDENTITY_LUT3D : 

  OPTIMIZATION_PAIR_IDENTITY_LOG : 

  OPTIMIZATION_PAIR_IDENTITY_GRADING : 

  OPTIMIZATION_COMP_EXPONENT : 

  OPTIMIZATION_COMP_GAMMA : 

  OPTIMIZATION_COMP_MATRIX : 

  OPTIMIZATION_COMP_LUT1D : 

  OPTIMIZATION_COMP_LUT3D : 

  OPTIMIZATION_COMP_RANGE : 

  OPTIMIZATION_COMP_SEPARABLE_PREFIX : 

  OPTIMIZATION_LUT_INV_FAST : 

  OPTIMIZATION_FAST_LOG_EXP_POW : 

  OPTIMIZATION_SIMPLIFY_OPS : 

  OPTIMIZATION_NO_DYNAMIC_PROPERTIES : 

  OPTIMIZATION_ALL : 

  OPTIMIZATION_LOSSLESS : 

  OPTIMIZATION_VERY_GOOD : 

  OPTIMIZATION_GOOD : 

  OPTIMIZATION_DRAFT : 

  OPTIMIZATION_DEFAULT : '''
    ...
    def OPTIMIZATION_PAIR_IDENTITY_EXPOSURE_CONTRAST (self, *args, **kwargs):
      '''

Members:

  OPTIMIZATION_NONE : 

  OPTIMIZATION_IDENTITY : 

  OPTIMIZATION_IDENTITY_GAMMA : 

  OPTIMIZATION_PAIR_IDENTITY_CDL : 

  OPTIMIZATION_PAIR_IDENTITY_EXPOSURE_CONTRAST : 

  OPTIMIZATION_PAIR_IDENTITY_FIXED_FUNCTION : 

  OPTIMIZATION_PAIR_IDENTITY_GAMMA : 

  OPTIMIZATION_PAIR_IDENTITY_LUT1D : 

  OPTIMIZATION_PAIR_IDENTITY_LUT3D : 

  OPTIMIZATION_PAIR_IDENTITY_LOG : 

  OPTIMIZATION_PAIR_IDENTITY_GRADING : 

  OPTIMIZATION_COMP_EXPONENT : 

  OPTIMIZATION_COMP_GAMMA : 

  OPTIMIZATION_COMP_MATRIX : 

  OPTIMIZATION_COMP_LUT1D : 

  OPTIMIZATION_COMP_LUT3D : 

  OPTIMIZATION_COMP_RANGE : 

  OPTIMIZATION_COMP_SEPARABLE_PREFIX : 

  OPTIMIZATION_LUT_INV_FAST : 

  OPTIMIZATION_FAST_LOG_EXP_POW : 

  OPTIMIZATION_SIMPLIFY_OPS : 

  OPTIMIZATION_NO_DYNAMIC_PROPERTIES : 

  OPTIMIZATION_ALL : 

  OPTIMIZATION_LOSSLESS : 

  OPTIMIZATION_VERY_GOOD : 

  OPTIMIZATION_GOOD : 

  OPTIMIZATION_DRAFT : 

  OPTIMIZATION_DEFAULT : '''
    ...
    def OPTIMIZATION_PAIR_IDENTITY_FIXED_FUNCTION (self, *args, **kwargs):
      '''

Members:

  OPTIMIZATION_NONE : 

  OPTIMIZATION_IDENTITY : 

  OPTIMIZATION_IDENTITY_GAMMA : 

  OPTIMIZATION_PAIR_IDENTITY_CDL : 

  OPTIMIZATION_PAIR_IDENTITY_EXPOSURE_CONTRAST : 

  OPTIMIZATION_PAIR_IDENTITY_FIXED_FUNCTION : 

  OPTIMIZATION_PAIR_IDENTITY_GAMMA : 

  OPTIMIZATION_PAIR_IDENTITY_LUT1D : 

  OPTIMIZATION_PAIR_IDENTITY_LUT3D : 

  OPTIMIZATION_PAIR_IDENTITY_LOG : 

  OPTIMIZATION_PAIR_IDENTITY_GRADING : 

  OPTIMIZATION_COMP_EXPONENT : 

  OPTIMIZATION_COMP_GAMMA : 

  OPTIMIZATION_COMP_MATRIX : 

  OPTIMIZATION_COMP_LUT1D : 

  OPTIMIZATION_COMP_LUT3D : 

  OPTIMIZATION_COMP_RANGE : 

  OPTIMIZATION_COMP_SEPARABLE_PREFIX : 

  OPTIMIZATION_LUT_INV_FAST : 

  OPTIMIZATION_FAST_LOG_EXP_POW : 

  OPTIMIZATION_SIMPLIFY_OPS : 

  OPTIMIZATION_NO_DYNAMIC_PROPERTIES : 

  OPTIMIZATION_ALL : 

  OPTIMIZATION_LOSSLESS : 

  OPTIMIZATION_VERY_GOOD : 

  OPTIMIZATION_GOOD : 

  OPTIMIZATION_DRAFT : 

  OPTIMIZATION_DEFAULT : '''
    ...
    def OPTIMIZATION_PAIR_IDENTITY_GAMMA (self, *args, **kwargs):
      '''

Members:

  OPTIMIZATION_NONE : 

  OPTIMIZATION_IDENTITY : 

  OPTIMIZATION_IDENTITY_GAMMA : 

  OPTIMIZATION_PAIR_IDENTITY_CDL : 

  OPTIMIZATION_PAIR_IDENTITY_EXPOSURE_CONTRAST : 

  OPTIMIZATION_PAIR_IDENTITY_FIXED_FUNCTION : 

  OPTIMIZATION_PAIR_IDENTITY_GAMMA : 

  OPTIMIZATION_PAIR_IDENTITY_LUT1D : 

  OPTIMIZATION_PAIR_IDENTITY_LUT3D : 

  OPTIMIZATION_PAIR_IDENTITY_LOG : 

  OPTIMIZATION_PAIR_IDENTITY_GRADING : 

  OPTIMIZATION_COMP_EXPONENT : 

  OPTIMIZATION_COMP_GAMMA : 

  OPTIMIZATION_COMP_MATRIX : 

  OPTIMIZATION_COMP_LUT1D : 

  OPTIMIZATION_COMP_LUT3D : 

  OPTIMIZATION_COMP_RANGE : 

  OPTIMIZATION_COMP_SEPARABLE_PREFIX : 

  OPTIMIZATION_LUT_INV_FAST : 

  OPTIMIZATION_FAST_LOG_EXP_POW : 

  OPTIMIZATION_SIMPLIFY_OPS : 

  OPTIMIZATION_NO_DYNAMIC_PROPERTIES : 

  OPTIMIZATION_ALL : 

  OPTIMIZATION_LOSSLESS : 

  OPTIMIZATION_VERY_GOOD : 

  OPTIMIZATION_GOOD : 

  OPTIMIZATION_DRAFT : 

  OPTIMIZATION_DEFAULT : '''
    ...
    def OPTIMIZATION_PAIR_IDENTITY_GRADING (self, *args, **kwargs):
      '''

Members:

  OPTIMIZATION_NONE : 

  OPTIMIZATION_IDENTITY : 

  OPTIMIZATION_IDENTITY_GAMMA : 

  OPTIMIZATION_PAIR_IDENTITY_CDL : 

  OPTIMIZATION_PAIR_IDENTITY_EXPOSURE_CONTRAST : 

  OPTIMIZATION_PAIR_IDENTITY_FIXED_FUNCTION : 

  OPTIMIZATION_PAIR_IDENTITY_GAMMA : 

  OPTIMIZATION_PAIR_IDENTITY_LUT1D : 

  OPTIMIZATION_PAIR_IDENTITY_LUT3D : 

  OPTIMIZATION_PAIR_IDENTITY_LOG : 

  OPTIMIZATION_PAIR_IDENTITY_GRADING : 

  OPTIMIZATION_COMP_EXPONENT : 

  OPTIMIZATION_COMP_GAMMA : 

  OPTIMIZATION_COMP_MATRIX : 

  OPTIMIZATION_COMP_LUT1D : 

  OPTIMIZATION_COMP_LUT3D : 

  OPTIMIZATION_COMP_RANGE : 

  OPTIMIZATION_COMP_SEPARABLE_PREFIX : 

  OPTIMIZATION_LUT_INV_FAST : 

  OPTIMIZATION_FAST_LOG_EXP_POW : 

  OPTIMIZATION_SIMPLIFY_OPS : 

  OPTIMIZATION_NO_DYNAMIC_PROPERTIES : 

  OPTIMIZATION_ALL : 

  OPTIMIZATION_LOSSLESS : 

  OPTIMIZATION_VERY_GOOD : 

  OPTIMIZATION_GOOD : 

  OPTIMIZATION_DRAFT : 

  OPTIMIZATION_DEFAULT : '''
    ...
    def OPTIMIZATION_PAIR_IDENTITY_LOG (self, *args, **kwargs):
      '''

Members:

  OPTIMIZATION_NONE : 

  OPTIMIZATION_IDENTITY : 

  OPTIMIZATION_IDENTITY_GAMMA : 

  OPTIMIZATION_PAIR_IDENTITY_CDL : 

  OPTIMIZATION_PAIR_IDENTITY_EXPOSURE_CONTRAST : 

  OPTIMIZATION_PAIR_IDENTITY_FIXED_FUNCTION : 

  OPTIMIZATION_PAIR_IDENTITY_GAMMA : 

  OPTIMIZATION_PAIR_IDENTITY_LUT1D : 

  OPTIMIZATION_PAIR_IDENTITY_LUT3D : 

  OPTIMIZATION_PAIR_IDENTITY_LOG : 

  OPTIMIZATION_PAIR_IDENTITY_GRADING : 

  OPTIMIZATION_COMP_EXPONENT : 

  OPTIMIZATION_COMP_GAMMA : 

  OPTIMIZATION_COMP_MATRIX : 

  OPTIMIZATION_COMP_LUT1D : 

  OPTIMIZATION_COMP_LUT3D : 

  OPTIMIZATION_COMP_RANGE : 

  OPTIMIZATION_COMP_SEPARABLE_PREFIX : 

  OPTIMIZATION_LUT_INV_FAST : 

  OPTIMIZATION_FAST_LOG_EXP_POW : 

  OPTIMIZATION_SIMPLIFY_OPS : 

  OPTIMIZATION_NO_DYNAMIC_PROPERTIES : 

  OPTIMIZATION_ALL : 

  OPTIMIZATION_LOSSLESS : 

  OPTIMIZATION_VERY_GOOD : 

  OPTIMIZATION_GOOD : 

  OPTIMIZATION_DRAFT : 

  OPTIMIZATION_DEFAULT : '''
    ...
    def OPTIMIZATION_PAIR_IDENTITY_LUT1D (self, *args, **kwargs):
      '''

Members:

  OPTIMIZATION_NONE : 

  OPTIMIZATION_IDENTITY : 

  OPTIMIZATION_IDENTITY_GAMMA : 

  OPTIMIZATION_PAIR_IDENTITY_CDL : 

  OPTIMIZATION_PAIR_IDENTITY_EXPOSURE_CONTRAST : 

  OPTIMIZATION_PAIR_IDENTITY_FIXED_FUNCTION : 

  OPTIMIZATION_PAIR_IDENTITY_GAMMA : 

  OPTIMIZATION_PAIR_IDENTITY_LUT1D : 

  OPTIMIZATION_PAIR_IDENTITY_LUT3D : 

  OPTIMIZATION_PAIR_IDENTITY_LOG : 

  OPTIMIZATION_PAIR_IDENTITY_GRADING : 

  OPTIMIZATION_COMP_EXPONENT : 

  OPTIMIZATION_COMP_GAMMA : 

  OPTIMIZATION_COMP_MATRIX : 

  OPTIMIZATION_COMP_LUT1D : 

  OPTIMIZATION_COMP_LUT3D : 

  OPTIMIZATION_COMP_RANGE : 

  OPTIMIZATION_COMP_SEPARABLE_PREFIX : 

  OPTIMIZATION_LUT_INV_FAST : 

  OPTIMIZATION_FAST_LOG_EXP_POW : 

  OPTIMIZATION_SIMPLIFY_OPS : 

  OPTIMIZATION_NO_DYNAMIC_PROPERTIES : 

  OPTIMIZATION_ALL : 

  OPTIMIZATION_LOSSLESS : 

  OPTIMIZATION_VERY_GOOD : 

  OPTIMIZATION_GOOD : 

  OPTIMIZATION_DRAFT : 

  OPTIMIZATION_DEFAULT : '''
    ...
    def OPTIMIZATION_PAIR_IDENTITY_LUT3D (self, *args, **kwargs):
      '''

Members:

  OPTIMIZATION_NONE : 

  OPTIMIZATION_IDENTITY : 

  OPTIMIZATION_IDENTITY_GAMMA : 

  OPTIMIZATION_PAIR_IDENTITY_CDL : 

  OPTIMIZATION_PAIR_IDENTITY_EXPOSURE_CONTRAST : 

  OPTIMIZATION_PAIR_IDENTITY_FIXED_FUNCTION : 

  OPTIMIZATION_PAIR_IDENTITY_GAMMA : 

  OPTIMIZATION_PAIR_IDENTITY_LUT1D : 

  OPTIMIZATION_PAIR_IDENTITY_LUT3D : 

  OPTIMIZATION_PAIR_IDENTITY_LOG : 

  OPTIMIZATION_PAIR_IDENTITY_GRADING : 

  OPTIMIZATION_COMP_EXPONENT : 

  OPTIMIZATION_COMP_GAMMA : 

  OPTIMIZATION_COMP_MATRIX : 

  OPTIMIZATION_COMP_LUT1D : 

  OPTIMIZATION_COMP_LUT3D : 

  OPTIMIZATION_COMP_RANGE : 

  OPTIMIZATION_COMP_SEPARABLE_PREFIX : 

  OPTIMIZATION_LUT_INV_FAST : 

  OPTIMIZATION_FAST_LOG_EXP_POW : 

  OPTIMIZATION_SIMPLIFY_OPS : 

  OPTIMIZATION_NO_DYNAMIC_PROPERTIES : 

  OPTIMIZATION_ALL : 

  OPTIMIZATION_LOSSLESS : 

  OPTIMIZATION_VERY_GOOD : 

  OPTIMIZATION_GOOD : 

  OPTIMIZATION_DRAFT : 

  OPTIMIZATION_DEFAULT : '''
    ...
    def OPTIMIZATION_SIMPLIFY_OPS (self, *args, **kwargs):
      '''

Members:

  OPTIMIZATION_NONE : 

  OPTIMIZATION_IDENTITY : 

  OPTIMIZATION_IDENTITY_GAMMA : 

  OPTIMIZATION_PAIR_IDENTITY_CDL : 

  OPTIMIZATION_PAIR_IDENTITY_EXPOSURE_CONTRAST : 

  OPTIMIZATION_PAIR_IDENTITY_FIXED_FUNCTION : 

  OPTIMIZATION_PAIR_IDENTITY_GAMMA : 

  OPTIMIZATION_PAIR_IDENTITY_LUT1D : 

  OPTIMIZATION_PAIR_IDENTITY_LUT3D : 

  OPTIMIZATION_PAIR_IDENTITY_LOG : 

  OPTIMIZATION_PAIR_IDENTITY_GRADING : 

  OPTIMIZATION_COMP_EXPONENT : 

  OPTIMIZATION_COMP_GAMMA : 

  OPTIMIZATION_COMP_MATRIX : 

  OPTIMIZATION_COMP_LUT1D : 

  OPTIMIZATION_COMP_LUT3D : 

  OPTIMIZATION_COMP_RANGE : 

  OPTIMIZATION_COMP_SEPARABLE_PREFIX : 

  OPTIMIZATION_LUT_INV_FAST : 

  OPTIMIZATION_FAST_LOG_EXP_POW : 

  OPTIMIZATION_SIMPLIFY_OPS : 

  OPTIMIZATION_NO_DYNAMIC_PROPERTIES : 

  OPTIMIZATION_ALL : 

  OPTIMIZATION_LOSSLESS : 

  OPTIMIZATION_VERY_GOOD : 

  OPTIMIZATION_GOOD : 

  OPTIMIZATION_DRAFT : 

  OPTIMIZATION_DEFAULT : '''
    ...
    def OPTIMIZATION_VERY_GOOD (self, *args, **kwargs):
      '''

Members:

  OPTIMIZATION_NONE : 

  OPTIMIZATION_IDENTITY : 

  OPTIMIZATION_IDENTITY_GAMMA : 

  OPTIMIZATION_PAIR_IDENTITY_CDL : 

  OPTIMIZATION_PAIR_IDENTITY_EXPOSURE_CONTRAST : 

  OPTIMIZATION_PAIR_IDENTITY_FIXED_FUNCTION : 

  OPTIMIZATION_PAIR_IDENTITY_GAMMA : 

  OPTIMIZATION_PAIR_IDENTITY_LUT1D : 

  OPTIMIZATION_PAIR_IDENTITY_LUT3D : 

  OPTIMIZATION_PAIR_IDENTITY_LOG : 

  OPTIMIZATION_PAIR_IDENTITY_GRADING : 

  OPTIMIZATION_COMP_EXPONENT : 

  OPTIMIZATION_COMP_GAMMA : 

  OPTIMIZATION_COMP_MATRIX : 

  OPTIMIZATION_COMP_LUT1D : 

  OPTIMIZATION_COMP_LUT3D : 

  OPTIMIZATION_COMP_RANGE : 

  OPTIMIZATION_COMP_SEPARABLE_PREFIX : 

  OPTIMIZATION_LUT_INV_FAST : 

  OPTIMIZATION_FAST_LOG_EXP_POW : 

  OPTIMIZATION_SIMPLIFY_OPS : 

  OPTIMIZATION_NO_DYNAMIC_PROPERTIES : 

  OPTIMIZATION_ALL : 

  OPTIMIZATION_LOSSLESS : 

  OPTIMIZATION_VERY_GOOD : 

  OPTIMIZATION_GOOD : 

  OPTIMIZATION_DRAFT : 

  OPTIMIZATION_DEFAULT : '''
    ...
    def name (self, *args, **kwargs):
      '''name(self: handle) -> str
'''
    ...
    def value (self, *args, **kwargs):
      ''''''
    ...

def PROCESSOR_CACHE_DEFAULT (*args):
      '''

'''      
    ...

def PROCESSOR_CACHE_ENABLED (*args):
      '''

'''      
    ...

def PROCESSOR_CACHE_OFF (*args):
      '''

'''      
    ...

def PROCESSOR_CACHE_SHARE_DYN_PROPERTIES (*args):
      '''

'''      
    ...

def PackedImageDesc (*args):
      '''

'''      
    ...

class PackedImageDesc:
    def getBitDepth (self, *args, **kwargs):
      '''getBitDepth(self: PyOpenColorIO.ImageDesc) -> PyOpenColorIO.BitDepth
'''
    ...
    def getChanStrideBytes (self, *args, **kwargs):
      '''getChanStrideBytes(self: PyOpenColorIO.PackedImageDesc) -> int
'''
    ...
    def getChannelOrder (self, *args, **kwargs):
      '''getChannelOrder(self: PyOpenColorIO.PackedImageDesc) -> PyOpenColorIO.ChannelOrdering
'''
    ...
    def getData (self, *args, **kwargs):
      '''getData(self: PyOpenColorIO.PackedImageDesc) -> numpy.ndarray
'''
    ...
    def getHeight (self, *args, **kwargs):
      '''getHeight(self: PyOpenColorIO.ImageDesc) -> int
'''
    ...
    def getNumChannels (self, *args, **kwargs):
      '''getNumChannels(self: PyOpenColorIO.PackedImageDesc) -> int
'''
    ...
    def getWidth (self, *args, **kwargs):
      '''getWidth(self: PyOpenColorIO.ImageDesc) -> int
'''
    ...
    def getXStrideBytes (self, *args, **kwargs):
      '''getXStrideBytes(self: PyOpenColorIO.ImageDesc) -> int
'''
    ...
    def getYStrideBytes (self, *args, **kwargs):
      '''getYStrideBytes(self: PyOpenColorIO.ImageDesc) -> int
'''
    ...
    def isFloat (self, *args, **kwargs):
      '''isFloat(self: PyOpenColorIO.ImageDesc) -> bool
'''
    ...
    def isRGBAPacked (self, *args, **kwargs):
      '''isRGBAPacked(self: PyOpenColorIO.ImageDesc) -> bool
'''
    ...

def PlanarImageDesc (*args):
      '''

'''      
    ...

class PlanarImageDesc:
    def getAData (self, *args, **kwargs):
      '''getAData(self: PyOpenColorIO.PlanarImageDesc) -> numpy.ndarray
'''
    ...
    def getBData (self, *args, **kwargs):
      '''getBData(self: PyOpenColorIO.PlanarImageDesc) -> numpy.ndarray
'''
    ...
    def getBitDepth (self, *args, **kwargs):
      '''getBitDepth(self: PyOpenColorIO.ImageDesc) -> PyOpenColorIO.BitDepth
'''
    ...
    def getGData (self, *args, **kwargs):
      '''getGData(self: PyOpenColorIO.PlanarImageDesc) -> numpy.ndarray
'''
    ...
    def getHeight (self, *args, **kwargs):
      '''getHeight(self: PyOpenColorIO.ImageDesc) -> int
'''
    ...
    def getRData (self, *args, **kwargs):
      '''getRData(self: PyOpenColorIO.PlanarImageDesc) -> numpy.ndarray
'''
    ...
    def getWidth (self, *args, **kwargs):
      '''getWidth(self: PyOpenColorIO.ImageDesc) -> int
'''
    ...
    def getXStrideBytes (self, *args, **kwargs):
      '''getXStrideBytes(self: PyOpenColorIO.ImageDesc) -> int
'''
    ...
    def getYStrideBytes (self, *args, **kwargs):
      '''getYStrideBytes(self: PyOpenColorIO.ImageDesc) -> int
'''
    ...
    def isFloat (self, *args, **kwargs):
      '''isFloat(self: PyOpenColorIO.ImageDesc) -> bool
'''
    ...
    def isRGBAPacked (self, *args, **kwargs):
      '''isRGBAPacked(self: PyOpenColorIO.ImageDesc) -> bool
'''
    ...

def Processor (*args):
      '''

'''      
    ...

class Processor:
    def TransformFormatMetadataIterator (self, *args, **kwargs):
      '''None'''
    ...
    def createGroupTransform (self, *args, **kwargs):
      '''createGroupTransform(self: PyOpenColorIO.Processor) -> PyOpenColorIO.GroupTransform
'''
    ...
    def getCacheID (self, *args, **kwargs):
      '''getCacheID(self: PyOpenColorIO.Processor) -> str
'''
    ...
    def getDefaultCPUProcessor (self, *args, **kwargs):
      '''getDefaultCPUProcessor(self: PyOpenColorIO.Processor) -> PyOpenColorIO.CPUProcessor
'''
    ...
    def getDefaultGPUProcessor (self, *args, **kwargs):
      '''getDefaultGPUProcessor(self: PyOpenColorIO.Processor) -> PyOpenColorIO.GPUProcessor
'''
    ...
    def getDynamicProperty (self, *args, **kwargs):
      '''getDynamicProperty(self: PyOpenColorIO.Processor, type: PyOpenColorIO.DynamicPropertyType) -> PyOpenColorIO.DynamicProperty
'''
    ...
    def getFormatMetadata (self, *args, **kwargs):
      '''getFormatMetadata(self: PyOpenColorIO.Processor) -> PyOpenColorIO.FormatMetadata
'''
    ...
    def getOptimizedCPUProcessor (self, *args, **kwargs):
      '''getOptimizedCPUProcessor(*args, **kwargs)
Overloaded function.

1. getOptimizedCPUProcessor(self: PyOpenColorIO.Processor, oFlags: PyOpenColorIO.OptimizationFlags) -> PyOpenColorIO.CPUProcessor

2. getOptimizedCPUProcessor(self: PyOpenColorIO.Processor, inBitDepth: PyOpenColorIO.BitDepth, outBitDepth: PyOpenColorIO.BitDepth, oFlags: PyOpenColorIO.OptimizationFlags) -> PyOpenColorIO.CPUProcessor
'''
    ...
    def getOptimizedGPUProcessor (self, *args, **kwargs):
      '''getOptimizedGPUProcessor(self: PyOpenColorIO.Processor, oFlags: PyOpenColorIO.OptimizationFlags) -> PyOpenColorIO.GPUProcessor
'''
    ...
    def getOptimizedProcessor (self, *args, **kwargs):
      '''getOptimizedProcessor(*args, **kwargs)
Overloaded function.

1. getOptimizedProcessor(self: PyOpenColorIO.Processor, oFlags: PyOpenColorIO.OptimizationFlags) -> PyOpenColorIO.Processor

2. getOptimizedProcessor(self: PyOpenColorIO.Processor, inBitDepth: PyOpenColorIO.BitDepth, outBitDepth: PyOpenColorIO.BitDepth, oFlags: PyOpenColorIO.OptimizationFlags) -> PyOpenColorIO.Processor
'''
    ...
    def getProcessorMetadata (self, *args, **kwargs):
      '''getProcessorMetadata(self: PyOpenColorIO.Processor) -> PyOpenColorIO.ProcessorMetadata
'''
    ...
    def getTransformFormatMetadata (self, *args, **kwargs):
      '''getTransformFormatMetadata(self: PyOpenColorIO.Processor) -> PyOpenColorIO.Processor.TransformFormatMetadataIterator
'''
    ...
    def hasChannelCrosstalk (self, *args, **kwargs):
      '''hasChannelCrosstalk(self: PyOpenColorIO.Processor) -> bool
'''
    ...
    def hasDynamicProperty (self, *args, **kwargs):
      '''hasDynamicProperty(self: PyOpenColorIO.Processor, type: PyOpenColorIO.DynamicPropertyType) -> bool
'''
    ...
    def isDynamic (self, *args, **kwargs):
      '''isDynamic(self: PyOpenColorIO.Processor) -> bool
'''
    ...
    def isNoOp (self, *args, **kwargs):
      '''isNoOp(self: PyOpenColorIO.Processor) -> bool
'''
    ...

def ProcessorCacheFlags (*args):
      '''

'''      
    ...

class ProcessorCacheFlags:
    def PROCESSOR_CACHE_DEFAULT (self, *args, **kwargs):
      '''

Members:

  PROCESSOR_CACHE_OFF : 

  PROCESSOR_CACHE_ENABLED : 

  PROCESSOR_CACHE_SHARE_DYN_PROPERTIES : 

  PROCESSOR_CACHE_DEFAULT : '''
    ...
    def PROCESSOR_CACHE_ENABLED (self, *args, **kwargs):
      '''

Members:

  PROCESSOR_CACHE_OFF : 

  PROCESSOR_CACHE_ENABLED : 

  PROCESSOR_CACHE_SHARE_DYN_PROPERTIES : 

  PROCESSOR_CACHE_DEFAULT : '''
    ...
    def PROCESSOR_CACHE_OFF (self, *args, **kwargs):
      '''

Members:

  PROCESSOR_CACHE_OFF : 

  PROCESSOR_CACHE_ENABLED : 

  PROCESSOR_CACHE_SHARE_DYN_PROPERTIES : 

  PROCESSOR_CACHE_DEFAULT : '''
    ...
    def PROCESSOR_CACHE_SHARE_DYN_PROPERTIES (self, *args, **kwargs):
      '''

Members:

  PROCESSOR_CACHE_OFF : 

  PROCESSOR_CACHE_ENABLED : 

  PROCESSOR_CACHE_SHARE_DYN_PROPERTIES : 

  PROCESSOR_CACHE_DEFAULT : '''
    ...
    def name (self, *args, **kwargs):
      '''name(self: handle) -> str
'''
    ...
    def value (self, *args, **kwargs):
      ''''''
    ...

def ProcessorMetadata (*args):
      '''

'''      
    ...

class ProcessorMetadata:
    def FileIterator (self, *args, **kwargs):
      '''None'''
    ...
    def LookIterator (self, *args, **kwargs):
      '''None'''
    ...
    def addFile (self, *args, **kwargs):
      '''addFile(self: PyOpenColorIO.ProcessorMetadata, fileName: str) -> None
'''
    ...
    def addLook (self, *args, **kwargs):
      '''addLook(self: PyOpenColorIO.ProcessorMetadata, look: str) -> None
'''
    ...
    def getFiles (self, *args, **kwargs):
      '''getFiles(self: PyOpenColorIO.ProcessorMetadata) -> PyOpenColorIO.ProcessorMetadata.FileIterator
'''
    ...
    def getLooks (self, *args, **kwargs):
      '''getLooks(self: PyOpenColorIO.ProcessorMetadata) -> PyOpenColorIO.ProcessorMetadata.LookIterator
'''
    ...

def PyConfigIOProxy (*args):
      '''

'''      
    ...

class PyConfigIOProxy:
    def getConfigData (self, *args, **kwargs):
      '''getConfigData(self: PyOpenColorIO.PyConfigIOProxy) -> str
'''
    ...
    def getFastLutFileHash (self, *args, **kwargs):
      '''getFastLutFileHash(self: PyOpenColorIO.PyConfigIOProxy, arg0: str) -> str
'''
    ...
    def getLutData (self, *args, **kwargs):
      '''getLutData(self: PyOpenColorIO.PyConfigIOProxy, arg0: str) -> PyOpenColorIO.vector_of_uint8_t
'''
    ...

def RANGE_CLAMP (*args):
      '''

'''      
    ...

def RANGE_NO_CLAMP (*args):
      '''

'''      
    ...

def REFERENCE_SPACE_DISPLAY (*args):
      '''

'''      
    ...

def REFERENCE_SPACE_SCENE (*args):
      '''

'''      
    ...

def RGBCurveType (*args):
      '''

'''      
    ...

class RGBCurveType:
    def RGB_BLUE (self, *args, **kwargs):
      '''

Members:

  RGB_RED : 

  RGB_GREEN : 

  RGB_BLUE : 

  RGB_MASTER : 

  RGB_NUM_CURVES : '''
    ...
    def RGB_GREEN (self, *args, **kwargs):
      '''

Members:

  RGB_RED : 

  RGB_GREEN : 

  RGB_BLUE : 

  RGB_MASTER : 

  RGB_NUM_CURVES : '''
    ...
    def RGB_MASTER (self, *args, **kwargs):
      '''

Members:

  RGB_RED : 

  RGB_GREEN : 

  RGB_BLUE : 

  RGB_MASTER : 

  RGB_NUM_CURVES : '''
    ...
    def RGB_NUM_CURVES (self, *args, **kwargs):
      '''

Members:

  RGB_RED : 

  RGB_GREEN : 

  RGB_BLUE : 

  RGB_MASTER : 

  RGB_NUM_CURVES : '''
    ...
    def RGB_RED (self, *args, **kwargs):
      '''

Members:

  RGB_RED : 

  RGB_GREEN : 

  RGB_BLUE : 

  RGB_MASTER : 

  RGB_NUM_CURVES : '''
    ...
    def name (self, *args, **kwargs):
      '''name(self: handle) -> str
'''
    ...
    def value (self, *args, **kwargs):
      ''''''
    ...

def RGB_BLUE (*args):
      '''

'''      
    ...

def RGB_GREEN (*args):
      '''

'''      
    ...

def RGB_MASTER (*args):
      '''

'''      
    ...

def RGB_NUM_CURVES (*args):
      '''

'''      
    ...

def RGB_RED (*args):
      '''

'''      
    ...

def ROLE_COLOR_PICKING (*args):
      '''

'''      
    ...

def ROLE_COLOR_TIMING (*args):
      '''

'''      
    ...

def ROLE_COMPOSITING_LOG (*args):
      '''

'''      
    ...

def ROLE_DATA (*args):
      '''

'''      
    ...

def ROLE_DEFAULT (*args):
      '''

'''      
    ...

def ROLE_INTERCHANGE_DISPLAY (*args):
      '''

'''      
    ...

def ROLE_INTERCHANGE_SCENE (*args):
      '''

'''      
    ...

def ROLE_MATTE_PAINT (*args):
      '''

'''      
    ...

def ROLE_REFERENCE (*args):
      '''

'''      
    ...

def ROLE_RENDERING (*args):
      '''

'''      
    ...

def ROLE_SCENE_LINEAR (*args):
      '''

'''      
    ...

def ROLE_TEXTURE_PAINT (*args):
      '''

'''      
    ...

def RangeStyle (*args):
      '''

'''      
    ...

class RangeStyle:
    def RANGE_CLAMP (self, *args, **kwargs):
      '''

Members:

  RANGE_NO_CLAMP : 

  RANGE_CLAMP : '''
    ...
    def RANGE_NO_CLAMP (self, *args, **kwargs):
      '''

Members:

  RANGE_NO_CLAMP : 

  RANGE_CLAMP : '''
    ...
    def name (self, *args, **kwargs):
      '''name(self: handle) -> str
'''
    ...
    def value (self, *args, **kwargs):
      ''''''
    ...

def RangeStyleFromString (*args):
      '''

'''      
    ...

def RangeStyleToString (*args):
      '''

'''      
    ...

def RangeTransform (*args):
      '''

'''      
    ...

class RangeTransform:
    def equals (self, *args, **kwargs):
      '''equals(self: PyOpenColorIO.RangeTransform, other: PyOpenColorIO.RangeTransform) -> bool
'''
    ...
    def getDirection (self, *args, **kwargs):
      '''getDirection(self: PyOpenColorIO.Transform) -> PyOpenColorIO.TransformDirection
'''
    ...
    def getFileInputBitDepth (self, *args, **kwargs):
      '''getFileInputBitDepth(self: PyOpenColorIO.RangeTransform) -> PyOpenColorIO.BitDepth
'''
    ...
    def getFileOutputBitDepth (self, *args, **kwargs):
      '''getFileOutputBitDepth(self: PyOpenColorIO.RangeTransform) -> PyOpenColorIO.BitDepth
'''
    ...
    def getFormatMetadata (self, *args, **kwargs):
      '''getFormatMetadata(self: PyOpenColorIO.RangeTransform) -> PyOpenColorIO.FormatMetadata
'''
    ...
    def getMaxInValue (self, *args, **kwargs):
      '''getMaxInValue(self: PyOpenColorIO.RangeTransform) -> float
'''
    ...
    def getMaxOutValue (self, *args, **kwargs):
      '''getMaxOutValue(self: PyOpenColorIO.RangeTransform) -> float
'''
    ...
    def getMinInValue (self, *args, **kwargs):
      '''getMinInValue(self: PyOpenColorIO.RangeTransform) -> float
'''
    ...
    def getMinOutValue (self, *args, **kwargs):
      '''getMinOutValue(self: PyOpenColorIO.RangeTransform) -> float
'''
    ...
    def getStyle (self, *args, **kwargs):
      '''getStyle(self: PyOpenColorIO.RangeTransform) -> PyOpenColorIO.RangeStyle
'''
    ...
    def getTransformType (self, *args, **kwargs):
      '''getTransformType(self: PyOpenColorIO.Transform) -> PyOpenColorIO.TransformType
'''
    ...
    def hasMaxInValue (self, *args, **kwargs):
      '''hasMaxInValue(self: PyOpenColorIO.RangeTransform) -> bool
'''
    ...
    def hasMaxOutValue (self, *args, **kwargs):
      '''hasMaxOutValue(self: PyOpenColorIO.RangeTransform) -> bool
'''
    ...
    def hasMinInValue (self, *args, **kwargs):
      '''hasMinInValue(self: PyOpenColorIO.RangeTransform) -> bool
'''
    ...
    def hasMinOutValue (self, *args, **kwargs):
      '''hasMinOutValue(self: PyOpenColorIO.RangeTransform) -> bool
'''
    ...
    def setDirection (self, *args, **kwargs):
      '''setDirection(self: PyOpenColorIO.Transform, direction: PyOpenColorIO.TransformDirection) -> None
'''
    ...
    def setFileInputBitDepth (self, *args, **kwargs):
      '''setFileInputBitDepth(self: PyOpenColorIO.RangeTransform, bitDepth: PyOpenColorIO.BitDepth) -> None
'''
    ...
    def setFileOutputBitDepth (self, *args, **kwargs):
      '''setFileOutputBitDepth(self: PyOpenColorIO.RangeTransform, bitDepth: PyOpenColorIO.BitDepth) -> None
'''
    ...
    def setMaxInValue (self, *args, **kwargs):
      '''setMaxInValue(self: PyOpenColorIO.RangeTransform, value: float) -> None
'''
    ...
    def setMaxOutValue (self, *args, **kwargs):
      '''setMaxOutValue(self: PyOpenColorIO.RangeTransform, value: float) -> None
'''
    ...
    def setMinInValue (self, *args, **kwargs):
      '''setMinInValue(self: PyOpenColorIO.RangeTransform, value: float) -> None
'''
    ...
    def setMinOutValue (self, *args, **kwargs):
      '''setMinOutValue(self: PyOpenColorIO.RangeTransform, value: float) -> None
'''
    ...
    def setStyle (self, *args, **kwargs):
      '''setStyle(self: PyOpenColorIO.RangeTransform, style: PyOpenColorIO.RangeStyle) -> None
'''
    ...
    def unsetMaxInValue (self, *args, **kwargs):
      '''unsetMaxInValue(self: PyOpenColorIO.RangeTransform) -> None
'''
    ...
    def unsetMaxOutValue (self, *args, **kwargs):
      '''unsetMaxOutValue(self: PyOpenColorIO.RangeTransform) -> None
'''
    ...
    def unsetMinInValue (self, *args, **kwargs):
      '''unsetMinInValue(self: PyOpenColorIO.RangeTransform) -> None
'''
    ...
    def unsetMinOutValue (self, *args, **kwargs):
      '''unsetMinOutValue(self: PyOpenColorIO.RangeTransform) -> None
'''
    ...
    def validate (self, *args, **kwargs):
      '''validate(self: PyOpenColorIO.Transform) -> None
'''
    ...

def ReferenceSpaceType (*args):
      '''

'''      
    ...

class ReferenceSpaceType:
    def REFERENCE_SPACE_DISPLAY (self, *args, **kwargs):
      '''

Members:

  REFERENCE_SPACE_SCENE : 

  REFERENCE_SPACE_DISPLAY : '''
    ...
    def REFERENCE_SPACE_SCENE (self, *args, **kwargs):
      '''

Members:

  REFERENCE_SPACE_SCENE : 

  REFERENCE_SPACE_DISPLAY : '''
    ...
    def name (self, *args, **kwargs):
      '''name(self: handle) -> str
'''
    ...
    def value (self, *args, **kwargs):
      ''''''
    ...

def ResetComputeHashFunction (*args):
      '''

'''      
    ...

def ResetToDefaultLoggingFunction (*args):
      '''

'''      
    ...

def SEARCH_REFERENCE_SPACE_ALL (*args):
      '''

'''      
    ...

def SEARCH_REFERENCE_SPACE_DISPLAY (*args):
      '''

'''      
    ...

def SEARCH_REFERENCE_SPACE_SCENE (*args):
      '''

'''      
    ...

def SearchReferenceSpaceType (*args):
      '''

'''      
    ...

class SearchReferenceSpaceType:
    def SEARCH_REFERENCE_SPACE_ALL (self, *args, **kwargs):
      '''

Members:

  SEARCH_REFERENCE_SPACE_SCENE : 

  SEARCH_REFERENCE_SPACE_DISPLAY : 

  SEARCH_REFERENCE_SPACE_ALL : '''
    ...
    def SEARCH_REFERENCE_SPACE_DISPLAY (self, *args, **kwargs):
      '''

Members:

  SEARCH_REFERENCE_SPACE_SCENE : 

  SEARCH_REFERENCE_SPACE_DISPLAY : 

  SEARCH_REFERENCE_SPACE_ALL : '''
    ...
    def SEARCH_REFERENCE_SPACE_SCENE (self, *args, **kwargs):
      '''

Members:

  SEARCH_REFERENCE_SPACE_SCENE : 

  SEARCH_REFERENCE_SPACE_DISPLAY : 

  SEARCH_REFERENCE_SPACE_ALL : '''
    ...
    def name (self, *args, **kwargs):
      '''name(self: handle) -> str
'''
    ...
    def value (self, *args, **kwargs):
      ''''''
    ...

def SetComputeHashFunction (*args):
      '''

'''      
    ...

def SetCurrentConfig (*args):
      '''

'''      
    ...

def SetEnvVariable (*args):
      '''

'''      
    ...

def SetLoggingFunction (*args):
      '''

'''      
    ...

def SetLoggingLevel (*args):
      '''

'''      
    ...

def SystemMonitors (*args):
      '''

'''      
    ...

class SystemMonitors:
    def MonitorIterator (self, *args, **kwargs):
      '''None'''
    ...
    def getMonitors (self, *args, **kwargs):
      '''getMonitors(self: PyOpenColorIO.SystemMonitors) -> PyOpenColorIO.SystemMonitors.MonitorIterator
'''
    ...

def TRANSFORM_DIR_FORWARD (*args):
      '''

'''      
    ...

def TRANSFORM_DIR_INVERSE (*args):
      '''

'''      
    ...

def TRANSFORM_TYPE_ALLOCATION (*args):
      '''

'''      
    ...

def TRANSFORM_TYPE_BUILTIN (*args):
      '''

'''      
    ...

def TRANSFORM_TYPE_CDL (*args):
      '''

'''      
    ...

def TRANSFORM_TYPE_COLORSPACE (*args):
      '''

'''      
    ...

def TRANSFORM_TYPE_DISPLAY_VIEW (*args):
      '''

'''      
    ...

def TRANSFORM_TYPE_EXPONENT (*args):
      '''

'''      
    ...

def TRANSFORM_TYPE_EXPONENT_WITH_LINEAR (*args):
      '''

'''      
    ...

def TRANSFORM_TYPE_EXPOSURE_CONTRAST (*args):
      '''

'''      
    ...

def TRANSFORM_TYPE_FILE (*args):
      '''

'''      
    ...

def TRANSFORM_TYPE_FIXED_FUNCTION (*args):
      '''

'''      
    ...

def TRANSFORM_TYPE_GRADING_PRIMARY (*args):
      '''

'''      
    ...

def TRANSFORM_TYPE_GRADING_RGB_CURVE (*args):
      '''

'''      
    ...

def TRANSFORM_TYPE_GRADING_TONE (*args):
      '''

'''      
    ...

def TRANSFORM_TYPE_GROUP (*args):
      '''

'''      
    ...

def TRANSFORM_TYPE_LOG (*args):
      '''

'''      
    ...

def TRANSFORM_TYPE_LOG_AFFINE (*args):
      '''

'''      
    ...

def TRANSFORM_TYPE_LOG_CAMERA (*args):
      '''

'''      
    ...

def TRANSFORM_TYPE_LOOK (*args):
      '''

'''      
    ...

def TRANSFORM_TYPE_LUT1D (*args):
      '''

'''      
    ...

def TRANSFORM_TYPE_LUT3D (*args):
      '''

'''      
    ...

def TRANSFORM_TYPE_MATRIX (*args):
      '''

'''      
    ...

def TRANSFORM_TYPE_RANGE (*args):
      '''

'''      
    ...

def Transform (*args):
      '''

'''      
    ...

class Transform:
    def getDirection (self, *args, **kwargs):
      '''getDirection(self: PyOpenColorIO.Transform) -> PyOpenColorIO.TransformDirection
'''
    ...
    def getTransformType (self, *args, **kwargs):
      '''getTransformType(self: PyOpenColorIO.Transform) -> PyOpenColorIO.TransformType
'''
    ...
    def setDirection (self, *args, **kwargs):
      '''setDirection(self: PyOpenColorIO.Transform, direction: PyOpenColorIO.TransformDirection) -> None
'''
    ...
    def validate (self, *args, **kwargs):
      '''validate(self: PyOpenColorIO.Transform) -> None
'''
    ...

def TransformDirection (*args):
      '''

'''      
    ...

class TransformDirection:
    def TRANSFORM_DIR_FORWARD (self, *args, **kwargs):
      '''

Members:

  TRANSFORM_DIR_FORWARD : 

  TRANSFORM_DIR_INVERSE : '''
    ...
    def TRANSFORM_DIR_INVERSE (self, *args, **kwargs):
      '''

Members:

  TRANSFORM_DIR_FORWARD : 

  TRANSFORM_DIR_INVERSE : '''
    ...
    def name (self, *args, **kwargs):
      '''name(self: handle) -> str
'''
    ...
    def value (self, *args, **kwargs):
      ''''''
    ...

def TransformDirectionFromString (*args):
      '''

'''      
    ...

def TransformDirectionToString (*args):
      '''

'''      
    ...

def TransformType (*args):
      '''

'''      
    ...

class TransformType:
    def TRANSFORM_TYPE_ALLOCATION (self, *args, **kwargs):
      '''

Members:

  TRANSFORM_TYPE_ALLOCATION : 

  TRANSFORM_TYPE_BUILTIN : 

  TRANSFORM_TYPE_CDL : 

  TRANSFORM_TYPE_COLORSPACE : 

  TRANSFORM_TYPE_DISPLAY_VIEW : 

  TRANSFORM_TYPE_EXPONENT : 

  TRANSFORM_TYPE_EXPONENT_WITH_LINEAR : 

  TRANSFORM_TYPE_EXPOSURE_CONTRAST : 

  TRANSFORM_TYPE_FILE : 

  TRANSFORM_TYPE_FIXED_FUNCTION : 

  TRANSFORM_TYPE_GRADING_PRIMARY : 

  TRANSFORM_TYPE_GRADING_RGB_CURVE : 

  TRANSFORM_TYPE_GRADING_TONE : 

  TRANSFORM_TYPE_GROUP : 

  TRANSFORM_TYPE_LOG_AFFINE : 

  TRANSFORM_TYPE_LOG_CAMERA : 

  TRANSFORM_TYPE_LOG : 

  TRANSFORM_TYPE_LOOK : 

  TRANSFORM_TYPE_LUT1D : 

  TRANSFORM_TYPE_LUT3D : 

  TRANSFORM_TYPE_MATRIX : 

  TRANSFORM_TYPE_RANGE : '''
    ...
    def TRANSFORM_TYPE_BUILTIN (self, *args, **kwargs):
      '''

Members:

  TRANSFORM_TYPE_ALLOCATION : 

  TRANSFORM_TYPE_BUILTIN : 

  TRANSFORM_TYPE_CDL : 

  TRANSFORM_TYPE_COLORSPACE : 

  TRANSFORM_TYPE_DISPLAY_VIEW : 

  TRANSFORM_TYPE_EXPONENT : 

  TRANSFORM_TYPE_EXPONENT_WITH_LINEAR : 

  TRANSFORM_TYPE_EXPOSURE_CONTRAST : 

  TRANSFORM_TYPE_FILE : 

  TRANSFORM_TYPE_FIXED_FUNCTION : 

  TRANSFORM_TYPE_GRADING_PRIMARY : 

  TRANSFORM_TYPE_GRADING_RGB_CURVE : 

  TRANSFORM_TYPE_GRADING_TONE : 

  TRANSFORM_TYPE_GROUP : 

  TRANSFORM_TYPE_LOG_AFFINE : 

  TRANSFORM_TYPE_LOG_CAMERA : 

  TRANSFORM_TYPE_LOG : 

  TRANSFORM_TYPE_LOOK : 

  TRANSFORM_TYPE_LUT1D : 

  TRANSFORM_TYPE_LUT3D : 

  TRANSFORM_TYPE_MATRIX : 

  TRANSFORM_TYPE_RANGE : '''
    ...
    def TRANSFORM_TYPE_CDL (self, *args, **kwargs):
      '''

Members:

  TRANSFORM_TYPE_ALLOCATION : 

  TRANSFORM_TYPE_BUILTIN : 

  TRANSFORM_TYPE_CDL : 

  TRANSFORM_TYPE_COLORSPACE : 

  TRANSFORM_TYPE_DISPLAY_VIEW : 

  TRANSFORM_TYPE_EXPONENT : 

  TRANSFORM_TYPE_EXPONENT_WITH_LINEAR : 

  TRANSFORM_TYPE_EXPOSURE_CONTRAST : 

  TRANSFORM_TYPE_FILE : 

  TRANSFORM_TYPE_FIXED_FUNCTION : 

  TRANSFORM_TYPE_GRADING_PRIMARY : 

  TRANSFORM_TYPE_GRADING_RGB_CURVE : 

  TRANSFORM_TYPE_GRADING_TONE : 

  TRANSFORM_TYPE_GROUP : 

  TRANSFORM_TYPE_LOG_AFFINE : 

  TRANSFORM_TYPE_LOG_CAMERA : 

  TRANSFORM_TYPE_LOG : 

  TRANSFORM_TYPE_LOOK : 

  TRANSFORM_TYPE_LUT1D : 

  TRANSFORM_TYPE_LUT3D : 

  TRANSFORM_TYPE_MATRIX : 

  TRANSFORM_TYPE_RANGE : '''
    ...
    def TRANSFORM_TYPE_COLORSPACE (self, *args, **kwargs):
      '''

Members:

  TRANSFORM_TYPE_ALLOCATION : 

  TRANSFORM_TYPE_BUILTIN : 

  TRANSFORM_TYPE_CDL : 

  TRANSFORM_TYPE_COLORSPACE : 

  TRANSFORM_TYPE_DISPLAY_VIEW : 

  TRANSFORM_TYPE_EXPONENT : 

  TRANSFORM_TYPE_EXPONENT_WITH_LINEAR : 

  TRANSFORM_TYPE_EXPOSURE_CONTRAST : 

  TRANSFORM_TYPE_FILE : 

  TRANSFORM_TYPE_FIXED_FUNCTION : 

  TRANSFORM_TYPE_GRADING_PRIMARY : 

  TRANSFORM_TYPE_GRADING_RGB_CURVE : 

  TRANSFORM_TYPE_GRADING_TONE : 

  TRANSFORM_TYPE_GROUP : 

  TRANSFORM_TYPE_LOG_AFFINE : 

  TRANSFORM_TYPE_LOG_CAMERA : 

  TRANSFORM_TYPE_LOG : 

  TRANSFORM_TYPE_LOOK : 

  TRANSFORM_TYPE_LUT1D : 

  TRANSFORM_TYPE_LUT3D : 

  TRANSFORM_TYPE_MATRIX : 

  TRANSFORM_TYPE_RANGE : '''
    ...
    def TRANSFORM_TYPE_DISPLAY_VIEW (self, *args, **kwargs):
      '''

Members:

  TRANSFORM_TYPE_ALLOCATION : 

  TRANSFORM_TYPE_BUILTIN : 

  TRANSFORM_TYPE_CDL : 

  TRANSFORM_TYPE_COLORSPACE : 

  TRANSFORM_TYPE_DISPLAY_VIEW : 

  TRANSFORM_TYPE_EXPONENT : 

  TRANSFORM_TYPE_EXPONENT_WITH_LINEAR : 

  TRANSFORM_TYPE_EXPOSURE_CONTRAST : 

  TRANSFORM_TYPE_FILE : 

  TRANSFORM_TYPE_FIXED_FUNCTION : 

  TRANSFORM_TYPE_GRADING_PRIMARY : 

  TRANSFORM_TYPE_GRADING_RGB_CURVE : 

  TRANSFORM_TYPE_GRADING_TONE : 

  TRANSFORM_TYPE_GROUP : 

  TRANSFORM_TYPE_LOG_AFFINE : 

  TRANSFORM_TYPE_LOG_CAMERA : 

  TRANSFORM_TYPE_LOG : 

  TRANSFORM_TYPE_LOOK : 

  TRANSFORM_TYPE_LUT1D : 

  TRANSFORM_TYPE_LUT3D : 

  TRANSFORM_TYPE_MATRIX : 

  TRANSFORM_TYPE_RANGE : '''
    ...
    def TRANSFORM_TYPE_EXPONENT (self, *args, **kwargs):
      '''

Members:

  TRANSFORM_TYPE_ALLOCATION : 

  TRANSFORM_TYPE_BUILTIN : 

  TRANSFORM_TYPE_CDL : 

  TRANSFORM_TYPE_COLORSPACE : 

  TRANSFORM_TYPE_DISPLAY_VIEW : 

  TRANSFORM_TYPE_EXPONENT : 

  TRANSFORM_TYPE_EXPONENT_WITH_LINEAR : 

  TRANSFORM_TYPE_EXPOSURE_CONTRAST : 

  TRANSFORM_TYPE_FILE : 

  TRANSFORM_TYPE_FIXED_FUNCTION : 

  TRANSFORM_TYPE_GRADING_PRIMARY : 

  TRANSFORM_TYPE_GRADING_RGB_CURVE : 

  TRANSFORM_TYPE_GRADING_TONE : 

  TRANSFORM_TYPE_GROUP : 

  TRANSFORM_TYPE_LOG_AFFINE : 

  TRANSFORM_TYPE_LOG_CAMERA : 

  TRANSFORM_TYPE_LOG : 

  TRANSFORM_TYPE_LOOK : 

  TRANSFORM_TYPE_LUT1D : 

  TRANSFORM_TYPE_LUT3D : 

  TRANSFORM_TYPE_MATRIX : 

  TRANSFORM_TYPE_RANGE : '''
    ...
    def TRANSFORM_TYPE_EXPONENT_WITH_LINEAR (self, *args, **kwargs):
      '''

Members:

  TRANSFORM_TYPE_ALLOCATION : 

  TRANSFORM_TYPE_BUILTIN : 

  TRANSFORM_TYPE_CDL : 

  TRANSFORM_TYPE_COLORSPACE : 

  TRANSFORM_TYPE_DISPLAY_VIEW : 

  TRANSFORM_TYPE_EXPONENT : 

  TRANSFORM_TYPE_EXPONENT_WITH_LINEAR : 

  TRANSFORM_TYPE_EXPOSURE_CONTRAST : 

  TRANSFORM_TYPE_FILE : 

  TRANSFORM_TYPE_FIXED_FUNCTION : 

  TRANSFORM_TYPE_GRADING_PRIMARY : 

  TRANSFORM_TYPE_GRADING_RGB_CURVE : 

  TRANSFORM_TYPE_GRADING_TONE : 

  TRANSFORM_TYPE_GROUP : 

  TRANSFORM_TYPE_LOG_AFFINE : 

  TRANSFORM_TYPE_LOG_CAMERA : 

  TRANSFORM_TYPE_LOG : 

  TRANSFORM_TYPE_LOOK : 

  TRANSFORM_TYPE_LUT1D : 

  TRANSFORM_TYPE_LUT3D : 

  TRANSFORM_TYPE_MATRIX : 

  TRANSFORM_TYPE_RANGE : '''
    ...
    def TRANSFORM_TYPE_EXPOSURE_CONTRAST (self, *args, **kwargs):
      '''

Members:

  TRANSFORM_TYPE_ALLOCATION : 

  TRANSFORM_TYPE_BUILTIN : 

  TRANSFORM_TYPE_CDL : 

  TRANSFORM_TYPE_COLORSPACE : 

  TRANSFORM_TYPE_DISPLAY_VIEW : 

  TRANSFORM_TYPE_EXPONENT : 

  TRANSFORM_TYPE_EXPONENT_WITH_LINEAR : 

  TRANSFORM_TYPE_EXPOSURE_CONTRAST : 

  TRANSFORM_TYPE_FILE : 

  TRANSFORM_TYPE_FIXED_FUNCTION : 

  TRANSFORM_TYPE_GRADING_PRIMARY : 

  TRANSFORM_TYPE_GRADING_RGB_CURVE : 

  TRANSFORM_TYPE_GRADING_TONE : 

  TRANSFORM_TYPE_GROUP : 

  TRANSFORM_TYPE_LOG_AFFINE : 

  TRANSFORM_TYPE_LOG_CAMERA : 

  TRANSFORM_TYPE_LOG : 

  TRANSFORM_TYPE_LOOK : 

  TRANSFORM_TYPE_LUT1D : 

  TRANSFORM_TYPE_LUT3D : 

  TRANSFORM_TYPE_MATRIX : 

  TRANSFORM_TYPE_RANGE : '''
    ...
    def TRANSFORM_TYPE_FILE (self, *args, **kwargs):
      '''

Members:

  TRANSFORM_TYPE_ALLOCATION : 

  TRANSFORM_TYPE_BUILTIN : 

  TRANSFORM_TYPE_CDL : 

  TRANSFORM_TYPE_COLORSPACE : 

  TRANSFORM_TYPE_DISPLAY_VIEW : 

  TRANSFORM_TYPE_EXPONENT : 

  TRANSFORM_TYPE_EXPONENT_WITH_LINEAR : 

  TRANSFORM_TYPE_EXPOSURE_CONTRAST : 

  TRANSFORM_TYPE_FILE : 

  TRANSFORM_TYPE_FIXED_FUNCTION : 

  TRANSFORM_TYPE_GRADING_PRIMARY : 

  TRANSFORM_TYPE_GRADING_RGB_CURVE : 

  TRANSFORM_TYPE_GRADING_TONE : 

  TRANSFORM_TYPE_GROUP : 

  TRANSFORM_TYPE_LOG_AFFINE : 

  TRANSFORM_TYPE_LOG_CAMERA : 

  TRANSFORM_TYPE_LOG : 

  TRANSFORM_TYPE_LOOK : 

  TRANSFORM_TYPE_LUT1D : 

  TRANSFORM_TYPE_LUT3D : 

  TRANSFORM_TYPE_MATRIX : 

  TRANSFORM_TYPE_RANGE : '''
    ...
    def TRANSFORM_TYPE_FIXED_FUNCTION (self, *args, **kwargs):
      '''

Members:

  TRANSFORM_TYPE_ALLOCATION : 

  TRANSFORM_TYPE_BUILTIN : 

  TRANSFORM_TYPE_CDL : 

  TRANSFORM_TYPE_COLORSPACE : 

  TRANSFORM_TYPE_DISPLAY_VIEW : 

  TRANSFORM_TYPE_EXPONENT : 

  TRANSFORM_TYPE_EXPONENT_WITH_LINEAR : 

  TRANSFORM_TYPE_EXPOSURE_CONTRAST : 

  TRANSFORM_TYPE_FILE : 

  TRANSFORM_TYPE_FIXED_FUNCTION : 

  TRANSFORM_TYPE_GRADING_PRIMARY : 

  TRANSFORM_TYPE_GRADING_RGB_CURVE : 

  TRANSFORM_TYPE_GRADING_TONE : 

  TRANSFORM_TYPE_GROUP : 

  TRANSFORM_TYPE_LOG_AFFINE : 

  TRANSFORM_TYPE_LOG_CAMERA : 

  TRANSFORM_TYPE_LOG : 

  TRANSFORM_TYPE_LOOK : 

  TRANSFORM_TYPE_LUT1D : 

  TRANSFORM_TYPE_LUT3D : 

  TRANSFORM_TYPE_MATRIX : 

  TRANSFORM_TYPE_RANGE : '''
    ...
    def TRANSFORM_TYPE_GRADING_PRIMARY (self, *args, **kwargs):
      '''

Members:

  TRANSFORM_TYPE_ALLOCATION : 

  TRANSFORM_TYPE_BUILTIN : 

  TRANSFORM_TYPE_CDL : 

  TRANSFORM_TYPE_COLORSPACE : 

  TRANSFORM_TYPE_DISPLAY_VIEW : 

  TRANSFORM_TYPE_EXPONENT : 

  TRANSFORM_TYPE_EXPONENT_WITH_LINEAR : 

  TRANSFORM_TYPE_EXPOSURE_CONTRAST : 

  TRANSFORM_TYPE_FILE : 

  TRANSFORM_TYPE_FIXED_FUNCTION : 

  TRANSFORM_TYPE_GRADING_PRIMARY : 

  TRANSFORM_TYPE_GRADING_RGB_CURVE : 

  TRANSFORM_TYPE_GRADING_TONE : 

  TRANSFORM_TYPE_GROUP : 

  TRANSFORM_TYPE_LOG_AFFINE : 

  TRANSFORM_TYPE_LOG_CAMERA : 

  TRANSFORM_TYPE_LOG : 

  TRANSFORM_TYPE_LOOK : 

  TRANSFORM_TYPE_LUT1D : 

  TRANSFORM_TYPE_LUT3D : 

  TRANSFORM_TYPE_MATRIX : 

  TRANSFORM_TYPE_RANGE : '''
    ...
    def TRANSFORM_TYPE_GRADING_RGB_CURVE (self, *args, **kwargs):
      '''

Members:

  TRANSFORM_TYPE_ALLOCATION : 

  TRANSFORM_TYPE_BUILTIN : 

  TRANSFORM_TYPE_CDL : 

  TRANSFORM_TYPE_COLORSPACE : 

  TRANSFORM_TYPE_DISPLAY_VIEW : 

  TRANSFORM_TYPE_EXPONENT : 

  TRANSFORM_TYPE_EXPONENT_WITH_LINEAR : 

  TRANSFORM_TYPE_EXPOSURE_CONTRAST : 

  TRANSFORM_TYPE_FILE : 

  TRANSFORM_TYPE_FIXED_FUNCTION : 

  TRANSFORM_TYPE_GRADING_PRIMARY : 

  TRANSFORM_TYPE_GRADING_RGB_CURVE : 

  TRANSFORM_TYPE_GRADING_TONE : 

  TRANSFORM_TYPE_GROUP : 

  TRANSFORM_TYPE_LOG_AFFINE : 

  TRANSFORM_TYPE_LOG_CAMERA : 

  TRANSFORM_TYPE_LOG : 

  TRANSFORM_TYPE_LOOK : 

  TRANSFORM_TYPE_LUT1D : 

  TRANSFORM_TYPE_LUT3D : 

  TRANSFORM_TYPE_MATRIX : 

  TRANSFORM_TYPE_RANGE : '''
    ...
    def TRANSFORM_TYPE_GRADING_TONE (self, *args, **kwargs):
      '''

Members:

  TRANSFORM_TYPE_ALLOCATION : 

  TRANSFORM_TYPE_BUILTIN : 

  TRANSFORM_TYPE_CDL : 

  TRANSFORM_TYPE_COLORSPACE : 

  TRANSFORM_TYPE_DISPLAY_VIEW : 

  TRANSFORM_TYPE_EXPONENT : 

  TRANSFORM_TYPE_EXPONENT_WITH_LINEAR : 

  TRANSFORM_TYPE_EXPOSURE_CONTRAST : 

  TRANSFORM_TYPE_FILE : 

  TRANSFORM_TYPE_FIXED_FUNCTION : 

  TRANSFORM_TYPE_GRADING_PRIMARY : 

  TRANSFORM_TYPE_GRADING_RGB_CURVE : 

  TRANSFORM_TYPE_GRADING_TONE : 

  TRANSFORM_TYPE_GROUP : 

  TRANSFORM_TYPE_LOG_AFFINE : 

  TRANSFORM_TYPE_LOG_CAMERA : 

  TRANSFORM_TYPE_LOG : 

  TRANSFORM_TYPE_LOOK : 

  TRANSFORM_TYPE_LUT1D : 

  TRANSFORM_TYPE_LUT3D : 

  TRANSFORM_TYPE_MATRIX : 

  TRANSFORM_TYPE_RANGE : '''
    ...
    def TRANSFORM_TYPE_GROUP (self, *args, **kwargs):
      '''

Members:

  TRANSFORM_TYPE_ALLOCATION : 

  TRANSFORM_TYPE_BUILTIN : 

  TRANSFORM_TYPE_CDL : 

  TRANSFORM_TYPE_COLORSPACE : 

  TRANSFORM_TYPE_DISPLAY_VIEW : 

  TRANSFORM_TYPE_EXPONENT : 

  TRANSFORM_TYPE_EXPONENT_WITH_LINEAR : 

  TRANSFORM_TYPE_EXPOSURE_CONTRAST : 

  TRANSFORM_TYPE_FILE : 

  TRANSFORM_TYPE_FIXED_FUNCTION : 

  TRANSFORM_TYPE_GRADING_PRIMARY : 

  TRANSFORM_TYPE_GRADING_RGB_CURVE : 

  TRANSFORM_TYPE_GRADING_TONE : 

  TRANSFORM_TYPE_GROUP : 

  TRANSFORM_TYPE_LOG_AFFINE : 

  TRANSFORM_TYPE_LOG_CAMERA : 

  TRANSFORM_TYPE_LOG : 

  TRANSFORM_TYPE_LOOK : 

  TRANSFORM_TYPE_LUT1D : 

  TRANSFORM_TYPE_LUT3D : 

  TRANSFORM_TYPE_MATRIX : 

  TRANSFORM_TYPE_RANGE : '''
    ...
    def TRANSFORM_TYPE_LOG (self, *args, **kwargs):
      '''

Members:

  TRANSFORM_TYPE_ALLOCATION : 

  TRANSFORM_TYPE_BUILTIN : 

  TRANSFORM_TYPE_CDL : 

  TRANSFORM_TYPE_COLORSPACE : 

  TRANSFORM_TYPE_DISPLAY_VIEW : 

  TRANSFORM_TYPE_EXPONENT : 

  TRANSFORM_TYPE_EXPONENT_WITH_LINEAR : 

  TRANSFORM_TYPE_EXPOSURE_CONTRAST : 

  TRANSFORM_TYPE_FILE : 

  TRANSFORM_TYPE_FIXED_FUNCTION : 

  TRANSFORM_TYPE_GRADING_PRIMARY : 

  TRANSFORM_TYPE_GRADING_RGB_CURVE : 

  TRANSFORM_TYPE_GRADING_TONE : 

  TRANSFORM_TYPE_GROUP : 

  TRANSFORM_TYPE_LOG_AFFINE : 

  TRANSFORM_TYPE_LOG_CAMERA : 

  TRANSFORM_TYPE_LOG : 

  TRANSFORM_TYPE_LOOK : 

  TRANSFORM_TYPE_LUT1D : 

  TRANSFORM_TYPE_LUT3D : 

  TRANSFORM_TYPE_MATRIX : 

  TRANSFORM_TYPE_RANGE : '''
    ...
    def TRANSFORM_TYPE_LOG_AFFINE (self, *args, **kwargs):
      '''

Members:

  TRANSFORM_TYPE_ALLOCATION : 

  TRANSFORM_TYPE_BUILTIN : 

  TRANSFORM_TYPE_CDL : 

  TRANSFORM_TYPE_COLORSPACE : 

  TRANSFORM_TYPE_DISPLAY_VIEW : 

  TRANSFORM_TYPE_EXPONENT : 

  TRANSFORM_TYPE_EXPONENT_WITH_LINEAR : 

  TRANSFORM_TYPE_EXPOSURE_CONTRAST : 

  TRANSFORM_TYPE_FILE : 

  TRANSFORM_TYPE_FIXED_FUNCTION : 

  TRANSFORM_TYPE_GRADING_PRIMARY : 

  TRANSFORM_TYPE_GRADING_RGB_CURVE : 

  TRANSFORM_TYPE_GRADING_TONE : 

  TRANSFORM_TYPE_GROUP : 

  TRANSFORM_TYPE_LOG_AFFINE : 

  TRANSFORM_TYPE_LOG_CAMERA : 

  TRANSFORM_TYPE_LOG : 

  TRANSFORM_TYPE_LOOK : 

  TRANSFORM_TYPE_LUT1D : 

  TRANSFORM_TYPE_LUT3D : 

  TRANSFORM_TYPE_MATRIX : 

  TRANSFORM_TYPE_RANGE : '''
    ...
    def TRANSFORM_TYPE_LOG_CAMERA (self, *args, **kwargs):
      '''

Members:

  TRANSFORM_TYPE_ALLOCATION : 

  TRANSFORM_TYPE_BUILTIN : 

  TRANSFORM_TYPE_CDL : 

  TRANSFORM_TYPE_COLORSPACE : 

  TRANSFORM_TYPE_DISPLAY_VIEW : 

  TRANSFORM_TYPE_EXPONENT : 

  TRANSFORM_TYPE_EXPONENT_WITH_LINEAR : 

  TRANSFORM_TYPE_EXPOSURE_CONTRAST : 

  TRANSFORM_TYPE_FILE : 

  TRANSFORM_TYPE_FIXED_FUNCTION : 

  TRANSFORM_TYPE_GRADING_PRIMARY : 

  TRANSFORM_TYPE_GRADING_RGB_CURVE : 

  TRANSFORM_TYPE_GRADING_TONE : 

  TRANSFORM_TYPE_GROUP : 

  TRANSFORM_TYPE_LOG_AFFINE : 

  TRANSFORM_TYPE_LOG_CAMERA : 

  TRANSFORM_TYPE_LOG : 

  TRANSFORM_TYPE_LOOK : 

  TRANSFORM_TYPE_LUT1D : 

  TRANSFORM_TYPE_LUT3D : 

  TRANSFORM_TYPE_MATRIX : 

  TRANSFORM_TYPE_RANGE : '''
    ...
    def TRANSFORM_TYPE_LOOK (self, *args, **kwargs):
      '''

Members:

  TRANSFORM_TYPE_ALLOCATION : 

  TRANSFORM_TYPE_BUILTIN : 

  TRANSFORM_TYPE_CDL : 

  TRANSFORM_TYPE_COLORSPACE : 

  TRANSFORM_TYPE_DISPLAY_VIEW : 

  TRANSFORM_TYPE_EXPONENT : 

  TRANSFORM_TYPE_EXPONENT_WITH_LINEAR : 

  TRANSFORM_TYPE_EXPOSURE_CONTRAST : 

  TRANSFORM_TYPE_FILE : 

  TRANSFORM_TYPE_FIXED_FUNCTION : 

  TRANSFORM_TYPE_GRADING_PRIMARY : 

  TRANSFORM_TYPE_GRADING_RGB_CURVE : 

  TRANSFORM_TYPE_GRADING_TONE : 

  TRANSFORM_TYPE_GROUP : 

  TRANSFORM_TYPE_LOG_AFFINE : 

  TRANSFORM_TYPE_LOG_CAMERA : 

  TRANSFORM_TYPE_LOG : 

  TRANSFORM_TYPE_LOOK : 

  TRANSFORM_TYPE_LUT1D : 

  TRANSFORM_TYPE_LUT3D : 

  TRANSFORM_TYPE_MATRIX : 

  TRANSFORM_TYPE_RANGE : '''
    ...
    def TRANSFORM_TYPE_LUT1D (self, *args, **kwargs):
      '''

Members:

  TRANSFORM_TYPE_ALLOCATION : 

  TRANSFORM_TYPE_BUILTIN : 

  TRANSFORM_TYPE_CDL : 

  TRANSFORM_TYPE_COLORSPACE : 

  TRANSFORM_TYPE_DISPLAY_VIEW : 

  TRANSFORM_TYPE_EXPONENT : 

  TRANSFORM_TYPE_EXPONENT_WITH_LINEAR : 

  TRANSFORM_TYPE_EXPOSURE_CONTRAST : 

  TRANSFORM_TYPE_FILE : 

  TRANSFORM_TYPE_FIXED_FUNCTION : 

  TRANSFORM_TYPE_GRADING_PRIMARY : 

  TRANSFORM_TYPE_GRADING_RGB_CURVE : 

  TRANSFORM_TYPE_GRADING_TONE : 

  TRANSFORM_TYPE_GROUP : 

  TRANSFORM_TYPE_LOG_AFFINE : 

  TRANSFORM_TYPE_LOG_CAMERA : 

  TRANSFORM_TYPE_LOG : 

  TRANSFORM_TYPE_LOOK : 

  TRANSFORM_TYPE_LUT1D : 

  TRANSFORM_TYPE_LUT3D : 

  TRANSFORM_TYPE_MATRIX : 

  TRANSFORM_TYPE_RANGE : '''
    ...
    def TRANSFORM_TYPE_LUT3D (self, *args, **kwargs):
      '''

Members:

  TRANSFORM_TYPE_ALLOCATION : 

  TRANSFORM_TYPE_BUILTIN : 

  TRANSFORM_TYPE_CDL : 

  TRANSFORM_TYPE_COLORSPACE : 

  TRANSFORM_TYPE_DISPLAY_VIEW : 

  TRANSFORM_TYPE_EXPONENT : 

  TRANSFORM_TYPE_EXPONENT_WITH_LINEAR : 

  TRANSFORM_TYPE_EXPOSURE_CONTRAST : 

  TRANSFORM_TYPE_FILE : 

  TRANSFORM_TYPE_FIXED_FUNCTION : 

  TRANSFORM_TYPE_GRADING_PRIMARY : 

  TRANSFORM_TYPE_GRADING_RGB_CURVE : 

  TRANSFORM_TYPE_GRADING_TONE : 

  TRANSFORM_TYPE_GROUP : 

  TRANSFORM_TYPE_LOG_AFFINE : 

  TRANSFORM_TYPE_LOG_CAMERA : 

  TRANSFORM_TYPE_LOG : 

  TRANSFORM_TYPE_LOOK : 

  TRANSFORM_TYPE_LUT1D : 

  TRANSFORM_TYPE_LUT3D : 

  TRANSFORM_TYPE_MATRIX : 

  TRANSFORM_TYPE_RANGE : '''
    ...
    def TRANSFORM_TYPE_MATRIX (self, *args, **kwargs):
      '''

Members:

  TRANSFORM_TYPE_ALLOCATION : 

  TRANSFORM_TYPE_BUILTIN : 

  TRANSFORM_TYPE_CDL : 

  TRANSFORM_TYPE_COLORSPACE : 

  TRANSFORM_TYPE_DISPLAY_VIEW : 

  TRANSFORM_TYPE_EXPONENT : 

  TRANSFORM_TYPE_EXPONENT_WITH_LINEAR : 

  TRANSFORM_TYPE_EXPOSURE_CONTRAST : 

  TRANSFORM_TYPE_FILE : 

  TRANSFORM_TYPE_FIXED_FUNCTION : 

  TRANSFORM_TYPE_GRADING_PRIMARY : 

  TRANSFORM_TYPE_GRADING_RGB_CURVE : 

  TRANSFORM_TYPE_GRADING_TONE : 

  TRANSFORM_TYPE_GROUP : 

  TRANSFORM_TYPE_LOG_AFFINE : 

  TRANSFORM_TYPE_LOG_CAMERA : 

  TRANSFORM_TYPE_LOG : 

  TRANSFORM_TYPE_LOOK : 

  TRANSFORM_TYPE_LUT1D : 

  TRANSFORM_TYPE_LUT3D : 

  TRANSFORM_TYPE_MATRIX : 

  TRANSFORM_TYPE_RANGE : '''
    ...
    def TRANSFORM_TYPE_RANGE (self, *args, **kwargs):
      '''

Members:

  TRANSFORM_TYPE_ALLOCATION : 

  TRANSFORM_TYPE_BUILTIN : 

  TRANSFORM_TYPE_CDL : 

  TRANSFORM_TYPE_COLORSPACE : 

  TRANSFORM_TYPE_DISPLAY_VIEW : 

  TRANSFORM_TYPE_EXPONENT : 

  TRANSFORM_TYPE_EXPONENT_WITH_LINEAR : 

  TRANSFORM_TYPE_EXPOSURE_CONTRAST : 

  TRANSFORM_TYPE_FILE : 

  TRANSFORM_TYPE_FIXED_FUNCTION : 

  TRANSFORM_TYPE_GRADING_PRIMARY : 

  TRANSFORM_TYPE_GRADING_RGB_CURVE : 

  TRANSFORM_TYPE_GRADING_TONE : 

  TRANSFORM_TYPE_GROUP : 

  TRANSFORM_TYPE_LOG_AFFINE : 

  TRANSFORM_TYPE_LOG_CAMERA : 

  TRANSFORM_TYPE_LOG : 

  TRANSFORM_TYPE_LOOK : 

  TRANSFORM_TYPE_LUT1D : 

  TRANSFORM_TYPE_LUT3D : 

  TRANSFORM_TYPE_MATRIX : 

  TRANSFORM_TYPE_RANGE : '''
    ...
    def name (self, *args, **kwargs):
      '''name(self: handle) -> str
'''
    ...
    def value (self, *args, **kwargs):
      ''''''
    ...

def UNIFORM_BOOL (*args):
      '''

'''      
    ...

def UNIFORM_DOUBLE (*args):
      '''

'''      
    ...

def UNIFORM_FLOAT3 (*args):
      '''

'''      
    ...

def UNIFORM_UNKNOWN (*args):
      '''

'''      
    ...

def UNIFORM_VECTOR_FLOAT (*args):
      '''

'''      
    ...

def UNIFORM_VECTOR_INT (*args):
      '''

'''      
    ...

def UniformDataType (*args):
      '''

'''      
    ...

class UniformDataType:
    def UNIFORM_BOOL (self, *args, **kwargs):
      '''

Members:

  UNIFORM_DOUBLE : 

  UNIFORM_BOOL : 

  UNIFORM_FLOAT3 : 

  UNIFORM_VECTOR_FLOAT : 

  UNIFORM_VECTOR_INT : 

  UNIFORM_UNKNOWN : '''
    ...
    def UNIFORM_DOUBLE (self, *args, **kwargs):
      '''

Members:

  UNIFORM_DOUBLE : 

  UNIFORM_BOOL : 

  UNIFORM_FLOAT3 : 

  UNIFORM_VECTOR_FLOAT : 

  UNIFORM_VECTOR_INT : 

  UNIFORM_UNKNOWN : '''
    ...
    def UNIFORM_FLOAT3 (self, *args, **kwargs):
      '''

Members:

  UNIFORM_DOUBLE : 

  UNIFORM_BOOL : 

  UNIFORM_FLOAT3 : 

  UNIFORM_VECTOR_FLOAT : 

  UNIFORM_VECTOR_INT : 

  UNIFORM_UNKNOWN : '''
    ...
    def UNIFORM_UNKNOWN (self, *args, **kwargs):
      '''

Members:

  UNIFORM_DOUBLE : 

  UNIFORM_BOOL : 

  UNIFORM_FLOAT3 : 

  UNIFORM_VECTOR_FLOAT : 

  UNIFORM_VECTOR_INT : 

  UNIFORM_UNKNOWN : '''
    ...
    def UNIFORM_VECTOR_FLOAT (self, *args, **kwargs):
      '''

Members:

  UNIFORM_DOUBLE : 

  UNIFORM_BOOL : 

  UNIFORM_FLOAT3 : 

  UNIFORM_VECTOR_FLOAT : 

  UNIFORM_VECTOR_INT : 

  UNIFORM_UNKNOWN : '''
    ...
    def UNIFORM_VECTOR_INT (self, *args, **kwargs):
      '''

Members:

  UNIFORM_DOUBLE : 

  UNIFORM_BOOL : 

  UNIFORM_FLOAT3 : 

  UNIFORM_VECTOR_FLOAT : 

  UNIFORM_VECTOR_INT : 

  UNIFORM_UNKNOWN : '''
    ...
    def name (self, *args, **kwargs):
      '''name(self: handle) -> str
'''
    ...
    def value (self, *args, **kwargs):
      ''''''
    ...

def UnsetEnvVariable (*args):
      '''

'''      
    ...

def VIEWTRANSFORM_DIR_FROM_REFERENCE (*args):
      '''

'''      
    ...

def VIEWTRANSFORM_DIR_TO_REFERENCE (*args):
      '''

'''      
    ...

def VIEW_DISPLAY_DEFINED (*args):
      '''

'''      
    ...

def VIEW_SHARED (*args):
      '''

'''      
    ...

def ViewTransform (*args):
      '''

'''      
    ...

class ViewTransform:
    def ViewTransformCategoryIterator (self, *args, **kwargs):
      '''None'''
    ...
    def addCategory (self, *args, **kwargs):
      '''addCategory(self: PyOpenColorIO.ViewTransform, category: str) -> None
'''
    ...
    def clearCategories (self, *args, **kwargs):
      '''clearCategories(self: PyOpenColorIO.ViewTransform) -> None
'''
    ...
    def getCategories (self, *args, **kwargs):
      '''getCategories(self: PyOpenColorIO.ViewTransform) -> PyOpenColorIO.ViewTransform.ViewTransformCategoryIterator
'''
    ...
    def getDescription (self, *args, **kwargs):
      '''getDescription(self: PyOpenColorIO.ViewTransform) -> str
'''
    ...
    def getFamily (self, *args, **kwargs):
      '''getFamily(self: PyOpenColorIO.ViewTransform) -> str
'''
    ...
    def getName (self, *args, **kwargs):
      '''getName(self: PyOpenColorIO.ViewTransform) -> str
'''
    ...
    def getReferenceSpaceType (self, *args, **kwargs):
      '''getReferenceSpaceType(self: PyOpenColorIO.ViewTransform) -> PyOpenColorIO.ReferenceSpaceType
'''
    ...
    def getTransform (self, *args, **kwargs):
      '''getTransform(self: PyOpenColorIO.ViewTransform, direction: PyOpenColorIO.ViewTransformDirection) -> PyOpenColorIO.Transform
'''
    ...
    def hasCategory (self, *args, **kwargs):
      '''hasCategory(self: PyOpenColorIO.ViewTransform, category: str) -> bool
'''
    ...
    def removeCategory (self, *args, **kwargs):
      '''removeCategory(self: PyOpenColorIO.ViewTransform, category: str) -> None
'''
    ...
    def setDescription (self, *args, **kwargs):
      '''setDescription(self: PyOpenColorIO.ViewTransform, description: str) -> None
'''
    ...
    def setFamily (self, *args, **kwargs):
      '''setFamily(self: PyOpenColorIO.ViewTransform, family: str) -> None
'''
    ...
    def setName (self, *args, **kwargs):
      '''setName(self: PyOpenColorIO.ViewTransform, name: str) -> None
'''
    ...
    def setTransform (self, *args, **kwargs):
      '''setTransform(self: PyOpenColorIO.ViewTransform, transform: PyOpenColorIO.Transform, direction: PyOpenColorIO.ViewTransformDirection) -> None
'''
    ...

def ViewTransformDirection (*args):
      '''

'''      
    ...

class ViewTransformDirection:
    def VIEWTRANSFORM_DIR_FROM_REFERENCE (self, *args, **kwargs):
      '''

Members:

  VIEWTRANSFORM_DIR_TO_REFERENCE : 

  VIEWTRANSFORM_DIR_FROM_REFERENCE : '''
    ...
    def VIEWTRANSFORM_DIR_TO_REFERENCE (self, *args, **kwargs):
      '''

Members:

  VIEWTRANSFORM_DIR_TO_REFERENCE : 

  VIEWTRANSFORM_DIR_FROM_REFERENCE : '''
    ...
    def name (self, *args, **kwargs):
      '''name(self: handle) -> str
'''
    ...
    def value (self, *args, **kwargs):
      ''''''
    ...

def ViewType (*args):
      '''

'''      
    ...

class ViewType:
    def VIEW_DISPLAY_DEFINED (self, *args, **kwargs):
      '''

Members:

  VIEW_SHARED : 

  VIEW_DISPLAY_DEFINED : '''
    ...
    def VIEW_SHARED (self, *args, **kwargs):
      '''

Members:

  VIEW_SHARED : 

  VIEW_DISPLAY_DEFINED : '''
    ...
    def name (self, *args, **kwargs):
      '''name(self: handle) -> str
'''
    ...
    def value (self, *args, **kwargs):
      ''''''
    ...

def ViewingRules (*args):
      '''

'''      
    ...

class ViewingRules:
    def ViewingRuleColorSpaceIterator (self, *args, **kwargs):
      '''None'''
    ...
    def ViewingRuleEncodingIterator (self, *args, **kwargs):
      '''None'''
    ...
    def addColorSpace (self, *args, **kwargs):
      '''addColorSpace(self: PyOpenColorIO.ViewingRules, ruleIndex: int, colorSpaceName: str) -> None
'''
    ...
    def addEncoding (self, *args, **kwargs):
      '''addEncoding(self: PyOpenColorIO.ViewingRules, ruleIndex: int, encodingName: str) -> None
'''
    ...
    def getColorSpaces (self, *args, **kwargs):
      '''getColorSpaces(self: PyOpenColorIO.ViewingRules, ruleIndex: int) -> PyOpenColorIO.ViewingRules.ViewingRuleColorSpaceIterator
'''
    ...
    def getCustomKeyName (self, *args, **kwargs):
      '''getCustomKeyName(self: PyOpenColorIO.ViewingRules, ruleIndex: int, key: int) -> str
'''
    ...
    def getCustomKeyValue (self, *args, **kwargs):
      '''getCustomKeyValue(self: PyOpenColorIO.ViewingRules, ruleIndex: int, key: int) -> str
'''
    ...
    def getEncodings (self, *args, **kwargs):
      '''getEncodings(self: PyOpenColorIO.ViewingRules, ruleIndex: int) -> PyOpenColorIO.ViewingRules.ViewingRuleEncodingIterator
'''
    ...
    def getIndexForRule (self, *args, **kwargs):
      '''getIndexForRule(self: PyOpenColorIO.ViewingRules, ruleName: str) -> int
'''
    ...
    def getName (self, *args, **kwargs):
      '''getName(self: PyOpenColorIO.ViewingRules, ruleIndex: int) -> str
'''
    ...
    def getNumCustomKeys (self, *args, **kwargs):
      '''getNumCustomKeys(self: PyOpenColorIO.ViewingRules, ruleIndex: int) -> int
'''
    ...
    def getNumEntries (self, *args, **kwargs):
      '''getNumEntries(self: PyOpenColorIO.ViewingRules) -> int
'''
    ...
    def insertRule (self, *args, **kwargs):
      '''insertRule(self: PyOpenColorIO.ViewingRules, ruleIndex: int, name: str) -> None
'''
    ...
    def removeColorSpace (self, *args, **kwargs):
      '''removeColorSpace(self: PyOpenColorIO.ViewingRules, ruleIndex: int, colorSpaceIndex: int) -> None
'''
    ...
    def removeEncoding (self, *args, **kwargs):
      '''removeEncoding(self: PyOpenColorIO.ViewingRules, ruleIndex: int, encodingIndex: int) -> None
'''
    ...
    def removeRule (self, *args, **kwargs):
      '''removeRule(self: PyOpenColorIO.ViewingRules, ruleIndex: int) -> None
'''
    ...
    def setCustomKey (self, *args, **kwargs):
      '''setCustomKey(self: PyOpenColorIO.ViewingRules, ruleIndex: int, key: str, value: str) -> None
'''
    ...

def __author__ (*args):
      '''

'''      
    ...

def __copyright__ (*args):
      '''

'''      
    ...

def __doc__ (*args):
      '''

'''      
    ...

def __email__ (*args):
      '''

'''      
    ...

def __file__ (*args):
      '''

'''      
    ...

def __license__ (*args):
      '''

'''      
    ...

def __loader__ (*args):
      '''

'''      
    ...

def __name__ (*args):
      '''

'''      
    ...

def __package__ (*args):
      '''

'''      
    ...

def __spec__ (*args):
      '''

'''      
    ...

def __status__ (*args):
      '''

'''      
    ...

def __version__ (*args):
      '''

'''      
    ...

def vector_of_uint8_t (*args):
      '''

'''      
    ...

class vector_of_uint8_t:
    def append (self, *args, **kwargs):
      '''append(self: PyOpenColorIO.vector_of_uint8_t, x: int) -> None

Add an item to the end of the list
'''
    ...
    def clear (self, *args, **kwargs):
      '''clear(self: PyOpenColorIO.vector_of_uint8_t) -> None

Clear the contents
'''
    ...
    def count (self, *args, **kwargs):
      '''count(self: PyOpenColorIO.vector_of_uint8_t, x: int) -> int

Return the number of times ``x`` appears in the list
'''
    ...
    def extend (self, *args, **kwargs):
      '''extend(*args, **kwargs)
Overloaded function.

1. extend(self: PyOpenColorIO.vector_of_uint8_t, L: PyOpenColorIO.vector_of_uint8_t) -> None

Extend the list by appending all the items in the given list

2. extend(self: PyOpenColorIO.vector_of_uint8_t, L: Iterable) -> None

Extend the list by appending all the items in the given list
'''
    ...
    def insert (self, *args, **kwargs):
      '''insert(self: PyOpenColorIO.vector_of_uint8_t, i: int, x: int) -> None

Insert an item at a given position.
'''
    ...
    def pop (self, *args, **kwargs):
      '''pop(*args, **kwargs)
Overloaded function.

1. pop(self: PyOpenColorIO.vector_of_uint8_t) -> int

Remove and return the last item

2. pop(self: PyOpenColorIO.vector_of_uint8_t, i: int) -> int

Remove and return the item at index ``i``
'''
    ...
    def remove (self, *args, **kwargs):
      '''remove(self: PyOpenColorIO.vector_of_uint8_t, x: int) -> None

Remove the first item from the list whose value is x. It is an error if there is no such item.
'''
    ...
