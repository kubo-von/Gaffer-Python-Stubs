
def ChannelOp (*args):
      '''

'''      
    ...

class ChannelOp:
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
    def collectGarbage (self, *args, **kwargs):
      '''
collectGarbage() -> None :

    C++ signature :
        void collectGarbage()'''
    ...
    def derivedTypeIds (self, *args, **kwargs):
      '''
derivedTypeIds( (TypeId)arg1) -> list :

    C++ signature :
        boost::python::list derivedTypeIds(IECore::TypeId)'''
    ...
    def description (self, *args, **kwargs):
      '''None'''
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
isInstanceOf( (ChannelOp)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreImage::ChannelOp {lvalue},IECore::TypeId)

isInstanceOf( (ChannelOp)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreImage::ChannelOp {lvalue},char const*)'''
    ...
    def isSame (self, *args, **kwargs):
      '''
isSame( (RefCounted)arg1, (RefCounted)arg2) -> bool :

    C++ signature :
        bool isSame(IECore::RefCounted const*,IECore::RefCounted const*)'''
    ...
    def numWrappedInstances (self, *args, **kwargs):
      '''
numWrappedInstances() -> int :

    C++ signature :
        unsigned long numWrappedInstances()'''
    ...
    def operate (self, *args, **kwargs):
      '''
operate( (Op)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::Object> operate(IECore::Op {lvalue})

operate( (Op)arg1, (CompoundObject)arg2) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::Object> operate(IECore::Op {lvalue},IECore::CompoundObject const*)'''
    ...
    def parameters (self, *args, **kwargs):
      '''
parameters( (Parameterised)arg1) -> object :

    C++ signature :
        IECore::CompoundParameter* parameters(IECore::Parameterised {lvalue})'''
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
    def resultParameter (self, *args, **kwargs):
      '''
resultParameter( (Op)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::Parameter> resultParameter(IECore::Op)'''
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
typeId( (ChannelOp)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreImage::ChannelOp {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (ChannelOp)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreImage::ChannelOp {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...
    def userData (self, *args, **kwargs):
      '''
userData( (Parameterised)arg1) -> object :

    C++ signature :
        IECore::CompoundObject* userData(IECore::Parameterised {lvalue})'''
    ...

def ClampOp (*args):
      '''
__init__(_object*)

'''      
    ...

class ClampOp:
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
    def collectGarbage (self, *args, **kwargs):
      '''
collectGarbage() -> None :

    C++ signature :
        void collectGarbage()'''
    ...
    def derivedTypeIds (self, *args, **kwargs):
      '''
derivedTypeIds( (TypeId)arg1) -> list :

    C++ signature :
        boost::python::list derivedTypeIds(IECore::TypeId)'''
    ...
    def description (self, *args, **kwargs):
      '''None'''
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
isInstanceOf( (ClampOp)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreImage::ClampOp {lvalue},IECore::TypeId)

isInstanceOf( (ClampOp)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreImage::ClampOp {lvalue},char const*)'''
    ...
    def isSame (self, *args, **kwargs):
      '''
isSame( (RefCounted)arg1, (RefCounted)arg2) -> bool :

    C++ signature :
        bool isSame(IECore::RefCounted const*,IECore::RefCounted const*)'''
    ...
    def numWrappedInstances (self, *args, **kwargs):
      '''
numWrappedInstances() -> int :

    C++ signature :
        unsigned long numWrappedInstances()'''
    ...
    def operate (self, *args, **kwargs):
      '''
operate( (Op)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::Object> operate(IECore::Op {lvalue})

operate( (Op)arg1, (CompoundObject)arg2) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::Object> operate(IECore::Op {lvalue},IECore::CompoundObject const*)'''
    ...
    def parameters (self, *args, **kwargs):
      '''
parameters( (Parameterised)arg1) -> object :

    C++ signature :
        IECore::CompoundParameter* parameters(IECore::Parameterised {lvalue})'''
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
    def resultParameter (self, *args, **kwargs):
      '''
resultParameter( (Op)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::Parameter> resultParameter(IECore::Op)'''
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
typeId( (ClampOp)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreImage::ClampOp {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (ClampOp)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreImage::ClampOp {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...
    def userData (self, *args, **kwargs):
      '''
userData( (Parameterised)arg1) -> object :

    C++ signature :
        IECore::CompoundObject* userData(IECore::Parameterised {lvalue})'''
    ...

def ClientDisplayDriver (*args):
      '''
__init__(boost::python::api::object, Imath_3_1::Box<Imath_3_1::Vec2<int> > displayWindow, Imath_3_1::Box<Imath_3_1::Vec2<int> > dataWindow, boost::python::list channelNames, boost::intrusive_ptr<IECore::CompoundData> parameters)

'''      
    ...

class ClientDisplayDriver:
    def acceptsRepeatedData (self, *args, **kwargs):
      '''
acceptsRepeatedData( (DisplayDriver)arg1) -> bool :

    C++ signature :
        bool acceptsRepeatedData(IECoreImage::DisplayDriver {lvalue})'''
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
    def channelNames (self, *args, **kwargs):
      '''
channelNames( (object)arg1) -> list :

    C++ signature :
        boost::python::list channelNames(boost::intrusive_ptr<IECoreImage::DisplayDriver>)'''
    ...
    def collectGarbage (self, *args, **kwargs):
      '''
collectGarbage() -> None :

    C++ signature :
        void collectGarbage()'''
    ...
    def create (self, *args, **kwargs):
      '''
create( (object)arg1, (Box2i)arg2, (Box2i)arg3, (list)arg4, (object)arg5) -> object :

    C++ signature :
        boost::intrusive_ptr<IECoreImage::DisplayDriver> create(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >,Imath_3_1::Box<Imath_3_1::Vec2<int> >,Imath_3_1::Box<Imath_3_1::Vec2<int> >,boost::python::list,boost::intrusive_ptr<IECore::CompoundData>)'''
    ...
    def dataWindow (self, *args, **kwargs):
      '''
dataWindow( (DisplayDriver)arg1) -> Box2i :

    C++ signature :
        Imath_3_1::Box<Imath_3_1::Vec2<int> > dataWindow(IECoreImage::DisplayDriver {lvalue})'''
    ...
    def derivedTypeIds (self, *args, **kwargs):
      '''
derivedTypeIds( (TypeId)arg1) -> list :

    C++ signature :
        boost::python::list derivedTypeIds(IECore::TypeId)'''
    ...
    def displayWindow (self, *args, **kwargs):
      '''
displayWindow( (DisplayDriver)arg1) -> Box2i :

    C++ signature :
        Imath_3_1::Box<Imath_3_1::Vec2<int> > displayWindow(IECoreImage::DisplayDriver {lvalue})'''
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
    def host (self, *args, **kwargs):
      '''
host( (ClientDisplayDriver)arg1) -> str :

    C++ signature :
        std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > host(IECoreImage::ClientDisplayDriver {lvalue})'''
    ...
    def imageClose (self, *args, **kwargs):
      '''
imageClose( (object)arg1) -> None :

    C++ signature :
        void imageClose(boost::intrusive_ptr<IECoreImage::DisplayDriver>)'''
    ...
    def imageData (self, *args, **kwargs):
      '''
imageData( (object)arg1, (Box2i)arg2, (object)arg3) -> None :

    C++ signature :
        void imageData(boost::intrusive_ptr<IECoreImage::DisplayDriver>,Imath_3_1::Box<Imath_3_1::Vec2<int> >,boost::intrusive_ptr<IECore::TypedData<std::vector<float, std::allocator<float> > > >)'''
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
isInstanceOf( (ClientDisplayDriver)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreImage::ClientDisplayDriver {lvalue},IECore::TypeId)

isInstanceOf( (ClientDisplayDriver)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreImage::ClientDisplayDriver {lvalue},char const*)'''
    ...
    def isSame (self, *args, **kwargs):
      '''
isSame( (RefCounted)arg1, (RefCounted)arg2) -> bool :

    C++ signature :
        bool isSame(IECore::RefCounted const*,IECore::RefCounted const*)'''
    ...
    def numWrappedInstances (self, *args, **kwargs):
      '''
numWrappedInstances() -> int :

    C++ signature :
        unsigned long numWrappedInstances()'''
    ...
    def port (self, *args, **kwargs):
      '''
port( (ClientDisplayDriver)arg1) -> str :

    C++ signature :
        std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > port(IECoreImage::ClientDisplayDriver {lvalue})'''
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
    def scanLineOrderOnly (self, *args, **kwargs):
      '''
scanLineOrderOnly( (object)arg1) -> bool :

    C++ signature :
        bool scanLineOrderOnly(boost::intrusive_ptr<IECoreImage::DisplayDriver>)'''
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
typeId( (ClientDisplayDriver)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreImage::ClientDisplayDriver {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (ClientDisplayDriver)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreImage::ClientDisplayDriver {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...

def ColorAlgo (*args):
      '''

'''      
    ...

def DisplayDriver (*args):
      '''

'''      
    ...

class DisplayDriver:
    def acceptsRepeatedData (self, *args, **kwargs):
      '''
acceptsRepeatedData( (DisplayDriver)arg1) -> bool :

    C++ signature :
        bool acceptsRepeatedData(IECoreImage::DisplayDriver {lvalue})'''
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
    def channelNames (self, *args, **kwargs):
      '''
channelNames( (object)arg1) -> list :

    C++ signature :
        boost::python::list channelNames(boost::intrusive_ptr<IECoreImage::DisplayDriver>)'''
    ...
    def collectGarbage (self, *args, **kwargs):
      '''
collectGarbage() -> None :

    C++ signature :
        void collectGarbage()'''
    ...
    def create (self, *args, **kwargs):
      '''
create( (object)arg1, (Box2i)arg2, (Box2i)arg3, (list)arg4, (object)arg5) -> object :

    C++ signature :
        boost::intrusive_ptr<IECoreImage::DisplayDriver> create(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >,Imath_3_1::Box<Imath_3_1::Vec2<int> >,Imath_3_1::Box<Imath_3_1::Vec2<int> >,boost::python::list,boost::intrusive_ptr<IECore::CompoundData>)'''
    ...
    def dataWindow (self, *args, **kwargs):
      '''
dataWindow( (DisplayDriver)arg1) -> Box2i :

    C++ signature :
        Imath_3_1::Box<Imath_3_1::Vec2<int> > dataWindow(IECoreImage::DisplayDriver {lvalue})'''
    ...
    def derivedTypeIds (self, *args, **kwargs):
      '''
derivedTypeIds( (TypeId)arg1) -> list :

    C++ signature :
        boost::python::list derivedTypeIds(IECore::TypeId)'''
    ...
    def displayWindow (self, *args, **kwargs):
      '''
displayWindow( (DisplayDriver)arg1) -> Box2i :

    C++ signature :
        Imath_3_1::Box<Imath_3_1::Vec2<int> > displayWindow(IECoreImage::DisplayDriver {lvalue})'''
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
    def imageClose (self, *args, **kwargs):
      '''
imageClose( (object)arg1) -> None :

    C++ signature :
        void imageClose(boost::intrusive_ptr<IECoreImage::DisplayDriver>)'''
    ...
    def imageData (self, *args, **kwargs):
      '''
imageData( (object)arg1, (Box2i)arg2, (object)arg3) -> None :

    C++ signature :
        void imageData(boost::intrusive_ptr<IECoreImage::DisplayDriver>,Imath_3_1::Box<Imath_3_1::Vec2<int> >,boost::intrusive_ptr<IECore::TypedData<std::vector<float, std::allocator<float> > > >)'''
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
isInstanceOf( (DisplayDriver)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreImage::DisplayDriver {lvalue},IECore::TypeId)

isInstanceOf( (DisplayDriver)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreImage::DisplayDriver {lvalue},char const*)'''
    ...
    def isSame (self, *args, **kwargs):
      '''
isSame( (RefCounted)arg1, (RefCounted)arg2) -> bool :

    C++ signature :
        bool isSame(IECore::RefCounted const*,IECore::RefCounted const*)'''
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
registerType( (TypeId)arg1, (str)arg2, (TypeId)arg3) -> None :

    C++ signature :
        void registerType(IECore::TypeId,char const*,IECore::TypeId)'''
    ...
    def scanLineOrderOnly (self, *args, **kwargs):
      '''
scanLineOrderOnly( (object)arg1) -> bool :

    C++ signature :
        bool scanLineOrderOnly(boost::intrusive_ptr<IECoreImage::DisplayDriver>)'''
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
typeId( (DisplayDriver)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreImage::DisplayDriver {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (DisplayDriver)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreImage::DisplayDriver {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...

def DisplayDriverServer (*args):
      '''
__init__(_object*, unsigned short portNumber=0)

'''      
    ...

class DisplayDriverServer:
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
    def collectGarbage (self, *args, **kwargs):
      '''
collectGarbage() -> None :

    C++ signature :
        void collectGarbage()'''
    ...
    def deregisterPortRange (self, *args, **kwargs):
      '''
deregisterPortRange( (object)arg1) -> None :

    C++ signature :
        void deregisterPortRange(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)'''
    ...
    def derivedTypeIds (self, *args, **kwargs):
      '''
derivedTypeIds( (TypeId)arg1) -> list :

    C++ signature :
        boost::python::list derivedTypeIds(IECore::TypeId)'''
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
    def getPortRange (self, *args, **kwargs):
      '''
getPortRange() -> tuple :

    C++ signature :
        boost::python::tuple getPortRange()'''
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
isInstanceOf( (DisplayDriverServer)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreImage::DisplayDriverServer {lvalue},IECore::TypeId)

isInstanceOf( (DisplayDriverServer)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreImage::DisplayDriverServer {lvalue},char const*)'''
    ...
    def isSame (self, *args, **kwargs):
      '''
isSame( (RefCounted)arg1, (RefCounted)arg2) -> bool :

    C++ signature :
        bool isSame(IECore::RefCounted const*,IECore::RefCounted const*)'''
    ...
    def numWrappedInstances (self, *args, **kwargs):
      '''
numWrappedInstances() -> int :

    C++ signature :
        unsigned long numWrappedInstances()'''
    ...
    def portNumber (self, *args, **kwargs):
      '''
portNumber( (DisplayDriverServer)arg1) -> int :

    C++ signature :
        unsigned short portNumber(IECoreImage::DisplayDriverServer {lvalue})'''
    ...
    def refCount (self, *args, **kwargs):
      '''
refCount( (RefCounted)arg1) -> int :

    C++ signature :
        unsigned long refCount(IECore::RefCounted {lvalue})'''
    ...
    def registerPortRange (self, *args, **kwargs):
      '''
registerPortRange( (object)arg1, (tuple)arg2) -> None :

    C++ signature :
        void registerPortRange(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >,boost::python::tuple)'''
    ...
    def registerType (self, *args, **kwargs):
      '''
registerType( (TypeId)arg1, (str)arg2, (TypeId)arg3) -> None :

    C++ signature :
        void registerType(IECore::TypeId,char const*,IECore::TypeId)'''
    ...
    def registeredPortRange (self, *args, **kwargs):
      '''
registeredPortRange( (object)arg1) -> tuple :

    C++ signature :
        boost::python::tuple registeredPortRange(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)'''
    ...
    def setPortRange (self, *args, **kwargs):
      '''
setPortRange( (tuple)arg1) -> None :

    C++ signature :
        void setPortRange(boost::python::tuple)'''
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
typeId( (DisplayDriverServer)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreImage::DisplayDriverServer {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (DisplayDriverServer)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreImage::DisplayDriverServer {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...

def EnvMapSampler (*args):
      '''
__init__(_object*)

'''      
    ...

class EnvMapSampler:
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
    def collectGarbage (self, *args, **kwargs):
      '''
collectGarbage() -> None :

    C++ signature :
        void collectGarbage()'''
    ...
    def derivedTypeIds (self, *args, **kwargs):
      '''
derivedTypeIds( (TypeId)arg1) -> list :

    C++ signature :
        boost::python::list derivedTypeIds(IECore::TypeId)'''
    ...
    def description (self, *args, **kwargs):
      '''None'''
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
isInstanceOf( (EnvMapSampler)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreImage::EnvMapSampler {lvalue},IECore::TypeId)

isInstanceOf( (EnvMapSampler)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreImage::EnvMapSampler {lvalue},char const*)'''
    ...
    def isSame (self, *args, **kwargs):
      '''
isSame( (RefCounted)arg1, (RefCounted)arg2) -> bool :

    C++ signature :
        bool isSame(IECore::RefCounted const*,IECore::RefCounted const*)'''
    ...
    def numWrappedInstances (self, *args, **kwargs):
      '''
numWrappedInstances() -> int :

    C++ signature :
        unsigned long numWrappedInstances()'''
    ...
    def operate (self, *args, **kwargs):
      '''
operate( (Op)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::Object> operate(IECore::Op {lvalue})

operate( (Op)arg1, (CompoundObject)arg2) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::Object> operate(IECore::Op {lvalue},IECore::CompoundObject const*)'''
    ...
    def parameters (self, *args, **kwargs):
      '''
parameters( (Parameterised)arg1) -> object :

    C++ signature :
        IECore::CompoundParameter* parameters(IECore::Parameterised {lvalue})'''
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
    def resultParameter (self, *args, **kwargs):
      '''
resultParameter( (Op)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::Parameter> resultParameter(IECore::Op)'''
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
typeId( (EnvMapSampler)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreImage::EnvMapSampler {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (EnvMapSampler)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreImage::EnvMapSampler {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...
    def userData (self, *args, **kwargs):
      '''
userData( (Parameterised)arg1) -> object :

    C++ signature :
        IECore::CompoundObject* userData(IECore::Parameterised {lvalue})'''
    ...

def Font (*args):
      '''
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)

'''      
    ...

class Font:
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
    def collectGarbage (self, *args, **kwargs):
      '''
collectGarbage() -> None :

    C++ signature :
        void collectGarbage()'''
    ...
    def derivedTypeIds (self, *args, **kwargs):
      '''
derivedTypeIds( (TypeId)arg1) -> list :

    C++ signature :
        boost::python::list derivedTypeIds(IECore::TypeId)'''
    ...
    def fileName (self, *args, **kwargs):
      '''
fileName( (Font)arg1) -> str :

    C++ signature :
        std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > fileName(IECoreImage::Font {lvalue})'''
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
    def getKerning (self, *args, **kwargs):
      '''
getKerning( (Font)arg1) -> float :

    C++ signature :
        float getKerning(IECoreImage::Font {lvalue})'''
    ...
    def getResolution (self, *args, **kwargs):
      '''
getResolution( (Font)arg1) -> float :

    C++ signature :
        float getResolution(IECoreImage::Font {lvalue})'''
    ...
    def image (self, *args, **kwargs):
      '''
image( (Font)arg1 [, (str)arg2]) -> object :

    C++ signature :
        boost::intrusive_ptr<IECoreImage::ImagePrimitive> image(IECoreImage::Font {lvalue} [,char])'''
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
isInstanceOf( (Font)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreImage::Font {lvalue},IECore::TypeId)

isInstanceOf( (Font)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreImage::Font {lvalue},char const*)'''
    ...
    def isSame (self, *args, **kwargs):
      '''
isSame( (RefCounted)arg1, (RefCounted)arg2) -> bool :

    C++ signature :
        bool isSame(IECore::RefCounted const*,IECore::RefCounted const*)'''
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
registerType( (TypeId)arg1, (str)arg2, (TypeId)arg3) -> None :

    C++ signature :
        void registerType(IECore::TypeId,char const*,IECore::TypeId)'''
    ...
    def setKerning (self, *args, **kwargs):
      '''
setKerning( (Font)arg1, (float)arg2) -> None :

    C++ signature :
        void setKerning(IECoreImage::Font {lvalue},float)'''
    ...
    def setResolution (self, *args, **kwargs):
      '''
setResolution( (Font)arg1, (float)arg2) -> None :

    C++ signature :
        void setResolution(IECoreImage::Font {lvalue},float)'''
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
typeId( (Font)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreImage::Font {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (Font)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreImage::Font {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...

def HdrMergeOp (*args):
      '''
__init__(_object*)

'''      
    ...

class HdrMergeOp:
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
    def collectGarbage (self, *args, **kwargs):
      '''
collectGarbage() -> None :

    C++ signature :
        void collectGarbage()'''
    ...
    def derivedTypeIds (self, *args, **kwargs):
      '''
derivedTypeIds( (TypeId)arg1) -> list :

    C++ signature :
        boost::python::list derivedTypeIds(IECore::TypeId)'''
    ...
    def description (self, *args, **kwargs):
      '''None'''
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
isInstanceOf( (HdrMergeOp)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreImage::HdrMergeOp {lvalue},IECore::TypeId)

isInstanceOf( (HdrMergeOp)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreImage::HdrMergeOp {lvalue},char const*)'''
    ...
    def isSame (self, *args, **kwargs):
      '''
isSame( (RefCounted)arg1, (RefCounted)arg2) -> bool :

    C++ signature :
        bool isSame(IECore::RefCounted const*,IECore::RefCounted const*)'''
    ...
    def numWrappedInstances (self, *args, **kwargs):
      '''
numWrappedInstances() -> int :

    C++ signature :
        unsigned long numWrappedInstances()'''
    ...
    def operate (self, *args, **kwargs):
      '''
operate( (Op)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::Object> operate(IECore::Op {lvalue})

operate( (Op)arg1, (CompoundObject)arg2) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::Object> operate(IECore::Op {lvalue},IECore::CompoundObject const*)'''
    ...
    def parameters (self, *args, **kwargs):
      '''
parameters( (Parameterised)arg1) -> object :

    C++ signature :
        IECore::CompoundParameter* parameters(IECore::Parameterised {lvalue})'''
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
    def resultParameter (self, *args, **kwargs):
      '''
resultParameter( (Op)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::Parameter> resultParameter(IECore::Op)'''
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
typeId( (HdrMergeOp)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreImage::HdrMergeOp {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (HdrMergeOp)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreImage::HdrMergeOp {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...
    def userData (self, *args, **kwargs):
      '''
userData( (Parameterised)arg1) -> object :

    C++ signature :
        IECore::CompoundObject* userData(IECore::Parameterised {lvalue})'''
    ...

def ImageCropOp (*args):
      '''
__init__(_object*)

'''      
    ...

class ImageCropOp:
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
    def collectGarbage (self, *args, **kwargs):
      '''
collectGarbage() -> None :

    C++ signature :
        void collectGarbage()'''
    ...
    def derivedTypeIds (self, *args, **kwargs):
      '''
derivedTypeIds( (TypeId)arg1) -> list :

    C++ signature :
        boost::python::list derivedTypeIds(IECore::TypeId)'''
    ...
    def description (self, *args, **kwargs):
      '''None'''
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
isInstanceOf( (ImageCropOp)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreImage::ImageCropOp {lvalue},IECore::TypeId)

isInstanceOf( (ImageCropOp)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreImage::ImageCropOp {lvalue},char const*)'''
    ...
    def isSame (self, *args, **kwargs):
      '''
isSame( (RefCounted)arg1, (RefCounted)arg2) -> bool :

    C++ signature :
        bool isSame(IECore::RefCounted const*,IECore::RefCounted const*)'''
    ...
    def numWrappedInstances (self, *args, **kwargs):
      '''
numWrappedInstances() -> int :

    C++ signature :
        unsigned long numWrappedInstances()'''
    ...
    def operate (self, *args, **kwargs):
      '''
operate( (Op)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::Object> operate(IECore::Op {lvalue})

operate( (Op)arg1, (CompoundObject)arg2) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::Object> operate(IECore::Op {lvalue},IECore::CompoundObject const*)'''
    ...
    def parameters (self, *args, **kwargs):
      '''
parameters( (Parameterised)arg1) -> object :

    C++ signature :
        IECore::CompoundParameter* parameters(IECore::Parameterised {lvalue})'''
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
    def resultParameter (self, *args, **kwargs):
      '''
resultParameter( (Op)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::Parameter> resultParameter(IECore::Op)'''
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
typeId( (ImageCropOp)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreImage::ImageCropOp {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (ImageCropOp)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreImage::ImageCropOp {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...
    def userData (self, *args, **kwargs):
      '''
userData( (Parameterised)arg1) -> object :

    C++ signature :
        IECore::CompoundObject* userData(IECore::Parameterised {lvalue})'''
    ...

def ImageDiffOp (*args):
      '''
__init__(_object*)

'''      
    ...

class ImageDiffOp:
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
    def collectGarbage (self, *args, **kwargs):
      '''
collectGarbage() -> None :

    C++ signature :
        void collectGarbage()'''
    ...
    def derivedTypeIds (self, *args, **kwargs):
      '''
derivedTypeIds( (TypeId)arg1) -> list :

    C++ signature :
        boost::python::list derivedTypeIds(IECore::TypeId)'''
    ...
    def description (self, *args, **kwargs):
      '''None'''
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
isInstanceOf( (ImageDiffOp)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreImage::ImageDiffOp {lvalue},IECore::TypeId)

isInstanceOf( (ImageDiffOp)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreImage::ImageDiffOp {lvalue},char const*)'''
    ...
    def isSame (self, *args, **kwargs):
      '''
isSame( (RefCounted)arg1, (RefCounted)arg2) -> bool :

    C++ signature :
        bool isSame(IECore::RefCounted const*,IECore::RefCounted const*)'''
    ...
    def numWrappedInstances (self, *args, **kwargs):
      '''
numWrappedInstances() -> int :

    C++ signature :
        unsigned long numWrappedInstances()'''
    ...
    def operate (self, *args, **kwargs):
      '''
operate( (Op)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::Object> operate(IECore::Op {lvalue})

operate( (Op)arg1, (CompoundObject)arg2) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::Object> operate(IECore::Op {lvalue},IECore::CompoundObject const*)'''
    ...
    def parameters (self, *args, **kwargs):
      '''
parameters( (Parameterised)arg1) -> object :

    C++ signature :
        IECore::CompoundParameter* parameters(IECore::Parameterised {lvalue})'''
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
    def resultParameter (self, *args, **kwargs):
      '''
resultParameter( (Op)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::Parameter> resultParameter(IECore::Op)'''
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
typeId( (ImageDiffOp)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreImage::ImageDiffOp {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (ImageDiffOp)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreImage::ImageDiffOp {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...
    def userData (self, *args, **kwargs):
      '''
userData( (Parameterised)arg1) -> object :

    C++ signature :
        IECore::CompoundObject* userData(IECore::Parameterised {lvalue})'''
    ...

def ImageDisplayDriver (*args):
      '''
__init__(boost::python::api::object, Imath_3_1::Box<Imath_3_1::Vec2<int> > displayWindow, Imath_3_1::Box<Imath_3_1::Vec2<int> > dataWindow, boost::python::list channelNames, boost::intrusive_ptr<IECore::CompoundData> parameters)

'''      
    ...

class ImageDisplayDriver:
    def acceptsRepeatedData (self, *args, **kwargs):
      '''
acceptsRepeatedData( (DisplayDriver)arg1) -> bool :

    C++ signature :
        bool acceptsRepeatedData(IECoreImage::DisplayDriver {lvalue})'''
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
    def channelNames (self, *args, **kwargs):
      '''
channelNames( (object)arg1) -> list :

    C++ signature :
        boost::python::list channelNames(boost::intrusive_ptr<IECoreImage::DisplayDriver>)'''
    ...
    def collectGarbage (self, *args, **kwargs):
      '''
collectGarbage() -> None :

    C++ signature :
        void collectGarbage()'''
    ...
    def create (self, *args, **kwargs):
      '''
create( (object)arg1, (Box2i)arg2, (Box2i)arg3, (list)arg4, (object)arg5) -> object :

    C++ signature :
        boost::intrusive_ptr<IECoreImage::DisplayDriver> create(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >,Imath_3_1::Box<Imath_3_1::Vec2<int> >,Imath_3_1::Box<Imath_3_1::Vec2<int> >,boost::python::list,boost::intrusive_ptr<IECore::CompoundData>)'''
    ...
    def dataWindow (self, *args, **kwargs):
      '''
dataWindow( (DisplayDriver)arg1) -> Box2i :

    C++ signature :
        Imath_3_1::Box<Imath_3_1::Vec2<int> > dataWindow(IECoreImage::DisplayDriver {lvalue})'''
    ...
    def derivedTypeIds (self, *args, **kwargs):
      '''
derivedTypeIds( (TypeId)arg1) -> list :

    C++ signature :
        boost::python::list derivedTypeIds(IECore::TypeId)'''
    ...
    def displayWindow (self, *args, **kwargs):
      '''
displayWindow( (DisplayDriver)arg1) -> Box2i :

    C++ signature :
        Imath_3_1::Box<Imath_3_1::Vec2<int> > displayWindow(IECoreImage::DisplayDriver {lvalue})'''
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
    def image (self, *args, **kwargs):
      '''
image( (object)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECoreImage::ImagePrimitive> image(boost::intrusive_ptr<IECoreImage::ImageDisplayDriver>)'''
    ...
    def imageClose (self, *args, **kwargs):
      '''
imageClose( (object)arg1) -> None :

    C++ signature :
        void imageClose(boost::intrusive_ptr<IECoreImage::DisplayDriver>)'''
    ...
    def imageData (self, *args, **kwargs):
      '''
imageData( (object)arg1, (Box2i)arg2, (object)arg3) -> None :

    C++ signature :
        void imageData(boost::intrusive_ptr<IECoreImage::DisplayDriver>,Imath_3_1::Box<Imath_3_1::Vec2<int> >,boost::intrusive_ptr<IECore::TypedData<std::vector<float, std::allocator<float> > > >)'''
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
isInstanceOf( (ImageDisplayDriver)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreImage::ImageDisplayDriver {lvalue},IECore::TypeId)

isInstanceOf( (ImageDisplayDriver)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreImage::ImageDisplayDriver {lvalue},char const*)'''
    ...
    def isSame (self, *args, **kwargs):
      '''
isSame( (RefCounted)arg1, (RefCounted)arg2) -> bool :

    C++ signature :
        bool isSame(IECore::RefCounted const*,IECore::RefCounted const*)'''
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
registerType( (TypeId)arg1, (str)arg2, (TypeId)arg3) -> None :

    C++ signature :
        void registerType(IECore::TypeId,char const*,IECore::TypeId)'''
    ...
    def removeStoredImage (self, *args, **kwargs):
      '''
removeStoredImage( (object)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECoreImage::ImagePrimitive> removeStoredImage(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)'''
    ...
    def scanLineOrderOnly (self, *args, **kwargs):
      '''
scanLineOrderOnly( (object)arg1) -> bool :

    C++ signature :
        bool scanLineOrderOnly(boost::intrusive_ptr<IECoreImage::DisplayDriver>)'''
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
    def storedImage (self, *args, **kwargs):
      '''
storedImage( (object)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECoreImage::ImagePrimitive> storedImage(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)'''
    ...
    def typeId (self, *args, **kwargs):
      '''
typeId( (ImageDisplayDriver)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreImage::ImageDisplayDriver {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (ImageDisplayDriver)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreImage::ImageDisplayDriver {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...

def ImagePrimitive (*args):
      '''
__init__(_object*, Imath_3_1::Box<Imath_3_1::Vec2<int> >, Imath_3_1::Box<Imath_3_1::Vec2<int> >)
__init__(_object*)

'''      
    ...

class ImagePrimitive:
    def Space (self, *args, **kwargs):
      '''None'''
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
    def blindData (self, *args, **kwargs):
      '''
blindData( (BlindDataHolder)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::CompoundData> blindData(IECore::BlindDataHolder {lvalue})'''
    ...
    def channelNames (self, *args, **kwargs):
      '''
channelNames( (ImagePrimitive)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::TypedData<std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > > > channelNames(IECoreImage::ImagePrimitive {lvalue})'''
    ...
    def channelSize (self, *args, **kwargs):
      '''
channelSize( (ImagePrimitive)arg1) -> int :

    C++ signature :
        unsigned long channelSize(IECoreImage::ImagePrimitive {lvalue})'''
    ...
    def channelValid (self, *args, **kwargs):
      '''
channelValid( (ImagePrimitive)image, (Data)channel [, (bool)wantReason=False]) -> object :

    C++ signature :
        boost::python::api::object channelValid(IECoreImage::ImagePrimitive {lvalue},IECore::Data {lvalue} [,bool=False])

channelValid( (ImagePrimitive)image, (str)channelName [, (bool)wantReason=False]) -> object :

    C++ signature :
        boost::python::api::object channelValid(IECoreImage::ImagePrimitive {lvalue},char const* [,bool=False])'''
    ...
    def channelsValid (self, *args, **kwargs):
      '''
channelsValid( (ImagePrimitive)image [, (bool)wantReason=False]) -> object :

    C++ signature :
        boost::python::api::object channelsValid(IECoreImage::ImagePrimitive {lvalue} [,bool=False])'''
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
    def createFloatChannel (self, *args, **kwargs):
      '''
createFloatChannel( (ImagePrimitive)arg1, (object)arg2) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::Data> createFloatChannel(IECoreImage::ImagePrimitive {lvalue},std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)'''
    ...
    def createGreyscaleFloat (self, *args, **kwargs):
      '''
createGreyscaleFloat( (float)arg1, (Box2i)arg2, (Box2i)arg3) -> object :

    C++ signature :
        boost::intrusive_ptr<IECoreImage::ImagePrimitive> createGreyscaleFloat(float,Imath_3_1::Box<Imath_3_1::Vec2<int> >,Imath_3_1::Box<Imath_3_1::Vec2<int> >)'''
    ...
    def createHalfChannel (self, *args, **kwargs):
      '''
createHalfChannel( (ImagePrimitive)arg1, (object)arg2) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::Data> createHalfChannel(IECoreImage::ImagePrimitive {lvalue},std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)'''
    ...
    def createRGBFloat (self, *args, **kwargs):
      '''
createRGBFloat( (Color3f)arg1, (Box2i)arg2, (Box2i)arg3) -> object :

    C++ signature :
        boost::intrusive_ptr<IECoreImage::ImagePrimitive> createRGBFloat(Imath_3_1::Color3<float>,Imath_3_1::Box<Imath_3_1::Vec2<int> >,Imath_3_1::Box<Imath_3_1::Vec2<int> >)'''
    ...
    def createUIntChannel (self, *args, **kwargs):
      '''
createUIntChannel( (ImagePrimitive)arg1, (object)arg2) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::Data> createUIntChannel(IECoreImage::ImagePrimitive {lvalue},std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)'''
    ...
    def dataWindow (self, *args, **kwargs):
      '''None'''
    ...
    def derivedTypeIds (self, *args, **kwargs):
      '''
derivedTypeIds( (TypeId)arg1) -> list :

    C++ signature :
        boost::python::list derivedTypeIds(IECore::TypeId)'''
    ...
    def displayWindow (self, *args, **kwargs):
      '''None'''
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
    def getChannel (self, *args, **kwargs):
      '''
getChannel( (ImagePrimitive)arg1, (str)arg2) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::Data> getChannel(IECoreImage::ImagePrimitive {lvalue},char const*)'''
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
isInstanceOf( (ImagePrimitive)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreImage::ImagePrimitive {lvalue},IECore::TypeId)

isInstanceOf( (ImagePrimitive)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreImage::ImagePrimitive {lvalue},char const*)'''
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
    def keys (self, *args, **kwargs):
      '''
keys( (ImagePrimitive)arg1) -> list :

    C++ signature :
        boost::python::list keys(IECoreImage::ImagePrimitive {lvalue})'''
    ...
    def load (self, *args, **kwargs):
      '''
load( (object)ioInterface, (InternedString)name [, (Canceller)canceller=None]) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::Object> load(boost::intrusive_ptr<IECore::IndexedIO const>,IECore::InternedString [,IECore::Canceller const*=None])'''
    ...
    def matrix (self, *args, **kwargs):
      '''
matrix( (ImagePrimitive)arg1, (Space)arg2, (Space)arg3) -> M33f :

    C++ signature :
        Imath_3_1::Matrix33<float> matrix(IECoreImage::ImagePrimitive {lvalue},IECoreImage::ImagePrimitive::Space,IECoreImage::ImagePrimitive::Space)'''
    ...
    def memoryUsage (self, *args, **kwargs):
      '''
memoryUsage( (Object)arg1) -> int :
    Returns the number of bytes this instance occupies in memory

    C++ signature :
        unsigned long memoryUsage(IECore::Object {lvalue})'''
    ...
    def numWrappedInstances (self, *args, **kwargs):
      '''
numWrappedInstances() -> int :

    C++ signature :
        unsigned long numWrappedInstances()'''
    ...
    def objectToPixelMatrix (self, *args, **kwargs):
      '''
objectToPixelMatrix( (ImagePrimitive)arg1) -> M33f :

    C++ signature :
        Imath_3_1::Matrix33<float> objectToPixelMatrix(IECoreImage::ImagePrimitive {lvalue})'''
    ...
    def objectToUVMatrix (self, *args, **kwargs):
      '''
objectToUVMatrix( (ImagePrimitive)arg1) -> M33f :

    C++ signature :
        Imath_3_1::Matrix33<float> objectToUVMatrix(IECoreImage::ImagePrimitive {lvalue})'''
    ...
    def pixelToObjectMatrix (self, *args, **kwargs):
      '''
pixelToObjectMatrix( (ImagePrimitive)arg1) -> M33f :

    C++ signature :
        Imath_3_1::Matrix33<float> pixelToObjectMatrix(IECoreImage::ImagePrimitive {lvalue})'''
    ...
    def pixelToUVMatrix (self, *args, **kwargs):
      '''
pixelToUVMatrix( (ImagePrimitive)arg1) -> M33f :

    C++ signature :
        Imath_3_1::Matrix33<float> pixelToUVMatrix(IECoreImage::ImagePrimitive {lvalue})'''
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
typeId( (ImagePrimitive)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreImage::ImagePrimitive {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (ImagePrimitive)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreImage::ImagePrimitive {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...
    def uvToObjectMatrix (self, *args, **kwargs):
      '''
uvToObjectMatrix( (ImagePrimitive)arg1) -> M33f :

    C++ signature :
        Imath_3_1::Matrix33<float> uvToObjectMatrix(IECoreImage::ImagePrimitive {lvalue})'''
    ...
    def uvToPixelMatrix (self, *args, **kwargs):
      '''
uvToPixelMatrix( (ImagePrimitive)arg1) -> M33f :

    C++ signature :
        Imath_3_1::Matrix33<float> uvToPixelMatrix(IECoreImage::ImagePrimitive {lvalue})'''
    ...
    def values (self, *args, **kwargs):
      '''
values( (ImagePrimitive)arg1) -> list :
    Returns a list containing shallow copies of all channel data.

    C++ signature :
        boost::python::list values(IECoreImage::ImagePrimitive {lvalue})'''
    ...

def ImagePrimitiveParameter (*args):
      '''
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > name, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > description, boost::intrusive_ptr<IECoreImage::ImagePrimitive> defaultValue)
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > name, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > description, boost::intrusive_ptr<IECoreImage::ImagePrimitive> defaultValue, boost::python::api::object presets=())
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > name, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > description, boost::intrusive_ptr<IECoreImage::ImagePrimitive> defaultValue, boost::python::api::object presets=(), bool presetsOnly=False)
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > name, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > description, boost::intrusive_ptr<IECoreImage::ImagePrimitive> defaultValue, boost::python::api::object presets=(), bool presetsOnly=False, boost::intrusive_ptr<IECore::CompoundObject> userData=None)

'''      
    ...

class ImagePrimitiveParameter:
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
    def collectGarbage (self, *args, **kwargs):
      '''
collectGarbage() -> None :

    C++ signature :
        void collectGarbage()'''
    ...
    def defaultValue (self, *args, **kwargs):
      '''None'''
    ...
    def derivedTypeIds (self, *args, **kwargs):
      '''
derivedTypeIds( (TypeId)arg1) -> list :

    C++ signature :
        boost::python::list derivedTypeIds(IECore::TypeId)'''
    ...
    def description (self, *args, **kwargs):
      '''None'''
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
    def getCurrentPresetName (self, *args, **kwargs):
      '''
getCurrentPresetName( (Parameter)arg1) -> str :

    C++ signature :
        std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > getCurrentPresetName(IECore::Parameter {lvalue})'''
    ...
    def getPresets (self, *args, **kwargs):
      '''
getPresets( (Parameter)arg1) -> dict :
    Returns a dictionary containing presets for the parameter.

    C++ signature :
        boost::python::dict getPresets(IECore::Parameter {lvalue})'''
    ...
    def getValidatedValue (self, *args, **kwargs):
      '''
getValidatedValue( (Parameter)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::Object> getValidatedValue(IECore::Parameter {lvalue})'''
    ...
    def getValue (self, *args, **kwargs):
      '''
getValue( (Parameter)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::Object> getValue(IECore::Parameter {lvalue})'''
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
isInstanceOf( (ImagePrimitiveParameter)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECore::TypedObjectParameter<IECoreImage::ImagePrimitive> {lvalue},IECore::TypeId)

isInstanceOf( (ImagePrimitiveParameter)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECore::TypedObjectParameter<IECoreImage::ImagePrimitive> {lvalue},char const*)'''
    ...
    def isSame (self, *args, **kwargs):
      '''
isSame( (RefCounted)arg1, (RefCounted)arg2) -> bool :

    C++ signature :
        bool isSame(IECore::RefCounted const*,IECore::RefCounted const*)'''
    ...
    def name (self, *args, **kwargs):
      '''None'''
    ...
    def numWrappedInstances (self, *args, **kwargs):
      '''
numWrappedInstances() -> int :

    C++ signature :
        unsigned long numWrappedInstances()'''
    ...
    def presetNames (self, *args, **kwargs):
      '''
presetNames( (Parameter)arg1) -> tuple :
    Returns a tuple containing the names of all presets for the parameter.

    C++ signature :
        boost::python::tuple presetNames(IECore::Parameter)'''
    ...
    def presetValues (self, *args, **kwargs):
      '''
presetValues( (Parameter)arg1) -> tuple :
    Returns a tuple containing the values of all presets for the parameter.

    C++ signature :
        boost::python::tuple presetValues(IECore::Parameter)'''
    ...
    def presetsOnly (self, *args, **kwargs):
      '''None'''
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
    def setPresets (self, *args, **kwargs):
      '''
setPresets( (Parameter)arg1, (object)arg2) -> None :
    Sets the presets for the parameter from a dictionary.

    C++ signature :
        void setPresets(IECore::Parameter {lvalue},boost::python::api::object)'''
    ...
    def setValidatedValue (self, *args, **kwargs):
      '''
setValidatedValue( (Parameter)arg1, (object)arg2) -> None :

    C++ signature :
        void setValidatedValue(IECore::Parameter {lvalue},boost::intrusive_ptr<IECore::Object>)'''
    ...
    def setValue (self, *args, **kwargs):
      '''
setValue( (Parameter)arg1, (object)arg2) -> None :

    C++ signature :
        void setValue(IECore::Parameter {lvalue},boost::intrusive_ptr<IECore::Object>)

setValue( (Parameter)arg1, (object)arg2) -> None :

    C++ signature :
        void setValue(IECore::Parameter {lvalue},std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)'''
    ...
    def smartSetValue (self, value):
      '''
	Smart setValue operator for Parameter objects. Uses introspection on the given value to define
	how the value will be assigned to the Parameter object.
	'''
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
typeId( (ImagePrimitiveParameter)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECore::TypedObjectParameter<IECoreImage::ImagePrimitive> {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (ImagePrimitiveParameter)arg1) -> str :

    C++ signature :
        char const* typeName(IECore::TypedObjectParameter<IECoreImage::ImagePrimitive> {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...
    def userData (self, *args, **kwargs):
      '''
userData( (Parameter)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::CompoundObject> userData(IECore::Parameter {lvalue})'''
    ...
    def validTypes (self, *args, **kwargs):
      '''
validTypes( (ObjectParameter)arg1) -> list :

    C++ signature :
        boost::python::list validTypes(IECore::ObjectParameter {lvalue})'''
    ...
    def validate (self, *args, **kwargs):
      '''
validate( (Parameter)arg1) -> None :

    C++ signature :
        void validate(IECore::Parameter {lvalue})

validate( (Parameter)arg1, (object)arg2) -> None :

    C++ signature :
        void validate(IECore::Parameter {lvalue},boost::intrusive_ptr<IECore::Object>)'''
    ...
    def valueValid (self, *args, **kwargs):
      '''
valueValid( (ImagePrimitiveParameter)arg1, (object)arg2) -> tuple :
    Returns a tuple containing a bool specifying validity and a string giving a reason for invalidity.

    C++ signature :
        boost::python::tuple valueValid(IECore::TypedObjectParameter<IECoreImage::ImagePrimitive>,boost::intrusive_ptr<IECore::Object const>)

valueValid( (Parameter)arg1) -> tuple :
    Returns a tuple containing a bool specifying validity and a string giving a reason for invalidity.

    C++ signature :
        boost::python::tuple valueValid(IECore::Parameter)'''
    ...

def ImageReader (*args):
      '''
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)
__init__(_object*)

'''      
    ...

class ImageReader:
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
    def canRead (self, *args, **kwargs):
      '''
canRead( (object)arg1) -> bool :

    C++ signature :
        bool canRead(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)'''
    ...
    def channelNames (self, *args, **kwargs):
      '''
channelNames( (ImageReader)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::TypedData<std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > > > channelNames(IECoreImage::ImageReader {lvalue})'''
    ...
    def collectGarbage (self, *args, **kwargs):
      '''
collectGarbage() -> None :

    C++ signature :
        void collectGarbage()'''
    ...
    def create (self, *args, **kwargs):
      '''
create( (object)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::Reader> create(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)'''
    ...
    def dataWindow (self, *args, **kwargs):
      '''
dataWindow( (ImageReader)arg1) -> Box2i :

    C++ signature :
        Imath_3_1::Box<Imath_3_1::Vec2<int> > dataWindow(IECoreImage::ImageReader {lvalue})'''
    ...
    def derivedTypeIds (self, *args, **kwargs):
      '''
derivedTypeIds( (TypeId)arg1) -> list :

    C++ signature :
        boost::python::list derivedTypeIds(IECore::TypeId)'''
    ...
    def description (self, *args, **kwargs):
      '''None'''
    ...
    def displayWindow (self, *args, **kwargs):
      '''
displayWindow( (ImageReader)arg1) -> Box2i :

    C++ signature :
        Imath_3_1::Box<Imath_3_1::Vec2<int> > displayWindow(IECoreImage::ImageReader {lvalue})'''
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
    def isComplete (self, *args, **kwargs):
      '''
isComplete( (ImageReader)arg1) -> bool :

    C++ signature :
        bool isComplete(IECoreImage::ImageReader {lvalue})'''
    ...
    def isInstanceOf (self, *args, **kwargs):
      '''
isInstanceOf( (ImageReader)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreImage::ImageReader {lvalue},IECore::TypeId)

isInstanceOf( (ImageReader)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreImage::ImageReader {lvalue},char const*)'''
    ...
    def isSame (self, *args, **kwargs):
      '''
isSame( (RefCounted)arg1, (RefCounted)arg2) -> bool :

    C++ signature :
        bool isSame(IECore::RefCounted const*,IECore::RefCounted const*)'''
    ...
    def numWrappedInstances (self, *args, **kwargs):
      '''
numWrappedInstances() -> int :

    C++ signature :
        unsigned long numWrappedInstances()'''
    ...
    def operate (self, *args, **kwargs):
      '''
operate( (Op)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::Object> operate(IECore::Op {lvalue})

operate( (Op)arg1, (CompoundObject)arg2) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::Object> operate(IECore::Op {lvalue},IECore::CompoundObject const*)'''
    ...
    def parameters (self, *args, **kwargs):
      '''
parameters( (Parameterised)arg1) -> object :

    C++ signature :
        IECore::CompoundParameter* parameters(IECore::Parameterised {lvalue})'''
    ...
    def read (self, *args, **kwargs):
      '''
read( (ImageReader)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::Object> read(IECoreImage::ImageReader {lvalue})'''
    ...
    def readChannel (self, *args, **kwargs):
      '''
readChannel( (ImageReader)arg1, (object)name [, (bool)raw=False]) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::Data> readChannel(IECoreImage::ImageReader {lvalue},std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > [,bool=False])'''
    ...
    def readHeader (self, *args, **kwargs):
      '''
readHeader( (ImageReader)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::CompoundObject> readHeader(IECoreImage::ImageReader {lvalue})'''
    ...
    def refCount (self, *args, **kwargs):
      '''
refCount( (RefCounted)arg1) -> int :

    C++ signature :
        unsigned long refCount(IECore::RefCounted {lvalue})'''
    ...
    def registerReader (self, *args, **kwargs):
      '''
registerReader( (object)arg1, (object)arg2, (object)arg3, (TypeId)arg4) -> None :

    C++ signature :
        void registerReader(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >,boost::python::api::object {lvalue},boost::python::api::object {lvalue},IECore::TypeId)'''
    ...
    def registerType (self, *args, **kwargs):
      '''
registerType( (TypeId)arg1, (str)arg2, (TypeId)arg3) -> None :

    C++ signature :
        void registerType(IECore::TypeId,char const*,IECore::TypeId)'''
    ...
    def resultParameter (self, *args, **kwargs):
      '''
resultParameter( (Op)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::Parameter> resultParameter(IECore::Op)'''
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
    def supportedExtensions (self, *args, **kwargs):
      '''
supportedExtensions() -> list :

    C++ signature :
        boost::python::list supportedExtensions()

supportedExtensions( (TypeId)arg1) -> list :

    C++ signature :
        boost::python::list supportedExtensions(IECore::TypeId)'''
    ...
    def typeId (self, *args, **kwargs):
      '''
typeId( (ImageReader)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreImage::ImageReader {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (ImageReader)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreImage::ImageReader {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...
    def userData (self, *args, **kwargs):
      '''
userData( (Parameterised)arg1) -> object :

    C++ signature :
        IECore::CompoundObject* userData(IECore::Parameterised {lvalue})'''
    ...

def ImageThinner (*args):
      '''
__init__(_object*)

'''      
    ...

class ImageThinner:
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
    def collectGarbage (self, *args, **kwargs):
      '''
collectGarbage() -> None :

    C++ signature :
        void collectGarbage()'''
    ...
    def derivedTypeIds (self, *args, **kwargs):
      '''
derivedTypeIds( (TypeId)arg1) -> list :

    C++ signature :
        boost::python::list derivedTypeIds(IECore::TypeId)'''
    ...
    def description (self, *args, **kwargs):
      '''None'''
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
isInstanceOf( (ImageThinner)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreImage::ImageThinner {lvalue},IECore::TypeId)

isInstanceOf( (ImageThinner)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreImage::ImageThinner {lvalue},char const*)'''
    ...
    def isSame (self, *args, **kwargs):
      '''
isSame( (RefCounted)arg1, (RefCounted)arg2) -> bool :

    C++ signature :
        bool isSame(IECore::RefCounted const*,IECore::RefCounted const*)'''
    ...
    def numWrappedInstances (self, *args, **kwargs):
      '''
numWrappedInstances() -> int :

    C++ signature :
        unsigned long numWrappedInstances()'''
    ...
    def operate (self, *args, **kwargs):
      '''
operate( (Op)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::Object> operate(IECore::Op {lvalue})

operate( (Op)arg1, (CompoundObject)arg2) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::Object> operate(IECore::Op {lvalue},IECore::CompoundObject const*)'''
    ...
    def parameters (self, *args, **kwargs):
      '''
parameters( (Parameterised)arg1) -> object :

    C++ signature :
        IECore::CompoundParameter* parameters(IECore::Parameterised {lvalue})'''
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
    def resultParameter (self, *args, **kwargs):
      '''
resultParameter( (Op)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::Parameter> resultParameter(IECore::Op)'''
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
typeId( (ImageThinner)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreImage::ImageThinner {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (ImageThinner)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreImage::ImageThinner {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...
    def userData (self, *args, **kwargs):
      '''
userData( (Parameterised)arg1) -> object :

    C++ signature :
        IECore::CompoundObject* userData(IECore::Parameterised {lvalue})'''
    ...

def ImageWriter (*args):
      '''
__init__(_object*, boost::intrusive_ptr<IECore::Object>, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)
__init__(_object*)

'''      
    ...

class ImageWriter:
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
    def canWrite (self, *args, **kwargs):
      '''
canWrite( (object)arg1, (object)arg2) -> bool :

    C++ signature :
        bool canWrite(boost::intrusive_ptr<IECore::Object const>,std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)'''
    ...
    def collectGarbage (self, *args, **kwargs):
      '''
collectGarbage() -> None :

    C++ signature :
        void collectGarbage()'''
    ...
    def create (self, *args, **kwargs):
      '''
create( (object)arg1, (object)arg2) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::Writer> create(boost::intrusive_ptr<IECore::Object>,std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)

create( (object)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::Writer> create(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)'''
    ...
    def derivedTypeIds (self, *args, **kwargs):
      '''
derivedTypeIds( (TypeId)arg1) -> list :

    C++ signature :
        boost::python::list derivedTypeIds(IECore::TypeId)'''
    ...
    def description (self, *args, **kwargs):
      '''None'''
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
isInstanceOf( (ImageWriter)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreImage::ImageWriter {lvalue},IECore::TypeId)

isInstanceOf( (ImageWriter)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreImage::ImageWriter {lvalue},char const*)'''
    ...
    def isSame (self, *args, **kwargs):
      '''
isSame( (RefCounted)arg1, (RefCounted)arg2) -> bool :

    C++ signature :
        bool isSame(IECore::RefCounted const*,IECore::RefCounted const*)'''
    ...
    def numWrappedInstances (self, *args, **kwargs):
      '''
numWrappedInstances() -> int :

    C++ signature :
        unsigned long numWrappedInstances()'''
    ...
    def operate (self, *args, **kwargs):
      '''
operate( (Op)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::Object> operate(IECore::Op {lvalue})

operate( (Op)arg1, (CompoundObject)arg2) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::Object> operate(IECore::Op {lvalue},IECore::CompoundObject const*)'''
    ...
    def parameters (self, *args, **kwargs):
      '''
parameters( (Parameterised)arg1) -> object :

    C++ signature :
        IECore::CompoundParameter* parameters(IECore::Parameterised {lvalue})'''
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
    def resultParameter (self, *args, **kwargs):
      '''
resultParameter( (Op)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::Parameter> resultParameter(IECore::Op)'''
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
    def supportedExtensions (self, *args, **kwargs):
      '''
supportedExtensions() -> list :

    C++ signature :
        boost::python::list supportedExtensions()

supportedExtensions( (TypeId)arg1) -> list :

    C++ signature :
        boost::python::list supportedExtensions(IECore::TypeId)'''
    ...
    def typeId (self, *args, **kwargs):
      '''
typeId( (ImageWriter)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreImage::ImageWriter {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (ImageWriter)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreImage::ImageWriter {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...
    def userData (self, *args, **kwargs):
      '''
userData( (Parameterised)arg1) -> object :

    C++ signature :
        IECore::CompoundObject* userData(IECore::Parameterised {lvalue})'''
    ...
    def write (self, *args, **kwargs):
      '''
write( (Writer)arg1) -> None :

    C++ signature :
        void write(IECore::Writer {lvalue})'''
    ...

def LensDistortOp (*args):
      '''
__init__(_object*)

'''      
    ...

class LensDistortOp:
    def BoundMode (self, *args, **kwargs):
      '''None'''
    ...
    def FilterType (self, *args, **kwargs):
      '''None'''
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
    def collectGarbage (self, *args, **kwargs):
      '''
collectGarbage() -> None :

    C++ signature :
        void collectGarbage()'''
    ...
    def derivedTypeIds (self, *args, **kwargs):
      '''
derivedTypeIds( (TypeId)arg1) -> list :

    C++ signature :
        boost::python::list derivedTypeIds(IECore::TypeId)'''
    ...
    def description (self, *args, **kwargs):
      '''None'''
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
isInstanceOf( (LensDistortOp)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreImage::LensDistortOp {lvalue},IECore::TypeId)

isInstanceOf( (LensDistortOp)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreImage::LensDistortOp {lvalue},char const*)'''
    ...
    def isSame (self, *args, **kwargs):
      '''
isSame( (RefCounted)arg1, (RefCounted)arg2) -> bool :

    C++ signature :
        bool isSame(IECore::RefCounted const*,IECore::RefCounted const*)'''
    ...
    def numWrappedInstances (self, *args, **kwargs):
      '''
numWrappedInstances() -> int :

    C++ signature :
        unsigned long numWrappedInstances()'''
    ...
    def operate (self, *args, **kwargs):
      '''
operate( (Op)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::Object> operate(IECore::Op {lvalue})

operate( (Op)arg1, (CompoundObject)arg2) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::Object> operate(IECore::Op {lvalue},IECore::CompoundObject const*)'''
    ...
    def parameters (self, *args, **kwargs):
      '''
parameters( (Parameterised)arg1) -> object :

    C++ signature :
        IECore::CompoundParameter* parameters(IECore::Parameterised {lvalue})'''
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
    def resultParameter (self, *args, **kwargs):
      '''
resultParameter( (Op)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::Parameter> resultParameter(IECore::Op)'''
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
typeId( (LensDistortOp)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreImage::LensDistortOp {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (LensDistortOp)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreImage::LensDistortOp {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...
    def userData (self, *args, **kwargs):
      '''
userData( (Parameterised)arg1) -> object :

    C++ signature :
        IECore::CompoundObject* userData(IECore::Parameterised {lvalue})'''
    ...

def LuminanceOp (*args):
      '''
__init__(_object*)

'''      
    ...

class LuminanceOp:
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
    def collectGarbage (self, *args, **kwargs):
      '''
collectGarbage() -> None :

    C++ signature :
        void collectGarbage()'''
    ...
    def derivedTypeIds (self, *args, **kwargs):
      '''
derivedTypeIds( (TypeId)arg1) -> list :

    C++ signature :
        boost::python::list derivedTypeIds(IECore::TypeId)'''
    ...
    def description (self, *args, **kwargs):
      '''None'''
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
isInstanceOf( (LuminanceOp)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreImage::LuminanceOp {lvalue},IECore::TypeId)

isInstanceOf( (LuminanceOp)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreImage::LuminanceOp {lvalue},char const*)'''
    ...
    def isSame (self, *args, **kwargs):
      '''
isSame( (RefCounted)arg1, (RefCounted)arg2) -> bool :

    C++ signature :
        bool isSame(IECore::RefCounted const*,IECore::RefCounted const*)'''
    ...
    def numWrappedInstances (self, *args, **kwargs):
      '''
numWrappedInstances() -> int :

    C++ signature :
        unsigned long numWrappedInstances()'''
    ...
    def operate (self, *args, **kwargs):
      '''
operate( (Op)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::Object> operate(IECore::Op {lvalue})

operate( (Op)arg1, (CompoundObject)arg2) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::Object> operate(IECore::Op {lvalue},IECore::CompoundObject const*)'''
    ...
    def parameters (self, *args, **kwargs):
      '''
parameters( (Parameterised)arg1) -> object :

    C++ signature :
        IECore::CompoundParameter* parameters(IECore::Parameterised {lvalue})'''
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
    def resultParameter (self, *args, **kwargs):
      '''
resultParameter( (Op)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::Parameter> resultParameter(IECore::Op)'''
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
typeId( (LuminanceOp)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreImage::LuminanceOp {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (LuminanceOp)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreImage::LuminanceOp {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...
    def userData (self, *args, **kwargs):
      '''
userData( (Parameterised)arg1) -> object :

    C++ signature :
        IECore::CompoundObject* userData(IECore::Parameterised {lvalue})'''
    ...

def MPlayDisplayDriver (*args):
      '''
__init__(boost::python::api::object, Imath_3_1::Box<Imath_3_1::Vec2<int> > displayWindow, Imath_3_1::Box<Imath_3_1::Vec2<int> > dataWindow, boost::python::list channelNames, boost::intrusive_ptr<IECore::CompoundData> parameters)

'''      
    ...

class MPlayDisplayDriver:
    def acceptsRepeatedData (self, *args, **kwargs):
      '''
acceptsRepeatedData( (DisplayDriver)arg1) -> bool :

    C++ signature :
        bool acceptsRepeatedData(IECoreImage::DisplayDriver {lvalue})'''
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
    def channelNames (self, *args, **kwargs):
      '''
channelNames( (object)arg1) -> list :

    C++ signature :
        boost::python::list channelNames(boost::intrusive_ptr<IECoreImage::DisplayDriver>)'''
    ...
    def collectGarbage (self, *args, **kwargs):
      '''
collectGarbage() -> None :

    C++ signature :
        void collectGarbage()'''
    ...
    def create (self, *args, **kwargs):
      '''
create( (object)arg1, (Box2i)arg2, (Box2i)arg3, (list)arg4, (object)arg5) -> object :

    C++ signature :
        boost::intrusive_ptr<IECoreImage::DisplayDriver> create(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >,Imath_3_1::Box<Imath_3_1::Vec2<int> >,Imath_3_1::Box<Imath_3_1::Vec2<int> >,boost::python::list,boost::intrusive_ptr<IECore::CompoundData>)'''
    ...
    def dataWindow (self, *args, **kwargs):
      '''
dataWindow( (DisplayDriver)arg1) -> Box2i :

    C++ signature :
        Imath_3_1::Box<Imath_3_1::Vec2<int> > dataWindow(IECoreImage::DisplayDriver {lvalue})'''
    ...
    def derivedTypeIds (self, *args, **kwargs):
      '''
derivedTypeIds( (TypeId)arg1) -> list :

    C++ signature :
        boost::python::list derivedTypeIds(IECore::TypeId)'''
    ...
    def displayWindow (self, *args, **kwargs):
      '''
displayWindow( (DisplayDriver)arg1) -> Box2i :

    C++ signature :
        Imath_3_1::Box<Imath_3_1::Vec2<int> > displayWindow(IECoreImage::DisplayDriver {lvalue})'''
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
    def imageClose (self, *args, **kwargs):
      '''
imageClose( (object)arg1) -> None :

    C++ signature :
        void imageClose(boost::intrusive_ptr<IECoreImage::DisplayDriver>)'''
    ...
    def imageData (self, *args, **kwargs):
      '''
imageData( (object)arg1, (Box2i)arg2, (object)arg3) -> None :

    C++ signature :
        void imageData(boost::intrusive_ptr<IECoreImage::DisplayDriver>,Imath_3_1::Box<Imath_3_1::Vec2<int> >,boost::intrusive_ptr<IECore::TypedData<std::vector<float, std::allocator<float> > > >)'''
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
isInstanceOf( (MPlayDisplayDriver)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreImage::MPlayDisplayDriver {lvalue},IECore::TypeId)

isInstanceOf( (MPlayDisplayDriver)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreImage::MPlayDisplayDriver {lvalue},char const*)'''
    ...
    def isSame (self, *args, **kwargs):
      '''
isSame( (RefCounted)arg1, (RefCounted)arg2) -> bool :

    C++ signature :
        bool isSame(IECore::RefCounted const*,IECore::RefCounted const*)'''
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
registerType( (TypeId)arg1, (str)arg2, (TypeId)arg3) -> None :

    C++ signature :
        void registerType(IECore::TypeId,char const*,IECore::TypeId)'''
    ...
    def scanLineOrderOnly (self, *args, **kwargs):
      '''
scanLineOrderOnly( (object)arg1) -> bool :

    C++ signature :
        bool scanLineOrderOnly(boost::intrusive_ptr<IECoreImage::DisplayDriver>)'''
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
typeId( (MPlayDisplayDriver)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreImage::MPlayDisplayDriver {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (MPlayDisplayDriver)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreImage::MPlayDisplayDriver {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...

def MedianCutSampler (*args):
      '''
__init__(_object*)

'''      
    ...

class MedianCutSampler:
    def Projection (self, *args, **kwargs):
      '''None'''
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
    def collectGarbage (self, *args, **kwargs):
      '''
collectGarbage() -> None :

    C++ signature :
        void collectGarbage()'''
    ...
    def derivedTypeIds (self, *args, **kwargs):
      '''
derivedTypeIds( (TypeId)arg1) -> list :

    C++ signature :
        boost::python::list derivedTypeIds(IECore::TypeId)'''
    ...
    def description (self, *args, **kwargs):
      '''None'''
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
isInstanceOf( (MedianCutSampler)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreImage::MedianCutSampler {lvalue},IECore::TypeId)

isInstanceOf( (MedianCutSampler)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreImage::MedianCutSampler {lvalue},char const*)'''
    ...
    def isSame (self, *args, **kwargs):
      '''
isSame( (RefCounted)arg1, (RefCounted)arg2) -> bool :

    C++ signature :
        bool isSame(IECore::RefCounted const*,IECore::RefCounted const*)'''
    ...
    def numWrappedInstances (self, *args, **kwargs):
      '''
numWrappedInstances() -> int :

    C++ signature :
        unsigned long numWrappedInstances()'''
    ...
    def operate (self, *args, **kwargs):
      '''
operate( (Op)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::Object> operate(IECore::Op {lvalue})

operate( (Op)arg1, (CompoundObject)arg2) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::Object> operate(IECore::Op {lvalue},IECore::CompoundObject const*)'''
    ...
    def parameters (self, *args, **kwargs):
      '''
parameters( (Parameterised)arg1) -> object :

    C++ signature :
        IECore::CompoundParameter* parameters(IECore::Parameterised {lvalue})'''
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
    def resultParameter (self, *args, **kwargs):
      '''
resultParameter( (Op)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::Parameter> resultParameter(IECore::Op)'''
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
typeId( (MedianCutSampler)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreImage::MedianCutSampler {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (MedianCutSampler)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreImage::MedianCutSampler {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...
    def userData (self, *args, **kwargs):
      '''
userData( (Parameterised)arg1) -> object :

    C++ signature :
        IECore::CompoundObject* userData(IECore::Parameterised {lvalue})'''
    ...

def OpenImageIOAlgo (*args):
      '''

'''      
    ...

def SplineToImage (*args):
      '''
__init__(_object*)

'''      
    ...

class SplineToImage:
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
    def collectGarbage (self, *args, **kwargs):
      '''
collectGarbage() -> None :

    C++ signature :
        void collectGarbage()'''
    ...
    def derivedTypeIds (self, *args, **kwargs):
      '''
derivedTypeIds( (TypeId)arg1) -> list :

    C++ signature :
        boost::python::list derivedTypeIds(IECore::TypeId)'''
    ...
    def description (self, *args, **kwargs):
      '''None'''
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
isInstanceOf( (SplineToImage)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreImage::SplineToImage {lvalue},IECore::TypeId)

isInstanceOf( (SplineToImage)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreImage::SplineToImage {lvalue},char const*)'''
    ...
    def isSame (self, *args, **kwargs):
      '''
isSame( (RefCounted)arg1, (RefCounted)arg2) -> bool :

    C++ signature :
        bool isSame(IECore::RefCounted const*,IECore::RefCounted const*)'''
    ...
    def numWrappedInstances (self, *args, **kwargs):
      '''
numWrappedInstances() -> int :

    C++ signature :
        unsigned long numWrappedInstances()'''
    ...
    def operate (self, *args, **kwargs):
      '''
operate( (Op)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::Object> operate(IECore::Op {lvalue})

operate( (Op)arg1, (CompoundObject)arg2) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::Object> operate(IECore::Op {lvalue},IECore::CompoundObject const*)'''
    ...
    def parameters (self, *args, **kwargs):
      '''
parameters( (Parameterised)arg1) -> object :

    C++ signature :
        IECore::CompoundParameter* parameters(IECore::Parameterised {lvalue})'''
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
    def resultParameter (self, *args, **kwargs):
      '''
resultParameter( (Op)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::Parameter> resultParameter(IECore::Op)'''
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
typeId( (SplineToImage)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreImage::SplineToImage {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (SplineToImage)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreImage::SplineToImage {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...
    def userData (self, *args, **kwargs):
      '''
userData( (Parameterised)arg1) -> object :

    C++ signature :
        IECore::CompoundObject* userData(IECore::Parameterised {lvalue})'''
    ...

def SummedAreaOp (*args):
      '''
__init__(_object*)

'''      
    ...

class SummedAreaOp:
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
    def collectGarbage (self, *args, **kwargs):
      '''
collectGarbage() -> None :

    C++ signature :
        void collectGarbage()'''
    ...
    def derivedTypeIds (self, *args, **kwargs):
      '''
derivedTypeIds( (TypeId)arg1) -> list :

    C++ signature :
        boost::python::list derivedTypeIds(IECore::TypeId)'''
    ...
    def description (self, *args, **kwargs):
      '''None'''
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
isInstanceOf( (SummedAreaOp)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreImage::SummedAreaOp {lvalue},IECore::TypeId)

isInstanceOf( (SummedAreaOp)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreImage::SummedAreaOp {lvalue},char const*)'''
    ...
    def isSame (self, *args, **kwargs):
      '''
isSame( (RefCounted)arg1, (RefCounted)arg2) -> bool :

    C++ signature :
        bool isSame(IECore::RefCounted const*,IECore::RefCounted const*)'''
    ...
    def numWrappedInstances (self, *args, **kwargs):
      '''
numWrappedInstances() -> int :

    C++ signature :
        unsigned long numWrappedInstances()'''
    ...
    def operate (self, *args, **kwargs):
      '''
operate( (Op)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::Object> operate(IECore::Op {lvalue})

operate( (Op)arg1, (CompoundObject)arg2) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::Object> operate(IECore::Op {lvalue},IECore::CompoundObject const*)'''
    ...
    def parameters (self, *args, **kwargs):
      '''
parameters( (Parameterised)arg1) -> object :

    C++ signature :
        IECore::CompoundParameter* parameters(IECore::Parameterised {lvalue})'''
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
    def resultParameter (self, *args, **kwargs):
      '''
resultParameter( (Op)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::Parameter> resultParameter(IECore::Op)'''
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
typeId( (SummedAreaOp)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreImage::SummedAreaOp {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (SummedAreaOp)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreImage::SummedAreaOp {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...
    def userData (self, *args, **kwargs):
      '''
userData( (Parameterised)arg1) -> object :

    C++ signature :
        IECore::CompoundObject* userData(IECore::Parameterised {lvalue})'''
    ...

def WarpOp (*args):
      '''

'''      
    ...

class WarpOp:
    def BoundMode (self, *args, **kwargs):
      '''None'''
    ...
    def FilterType (self, *args, **kwargs):
      '''None'''
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
    def collectGarbage (self, *args, **kwargs):
      '''
collectGarbage() -> None :

    C++ signature :
        void collectGarbage()'''
    ...
    def derivedTypeIds (self, *args, **kwargs):
      '''
derivedTypeIds( (TypeId)arg1) -> list :

    C++ signature :
        boost::python::list derivedTypeIds(IECore::TypeId)'''
    ...
    def description (self, *args, **kwargs):
      '''None'''
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
isInstanceOf( (WarpOp)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreImage::WarpOp {lvalue},IECore::TypeId)

isInstanceOf( (WarpOp)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreImage::WarpOp {lvalue},char const*)'''
    ...
    def isSame (self, *args, **kwargs):
      '''
isSame( (RefCounted)arg1, (RefCounted)arg2) -> bool :

    C++ signature :
        bool isSame(IECore::RefCounted const*,IECore::RefCounted const*)'''
    ...
    def numWrappedInstances (self, *args, **kwargs):
      '''
numWrappedInstances() -> int :

    C++ signature :
        unsigned long numWrappedInstances()'''
    ...
    def operate (self, *args, **kwargs):
      '''
operate( (Op)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::Object> operate(IECore::Op {lvalue})

operate( (Op)arg1, (CompoundObject)arg2) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::Object> operate(IECore::Op {lvalue},IECore::CompoundObject const*)'''
    ...
    def parameters (self, *args, **kwargs):
      '''
parameters( (Parameterised)arg1) -> object :

    C++ signature :
        IECore::CompoundParameter* parameters(IECore::Parameterised {lvalue})'''
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
    def resultParameter (self, *args, **kwargs):
      '''
resultParameter( (Op)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::Parameter> resultParameter(IECore::Op)'''
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
typeId( (WarpOp)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreImage::WarpOp {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (WarpOp)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreImage::WarpOp {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...
    def userData (self, *args, **kwargs):
      '''
userData( (Parameterised)arg1) -> object :

    C++ signature :
        IECore::CompoundObject* userData(IECore::Parameterised {lvalue})'''
    ...

def _IECoreImage (*args):
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
