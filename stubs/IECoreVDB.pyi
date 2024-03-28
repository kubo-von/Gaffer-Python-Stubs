
def VDBObject (*args):
      '''
__init__(_object*)
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)

'''      
    ...

class VDBObject:
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
    def blindData (self, *args, **kwargs):
      '''
blindData( (BlindDataHolder)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::CompoundData> blindData(IECore::BlindDataHolder {lvalue})'''
    ...
    def bound (self, *args, **kwargs):
      '''
bound( (VisibleRenderable)arg1) -> Box3f :

    C++ signature :
        Imath_3_1::Box<Imath_3_1::Vec3<float> > bound(IECoreScene::VisibleRenderable {lvalue})'''
    ...
    def collectGarbage (self, *args, **kwargs):
      '''
collectGarbage() -> None :

    C++ signature :
        void collectGarbage()'''
    ...
    def copy (self, *args, **kwargs):
      '''
copy( (Object)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::Object> copy(IECore::Object {lvalue})'''
    ...
    def copyFrom (self, *args, **kwargs):
      '''
copyFrom( (Object)arg1, (Object)arg2) -> None :

    C++ signature :
        void copyFrom(IECore::Object {lvalue},IECore::Object const*)'''
    ...
    def create (self, *args, **kwargs):
      '''
create( (object)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::Object> create(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)

create( (TypeId)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::Object> create(IECore::TypeId)'''
    ...
    def derivedTypeIds (self, *args, **kwargs):
      '''
derivedTypeIds( (TypeId)arg1) -> list :

    C++ signature :
        boost::python::list derivedTypeIds(IECore::TypeId)'''
    ...
    def fileName (self, *args, **kwargs):
      '''
fileName( (VDBObject)arg1) -> str :

    C++ signature :
        std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > fileName(IECoreVDB::VDBObject {lvalue})'''
    ...
    def findGrid (self, *args, **kwargs):
      '''
findGrid( (VDBObject)arg1, (object)arg2) -> object :

    C++ signature :
        std::shared_ptr<openvdb::v10_1::GridBase> findGrid(IECoreVDB::VDBObject {lvalue},std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)'''
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
    def gridNames (self, *args, **kwargs):
      '''
gridNames( (object)arg1) -> list :

    C++ signature :
        boost::python::list gridNames(boost::intrusive_ptr<IECoreVDB::VDBObject>)'''
    ...
    def hash (self, *args, **kwargs):
      '''
hash( (Object)arg1) -> MurmurHash :

    C++ signature :
        IECore::MurmurHash hash(IECore::Object {lvalue})

hash( (Object)arg1, (MurmurHash)arg2) -> None :

    C++ signature :
        void hash(IECore::Object {lvalue},IECore::MurmurHash {lvalue})'''
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
    def insertGrid (self, *args, **kwargs):
      '''
insertGrid( (VDBObject)arg1, (object)arg2) -> None :

    C++ signature :
        void insertGrid(IECoreVDB::VDBObject {lvalue},std::shared_ptr<openvdb::v10_1::GridBase>)'''
    ...
    def isAbstractType (self, *args, **kwargs):
      '''
isAbstractType( (object)arg1) -> bool :

    C++ signature :
        bool isAbstractType(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)

isAbstractType( (TypeId)arg1) -> bool :

    C++ signature :
        bool isAbstractType(IECore::TypeId)'''
    ...
    def isInstanceOf (self, *args, **kwargs):
      '''
isInstanceOf( (VDBObject)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreVDB::VDBObject {lvalue},IECore::TypeId)

isInstanceOf( (VDBObject)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreVDB::VDBObject {lvalue},char const*)'''
    ...
    def isSame (self, *args, **kwargs):
      '''
isSame( (RefCounted)arg1, (RefCounted)arg2) -> bool :

    C++ signature :
        bool isSame(IECore::RefCounted const*,IECore::RefCounted const*)'''
    ...
    def isType (self, *args, **kwargs):
      '''
isType( (object)arg1) -> bool :

    C++ signature :
        bool isType(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)

isType( (TypeId)arg1) -> bool :

    C++ signature :
        bool isType(IECore::TypeId)'''
    ...
    def load (self, *args, **kwargs):
      '''
load( (object)ioInterface, (InternedString)name [, (Canceller)canceller=None]) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::Object> load(boost::intrusive_ptr<IECore::IndexedIO const>,IECore::InternedString [,IECore::Canceller const*=None])'''
    ...
    def memoryUsage (self, *args, **kwargs):
      '''
memoryUsage( (Object)arg1) -> int :
    Returns the number of bytes this instance occupies in memory

    C++ signature :
        unsigned long memoryUsage(IECore::Object {lvalue})'''
    ...
    def metadata (self, *args, **kwargs):
      '''
metadata( (VDBObject)arg1, (object)arg2) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::CompoundObject> metadata(IECoreVDB::VDBObject {lvalue},std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)'''
    ...
    def numWrappedInstances (self, *args, **kwargs):
      '''
numWrappedInstances() -> int :

    C++ signature :
        unsigned long numWrappedInstances()'''
    ...
    def refCount (self, *args, **kwargs):
      '''
refCount( (RefCounted)arg1) -> int :

    C++ signature :
        unsigned long refCount(IECore::RefCounted {lvalue})'''
    ...
    def registerType (self, *args, **kwargs):
      '''
registerType( (TypeId)typeId, (object)typeName [, (object)creator=None]) -> None :

    C++ signature :
        void registerType(IECore::TypeId,std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > [,boost::python::api::object=None])'''
    ...
    def removeGrid (self, *args, **kwargs):
      '''
removeGrid( (VDBObject)arg1, (object)arg2) -> None :

    C++ signature :
        void removeGrid(IECoreVDB::VDBObject {lvalue},std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)'''
    ...
    def render (self, *args, **kwargs):
      '''
render( (Renderable)arg1, (Renderer)arg2) -> None :

    C++ signature :
        void render(IECoreScene::Renderable,IECoreScene::Renderer*)'''
    ...
    def save (self, *args, **kwargs):
      '''
save( (Object)arg1, (object)arg2, (InternedString)arg3) -> None :

    C++ signature :
        void save(IECore::Object {lvalue},boost::intrusive_ptr<IECore::IndexedIO>,IECore::InternedString)'''
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
    def typeId (self, *args, **kwargs):
      '''
typeId( (VDBObject)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreVDB::VDBObject {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (VDBObject)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreVDB::VDBObject {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...
    def unmodifiedFromFile (self, *args, **kwargs):
      '''
unmodifiedFromFile( (VDBObject)arg1) -> bool :

    C++ signature :
        bool unmodifiedFromFile(IECoreVDB::VDBObject {lvalue})'''
    ...

def _IECoreVDB (*args):
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

def pyopenvdb (*args):
      '''

'''      
    ...

def warnings (*args):
      '''

'''      
    ...
