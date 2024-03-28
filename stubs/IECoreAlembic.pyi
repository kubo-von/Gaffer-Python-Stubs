
def AlembicScene (*args):
      '''
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, unsigned int)

'''      
    ...

class AlembicScene:
    def AncestorTag (self, *args, **kwargs):
      '''None'''
    ...
    def AttributesHash (self, *args, **kwargs):
      '''None'''
    ...
    def BoundHash (self, *args, **kwargs):
      '''None'''
    ...
    def ChildNamesHash (self, *args, **kwargs):
      '''None'''
    ...
    def CreateIfMissing (self, *args, **kwargs):
      '''None'''
    ...
    def DescendantTag (self, *args, **kwargs):
      '''None'''
    ...
    def EveryTag (self, *args, **kwargs):
      '''None'''
    ...
    def HashType (self, *args, **kwargs):
      '''None'''
    ...
    def HierarchyHash (self, *args, **kwargs):
      '''None'''
    ...
    def LocalTag (self, *args, **kwargs):
      '''None'''
    ...
    def MissingBehaviour (self, *args, **kwargs):
      '''None'''
    ...
    def NullIfMissing (self, *args, **kwargs):
      '''None'''
    ...
    def ObjectHash (self, *args, **kwargs):
      '''None'''
    ...
    def TagFilter (self, *args, **kwargs):
      '''None'''
    ...
    def ThrowIfMissing (self, *args, **kwargs):
      '''None'''
    ...
    def TransformHash (self, *args, **kwargs):
      '''None'''
    ...
    def attributeNames (self, *args, **kwargs):
      '''
attributeNames( (SceneInterface)arg1) -> list :

    C++ signature :
        boost::python::list attributeNames(IECoreScene::SceneInterface)'''
    ...
    def attributeSampleInterval (self, *args, **kwargs):
      '''
attributeSampleInterval( (SampledSceneInterface)arg1, (InternedString)arg2, (float)arg3) -> tuple :

    C++ signature :
        boost::python::tuple attributeSampleInterval(IECoreScene::SampledSceneInterface,IECore::InternedString,double)'''
    ...
    def attributeSampleTime (self, *args, **kwargs):
      '''
attributeSampleTime( (SampledSceneInterface)arg1, (InternedString)arg2, (int)arg3) -> float :

    C++ signature :
        double attributeSampleTime(IECoreScene::SampledSceneInterface {lvalue},IECore::InternedString,unsigned long)'''
    ...
    def baseTypeId (self, *args, **kwargs):
      '''
baseTypeId([  (TypeId)arg1]) -> TypeId :

    C++ signature :
        IECore::TypeId baseTypeId([ IECore::TypeId])'''
    ...
    def baseTypeIds (self, *args, **kwargs):
      '''
baseTypeIds( (TypeId)arg1) -> list :

    C++ signature :
        boost::python::list baseTypeIds(IECore::TypeId)'''
    ...
    def baseTypeName (self, *args, **kwargs):
      '''
baseTypeName() -> str :

    C++ signature :
        char const* baseTypeName()'''
    ...
    def boundSampleInterval (self, *args, **kwargs):
      '''
boundSampleInterval( (SampledSceneInterface)arg1, (float)arg2) -> tuple :

    C++ signature :
        boost::python::tuple boundSampleInterval(IECoreScene::SampledSceneInterface,double)'''
    ...
    def boundSampleTime (self, *args, **kwargs):
      '''
boundSampleTime( (SampledSceneInterface)arg1, (int)arg2) -> float :

    C++ signature :
        double boundSampleTime(IECoreScene::SampledSceneInterface {lvalue},unsigned long)'''
    ...
    def child (self, *args, **kwargs):
      '''
child( (SceneInterface)arg1, (InternedString)name [, (MissingBehaviour)missingBehaviour=IECoreScene._IECoreScene.MissingBehaviour.ThrowIfMissing]) -> object :

    C++ signature :
        boost::intrusive_ptr<IECoreScene::SceneInterface> child(IECoreScene::SceneInterface {lvalue},IECore::InternedString [,IECoreScene::SceneInterface::MissingBehaviour=IECoreScene._IECoreScene.MissingBehaviour.ThrowIfMissing])'''
    ...
    def childNames (self, *args, **kwargs):
      '''
childNames( (SceneInterface)arg1) -> list :

    C++ signature :
        boost::python::list childNames(IECoreScene::SceneInterface)'''
    ...
    def collectGarbage (self, *args, **kwargs):
      '''
collectGarbage() -> None :

    C++ signature :
        void collectGarbage()'''
    ...
    def create (self, *args, **kwargs):
      '''
create( (object)arg1, (int)arg2) -> object :

    C++ signature :
        boost::intrusive_ptr<IECoreScene::SceneInterface> create(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >,unsigned int)'''
    ...
    def createChild (self, *args, **kwargs):
      '''
createChild( (SceneInterface)arg1, (InternedString)arg2) -> object :

    C++ signature :
        boost::intrusive_ptr<IECoreScene::SceneInterface> createChild(IECoreScene::SceneInterface {lvalue},IECore::InternedString)'''
    ...
    def derivedTypeIds (self, *args, **kwargs):
      '''
derivedTypeIds( (TypeId)arg1) -> list :

    C++ signature :
        boost::python::list derivedTypeIds(IECore::TypeId)'''
    ...
    def fileName (self, *args, **kwargs):
      '''
fileName( (SceneInterface)arg1) -> str :

    C++ signature :
        std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > fileName(IECoreScene::SceneInterface {lvalue})'''
    ...
    def garbageCollectionThreshold (self, *args, **kwargs):
      '''int([x]) -> integer
int(x, base=10) -> integer

Convert a number or string to an integer, or return 0 if no arguments
are given.  If x is a number, return x.__int__().  For floating point
numbers, this truncates towards zero.

If x is not a number or if base is given, then x must be a string,
bytes, or bytearray instance representing an integer literal in the
given base.  The literal can be preceded by '+' or '-' and be surrounded
by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
Base 0 means to interpret the base from the string as an integer literal.
>>> int('0b100', base=0)
4'''
    ...
    def hasAttribute (self, *args, **kwargs):
      '''
hasAttribute( (SceneInterface)arg1, (InternedString)arg2) -> bool :

    C++ signature :
        bool hasAttribute(IECoreScene::SceneInterface {lvalue},IECore::InternedString)'''
    ...
    def hasBound (self, *args, **kwargs):
      '''
hasBound( (SceneInterface)arg1) -> bool :

    C++ signature :
        bool hasBound(IECoreScene::SceneInterface {lvalue})'''
    ...
    def hasChild (self, *args, **kwargs):
      '''
hasChild( (SceneInterface)arg1, (InternedString)arg2) -> bool :

    C++ signature :
        bool hasChild(IECoreScene::SceneInterface {lvalue},IECore::InternedString)'''
    ...
    def hasObject (self, *args, **kwargs):
      '''
hasObject( (SceneInterface)arg1) -> bool :

    C++ signature :
        bool hasObject(IECoreScene::SceneInterface {lvalue})'''
    ...
    def hasTag (self, *args, **kwargs):
      '''
hasTag( (SceneInterface)arg1, (InternedString)name [, (int)filter=IECoreScene._IECoreScene.TagFilter.LocalTag]) -> bool :

    C++ signature :
        bool hasTag(IECoreScene::SceneInterface {lvalue},IECore::InternedString [,int=IECoreScene._IECoreScene.TagFilter.LocalTag])'''
    ...
    def hash (self, *args, **kwargs):
      '''
hash( (SceneInterface)arg1, (HashType)arg2, (float)arg3) -> MurmurHash :

    C++ signature :
        IECore::MurmurHash hash(IECoreScene::SceneInterface {lvalue},IECoreScene::SceneInterface::HashType,double)'''
    ...
    def hashSet (self, *args, **kwargs):
      '''
hashSet( (SceneInterface)arg1, (InternedString)arg2) -> MurmurHash :

    C++ signature :
        IECore::MurmurHash hashSet(IECoreScene::SceneInterface {lvalue},IECore::InternedString)'''
    ...
    def inheritsFrom (self, *args, **kwargs):
      '''
inheritsFrom( (str)arg1) -> bool :

    C++ signature :
        bool inheritsFrom(char const*)

inheritsFrom( (TypeId)arg1) -> bool :

    C++ signature :
        bool inheritsFrom(IECore::TypeId)

inheritsFrom( (str)arg1, (str)arg2) -> bool :

    C++ signature :
        bool inheritsFrom(char const*,char const*)

inheritsFrom( (TypeId)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool inheritsFrom(IECore::TypeId,IECore::TypeId)'''
    ...
    def isInstanceOf (self, *args, **kwargs):
      '''
isInstanceOf( (AlembicScene)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreAlembic::AlembicScene {lvalue},IECore::TypeId)

isInstanceOf( (AlembicScene)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreAlembic::AlembicScene {lvalue},char const*)'''
    ...
    def isSame (self, *args, **kwargs):
      '''
isSame( (RefCounted)arg1, (RefCounted)arg2) -> bool :

    C++ signature :
        bool isSame(IECore::RefCounted const*,IECore::RefCounted const*)'''
    ...
    def name (self, *args, **kwargs):
      '''
name( (SceneInterface)arg1) -> InternedString :

    C++ signature :
        IECore::InternedString name(IECoreScene::SceneInterface {lvalue})'''
    ...
    def numAttributeSamples (self, *args, **kwargs):
      '''
numAttributeSamples( (SampledSceneInterface)arg1, (InternedString)arg2) -> int :

    C++ signature :
        unsigned long numAttributeSamples(IECoreScene::SampledSceneInterface {lvalue},IECore::InternedString)'''
    ...
    def numBoundSamples (self, *args, **kwargs):
      '''
numBoundSamples( (SampledSceneInterface)arg1) -> int :

    C++ signature :
        unsigned long numBoundSamples(IECoreScene::SampledSceneInterface {lvalue})'''
    ...
    def numObjectSamples (self, *args, **kwargs):
      '''
numObjectSamples( (SampledSceneInterface)arg1) -> int :

    C++ signature :
        unsigned long numObjectSamples(IECoreScene::SampledSceneInterface {lvalue})'''
    ...
    def numTransformSamples (self, *args, **kwargs):
      '''
numTransformSamples( (SampledSceneInterface)arg1) -> int :

    C++ signature :
        unsigned long numTransformSamples(IECoreScene::SampledSceneInterface {lvalue})'''
    ...
    def numWrappedInstances (self, *args, **kwargs):
      '''
numWrappedInstances() -> int :

    C++ signature :
        unsigned long numWrappedInstances()'''
    ...
    def objectSampleInterval (self, *args, **kwargs):
      '''
objectSampleInterval( (SampledSceneInterface)arg1, (float)arg2) -> tuple :

    C++ signature :
        boost::python::tuple objectSampleInterval(IECoreScene::SampledSceneInterface,double)'''
    ...
    def objectSampleTime (self, *args, **kwargs):
      '''
objectSampleTime( (SampledSceneInterface)arg1, (int)arg2) -> float :

    C++ signature :
        double objectSampleTime(IECoreScene::SampledSceneInterface {lvalue},unsigned long)'''
    ...
    def path (self, *args, **kwargs):
      '''
path( (SceneInterface)arg1) -> list :

    C++ signature :
        boost::python::list path(IECoreScene::SceneInterface)'''
    ...
    def pathAsString (self, *args, **kwargs):
      '''
pathAsString( (SceneInterface)arg1) -> str :

    C++ signature :
        std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > pathAsString(IECoreScene::SceneInterface)'''
    ...
    def pathToString (self, *args, **kwargs):
      '''
pathToString( (list)arg1) -> str :

    C++ signature :
        std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > pathToString(boost::python::list)'''
    ...
    def readAttribute (self, *args, **kwargs):
      '''
readAttribute( (SceneInterface)arg1, (InternedString)name, (float)time [, (bool)_copy=True]) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::Object> readAttribute(IECoreScene::SceneInterface {lvalue},IECore::InternedString,double [,bool=True])'''
    ...
    def readAttributeAtSample (self, *args, **kwargs):
      '''
readAttributeAtSample( (SampledSceneInterface)arg1, (InternedString)arg2, (int)arg3) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::Object> readAttributeAtSample(IECoreScene::SampledSceneInterface {lvalue},IECore::InternedString,unsigned long)'''
    ...
    def readBound (self, *args, **kwargs):
      '''
readBound( (SceneInterface)arg1, (float)arg2) -> Box3d :

    C++ signature :
        Imath_3_1::Box<Imath_3_1::Vec3<double> > readBound(IECoreScene::SceneInterface {lvalue},double)'''
    ...
    def readBoundAtSample (self, *args, **kwargs):
      '''
readBoundAtSample( (SampledSceneInterface)arg1, (int)arg2) -> Box3d :

    C++ signature :
        Imath_3_1::Box<Imath_3_1::Vec3<double> > readBoundAtSample(IECoreScene::SampledSceneInterface {lvalue},unsigned long)'''
    ...
    def readObject (self, *args, **kwargs):
      '''
readObject( (SceneInterface)arg1, (float)time [, (Canceller)canceller=None [, (bool)_copy=True]]) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::Object> readObject(IECoreScene::SceneInterface {lvalue},double [,IECore::Canceller const*=None [,bool=True]])'''
    ...
    def readObjectAtSample (self, *args, **kwargs):
      '''
readObjectAtSample( (SampledSceneInterface)arg1, (int)arg2) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::Object> readObjectAtSample(IECoreScene::SampledSceneInterface {lvalue},unsigned long)'''
    ...
    def readObjectPrimitiveVariables (self, *args, **kwargs):
      '''
readObjectPrimitiveVariables( (SceneInterface)arg1, (list)arg2, (float)arg3) -> dict :

    C++ signature :
        boost::python::dict readObjectPrimitiveVariables(IECoreScene::SceneInterface,boost::python::list,double)'''
    ...
    def readSet (self, *args, **kwargs):
      '''
readSet( (SceneInterface)arg1, (InternedString)name [, (bool)includeDescendantSets=True [, (Canceller)canceller=None]]) -> PathMatcher :

    C++ signature :
        IECore::PathMatcher readSet(IECoreScene::SceneInterface {lvalue},IECore::InternedString [,bool=True [,IECore::Canceller const*=None]])'''
    ...
    def readTags (self, *args, **kwargs):
      '''
readTags( (SceneInterface)arg1 [, (int)filter=IECoreScene._IECoreScene.TagFilter.LocalTag]) -> list :

    C++ signature :
        boost::python::list readTags(IECoreScene::SceneInterface [,int=IECoreScene._IECoreScene.TagFilter.LocalTag])'''
    ...
    def readTransform (self, *args, **kwargs):
      '''
readTransform( (SceneInterface)arg1, (float)time [, (bool)_copy=True]) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::Data> readTransform(IECoreScene::SceneInterface {lvalue},double [,bool=True])'''
    ...
    def readTransformAsMatrix (self, *args, **kwargs):
      '''
readTransformAsMatrix( (SceneInterface)arg1, (float)arg2) -> M44d :

    C++ signature :
        Imath_3_1::Matrix44<double> readTransformAsMatrix(IECoreScene::SceneInterface {lvalue},double)'''
    ...
    def readTransformAsMatrixAtSample (self, *args, **kwargs):
      '''
readTransformAsMatrixAtSample( (SampledSceneInterface)arg1, (int)arg2) -> M44d :

    C++ signature :
        Imath_3_1::Matrix44<double> readTransformAsMatrixAtSample(IECoreScene::SampledSceneInterface {lvalue},unsigned long)'''
    ...
    def readTransformAtSample (self, *args, **kwargs):
      '''
readTransformAtSample( (SampledSceneInterface)arg1, (int)arg2) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::Data> readTransformAtSample(IECoreScene::SampledSceneInterface {lvalue},unsigned long)'''
    ...
    def refCount (self, *args, **kwargs):
      '''
refCount( (RefCounted)arg1) -> int :

    C++ signature :
        unsigned long refCount(IECore::RefCounted {lvalue})'''
    ...
    def registerType (self, *args, **kwargs):
      '''
registerType( (TypeId)arg1, (str)arg2, (TypeId)arg3) -> None :

    C++ signature :
        void registerType(IECore::TypeId,char const*,IECore::TypeId)'''
    ...
    def scene (self, *args, **kwargs):
      '''
scene( (SceneInterface)arg1, (list)path [, (MissingBehaviour)missingBehaviour=IECoreScene._IECoreScene.MissingBehaviour.ThrowIfMissing]) -> object :

    C++ signature :
        boost::intrusive_ptr<IECoreScene::SceneInterface> scene(IECoreScene::SceneInterface {lvalue},boost::python::list [,IECoreScene::SceneInterface::MissingBehaviour=IECoreScene._IECoreScene.MissingBehaviour.ThrowIfMissing])'''
    ...
    def setNames (self, *args, **kwargs):
      '''
setNames( (SceneInterface)arg1 [, (bool)includeDescendantSets=True]) -> list :

    C++ signature :
        boost::python::list setNames(IECoreScene::SceneInterface [,bool=True])'''
    ...
    def staticTypeId (self, *args, **kwargs):
      '''
staticTypeId() -> TypeId :

    C++ signature :
        IECore::TypeId staticTypeId()'''
    ...
    def staticTypeName (self, *args, **kwargs):
      '''
staticTypeName() -> str :

    C++ signature :
        char const* staticTypeName()'''
    ...
    def stringToPath (self, *args, **kwargs):
      '''
stringToPath( (object)arg1) -> list :

    C++ signature :
        boost::python::list stringToPath(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)'''
    ...
    def supportedExtensions (self, *args, **kwargs):
      '''
supportedExtensions([  (int)modes=7]) -> list :

    C++ signature :
        boost::python::list supportedExtensions([ unsigned int=7])'''
    ...
    def transformSampleInterval (self, *args, **kwargs):
      '''
transformSampleInterval( (SampledSceneInterface)arg1, (float)arg2) -> tuple :

    C++ signature :
        boost::python::tuple transformSampleInterval(IECoreScene::SampledSceneInterface,double)'''
    ...
    def transformSampleTime (self, *args, **kwargs):
      '''
transformSampleTime( (SampledSceneInterface)arg1, (int)arg2) -> float :

    C++ signature :
        double transformSampleTime(IECoreScene::SampledSceneInterface {lvalue},unsigned long)'''
    ...
    def typeId (self, *args, **kwargs):
      '''
typeId( (AlembicScene)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreAlembic::AlembicScene {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (AlembicScene)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreAlembic::AlembicScene {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...
    def visibilityName (self, *args, **kwargs):
      '''None'''
    ...
    def writeAttribute (self, *args, **kwargs):
      '''
writeAttribute( (SceneInterface)arg1, (InternedString)arg2, (Object)arg3, (float)arg4) -> None :

    C++ signature :
        void writeAttribute(IECoreScene::SceneInterface {lvalue},IECore::InternedString,IECore::Object const*,double)'''
    ...
    def writeBound (self, *args, **kwargs):
      '''
writeBound( (SceneInterface)arg1, (Box3d)arg2, (float)arg3) -> None :

    C++ signature :
        void writeBound(IECoreScene::SceneInterface {lvalue},Imath_3_1::Box<Imath_3_1::Vec3<double> >,double)'''
    ...
    def writeObject (self, *args, **kwargs):
      '''
writeObject( (SceneInterface)arg1, (Object)arg2, (float)arg3) -> None :

    C++ signature :
        void writeObject(IECoreScene::SceneInterface {lvalue},IECore::Object const*,double)'''
    ...
    def writeSet (self, *args, **kwargs):
      '''
writeSet( (SceneInterface)arg1, (InternedString)arg2, (PathMatcher)arg3) -> None :

    C++ signature :
        void writeSet(IECoreScene::SceneInterface {lvalue},IECore::InternedString,IECore::PathMatcher)'''
    ...
    def writeTags (self, *args, **kwargs):
      '''
writeTags( (SceneInterface)arg1, (list)arg2) -> None :

    C++ signature :
        void writeTags(IECoreScene::SceneInterface {lvalue},boost::python::list)'''
    ...
    def writeTransform (self, *args, **kwargs):
      '''
writeTransform( (SceneInterface)arg1, (Data)arg2, (float)arg3) -> None :

    C++ signature :
        void writeTransform(IECoreScene::SceneInterface {lvalue},IECore::Data const*,double)'''
    ...

def _IECoreAlembic (*args):
      '''

'''      
    ...

def __builtins__ (*args):
      '''

'''      
    ...

def __cached__ (*args):
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

def __path__ (*args):
      '''

'''      
    ...

def __spec__ (*args):
      '''

'''      
    ...
