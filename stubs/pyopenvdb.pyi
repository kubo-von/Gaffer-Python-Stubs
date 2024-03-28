
def Axis (*args):
      '''

'''      
    ...

class Axis:
    def X (self, *args, **kwargs):
      '''Members:

  X

  Y

  Z'''
    ...
    def Y (self, *args, **kwargs):
      '''Members:

  X

  Y

  Z'''
    ...
    def Z (self, *args, **kwargs):
      '''Members:

  X

  Y

  Z'''
    ...
    def name (self, *args, **kwargs):
      '''None'''
    ...
    def value (self, *args, **kwargs):
      ''''''
    ...

def BoolGrid (*args):
      '''

'''      
    ...

class BoolGrid:
    def activeLeafVoxelCount (self, *args, **kwargs):
      '''activeLeafVoxelCount() -> int

Return the number of active voxels that are stored
in the leaf nodes of this grid's tree.'''
    ...
    def activeVoxelCount (self, *args, **kwargs):
      '''activeVoxelCount() -> int

Return the number of active voxels in this grid.'''
    ...
    def addStatsMetadata (self, *args, **kwargs):
      '''addStatsMetadata()

Add metadata to this grid comprising the current values
of statistics like the active voxel count and bounding box.
(This metadata is not automatically kept up-to-date with
changes to this grid.)'''
    ...
    def background (self, *args, **kwargs):
      '''value of this grid's background voxels'''
    ...
    def citerAllValues (self, *args, **kwargs):
      '''iterAllValues() -> iterator

Return a read-only iterator over all of this grid's
tile and voxel values.'''
    ...
    def citerOffValues (self, *args, **kwargs):
      '''iterOffValues() -> iterator

Return a read-only iterator over this grid's inactive
tile and voxel values.'''
    ...
    def citerOnValues (self, *args, **kwargs):
      '''citerOnValues() -> iterator

Return a read-only iterator over this grid's active
tile and voxel values.'''
    ...
    def clear (self, *args, **kwargs):
      '''clear()

Remove all tiles from this grid and all nodes other than the root node.'''
    ...
    def combine (self, *args, **kwargs):
      '''combine(grid, function)

Compute function(self, other) over all corresponding pairs
of values (tile or voxel) of this grid and the other grid
and store the result in this grid.

Note: this operation always empties the other grid.

Example: grid.combine(otherGrid, lambda a, b: min(a, b))'''
    ...
    def convertToPolygons (self, *args, **kwargs):
      '''convertToPolygons(isovalue=0, adaptivity=0) -> points, triangles, quads

Adaptively mesh a scalar grid that has a continuous isosurface
at the given isovalue.  Return a NumPy array of world-space
points and NumPy arrays of 3- and 4-tuples of point indices,
which specify the vertices of the triangles and quadrilaterals
that form the mesh.  Adaptivity can vary from 0 to 1, where 0
produces a high-polygon-count mesh that closely approximates
the isosurface, and 1 produces a lower-polygon-count mesh
with some loss of surface detail.'''
    ...
    def convertToQuads (self, *args, **kwargs):
      '''convertToQuads(isovalue=0) -> points, quads

Uniformly mesh a scalar grid that has a continuous isosurface
at the given isovalue.  Return a NumPy array of world-space
points and a NumPy array of 4-tuples of point indices, which
specify the vertices of the quadrilaterals that form the mesh.'''
    ...
    def copy (self, *args, **kwargs):
      '''copy() -> BoolGrid

Return a shallow copy of this grid, i.e., a grid
that shares its voxel data with this grid.'''
    ...
    def copyFromArray (self, *args, **kwargs):
      '''copyFromArray(array, ijk=(0, 0, 0), tolerance=0)

Populate this grid, starting at voxel (i, j, k), with values
from a three-dimensional array.  Mark voxels as inactive
if and only if their values are equal to this grid's
background value within the given tolerance.'''
    ...
    def copyToArray (self, *args, **kwargs):
      '''copyToArray(array, ijk=(0, 0, 0))

Populate a three-dimensional array with values
from this grid, starting at voxel (i, j, k).'''
    ...
    def createLevelSetFromPolygons (self, *args, **kwargs):
      '''createLevelSetFromPolygons(points, triangles=None, quads=None,
    transform=None, halfWidth=3.000000) -> BoolGrid

Convert a triangle and/or quad mesh to a narrow-band level set volume.
The mesh must form a closed surface, but the surface need not be
manifold and may have self intersections and degenerate faces.
The mesh is described by a NumPy array of world-space points
and NumPy arrays of 3- and 4-tuples of point indices that specify
the vertices of the triangles and quadrilaterals that form the mesh.
Either the triangle or the quad array may be empty or None.
The resulting volume will have the given transform (or the identity
transform if no transform is given) and a narrow band width of
2 x halfWidth voxels.'''
    ...
    def creator (self, *args, **kwargs):
      '''user-specified description of this grid's creator'''
    ...
    def deepCopy (self, *args, **kwargs):
      '''deepCopy() -> BoolGrid

Return a deep copy of this grid.
'''
    ...
    def empty (self, *args, **kwargs):
      '''empty() -> bool

Return True if this grid contains only background voxels.'''
    ...
    def evalActiveVoxelBoundingBox (self, *args, **kwargs):
      '''evalActiveVoxelBoundingBox() -> xyzMin, xyzMax

Return the coordinates of opposite corners of the axis-aligned
bounding box of all active voxels.'''
    ...
    def evalActiveVoxelDim (self, *args, **kwargs):
      '''evalActiveVoxelDim() -> x, y, z

Return the dimensions of the axis-aligned bounding box of all
active voxels.'''
    ...
    def evalLeafBoundingBox (self, *args, **kwargs):
      '''evalLeafBoundingBox() -> xyzMin, xyzMax

Return the coordinates of opposite corners of the axis-aligned
bounding box of all leaf nodes.'''
    ...
    def evalLeafDim (self, *args, **kwargs):
      '''evalLeafDim() -> x, y, z

Return the dimensions of the axis-aligned bounding box
of all leaf nodes.'''
    ...
    def evalMinMax (self, *args, **kwargs):
      '''evalMinMax() -> min, max

Return the minimum and maximum active values in this grid.'''
    ...
    def fill (self, *args, **kwargs):
      '''fill(min, max, value, active=True)

Set all voxels within a given axis-aligned box to
a constant value (either active or inactive).'''
    ...
    def getAccessor (self, *args, **kwargs):
      '''getAccessor() -> BoolGridAccessor

Return an accessor that provides random read and write access
to this grid's voxels.'''
    ...
    def getConstAccessor (self, *args, **kwargs):
      '''getConstAccessor() -> BoolGridAccessor

Return an accessor that provides random read-only access
to this grid's voxels.'''
    ...
    def getIndexRange (self, *args, **kwargs):
      '''getIndexRange() -> min, max

Return the minimum and maximum coordinates that are represented
in this grid.  These might include background voxels.'''
    ...
    def getStatsMetadata (self, *args, **kwargs):
      '''getStatsMetadata() -> dict

Return a (possibly empty) dict containing just the metadata
that was added to this grid with addStatsMetadata().'''
    ...
    def gridClass (self, *args, **kwargs):
      '''the class of volumetric data (level set, fog volume, etc.)
stored in this grid'''
    ...
    def info (self, *args, **kwargs):
      '''info(verbosity=1) -> str

Return a string containing information about this grid
with a specified level of verbosity.
'''
    ...
    def iterAllValues (self, *args, **kwargs):
      '''iterAllValues() -> iterator

Return a read/write iterator over all of this grid's
tile and voxel values.'''
    ...
    def iterOffValues (self, *args, **kwargs):
      '''iterOffValues() -> iterator

Return a read/write iterator over this grid's inactive
tile and voxel values.'''
    ...
    def iterOnValues (self, *args, **kwargs):
      '''iterOnValues() -> iterator

Return a read/write iterator over this grid's active
tile and voxel values.'''
    ...
    def iterkeys (self, *args, **kwargs):
      '''iterkeys() -> iterator

Return an iterator over this grid's metadata keys.'''
    ...
    def leafCount (self, *args, **kwargs):
      '''leafCount() -> int

Return the number of leaf nodes in this grid's tree.'''
    ...
    def mapAll (self, *args, **kwargs):
      '''mapAll(function)

Iterate over all values (tile and voxel) of this grid
and replace each value with function(value).

Example: grid.mapAll(lambda x: x * 2 if x < 0.5 else x)'''
    ...
    def mapOff (self, *args, **kwargs):
      '''mapOff(function)

Iterate over all the inactive ("off") values (tile and voxel)
of this grid and replace each value with function(value).

Example: grid.mapOff(lambda x: x * 2 if x < 0.5 else x)'''
    ...
    def mapOn (self, *args, **kwargs):
      '''mapOn(function)

Iterate over all the active ("on") values (tile and voxel)
of this grid and replace each value with function(value).

Example: grid.mapOn(lambda x: x * 2 if x < 0.5 else x)'''
    ...
    def memUsage (self, *args, **kwargs):
      '''memUsage() -> int

Return the memory usage of this grid in bytes.'''
    ...
    def merge (self, *args, **kwargs):
      '''merge(BoolGrid)

Move child nodes from the other grid into this grid wherever
those nodes correspond to constant-value tiles in this grid,
and replace leaf-level inactive voxels in this grid with
corresponding voxels in the other grid that are active.

Note: this operation always empties the other grid.'''
    ...
    def metadata (self, *args, **kwargs):
      '''dict of this grid's metadata

Setting this attribute replaces all of this grid's metadata,
but mutating it in place has no effect on the grid, since
the value of this attribute is a only a copy of the metadata.
Use either indexing or updateMetadata() to mutate metadata in place.'''
    ...
    def name (self, *args, **kwargs):
      '''this grid's user-specified name'''
    ...
    def nodeLog2Dims (self, *args, **kwargs):
      '''list of Log2Dims of the nodes of this grid's tree
in order from root to leaf'''
    ...
    def nonLeafCount (self, *args, **kwargs):
      '''nonLeafCount() -> int

Return the number of non-leaf nodes in this grid's tree.'''
    ...
    def oneValue (self, *args, **kwargs):
      '''bool(x) -> bool

Returns True when the argument x is true, False otherwise.
The builtins True and False are the only two instances of the class bool.
The class bool is a subclass of the class int, and cannot be subclassed.'''
    ...
    def prune (self, *args, **kwargs):
      '''prune(tolerance=0)

Remove nodes whose values all have the same active state
and are equal to within a given tolerance.'''
    ...
    def pruneInactive (self, *args, **kwargs):
      '''pruneInactive()

Remove nodes whose values are all inactive and replace them
with background tiles.'''
    ...
    def saveFloatAsHalf (self, *args, **kwargs):
      '''if True, write floating-point voxel values as 16-bit half floats'''
    ...
    def sharesWith (self, *args, **kwargs):
      '''sharesWith(BoolGrid) -> bool

Return True if this grid shares its voxel data with the given grid.'''
    ...
    def signedFloodFill (self, *args, **kwargs):
      '''signedFloodFill()

Propagate the sign from a narrow-band level set into inactive
voxels and tiles.'''
    ...
    def transform (self, *args, **kwargs):
      '''transform associated with this grid'''
    ...
    def treeDepth (self, *args, **kwargs):
      '''depth of this grid's tree from root node to leaf node'''
    ...
    def updateMetadata (self, *args, **kwargs):
      '''updateMetadata(dict)

Add metadata to this grid, replacing any existing items
having the same names as the new items.'''
    ...
    def valueTypeName (self, *args, **kwargs):
      '''str(object='') -> str
str(bytes_or_buffer[, encoding[, errors]]) -> str

Create a new string object from the given object. If encoding or
errors is specified, then the object must expose a data buffer
that will be decoded using the given encoding and error handler.
Otherwise, returns the result of object.__str__() (if defined)
or repr(object).
encoding defaults to sys.getdefaultencoding().
errors defaults to 'strict'.'''
    ...
    def vectorType (self, *args, **kwargs):
      '''how transforms are applied to values stored in this grid'''
    ...
    def zeroValue (self, *args, **kwargs):
      '''bool(x) -> bool

Returns True when the argument x is true, False otherwise.
The builtins True and False are the only two instances of the class bool.
The class bool is a subclass of the class int, and cannot be subclassed.'''
    ...

def BoolGridAccessor (*args):
      '''

'''      
    ...

class BoolGridAccessor:
    def clear (self, *args, **kwargs):
      '''clear()

Clear this accessor of all cached data.'''
    ...
    def copy (self, *args, **kwargs):
      '''copy() -> Accessor

Return a copy of this accessor.'''
    ...
    def getValue (self, *args, **kwargs):
      '''getValue(ijk) -> bool

Return the value of the voxel at coordinates (i, j, k).'''
    ...
    def getValueDepth (self, *args, **kwargs):
      '''getValueDepth(ijk) -> int

Return the tree depth (0 = root) at which the value of voxel
(i, j, k) resides.  If (i, j, k) isn't explicitly represented in
the tree (i.e., it is implicitly a background voxel), return -1.'''
    ...
    def isCached (self, *args, **kwargs):
      '''isCached(ijk) -> bool

Return True if this accessor has cached the path to voxel (i, j, k).'''
    ...
    def isValueOn (self, *args, **kwargs):
      '''isValueOn(ijk) -> bool

Return the active state of the voxel at coordinates (i, j, k).'''
    ...
    def isVoxel (self, *args, **kwargs):
      '''isVoxel(ijk) -> bool

Return True if voxel (i, j, k) resides at the leaf level of the tree.'''
    ...
    def parent (self, *args, **kwargs):
      '''this accessor's parent BoolGrid'''
    ...
    def probeValue (self, *args, **kwargs):
      '''probeValue(ijk) -> value, bool

Return the value of the voxel at coordinates (i, j, k)
together with the voxel's active state.'''
    ...
    def setActiveState (self, *args, **kwargs):
      '''setActiveState(ijk, on)

Mark voxel (i, j, k) as either active or inactive (True or False),
but don't change its value.'''
    ...
    def setValueOff (self, *args, **kwargs):
      '''setValueOff(ijk, value)

Mark voxel (i, j, k) as inactive and set the voxel's value if specified.'''
    ...
    def setValueOn (self, *args, **kwargs):
      '''setValueOn(ijk, value)

Mark voxel (i, j, k) as active and set the voxel's value if specified.
'''
    ...
    def setValueOnly (self, *args, **kwargs):
      '''setValueOnly(ijk, value)

Set the value of voxel (i, j, k), but don't change its active state.'''
    ...

def BoolGridConstAccessor (*args):
      '''

'''      
    ...

class BoolGridConstAccessor:
    def clear (self, *args, **kwargs):
      '''clear()

Clear this accessor of all cached data.'''
    ...
    def copy (self, *args, **kwargs):
      '''copy() -> ConstAccessor

Return a copy of this accessor.'''
    ...
    def getValue (self, *args, **kwargs):
      '''getValue(ijk) -> bool

Return the value of the voxel at coordinates (i, j, k).'''
    ...
    def getValueDepth (self, *args, **kwargs):
      '''getValueDepth(ijk) -> int

Return the tree depth (0 = root) at which the value of voxel
(i, j, k) resides.  If (i, j, k) isn't explicitly represented in
the tree (i.e., it is implicitly a background voxel), return -1.'''
    ...
    def isCached (self, *args, **kwargs):
      '''isCached(ijk) -> bool

Return True if this accessor has cached the path to voxel (i, j, k).'''
    ...
    def isValueOn (self, *args, **kwargs):
      '''isValueOn(ijk) -> bool

Return the active state of the voxel at coordinates (i, j, k).'''
    ...
    def isVoxel (self, *args, **kwargs):
      '''isVoxel(ijk) -> bool

Return True if voxel (i, j, k) resides at the leaf level of the tree.'''
    ...
    def parent (self, *args, **kwargs):
      '''this accessor's parent BoolGrid'''
    ...
    def probeValue (self, *args, **kwargs):
      '''probeValue(ijk) -> value, bool

Return the value of the voxel at coordinates (i, j, k)
together with the voxel's active state.'''
    ...
    def setActiveState (self, *args, **kwargs):
      '''setActiveState(ijk, on)

Mark voxel (i, j, k) as either active or inactive (True or False),
but don't change its value.'''
    ...
    def setValueOff (self, *args, **kwargs):
      '''setValueOff(ijk, value)

Mark voxel (i, j, k) as inactive and set the voxel's value if specified.'''
    ...
    def setValueOn (self, *args, **kwargs):
      '''setValueOn(ijk, value)

Mark voxel (i, j, k) as active and set the voxel's value if specified.
'''
    ...
    def setValueOnly (self, *args, **kwargs):
      '''setValueOnly(ijk, value)

Set the value of voxel (i, j, k), but don't change its active state.'''
    ...

def BoolGridValueAllCIter (*args):
      '''

'''      
    ...

class BoolGridValueAllCIter:
    def next (self, *args, **kwargs):
      '''next() -> BoolGridValueAllCIterValue'''
    ...
    def parent (self, *args, **kwargs):
      '''the BoolGrid over which to iterate'''
    ...

def BoolGridValueAllCIterValue (*args):
      '''

'''      
    ...

class BoolGridValueAllCIterValue:
    def active (self, *args, **kwargs):
      '''active state of this tile or voxel'''
    ...
    def copy (self, *args, **kwargs):
      '''copy() -> BoolGridValueAllCIterValue

Return a shallow copy of this value, i.e., one that shares
its data with the original.'''
    ...
    def count (self, *args, **kwargs):
      '''number of voxels spanned by this value'''
    ...
    def depth (self, *args, **kwargs):
      '''tree depth at which this value is stored'''
    ...
    def keys (self, *args, **kwargs):
      '''keys() -> list

Return a list of keys for this tile or voxel.'''
    ...
    def max (self, *args, **kwargs):
      '''upper bound of the axis-aligned bounding box of this tile or voxel'''
    ...
    def min (self, *args, **kwargs):
      '''lower bound of the axis-aligned bounding box of this tile or voxel'''
    ...
    def parent (self, *args, **kwargs):
      '''the BoolGrid to which this value belongs'''
    ...
    def value (self, *args, **kwargs):
      '''value of this tile or voxel'''
    ...

def BoolGridValueAllIter (*args):
      '''

'''      
    ...

class BoolGridValueAllIter:
    def next (self, *args, **kwargs):
      '''next() -> BoolGridValueAllIterValue'''
    ...
    def parent (self, *args, **kwargs):
      '''the BoolGrid over which to iterate'''
    ...

def BoolGridValueAllIterValue (*args):
      '''

'''      
    ...

class BoolGridValueAllIterValue:
    def active (self, *args, **kwargs):
      '''active state of this tile or voxel'''
    ...
    def copy (self, *args, **kwargs):
      '''copy() -> BoolGridValueAllIterValue

Return a shallow copy of this value, i.e., one that shares
its data with the original.'''
    ...
    def count (self, *args, **kwargs):
      '''number of voxels spanned by this value'''
    ...
    def depth (self, *args, **kwargs):
      '''tree depth at which this value is stored'''
    ...
    def keys (self, *args, **kwargs):
      '''keys() -> list

Return a list of keys for this tile or voxel.'''
    ...
    def max (self, *args, **kwargs):
      '''upper bound of the axis-aligned bounding box of this tile or voxel'''
    ...
    def min (self, *args, **kwargs):
      '''lower bound of the axis-aligned bounding box of this tile or voxel'''
    ...
    def parent (self, *args, **kwargs):
      '''the BoolGrid to which this value belongs'''
    ...
    def value (self, *args, **kwargs):
      '''value of this tile or voxel'''
    ...

def BoolGridValueOffCIter (*args):
      '''

'''      
    ...

class BoolGridValueOffCIter:
    def next (self, *args, **kwargs):
      '''next() -> BoolGridValueOffCIterValue'''
    ...
    def parent (self, *args, **kwargs):
      '''the BoolGrid over which to iterate'''
    ...

def BoolGridValueOffCIterValue (*args):
      '''

'''      
    ...

class BoolGridValueOffCIterValue:
    def active (self, *args, **kwargs):
      '''active state of this tile or voxel'''
    ...
    def copy (self, *args, **kwargs):
      '''copy() -> BoolGridValueOffCIterValue

Return a shallow copy of this value, i.e., one that shares
its data with the original.'''
    ...
    def count (self, *args, **kwargs):
      '''number of voxels spanned by this value'''
    ...
    def depth (self, *args, **kwargs):
      '''tree depth at which this value is stored'''
    ...
    def keys (self, *args, **kwargs):
      '''keys() -> list

Return a list of keys for this tile or voxel.'''
    ...
    def max (self, *args, **kwargs):
      '''upper bound of the axis-aligned bounding box of this tile or voxel'''
    ...
    def min (self, *args, **kwargs):
      '''lower bound of the axis-aligned bounding box of this tile or voxel'''
    ...
    def parent (self, *args, **kwargs):
      '''the BoolGrid to which this value belongs'''
    ...
    def value (self, *args, **kwargs):
      '''value of this tile or voxel'''
    ...

def BoolGridValueOffIter (*args):
      '''

'''      
    ...

class BoolGridValueOffIter:
    def next (self, *args, **kwargs):
      '''next() -> BoolGridValueOffIterValue'''
    ...
    def parent (self, *args, **kwargs):
      '''the BoolGrid over which to iterate'''
    ...

def BoolGridValueOffIterValue (*args):
      '''

'''      
    ...

class BoolGridValueOffIterValue:
    def active (self, *args, **kwargs):
      '''active state of this tile or voxel'''
    ...
    def copy (self, *args, **kwargs):
      '''copy() -> BoolGridValueOffIterValue

Return a shallow copy of this value, i.e., one that shares
its data with the original.'''
    ...
    def count (self, *args, **kwargs):
      '''number of voxels spanned by this value'''
    ...
    def depth (self, *args, **kwargs):
      '''tree depth at which this value is stored'''
    ...
    def keys (self, *args, **kwargs):
      '''keys() -> list

Return a list of keys for this tile or voxel.'''
    ...
    def max (self, *args, **kwargs):
      '''upper bound of the axis-aligned bounding box of this tile or voxel'''
    ...
    def min (self, *args, **kwargs):
      '''lower bound of the axis-aligned bounding box of this tile or voxel'''
    ...
    def parent (self, *args, **kwargs):
      '''the BoolGrid to which this value belongs'''
    ...
    def value (self, *args, **kwargs):
      '''value of this tile or voxel'''
    ...

def BoolGridValueOnCIter (*args):
      '''

'''      
    ...

class BoolGridValueOnCIter:
    def next (self, *args, **kwargs):
      '''next() -> BoolGridValueOnCIterValue'''
    ...
    def parent (self, *args, **kwargs):
      '''the BoolGrid over which to iterate'''
    ...

def BoolGridValueOnCIterValue (*args):
      '''

'''      
    ...

class BoolGridValueOnCIterValue:
    def active (self, *args, **kwargs):
      '''active state of this tile or voxel'''
    ...
    def copy (self, *args, **kwargs):
      '''copy() -> BoolGridValueOnCIterValue

Return a shallow copy of this value, i.e., one that shares
its data with the original.'''
    ...
    def count (self, *args, **kwargs):
      '''number of voxels spanned by this value'''
    ...
    def depth (self, *args, **kwargs):
      '''tree depth at which this value is stored'''
    ...
    def keys (self, *args, **kwargs):
      '''keys() -> list

Return a list of keys for this tile or voxel.'''
    ...
    def max (self, *args, **kwargs):
      '''upper bound of the axis-aligned bounding box of this tile or voxel'''
    ...
    def min (self, *args, **kwargs):
      '''lower bound of the axis-aligned bounding box of this tile or voxel'''
    ...
    def parent (self, *args, **kwargs):
      '''the BoolGrid to which this value belongs'''
    ...
    def value (self, *args, **kwargs):
      '''value of this tile or voxel'''
    ...

def BoolGridValueOnIter (*args):
      '''

'''      
    ...

class BoolGridValueOnIter:
    def next (self, *args, **kwargs):
      '''next() -> BoolGridValueOnIterValue'''
    ...
    def parent (self, *args, **kwargs):
      '''the BoolGrid over which to iterate'''
    ...

def BoolGridValueOnIterValue (*args):
      '''

'''      
    ...

class BoolGridValueOnIterValue:
    def active (self, *args, **kwargs):
      '''active state of this tile or voxel'''
    ...
    def copy (self, *args, **kwargs):
      '''copy() -> BoolGridValueOnIterValue

Return a shallow copy of this value, i.e., one that shares
its data with the original.'''
    ...
    def count (self, *args, **kwargs):
      '''number of voxels spanned by this value'''
    ...
    def depth (self, *args, **kwargs):
      '''tree depth at which this value is stored'''
    ...
    def keys (self, *args, **kwargs):
      '''keys() -> list

Return a list of keys for this tile or voxel.'''
    ...
    def max (self, *args, **kwargs):
      '''upper bound of the axis-aligned bounding box of this tile or voxel'''
    ...
    def min (self, *args, **kwargs):
      '''lower bound of the axis-aligned bounding box of this tile or voxel'''
    ...
    def parent (self, *args, **kwargs):
      '''the BoolGrid to which this value belongs'''
    ...
    def value (self, *args, **kwargs):
      '''value of this tile or voxel'''
    ...

def COORD_MAX (*args):
      '''

'''      
    ...

def COORD_MIN (*args):
      '''

'''      
    ...

def Coord (*args):
      '''

'''      
    ...

class Coord:

def FILE_FORMAT_VERSION (*args):
      '''

'''      
    ...

def FloatGrid (*args):
      '''

'''      
    ...

class FloatGrid:
    def activeLeafVoxelCount (self, *args, **kwargs):
      '''activeLeafVoxelCount() -> int

Return the number of active voxels that are stored
in the leaf nodes of this grid's tree.'''
    ...
    def activeVoxelCount (self, *args, **kwargs):
      '''activeVoxelCount() -> int

Return the number of active voxels in this grid.'''
    ...
    def addStatsMetadata (self, *args, **kwargs):
      '''addStatsMetadata()

Add metadata to this grid comprising the current values
of statistics like the active voxel count and bounding box.
(This metadata is not automatically kept up-to-date with
changes to this grid.)'''
    ...
    def background (self, *args, **kwargs):
      '''value of this grid's background voxels'''
    ...
    def citerAllValues (self, *args, **kwargs):
      '''iterAllValues() -> iterator

Return a read-only iterator over all of this grid's
tile and voxel values.'''
    ...
    def citerOffValues (self, *args, **kwargs):
      '''iterOffValues() -> iterator

Return a read-only iterator over this grid's inactive
tile and voxel values.'''
    ...
    def citerOnValues (self, *args, **kwargs):
      '''citerOnValues() -> iterator

Return a read-only iterator over this grid's active
tile and voxel values.'''
    ...
    def clear (self, *args, **kwargs):
      '''clear()

Remove all tiles from this grid and all nodes other than the root node.'''
    ...
    def combine (self, *args, **kwargs):
      '''combine(grid, function)

Compute function(self, other) over all corresponding pairs
of values (tile or voxel) of this grid and the other grid
and store the result in this grid.

Note: this operation always empties the other grid.

Example: grid.combine(otherGrid, lambda a, b: min(a, b))'''
    ...
    def convertToPolygons (self, *args, **kwargs):
      '''convertToPolygons(isovalue=0, adaptivity=0) -> points, triangles, quads

Adaptively mesh a scalar grid that has a continuous isosurface
at the given isovalue.  Return a NumPy array of world-space
points and NumPy arrays of 3- and 4-tuples of point indices,
which specify the vertices of the triangles and quadrilaterals
that form the mesh.  Adaptivity can vary from 0 to 1, where 0
produces a high-polygon-count mesh that closely approximates
the isosurface, and 1 produces a lower-polygon-count mesh
with some loss of surface detail.'''
    ...
    def convertToQuads (self, *args, **kwargs):
      '''convertToQuads(isovalue=0) -> points, quads

Uniformly mesh a scalar grid that has a continuous isosurface
at the given isovalue.  Return a NumPy array of world-space
points and a NumPy array of 4-tuples of point indices, which
specify the vertices of the quadrilaterals that form the mesh.'''
    ...
    def copy (self, *args, **kwargs):
      '''copy() -> FloatGrid

Return a shallow copy of this grid, i.e., a grid
that shares its voxel data with this grid.'''
    ...
    def copyFromArray (self, *args, **kwargs):
      '''copyFromArray(array, ijk=(0, 0, 0), tolerance=0)

Populate this grid, starting at voxel (i, j, k), with values
from a three-dimensional array.  Mark voxels as inactive
if and only if their values are equal to this grid's
background value within the given tolerance.'''
    ...
    def copyToArray (self, *args, **kwargs):
      '''copyToArray(array, ijk=(0, 0, 0))

Populate a three-dimensional array with values
from this grid, starting at voxel (i, j, k).'''
    ...
    def createLevelSetFromPolygons (self, *args, **kwargs):
      '''createLevelSetFromPolygons(points, triangles=None, quads=None,
    transform=None, halfWidth=3.000000) -> FloatGrid

Convert a triangle and/or quad mesh to a narrow-band level set volume.
The mesh must form a closed surface, but the surface need not be
manifold and may have self intersections and degenerate faces.
The mesh is described by a NumPy array of world-space points
and NumPy arrays of 3- and 4-tuples of point indices that specify
the vertices of the triangles and quadrilaterals that form the mesh.
Either the triangle or the quad array may be empty or None.
The resulting volume will have the given transform (or the identity
transform if no transform is given) and a narrow band width of
2 x halfWidth voxels.'''
    ...
    def creator (self, *args, **kwargs):
      '''user-specified description of this grid's creator'''
    ...
    def deepCopy (self, *args, **kwargs):
      '''deepCopy() -> FloatGrid

Return a deep copy of this grid.
'''
    ...
    def empty (self, *args, **kwargs):
      '''empty() -> bool

Return True if this grid contains only background voxels.'''
    ...
    def evalActiveVoxelBoundingBox (self, *args, **kwargs):
      '''evalActiveVoxelBoundingBox() -> xyzMin, xyzMax

Return the coordinates of opposite corners of the axis-aligned
bounding box of all active voxels.'''
    ...
    def evalActiveVoxelDim (self, *args, **kwargs):
      '''evalActiveVoxelDim() -> x, y, z

Return the dimensions of the axis-aligned bounding box of all
active voxels.'''
    ...
    def evalLeafBoundingBox (self, *args, **kwargs):
      '''evalLeafBoundingBox() -> xyzMin, xyzMax

Return the coordinates of opposite corners of the axis-aligned
bounding box of all leaf nodes.'''
    ...
    def evalLeafDim (self, *args, **kwargs):
      '''evalLeafDim() -> x, y, z

Return the dimensions of the axis-aligned bounding box
of all leaf nodes.'''
    ...
    def evalMinMax (self, *args, **kwargs):
      '''evalMinMax() -> min, max

Return the minimum and maximum active values in this grid.'''
    ...
    def fill (self, *args, **kwargs):
      '''fill(min, max, value, active=True)

Set all voxels within a given axis-aligned box to
a constant value (either active or inactive).'''
    ...
    def getAccessor (self, *args, **kwargs):
      '''getAccessor() -> FloatGridAccessor

Return an accessor that provides random read and write access
to this grid's voxels.'''
    ...
    def getConstAccessor (self, *args, **kwargs):
      '''getConstAccessor() -> FloatGridAccessor

Return an accessor that provides random read-only access
to this grid's voxels.'''
    ...
    def getIndexRange (self, *args, **kwargs):
      '''getIndexRange() -> min, max

Return the minimum and maximum coordinates that are represented
in this grid.  These might include background voxels.'''
    ...
    def getStatsMetadata (self, *args, **kwargs):
      '''getStatsMetadata() -> dict

Return a (possibly empty) dict containing just the metadata
that was added to this grid with addStatsMetadata().'''
    ...
    def gridClass (self, *args, **kwargs):
      '''the class of volumetric data (level set, fog volume, etc.)
stored in this grid'''
    ...
    def info (self, *args, **kwargs):
      '''info(verbosity=1) -> str

Return a string containing information about this grid
with a specified level of verbosity.
'''
    ...
    def iterAllValues (self, *args, **kwargs):
      '''iterAllValues() -> iterator

Return a read/write iterator over all of this grid's
tile and voxel values.'''
    ...
    def iterOffValues (self, *args, **kwargs):
      '''iterOffValues() -> iterator

Return a read/write iterator over this grid's inactive
tile and voxel values.'''
    ...
    def iterOnValues (self, *args, **kwargs):
      '''iterOnValues() -> iterator

Return a read/write iterator over this grid's active
tile and voxel values.'''
    ...
    def iterkeys (self, *args, **kwargs):
      '''iterkeys() -> iterator

Return an iterator over this grid's metadata keys.'''
    ...
    def leafCount (self, *args, **kwargs):
      '''leafCount() -> int

Return the number of leaf nodes in this grid's tree.'''
    ...
    def mapAll (self, *args, **kwargs):
      '''mapAll(function)

Iterate over all values (tile and voxel) of this grid
and replace each value with function(value).

Example: grid.mapAll(lambda x: x * 2 if x < 0.5 else x)'''
    ...
    def mapOff (self, *args, **kwargs):
      '''mapOff(function)

Iterate over all the inactive ("off") values (tile and voxel)
of this grid and replace each value with function(value).

Example: grid.mapOff(lambda x: x * 2 if x < 0.5 else x)'''
    ...
    def mapOn (self, *args, **kwargs):
      '''mapOn(function)

Iterate over all the active ("on") values (tile and voxel)
of this grid and replace each value with function(value).

Example: grid.mapOn(lambda x: x * 2 if x < 0.5 else x)'''
    ...
    def memUsage (self, *args, **kwargs):
      '''memUsage() -> int

Return the memory usage of this grid in bytes.'''
    ...
    def merge (self, *args, **kwargs):
      '''merge(FloatGrid)

Move child nodes from the other grid into this grid wherever
those nodes correspond to constant-value tiles in this grid,
and replace leaf-level inactive voxels in this grid with
corresponding voxels in the other grid that are active.

Note: this operation always empties the other grid.'''
    ...
    def metadata (self, *args, **kwargs):
      '''dict of this grid's metadata

Setting this attribute replaces all of this grid's metadata,
but mutating it in place has no effect on the grid, since
the value of this attribute is a only a copy of the metadata.
Use either indexing or updateMetadata() to mutate metadata in place.'''
    ...
    def name (self, *args, **kwargs):
      '''this grid's user-specified name'''
    ...
    def nodeLog2Dims (self, *args, **kwargs):
      '''list of Log2Dims of the nodes of this grid's tree
in order from root to leaf'''
    ...
    def nonLeafCount (self, *args, **kwargs):
      '''nonLeafCount() -> int

Return the number of non-leaf nodes in this grid's tree.'''
    ...
    def oneValue (self, *args, **kwargs):
      '''Convert a string or number to a floating point number, if possible.'''
    ...
    def prune (self, *args, **kwargs):
      '''prune(tolerance=0)

Remove nodes whose values all have the same active state
and are equal to within a given tolerance.'''
    ...
    def pruneInactive (self, *args, **kwargs):
      '''pruneInactive()

Remove nodes whose values are all inactive and replace them
with background tiles.'''
    ...
    def saveFloatAsHalf (self, *args, **kwargs):
      '''if True, write floating-point voxel values as 16-bit half floats'''
    ...
    def sharesWith (self, *args, **kwargs):
      '''sharesWith(FloatGrid) -> bool

Return True if this grid shares its voxel data with the given grid.'''
    ...
    def signedFloodFill (self, *args, **kwargs):
      '''signedFloodFill()

Propagate the sign from a narrow-band level set into inactive
voxels and tiles.'''
    ...
    def transform (self, *args, **kwargs):
      '''transform associated with this grid'''
    ...
    def treeDepth (self, *args, **kwargs):
      '''depth of this grid's tree from root node to leaf node'''
    ...
    def updateMetadata (self, *args, **kwargs):
      '''updateMetadata(dict)

Add metadata to this grid, replacing any existing items
having the same names as the new items.'''
    ...
    def valueTypeName (self, *args, **kwargs):
      '''str(object='') -> str
str(bytes_or_buffer[, encoding[, errors]]) -> str

Create a new string object from the given object. If encoding or
errors is specified, then the object must expose a data buffer
that will be decoded using the given encoding and error handler.
Otherwise, returns the result of object.__str__() (if defined)
or repr(object).
encoding defaults to sys.getdefaultencoding().
errors defaults to 'strict'.'''
    ...
    def vectorType (self, *args, **kwargs):
      '''how transforms are applied to values stored in this grid'''
    ...
    def zeroValue (self, *args, **kwargs):
      '''Convert a string or number to a floating point number, if possible.'''
    ...

def FloatGridAccessor (*args):
      '''

'''      
    ...

class FloatGridAccessor:
    def clear (self, *args, **kwargs):
      '''clear()

Clear this accessor of all cached data.'''
    ...
    def copy (self, *args, **kwargs):
      '''copy() -> Accessor

Return a copy of this accessor.'''
    ...
    def getValue (self, *args, **kwargs):
      '''getValue(ijk) -> float

Return the value of the voxel at coordinates (i, j, k).'''
    ...
    def getValueDepth (self, *args, **kwargs):
      '''getValueDepth(ijk) -> int

Return the tree depth (0 = root) at which the value of voxel
(i, j, k) resides.  If (i, j, k) isn't explicitly represented in
the tree (i.e., it is implicitly a background voxel), return -1.'''
    ...
    def isCached (self, *args, **kwargs):
      '''isCached(ijk) -> bool

Return True if this accessor has cached the path to voxel (i, j, k).'''
    ...
    def isValueOn (self, *args, **kwargs):
      '''isValueOn(ijk) -> bool

Return the active state of the voxel at coordinates (i, j, k).'''
    ...
    def isVoxel (self, *args, **kwargs):
      '''isVoxel(ijk) -> bool

Return True if voxel (i, j, k) resides at the leaf level of the tree.'''
    ...
    def parent (self, *args, **kwargs):
      '''this accessor's parent FloatGrid'''
    ...
    def probeValue (self, *args, **kwargs):
      '''probeValue(ijk) -> value, bool

Return the value of the voxel at coordinates (i, j, k)
together with the voxel's active state.'''
    ...
    def setActiveState (self, *args, **kwargs):
      '''setActiveState(ijk, on)

Mark voxel (i, j, k) as either active or inactive (True or False),
but don't change its value.'''
    ...
    def setValueOff (self, *args, **kwargs):
      '''setValueOff(ijk, value)

Mark voxel (i, j, k) as inactive and set the voxel's value if specified.'''
    ...
    def setValueOn (self, *args, **kwargs):
      '''setValueOn(ijk, value)

Mark voxel (i, j, k) as active and set the voxel's value if specified.
'''
    ...
    def setValueOnly (self, *args, **kwargs):
      '''setValueOnly(ijk, value)

Set the value of voxel (i, j, k), but don't change its active state.'''
    ...

def FloatGridConstAccessor (*args):
      '''

'''      
    ...

class FloatGridConstAccessor:
    def clear (self, *args, **kwargs):
      '''clear()

Clear this accessor of all cached data.'''
    ...
    def copy (self, *args, **kwargs):
      '''copy() -> ConstAccessor

Return a copy of this accessor.'''
    ...
    def getValue (self, *args, **kwargs):
      '''getValue(ijk) -> float

Return the value of the voxel at coordinates (i, j, k).'''
    ...
    def getValueDepth (self, *args, **kwargs):
      '''getValueDepth(ijk) -> int

Return the tree depth (0 = root) at which the value of voxel
(i, j, k) resides.  If (i, j, k) isn't explicitly represented in
the tree (i.e., it is implicitly a background voxel), return -1.'''
    ...
    def isCached (self, *args, **kwargs):
      '''isCached(ijk) -> bool

Return True if this accessor has cached the path to voxel (i, j, k).'''
    ...
    def isValueOn (self, *args, **kwargs):
      '''isValueOn(ijk) -> bool

Return the active state of the voxel at coordinates (i, j, k).'''
    ...
    def isVoxel (self, *args, **kwargs):
      '''isVoxel(ijk) -> bool

Return True if voxel (i, j, k) resides at the leaf level of the tree.'''
    ...
    def parent (self, *args, **kwargs):
      '''this accessor's parent FloatGrid'''
    ...
    def probeValue (self, *args, **kwargs):
      '''probeValue(ijk) -> value, bool

Return the value of the voxel at coordinates (i, j, k)
together with the voxel's active state.'''
    ...
    def setActiveState (self, *args, **kwargs):
      '''setActiveState(ijk, on)

Mark voxel (i, j, k) as either active or inactive (True or False),
but don't change its value.'''
    ...
    def setValueOff (self, *args, **kwargs):
      '''setValueOff(ijk, value)

Mark voxel (i, j, k) as inactive and set the voxel's value if specified.'''
    ...
    def setValueOn (self, *args, **kwargs):
      '''setValueOn(ijk, value)

Mark voxel (i, j, k) as active and set the voxel's value if specified.
'''
    ...
    def setValueOnly (self, *args, **kwargs):
      '''setValueOnly(ijk, value)

Set the value of voxel (i, j, k), but don't change its active state.'''
    ...

def FloatGridValueAllCIter (*args):
      '''

'''      
    ...

class FloatGridValueAllCIter:
    def next (self, *args, **kwargs):
      '''next() -> FloatGridValueAllCIterValue'''
    ...
    def parent (self, *args, **kwargs):
      '''the FloatGrid over which to iterate'''
    ...

def FloatGridValueAllCIterValue (*args):
      '''

'''      
    ...

class FloatGridValueAllCIterValue:
    def active (self, *args, **kwargs):
      '''active state of this tile or voxel'''
    ...
    def copy (self, *args, **kwargs):
      '''copy() -> FloatGridValueAllCIterValue

Return a shallow copy of this value, i.e., one that shares
its data with the original.'''
    ...
    def count (self, *args, **kwargs):
      '''number of voxels spanned by this value'''
    ...
    def depth (self, *args, **kwargs):
      '''tree depth at which this value is stored'''
    ...
    def keys (self, *args, **kwargs):
      '''keys() -> list

Return a list of keys for this tile or voxel.'''
    ...
    def max (self, *args, **kwargs):
      '''upper bound of the axis-aligned bounding box of this tile or voxel'''
    ...
    def min (self, *args, **kwargs):
      '''lower bound of the axis-aligned bounding box of this tile or voxel'''
    ...
    def parent (self, *args, **kwargs):
      '''the FloatGrid to which this value belongs'''
    ...
    def value (self, *args, **kwargs):
      '''value of this tile or voxel'''
    ...

def FloatGridValueAllIter (*args):
      '''

'''      
    ...

class FloatGridValueAllIter:
    def next (self, *args, **kwargs):
      '''next() -> FloatGridValueAllIterValue'''
    ...
    def parent (self, *args, **kwargs):
      '''the FloatGrid over which to iterate'''
    ...

def FloatGridValueAllIterValue (*args):
      '''

'''      
    ...

class FloatGridValueAllIterValue:
    def active (self, *args, **kwargs):
      '''active state of this tile or voxel'''
    ...
    def copy (self, *args, **kwargs):
      '''copy() -> FloatGridValueAllIterValue

Return a shallow copy of this value, i.e., one that shares
its data with the original.'''
    ...
    def count (self, *args, **kwargs):
      '''number of voxels spanned by this value'''
    ...
    def depth (self, *args, **kwargs):
      '''tree depth at which this value is stored'''
    ...
    def keys (self, *args, **kwargs):
      '''keys() -> list

Return a list of keys for this tile or voxel.'''
    ...
    def max (self, *args, **kwargs):
      '''upper bound of the axis-aligned bounding box of this tile or voxel'''
    ...
    def min (self, *args, **kwargs):
      '''lower bound of the axis-aligned bounding box of this tile or voxel'''
    ...
    def parent (self, *args, **kwargs):
      '''the FloatGrid to which this value belongs'''
    ...
    def value (self, *args, **kwargs):
      '''value of this tile or voxel'''
    ...

def FloatGridValueOffCIter (*args):
      '''

'''      
    ...

class FloatGridValueOffCIter:
    def next (self, *args, **kwargs):
      '''next() -> FloatGridValueOffCIterValue'''
    ...
    def parent (self, *args, **kwargs):
      '''the FloatGrid over which to iterate'''
    ...

def FloatGridValueOffCIterValue (*args):
      '''

'''      
    ...

class FloatGridValueOffCIterValue:
    def active (self, *args, **kwargs):
      '''active state of this tile or voxel'''
    ...
    def copy (self, *args, **kwargs):
      '''copy() -> FloatGridValueOffCIterValue

Return a shallow copy of this value, i.e., one that shares
its data with the original.'''
    ...
    def count (self, *args, **kwargs):
      '''number of voxels spanned by this value'''
    ...
    def depth (self, *args, **kwargs):
      '''tree depth at which this value is stored'''
    ...
    def keys (self, *args, **kwargs):
      '''keys() -> list

Return a list of keys for this tile or voxel.'''
    ...
    def max (self, *args, **kwargs):
      '''upper bound of the axis-aligned bounding box of this tile or voxel'''
    ...
    def min (self, *args, **kwargs):
      '''lower bound of the axis-aligned bounding box of this tile or voxel'''
    ...
    def parent (self, *args, **kwargs):
      '''the FloatGrid to which this value belongs'''
    ...
    def value (self, *args, **kwargs):
      '''value of this tile or voxel'''
    ...

def FloatGridValueOffIter (*args):
      '''

'''      
    ...

class FloatGridValueOffIter:
    def next (self, *args, **kwargs):
      '''next() -> FloatGridValueOffIterValue'''
    ...
    def parent (self, *args, **kwargs):
      '''the FloatGrid over which to iterate'''
    ...

def FloatGridValueOffIterValue (*args):
      '''

'''      
    ...

class FloatGridValueOffIterValue:
    def active (self, *args, **kwargs):
      '''active state of this tile or voxel'''
    ...
    def copy (self, *args, **kwargs):
      '''copy() -> FloatGridValueOffIterValue

Return a shallow copy of this value, i.e., one that shares
its data with the original.'''
    ...
    def count (self, *args, **kwargs):
      '''number of voxels spanned by this value'''
    ...
    def depth (self, *args, **kwargs):
      '''tree depth at which this value is stored'''
    ...
    def keys (self, *args, **kwargs):
      '''keys() -> list

Return a list of keys for this tile or voxel.'''
    ...
    def max (self, *args, **kwargs):
      '''upper bound of the axis-aligned bounding box of this tile or voxel'''
    ...
    def min (self, *args, **kwargs):
      '''lower bound of the axis-aligned bounding box of this tile or voxel'''
    ...
    def parent (self, *args, **kwargs):
      '''the FloatGrid to which this value belongs'''
    ...
    def value (self, *args, **kwargs):
      '''value of this tile or voxel'''
    ...

def FloatGridValueOnCIter (*args):
      '''

'''      
    ...

class FloatGridValueOnCIter:
    def next (self, *args, **kwargs):
      '''next() -> FloatGridValueOnCIterValue'''
    ...
    def parent (self, *args, **kwargs):
      '''the FloatGrid over which to iterate'''
    ...

def FloatGridValueOnCIterValue (*args):
      '''

'''      
    ...

class FloatGridValueOnCIterValue:
    def active (self, *args, **kwargs):
      '''active state of this tile or voxel'''
    ...
    def copy (self, *args, **kwargs):
      '''copy() -> FloatGridValueOnCIterValue

Return a shallow copy of this value, i.e., one that shares
its data with the original.'''
    ...
    def count (self, *args, **kwargs):
      '''number of voxels spanned by this value'''
    ...
    def depth (self, *args, **kwargs):
      '''tree depth at which this value is stored'''
    ...
    def keys (self, *args, **kwargs):
      '''keys() -> list

Return a list of keys for this tile or voxel.'''
    ...
    def max (self, *args, **kwargs):
      '''upper bound of the axis-aligned bounding box of this tile or voxel'''
    ...
    def min (self, *args, **kwargs):
      '''lower bound of the axis-aligned bounding box of this tile or voxel'''
    ...
    def parent (self, *args, **kwargs):
      '''the FloatGrid to which this value belongs'''
    ...
    def value (self, *args, **kwargs):
      '''value of this tile or voxel'''
    ...

def FloatGridValueOnIter (*args):
      '''

'''      
    ...

class FloatGridValueOnIter:
    def next (self, *args, **kwargs):
      '''next() -> FloatGridValueOnIterValue'''
    ...
    def parent (self, *args, **kwargs):
      '''the FloatGrid over which to iterate'''
    ...

def FloatGridValueOnIterValue (*args):
      '''

'''      
    ...

class FloatGridValueOnIterValue:
    def active (self, *args, **kwargs):
      '''active state of this tile or voxel'''
    ...
    def copy (self, *args, **kwargs):
      '''copy() -> FloatGridValueOnIterValue

Return a shallow copy of this value, i.e., one that shares
its data with the original.'''
    ...
    def count (self, *args, **kwargs):
      '''number of voxels spanned by this value'''
    ...
    def depth (self, *args, **kwargs):
      '''tree depth at which this value is stored'''
    ...
    def keys (self, *args, **kwargs):
      '''keys() -> list

Return a list of keys for this tile or voxel.'''
    ...
    def max (self, *args, **kwargs):
      '''upper bound of the axis-aligned bounding box of this tile or voxel'''
    ...
    def min (self, *args, **kwargs):
      '''lower bound of the axis-aligned bounding box of this tile or voxel'''
    ...
    def parent (self, *args, **kwargs):
      '''the FloatGrid to which this value belongs'''
    ...
    def value (self, *args, **kwargs):
      '''value of this tile or voxel'''
    ...

def GridBase (*args):
      '''

'''      
    ...

class GridBase:
    def activeVoxelCount (self, *args, **kwargs):
      '''activeVoxelCount() -> int

Return the number of active voxels in this grid.'''
    ...
    def addStatsMetadata (self, *args, **kwargs):
      '''addStatsMetadata()

Add metadata to this grid comprising the current values
of statistics like the active voxel count and bounding box.
(This metadata is not automatically kept up-to-date with
changes to this grid.)'''
    ...
    def clear (self, *args, **kwargs):
      '''clear()

Remove all tiles from this grid and all nodes other than the root node.'''
    ...
    def creator (self, *args, **kwargs):
      '''user-specified description of this grid's creator'''
    ...
    def empty (self, *args, **kwargs):
      '''empty() -> bool

Return True if this grid contains only background voxels.'''
    ...
    def evalActiveVoxelBoundingBox (self, *args, **kwargs):
      '''evalActiveVoxelBoundingBox() -> xyzMin, xyzMax

Return the coordinates of opposite corners of the axis-aligned
bounding box of all active voxels.'''
    ...
    def evalActiveVoxelDim (self, *args, **kwargs):
      '''evalActiveVoxelDim() -> x, y, z

Return the dimensions of the axis-aligned bounding box of all
active voxels.'''
    ...
    def getStatsMetadata (self, *args, **kwargs):
      '''getStatsMetadata() -> dict

Return a (possibly empty) dict containing just the metadata
that was added to this grid with addStatsMetadata().'''
    ...
    def gridClass (self, *args, **kwargs):
      '''the class of volumetric data (level set, fog volume, etc.)
stored in this grid'''
    ...
    def info (self, *args, **kwargs):
      '''info(verbosity=1) -> str

Return a string containing information about this grid
with a specified level of verbosity.
'''
    ...
    def iterkeys (self, *args, **kwargs):
      '''iterkeys() -> iterator

Return an iterator over this grid's metadata keys.'''
    ...
    def memUsage (self, *args, **kwargs):
      '''memUsage() -> int

Return the memory usage of this grid in bytes.'''
    ...
    def metadata (self, *args, **kwargs):
      '''dict of this grid's metadata

Setting this attribute replaces all of this grid's metadata,
but mutating it in place has no effect on the grid, since
the value of this attribute is a only a copy of the metadata.
Use either indexing or updateMetadata() to mutate metadata in place.'''
    ...
    def name (self, *args, **kwargs):
      '''this grid's user-specified name'''
    ...
    def saveFloatAsHalf (self, *args, **kwargs):
      '''if True, write floating-point voxel values as 16-bit half floats'''
    ...
    def transform (self, *args, **kwargs):
      '''transform associated with this grid'''
    ...
    def updateMetadata (self, *args, **kwargs):
      '''updateMetadata(dict)

Add metadata to this grid, replacing any existing items
having the same names as the new items.'''
    ...
    def vectorType (self, *args, **kwargs):
      '''how transforms are applied to values stored in this grid'''
    ...

def GridClass (*args):
      '''

'''      
    ...

class GridClass:
    def FOG_VOLUME (self, *args, **kwargs):
      '''str(object='') -> str
str(bytes_or_buffer[, encoding[, errors]]) -> str

Create a new string object from the given object. If encoding or
errors is specified, then the object must expose a data buffer
that will be decoded using the given encoding and error handler.
Otherwise, returns the result of object.__str__() (if defined)
or repr(object).
encoding defaults to sys.getdefaultencoding().
errors defaults to 'strict'.'''
    ...
    def LEVEL_SET (self, *args, **kwargs):
      '''str(object='') -> str
str(bytes_or_buffer[, encoding[, errors]]) -> str

Create a new string object from the given object. If encoding or
errors is specified, then the object must expose a data buffer
that will be decoded using the given encoding and error handler.
Otherwise, returns the result of object.__str__() (if defined)
or repr(object).
encoding defaults to sys.getdefaultencoding().
errors defaults to 'strict'.'''
    ...
    def STAGGERED (self, *args, **kwargs):
      '''str(object='') -> str
str(bytes_or_buffer[, encoding[, errors]]) -> str

Create a new string object from the given object. If encoding or
errors is specified, then the object must expose a data buffer
that will be decoded using the given encoding and error handler.
Otherwise, returns the result of object.__str__() (if defined)
or repr(object).
encoding defaults to sys.getdefaultencoding().
errors defaults to 'strict'.'''
    ...
    def UNKNOWN (self, *args, **kwargs):
      '''str(object='') -> str
str(bytes_or_buffer[, encoding[, errors]]) -> str

Create a new string object from the given object. If encoding or
errors is specified, then the object must expose a data buffer
that will be decoded using the given encoding and error handler.
Otherwise, returns the result of object.__str__() (if defined)
or repr(object).
encoding defaults to sys.getdefaultencoding().
errors defaults to 'strict'.'''
    ...
    def keys (self, *args, **kwargs):
      '''keys() -> list'''
    ...

def GridTypes (*args):
      '''

'''      
    ...

def LEVEL_SET_HALF_WIDTH (*args):
      '''

'''      
    ...

def LIBRARY_VERSION (*args):
      '''

'''      
    ...

def Metadata (*args):
      '''

'''      
    ...

class Metadata:
    def copy (self, *args, **kwargs):
      '''copy() -> Metadata

Return a copy of this value.
copy() -> Metadata

Return a copy of this value.'''
    ...
    def size (self, *args, **kwargs):
      '''size() -> int

Return the size of this value in bytes.'''
    ...
    def type (self, *args, **kwargs):
      '''type() -> str

Return the name of this value's type.'''
    ...

def PointDataIndex32 (*args):
      '''

'''      
    ...

class PointDataIndex32:

def Transform (*args):
      '''

'''      
    ...

class Transform:
    def deepCopy (self, *args, **kwargs):
      '''deepCopy() -> Transform

Return a copy of this transform.'''
    ...
    def indexToWorld (self, *args, **kwargs):
      '''indexToWorld((x, y, z)) -> (x', y', z')

Apply this transformation to the given coordinates.'''
    ...
    def info (self, *args, **kwargs):
      '''info() -> str

Return a string containing a description of this transform.
'''
    ...
    def isLinear (self, *args, **kwargs):
      '''True if this transform is linear'''
    ...
    def rotate (self, *args, **kwargs):
      '''rotate(radians, axis)

Accumulate a rotation about either Axis.X, Axis.Y or Axis.Z.'''
    ...
    def scale (self, *args, **kwargs):
      '''scale(s)

Accumulate a uniform scale.
scale((sx, sy, sz))

Accumulate a nonuniform scale.'''
    ...
    def shear (self, *args, **kwargs):
      '''shear(s, axis0, axis1)

Accumulate a shear (axis0 and axis1 are either
Axis.X, Axis.Y or Axis.Z).'''
    ...
    def translate (self, *args, **kwargs):
      '''translate((x, y, z))

Accumulate a translation.'''
    ...
    def typeName (self, *args, **kwargs):
      '''name of this transform's type'''
    ...
    def voxelSize (self, *args, **kwargs):
      '''voxelSize() -> (dx, dy, dz)

Return the size of voxels of the linear component of this transform.
voxelSize((x, y, z)) -> (dx, dy, dz)

Return the size of the voxel at position (x, y, z).'''
    ...
    def voxelVolume (self, *args, **kwargs):
      '''voxelVolume() -> float

Return the voxel volume of the linear component of this transform.
voxelVolume((x, y, z)) -> float

Return the voxel volume at position (x, y, z).'''
    ...
    def worldToIndex (self, *args, **kwargs):
      '''worldToIndex((x, y, z)) -> (x', y', z')

Apply the inverse of this transformation to the given coordinates.'''
    ...
    def worldToIndexCellCentered (self, *args, **kwargs):
      '''worldToIndexCellCentered((x, y, z)) -> (i, j, k)

Apply the inverse of this transformation to the given coordinates
and round the result to the nearest integer coordinates.'''
    ...
    def worldToIndexNodeCentered (self, *args, **kwargs):
      '''worldToIndexNodeCentered((x, y, z)) -> (i, j, k)

Apply the inverse of this transformation to the given coordinates
and round the result down to the nearest integer coordinates.'''
    ...

def Vec2d (*args):
      '''

'''      
    ...

class Vec2d:

def Vec2f (*args):
      '''

'''      
    ...

class Vec2f:

def Vec2i (*args):
      '''

'''      
    ...

class Vec2i:

def Vec3SGrid (*args):
      '''

'''      
    ...

class Vec3SGrid:
    def activeLeafVoxelCount (self, *args, **kwargs):
      '''activeLeafVoxelCount() -> int

Return the number of active voxels that are stored
in the leaf nodes of this grid's tree.'''
    ...
    def activeVoxelCount (self, *args, **kwargs):
      '''activeVoxelCount() -> int

Return the number of active voxels in this grid.'''
    ...
    def addStatsMetadata (self, *args, **kwargs):
      '''addStatsMetadata()

Add metadata to this grid comprising the current values
of statistics like the active voxel count and bounding box.
(This metadata is not automatically kept up-to-date with
changes to this grid.)'''
    ...
    def background (self, *args, **kwargs):
      '''value of this grid's background voxels'''
    ...
    def citerAllValues (self, *args, **kwargs):
      '''iterAllValues() -> iterator

Return a read-only iterator over all of this grid's
tile and voxel values.'''
    ...
    def citerOffValues (self, *args, **kwargs):
      '''iterOffValues() -> iterator

Return a read-only iterator over this grid's inactive
tile and voxel values.'''
    ...
    def citerOnValues (self, *args, **kwargs):
      '''citerOnValues() -> iterator

Return a read-only iterator over this grid's active
tile and voxel values.'''
    ...
    def clear (self, *args, **kwargs):
      '''clear()

Remove all tiles from this grid and all nodes other than the root node.'''
    ...
    def combine (self, *args, **kwargs):
      '''combine(grid, function)

Compute function(self, other) over all corresponding pairs
of values (tile or voxel) of this grid and the other grid
and store the result in this grid.

Note: this operation always empties the other grid.

Example: grid.combine(otherGrid, lambda a, b: min(a, b))'''
    ...
    def convertToPolygons (self, *args, **kwargs):
      '''convertToPolygons(isovalue=0, adaptivity=0) -> points, triangles, quads

Adaptively mesh a scalar grid that has a continuous isosurface
at the given isovalue.  Return a NumPy array of world-space
points and NumPy arrays of 3- and 4-tuples of point indices,
which specify the vertices of the triangles and quadrilaterals
that form the mesh.  Adaptivity can vary from 0 to 1, where 0
produces a high-polygon-count mesh that closely approximates
the isosurface, and 1 produces a lower-polygon-count mesh
with some loss of surface detail.'''
    ...
    def convertToQuads (self, *args, **kwargs):
      '''convertToQuads(isovalue=0) -> points, quads

Uniformly mesh a scalar grid that has a continuous isosurface
at the given isovalue.  Return a NumPy array of world-space
points and a NumPy array of 4-tuples of point indices, which
specify the vertices of the quadrilaterals that form the mesh.'''
    ...
    def copy (self, *args, **kwargs):
      '''copy() -> Vec3SGrid

Return a shallow copy of this grid, i.e., a grid
that shares its voxel data with this grid.'''
    ...
    def copyFromArray (self, *args, **kwargs):
      '''copyFromArray(array, ijk=(0, 0, 0), tolerance=0)

Populate this grid, starting at voxel (i, j, k), with values
from a four-dimensional array.  Mark voxels as inactive
if and only if their values are equal to this grid's
background value within the given tolerance.'''
    ...
    def copyToArray (self, *args, **kwargs):
      '''copyToArray(array, ijk=(0, 0, 0))

Populate a four-dimensional array with values
from this grid, starting at voxel (i, j, k).'''
    ...
    def createLevelSetFromPolygons (self, *args, **kwargs):
      '''createLevelSetFromPolygons(points, triangles=None, quads=None,
    transform=None, halfWidth=3.000000) -> Vec3SGrid

Convert a triangle and/or quad mesh to a narrow-band level set volume.
The mesh must form a closed surface, but the surface need not be
manifold and may have self intersections and degenerate faces.
The mesh is described by a NumPy array of world-space points
and NumPy arrays of 3- and 4-tuples of point indices that specify
the vertices of the triangles and quadrilaterals that form the mesh.
Either the triangle or the quad array may be empty or None.
The resulting volume will have the given transform (or the identity
transform if no transform is given) and a narrow band width of
2 x halfWidth voxels.'''
    ...
    def creator (self, *args, **kwargs):
      '''user-specified description of this grid's creator'''
    ...
    def deepCopy (self, *args, **kwargs):
      '''deepCopy() -> Vec3SGrid

Return a deep copy of this grid.
'''
    ...
    def empty (self, *args, **kwargs):
      '''empty() -> bool

Return True if this grid contains only background voxels.'''
    ...
    def evalActiveVoxelBoundingBox (self, *args, **kwargs):
      '''evalActiveVoxelBoundingBox() -> xyzMin, xyzMax

Return the coordinates of opposite corners of the axis-aligned
bounding box of all active voxels.'''
    ...
    def evalActiveVoxelDim (self, *args, **kwargs):
      '''evalActiveVoxelDim() -> x, y, z

Return the dimensions of the axis-aligned bounding box of all
active voxels.'''
    ...
    def evalLeafBoundingBox (self, *args, **kwargs):
      '''evalLeafBoundingBox() -> xyzMin, xyzMax

Return the coordinates of opposite corners of the axis-aligned
bounding box of all leaf nodes.'''
    ...
    def evalLeafDim (self, *args, **kwargs):
      '''evalLeafDim() -> x, y, z

Return the dimensions of the axis-aligned bounding box
of all leaf nodes.'''
    ...
    def evalMinMax (self, *args, **kwargs):
      '''evalMinMax() -> min, max

Return the minimum and maximum active values in this grid.'''
    ...
    def fill (self, *args, **kwargs):
      '''fill(min, max, value, active=True)

Set all voxels within a given axis-aligned box to
a constant value (either active or inactive).'''
    ...
    def getAccessor (self, *args, **kwargs):
      '''getAccessor() -> Vec3SGridAccessor

Return an accessor that provides random read and write access
to this grid's voxels.'''
    ...
    def getConstAccessor (self, *args, **kwargs):
      '''getConstAccessor() -> Vec3SGridAccessor

Return an accessor that provides random read-only access
to this grid's voxels.'''
    ...
    def getIndexRange (self, *args, **kwargs):
      '''getIndexRange() -> min, max

Return the minimum and maximum coordinates that are represented
in this grid.  These might include background voxels.'''
    ...
    def getStatsMetadata (self, *args, **kwargs):
      '''getStatsMetadata() -> dict

Return a (possibly empty) dict containing just the metadata
that was added to this grid with addStatsMetadata().'''
    ...
    def gridClass (self, *args, **kwargs):
      '''the class of volumetric data (level set, fog volume, etc.)
stored in this grid'''
    ...
    def info (self, *args, **kwargs):
      '''info(verbosity=1) -> str

Return a string containing information about this grid
with a specified level of verbosity.
'''
    ...
    def iterAllValues (self, *args, **kwargs):
      '''iterAllValues() -> iterator

Return a read/write iterator over all of this grid's
tile and voxel values.'''
    ...
    def iterOffValues (self, *args, **kwargs):
      '''iterOffValues() -> iterator

Return a read/write iterator over this grid's inactive
tile and voxel values.'''
    ...
    def iterOnValues (self, *args, **kwargs):
      '''iterOnValues() -> iterator

Return a read/write iterator over this grid's active
tile and voxel values.'''
    ...
    def iterkeys (self, *args, **kwargs):
      '''iterkeys() -> iterator

Return an iterator over this grid's metadata keys.'''
    ...
    def leafCount (self, *args, **kwargs):
      '''leafCount() -> int

Return the number of leaf nodes in this grid's tree.'''
    ...
    def mapAll (self, *args, **kwargs):
      '''mapAll(function)

Iterate over all values (tile and voxel) of this grid
and replace each value with function(value).

Example: grid.mapAll(lambda x: x * 2 if x < 0.5 else x)'''
    ...
    def mapOff (self, *args, **kwargs):
      '''mapOff(function)

Iterate over all the inactive ("off") values (tile and voxel)
of this grid and replace each value with function(value).

Example: grid.mapOff(lambda x: x * 2 if x < 0.5 else x)'''
    ...
    def mapOn (self, *args, **kwargs):
      '''mapOn(function)

Iterate over all the active ("on") values (tile and voxel)
of this grid and replace each value with function(value).

Example: grid.mapOn(lambda x: x * 2 if x < 0.5 else x)'''
    ...
    def memUsage (self, *args, **kwargs):
      '''memUsage() -> int

Return the memory usage of this grid in bytes.'''
    ...
    def merge (self, *args, **kwargs):
      '''merge(Vec3SGrid)

Move child nodes from the other grid into this grid wherever
those nodes correspond to constant-value tiles in this grid,
and replace leaf-level inactive voxels in this grid with
corresponding voxels in the other grid that are active.

Note: this operation always empties the other grid.'''
    ...
    def metadata (self, *args, **kwargs):
      '''dict of this grid's metadata

Setting this attribute replaces all of this grid's metadata,
but mutating it in place has no effect on the grid, since
the value of this attribute is a only a copy of the metadata.
Use either indexing or updateMetadata() to mutate metadata in place.'''
    ...
    def name (self, *args, **kwargs):
      '''this grid's user-specified name'''
    ...
    def nodeLog2Dims (self, *args, **kwargs):
      '''list of Log2Dims of the nodes of this grid's tree
in order from root to leaf'''
    ...
    def nonLeafCount (self, *args, **kwargs):
      '''nonLeafCount() -> int

Return the number of non-leaf nodes in this grid's tree.'''
    ...
    def oneValue (self, *args, **kwargs):
      '''Built-in immutable sequence.

If no argument is given, the constructor returns an empty tuple.
If iterable is specified the tuple is initialized from iterable's items.

If the argument is a tuple, the return value is the same object.'''
    ...
    def prune (self, *args, **kwargs):
      '''prune(tolerance=0)

Remove nodes whose values all have the same active state
and are equal to within a given tolerance.'''
    ...
    def pruneInactive (self, *args, **kwargs):
      '''pruneInactive()

Remove nodes whose values are all inactive and replace them
with background tiles.'''
    ...
    def saveFloatAsHalf (self, *args, **kwargs):
      '''if True, write floating-point voxel values as 16-bit half floats'''
    ...
    def sharesWith (self, *args, **kwargs):
      '''sharesWith(Vec3SGrid) -> bool

Return True if this grid shares its voxel data with the given grid.'''
    ...
    def signedFloodFill (self, *args, **kwargs):
      '''signedFloodFill()

Propagate the sign from a narrow-band level set into inactive
voxels and tiles.'''
    ...
    def transform (self, *args, **kwargs):
      '''transform associated with this grid'''
    ...
    def treeDepth (self, *args, **kwargs):
      '''depth of this grid's tree from root node to leaf node'''
    ...
    def updateMetadata (self, *args, **kwargs):
      '''updateMetadata(dict)

Add metadata to this grid, replacing any existing items
having the same names as the new items.'''
    ...
    def valueTypeName (self, *args, **kwargs):
      '''str(object='') -> str
str(bytes_or_buffer[, encoding[, errors]]) -> str

Create a new string object from the given object. If encoding or
errors is specified, then the object must expose a data buffer
that will be decoded using the given encoding and error handler.
Otherwise, returns the result of object.__str__() (if defined)
or repr(object).
encoding defaults to sys.getdefaultencoding().
errors defaults to 'strict'.'''
    ...
    def vectorType (self, *args, **kwargs):
      '''how transforms are applied to values stored in this grid'''
    ...
    def zeroValue (self, *args, **kwargs):
      '''Built-in immutable sequence.

If no argument is given, the constructor returns an empty tuple.
If iterable is specified the tuple is initialized from iterable's items.

If the argument is a tuple, the return value is the same object.'''
    ...

def Vec3SGridAccessor (*args):
      '''

'''      
    ...

class Vec3SGridAccessor:
    def clear (self, *args, **kwargs):
      '''clear()

Clear this accessor of all cached data.'''
    ...
    def copy (self, *args, **kwargs):
      '''copy() -> Accessor

Return a copy of this accessor.'''
    ...
    def getValue (self, *args, **kwargs):
      '''getValue(ijk) -> vec3s

Return the value of the voxel at coordinates (i, j, k).'''
    ...
    def getValueDepth (self, *args, **kwargs):
      '''getValueDepth(ijk) -> int

Return the tree depth (0 = root) at which the value of voxel
(i, j, k) resides.  If (i, j, k) isn't explicitly represented in
the tree (i.e., it is implicitly a background voxel), return -1.'''
    ...
    def isCached (self, *args, **kwargs):
      '''isCached(ijk) -> bool

Return True if this accessor has cached the path to voxel (i, j, k).'''
    ...
    def isValueOn (self, *args, **kwargs):
      '''isValueOn(ijk) -> bool

Return the active state of the voxel at coordinates (i, j, k).'''
    ...
    def isVoxel (self, *args, **kwargs):
      '''isVoxel(ijk) -> bool

Return True if voxel (i, j, k) resides at the leaf level of the tree.'''
    ...
    def parent (self, *args, **kwargs):
      '''this accessor's parent Vec3SGrid'''
    ...
    def probeValue (self, *args, **kwargs):
      '''probeValue(ijk) -> value, bool

Return the value of the voxel at coordinates (i, j, k)
together with the voxel's active state.'''
    ...
    def setActiveState (self, *args, **kwargs):
      '''setActiveState(ijk, on)

Mark voxel (i, j, k) as either active or inactive (True or False),
but don't change its value.'''
    ...
    def setValueOff (self, *args, **kwargs):
      '''setValueOff(ijk, value)

Mark voxel (i, j, k) as inactive and set the voxel's value if specified.'''
    ...
    def setValueOn (self, *args, **kwargs):
      '''setValueOn(ijk, value)

Mark voxel (i, j, k) as active and set the voxel's value if specified.
'''
    ...
    def setValueOnly (self, *args, **kwargs):
      '''setValueOnly(ijk, value)

Set the value of voxel (i, j, k), but don't change its active state.'''
    ...

def Vec3SGridConstAccessor (*args):
      '''

'''      
    ...

class Vec3SGridConstAccessor:
    def clear (self, *args, **kwargs):
      '''clear()

Clear this accessor of all cached data.'''
    ...
    def copy (self, *args, **kwargs):
      '''copy() -> ConstAccessor

Return a copy of this accessor.'''
    ...
    def getValue (self, *args, **kwargs):
      '''getValue(ijk) -> vec3s

Return the value of the voxel at coordinates (i, j, k).'''
    ...
    def getValueDepth (self, *args, **kwargs):
      '''getValueDepth(ijk) -> int

Return the tree depth (0 = root) at which the value of voxel
(i, j, k) resides.  If (i, j, k) isn't explicitly represented in
the tree (i.e., it is implicitly a background voxel), return -1.'''
    ...
    def isCached (self, *args, **kwargs):
      '''isCached(ijk) -> bool

Return True if this accessor has cached the path to voxel (i, j, k).'''
    ...
    def isValueOn (self, *args, **kwargs):
      '''isValueOn(ijk) -> bool

Return the active state of the voxel at coordinates (i, j, k).'''
    ...
    def isVoxel (self, *args, **kwargs):
      '''isVoxel(ijk) -> bool

Return True if voxel (i, j, k) resides at the leaf level of the tree.'''
    ...
    def parent (self, *args, **kwargs):
      '''this accessor's parent Vec3SGrid'''
    ...
    def probeValue (self, *args, **kwargs):
      '''probeValue(ijk) -> value, bool

Return the value of the voxel at coordinates (i, j, k)
together with the voxel's active state.'''
    ...
    def setActiveState (self, *args, **kwargs):
      '''setActiveState(ijk, on)

Mark voxel (i, j, k) as either active or inactive (True or False),
but don't change its value.'''
    ...
    def setValueOff (self, *args, **kwargs):
      '''setValueOff(ijk, value)

Mark voxel (i, j, k) as inactive and set the voxel's value if specified.'''
    ...
    def setValueOn (self, *args, **kwargs):
      '''setValueOn(ijk, value)

Mark voxel (i, j, k) as active and set the voxel's value if specified.
'''
    ...
    def setValueOnly (self, *args, **kwargs):
      '''setValueOnly(ijk, value)

Set the value of voxel (i, j, k), but don't change its active state.'''
    ...

def Vec3SGridValueAllCIter (*args):
      '''

'''      
    ...

class Vec3SGridValueAllCIter:
    def next (self, *args, **kwargs):
      '''next() -> Vec3SGridValueAllCIterValue'''
    ...
    def parent (self, *args, **kwargs):
      '''the Vec3SGrid over which to iterate'''
    ...

def Vec3SGridValueAllCIterValue (*args):
      '''

'''      
    ...

class Vec3SGridValueAllCIterValue:
    def active (self, *args, **kwargs):
      '''active state of this tile or voxel'''
    ...
    def copy (self, *args, **kwargs):
      '''copy() -> Vec3SGridValueAllCIterValue

Return a shallow copy of this value, i.e., one that shares
its data with the original.'''
    ...
    def count (self, *args, **kwargs):
      '''number of voxels spanned by this value'''
    ...
    def depth (self, *args, **kwargs):
      '''tree depth at which this value is stored'''
    ...
    def keys (self, *args, **kwargs):
      '''keys() -> list

Return a list of keys for this tile or voxel.'''
    ...
    def max (self, *args, **kwargs):
      '''upper bound of the axis-aligned bounding box of this tile or voxel'''
    ...
    def min (self, *args, **kwargs):
      '''lower bound of the axis-aligned bounding box of this tile or voxel'''
    ...
    def parent (self, *args, **kwargs):
      '''the Vec3SGrid to which this value belongs'''
    ...
    def value (self, *args, **kwargs):
      '''value of this tile or voxel'''
    ...

def Vec3SGridValueAllIter (*args):
      '''

'''      
    ...

class Vec3SGridValueAllIter:
    def next (self, *args, **kwargs):
      '''next() -> Vec3SGridValueAllIterValue'''
    ...
    def parent (self, *args, **kwargs):
      '''the Vec3SGrid over which to iterate'''
    ...

def Vec3SGridValueAllIterValue (*args):
      '''

'''      
    ...

class Vec3SGridValueAllIterValue:
    def active (self, *args, **kwargs):
      '''active state of this tile or voxel'''
    ...
    def copy (self, *args, **kwargs):
      '''copy() -> Vec3SGridValueAllIterValue

Return a shallow copy of this value, i.e., one that shares
its data with the original.'''
    ...
    def count (self, *args, **kwargs):
      '''number of voxels spanned by this value'''
    ...
    def depth (self, *args, **kwargs):
      '''tree depth at which this value is stored'''
    ...
    def keys (self, *args, **kwargs):
      '''keys() -> list

Return a list of keys for this tile or voxel.'''
    ...
    def max (self, *args, **kwargs):
      '''upper bound of the axis-aligned bounding box of this tile or voxel'''
    ...
    def min (self, *args, **kwargs):
      '''lower bound of the axis-aligned bounding box of this tile or voxel'''
    ...
    def parent (self, *args, **kwargs):
      '''the Vec3SGrid to which this value belongs'''
    ...
    def value (self, *args, **kwargs):
      '''value of this tile or voxel'''
    ...

def Vec3SGridValueOffCIter (*args):
      '''

'''      
    ...

class Vec3SGridValueOffCIter:
    def next (self, *args, **kwargs):
      '''next() -> Vec3SGridValueOffCIterValue'''
    ...
    def parent (self, *args, **kwargs):
      '''the Vec3SGrid over which to iterate'''
    ...

def Vec3SGridValueOffCIterValue (*args):
      '''

'''      
    ...

class Vec3SGridValueOffCIterValue:
    def active (self, *args, **kwargs):
      '''active state of this tile or voxel'''
    ...
    def copy (self, *args, **kwargs):
      '''copy() -> Vec3SGridValueOffCIterValue

Return a shallow copy of this value, i.e., one that shares
its data with the original.'''
    ...
    def count (self, *args, **kwargs):
      '''number of voxels spanned by this value'''
    ...
    def depth (self, *args, **kwargs):
      '''tree depth at which this value is stored'''
    ...
    def keys (self, *args, **kwargs):
      '''keys() -> list

Return a list of keys for this tile or voxel.'''
    ...
    def max (self, *args, **kwargs):
      '''upper bound of the axis-aligned bounding box of this tile or voxel'''
    ...
    def min (self, *args, **kwargs):
      '''lower bound of the axis-aligned bounding box of this tile or voxel'''
    ...
    def parent (self, *args, **kwargs):
      '''the Vec3SGrid to which this value belongs'''
    ...
    def value (self, *args, **kwargs):
      '''value of this tile or voxel'''
    ...

def Vec3SGridValueOffIter (*args):
      '''

'''      
    ...

class Vec3SGridValueOffIter:
    def next (self, *args, **kwargs):
      '''next() -> Vec3SGridValueOffIterValue'''
    ...
    def parent (self, *args, **kwargs):
      '''the Vec3SGrid over which to iterate'''
    ...

def Vec3SGridValueOffIterValue (*args):
      '''

'''      
    ...

class Vec3SGridValueOffIterValue:
    def active (self, *args, **kwargs):
      '''active state of this tile or voxel'''
    ...
    def copy (self, *args, **kwargs):
      '''copy() -> Vec3SGridValueOffIterValue

Return a shallow copy of this value, i.e., one that shares
its data with the original.'''
    ...
    def count (self, *args, **kwargs):
      '''number of voxels spanned by this value'''
    ...
    def depth (self, *args, **kwargs):
      '''tree depth at which this value is stored'''
    ...
    def keys (self, *args, **kwargs):
      '''keys() -> list

Return a list of keys for this tile or voxel.'''
    ...
    def max (self, *args, **kwargs):
      '''upper bound of the axis-aligned bounding box of this tile or voxel'''
    ...
    def min (self, *args, **kwargs):
      '''lower bound of the axis-aligned bounding box of this tile or voxel'''
    ...
    def parent (self, *args, **kwargs):
      '''the Vec3SGrid to which this value belongs'''
    ...
    def value (self, *args, **kwargs):
      '''value of this tile or voxel'''
    ...

def Vec3SGridValueOnCIter (*args):
      '''

'''      
    ...

class Vec3SGridValueOnCIter:
    def next (self, *args, **kwargs):
      '''next() -> Vec3SGridValueOnCIterValue'''
    ...
    def parent (self, *args, **kwargs):
      '''the Vec3SGrid over which to iterate'''
    ...

def Vec3SGridValueOnCIterValue (*args):
      '''

'''      
    ...

class Vec3SGridValueOnCIterValue:
    def active (self, *args, **kwargs):
      '''active state of this tile or voxel'''
    ...
    def copy (self, *args, **kwargs):
      '''copy() -> Vec3SGridValueOnCIterValue

Return a shallow copy of this value, i.e., one that shares
its data with the original.'''
    ...
    def count (self, *args, **kwargs):
      '''number of voxels spanned by this value'''
    ...
    def depth (self, *args, **kwargs):
      '''tree depth at which this value is stored'''
    ...
    def keys (self, *args, **kwargs):
      '''keys() -> list

Return a list of keys for this tile or voxel.'''
    ...
    def max (self, *args, **kwargs):
      '''upper bound of the axis-aligned bounding box of this tile or voxel'''
    ...
    def min (self, *args, **kwargs):
      '''lower bound of the axis-aligned bounding box of this tile or voxel'''
    ...
    def parent (self, *args, **kwargs):
      '''the Vec3SGrid to which this value belongs'''
    ...
    def value (self, *args, **kwargs):
      '''value of this tile or voxel'''
    ...

def Vec3SGridValueOnIter (*args):
      '''

'''      
    ...

class Vec3SGridValueOnIter:
    def next (self, *args, **kwargs):
      '''next() -> Vec3SGridValueOnIterValue'''
    ...
    def parent (self, *args, **kwargs):
      '''the Vec3SGrid over which to iterate'''
    ...

def Vec3SGridValueOnIterValue (*args):
      '''

'''      
    ...

class Vec3SGridValueOnIterValue:
    def active (self, *args, **kwargs):
      '''active state of this tile or voxel'''
    ...
    def copy (self, *args, **kwargs):
      '''copy() -> Vec3SGridValueOnIterValue

Return a shallow copy of this value, i.e., one that shares
its data with the original.'''
    ...
    def count (self, *args, **kwargs):
      '''number of voxels spanned by this value'''
    ...
    def depth (self, *args, **kwargs):
      '''tree depth at which this value is stored'''
    ...
    def keys (self, *args, **kwargs):
      '''keys() -> list

Return a list of keys for this tile or voxel.'''
    ...
    def max (self, *args, **kwargs):
      '''upper bound of the axis-aligned bounding box of this tile or voxel'''
    ...
    def min (self, *args, **kwargs):
      '''lower bound of the axis-aligned bounding box of this tile or voxel'''
    ...
    def parent (self, *args, **kwargs):
      '''the Vec3SGrid to which this value belongs'''
    ...
    def value (self, *args, **kwargs):
      '''value of this tile or voxel'''
    ...

def Vec3d (*args):
      '''

'''      
    ...

class Vec3d:

def Vec3f (*args):
      '''

'''      
    ...

class Vec3f:

def Vec3i (*args):
      '''

'''      
    ...

class Vec3i:

def Vec4d (*args):
      '''

'''      
    ...

class Vec4d:

def Vec4f (*args):
      '''

'''      
    ...

class Vec4f:

def Vec4i (*args):
      '''

'''      
    ...

class Vec4i:

def VectorType (*args):
      '''

'''      
    ...

class VectorType:
    def CONTRAVARIANT_ABSOLUTE (self, *args, **kwargs):
      '''str(object='') -> str
str(bytes_or_buffer[, encoding[, errors]]) -> str

Create a new string object from the given object. If encoding or
errors is specified, then the object must expose a data buffer
that will be decoded using the given encoding and error handler.
Otherwise, returns the result of object.__str__() (if defined)
or repr(object).
encoding defaults to sys.getdefaultencoding().
errors defaults to 'strict'.'''
    ...
    def CONTRAVARIANT_RELATIVE (self, *args, **kwargs):
      '''str(object='') -> str
str(bytes_or_buffer[, encoding[, errors]]) -> str

Create a new string object from the given object. If encoding or
errors is specified, then the object must expose a data buffer
that will be decoded using the given encoding and error handler.
Otherwise, returns the result of object.__str__() (if defined)
or repr(object).
encoding defaults to sys.getdefaultencoding().
errors defaults to 'strict'.'''
    ...
    def COVARIANT (self, *args, **kwargs):
      '''str(object='') -> str
str(bytes_or_buffer[, encoding[, errors]]) -> str

Create a new string object from the given object. If encoding or
errors is specified, then the object must expose a data buffer
that will be decoded using the given encoding and error handler.
Otherwise, returns the result of object.__str__() (if defined)
or repr(object).
encoding defaults to sys.getdefaultencoding().
errors defaults to 'strict'.'''
    ...
    def COVARIANT_NORMALIZE (self, *args, **kwargs):
      '''str(object='') -> str
str(bytes_or_buffer[, encoding[, errors]]) -> str

Create a new string object from the given object. If encoding or
errors is specified, then the object must expose a data buffer
that will be decoded using the given encoding and error handler.
Otherwise, returns the result of object.__str__() (if defined)
or repr(object).
encoding defaults to sys.getdefaultencoding().
errors defaults to 'strict'.'''
    ...
    def INVARIANT (self, *args, **kwargs):
      '''str(object='') -> str
str(bytes_or_buffer[, encoding[, errors]]) -> str

Create a new string object from the given object. If encoding or
errors is specified, then the object must expose a data buffer
that will be decoded using the given encoding and error handler.
Otherwise, returns the result of object.__str__() (if defined)
or repr(object).
encoding defaults to sys.getdefaultencoding().
errors defaults to 'strict'.'''
    ...
    def keys (self, *args, **kwargs):
      '''keys() -> list'''
    ...

def X (*args):
      '''

'''      
    ...

def Y (*args):
      '''

'''      
    ...

def Z (*args):
      '''

'''      
    ...

def __doc__ (*args):
      '''

'''      
    ...

def __file__ (*args):
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

def createFrustumTransform (*args):
      '''

'''      
    ...

def createLevelSetSphere (*args):
      '''

'''      
    ...

def createLinearTransform (*args):
      '''

'''      
    ...

def getLoggingLevel (*args):
      '''

'''      
    ...

def read (*args):
      '''

'''      
    ...

def readAll (*args):
      '''

'''      
    ...

def readAllGridMetadata (*args):
      '''

'''      
    ...

def readGridMetadata (*args):
      '''

'''      
    ...

def readMetadata (*args):
      '''

'''      
    ...

def setLoggingLevel (*args):
      '''

'''      
    ...

def setProgramName (*args):
      '''

'''      
    ...

def write (*args):
      '''

'''      
    ...
