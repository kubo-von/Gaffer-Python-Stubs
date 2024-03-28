
def AddSmoothSkinningInfluencesOp (*args):
      '''
__init__(_object*)

'''      
    ...

class AddSmoothSkinningInfluencesOp:
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
isInstanceOf( (AddSmoothSkinningInfluencesOp)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::AddSmoothSkinningInfluencesOp {lvalue},IECore::TypeId)

isInstanceOf( (AddSmoothSkinningInfluencesOp)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::AddSmoothSkinningInfluencesOp {lvalue},char const*)'''
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
typeId( (AddSmoothSkinningInfluencesOp)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreScene::AddSmoothSkinningInfluencesOp {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (AddSmoothSkinningInfluencesOp)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreScene::AddSmoothSkinningInfluencesOp {lvalue})'''
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

def AttributeBlock (*args):
      '''

'''      
    ...

class AttributeBlock:

def AttributeState (*args):
      '''
__init__(_object*, boost::intrusive_ptr<IECore::CompoundData>)
__init__(_object*)

'''      
    ...

class AttributeState:
    def attributes (self, *args, **kwargs):
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
isInstanceOf( (AttributeState)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::AttributeState {lvalue},IECore::TypeId)

isInstanceOf( (AttributeState)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::AttributeState {lvalue},char const*)'''
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
typeId( (AttributeState)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreScene::AttributeState {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (AttributeState)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreScene::AttributeState {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...

def AttributeStateParameter (*args):
      '''
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > name, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > description, boost::intrusive_ptr<IECoreScene::AttributeState> defaultValue)
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > name, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > description, boost::intrusive_ptr<IECoreScene::AttributeState> defaultValue, boost::python::api::object presets=())
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > name, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > description, boost::intrusive_ptr<IECoreScene::AttributeState> defaultValue, boost::python::api::object presets=(), bool presetsOnly=False)
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > name, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > description, boost::intrusive_ptr<IECoreScene::AttributeState> defaultValue, boost::python::api::object presets=(), bool presetsOnly=False, boost::intrusive_ptr<IECore::CompoundObject> userData=None)

'''      
    ...

class AttributeStateParameter:
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
isInstanceOf( (AttributeStateParameter)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECore::TypedObjectParameter<IECoreScene::AttributeState> {lvalue},IECore::TypeId)

isInstanceOf( (AttributeStateParameter)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECore::TypedObjectParameter<IECoreScene::AttributeState> {lvalue},char const*)'''
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
typeId( (AttributeStateParameter)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECore::TypedObjectParameter<IECoreScene::AttributeState> {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (AttributeStateParameter)arg1) -> str :

    C++ signature :
        char const* typeName(IECore::TypedObjectParameter<IECoreScene::AttributeState> {lvalue})'''
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
valueValid( (AttributeStateParameter)arg1, (object)arg2) -> tuple :
    Returns a tuple containing a bool specifying validity and a string giving a reason for invalidity.

    C++ signature :
        boost::python::tuple valueValid(IECore::TypedObjectParameter<IECoreScene::AttributeState>,boost::intrusive_ptr<IECore::Object const>)

valueValid( (Parameter)arg1) -> tuple :
    Returns a tuple containing a bool specifying validity and a string giving a reason for invalidity.

    C++ signature :
        boost::python::tuple valueValid(IECore::Parameter)'''
    ...

def Camera (*args):
      '''
__init__(_object*)
__init__(_object*, boost::intrusive_ptr<IECore::CompoundData> parameters=IECore.CompoundData())

'''      
    ...

class Camera:
    def Distort (self, *args, **kwargs):
      '''None'''
    ...
    def Fill (self, *args, **kwargs):
      '''None'''
    ...
    def FilmFit (self, *args, **kwargs):
      '''None'''
    ...
    def Fit (self, *args, **kwargs):
      '''None'''
    ...
    def Horizontal (self, *args, **kwargs):
      '''None'''
    ...
    def Vertical (self, *args, **kwargs):
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
    def calculateFieldOfView (self, *args, **kwargs):
      '''
calculateFieldOfView( (Camera)arg1) -> V2f :

    C++ signature :
        Imath_3_1::Vec2<float> calculateFieldOfView(IECoreScene::Camera {lvalue})'''
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
    def fitWindow (self, *args, **kwargs):
      '''
fitWindow( (Box2f)arg1, (FilmFit)arg2, (float)arg3) -> Box2f :

    C++ signature :
        Imath_3_1::Box<Imath_3_1::Vec2<float> > fitWindow(Imath_3_1::Box<Imath_3_1::Vec2<float> >,IECoreScene::Camera::FilmFit,float)'''
    ...
    def frustum (self, *args, **kwargs):
      '''
frustum( (Camera)arg1) -> Box2f :

    C++ signature :
        Imath_3_1::Box<Imath_3_1::Vec2<float> > frustum(IECoreScene::Camera {lvalue})

frustum( (Camera)arg1, (FilmFit)arg2) -> Box2f :

    C++ signature :
        Imath_3_1::Box<Imath_3_1::Vec2<float> > frustum(IECoreScene::Camera {lvalue},IECoreScene::Camera::FilmFit)

frustum( (Camera)arg1, (FilmFit)arg2, (float)arg3) -> Box2f :

    C++ signature :
        Imath_3_1::Box<Imath_3_1::Vec2<float> > frustum(IECoreScene::Camera {lvalue},IECoreScene::Camera::FilmFit,float)'''
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
    def getAperture (self, *args, **kwargs):
      '''
getAperture( (Camera)arg1) -> V2f :

    C++ signature :
        Imath_3_1::Vec2<float> getAperture(IECoreScene::Camera {lvalue})'''
    ...
    def getApertureOffset (self, *args, **kwargs):
      '''
getApertureOffset( (Camera)arg1) -> V2f :

    C++ signature :
        Imath_3_1::Vec2<float> getApertureOffset(IECoreScene::Camera {lvalue})'''
    ...
    def getClippingPlanes (self, *args, **kwargs):
      '''
getClippingPlanes( (Camera)arg1) -> V2f :

    C++ signature :
        Imath_3_1::Vec2<float> getClippingPlanes(IECoreScene::Camera {lvalue})'''
    ...
    def getCropWindow (self, *args, **kwargs):
      '''
getCropWindow( (Camera)arg1) -> Box2f :

    C++ signature :
        Imath_3_1::Box<Imath_3_1::Vec2<float> > getCropWindow(IECoreScene::Camera {lvalue})'''
    ...
    def getFStop (self, *args, **kwargs):
      '''
getFStop( (Camera)arg1) -> float :

    C++ signature :
        float getFStop(IECoreScene::Camera {lvalue})'''
    ...
    def getFilmFit (self, *args, **kwargs):
      '''
getFilmFit( (Camera)arg1) -> FilmFit :

    C++ signature :
        IECoreScene::Camera::FilmFit getFilmFit(IECoreScene::Camera {lvalue})'''
    ...
    def getFocalLength (self, *args, **kwargs):
      '''
getFocalLength( (Camera)arg1) -> float :

    C++ signature :
        float getFocalLength(IECoreScene::Camera {lvalue})'''
    ...
    def getFocalLengthWorldScale (self, *args, **kwargs):
      '''
getFocalLengthWorldScale( (Camera)arg1) -> float :

    C++ signature :
        float getFocalLengthWorldScale(IECoreScene::Camera {lvalue})'''
    ...
    def getFocusDistance (self, *args, **kwargs):
      '''
getFocusDistance( (Camera)arg1) -> float :

    C++ signature :
        float getFocusDistance(IECoreScene::Camera {lvalue})'''
    ...
    def getOverscan (self, *args, **kwargs):
      '''
getOverscan( (Camera)arg1) -> bool :

    C++ signature :
        bool getOverscan(IECoreScene::Camera {lvalue})'''
    ...
    def getOverscanBottom (self, *args, **kwargs):
      '''
getOverscanBottom( (Camera)arg1) -> float :

    C++ signature :
        float getOverscanBottom(IECoreScene::Camera {lvalue})'''
    ...
    def getOverscanLeft (self, *args, **kwargs):
      '''
getOverscanLeft( (Camera)arg1) -> float :

    C++ signature :
        float getOverscanLeft(IECoreScene::Camera {lvalue})'''
    ...
    def getOverscanRight (self, *args, **kwargs):
      '''
getOverscanRight( (Camera)arg1) -> float :

    C++ signature :
        float getOverscanRight(IECoreScene::Camera {lvalue})'''
    ...
    def getOverscanTop (self, *args, **kwargs):
      '''
getOverscanTop( (Camera)arg1) -> float :

    C++ signature :
        float getOverscanTop(IECoreScene::Camera {lvalue})'''
    ...
    def getPixelAspectRatio (self, *args, **kwargs):
      '''
getPixelAspectRatio( (Camera)arg1) -> float :

    C++ signature :
        float getPixelAspectRatio(IECoreScene::Camera {lvalue})'''
    ...
    def getProjection (self, *args, **kwargs):
      '''
getProjection( (Camera)arg1) -> str :

    C++ signature :
        std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > getProjection(IECoreScene::Camera {lvalue})'''
    ...
    def getResolution (self, *args, **kwargs):
      '''
getResolution( (Camera)arg1) -> V2i :

    C++ signature :
        Imath_3_1::Vec2<int> getResolution(IECoreScene::Camera {lvalue})'''
    ...
    def getResolutionMultiplier (self, *args, **kwargs):
      '''
getResolutionMultiplier( (Camera)arg1) -> float :

    C++ signature :
        float getResolutionMultiplier(IECoreScene::Camera {lvalue})'''
    ...
    def getShutter (self, *args, **kwargs):
      '''
getShutter( (Camera)arg1) -> V2f :

    C++ signature :
        Imath_3_1::Vec2<float> getShutter(IECoreScene::Camera {lvalue})'''
    ...
    def hasCropWindow (self, *args, **kwargs):
      '''
hasCropWindow( (Camera)arg1) -> bool :

    C++ signature :
        bool hasCropWindow(IECoreScene::Camera {lvalue})'''
    ...
    def hasFilmFit (self, *args, **kwargs):
      '''
hasFilmFit( (Camera)arg1) -> bool :

    C++ signature :
        bool hasFilmFit(IECoreScene::Camera {lvalue})'''
    ...
    def hasOverscan (self, *args, **kwargs):
      '''
hasOverscan( (Camera)arg1) -> bool :

    C++ signature :
        bool hasOverscan(IECoreScene::Camera {lvalue})'''
    ...
    def hasOverscanBottom (self, *args, **kwargs):
      '''
hasOverscanBottom( (Camera)arg1) -> bool :

    C++ signature :
        bool hasOverscanBottom(IECoreScene::Camera {lvalue})'''
    ...
    def hasOverscanLeft (self, *args, **kwargs):
      '''
hasOverscanLeft( (Camera)arg1) -> bool :

    C++ signature :
        bool hasOverscanLeft(IECoreScene::Camera {lvalue})'''
    ...
    def hasOverscanRight (self, *args, **kwargs):
      '''
hasOverscanRight( (Camera)arg1) -> bool :

    C++ signature :
        bool hasOverscanRight(IECoreScene::Camera {lvalue})'''
    ...
    def hasOverscanTop (self, *args, **kwargs):
      '''
hasOverscanTop( (Camera)arg1) -> bool :

    C++ signature :
        bool hasOverscanTop(IECoreScene::Camera {lvalue})'''
    ...
    def hasPixelAspectRatio (self, *args, **kwargs):
      '''
hasPixelAspectRatio( (Camera)arg1) -> bool :

    C++ signature :
        bool hasPixelAspectRatio(IECoreScene::Camera {lvalue})'''
    ...
    def hasResolution (self, *args, **kwargs):
      '''
hasResolution( (Camera)arg1) -> bool :

    C++ signature :
        bool hasResolution(IECoreScene::Camera {lvalue})'''
    ...
    def hasResolutionMultiplier (self, *args, **kwargs):
      '''
hasResolutionMultiplier( (Camera)arg1) -> bool :

    C++ signature :
        bool hasResolutionMultiplier(IECoreScene::Camera {lvalue})'''
    ...
    def hasShutter (self, *args, **kwargs):
      '''
hasShutter( (Camera)arg1) -> bool :

    C++ signature :
        bool hasShutter(IECoreScene::Camera {lvalue})'''
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
isInstanceOf( (Camera)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::Camera {lvalue},IECore::TypeId)

isInstanceOf( (Camera)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::Camera {lvalue},char const*)'''
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
    def numWrappedInstances (self, *args, **kwargs):
      '''
numWrappedInstances() -> int :

    C++ signature :
        unsigned long numWrappedInstances()'''
    ...
    def parameters (self, *args, **kwargs):
      '''
parameters( (Camera)arg1) -> object :

    C++ signature :
        IECore::CompoundData* parameters(IECoreScene::Camera {lvalue})'''
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
    def removeCropWindow (self, *args, **kwargs):
      '''
removeCropWindow( (Camera)arg1) -> None :

    C++ signature :
        void removeCropWindow(IECoreScene::Camera {lvalue})'''
    ...
    def removeFilmFit (self, *args, **kwargs):
      '''
removeFilmFit( (Camera)arg1) -> None :

    C++ signature :
        void removeFilmFit(IECoreScene::Camera {lvalue})'''
    ...
    def removeOverscan (self, *args, **kwargs):
      '''
removeOverscan( (Camera)arg1) -> None :

    C++ signature :
        void removeOverscan(IECoreScene::Camera {lvalue})'''
    ...
    def removeOverscanBottom (self, *args, **kwargs):
      '''
removeOverscanBottom( (Camera)arg1) -> None :

    C++ signature :
        void removeOverscanBottom(IECoreScene::Camera {lvalue})'''
    ...
    def removeOverscanLeft (self, *args, **kwargs):
      '''
removeOverscanLeft( (Camera)arg1) -> None :

    C++ signature :
        void removeOverscanLeft(IECoreScene::Camera {lvalue})'''
    ...
    def removeOverscanRight (self, *args, **kwargs):
      '''
removeOverscanRight( (Camera)arg1) -> None :

    C++ signature :
        void removeOverscanRight(IECoreScene::Camera {lvalue})'''
    ...
    def removeOverscanTop (self, *args, **kwargs):
      '''
removeOverscanTop( (Camera)arg1) -> None :

    C++ signature :
        void removeOverscanTop(IECoreScene::Camera {lvalue})'''
    ...
    def removePixelAspectRatio (self, *args, **kwargs):
      '''
removePixelAspectRatio( (Camera)arg1) -> None :

    C++ signature :
        void removePixelAspectRatio(IECoreScene::Camera {lvalue})'''
    ...
    def removeResolution (self, *args, **kwargs):
      '''
removeResolution( (Camera)arg1) -> None :

    C++ signature :
        void removeResolution(IECoreScene::Camera {lvalue})'''
    ...
    def removeResolutionMultiplier (self, *args, **kwargs):
      '''
removeResolutionMultiplier( (Camera)arg1) -> None :

    C++ signature :
        void removeResolutionMultiplier(IECoreScene::Camera {lvalue})'''
    ...
    def removeShutter (self, *args, **kwargs):
      '''
removeShutter( (Camera)arg1) -> None :

    C++ signature :
        void removeShutter(IECoreScene::Camera {lvalue})'''
    ...
    def render (self, *args, **kwargs):
      '''
render( (Renderable)arg1, (Renderer)arg2) -> None :

    C++ signature :
        void render(IECoreScene::Renderable,IECoreScene::Renderer*)'''
    ...
    def renderRegion (self, *args, **kwargs):
      '''
renderRegion( (Camera)arg1) -> Box2i :

    C++ signature :
        Imath_3_1::Box<Imath_3_1::Vec2<int> > renderRegion(IECoreScene::Camera {lvalue})'''
    ...
    def renderResolution (self, *args, **kwargs):
      '''
renderResolution( (Camera)arg1) -> V2i :

    C++ signature :
        Imath_3_1::Vec2<int> renderResolution(IECoreScene::Camera {lvalue})'''
    ...
    def save (self, *args, **kwargs):
      '''
save( (Object)arg1, (object)arg2, (InternedString)arg3) -> None :

    C++ signature :
        void save(IECore::Object {lvalue},boost::intrusive_ptr<IECore::IndexedIO>,IECore::InternedString)'''
    ...
    def setAperture (self, *args, **kwargs):
      '''
setAperture( (Camera)arg1, (V2f)arg2) -> None :

    C++ signature :
        void setAperture(IECoreScene::Camera {lvalue},Imath_3_1::Vec2<float>)'''
    ...
    def setApertureOffset (self, *args, **kwargs):
      '''
setApertureOffset( (Camera)arg1, (V2f)arg2) -> None :

    C++ signature :
        void setApertureOffset(IECoreScene::Camera {lvalue},Imath_3_1::Vec2<float>)'''
    ...
    def setClippingPlanes (self, *args, **kwargs):
      '''
setClippingPlanes( (Camera)arg1, (V2f)arg2) -> None :

    C++ signature :
        void setClippingPlanes(IECoreScene::Camera {lvalue},Imath_3_1::Vec2<float>)'''
    ...
    def setCropWindow (self, *args, **kwargs):
      '''
setCropWindow( (Camera)arg1, (Box2f)arg2) -> None :

    C++ signature :
        void setCropWindow(IECoreScene::Camera {lvalue},Imath_3_1::Box<Imath_3_1::Vec2<float> >)'''
    ...
    def setFStop (self, *args, **kwargs):
      '''
setFStop( (Camera)arg1, (float)arg2) -> None :

    C++ signature :
        void setFStop(IECoreScene::Camera {lvalue},float)'''
    ...
    def setFilmFit (self, *args, **kwargs):
      '''
setFilmFit( (Camera)arg1, (FilmFit)arg2) -> None :

    C++ signature :
        void setFilmFit(IECoreScene::Camera {lvalue},IECoreScene::Camera::FilmFit)'''
    ...
    def setFocalLength (self, *args, **kwargs):
      '''
setFocalLength( (Camera)arg1, (float)arg2) -> None :

    C++ signature :
        void setFocalLength(IECoreScene::Camera {lvalue},float)'''
    ...
    def setFocalLengthFromFieldOfView (self, *args, **kwargs):
      '''
setFocalLengthFromFieldOfView( (Camera)arg1, (float)arg2) -> None :

    C++ signature :
        void setFocalLengthFromFieldOfView(IECoreScene::Camera {lvalue},float)'''
    ...
    def setFocalLengthWorldScale (self, *args, **kwargs):
      '''
setFocalLengthWorldScale( (Camera)arg1, (float)arg2) -> None :

    C++ signature :
        void setFocalLengthWorldScale(IECoreScene::Camera {lvalue},float)'''
    ...
    def setFocusDistance (self, *args, **kwargs):
      '''
setFocusDistance( (Camera)arg1, (float)arg2) -> None :

    C++ signature :
        void setFocusDistance(IECoreScene::Camera {lvalue},float)'''
    ...
    def setOverscan (self, *args, **kwargs):
      '''
setOverscan( (Camera)arg1, (bool)arg2) -> None :

    C++ signature :
        void setOverscan(IECoreScene::Camera {lvalue},bool)'''
    ...
    def setOverscanBottom (self, *args, **kwargs):
      '''
setOverscanBottom( (Camera)arg1, (float)arg2) -> None :

    C++ signature :
        void setOverscanBottom(IECoreScene::Camera {lvalue},float)'''
    ...
    def setOverscanLeft (self, *args, **kwargs):
      '''
setOverscanLeft( (Camera)arg1, (float)arg2) -> None :

    C++ signature :
        void setOverscanLeft(IECoreScene::Camera {lvalue},float)'''
    ...
    def setOverscanRight (self, *args, **kwargs):
      '''
setOverscanRight( (Camera)arg1, (float)arg2) -> None :

    C++ signature :
        void setOverscanRight(IECoreScene::Camera {lvalue},float)'''
    ...
    def setOverscanTop (self, *args, **kwargs):
      '''
setOverscanTop( (Camera)arg1, (float)arg2) -> None :

    C++ signature :
        void setOverscanTop(IECoreScene::Camera {lvalue},float)'''
    ...
    def setPixelAspectRatio (self, *args, **kwargs):
      '''
setPixelAspectRatio( (Camera)arg1, (float)arg2) -> None :

    C++ signature :
        void setPixelAspectRatio(IECoreScene::Camera {lvalue},float)'''
    ...
    def setProjection (self, *args, **kwargs):
      '''
setProjection( (Camera)arg1, (object)arg2) -> None :

    C++ signature :
        void setProjection(IECoreScene::Camera {lvalue},std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)'''
    ...
    def setResolution (self, *args, **kwargs):
      '''
setResolution( (Camera)arg1, (V2i)arg2) -> None :

    C++ signature :
        void setResolution(IECoreScene::Camera {lvalue},Imath_3_1::Vec2<int>)'''
    ...
    def setResolutionMultiplier (self, *args, **kwargs):
      '''
setResolutionMultiplier( (Camera)arg1, (float)arg2) -> None :

    C++ signature :
        void setResolutionMultiplier(IECoreScene::Camera {lvalue},float)'''
    ...
    def setShutter (self, *args, **kwargs):
      '''
setShutter( (Camera)arg1, (V2f)arg2) -> None :

    C++ signature :
        void setShutter(IECoreScene::Camera {lvalue},Imath_3_1::Vec2<float>)'''
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
typeId( (Camera)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreScene::Camera {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (Camera)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreScene::Camera {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...

def ClippingPlane (*args):
      '''
__init__(_object*)

'''      
    ...

class ClippingPlane:
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
isInstanceOf( (ClippingPlane)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::ClippingPlane {lvalue},IECore::TypeId)

isInstanceOf( (ClippingPlane)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::ClippingPlane {lvalue},char const*)'''
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
typeId( (ClippingPlane)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreScene::ClippingPlane {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (ClippingPlane)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreScene::ClippingPlane {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...

def CompressSmoothSkinningDataOp (*args):
      '''
__init__(_object*)

'''      
    ...

class CompressSmoothSkinningDataOp:
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
isInstanceOf( (CompressSmoothSkinningDataOp)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::CompressSmoothSkinningDataOp {lvalue},IECore::TypeId)

isInstanceOf( (CompressSmoothSkinningDataOp)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::CompressSmoothSkinningDataOp {lvalue},char const*)'''
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
typeId( (CompressSmoothSkinningDataOp)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreScene::CompressSmoothSkinningDataOp {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (CompressSmoothSkinningDataOp)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreScene::CompressSmoothSkinningDataOp {lvalue})'''
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

def ContrastSmoothSkinningWeightsOp (*args):
      '''
__init__(_object*)

'''      
    ...

class ContrastSmoothSkinningWeightsOp:
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
isInstanceOf( (ContrastSmoothSkinningWeightsOp)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::ContrastSmoothSkinningWeightsOp {lvalue},IECore::TypeId)

isInstanceOf( (ContrastSmoothSkinningWeightsOp)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::ContrastSmoothSkinningWeightsOp {lvalue},char const*)'''
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
typeId( (ContrastSmoothSkinningWeightsOp)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreScene::ContrastSmoothSkinningWeightsOp {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (ContrastSmoothSkinningWeightsOp)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreScene::ContrastSmoothSkinningWeightsOp {lvalue})'''
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

def CoordinateSystem (*args):
      '''
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, boost::intrusive_ptr<IECoreScene::Transform>)
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)
__init__(_object*)

'''      
    ...

class CoordinateSystem:
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
    def getName (self, *args, **kwargs):
      '''
getName( (CoordinateSystem)arg1) -> str :

    C++ signature :
        std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > getName(IECoreScene::CoordinateSystem {lvalue})'''
    ...
    def getTransform (self, *args, **kwargs):
      '''
getTransform( (CoordinateSystem)arg1) -> object :

    C++ signature :
        IECoreScene::Transform* getTransform(IECoreScene::CoordinateSystem {lvalue})'''
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
isInstanceOf( (CoordinateSystem)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::CoordinateSystem {lvalue},IECore::TypeId)

isInstanceOf( (CoordinateSystem)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::CoordinateSystem {lvalue},char const*)'''
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
    def setName (self, *args, **kwargs):
      '''
setName( (CoordinateSystem)arg1, (object)arg2) -> None :

    C++ signature :
        void setName(IECoreScene::CoordinateSystem {lvalue},std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)'''
    ...
    def setTransform (self, *args, **kwargs):
      '''
setTransform( (CoordinateSystem)arg1, (object)arg2) -> None :

    C++ signature :
        void setTransform(IECoreScene::CoordinateSystem {lvalue},boost::intrusive_ptr<IECoreScene::Transform>)'''
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
typeId( (CoordinateSystem)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreScene::CoordinateSystem {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (CoordinateSystem)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreScene::CoordinateSystem {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...

def CurveExtrudeOp (*args):
      '''
__init__(_object*)

'''      
    ...

class CurveExtrudeOp:
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
isInstanceOf( (CurveExtrudeOp)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::CurveExtrudeOp {lvalue},IECore::TypeId)

isInstanceOf( (CurveExtrudeOp)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::CurveExtrudeOp {lvalue},char const*)'''
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
typeId( (CurveExtrudeOp)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreScene::CurveExtrudeOp {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (CurveExtrudeOp)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreScene::CurveExtrudeOp {lvalue})'''
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

def CurveLineariser (*args):
      '''
__init__(_object*)

'''      
    ...

class CurveLineariser:
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
isInstanceOf( (CurveLineariser)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::CurveLineariser {lvalue},IECore::TypeId)

isInstanceOf( (CurveLineariser)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::CurveLineariser {lvalue},char const*)'''
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
typeId( (CurveLineariser)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreScene::CurveLineariser {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (CurveLineariser)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreScene::CurveLineariser {lvalue})'''
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

def CurveTangentsOp (*args):
      '''
__init__(_object*)

'''      
    ...

class CurveTangentsOp:
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
isInstanceOf( (CurveTangentsOp)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::CurveTangentsOp {lvalue},IECore::TypeId)

isInstanceOf( (CurveTangentsOp)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::CurveTangentsOp {lvalue},char const*)'''
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
typeId( (CurveTangentsOp)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreScene::CurveTangentsOp {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (CurveTangentsOp)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreScene::CurveTangentsOp {lvalue})'''
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

def CurvesAlgo (*args):
      '''

'''      
    ...

def CurvesMergeOp (*args):
      '''
__init__(_object*)

'''      
    ...

class CurvesMergeOp:
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
isInstanceOf( (CurvesMergeOp)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::CurvesMergeOp {lvalue},IECore::TypeId)

isInstanceOf( (CurvesMergeOp)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::CurvesMergeOp {lvalue},char const*)'''
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
typeId( (CurvesMergeOp)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreScene::CurvesMergeOp {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (CurvesMergeOp)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreScene::CurvesMergeOp {lvalue})'''
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

def CurvesPrimitive (*args):
      '''
__init__(_object*, boost::intrusive_ptr<IECore::TypedData<std::vector<int, std::allocator<int> > > > verticesPerCurve, IECore::CubicBasis<float> basis=IECore.CubicBasisf( imath.M44f( 0, 0, 0, 0, 0, 0, 0, 0, -1, 1, 0, 0, 1, 0, 0, 0 ), 1 ), bool periodic=False, boost::intrusive_ptr<IECore::GeometricTypedData<std::vector<Imath_3_1::Vec3<float>, std::allocator<Imath_3_1::Vec3<float> > > > const> p=None)
__init__(_object*)

'''      
    ...

class CurvesPrimitive:
    def arePrimitiveVariablesValid (self, *args, **kwargs):
      '''
arePrimitiveVariablesValid( (Primitive)arg1) -> bool :

    C++ signature :
        bool arePrimitiveVariablesValid(IECoreScene::Primitive {lvalue})'''
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
    def basis (self, *args, **kwargs):
      '''
basis( (CurvesPrimitive)arg1) -> CubicBasisf :

    C++ signature :
        IECore::CubicBasis<float> basis(IECoreScene::CurvesPrimitive {lvalue})'''
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
    def createBox (self, *args, **kwargs):
      '''
createBox( (Box3f)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECoreScene::CurvesPrimitive> createBox(Imath_3_1::Box<Imath_3_1::Vec3<float> >)'''
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
    def hash (self, *args, **kwargs):
      '''
hash( (Object)arg1) -> MurmurHash :

    C++ signature :
        IECore::MurmurHash hash(IECore::Object {lvalue})

hash( (Object)arg1, (MurmurHash)arg2) -> None :

    C++ signature :
        void hash(IECore::Object {lvalue},IECore::MurmurHash {lvalue})'''
    ...
    def inferInterpolation (self, *args, **kwargs):
      '''
inferInterpolation( (Primitive)arg1, (Data)arg2) -> Interpolation :

    C++ signature :
        IECoreScene::PrimitiveVariable::Interpolation inferInterpolation(IECoreScene::Primitive {lvalue},IECore::Data const*)

inferInterpolation( (Primitive)arg1, (int)arg2) -> Interpolation :

    C++ signature :
        IECoreScene::PrimitiveVariable::Interpolation inferInterpolation(IECoreScene::Primitive {lvalue},unsigned long)'''
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
isInstanceOf( (CurvesPrimitive)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::CurvesPrimitive {lvalue},IECore::TypeId)

isInstanceOf( (CurvesPrimitive)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::CurvesPrimitive {lvalue},char const*)'''
    ...
    def isPrimitiveVariableValid (self, *args, **kwargs):
      '''
isPrimitiveVariableValid( (Primitive)arg1, (PrimitiveVariable)arg2) -> bool :

    C++ signature :
        bool isPrimitiveVariableValid(IECoreScene::Primitive {lvalue},IECoreScene::PrimitiveVariable)'''
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
keys( (Primitive)arg1) -> list :

    C++ signature :
        boost::python::list keys(IECoreScene::Primitive {lvalue})'''
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
    def numCurves (self, *args, **kwargs):
      '''
numCurves( (CurvesPrimitive)arg1) -> int :

    C++ signature :
        unsigned long numCurves(IECoreScene::CurvesPrimitive {lvalue})'''
    ...
    def numSegments (self, *args, **kwargs):
      '''
numSegments( (CurvesPrimitive)arg1, (int)arg2) -> int :

    C++ signature :
        unsigned int numSegments(IECoreScene::CurvesPrimitive {lvalue},unsigned int)'''
    ...
    def numWrappedInstances (self, *args, **kwargs):
      '''
numWrappedInstances() -> int :

    C++ signature :
        unsigned long numWrappedInstances()'''
    ...
    def periodic (self, *args, **kwargs):
      '''
periodic( (CurvesPrimitive)arg1) -> bool :

    C++ signature :
        bool periodic(IECoreScene::CurvesPrimitive {lvalue})'''
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
    def setTopology (self, *args, **kwargs):
      '''
setTopology( (CurvesPrimitive)arg1, (object)arg2, (CubicBasisf)arg3, (bool)arg4) -> None :

    C++ signature :
        void setTopology(IECoreScene::CurvesPrimitive {lvalue},boost::intrusive_ptr<IECore::TypedData<std::vector<int, std::allocator<int> > > const>,IECore::CubicBasis<float>,bool)'''
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
    def topologyHash (self, *args, **kwargs):
      '''
topologyHash( (Primitive)arg1) -> MurmurHash :

    C++ signature :
        IECore::MurmurHash topologyHash(IECoreScene::Primitive {lvalue})

topologyHash( (Primitive)arg1, (MurmurHash)arg2) -> None :

    C++ signature :
        void topologyHash(IECoreScene::Primitive {lvalue},IECore::MurmurHash {lvalue})'''
    ...
    def typeId (self, *args, **kwargs):
      '''
typeId( (CurvesPrimitive)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreScene::CurvesPrimitive {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (CurvesPrimitive)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreScene::CurvesPrimitive {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...
    def values (self, *args, **kwargs):
      '''
values( (Primitive)arg1) -> list :
    Returns a list containing shallow copies of the PrimitiveVariable objects held.

    C++ signature :
        boost::python::list values(IECoreScene::Primitive {lvalue})'''
    ...
    def variableSize (self, *args, **kwargs):
      '''
variableSize( (CurvesPrimitive)arg1, (Interpolation)arg2) -> int :

    C++ signature :
        unsigned long variableSize(IECoreScene::CurvesPrimitive {lvalue},IECoreScene::PrimitiveVariable::Interpolation)

variableSize( (CurvesPrimitive)arg1, (Interpolation)arg2, (int)arg3) -> int :

    C++ signature :
        unsigned long variableSize(IECoreScene::CurvesPrimitive {lvalue},IECoreScene::PrimitiveVariable::Interpolation,unsigned int)'''
    ...
    def verticesPerCurve (self, *args, **kwargs):
      '''
verticesPerCurve( (CurvesPrimitive)arg1) -> object :
    A copy of the list of vertices per curve.

    C++ signature :
        boost::intrusive_ptr<IECore::TypedData<std::vector<int, std::allocator<int> > > > verticesPerCurve(IECoreScene::CurvesPrimitive)'''
    ...

def CurvesPrimitiveEvaluator (*args):
      '''
__init__(_object*, boost::intrusive_ptr<IECoreScene::CurvesPrimitive>)

'''      
    ...

class CurvesPrimitiveEvaluator:
    def Result (self, *args, **kwargs):
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
    def centerOfGravity (self, *args, **kwargs):
      '''
centerOfGravity( (PrimitiveEvaluator)arg1) -> V3f :

    C++ signature :
        Imath_3_1::Vec3<float> centerOfGravity(IECoreScene::PrimitiveEvaluator {lvalue})'''
    ...
    def closestPoint (self, *args, **kwargs):
      '''
closestPoint( (PrimitiveEvaluator)arg1, (V3f)arg2, (Result)arg3) -> bool :

    C++ signature :
        bool closestPoint(IECoreScene::PrimitiveEvaluator {lvalue},Imath_3_1::Vec3<float>,IECoreScene::PrimitiveEvaluator::Result*)'''
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
        boost::intrusive_ptr<IECoreScene::PrimitiveEvaluator> create(boost::intrusive_ptr<IECoreScene::Primitive>)'''
    ...
    def createResult (self, *args, **kwargs):
      '''
createResult( (PrimitiveEvaluator)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECoreScene::PrimitiveEvaluator::Result> createResult(IECoreScene::PrimitiveEvaluator {lvalue})'''
    ...
    def curveLength (self, *args, **kwargs):
      '''
curveLength( (CurvesPrimitiveEvaluator)arg1, (int)curveIndex [, (float)vStart=0.0 [, (float)vEnd=1.0]]) -> float :

    C++ signature :
        float curveLength(IECoreScene::CurvesPrimitiveEvaluator {lvalue},unsigned int [,float=0.0 [,float=1.0]])'''
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
    def intersectionPoint (self, *args, **kwargs):
      '''
intersectionPoint( (PrimitiveEvaluator)arg1, (V3f)arg2, (V3f)arg3, (Result)arg4) -> bool :

    C++ signature :
        bool intersectionPoint(IECoreScene::PrimitiveEvaluator {lvalue},Imath_3_1::Vec3<float>,Imath_3_1::Vec3<float>,IECoreScene::PrimitiveEvaluator::Result*)

intersectionPoint( (PrimitiveEvaluator)arg1, (V3f)arg2, (V3f)arg3, (Result)arg4, (float)arg5) -> bool :

    C++ signature :
        bool intersectionPoint(IECoreScene::PrimitiveEvaluator {lvalue},Imath_3_1::Vec3<float>,Imath_3_1::Vec3<float>,IECoreScene::PrimitiveEvaluator::Result*,float)'''
    ...
    def intersectionPoints (self, *args, **kwargs):
      '''
intersectionPoints( (PrimitiveEvaluator)arg1, (V3f)arg2, (V3f)arg3) -> list :

    C++ signature :
        boost::python::list intersectionPoints(IECoreScene::PrimitiveEvaluator {lvalue},Imath_3_1::Vec3<float>,Imath_3_1::Vec3<float>)

intersectionPoints( (PrimitiveEvaluator)arg1, (V3f)arg2, (V3f)arg3, (float)arg4) -> list :

    C++ signature :
        boost::python::list intersectionPoints(IECoreScene::PrimitiveEvaluator {lvalue},Imath_3_1::Vec3<float>,Imath_3_1::Vec3<float>,float)'''
    ...
    def isInstanceOf (self, *args, **kwargs):
      '''
isInstanceOf( (CurvesPrimitiveEvaluator)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::CurvesPrimitiveEvaluator {lvalue},IECore::TypeId)

isInstanceOf( (CurvesPrimitiveEvaluator)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::CurvesPrimitiveEvaluator {lvalue},char const*)'''
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
    def pointAtUV (self, *args, **kwargs):
      '''
pointAtUV( (PrimitiveEvaluator)arg1, (V2f)arg2, (Result)arg3) -> bool :

    C++ signature :
        bool pointAtUV(IECoreScene::PrimitiveEvaluator {lvalue},Imath_3_1::Vec2<float>,IECoreScene::PrimitiveEvaluator::Result*)'''
    ...
    def pointAtV (self, *args, **kwargs):
      '''
pointAtV( (CurvesPrimitiveEvaluator)arg1, (int)arg2, (float)arg3, (Result)arg4) -> bool :

    C++ signature :
        bool pointAtV(IECoreScene::CurvesPrimitiveEvaluator,unsigned int,float,IECoreScene::PrimitiveEvaluator::Result*)'''
    ...
    def primitive (self, *args, **kwargs):
      '''
primitive( (PrimitiveEvaluator)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECoreScene::Primitive> primitive(IECoreScene::PrimitiveEvaluator {lvalue})'''
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
    def signedDistance (self, *args, **kwargs):
      '''
signedDistance( (PrimitiveEvaluator)arg1, (V3f)arg2, (Result)arg3) -> float :

    C++ signature :
        float signedDistance(IECoreScene::PrimitiveEvaluator {lvalue},Imath_3_1::Vec3<float>,IECoreScene::PrimitiveEvaluator::Result*)'''
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
    def surfaceArea (self, *args, **kwargs):
      '''
surfaceArea( (PrimitiveEvaluator)arg1) -> float :

    C++ signature :
        float surfaceArea(IECoreScene::PrimitiveEvaluator {lvalue})'''
    ...
    def typeId (self, *args, **kwargs):
      '''
typeId( (CurvesPrimitiveEvaluator)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreScene::CurvesPrimitiveEvaluator {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (CurvesPrimitiveEvaluator)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreScene::CurvesPrimitiveEvaluator {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...
    def validateResult (self, *args, **kwargs):
      '''
validateResult( (PrimitiveEvaluator)arg1, (Result)arg2) -> None :

    C++ signature :
        void validateResult(IECoreScene::PrimitiveEvaluator {lvalue},IECoreScene::PrimitiveEvaluator::Result*)'''
    ...
    def varyingDataOffsets (self, *args, **kwargs):
      '''
varyingDataOffsets( (CurvesPrimitiveEvaluator)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::TypedData<std::vector<int, std::allocator<int> > > > varyingDataOffsets(IECoreScene::CurvesPrimitiveEvaluator)'''
    ...
    def vertexDataOffsets (self, *args, **kwargs):
      '''
vertexDataOffsets( (CurvesPrimitiveEvaluator)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::TypedData<std::vector<int, std::allocator<int> > > > vertexDataOffsets(IECoreScene::CurvesPrimitiveEvaluator)'''
    ...
    def verticesPerCurve (self, *args, **kwargs):
      '''
verticesPerCurve( (CurvesPrimitiveEvaluator)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::TypedData<std::vector<int, std::allocator<int> > > > verticesPerCurve(IECoreScene::CurvesPrimitiveEvaluator)'''
    ...
    def volume (self, *args, **kwargs):
      '''
volume( (PrimitiveEvaluator)arg1) -> float :

    C++ signature :
        float volume(IECoreScene::PrimitiveEvaluator {lvalue})'''
    ...

def CurvesPrimitiveOp (*args):
      '''
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)

'''      
    ...

class CurvesPrimitiveOp:
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
isInstanceOf( (CurvesPrimitiveOp)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::TypedPrimitiveOp<IECoreScene::CurvesPrimitive> {lvalue},IECore::TypeId)

isInstanceOf( (CurvesPrimitiveOp)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::TypedPrimitiveOp<IECoreScene::CurvesPrimitive> {lvalue},char const*)'''
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
typeId( (CurvesPrimitiveOp)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreScene::TypedPrimitiveOp<IECoreScene::CurvesPrimitive> {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (CurvesPrimitiveOp)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreScene::TypedPrimitiveOp<IECoreScene::CurvesPrimitive> {lvalue})'''
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

def CurvesPrimitiveParameter (*args):
      '''
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > name, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > description, boost::intrusive_ptr<IECoreScene::CurvesPrimitive> defaultValue)
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > name, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > description, boost::intrusive_ptr<IECoreScene::CurvesPrimitive> defaultValue, boost::python::api::object presets=())
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > name, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > description, boost::intrusive_ptr<IECoreScene::CurvesPrimitive> defaultValue, boost::python::api::object presets=(), bool presetsOnly=False)
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > name, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > description, boost::intrusive_ptr<IECoreScene::CurvesPrimitive> defaultValue, boost::python::api::object presets=(), bool presetsOnly=False, boost::intrusive_ptr<IECore::CompoundObject> userData=None)

'''      
    ...

class CurvesPrimitiveParameter:
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
isInstanceOf( (CurvesPrimitiveParameter)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECore::TypedObjectParameter<IECoreScene::CurvesPrimitive> {lvalue},IECore::TypeId)

isInstanceOf( (CurvesPrimitiveParameter)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECore::TypedObjectParameter<IECoreScene::CurvesPrimitive> {lvalue},char const*)'''
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
typeId( (CurvesPrimitiveParameter)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECore::TypedObjectParameter<IECoreScene::CurvesPrimitive> {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (CurvesPrimitiveParameter)arg1) -> str :

    C++ signature :
        char const* typeName(IECore::TypedObjectParameter<IECoreScene::CurvesPrimitive> {lvalue})'''
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
valueValid( (CurvesPrimitiveParameter)arg1, (object)arg2) -> tuple :
    Returns a tuple containing a bool specifying validity and a string giving a reason for invalidity.

    C++ signature :
        boost::python::tuple valueValid(IECore::TypedObjectParameter<IECoreScene::CurvesPrimitive>,boost::intrusive_ptr<IECore::Object const>)

valueValid( (Parameter)arg1) -> tuple :
    Returns a tuple containing a bool specifying validity and a string giving a reason for invalidity.

    C++ signature :
        boost::python::tuple valueValid(IECore::Parameter)'''
    ...

def DecompressSmoothSkinningDataOp (*args):
      '''
__init__(_object*)

'''      
    ...

class DecompressSmoothSkinningDataOp:
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
isInstanceOf( (DecompressSmoothSkinningDataOp)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::DecompressSmoothSkinningDataOp {lvalue},IECore::TypeId)

isInstanceOf( (DecompressSmoothSkinningDataOp)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::DecompressSmoothSkinningDataOp {lvalue},char const*)'''
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
typeId( (DecompressSmoothSkinningDataOp)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreScene::DecompressSmoothSkinningDataOp {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (DecompressSmoothSkinningDataOp)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreScene::DecompressSmoothSkinningDataOp {lvalue})'''
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

def DiskPrimitive (*args):
      '''
__init__(_object*)
__init__(_object*, float)
__init__(_object*, float, float)
__init__(_object*, float, float, float)

'''      
    ...

class DiskPrimitive:
    def arePrimitiveVariablesValid (self, *args, **kwargs):
      '''
arePrimitiveVariablesValid( (Primitive)arg1) -> bool :

    C++ signature :
        bool arePrimitiveVariablesValid(IECoreScene::Primitive {lvalue})'''
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
    def getRadius (self, *args, **kwargs):
      '''
getRadius( (DiskPrimitive)arg1) -> float :

    C++ signature :
        float getRadius(IECoreScene::DiskPrimitive {lvalue})'''
    ...
    def getThetaMax (self, *args, **kwargs):
      '''
getThetaMax( (DiskPrimitive)arg1) -> float :

    C++ signature :
        float getThetaMax(IECoreScene::DiskPrimitive {lvalue})'''
    ...
    def getZ (self, *args, **kwargs):
      '''
getZ( (DiskPrimitive)arg1) -> float :

    C++ signature :
        float getZ(IECoreScene::DiskPrimitive {lvalue})'''
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
    def inferInterpolation (self, *args, **kwargs):
      '''
inferInterpolation( (Primitive)arg1, (Data)arg2) -> Interpolation :

    C++ signature :
        IECoreScene::PrimitiveVariable::Interpolation inferInterpolation(IECoreScene::Primitive {lvalue},IECore::Data const*)

inferInterpolation( (Primitive)arg1, (int)arg2) -> Interpolation :

    C++ signature :
        IECoreScene::PrimitiveVariable::Interpolation inferInterpolation(IECoreScene::Primitive {lvalue},unsigned long)'''
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
isInstanceOf( (DiskPrimitive)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::DiskPrimitive {lvalue},IECore::TypeId)

isInstanceOf( (DiskPrimitive)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::DiskPrimitive {lvalue},char const*)'''
    ...
    def isPrimitiveVariableValid (self, *args, **kwargs):
      '''
isPrimitiveVariableValid( (Primitive)arg1, (PrimitiveVariable)arg2) -> bool :

    C++ signature :
        bool isPrimitiveVariableValid(IECoreScene::Primitive {lvalue},IECoreScene::PrimitiveVariable)'''
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
keys( (Primitive)arg1) -> list :

    C++ signature :
        boost::python::list keys(IECoreScene::Primitive {lvalue})'''
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
    def setRadius (self, *args, **kwargs):
      '''
setRadius( (DiskPrimitive)arg1, (float)arg2) -> None :

    C++ signature :
        void setRadius(IECoreScene::DiskPrimitive {lvalue},float)'''
    ...
    def setThetaMax (self, *args, **kwargs):
      '''
setThetaMax( (DiskPrimitive)arg1, (float)arg2) -> None :

    C++ signature :
        void setThetaMax(IECoreScene::DiskPrimitive {lvalue},float)'''
    ...
    def setZ (self, *args, **kwargs):
      '''
setZ( (DiskPrimitive)arg1, (float)arg2) -> None :

    C++ signature :
        void setZ(IECoreScene::DiskPrimitive {lvalue},float)'''
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
    def topologyHash (self, *args, **kwargs):
      '''
topologyHash( (Primitive)arg1) -> MurmurHash :

    C++ signature :
        IECore::MurmurHash topologyHash(IECoreScene::Primitive {lvalue})

topologyHash( (Primitive)arg1, (MurmurHash)arg2) -> None :

    C++ signature :
        void topologyHash(IECoreScene::Primitive {lvalue},IECore::MurmurHash {lvalue})'''
    ...
    def typeId (self, *args, **kwargs):
      '''
typeId( (DiskPrimitive)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreScene::DiskPrimitive {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (DiskPrimitive)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreScene::DiskPrimitive {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...
    def values (self, *args, **kwargs):
      '''
values( (Primitive)arg1) -> list :
    Returns a list containing shallow copies of the PrimitiveVariable objects held.

    C++ signature :
        boost::python::list values(IECoreScene::Primitive {lvalue})'''
    ...
    def variableSize (self, *args, **kwargs):
      '''
variableSize( (Primitive)arg1, (Interpolation)arg2) -> int :

    C++ signature :
        unsigned long variableSize(IECoreScene::Primitive {lvalue},IECoreScene::PrimitiveVariable::Interpolation)'''
    ...

def EditBlock (*args):
      '''

'''      
    ...

class EditBlock:

def ExternalProcedural (*args):
      '''
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > fileName='', Imath_3_1::Box<Imath_3_1::Vec3<float> > bound=Box3f(V3f(3.40282347e+38, 3.40282347e+38, 3.40282347e+38), V3f(-3.40282347e+38, -3.40282347e+38, -3.40282347e+38)), IECore::CompoundData const* parameters=None)

'''      
    ...

class ExternalProcedural:
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
    def getBound (self, *args, **kwargs):
      '''
getBound( (ExternalProcedural)arg1) -> Box3f :

    C++ signature :
        Imath_3_1::Box<Imath_3_1::Vec3<float> > getBound(IECoreScene::ExternalProcedural {lvalue})'''
    ...
    def getFileName (self, *args, **kwargs):
      '''
getFileName( (ExternalProcedural)arg1) -> str :

    C++ signature :
        std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > getFileName(IECoreScene::ExternalProcedural {lvalue})'''
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
isInstanceOf( (ExternalProcedural)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::ExternalProcedural {lvalue},IECore::TypeId)

isInstanceOf( (ExternalProcedural)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::ExternalProcedural {lvalue},char const*)'''
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
    def numWrappedInstances (self, *args, **kwargs):
      '''
numWrappedInstances() -> int :

    C++ signature :
        unsigned long numWrappedInstances()'''
    ...
    def parameters (self, *args, **kwargs):
      '''
parameters( (ExternalProcedural)arg1) -> object :

    C++ signature :
        IECore::CompoundData* parameters(IECoreScene::ExternalProcedural {lvalue})'''
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
    def setBound (self, *args, **kwargs):
      '''
setBound( (ExternalProcedural)arg1, (Box3f)arg2) -> None :

    C++ signature :
        void setBound(IECoreScene::ExternalProcedural {lvalue},Imath_3_1::Box<Imath_3_1::Vec3<float> >)'''
    ...
    def setFileName (self, *args, **kwargs):
      '''
setFileName( (ExternalProcedural)arg1, (object)arg2) -> None :

    C++ signature :
        void setFileName(IECoreScene::ExternalProcedural {lvalue},std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)'''
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
typeId( (ExternalProcedural)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreScene::ExternalProcedural {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (ExternalProcedural)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreScene::ExternalProcedural {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...

def FaceVaryingPromotionOp (*args):
      '''
__init__(_object*)

'''      
    ...

class FaceVaryingPromotionOp:
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
isInstanceOf( (FaceVaryingPromotionOp)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::FaceVaryingPromotionOp {lvalue},IECore::TypeId)

isInstanceOf( (FaceVaryingPromotionOp)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::FaceVaryingPromotionOp {lvalue},char const*)'''
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
typeId( (FaceVaryingPromotionOp)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreScene::FaceVaryingPromotionOp {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (FaceVaryingPromotionOp)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreScene::FaceVaryingPromotionOp {lvalue})'''
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
    def advance (self, *args, **kwargs):
      '''
advance( (Font)arg1, (str)arg2, (str)arg3) -> V2f :

    C++ signature :
        Imath_3_1::Vec2<float> advance(IECoreScene::Font {lvalue},char,char)'''
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
    def bound (self, *args, **kwargs):
      '''
bound( (Font)arg1) -> Box2f :

    C++ signature :
        Imath_3_1::Box<Imath_3_1::Vec2<float> > bound(IECoreScene::Font {lvalue})

bound( (Font)arg1, (str)arg2) -> Box2f :

    C++ signature :
        Imath_3_1::Box<Imath_3_1::Vec2<float> > bound(IECoreScene::Font {lvalue},char)

bound( (Font)arg1, (object)arg2) -> Box2f :

    C++ signature :
        Imath_3_1::Box<Imath_3_1::Vec2<float> > bound(IECoreScene::Font {lvalue},std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)'''
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
        std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > fileName(IECoreScene::Font {lvalue})'''
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
    def getCurveTolerance (self, *args, **kwargs):
      '''
getCurveTolerance( (Font)arg1) -> float :

    C++ signature :
        float getCurveTolerance(IECoreScene::Font {lvalue})'''
    ...
    def getKerning (self, *args, **kwargs):
      '''
getKerning( (Font)arg1) -> float :

    C++ signature :
        float getKerning(IECoreScene::Font {lvalue})'''
    ...
    def getLineSpacing (self, *args, **kwargs):
      '''
getLineSpacing( (Font)arg1) -> float :

    C++ signature :
        float getLineSpacing(IECoreScene::Font {lvalue})'''
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
        bool isInstanceOf(IECoreScene::Font {lvalue},IECore::TypeId)

isInstanceOf( (Font)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::Font {lvalue},char const*)'''
    ...
    def isSame (self, *args, **kwargs):
      '''
isSame( (RefCounted)arg1, (RefCounted)arg2) -> bool :

    C++ signature :
        bool isSame(IECore::RefCounted const*,IECore::RefCounted const*)'''
    ...
    def mesh (self, *args, **kwargs):
      '''
mesh( (Font)arg1, (str)arg2) -> object :

    C++ signature :
        boost::intrusive_ptr<IECoreScene::MeshPrimitive> mesh(IECoreScene::Font {lvalue},char)

mesh( (Font)arg1, (object)arg2) -> object :

    C++ signature :
        boost::intrusive_ptr<IECoreScene::MeshPrimitive> mesh(IECoreScene::Font {lvalue},std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)'''
    ...
    def meshGroup (self, *args, **kwargs):
      '''
meshGroup( (Font)arg1, (object)arg2) -> object :

    C++ signature :
        boost::intrusive_ptr<IECoreScene::Group> meshGroup(IECoreScene::Font {lvalue},std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)'''
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
    def setCurveTolerance (self, *args, **kwargs):
      '''
setCurveTolerance( (Font)arg1, (float)arg2) -> None :

    C++ signature :
        void setCurveTolerance(IECoreScene::Font {lvalue},float)'''
    ...
    def setKerning (self, *args, **kwargs):
      '''
setKerning( (Font)arg1, (float)arg2) -> None :

    C++ signature :
        void setKerning(IECoreScene::Font {lvalue},float)'''
    ...
    def setLineSpacing (self, *args, **kwargs):
      '''
setLineSpacing( (Font)arg1, (float)arg2) -> None :

    C++ signature :
        void setLineSpacing(IECoreScene::Font {lvalue},float)'''
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
        IECore::TypeId typeId(IECoreScene::Font {lvalue})'''
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
        char const* typeName(IECoreScene::Font {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...

def Group (*args):
      '''
__init__(_object*)

'''      
    ...

class Group:
    def addChild (self, *args, **kwargs):
      '''
addChild( (Group)arg1, (object)arg2) -> None :

    C++ signature :
        void addChild(IECoreScene::Group {lvalue},boost::intrusive_ptr<IECoreScene::VisibleRenderable>)'''
    ...
    def addState (self, *args, **kwargs):
      '''
addState( (Group)arg1, (object)arg2) -> None :

    C++ signature :
        void addState(IECoreScene::Group {lvalue},boost::intrusive_ptr<IECoreScene::StateRenderable>)'''
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
    def bound (self, *args, **kwargs):
      '''
bound( (VisibleRenderable)arg1) -> Box3f :

    C++ signature :
        Imath_3_1::Box<Imath_3_1::Vec3<float> > bound(IECoreScene::VisibleRenderable {lvalue})'''
    ...
    def children (self, *args, **kwargs):
      '''
children( (Group)arg1) -> list :
    Returns all the children in a list - note that modifying the list will not add or remove children.

    C++ signature :
        boost::python::list children(IECoreScene::Group {lvalue})'''
    ...
    def clearChildren (self, *args, **kwargs):
      '''
clearChildren( (Group)arg1) -> None :

    C++ signature :
        void clearChildren(IECoreScene::Group {lvalue})'''
    ...
    def clearState (self, *args, **kwargs):
      '''
clearState( (Group)arg1) -> None :

    C++ signature :
        void clearState(IECoreScene::Group {lvalue})'''
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
    def getAttribute (self, *args, **kwargs):
      '''
getAttribute( (Group)arg1, (object)arg2) -> object :
    Returns a copy of the internal attribute data.

    C++ signature :
        boost::intrusive_ptr<IECore::Data> getAttribute(IECoreScene::Group {lvalue},std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)'''
    ...
    def getTransform (self, *args, **kwargs):
      '''
getTransform( (Group)arg1) -> object :

    C++ signature :
        IECoreScene::Transform* getTransform(IECoreScene::Group {lvalue})'''
    ...
    def globalTransformMatrix (self, *args, **kwargs):
      '''
globalTransformMatrix( (Group)arg1 [, (float)arg2]) -> M44f :

    C++ signature :
        Imath_3_1::Matrix44<float> globalTransformMatrix(IECoreScene::Group {lvalue} [,float])'''
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
isInstanceOf( (Group)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::Group {lvalue},IECore::TypeId)

isInstanceOf( (Group)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::Group {lvalue},char const*)'''
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
    def numWrappedInstances (self, *args, **kwargs):
      '''
numWrappedInstances() -> int :

    C++ signature :
        unsigned long numWrappedInstances()'''
    ...
    def parent (self, *args, **kwargs):
      '''
parent( (Group)arg1) -> object :

    C++ signature :
        IECoreScene::Group* parent(IECoreScene::Group {lvalue})'''
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
    def removeChild (self, *args, **kwargs):
      '''
removeChild( (Group)arg1, (object)arg2) -> None :

    C++ signature :
        void removeChild(IECoreScene::Group {lvalue},boost::intrusive_ptr<IECoreScene::VisibleRenderable>)'''
    ...
    def removeState (self, *args, **kwargs):
      '''
removeState( (Group)arg1, (object)arg2) -> None :

    C++ signature :
        void removeState(IECoreScene::Group {lvalue},boost::intrusive_ptr<IECoreScene::StateRenderable>)'''
    ...
    def render (self, *args, **kwargs):
      '''
render( (Group)arg1, (Renderer)arg2) -> None :

    C++ signature :
        void render(IECoreScene::Group,IECoreScene::Renderer*)

render( (Group)arg1, (Renderer)arg2, (bool)arg3) -> None :

    C++ signature :
        void render(IECoreScene::Group,IECoreScene::Renderer*,bool)'''
    ...
    def renderChildren (self, *args, **kwargs):
      '''
renderChildren( (Group)arg1, (Renderer)arg2) -> None :

    C++ signature :
        void renderChildren(IECoreScene::Group,IECoreScene::Renderer*)'''
    ...
    def renderState (self, *args, **kwargs):
      '''
renderState( (Group)arg1, (Renderer)arg2) -> None :

    C++ signature :
        void renderState(IECoreScene::Group,IECoreScene::Renderer*)'''
    ...
    def save (self, *args, **kwargs):
      '''
save( (Object)arg1, (object)arg2, (InternedString)arg3) -> None :

    C++ signature :
        void save(IECore::Object {lvalue},boost::intrusive_ptr<IECore::IndexedIO>,IECore::InternedString)'''
    ...
    def setAttribute (self, *args, **kwargs):
      '''
setAttribute( (Group)arg1, (object)arg2, (object)arg3) -> None :

    C++ signature :
        void setAttribute(IECoreScene::Group {lvalue},std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >,boost::intrusive_ptr<IECore::Data const>)'''
    ...
    def setTransform (self, *args, **kwargs):
      '''
setTransform( (Group)arg1, (object)arg2) -> None :

    C++ signature :
        void setTransform(IECoreScene::Group {lvalue},boost::intrusive_ptr<IECoreScene::Transform>)'''
    ...
    def state (self, *args, **kwargs):
      '''
state( (Group)arg1) -> list :
    Returns all the state in a list - note that modifying the list will not add or remove state.

    C++ signature :
        boost::python::list state(IECoreScene::Group {lvalue})'''
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
    def transformMatrix (self, *args, **kwargs):
      '''
transformMatrix( (Group)arg1 [, (float)arg2]) -> M44f :

    C++ signature :
        Imath_3_1::Matrix44<float> transformMatrix(IECoreScene::Group {lvalue} [,float])'''
    ...
    def typeId (self, *args, **kwargs):
      '''
typeId( (Group)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreScene::Group {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (Group)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreScene::Group {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...

def GroupParameter (*args):
      '''
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > name, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > description, boost::intrusive_ptr<IECoreScene::Group> defaultValue)
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > name, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > description, boost::intrusive_ptr<IECoreScene::Group> defaultValue, boost::python::api::object presets=())
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > name, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > description, boost::intrusive_ptr<IECoreScene::Group> defaultValue, boost::python::api::object presets=(), bool presetsOnly=False)
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > name, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > description, boost::intrusive_ptr<IECoreScene::Group> defaultValue, boost::python::api::object presets=(), bool presetsOnly=False, boost::intrusive_ptr<IECore::CompoundObject> userData=None)

'''      
    ...

class GroupParameter:
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
isInstanceOf( (GroupParameter)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECore::TypedObjectParameter<IECoreScene::Group> {lvalue},IECore::TypeId)

isInstanceOf( (GroupParameter)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECore::TypedObjectParameter<IECoreScene::Group> {lvalue},char const*)'''
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
typeId( (GroupParameter)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECore::TypedObjectParameter<IECoreScene::Group> {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (GroupParameter)arg1) -> str :

    C++ signature :
        char const* typeName(IECore::TypedObjectParameter<IECoreScene::Group> {lvalue})'''
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
valueValid( (GroupParameter)arg1, (object)arg2) -> tuple :
    Returns a tuple containing a bool specifying validity and a string giving a reason for invalidity.

    C++ signature :
        boost::python::tuple valueValid(IECore::TypedObjectParameter<IECoreScene::Group>,boost::intrusive_ptr<IECore::Object const>)

valueValid( (Parameter)arg1) -> tuple :
    Returns a tuple containing a bool specifying validity and a string giving a reason for invalidity.

    C++ signature :
        boost::python::tuple valueValid(IECore::Parameter)'''
    ...

def IDXReader (*args):
      '''

'''      
    ...

class IDXReader:
    def _IDXReader__extractFields (self, data, names=None):
      '''None'''
    ...
    def _IDXReader__extractRows (self, columnString, rows, keyColumn=None):
      '''None'''
    ...
    def baseTypeId ():
      '''None'''
    ...
    def baseTypeIds (self, *args, **kwargs):
      '''
baseTypeIds( (TypeId)arg1) -> list :

    C++ signature :
        boost::python::list baseTypeIds(IECore::TypeId)'''
    ...
    def baseTypeName ():
      '''None'''
    ...
    def canRead (fileName):
      '''None'''
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
    def derivedTypeIds (self, *args, **kwargs):
      '''
derivedTypeIds( (TypeId)arg1) -> list :

    C++ signature :
        boost::python::list derivedTypeIds(IECore::TypeId)'''
    ...
    def description (self, *args, **kwargs):
      '''None'''
    ...
    def doOperation (self, args):
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
    def inheritsFrom (t):
      '''None'''
    ...
    def isInstanceOf (self, t):
      '''None'''
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
read( (Reader)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::Object> read(IECore::Reader {lvalue})'''
    ...
    def readHeader (self, *args, **kwargs):
      '''
readHeader( (Reader)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::CompoundObject> readHeader(IECore::Reader {lvalue})'''
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
    def staticTypeId ():
      '''None'''
    ...
    def staticTypeName ():
      '''None'''
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
    def typeId (x):
      '''None'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (x):
      '''None'''
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

def Light (*args):
      '''
__init__(boost::python::api::object, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > name='distantlight', std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > handle='', boost::intrusive_ptr<IECore::CompoundData> parameters=0)
__init__(_object*)
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::map<IECore::InternedString, boost::intrusive_ptr<IECore::Data>, std::less<IECore::InternedString>, std::allocator<std::pair<IECore::InternedString const, boost::intrusive_ptr<IECore::Data> > > >)
__init__(_object*)

'''      
    ...

class Light:
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
    def handle (self, *args, **kwargs):
      '''None'''
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
isInstanceOf( (Light)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::Light {lvalue},IECore::TypeId)

isInstanceOf( (Light)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::Light {lvalue},char const*)'''
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
    def name (self, *args, **kwargs):
      '''None'''
    ...
    def numWrappedInstances (self, *args, **kwargs):
      '''
numWrappedInstances() -> int :

    C++ signature :
        unsigned long numWrappedInstances()'''
    ...
    def parameters (self, *args, **kwargs):
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
registerType( (TypeId)typeId, (object)typeName [, (object)creator=None]) -> None :

    C++ signature :
        void registerType(IECore::TypeId,std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > [,boost::python::api::object=None])'''
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
typeId( (Light)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreScene::Light {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (Light)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreScene::Light {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...

def LimitSmoothSkinningInfluencesOp (*args):
      '''
__init__(_object*)

'''      
    ...

class LimitSmoothSkinningInfluencesOp:
    def Mode (self, *args, **kwargs):
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
isInstanceOf( (LimitSmoothSkinningInfluencesOp)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::LimitSmoothSkinningInfluencesOp {lvalue},IECore::TypeId)

isInstanceOf( (LimitSmoothSkinningInfluencesOp)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::LimitSmoothSkinningInfluencesOp {lvalue},char const*)'''
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
typeId( (LimitSmoothSkinningInfluencesOp)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreScene::LimitSmoothSkinningInfluencesOp {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (LimitSmoothSkinningInfluencesOp)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreScene::LimitSmoothSkinningInfluencesOp {lvalue})'''
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

def LinkedScene (*args):
      '''
__init__(boost::python::api::object, boost::intrusive_ptr<IECoreScene::SceneInterface>)
__init__(boost::python::api::object, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, unsigned int)

'''      
    ...

class LinkedScene:
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
    def fileNameLinkAttribute (self, *args, **kwargs):
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
isInstanceOf( (LinkedScene)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::LinkedScene {lvalue},IECore::TypeId)

isInstanceOf( (LinkedScene)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::LinkedScene {lvalue},char const*)'''
    ...
    def isSame (self, *args, **kwargs):
      '''
isSame( (RefCounted)arg1, (RefCounted)arg2) -> bool :

    C++ signature :
        bool isSame(IECore::RefCounted const*,IECore::RefCounted const*)'''
    ...
    def linkAttribute (self, *args, **kwargs):
      '''None'''
    ...
    def linkAttributeData (self, *args, **kwargs):
      '''
linkAttributeData( (SceneInterface)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::CompoundData> linkAttributeData(IECoreScene::SceneInterface const*)

linkAttributeData( (SceneInterface)arg1, (float)arg2) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::CompoundData> linkAttributeData(IECoreScene::SceneInterface const*,double)'''
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
    def rootLinkAttribute (self, *args, **kwargs):
      '''None'''
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
    def timeLinkAttribute (self, *args, **kwargs):
      '''None'''
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
typeId( (LinkedScene)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreScene::LinkedScene {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (LinkedScene)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreScene::LinkedScene {lvalue})'''
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
    def writeLink (self, *args, **kwargs):
      '''
writeLink( (LinkedScene)arg1, (SceneInterface)arg2) -> None :

    C++ signature :
        void writeLink(IECoreScene::LinkedScene {lvalue},IECoreScene::SceneInterface const*)'''
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

def MatrixMotionTransform (*args):
      '''
__init__(_object*)

'''      
    ...

class MatrixMotionTransform:
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
isInstanceOf( (MatrixMotionTransform)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::MatrixMotionTransform {lvalue},IECore::TypeId)

isInstanceOf( (MatrixMotionTransform)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::MatrixMotionTransform {lvalue},char const*)'''
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
keys( (MatrixMotionTransform)arg1) -> list :

    C++ signature :
        boost::python::list keys(IECoreScene::MatrixMotionTransform {lvalue})'''
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
    def transform (self, *args, **kwargs):
      '''
transform( (Transform)arg1 [, (float)arg2]) -> M44f :

    C++ signature :
        Imath_3_1::Matrix44<float> transform(IECoreScene::Transform {lvalue} [,float])'''
    ...
    def typeId (self, *args, **kwargs):
      '''
typeId( (MatrixMotionTransform)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreScene::MatrixMotionTransform {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (MatrixMotionTransform)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreScene::MatrixMotionTransform {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...
    def values (self, *args, **kwargs):
      '''
values( (MatrixMotionTransform)arg1) -> list :

    C++ signature :
        boost::python::list values(IECoreScene::MatrixMotionTransform {lvalue})'''
    ...

def MatrixMotionTransformParameter (*args):
      '''
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > name, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > description, boost::intrusive_ptr<IECoreScene::MatrixMotionTransform> defaultValue)
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > name, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > description, boost::intrusive_ptr<IECoreScene::MatrixMotionTransform> defaultValue, boost::python::api::object presets=())
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > name, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > description, boost::intrusive_ptr<IECoreScene::MatrixMotionTransform> defaultValue, boost::python::api::object presets=(), bool presetsOnly=False)
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > name, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > description, boost::intrusive_ptr<IECoreScene::MatrixMotionTransform> defaultValue, boost::python::api::object presets=(), bool presetsOnly=False, boost::intrusive_ptr<IECore::CompoundObject> userData=None)

'''      
    ...

class MatrixMotionTransformParameter:
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
isInstanceOf( (MatrixMotionTransformParameter)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECore::TypedObjectParameter<IECoreScene::MatrixMotionTransform> {lvalue},IECore::TypeId)

isInstanceOf( (MatrixMotionTransformParameter)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECore::TypedObjectParameter<IECoreScene::MatrixMotionTransform> {lvalue},char const*)'''
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
typeId( (MatrixMotionTransformParameter)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECore::TypedObjectParameter<IECoreScene::MatrixMotionTransform> {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (MatrixMotionTransformParameter)arg1) -> str :

    C++ signature :
        char const* typeName(IECore::TypedObjectParameter<IECoreScene::MatrixMotionTransform> {lvalue})'''
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
valueValid( (MatrixMotionTransformParameter)arg1, (object)arg2) -> tuple :
    Returns a tuple containing a bool specifying validity and a string giving a reason for invalidity.

    C++ signature :
        boost::python::tuple valueValid(IECore::TypedObjectParameter<IECoreScene::MatrixMotionTransform>,boost::intrusive_ptr<IECore::Object const>)

valueValid( (Parameter)arg1) -> tuple :
    Returns a tuple containing a bool specifying validity and a string giving a reason for invalidity.

    C++ signature :
        boost::python::tuple valueValid(IECore::Parameter)'''
    ...

def MatrixTransform (*args):
      '''
__init__(_object*, Imath_3_1::Matrix44<float>)

'''      
    ...

class MatrixTransform:
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
isInstanceOf( (MatrixTransform)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::MatrixTransform {lvalue},IECore::TypeId)

isInstanceOf( (MatrixTransform)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::MatrixTransform {lvalue},char const*)'''
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
    def matrix (self, *args, **kwargs):
      '''None'''
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
    def transform (self, *args, **kwargs):
      '''
transform( (Transform)arg1 [, (float)arg2]) -> M44f :

    C++ signature :
        Imath_3_1::Matrix44<float> transform(IECoreScene::Transform {lvalue} [,float])'''
    ...
    def typeId (self, *args, **kwargs):
      '''
typeId( (MatrixTransform)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreScene::MatrixTransform {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (MatrixTransform)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreScene::MatrixTransform {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...

def MatrixTransformParameter (*args):
      '''
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > name, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > description, boost::intrusive_ptr<IECoreScene::MatrixTransform> defaultValue)
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > name, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > description, boost::intrusive_ptr<IECoreScene::MatrixTransform> defaultValue, boost::python::api::object presets=())
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > name, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > description, boost::intrusive_ptr<IECoreScene::MatrixTransform> defaultValue, boost::python::api::object presets=(), bool presetsOnly=False)
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > name, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > description, boost::intrusive_ptr<IECoreScene::MatrixTransform> defaultValue, boost::python::api::object presets=(), bool presetsOnly=False, boost::intrusive_ptr<IECore::CompoundObject> userData=None)

'''      
    ...

class MatrixTransformParameter:
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
isInstanceOf( (MatrixTransformParameter)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECore::TypedObjectParameter<IECoreScene::MatrixTransform> {lvalue},IECore::TypeId)

isInstanceOf( (MatrixTransformParameter)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECore::TypedObjectParameter<IECoreScene::MatrixTransform> {lvalue},char const*)'''
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
typeId( (MatrixTransformParameter)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECore::TypedObjectParameter<IECoreScene::MatrixTransform> {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (MatrixTransformParameter)arg1) -> str :

    C++ signature :
        char const* typeName(IECore::TypedObjectParameter<IECoreScene::MatrixTransform> {lvalue})'''
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
valueValid( (MatrixTransformParameter)arg1, (object)arg2) -> tuple :
    Returns a tuple containing a bool specifying validity and a string giving a reason for invalidity.

    C++ signature :
        boost::python::tuple valueValid(IECore::TypedObjectParameter<IECoreScene::MatrixTransform>,boost::intrusive_ptr<IECore::Object const>)

valueValid( (Parameter)arg1) -> tuple :
    Returns a tuple containing a bool specifying validity and a string giving a reason for invalidity.

    C++ signature :
        boost::python::tuple valueValid(IECore::Parameter)'''
    ...

def MeshAlgo (*args):
      '''

'''      
    ...

def MeshMergeOp (*args):
      '''
__init__(_object*)

'''      
    ...

class MeshMergeOp:
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
isInstanceOf( (MeshMergeOp)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::MeshMergeOp {lvalue},IECore::TypeId)

isInstanceOf( (MeshMergeOp)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::MeshMergeOp {lvalue},char const*)'''
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
typeId( (MeshMergeOp)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreScene::MeshMergeOp {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (MeshMergeOp)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreScene::MeshMergeOp {lvalue})'''
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

def MeshNormalsOp (*args):
      '''
__init__(_object*)

'''      
    ...

class MeshNormalsOp:
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
isInstanceOf( (MeshNormalsOp)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::MeshNormalsOp {lvalue},IECore::TypeId)

isInstanceOf( (MeshNormalsOp)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::MeshNormalsOp {lvalue},char const*)'''
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
typeId( (MeshNormalsOp)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreScene::MeshNormalsOp {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (MeshNormalsOp)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreScene::MeshNormalsOp {lvalue})'''
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

def MeshPrimitive (*args):
      '''
__init__(_object*, boost::intrusive_ptr<IECore::TypedData<std::vector<int, std::allocator<int> > > >, boost::intrusive_ptr<IECore::TypedData<std::vector<int, std::allocator<int> > > >)
__init__(_object*, boost::intrusive_ptr<IECore::TypedData<std::vector<int, std::allocator<int> > > >, boost::intrusive_ptr<IECore::TypedData<std::vector<int, std::allocator<int> > > >, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)
__init__(_object*, boost::intrusive_ptr<IECore::TypedData<std::vector<int, std::allocator<int> > > >, boost::intrusive_ptr<IECore::TypedData<std::vector<int, std::allocator<int> > > >, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, boost::intrusive_ptr<IECore::GeometricTypedData<std::vector<Imath_3_1::Vec3<float>, std::allocator<Imath_3_1::Vec3<float> > > > >)
__init__(_object*)

'''      
    ...

class MeshPrimitive:
    def arePrimitiveVariablesValid (self, *args, **kwargs):
      '''
arePrimitiveVariablesValid( (Primitive)arg1) -> bool :

    C++ signature :
        bool arePrimitiveVariablesValid(IECoreScene::Primitive {lvalue})'''
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
    def cornerIds (self, *args, **kwargs):
      '''
cornerIds( (MeshPrimitive)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::TypedData<std::vector<int, std::allocator<int> > > > cornerIds(IECoreScene::MeshPrimitive)'''
    ...
    def cornerSharpnesses (self, *args, **kwargs):
      '''
cornerSharpnesses( (MeshPrimitive)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::TypedData<std::vector<float, std::allocator<float> > > > cornerSharpnesses(IECoreScene::MeshPrimitive)'''
    ...
    def creaseIds (self, *args, **kwargs):
      '''
creaseIds( (MeshPrimitive)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::TypedData<std::vector<int, std::allocator<int> > > > creaseIds(IECoreScene::MeshPrimitive)'''
    ...
    def creaseLengths (self, *args, **kwargs):
      '''
creaseLengths( (MeshPrimitive)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::TypedData<std::vector<int, std::allocator<int> > > > creaseLengths(IECoreScene::MeshPrimitive)'''
    ...
    def creaseSharpnesses (self, *args, **kwargs):
      '''
creaseSharpnesses( (MeshPrimitive)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::TypedData<std::vector<float, std::allocator<float> > > > creaseSharpnesses(IECoreScene::MeshPrimitive)'''
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
    def createBox (self, *args, **kwargs):
      '''
createBox( (Box3f)bounds) -> object :

    C++ signature :
        boost::intrusive_ptr<IECoreScene::MeshPrimitive> createBox(Imath_3_1::Box<Imath_3_1::Vec3<float> >)'''
    ...
    def createPlane (self, *args, **kwargs):
      '''
createPlane( (Box2f)bounds [, (V2i)divisions=V2i(1, 1) [, (Canceller)canceller=None]]) -> object :

    C++ signature :
        boost::intrusive_ptr<IECoreScene::MeshPrimitive> createPlane(Imath_3_1::Box<Imath_3_1::Vec2<float> > [,Imath_3_1::Vec2<int>=V2i(1, 1) [,IECore::Canceller const*=None]])'''
    ...
    def createSphere (self, *args, **kwargs):
      '''
createSphere( (float)radius [, (float)zMin=-1.0 [, (float)zMax=1.0 [, (float)thetaMax=360.0 [, (V2i)divisions=V2i(20, 40) [, (Canceller)canceller=None]]]]]) -> object :

    C++ signature :
        boost::intrusive_ptr<IECoreScene::MeshPrimitive> createSphere(float [,float=-1.0 [,float=1.0 [,float=360.0 [,Imath_3_1::Vec2<int>=V2i(20, 40) [,IECore::Canceller const*=None]]]]])'''
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
    def hash (self, *args, **kwargs):
      '''
hash( (Object)arg1) -> MurmurHash :

    C++ signature :
        IECore::MurmurHash hash(IECore::Object {lvalue})

hash( (Object)arg1, (MurmurHash)arg2) -> None :

    C++ signature :
        void hash(IECore::Object {lvalue},IECore::MurmurHash {lvalue})'''
    ...
    def inferInterpolation (self, *args, **kwargs):
      '''
inferInterpolation( (Primitive)arg1, (Data)arg2) -> Interpolation :

    C++ signature :
        IECoreScene::PrimitiveVariable::Interpolation inferInterpolation(IECoreScene::Primitive {lvalue},IECore::Data const*)

inferInterpolation( (Primitive)arg1, (int)arg2) -> Interpolation :

    C++ signature :
        IECoreScene::PrimitiveVariable::Interpolation inferInterpolation(IECoreScene::Primitive {lvalue},unsigned long)'''
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
    def interpolation (self, *args, **kwargs):
      '''None'''
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
isInstanceOf( (MeshPrimitive)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::MeshPrimitive {lvalue},IECore::TypeId)

isInstanceOf( (MeshPrimitive)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::MeshPrimitive {lvalue},char const*)'''
    ...
    def isPrimitiveVariableValid (self, *args, **kwargs):
      '''
isPrimitiveVariableValid( (Primitive)arg1, (PrimitiveVariable)arg2) -> bool :

    C++ signature :
        bool isPrimitiveVariableValid(IECoreScene::Primitive {lvalue},IECoreScene::PrimitiveVariable)'''
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
keys( (Primitive)arg1) -> list :

    C++ signature :
        boost::python::list keys(IECoreScene::Primitive {lvalue})'''
    ...
    def load (self, *args, **kwargs):
      '''
load( (object)ioInterface, (InternedString)name [, (Canceller)canceller=None]) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::Object> load(boost::intrusive_ptr<IECore::IndexedIO const>,IECore::InternedString [,IECore::Canceller const*=None])'''
    ...
    def maxVerticesPerFace (self, *args, **kwargs):
      '''
maxVerticesPerFace( (MeshPrimitive)arg1) -> int :

    C++ signature :
        int maxVerticesPerFace(IECoreScene::MeshPrimitive {lvalue})'''
    ...
    def memoryUsage (self, *args, **kwargs):
      '''
memoryUsage( (Object)arg1) -> int :
    Returns the number of bytes this instance occupies in memory

    C++ signature :
        unsigned long memoryUsage(IECore::Object {lvalue})'''
    ...
    def minVerticesPerFace (self, *args, **kwargs):
      '''
minVerticesPerFace( (MeshPrimitive)arg1) -> int :

    C++ signature :
        int minVerticesPerFace(IECoreScene::MeshPrimitive {lvalue})'''
    ...
    def numFaces (self, *args, **kwargs):
      '''
numFaces( (MeshPrimitive)arg1) -> int :

    C++ signature :
        unsigned long numFaces(IECoreScene::MeshPrimitive {lvalue})'''
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
    def removeCorners (self, *args, **kwargs):
      '''
removeCorners( (MeshPrimitive)arg1) -> None :

    C++ signature :
        void removeCorners(IECoreScene::MeshPrimitive {lvalue})'''
    ...
    def removeCreases (self, *args, **kwargs):
      '''
removeCreases( (MeshPrimitive)arg1) -> None :

    C++ signature :
        void removeCreases(IECoreScene::MeshPrimitive {lvalue})'''
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
    def setCorners (self, *args, **kwargs):
      '''
setCorners( (MeshPrimitive)arg1, (IntVectorData)arg2, (FloatVectorData)arg3) -> None :

    C++ signature :
        void setCorners(IECoreScene::MeshPrimitive {lvalue},IECore::TypedData<std::vector<int, std::allocator<int> > > const*,IECore::TypedData<std::vector<float, std::allocator<float> > > const*)'''
    ...
    def setCreases (self, *args, **kwargs):
      '''
setCreases( (MeshPrimitive)arg1, (IntVectorData)arg2, (IntVectorData)arg3, (FloatVectorData)arg4) -> None :

    C++ signature :
        void setCreases(IECoreScene::MeshPrimitive {lvalue},IECore::TypedData<std::vector<int, std::allocator<int> > > const*,IECore::TypedData<std::vector<int, std::allocator<int> > > const*,IECore::TypedData<std::vector<float, std::allocator<float> > > const*)'''
    ...
    def setInterpolation (self, *args, **kwargs):
      '''
setInterpolation( (MeshPrimitive)arg1, (object)arg2) -> None :

    C++ signature :
        void setInterpolation(IECoreScene::MeshPrimitive {lvalue},std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)'''
    ...
    def setTopology (self, *args, **kwargs):
      '''
setTopology( (MeshPrimitive)arg1, (object)arg2, (object)arg3, (object)arg4) -> None :

    C++ signature :
        void setTopology(IECoreScene::MeshPrimitive {lvalue},boost::intrusive_ptr<IECore::TypedData<std::vector<int, std::allocator<int> > > const>,boost::intrusive_ptr<IECore::TypedData<std::vector<int, std::allocator<int> > > const>,std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)'''
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
    def topologyHash (self, *args, **kwargs):
      '''
topologyHash( (Primitive)arg1) -> MurmurHash :

    C++ signature :
        IECore::MurmurHash topologyHash(IECoreScene::Primitive {lvalue})

topologyHash( (Primitive)arg1, (MurmurHash)arg2) -> None :

    C++ signature :
        void topologyHash(IECoreScene::Primitive {lvalue},IECore::MurmurHash {lvalue})'''
    ...
    def typeId (self, *args, **kwargs):
      '''
typeId( (MeshPrimitive)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreScene::MeshPrimitive {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (MeshPrimitive)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreScene::MeshPrimitive {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...
    def values (self, *args, **kwargs):
      '''
values( (Primitive)arg1) -> list :
    Returns a list containing shallow copies of the PrimitiveVariable objects held.

    C++ signature :
        boost::python::list values(IECoreScene::Primitive {lvalue})'''
    ...
    def variableSize (self, *args, **kwargs):
      '''
variableSize( (Primitive)arg1, (Interpolation)arg2) -> int :

    C++ signature :
        unsigned long variableSize(IECoreScene::Primitive {lvalue},IECoreScene::PrimitiveVariable::Interpolation)'''
    ...
    def vertexIds (self, *args, **kwargs):
      '''A copy of the mesh's list of vertex ids.'''
    ...
    def verticesPerFace (self, *args, **kwargs):
      '''A copy of the mesh's list of vertices per face.'''
    ...

def MeshPrimitiveBuilder (*args):
      '''
__init__(_object*)

'''      
    ...

class MeshPrimitiveBuilder:
    def addTriangle (self, *args, **kwargs):
      '''
addTriangle( (MeshPrimitiveBuilder)arg1, (int)arg2, (int)arg3, (int)arg4) -> None :

    C++ signature :
        void addTriangle(IECoreScene::MeshPrimitiveBuilder {lvalue},int,int,int)'''
    ...
    def addVertex (self, *args, **kwargs):
      '''
addVertex( (MeshPrimitiveBuilder)arg1, (V3f)arg2, (V3f)arg3) -> None :

    C++ signature :
        void addVertex(IECoreScene::MeshPrimitiveBuilder {lvalue},Imath_3_1::Vec3<float>,Imath_3_1::Vec3<float>)

addVertex( (MeshPrimitiveBuilder)arg1, (V3d)arg2, (V3d)arg3) -> None :

    C++ signature :
        void addVertex(IECoreScene::MeshPrimitiveBuilder {lvalue},Imath_3_1::Vec3<double>,Imath_3_1::Vec3<double>)'''
    ...
    def collectGarbage (self, *args, **kwargs):
      '''
collectGarbage() -> None :

    C++ signature :
        void collectGarbage()'''
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
    def isSame (self, *args, **kwargs):
      '''
isSame( (RefCounted)arg1, (RefCounted)arg2) -> bool :

    C++ signature :
        bool isSame(IECore::RefCounted const*,IECore::RefCounted const*)'''
    ...
    def mesh (self, *args, **kwargs):
      '''
mesh( (MeshPrimitiveBuilder)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECoreScene::MeshPrimitive> mesh(IECoreScene::MeshPrimitiveBuilder {lvalue})'''
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

def MeshPrimitiveEvaluator (*args):
      '''
__init__(_object*, boost::intrusive_ptr<IECoreScene::MeshPrimitive>)

'''      
    ...

class MeshPrimitiveEvaluator:
    def Result (self, *args, **kwargs):
      '''None'''
    ...
    def barycentricPosition (self, *args, **kwargs):
      '''
barycentricPosition( (MeshPrimitiveEvaluator)arg1, (int)arg2, (V3f)arg3, (Result)arg4) -> bool :

    C++ signature :
        bool barycentricPosition(IECoreScene::MeshPrimitiveEvaluator,unsigned int,Imath_3_1::Vec3<float>,IECoreScene::PrimitiveEvaluator::Result*)'''
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
    def centerOfGravity (self, *args, **kwargs):
      '''
centerOfGravity( (PrimitiveEvaluator)arg1) -> V3f :

    C++ signature :
        Imath_3_1::Vec3<float> centerOfGravity(IECoreScene::PrimitiveEvaluator {lvalue})'''
    ...
    def closestPoint (self, *args, **kwargs):
      '''
closestPoint( (PrimitiveEvaluator)arg1, (V3f)arg2, (Result)arg3) -> bool :

    C++ signature :
        bool closestPoint(IECoreScene::PrimitiveEvaluator {lvalue},Imath_3_1::Vec3<float>,IECoreScene::PrimitiveEvaluator::Result*)'''
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
        boost::intrusive_ptr<IECoreScene::PrimitiveEvaluator> create(boost::intrusive_ptr<IECoreScene::Primitive>)'''
    ...
    def createResult (self, *args, **kwargs):
      '''
createResult( (PrimitiveEvaluator)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECoreScene::PrimitiveEvaluator::Result> createResult(IECoreScene::PrimitiveEvaluator {lvalue})'''
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
    def intersectionPoint (self, *args, **kwargs):
      '''
intersectionPoint( (PrimitiveEvaluator)arg1, (V3f)arg2, (V3f)arg3, (Result)arg4) -> bool :

    C++ signature :
        bool intersectionPoint(IECoreScene::PrimitiveEvaluator {lvalue},Imath_3_1::Vec3<float>,Imath_3_1::Vec3<float>,IECoreScene::PrimitiveEvaluator::Result*)

intersectionPoint( (PrimitiveEvaluator)arg1, (V3f)arg2, (V3f)arg3, (Result)arg4, (float)arg5) -> bool :

    C++ signature :
        bool intersectionPoint(IECoreScene::PrimitiveEvaluator {lvalue},Imath_3_1::Vec3<float>,Imath_3_1::Vec3<float>,IECoreScene::PrimitiveEvaluator::Result*,float)'''
    ...
    def intersectionPoints (self, *args, **kwargs):
      '''
intersectionPoints( (PrimitiveEvaluator)arg1, (V3f)arg2, (V3f)arg3) -> list :

    C++ signature :
        boost::python::list intersectionPoints(IECoreScene::PrimitiveEvaluator {lvalue},Imath_3_1::Vec3<float>,Imath_3_1::Vec3<float>)

intersectionPoints( (PrimitiveEvaluator)arg1, (V3f)arg2, (V3f)arg3, (float)arg4) -> list :

    C++ signature :
        boost::python::list intersectionPoints(IECoreScene::PrimitiveEvaluator {lvalue},Imath_3_1::Vec3<float>,Imath_3_1::Vec3<float>,float)'''
    ...
    def isInstanceOf (self, *args, **kwargs):
      '''
isInstanceOf( (MeshPrimitiveEvaluator)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::MeshPrimitiveEvaluator {lvalue},IECore::TypeId)

isInstanceOf( (MeshPrimitiveEvaluator)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::MeshPrimitiveEvaluator {lvalue},char const*)'''
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
    def pointAtUV (self, *args, **kwargs):
      '''
pointAtUV( (PrimitiveEvaluator)arg1, (V2f)arg2, (Result)arg3) -> bool :

    C++ signature :
        bool pointAtUV(IECoreScene::PrimitiveEvaluator {lvalue},Imath_3_1::Vec2<float>,IECoreScene::PrimitiveEvaluator::Result*)'''
    ...
    def primitive (self, *args, **kwargs):
      '''
primitive( (PrimitiveEvaluator)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECoreScene::Primitive> primitive(IECoreScene::PrimitiveEvaluator {lvalue})'''
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
    def signedDistance (self, *args, **kwargs):
      '''
signedDistance( (PrimitiveEvaluator)arg1, (V3f)arg2, (Result)arg3) -> float :

    C++ signature :
        float signedDistance(IECoreScene::PrimitiveEvaluator {lvalue},Imath_3_1::Vec3<float>,IECoreScene::PrimitiveEvaluator::Result*)'''
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
    def surfaceArea (self, *args, **kwargs):
      '''
surfaceArea( (PrimitiveEvaluator)arg1) -> float :

    C++ signature :
        float surfaceArea(IECoreScene::PrimitiveEvaluator {lvalue})'''
    ...
    def typeId (self, *args, **kwargs):
      '''
typeId( (MeshPrimitiveEvaluator)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreScene::MeshPrimitiveEvaluator {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (MeshPrimitiveEvaluator)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreScene::MeshPrimitiveEvaluator {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...
    def uvBound (self, *args, **kwargs):
      '''
uvBound( (MeshPrimitiveEvaluator)arg1) -> Box2f :

    C++ signature :
        Imath_3_1::Box<Imath_3_1::Vec2<float> > uvBound(IECoreScene::MeshPrimitiveEvaluator {lvalue})'''
    ...
    def validateResult (self, *args, **kwargs):
      '''
validateResult( (PrimitiveEvaluator)arg1, (Result)arg2) -> None :

    C++ signature :
        void validateResult(IECoreScene::PrimitiveEvaluator {lvalue},IECoreScene::PrimitiveEvaluator::Result*)'''
    ...
    def volume (self, *args, **kwargs):
      '''
volume( (PrimitiveEvaluator)arg1) -> float :

    C++ signature :
        float volume(IECoreScene::PrimitiveEvaluator {lvalue})'''
    ...

def MeshPrimitiveOp (*args):
      '''
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)

'''      
    ...

class MeshPrimitiveOp:
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
isInstanceOf( (MeshPrimitiveOp)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::TypedPrimitiveOp<IECoreScene::MeshPrimitive> {lvalue},IECore::TypeId)

isInstanceOf( (MeshPrimitiveOp)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::TypedPrimitiveOp<IECoreScene::MeshPrimitive> {lvalue},char const*)'''
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
typeId( (MeshPrimitiveOp)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreScene::TypedPrimitiveOp<IECoreScene::MeshPrimitive> {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (MeshPrimitiveOp)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreScene::TypedPrimitiveOp<IECoreScene::MeshPrimitive> {lvalue})'''
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

def MeshPrimitiveParameter (*args):
      '''
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > name, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > description, boost::intrusive_ptr<IECoreScene::MeshPrimitive> defaultValue)
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > name, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > description, boost::intrusive_ptr<IECoreScene::MeshPrimitive> defaultValue, boost::python::api::object presets=())
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > name, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > description, boost::intrusive_ptr<IECoreScene::MeshPrimitive> defaultValue, boost::python::api::object presets=(), bool presetsOnly=False)
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > name, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > description, boost::intrusive_ptr<IECoreScene::MeshPrimitive> defaultValue, boost::python::api::object presets=(), bool presetsOnly=False, boost::intrusive_ptr<IECore::CompoundObject> userData=None)

'''      
    ...

class MeshPrimitiveParameter:
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
isInstanceOf( (MeshPrimitiveParameter)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECore::TypedObjectParameter<IECoreScene::MeshPrimitive> {lvalue},IECore::TypeId)

isInstanceOf( (MeshPrimitiveParameter)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECore::TypedObjectParameter<IECoreScene::MeshPrimitive> {lvalue},char const*)'''
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
typeId( (MeshPrimitiveParameter)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECore::TypedObjectParameter<IECoreScene::MeshPrimitive> {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (MeshPrimitiveParameter)arg1) -> str :

    C++ signature :
        char const* typeName(IECore::TypedObjectParameter<IECoreScene::MeshPrimitive> {lvalue})'''
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
valueValid( (MeshPrimitiveParameter)arg1, (object)arg2) -> tuple :
    Returns a tuple containing a bool specifying validity and a string giving a reason for invalidity.

    C++ signature :
        boost::python::tuple valueValid(IECore::TypedObjectParameter<IECoreScene::MeshPrimitive>,boost::intrusive_ptr<IECore::Object const>)

valueValid( (Parameter)arg1) -> tuple :
    Returns a tuple containing a bool specifying validity and a string giving a reason for invalidity.

    C++ signature :
        boost::python::tuple valueValid(IECore::Parameter)'''
    ...

def MeshPrimitiveShrinkWrapOp (*args):
      '''
__init__(_object*)

'''      
    ...

class MeshPrimitiveShrinkWrapOp:
    def Direction (self, *args, **kwargs):
      '''None'''
    ...
    def Method (self, *args, **kwargs):
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
isInstanceOf( (MeshPrimitiveShrinkWrapOp)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::MeshPrimitiveShrinkWrapOp {lvalue},IECore::TypeId)

isInstanceOf( (MeshPrimitiveShrinkWrapOp)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::MeshPrimitiveShrinkWrapOp {lvalue},char const*)'''
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
typeId( (MeshPrimitiveShrinkWrapOp)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreScene::MeshPrimitiveShrinkWrapOp {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (MeshPrimitiveShrinkWrapOp)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreScene::MeshPrimitiveShrinkWrapOp {lvalue})'''
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

def MeshVertexReorderOp (*args):
      '''
__init__(_object*)

'''      
    ...

class MeshVertexReorderOp:
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
isInstanceOf( (MeshVertexReorderOp)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::MeshVertexReorderOp {lvalue},IECore::TypeId)

isInstanceOf( (MeshVertexReorderOp)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::MeshVertexReorderOp {lvalue},char const*)'''
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
typeId( (MeshVertexReorderOp)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreScene::MeshVertexReorderOp {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (MeshVertexReorderOp)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreScene::MeshVertexReorderOp {lvalue})'''
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

def MixSmoothSkinningWeightsOp (*args):
      '''
__init__(_object*)

'''      
    ...

class MixSmoothSkinningWeightsOp:
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
isInstanceOf( (MixSmoothSkinningWeightsOp)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::MixSmoothSkinningWeightsOp {lvalue},IECore::TypeId)

isInstanceOf( (MixSmoothSkinningWeightsOp)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::MixSmoothSkinningWeightsOp {lvalue},char const*)'''
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
typeId( (MixSmoothSkinningWeightsOp)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreScene::MixSmoothSkinningWeightsOp {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (MixSmoothSkinningWeightsOp)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreScene::MixSmoothSkinningWeightsOp {lvalue})'''
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

def MotionBlock (*args):
      '''

'''      
    ...

class MotionBlock:

def MotionPrimitive (*args):
      '''
__init__(_object*)

'''      
    ...

class MotionPrimitive:
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
isInstanceOf( (MotionPrimitive)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::MotionPrimitive {lvalue},IECore::TypeId)

isInstanceOf( (MotionPrimitive)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::MotionPrimitive {lvalue},char const*)'''
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
    def items (self, *args, **kwargs):
      '''
items( (MotionPrimitive)arg1) -> list :

    C++ signature :
        boost::python::list items(IECoreScene::MotionPrimitive {lvalue})'''
    ...
    def keys (self, *args, **kwargs):
      '''
keys( (MotionPrimitive)arg1) -> list :

    C++ signature :
        boost::python::list keys(IECoreScene::MotionPrimitive {lvalue})'''
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
typeId( (MotionPrimitive)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreScene::MotionPrimitive {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (MotionPrimitive)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreScene::MotionPrimitive {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...
    def values (self, *args, **kwargs):
      '''
values( (MotionPrimitive)arg1) -> list :

    C++ signature :
        boost::python::list values(IECoreScene::MotionPrimitive {lvalue})'''
    ...

def MotionPrimitiveParameter (*args):
      '''
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > name, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > description, boost::intrusive_ptr<IECoreScene::MotionPrimitive> defaultValue)
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > name, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > description, boost::intrusive_ptr<IECoreScene::MotionPrimitive> defaultValue, boost::python::api::object presets=())
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > name, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > description, boost::intrusive_ptr<IECoreScene::MotionPrimitive> defaultValue, boost::python::api::object presets=(), bool presetsOnly=False)
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > name, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > description, boost::intrusive_ptr<IECoreScene::MotionPrimitive> defaultValue, boost::python::api::object presets=(), bool presetsOnly=False, boost::intrusive_ptr<IECore::CompoundObject> userData=None)

'''      
    ...

class MotionPrimitiveParameter:
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
isInstanceOf( (MotionPrimitiveParameter)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECore::TypedObjectParameter<IECoreScene::MotionPrimitive> {lvalue},IECore::TypeId)

isInstanceOf( (MotionPrimitiveParameter)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECore::TypedObjectParameter<IECoreScene::MotionPrimitive> {lvalue},char const*)'''
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
typeId( (MotionPrimitiveParameter)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECore::TypedObjectParameter<IECoreScene::MotionPrimitive> {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (MotionPrimitiveParameter)arg1) -> str :

    C++ signature :
        char const* typeName(IECore::TypedObjectParameter<IECoreScene::MotionPrimitive> {lvalue})'''
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
valueValid( (MotionPrimitiveParameter)arg1, (object)arg2) -> tuple :
    Returns a tuple containing a bool specifying validity and a string giving a reason for invalidity.

    C++ signature :
        boost::python::tuple valueValid(IECore::TypedObjectParameter<IECoreScene::MotionPrimitive>,boost::intrusive_ptr<IECore::Object const>)

valueValid( (Parameter)arg1) -> tuple :
    Returns a tuple containing a bool specifying validity and a string giving a reason for invalidity.

    C++ signature :
        boost::python::tuple valueValid(IECore::Parameter)'''
    ...

def NParticleReader (*args):
      '''
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)
__init__(_object*)

'''      
    ...

class NParticleReader:
    def attributeNames (self, *args, **kwargs):
      '''
attributeNames( (ParticleReader)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::TypedData<std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > > > attributeNames(IECoreScene::ParticleReader {lvalue})'''
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
    def canRead (self, *args, **kwargs):
      '''
canRead( (object)arg1) -> bool :

    C++ signature :
        bool canRead(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)'''
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
    def derivedTypeIds (self, *args, **kwargs):
      '''
derivedTypeIds( (TypeId)arg1) -> list :

    C++ signature :
        boost::python::list derivedTypeIds(IECore::TypeId)'''
    ...
    def description (self, *args, **kwargs):
      '''None'''
    ...
    def frameTimes (self, *args, **kwargs):
      '''
frameTimes( (NParticleReader)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::TypedData<std::vector<int, std::allocator<int> > > > frameTimes(IECoreScene::NParticleReader {lvalue})'''
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
isInstanceOf( (NParticleReader)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::NParticleReader {lvalue},IECore::TypeId)

isInstanceOf( (NParticleReader)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::NParticleReader {lvalue},char const*)'''
    ...
    def isSame (self, *args, **kwargs):
      '''
isSame( (RefCounted)arg1, (RefCounted)arg2) -> bool :

    C++ signature :
        bool isSame(IECore::RefCounted const*,IECore::RefCounted const*)'''
    ...
    def numParticles (self, *args, **kwargs):
      '''
numParticles( (ParticleReader)arg1) -> int :

    C++ signature :
        unsigned long numParticles(IECoreScene::ParticleReader {lvalue})'''
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
read( (Reader)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::Object> read(IECore::Reader {lvalue})'''
    ...
    def readAttribute (self, *args, **kwargs):
      '''
readAttribute( (ParticleReader)arg1, (object)arg2) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::Data> readAttribute(IECoreScene::ParticleReader {lvalue},std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)'''
    ...
    def readHeader (self, *args, **kwargs):
      '''
readHeader( (Reader)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::CompoundObject> readHeader(IECore::Reader {lvalue})'''
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
typeId( (NParticleReader)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreScene::NParticleReader {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (NParticleReader)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreScene::NParticleReader {lvalue})'''
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

def NURBSPrimitive (*args):
      '''
__init__(_object*, int, boost::intrusive_ptr<IECore::TypedData<std::vector<float, std::allocator<float> > > const>, float, float, int, boost::intrusive_ptr<IECore::TypedData<std::vector<float, std::allocator<float> > > const>, float, float)
__init__(_object*, int, boost::intrusive_ptr<IECore::TypedData<std::vector<float, std::allocator<float> > > const>, float, float, int, boost::intrusive_ptr<IECore::TypedData<std::vector<float, std::allocator<float> > > const>, float, float, boost::intrusive_ptr<IECore::GeometricTypedData<std::vector<Imath_3_1::Vec3<float>, std::allocator<Imath_3_1::Vec3<float> > > > >)
__init__(_object*)

'''      
    ...

class NURBSPrimitive:
    def arePrimitiveVariablesValid (self, *args, **kwargs):
      '''
arePrimitiveVariablesValid( (Primitive)arg1) -> bool :

    C++ signature :
        bool arePrimitiveVariablesValid(IECoreScene::Primitive {lvalue})'''
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
    def hash (self, *args, **kwargs):
      '''
hash( (Object)arg1) -> MurmurHash :

    C++ signature :
        IECore::MurmurHash hash(IECore::Object {lvalue})

hash( (Object)arg1, (MurmurHash)arg2) -> None :

    C++ signature :
        void hash(IECore::Object {lvalue},IECore::MurmurHash {lvalue})'''
    ...
    def inferInterpolation (self, *args, **kwargs):
      '''
inferInterpolation( (Primitive)arg1, (Data)arg2) -> Interpolation :

    C++ signature :
        IECoreScene::PrimitiveVariable::Interpolation inferInterpolation(IECoreScene::Primitive {lvalue},IECore::Data const*)

inferInterpolation( (Primitive)arg1, (int)arg2) -> Interpolation :

    C++ signature :
        IECoreScene::PrimitiveVariable::Interpolation inferInterpolation(IECoreScene::Primitive {lvalue},unsigned long)'''
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
isInstanceOf( (NURBSPrimitive)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::NURBSPrimitive {lvalue},IECore::TypeId)

isInstanceOf( (NURBSPrimitive)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::NURBSPrimitive {lvalue},char const*)'''
    ...
    def isPrimitiveVariableValid (self, *args, **kwargs):
      '''
isPrimitiveVariableValid( (Primitive)arg1, (PrimitiveVariable)arg2) -> bool :

    C++ signature :
        bool isPrimitiveVariableValid(IECoreScene::Primitive {lvalue},IECoreScene::PrimitiveVariable)'''
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
keys( (Primitive)arg1) -> list :

    C++ signature :
        boost::python::list keys(IECoreScene::Primitive {lvalue})'''
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
    def setTopology (self, *args, **kwargs):
      '''
setTopology( (NURBSPrimitive)arg1, (int)arg2, (object)arg3, (float)arg4, (float)arg5, (int)arg6, (object)arg7, (float)arg8, (float)arg9) -> None :

    C++ signature :
        void setTopology(IECoreScene::NURBSPrimitive {lvalue},int,boost::intrusive_ptr<IECore::TypedData<std::vector<float, std::allocator<float> > > const>,float,float,int,boost::intrusive_ptr<IECore::TypedData<std::vector<float, std::allocator<float> > > const>,float,float)'''
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
    def topologyHash (self, *args, **kwargs):
      '''
topologyHash( (Primitive)arg1) -> MurmurHash :

    C++ signature :
        IECore::MurmurHash topologyHash(IECoreScene::Primitive {lvalue})

topologyHash( (Primitive)arg1, (MurmurHash)arg2) -> None :

    C++ signature :
        void topologyHash(IECoreScene::Primitive {lvalue},IECore::MurmurHash {lvalue})'''
    ...
    def typeId (self, *args, **kwargs):
      '''
typeId( (NURBSPrimitive)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreScene::NURBSPrimitive {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (NURBSPrimitive)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreScene::NURBSPrimitive {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...
    def uKnot (self, *args, **kwargs):
      '''
uKnot( (NURBSPrimitive)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::TypedData<std::vector<float, std::allocator<float> > > > uKnot(IECoreScene::NURBSPrimitive)'''
    ...
    def uMax (self, *args, **kwargs):
      '''
uMax( (NURBSPrimitive)arg1) -> float :

    C++ signature :
        float uMax(IECoreScene::NURBSPrimitive {lvalue})'''
    ...
    def uMin (self, *args, **kwargs):
      '''
uMin( (NURBSPrimitive)arg1) -> float :

    C++ signature :
        float uMin(IECoreScene::NURBSPrimitive {lvalue})'''
    ...
    def uOrder (self, *args, **kwargs):
      '''
uOrder( (NURBSPrimitive)arg1) -> int :

    C++ signature :
        int uOrder(IECoreScene::NURBSPrimitive {lvalue})'''
    ...
    def uSegments (self, *args, **kwargs):
      '''
uSegments( (NURBSPrimitive)arg1) -> int :

    C++ signature :
        int uSegments(IECoreScene::NURBSPrimitive {lvalue})'''
    ...
    def uVertices (self, *args, **kwargs):
      '''
uVertices( (NURBSPrimitive)arg1) -> int :

    C++ signature :
        int uVertices(IECoreScene::NURBSPrimitive {lvalue})'''
    ...
    def vKnot (self, *args, **kwargs):
      '''
vKnot( (NURBSPrimitive)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::TypedData<std::vector<float, std::allocator<float> > > > vKnot(IECoreScene::NURBSPrimitive)'''
    ...
    def vMax (self, *args, **kwargs):
      '''
vMax( (NURBSPrimitive)arg1) -> float :

    C++ signature :
        float vMax(IECoreScene::NURBSPrimitive {lvalue})'''
    ...
    def vMin (self, *args, **kwargs):
      '''
vMin( (NURBSPrimitive)arg1) -> float :

    C++ signature :
        float vMin(IECoreScene::NURBSPrimitive {lvalue})'''
    ...
    def vOrder (self, *args, **kwargs):
      '''
vOrder( (NURBSPrimitive)arg1) -> int :

    C++ signature :
        int vOrder(IECoreScene::NURBSPrimitive {lvalue})'''
    ...
    def vSegments (self, *args, **kwargs):
      '''
vSegments( (NURBSPrimitive)arg1) -> int :

    C++ signature :
        int vSegments(IECoreScene::NURBSPrimitive {lvalue})'''
    ...
    def vVertices (self, *args, **kwargs):
      '''
vVertices( (NURBSPrimitive)arg1) -> int :

    C++ signature :
        int vVertices(IECoreScene::NURBSPrimitive {lvalue})'''
    ...
    def values (self, *args, **kwargs):
      '''
values( (Primitive)arg1) -> list :
    Returns a list containing shallow copies of the PrimitiveVariable objects held.

    C++ signature :
        boost::python::list values(IECoreScene::Primitive {lvalue})'''
    ...
    def variableSize (self, *args, **kwargs):
      '''
variableSize( (Primitive)arg1, (Interpolation)arg2) -> int :

    C++ signature :
        unsigned long variableSize(IECoreScene::Primitive {lvalue},IECoreScene::PrimitiveVariable::Interpolation)'''
    ...

def NormalizeSmoothSkinningWeightsOp (*args):
      '''
__init__(_object*)

'''      
    ...

class NormalizeSmoothSkinningWeightsOp:
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
isInstanceOf( (NormalizeSmoothSkinningWeightsOp)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::NormalizeSmoothSkinningWeightsOp {lvalue},IECore::TypeId)

isInstanceOf( (NormalizeSmoothSkinningWeightsOp)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::NormalizeSmoothSkinningWeightsOp {lvalue},char const*)'''
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
typeId( (NormalizeSmoothSkinningWeightsOp)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreScene::NormalizeSmoothSkinningWeightsOp {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (NormalizeSmoothSkinningWeightsOp)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreScene::NormalizeSmoothSkinningWeightsOp {lvalue})'''
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

def OBJReader (*args):
      '''
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)

'''      
    ...

class OBJReader:
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
isInstanceOf( (OBJReader)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::OBJReader {lvalue},IECore::TypeId)

isInstanceOf( (OBJReader)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::OBJReader {lvalue},char const*)'''
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
read( (Reader)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::Object> read(IECore::Reader {lvalue})'''
    ...
    def readHeader (self, *args, **kwargs):
      '''
readHeader( (Reader)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::CompoundObject> readHeader(IECore::Reader {lvalue})'''
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
typeId( (OBJReader)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreScene::OBJReader {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (OBJReader)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreScene::OBJReader {lvalue})'''
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

def Options (*args):
      '''
__init__(_object*, boost::intrusive_ptr<IECore::CompoundData>)
__init__(_object*)

'''      
    ...

class Options:
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
isInstanceOf( (Options)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::Options {lvalue},IECore::TypeId)

isInstanceOf( (Options)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::Options {lvalue},char const*)'''
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
    def numWrappedInstances (self, *args, **kwargs):
      '''
numWrappedInstances() -> int :

    C++ signature :
        unsigned long numWrappedInstances()'''
    ...
    def options (self, *args, **kwargs):
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
registerType( (TypeId)typeId, (object)typeName [, (object)creator=None]) -> None :

    C++ signature :
        void registerType(IECore::TypeId,std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > [,boost::python::api::object=None])'''
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
typeId( (Options)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreScene::Options {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (Options)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreScene::Options {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...

def Output (*args):
      '''
__init__(_object*)
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > name='default')
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > name='default', std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > type='exr')
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > name='default', std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > type='exr', std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > data='rgba')
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > name='default', std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > type='exr', std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > data='rgba', boost::intrusive_ptr<IECore::CompoundData> parameters=IECore.CompoundData())

'''      
    ...

class Output:
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
    def getData (self, *args, **kwargs):
      '''
getData( (Output)arg1) -> str :

    C++ signature :
        std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > getData(IECoreScene::Output {lvalue})'''
    ...
    def getName (self, *args, **kwargs):
      '''
getName( (Output)arg1) -> str :

    C++ signature :
        std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > getName(IECoreScene::Output {lvalue})'''
    ...
    def getType (self, *args, **kwargs):
      '''
getType( (Output)arg1) -> str :

    C++ signature :
        std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > getType(IECoreScene::Output {lvalue})'''
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
isInstanceOf( (Output)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::Output {lvalue},IECore::TypeId)

isInstanceOf( (Output)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::Output {lvalue},char const*)'''
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
    def numWrappedInstances (self, *args, **kwargs):
      '''
numWrappedInstances() -> int :

    C++ signature :
        unsigned long numWrappedInstances()'''
    ...
    def parameters (self, *args, **kwargs):
      '''
parameters( (Output)arg1) -> object :

    C++ signature :
        IECore::CompoundData* parameters(IECoreScene::Output {lvalue})'''
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
    def setData (self, *args, **kwargs):
      '''
setData( (Output)arg1, (object)arg2) -> None :

    C++ signature :
        void setData(IECoreScene::Output {lvalue},std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)'''
    ...
    def setName (self, *args, **kwargs):
      '''
setName( (Output)arg1, (object)arg2) -> None :

    C++ signature :
        void setName(IECoreScene::Output {lvalue},std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)'''
    ...
    def setType (self, *args, **kwargs):
      '''
setType( (Output)arg1, (object)arg2) -> None :

    C++ signature :
        void setType(IECoreScene::Output {lvalue},std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)'''
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
typeId( (Output)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreScene::Output {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (Output)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreScene::Output {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...

def PDCParticleReader (*args):
      '''
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)
__init__(_object*)

'''      
    ...

class PDCParticleReader:
    def attributeNames (self, *args, **kwargs):
      '''
attributeNames( (ParticleReader)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::TypedData<std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > > > attributeNames(IECoreScene::ParticleReader {lvalue})'''
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
    def canRead (self, *args, **kwargs):
      '''
canRead( (object)arg1) -> bool :

    C++ signature :
        bool canRead(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)'''
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
isInstanceOf( (PDCParticleReader)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::PDCParticleReader {lvalue},IECore::TypeId)

isInstanceOf( (PDCParticleReader)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::PDCParticleReader {lvalue},char const*)'''
    ...
    def isSame (self, *args, **kwargs):
      '''
isSame( (RefCounted)arg1, (RefCounted)arg2) -> bool :

    C++ signature :
        bool isSame(IECore::RefCounted const*,IECore::RefCounted const*)'''
    ...
    def numParticles (self, *args, **kwargs):
      '''
numParticles( (ParticleReader)arg1) -> int :

    C++ signature :
        unsigned long numParticles(IECoreScene::ParticleReader {lvalue})'''
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
read( (Reader)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::Object> read(IECore::Reader {lvalue})'''
    ...
    def readAttribute (self, *args, **kwargs):
      '''
readAttribute( (ParticleReader)arg1, (object)arg2) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::Data> readAttribute(IECoreScene::ParticleReader {lvalue},std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)'''
    ...
    def readHeader (self, *args, **kwargs):
      '''
readHeader( (Reader)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::CompoundObject> readHeader(IECore::Reader {lvalue})'''
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
typeId( (PDCParticleReader)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreScene::PDCParticleReader {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (PDCParticleReader)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreScene::PDCParticleReader {lvalue})'''
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

def PDCParticleWriter (*args):
      '''
__init__(_object*, boost::intrusive_ptr<IECore::Object>, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)
__init__(_object*)

'''      
    ...

class PDCParticleWriter:
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
isInstanceOf( (PDCParticleWriter)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::PDCParticleWriter {lvalue},IECore::TypeId)

isInstanceOf( (PDCParticleWriter)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::PDCParticleWriter {lvalue},char const*)'''
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
typeId( (PDCParticleWriter)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreScene::PDCParticleWriter {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (PDCParticleWriter)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreScene::PDCParticleWriter {lvalue})'''
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

def ParticleReader (*args):
      '''

'''      
    ...

class ParticleReader:
    def attributeNames (self, *args, **kwargs):
      '''
attributeNames( (ParticleReader)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::TypedData<std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > > > attributeNames(IECoreScene::ParticleReader {lvalue})'''
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
    def create (self, *args, **kwargs):
      '''
create( (object)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::Reader> create(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)'''
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
isInstanceOf( (ParticleReader)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::ParticleReader {lvalue},IECore::TypeId)

isInstanceOf( (ParticleReader)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::ParticleReader {lvalue},char const*)'''
    ...
    def isSame (self, *args, **kwargs):
      '''
isSame( (RefCounted)arg1, (RefCounted)arg2) -> bool :

    C++ signature :
        bool isSame(IECore::RefCounted const*,IECore::RefCounted const*)'''
    ...
    def numParticles (self, *args, **kwargs):
      '''
numParticles( (ParticleReader)arg1) -> int :

    C++ signature :
        unsigned long numParticles(IECoreScene::ParticleReader {lvalue})'''
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
read( (Reader)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::Object> read(IECore::Reader {lvalue})'''
    ...
    def readAttribute (self, *args, **kwargs):
      '''
readAttribute( (ParticleReader)arg1, (object)arg2) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::Data> readAttribute(IECoreScene::ParticleReader {lvalue},std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)'''
    ...
    def readHeader (self, *args, **kwargs):
      '''
readHeader( (Reader)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::CompoundObject> readHeader(IECore::Reader {lvalue})'''
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
typeId( (ParticleReader)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreScene::ParticleReader {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (ParticleReader)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreScene::ParticleReader {lvalue})'''
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

def ParticleWriter (*args):
      '''

'''      
    ...

class ParticleWriter:
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
isInstanceOf( (ParticleWriter)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::ParticleWriter {lvalue},IECore::TypeId)

isInstanceOf( (ParticleWriter)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::ParticleWriter {lvalue},char const*)'''
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
typeId( (ParticleWriter)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreScene::ParticleWriter {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (ParticleWriter)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreScene::ParticleWriter {lvalue})'''
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

def PatchMeshPrimitive (*args):
      '''
__init__(_object*, unsigned int, unsigned int)
__init__(_object*, unsigned int, unsigned int, IECore::CubicBasis<float>)
__init__(_object*, unsigned int, unsigned int, IECore::CubicBasis<float>, IECore::CubicBasis<float>)
__init__(_object*, unsigned int, unsigned int, IECore::CubicBasis<float>, IECore::CubicBasis<float>, bool)
__init__(_object*, unsigned int, unsigned int, IECore::CubicBasis<float>, IECore::CubicBasis<float>, bool, bool)
__init__(_object*, unsigned int, unsigned int, IECore::CubicBasis<float>, IECore::CubicBasis<float>, bool, bool, boost::intrusive_ptr<IECore::GeometricTypedData<std::vector<Imath_3_1::Vec3<float>, std::allocator<Imath_3_1::Vec3<float> > > > const>)

'''      
    ...

class PatchMeshPrimitive:
    def arePrimitiveVariablesValid (self, *args, **kwargs):
      '''
arePrimitiveVariablesValid( (Primitive)arg1) -> bool :

    C++ signature :
        bool arePrimitiveVariablesValid(IECoreScene::Primitive {lvalue})'''
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
    def hash (self, *args, **kwargs):
      '''
hash( (Object)arg1) -> MurmurHash :

    C++ signature :
        IECore::MurmurHash hash(IECore::Object {lvalue})

hash( (Object)arg1, (MurmurHash)arg2) -> None :

    C++ signature :
        void hash(IECore::Object {lvalue},IECore::MurmurHash {lvalue})'''
    ...
    def inferInterpolation (self, *args, **kwargs):
      '''
inferInterpolation( (Primitive)arg1, (Data)arg2) -> Interpolation :

    C++ signature :
        IECoreScene::PrimitiveVariable::Interpolation inferInterpolation(IECoreScene::Primitive {lvalue},IECore::Data const*)

inferInterpolation( (Primitive)arg1, (int)arg2) -> Interpolation :

    C++ signature :
        IECoreScene::PrimitiveVariable::Interpolation inferInterpolation(IECoreScene::Primitive {lvalue},unsigned long)'''
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
isInstanceOf( (PatchMeshPrimitive)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::PatchMeshPrimitive {lvalue},IECore::TypeId)

isInstanceOf( (PatchMeshPrimitive)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::PatchMeshPrimitive {lvalue},char const*)'''
    ...
    def isPrimitiveVariableValid (self, *args, **kwargs):
      '''
isPrimitiveVariableValid( (Primitive)arg1, (PrimitiveVariable)arg2) -> bool :

    C++ signature :
        bool isPrimitiveVariableValid(IECoreScene::Primitive {lvalue},IECoreScene::PrimitiveVariable)'''
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
keys( (Primitive)arg1) -> list :

    C++ signature :
        boost::python::list keys(IECoreScene::Primitive {lvalue})'''
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
    def topologyHash (self, *args, **kwargs):
      '''
topologyHash( (Primitive)arg1) -> MurmurHash :

    C++ signature :
        IECore::MurmurHash topologyHash(IECoreScene::Primitive {lvalue})

topologyHash( (Primitive)arg1, (MurmurHash)arg2) -> None :

    C++ signature :
        void topologyHash(IECoreScene::Primitive {lvalue},IECore::MurmurHash {lvalue})'''
    ...
    def typeId (self, *args, **kwargs):
      '''
typeId( (PatchMeshPrimitive)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreScene::PatchMeshPrimitive {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (PatchMeshPrimitive)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreScene::PatchMeshPrimitive {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...
    def uBasis (self, *args, **kwargs):
      '''
uBasis( (PatchMeshPrimitive)arg1) -> CubicBasisf :

    C++ signature :
        IECore::CubicBasis<float> uBasis(IECoreScene::PatchMeshPrimitive {lvalue})'''
    ...
    def uPatches (self, *args, **kwargs):
      '''
uPatches( (PatchMeshPrimitive)arg1) -> int :

    C++ signature :
        unsigned int uPatches(IECoreScene::PatchMeshPrimitive {lvalue})'''
    ...
    def uPeriodic (self, *args, **kwargs):
      '''
uPeriodic( (PatchMeshPrimitive)arg1) -> bool :

    C++ signature :
        bool uPeriodic(IECoreScene::PatchMeshPrimitive {lvalue})'''
    ...
    def uPoints (self, *args, **kwargs):
      '''
uPoints( (PatchMeshPrimitive)arg1) -> int :

    C++ signature :
        unsigned int uPoints(IECoreScene::PatchMeshPrimitive {lvalue})'''
    ...
    def vBasis (self, *args, **kwargs):
      '''
vBasis( (PatchMeshPrimitive)arg1) -> CubicBasisf :

    C++ signature :
        IECore::CubicBasis<float> vBasis(IECoreScene::PatchMeshPrimitive {lvalue})'''
    ...
    def vPatches (self, *args, **kwargs):
      '''
vPatches( (PatchMeshPrimitive)arg1) -> int :

    C++ signature :
        unsigned int vPatches(IECoreScene::PatchMeshPrimitive {lvalue})'''
    ...
    def vPeriodic (self, *args, **kwargs):
      '''
vPeriodic( (PatchMeshPrimitive)arg1) -> bool :

    C++ signature :
        bool vPeriodic(IECoreScene::PatchMeshPrimitive {lvalue})'''
    ...
    def vPoints (self, *args, **kwargs):
      '''
vPoints( (PatchMeshPrimitive)arg1) -> int :

    C++ signature :
        unsigned int vPoints(IECoreScene::PatchMeshPrimitive {lvalue})'''
    ...
    def values (self, *args, **kwargs):
      '''
values( (Primitive)arg1) -> list :
    Returns a list containing shallow copies of the PrimitiveVariable objects held.

    C++ signature :
        boost::python::list values(IECoreScene::Primitive {lvalue})'''
    ...
    def variableSize (self, *args, **kwargs):
      '''
variableSize( (Primitive)arg1, (Interpolation)arg2) -> int :

    C++ signature :
        unsigned long variableSize(IECoreScene::Primitive {lvalue},IECoreScene::PrimitiveVariable::Interpolation)'''
    ...

def PointSmoothSkinningOp (*args):
      '''
__init__(_object*)

'''      
    ...

class PointSmoothSkinningOp:
    def Blend (self, *args, **kwargs):
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
isInstanceOf( (PointSmoothSkinningOp)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::PointSmoothSkinningOp {lvalue},IECore::TypeId)

isInstanceOf( (PointSmoothSkinningOp)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::PointSmoothSkinningOp {lvalue},char const*)'''
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
typeId( (PointSmoothSkinningOp)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreScene::PointSmoothSkinningOp {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (PointSmoothSkinningOp)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreScene::PointSmoothSkinningOp {lvalue})'''
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

def PointsAlgo (*args):
      '''

'''      
    ...

def PointsPrimitive (*args):
      '''
__init__(_object*, boost::intrusive_ptr<IECore::GeometricTypedData<std::vector<Imath_3_1::Vec3<float>, std::allocator<Imath_3_1::Vec3<float> > > > >, boost::intrusive_ptr<IECore::TypedData<std::vector<float, std::allocator<float> > > >)
__init__(_object*, boost::intrusive_ptr<IECore::GeometricTypedData<std::vector<Imath_3_1::Vec3<float>, std::allocator<Imath_3_1::Vec3<float> > > > >)
__init__(_object*, unsigned long)

'''      
    ...

class PointsPrimitive:
    def arePrimitiveVariablesValid (self, *args, **kwargs):
      '''
arePrimitiveVariablesValid( (Primitive)arg1) -> bool :

    C++ signature :
        bool arePrimitiveVariablesValid(IECoreScene::Primitive {lvalue})'''
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
    def hash (self, *args, **kwargs):
      '''
hash( (Object)arg1) -> MurmurHash :

    C++ signature :
        IECore::MurmurHash hash(IECore::Object {lvalue})

hash( (Object)arg1, (MurmurHash)arg2) -> None :

    C++ signature :
        void hash(IECore::Object {lvalue},IECore::MurmurHash {lvalue})'''
    ...
    def inferInterpolation (self, *args, **kwargs):
      '''
inferInterpolation( (Primitive)arg1, (Data)arg2) -> Interpolation :

    C++ signature :
        IECoreScene::PrimitiveVariable::Interpolation inferInterpolation(IECoreScene::Primitive {lvalue},IECore::Data const*)

inferInterpolation( (Primitive)arg1, (int)arg2) -> Interpolation :

    C++ signature :
        IECoreScene::PrimitiveVariable::Interpolation inferInterpolation(IECoreScene::Primitive {lvalue},unsigned long)'''
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
isInstanceOf( (PointsPrimitive)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::PointsPrimitive {lvalue},IECore::TypeId)

isInstanceOf( (PointsPrimitive)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::PointsPrimitive {lvalue},char const*)'''
    ...
    def isPrimitiveVariableValid (self, *args, **kwargs):
      '''
isPrimitiveVariableValid( (Primitive)arg1, (PrimitiveVariable)arg2) -> bool :

    C++ signature :
        bool isPrimitiveVariableValid(IECoreScene::Primitive {lvalue},IECoreScene::PrimitiveVariable)'''
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
keys( (Primitive)arg1) -> list :

    C++ signature :
        boost::python::list keys(IECoreScene::Primitive {lvalue})'''
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
    def numPoints (self, *args, **kwargs):
      '''None'''
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
    def topologyHash (self, *args, **kwargs):
      '''
topologyHash( (Primitive)arg1) -> MurmurHash :

    C++ signature :
        IECore::MurmurHash topologyHash(IECoreScene::Primitive {lvalue})

topologyHash( (Primitive)arg1, (MurmurHash)arg2) -> None :

    C++ signature :
        void topologyHash(IECoreScene::Primitive {lvalue},IECore::MurmurHash {lvalue})'''
    ...
    def typeId (self, *args, **kwargs):
      '''
typeId( (PointsPrimitive)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreScene::PointsPrimitive {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (PointsPrimitive)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreScene::PointsPrimitive {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...
    def values (self, *args, **kwargs):
      '''
values( (Primitive)arg1) -> list :
    Returns a list containing shallow copies of the PrimitiveVariable objects held.

    C++ signature :
        boost::python::list values(IECoreScene::Primitive {lvalue})'''
    ...
    def variableSize (self, *args, **kwargs):
      '''
variableSize( (Primitive)arg1, (Interpolation)arg2) -> int :

    C++ signature :
        unsigned long variableSize(IECoreScene::Primitive {lvalue},IECoreScene::PrimitiveVariable::Interpolation)'''
    ...

def PointsPrimitiveEvaluator (*args):
      '''
__init__(_object*, boost::intrusive_ptr<IECoreScene::PointsPrimitive>)

'''      
    ...

class PointsPrimitiveEvaluator:
    def Result (self, *args, **kwargs):
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
    def centerOfGravity (self, *args, **kwargs):
      '''
centerOfGravity( (PrimitiveEvaluator)arg1) -> V3f :

    C++ signature :
        Imath_3_1::Vec3<float> centerOfGravity(IECoreScene::PrimitiveEvaluator {lvalue})'''
    ...
    def closestPoint (self, *args, **kwargs):
      '''
closestPoint( (PrimitiveEvaluator)arg1, (V3f)arg2, (Result)arg3) -> bool :

    C++ signature :
        bool closestPoint(IECoreScene::PrimitiveEvaluator {lvalue},Imath_3_1::Vec3<float>,IECoreScene::PrimitiveEvaluator::Result*)'''
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
        boost::intrusive_ptr<IECoreScene::PrimitiveEvaluator> create(boost::intrusive_ptr<IECoreScene::Primitive>)'''
    ...
    def createResult (self, *args, **kwargs):
      '''
createResult( (PrimitiveEvaluator)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECoreScene::PrimitiveEvaluator::Result> createResult(IECoreScene::PrimitiveEvaluator {lvalue})'''
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
    def intersectionPoint (self, *args, **kwargs):
      '''
intersectionPoint( (PrimitiveEvaluator)arg1, (V3f)arg2, (V3f)arg3, (Result)arg4) -> bool :

    C++ signature :
        bool intersectionPoint(IECoreScene::PrimitiveEvaluator {lvalue},Imath_3_1::Vec3<float>,Imath_3_1::Vec3<float>,IECoreScene::PrimitiveEvaluator::Result*)

intersectionPoint( (PrimitiveEvaluator)arg1, (V3f)arg2, (V3f)arg3, (Result)arg4, (float)arg5) -> bool :

    C++ signature :
        bool intersectionPoint(IECoreScene::PrimitiveEvaluator {lvalue},Imath_3_1::Vec3<float>,Imath_3_1::Vec3<float>,IECoreScene::PrimitiveEvaluator::Result*,float)'''
    ...
    def intersectionPoints (self, *args, **kwargs):
      '''
intersectionPoints( (PrimitiveEvaluator)arg1, (V3f)arg2, (V3f)arg3) -> list :

    C++ signature :
        boost::python::list intersectionPoints(IECoreScene::PrimitiveEvaluator {lvalue},Imath_3_1::Vec3<float>,Imath_3_1::Vec3<float>)

intersectionPoints( (PrimitiveEvaluator)arg1, (V3f)arg2, (V3f)arg3, (float)arg4) -> list :

    C++ signature :
        boost::python::list intersectionPoints(IECoreScene::PrimitiveEvaluator {lvalue},Imath_3_1::Vec3<float>,Imath_3_1::Vec3<float>,float)'''
    ...
    def isInstanceOf (self, *args, **kwargs):
      '''
isInstanceOf( (PointsPrimitiveEvaluator)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::PointsPrimitiveEvaluator {lvalue},IECore::TypeId)

isInstanceOf( (PointsPrimitiveEvaluator)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::PointsPrimitiveEvaluator {lvalue},char const*)'''
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
    def pointAtUV (self, *args, **kwargs):
      '''
pointAtUV( (PrimitiveEvaluator)arg1, (V2f)arg2, (Result)arg3) -> bool :

    C++ signature :
        bool pointAtUV(IECoreScene::PrimitiveEvaluator {lvalue},Imath_3_1::Vec2<float>,IECoreScene::PrimitiveEvaluator::Result*)'''
    ...
    def primitive (self, *args, **kwargs):
      '''
primitive( (PrimitiveEvaluator)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECoreScene::Primitive> primitive(IECoreScene::PrimitiveEvaluator {lvalue})'''
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
    def signedDistance (self, *args, **kwargs):
      '''
signedDistance( (PrimitiveEvaluator)arg1, (V3f)arg2, (Result)arg3) -> float :

    C++ signature :
        float signedDistance(IECoreScene::PrimitiveEvaluator {lvalue},Imath_3_1::Vec3<float>,IECoreScene::PrimitiveEvaluator::Result*)'''
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
    def surfaceArea (self, *args, **kwargs):
      '''
surfaceArea( (PrimitiveEvaluator)arg1) -> float :

    C++ signature :
        float surfaceArea(IECoreScene::PrimitiveEvaluator {lvalue})'''
    ...
    def typeId (self, *args, **kwargs):
      '''
typeId( (PointsPrimitiveEvaluator)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreScene::PointsPrimitiveEvaluator {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (PointsPrimitiveEvaluator)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreScene::PointsPrimitiveEvaluator {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...
    def validateResult (self, *args, **kwargs):
      '''
validateResult( (PrimitiveEvaluator)arg1, (Result)arg2) -> None :

    C++ signature :
        void validateResult(IECoreScene::PrimitiveEvaluator {lvalue},IECoreScene::PrimitiveEvaluator::Result*)'''
    ...
    def volume (self, *args, **kwargs):
      '''
volume( (PrimitiveEvaluator)arg1) -> float :

    C++ signature :
        float volume(IECoreScene::PrimitiveEvaluator {lvalue})'''
    ...

def PointsPrimitiveParameter (*args):
      '''
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > name, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > description, boost::intrusive_ptr<IECoreScene::PointsPrimitive> defaultValue)
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > name, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > description, boost::intrusive_ptr<IECoreScene::PointsPrimitive> defaultValue, boost::python::api::object presets=())
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > name, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > description, boost::intrusive_ptr<IECoreScene::PointsPrimitive> defaultValue, boost::python::api::object presets=(), bool presetsOnly=False)
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > name, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > description, boost::intrusive_ptr<IECoreScene::PointsPrimitive> defaultValue, boost::python::api::object presets=(), bool presetsOnly=False, boost::intrusive_ptr<IECore::CompoundObject> userData=None)

'''      
    ...

class PointsPrimitiveParameter:
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
isInstanceOf( (PointsPrimitiveParameter)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECore::TypedObjectParameter<IECoreScene::PointsPrimitive> {lvalue},IECore::TypeId)

isInstanceOf( (PointsPrimitiveParameter)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECore::TypedObjectParameter<IECoreScene::PointsPrimitive> {lvalue},char const*)'''
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
typeId( (PointsPrimitiveParameter)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECore::TypedObjectParameter<IECoreScene::PointsPrimitive> {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (PointsPrimitiveParameter)arg1) -> str :

    C++ signature :
        char const* typeName(IECore::TypedObjectParameter<IECoreScene::PointsPrimitive> {lvalue})'''
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
valueValid( (PointsPrimitiveParameter)arg1, (object)arg2) -> tuple :
    Returns a tuple containing a bool specifying validity and a string giving a reason for invalidity.

    C++ signature :
        boost::python::tuple valueValid(IECore::TypedObjectParameter<IECoreScene::PointsPrimitive>,boost::intrusive_ptr<IECore::Object const>)

valueValid( (Parameter)arg1) -> tuple :
    Returns a tuple containing a bool specifying validity and a string giving a reason for invalidity.

    C++ signature :
        boost::python::tuple valueValid(IECore::Parameter)'''
    ...

def PreWorldRenderable (*args):
      '''

'''      
    ...

class PreWorldRenderable:
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
isInstanceOf( (PreWorldRenderable)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::PreWorldRenderable {lvalue},IECore::TypeId)

isInstanceOf( (PreWorldRenderable)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::PreWorldRenderable {lvalue},char const*)'''
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
typeId( (PreWorldRenderable)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreScene::PreWorldRenderable {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (PreWorldRenderable)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreScene::PreWorldRenderable {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...

def Primitive (*args):
      '''

'''      
    ...

class Primitive:
    def arePrimitiveVariablesValid (self, *args, **kwargs):
      '''
arePrimitiveVariablesValid( (Primitive)arg1) -> bool :

    C++ signature :
        bool arePrimitiveVariablesValid(IECoreScene::Primitive {lvalue})'''
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
    def hash (self, *args, **kwargs):
      '''
hash( (Object)arg1) -> MurmurHash :

    C++ signature :
        IECore::MurmurHash hash(IECore::Object {lvalue})

hash( (Object)arg1, (MurmurHash)arg2) -> None :

    C++ signature :
        void hash(IECore::Object {lvalue},IECore::MurmurHash {lvalue})'''
    ...
    def inferInterpolation (self, *args, **kwargs):
      '''
inferInterpolation( (Primitive)arg1, (Data)arg2) -> Interpolation :

    C++ signature :
        IECoreScene::PrimitiveVariable::Interpolation inferInterpolation(IECoreScene::Primitive {lvalue},IECore::Data const*)

inferInterpolation( (Primitive)arg1, (int)arg2) -> Interpolation :

    C++ signature :
        IECoreScene::PrimitiveVariable::Interpolation inferInterpolation(IECoreScene::Primitive {lvalue},unsigned long)'''
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
isInstanceOf( (Primitive)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::Primitive {lvalue},IECore::TypeId)

isInstanceOf( (Primitive)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::Primitive {lvalue},char const*)'''
    ...
    def isPrimitiveVariableValid (self, *args, **kwargs):
      '''
isPrimitiveVariableValid( (Primitive)arg1, (PrimitiveVariable)arg2) -> bool :

    C++ signature :
        bool isPrimitiveVariableValid(IECoreScene::Primitive {lvalue},IECoreScene::PrimitiveVariable)'''
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
keys( (Primitive)arg1) -> list :

    C++ signature :
        boost::python::list keys(IECoreScene::Primitive {lvalue})'''
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
    def topologyHash (self, *args, **kwargs):
      '''
topologyHash( (Primitive)arg1) -> MurmurHash :

    C++ signature :
        IECore::MurmurHash topologyHash(IECoreScene::Primitive {lvalue})

topologyHash( (Primitive)arg1, (MurmurHash)arg2) -> None :

    C++ signature :
        void topologyHash(IECoreScene::Primitive {lvalue},IECore::MurmurHash {lvalue})'''
    ...
    def typeId (self, *args, **kwargs):
      '''
typeId( (Primitive)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreScene::Primitive {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (Primitive)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreScene::Primitive {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...
    def values (self, *args, **kwargs):
      '''
values( (Primitive)arg1) -> list :
    Returns a list containing shallow copies of the PrimitiveVariable objects held.

    C++ signature :
        boost::python::list values(IECoreScene::Primitive {lvalue})'''
    ...
    def variableSize (self, *args, **kwargs):
      '''
variableSize( (Primitive)arg1, (Interpolation)arg2) -> int :

    C++ signature :
        unsigned long variableSize(IECoreScene::Primitive {lvalue},IECoreScene::PrimitiveVariable::Interpolation)'''
    ...

def PrimitiveEvaluator (*args):
      '''

'''      
    ...

class PrimitiveEvaluator:
    def Result (self, *args, **kwargs):
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
    def centerOfGravity (self, *args, **kwargs):
      '''
centerOfGravity( (PrimitiveEvaluator)arg1) -> V3f :

    C++ signature :
        Imath_3_1::Vec3<float> centerOfGravity(IECoreScene::PrimitiveEvaluator {lvalue})'''
    ...
    def closestPoint (self, *args, **kwargs):
      '''
closestPoint( (PrimitiveEvaluator)arg1, (V3f)arg2, (Result)arg3) -> bool :

    C++ signature :
        bool closestPoint(IECoreScene::PrimitiveEvaluator {lvalue},Imath_3_1::Vec3<float>,IECoreScene::PrimitiveEvaluator::Result*)'''
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
        boost::intrusive_ptr<IECoreScene::PrimitiveEvaluator> create(boost::intrusive_ptr<IECoreScene::Primitive>)'''
    ...
    def createResult (self, *args, **kwargs):
      '''
createResult( (PrimitiveEvaluator)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECoreScene::PrimitiveEvaluator::Result> createResult(IECoreScene::PrimitiveEvaluator {lvalue})'''
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
    def intersectionPoint (self, *args, **kwargs):
      '''
intersectionPoint( (PrimitiveEvaluator)arg1, (V3f)arg2, (V3f)arg3, (Result)arg4) -> bool :

    C++ signature :
        bool intersectionPoint(IECoreScene::PrimitiveEvaluator {lvalue},Imath_3_1::Vec3<float>,Imath_3_1::Vec3<float>,IECoreScene::PrimitiveEvaluator::Result*)

intersectionPoint( (PrimitiveEvaluator)arg1, (V3f)arg2, (V3f)arg3, (Result)arg4, (float)arg5) -> bool :

    C++ signature :
        bool intersectionPoint(IECoreScene::PrimitiveEvaluator {lvalue},Imath_3_1::Vec3<float>,Imath_3_1::Vec3<float>,IECoreScene::PrimitiveEvaluator::Result*,float)'''
    ...
    def intersectionPoints (self, *args, **kwargs):
      '''
intersectionPoints( (PrimitiveEvaluator)arg1, (V3f)arg2, (V3f)arg3) -> list :

    C++ signature :
        boost::python::list intersectionPoints(IECoreScene::PrimitiveEvaluator {lvalue},Imath_3_1::Vec3<float>,Imath_3_1::Vec3<float>)

intersectionPoints( (PrimitiveEvaluator)arg1, (V3f)arg2, (V3f)arg3, (float)arg4) -> list :

    C++ signature :
        boost::python::list intersectionPoints(IECoreScene::PrimitiveEvaluator {lvalue},Imath_3_1::Vec3<float>,Imath_3_1::Vec3<float>,float)'''
    ...
    def isInstanceOf (self, *args, **kwargs):
      '''
isInstanceOf( (PrimitiveEvaluator)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::PrimitiveEvaluator {lvalue},IECore::TypeId)

isInstanceOf( (PrimitiveEvaluator)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::PrimitiveEvaluator {lvalue},char const*)'''
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
    def pointAtUV (self, *args, **kwargs):
      '''
pointAtUV( (PrimitiveEvaluator)arg1, (V2f)arg2, (Result)arg3) -> bool :

    C++ signature :
        bool pointAtUV(IECoreScene::PrimitiveEvaluator {lvalue},Imath_3_1::Vec2<float>,IECoreScene::PrimitiveEvaluator::Result*)'''
    ...
    def primitive (self, *args, **kwargs):
      '''
primitive( (PrimitiveEvaluator)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECoreScene::Primitive> primitive(IECoreScene::PrimitiveEvaluator {lvalue})'''
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
    def signedDistance (self, *args, **kwargs):
      '''
signedDistance( (PrimitiveEvaluator)arg1, (V3f)arg2, (Result)arg3) -> float :

    C++ signature :
        float signedDistance(IECoreScene::PrimitiveEvaluator {lvalue},Imath_3_1::Vec3<float>,IECoreScene::PrimitiveEvaluator::Result*)'''
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
    def surfaceArea (self, *args, **kwargs):
      '''
surfaceArea( (PrimitiveEvaluator)arg1) -> float :

    C++ signature :
        float surfaceArea(IECoreScene::PrimitiveEvaluator {lvalue})'''
    ...
    def typeId (self, *args, **kwargs):
      '''
typeId( (PrimitiveEvaluator)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreScene::PrimitiveEvaluator {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (PrimitiveEvaluator)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreScene::PrimitiveEvaluator {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...
    def validateResult (self, *args, **kwargs):
      '''
validateResult( (PrimitiveEvaluator)arg1, (Result)arg2) -> None :

    C++ signature :
        void validateResult(IECoreScene::PrimitiveEvaluator {lvalue},IECoreScene::PrimitiveEvaluator::Result*)'''
    ...
    def volume (self, *args, **kwargs):
      '''
volume( (PrimitiveEvaluator)arg1) -> float :

    C++ signature :
        float volume(IECoreScene::PrimitiveEvaluator {lvalue})'''
    ...

def PrimitiveOp (*args):
      '''
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)

'''      
    ...

class PrimitiveOp:
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
isInstanceOf( (PrimitiveOp)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::PrimitiveOp {lvalue},IECore::TypeId)

isInstanceOf( (PrimitiveOp)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::PrimitiveOp {lvalue},char const*)'''
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
typeId( (PrimitiveOp)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreScene::PrimitiveOp {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (PrimitiveOp)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreScene::PrimitiveOp {lvalue})'''
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

def PrimitiveParameter (*args):
      '''
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > name, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > description, boost::intrusive_ptr<IECoreScene::Primitive> defaultValue)
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > name, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > description, boost::intrusive_ptr<IECoreScene::Primitive> defaultValue, boost::python::api::object presets=())
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > name, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > description, boost::intrusive_ptr<IECoreScene::Primitive> defaultValue, boost::python::api::object presets=(), bool presetsOnly=False)
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > name, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > description, boost::intrusive_ptr<IECoreScene::Primitive> defaultValue, boost::python::api::object presets=(), bool presetsOnly=False, boost::intrusive_ptr<IECore::CompoundObject> userData=None)

'''      
    ...

class PrimitiveParameter:
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
isInstanceOf( (PrimitiveParameter)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECore::TypedObjectParameter<IECoreScene::Primitive> {lvalue},IECore::TypeId)

isInstanceOf( (PrimitiveParameter)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECore::TypedObjectParameter<IECoreScene::Primitive> {lvalue},char const*)'''
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
typeId( (PrimitiveParameter)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECore::TypedObjectParameter<IECoreScene::Primitive> {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (PrimitiveParameter)arg1) -> str :

    C++ signature :
        char const* typeName(IECore::TypedObjectParameter<IECoreScene::Primitive> {lvalue})'''
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
valueValid( (PrimitiveParameter)arg1, (object)arg2) -> tuple :
    Returns a tuple containing a bool specifying validity and a string giving a reason for invalidity.

    C++ signature :
        boost::python::tuple valueValid(IECore::TypedObjectParameter<IECoreScene::Primitive>,boost::intrusive_ptr<IECore::Object const>)

valueValid( (Parameter)arg1) -> tuple :
    Returns a tuple containing a bool specifying validity and a string giving a reason for invalidity.

    C++ signature :
        boost::python::tuple valueValid(IECore::Parameter)'''
    ...

def PrimitiveVariable (*args):
      '''
__init__(_object*, IECoreScene::PrimitiveVariable, bool)
__init__(_object*, IECoreScene::PrimitiveVariable)
__init__(_object*, IECoreScene::PrimitiveVariable::Interpolation, boost::intrusive_ptr<IECore::Data>, boost::intrusive_ptr<IECore::TypedData<std::vector<int, std::allocator<int> > > >)
__init__(_object*, IECoreScene::PrimitiveVariable::Interpolation, boost::intrusive_ptr<IECore::Data>)

'''      
    ...

class PrimitiveVariable:
    def Interpolation (self, *args, **kwargs):
      '''None'''
    ...
    def data (self, *args, **kwargs):
      '''None'''
    ...
    def expandedData (self, *args, **kwargs):
      '''
expandedData( (PrimitiveVariable)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::Data> expandedData(IECoreScene::PrimitiveVariable {lvalue})'''
    ...
    def indices (self, *args, **kwargs):
      '''None'''
    ...
    def interpolation (self, *args, **kwargs):
      '''None'''
    ...

def RemovePrimitiveVariables (*args):
      '''

'''      
    ...

class RemovePrimitiveVariables:
    def baseTypeId ():
      '''None'''
    ...
    def baseTypeIds (self, *args, **kwargs):
      '''
baseTypeIds( (TypeId)arg1) -> list :

    C++ signature :
        boost::python::list baseTypeIds(IECore::TypeId)'''
    ...
    def baseTypeName ():
      '''None'''
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
    def inheritsFrom (t):
      '''None'''
    ...
    def isInstanceOf (self, t):
      '''None'''
    ...
    def isSame (self, *args, **kwargs):
      '''
isSame( (RefCounted)arg1, (RefCounted)arg2) -> bool :

    C++ signature :
        bool isSame(IECore::RefCounted const*,IECore::RefCounted const*)'''
    ...
    def modifyPrimitive (self, primitive, args):
      '''None'''
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
    def staticTypeId ():
      '''None'''
    ...
    def staticTypeName ():
      '''None'''
    ...
    def typeId (x):
      '''None'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (x):
      '''None'''
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

def RemoveSmoothSkinningInfluencesOp (*args):
      '''
__init__(_object*)

'''      
    ...

class RemoveSmoothSkinningInfluencesOp:
    def Mode (self, *args, **kwargs):
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
isInstanceOf( (RemoveSmoothSkinningInfluencesOp)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::RemoveSmoothSkinningInfluencesOp {lvalue},IECore::TypeId)

isInstanceOf( (RemoveSmoothSkinningInfluencesOp)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::RemoveSmoothSkinningInfluencesOp {lvalue},char const*)'''
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
typeId( (RemoveSmoothSkinningInfluencesOp)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreScene::RemoveSmoothSkinningInfluencesOp {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (RemoveSmoothSkinningInfluencesOp)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreScene::RemoveSmoothSkinningInfluencesOp {lvalue})'''
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

def RenamePrimitiveVariables (*args):
      '''

'''      
    ...

class RenamePrimitiveVariables:
    def baseTypeId ():
      '''None'''
    ...
    def baseTypeIds (self, *args, **kwargs):
      '''
baseTypeIds( (TypeId)arg1) -> list :

    C++ signature :
        boost::python::list baseTypeIds(IECore::TypeId)'''
    ...
    def baseTypeName ():
      '''None'''
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
    def inheritsFrom (t):
      '''None'''
    ...
    def isInstanceOf (self, t):
      '''None'''
    ...
    def isSame (self, *args, **kwargs):
      '''
isSame( (RefCounted)arg1, (RefCounted)arg2) -> bool :

    C++ signature :
        bool isSame(IECore::RefCounted const*,IECore::RefCounted const*)'''
    ...
    def modifyPrimitive (self, primitive, args):
      '''None'''
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
    def staticTypeId ():
      '''None'''
    ...
    def staticTypeName ():
      '''None'''
    ...
    def typeId (x):
      '''None'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (x):
      '''None'''
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

def Renderable (*args):
      '''

'''      
    ...

class Renderable:
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
isInstanceOf( (Renderable)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::Renderable {lvalue},IECore::TypeId)

isInstanceOf( (Renderable)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::Renderable {lvalue},char const*)'''
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
typeId( (Renderable)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreScene::Renderable {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (Renderable)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreScene::Renderable {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...

def RenderableParameter (*args):
      '''
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > name, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > description, boost::intrusive_ptr<IECoreScene::Renderable> defaultValue)
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > name, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > description, boost::intrusive_ptr<IECoreScene::Renderable> defaultValue, boost::python::api::object presets=())
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > name, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > description, boost::intrusive_ptr<IECoreScene::Renderable> defaultValue, boost::python::api::object presets=(), bool presetsOnly=False)
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > name, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > description, boost::intrusive_ptr<IECoreScene::Renderable> defaultValue, boost::python::api::object presets=(), bool presetsOnly=False, boost::intrusive_ptr<IECore::CompoundObject> userData=None)

'''      
    ...

class RenderableParameter:
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
isInstanceOf( (RenderableParameter)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECore::TypedObjectParameter<IECoreScene::Renderable> {lvalue},IECore::TypeId)

isInstanceOf( (RenderableParameter)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECore::TypedObjectParameter<IECoreScene::Renderable> {lvalue},char const*)'''
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
typeId( (RenderableParameter)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECore::TypedObjectParameter<IECoreScene::Renderable> {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (RenderableParameter)arg1) -> str :

    C++ signature :
        char const* typeName(IECore::TypedObjectParameter<IECoreScene::Renderable> {lvalue})'''
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
valueValid( (RenderableParameter)arg1, (object)arg2) -> tuple :
    Returns a tuple containing a bool specifying validity and a string giving a reason for invalidity.

    C++ signature :
        boost::python::tuple valueValid(IECore::TypedObjectParameter<IECoreScene::Renderable>,boost::intrusive_ptr<IECore::Object const>)

valueValid( (Parameter)arg1) -> tuple :
    Returns a tuple containing a bool specifying validity and a string giving a reason for invalidity.

    C++ signature :
        boost::python::tuple valueValid(IECore::Parameter)'''
    ...

def Renderer (*args):
      '''

'''      
    ...

class Renderer:
    def ExternalProcedural (self, *args, **kwargs):
      '''None'''
    ...
    def Procedural (self, *args, **kwargs):
      '''None'''
    ...
    def attributeBegin (self, *args, **kwargs):
      '''
attributeBegin( (Renderer)arg1) -> None :

    C++ signature :
        void attributeBegin(IECoreScene::Renderer {lvalue})'''
    ...
    def attributeEnd (self, *args, **kwargs):
      '''
attributeEnd( (Renderer)arg1) -> None :

    C++ signature :
        void attributeEnd(IECoreScene::Renderer {lvalue})'''
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
    def camera (self, *args, **kwargs):
      '''
camera( (Renderer)arg1, (object)arg2, (dict)arg3) -> None :

    C++ signature :
        void camera(IECoreScene::Renderer {lvalue},std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >,boost::python::dict)'''
    ...
    def collectGarbage (self, *args, **kwargs):
      '''
collectGarbage() -> None :

    C++ signature :
        void collectGarbage()'''
    ...
    def command (self, *args, **kwargs):
      '''
command( (Renderer)arg1, (object)arg2, (dict)arg3) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::Data> command(IECoreScene::Renderer {lvalue},std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >,boost::python::dict)'''
    ...
    def concatTransform (self, *args, **kwargs):
      '''
concatTransform( (Renderer)arg1, (M44f)arg2) -> None :

    C++ signature :
        void concatTransform(IECoreScene::Renderer {lvalue},Imath_3_1::Matrix44<float>)'''
    ...
    def coordinateSystem (self, *args, **kwargs):
      '''
coordinateSystem( (Renderer)arg1, (object)arg2) -> None :

    C++ signature :
        void coordinateSystem(IECoreScene::Renderer {lvalue},std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)'''
    ...
    def curves (self, *args, **kwargs):
      '''
curves( (Renderer)arg1, (CubicBasisf)arg2, (bool)arg3, (object)arg4, (dict)arg5) -> None :

    C++ signature :
        void curves(IECoreScene::Renderer {lvalue},IECore::CubicBasis<float>,bool,boost::intrusive_ptr<IECore::TypedData<std::vector<int, std::allocator<int> > > const>,boost::python::dict)'''
    ...
    def derivedTypeIds (self, *args, **kwargs):
      '''
derivedTypeIds( (TypeId)arg1) -> list :

    C++ signature :
        boost::python::list derivedTypeIds(IECore::TypeId)'''
    ...
    def disk (self, *args, **kwargs):
      '''
disk( (Renderer)arg1, (float)arg2, (float)arg3, (float)arg4, (dict)arg5) -> None :

    C++ signature :
        void disk(IECoreScene::Renderer {lvalue},float,float,float,boost::python::dict)'''
    ...
    def display (self, *args, **kwargs):
      '''
display( (Renderer)arg1, (object)arg2, (object)arg3, (object)arg4, (dict)arg5) -> None :

    C++ signature :
        void display(IECoreScene::Renderer {lvalue},std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >,std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >,std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >,boost::python::dict)'''
    ...
    def editBegin (self, *args, **kwargs):
      '''
editBegin( (Renderer)arg1, (object)arg2, (dict)arg3) -> None :

    C++ signature :
        void editBegin(IECoreScene::Renderer {lvalue},std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >,boost::python::dict)'''
    ...
    def editEnd (self, *args, **kwargs):
      '''
editEnd( (Renderer)arg1) -> None :

    C++ signature :
        void editEnd(IECoreScene::Renderer {lvalue})'''
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
    def geometry (self, *args, **kwargs):
      '''
geometry( (Renderer)arg1, (object)arg2, (dict)arg3, (dict)arg4) -> None :

    C++ signature :
        void geometry(IECoreScene::Renderer {lvalue},std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >,boost::python::dict,boost::python::dict)'''
    ...
    def getAttribute (self, *args, **kwargs):
      '''
getAttribute( (Renderer)arg1, (object)arg2) -> object :
    Returns a copy of the internal attribute data.

    C++ signature :
        boost::intrusive_ptr<IECore::Data> getAttribute(IECoreScene::Renderer {lvalue},std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)'''
    ...
    def getOption (self, *args, **kwargs):
      '''
getOption( (Renderer)arg1, (object)arg2) -> object :
    Returns a copy of the internal option data.

    C++ signature :
        boost::intrusive_ptr<IECore::Data> getOption(IECoreScene::Renderer {lvalue},std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)'''
    ...
    def getTransform (self, *args, **kwargs):
      '''
getTransform( (Renderer)arg1) -> M44f :

    C++ signature :
        Imath_3_1::Matrix44<float> getTransform(IECoreScene::Renderer {lvalue})

getTransform( (Renderer)arg1, (object)arg2) -> M44f :

    C++ signature :
        Imath_3_1::Matrix44<float> getTransform(IECoreScene::Renderer {lvalue},std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)'''
    ...
    def illuminate (self, *args, **kwargs):
      '''
illuminate( (Renderer)arg1, (object)arg2, (bool)arg3) -> None :

    C++ signature :
        void illuminate(IECoreScene::Renderer {lvalue},std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >,bool)'''
    ...
    def image (self, *args, **kwargs):
      '''
image( (Renderer)arg1, (Box2i)arg2, (Box2i)arg3, (dict)arg4) -> None :

    C++ signature :
        void image(IECoreScene::Renderer {lvalue},Imath_3_1::Box<Imath_3_1::Vec2<int> >,Imath_3_1::Box<Imath_3_1::Vec2<int> >,boost::python::dict)'''
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
    def instance (self, *args, **kwargs):
      '''
instance( (Renderer)arg1, (object)arg2) -> None :

    C++ signature :
        void instance(IECoreScene::Renderer {lvalue},std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)'''
    ...
    def instanceBegin (self, *args, **kwargs):
      '''
instanceBegin( (Renderer)arg1, (object)arg2, (dict)arg3) -> None :

    C++ signature :
        void instanceBegin(IECoreScene::Renderer {lvalue},std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >,boost::python::dict)'''
    ...
    def instanceEnd (self, *args, **kwargs):
      '''
instanceEnd( (Renderer)arg1) -> None :

    C++ signature :
        void instanceEnd(IECoreScene::Renderer {lvalue})'''
    ...
    def isInstanceOf (self, *args, **kwargs):
      '''
isInstanceOf( (Renderer)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::Renderer {lvalue},IECore::TypeId)

isInstanceOf( (Renderer)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::Renderer {lvalue},char const*)'''
    ...
    def isSame (self, *args, **kwargs):
      '''
isSame( (RefCounted)arg1, (RefCounted)arg2) -> bool :

    C++ signature :
        bool isSame(IECore::RefCounted const*,IECore::RefCounted const*)'''
    ...
    def light (self, *args, **kwargs):
      '''
light( (Renderer)arg1, (object)arg2, (object)arg3, (dict)arg4) -> None :

    C++ signature :
        void light(IECoreScene::Renderer {lvalue},std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >,std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >,boost::python::dict)'''
    ...
    def mesh (self, *args, **kwargs):
      '''
mesh( (Renderer)arg1, (object)arg2, (object)arg3, (object)arg4, (dict)arg5) -> None :

    C++ signature :
        void mesh(IECoreScene::Renderer {lvalue},boost::intrusive_ptr<IECore::TypedData<std::vector<int, std::allocator<int> > > const>,boost::intrusive_ptr<IECore::TypedData<std::vector<int, std::allocator<int> > > const>,std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >,boost::python::dict)'''
    ...
    def motionBegin (self, *args, **kwargs):
      '''
motionBegin( (Renderer)arg1, (list)arg2) -> None :

    C++ signature :
        void motionBegin(IECoreScene::Renderer {lvalue},boost::python::list)'''
    ...
    def motionEnd (self, *args, **kwargs):
      '''
motionEnd( (Renderer)arg1) -> None :

    C++ signature :
        void motionEnd(IECoreScene::Renderer {lvalue})'''
    ...
    def numWrappedInstances (self, *args, **kwargs):
      '''
numWrappedInstances() -> int :

    C++ signature :
        unsigned long numWrappedInstances()'''
    ...
    def nurbs (self, *args, **kwargs):
      '''
nurbs( (Renderer)arg1, (int)arg2, (object)arg3, (float)arg4, (float)arg5, (int)arg6, (object)arg7, (float)arg8, (float)arg9, (dict)arg10) -> None :

    C++ signature :
        void nurbs(IECoreScene::Renderer {lvalue},int,boost::intrusive_ptr<IECore::TypedData<std::vector<float, std::allocator<float> > > const>,float,float,int,boost::intrusive_ptr<IECore::TypedData<std::vector<float, std::allocator<float> > > const>,float,float,boost::python::dict)'''
    ...
    def patchMesh (self, *args, **kwargs):
      '''
patchMesh( (Renderer)arg1, (CubicBasisf)arg2, (CubicBasisf)arg3, (int)arg4, (bool)arg5, (int)arg6, (bool)arg7, (dict)arg8) -> None :

    C++ signature :
        void patchMesh(IECoreScene::Renderer {lvalue},IECore::CubicBasis<float>,IECore::CubicBasis<float>,int,bool,int,bool,boost::python::dict)'''
    ...
    def points (self, *args, **kwargs):
      '''
points( (Renderer)arg1, (int)arg2, (dict)arg3) -> None :

    C++ signature :
        void points(IECoreScene::Renderer {lvalue},unsigned long,boost::python::dict)'''
    ...
    def procedural (self, *args, **kwargs):
      '''
procedural( (Renderer)arg1, (object)arg2) -> None :

    C++ signature :
        void procedural(IECoreScene::Renderer {lvalue},boost::intrusive_ptr<IECoreScene::Renderer::Procedural>)'''
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
    def setAttribute (self, *args, **kwargs):
      '''
setAttribute( (Renderer)arg1, (object)arg2, (object)arg3) -> None :

    C++ signature :
        void setAttribute(IECoreScene::Renderer {lvalue},std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >,boost::intrusive_ptr<IECore::Data const>)'''
    ...
    def setOption (self, *args, **kwargs):
      '''
setOption( (Renderer)arg1, (object)arg2, (object)arg3) -> None :

    C++ signature :
        void setOption(IECoreScene::Renderer {lvalue},std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >,boost::intrusive_ptr<IECore::Data const>)'''
    ...
    def setTransform (self, *args, **kwargs):
      '''
setTransform( (Renderer)arg1, (M44f)arg2) -> None :

    C++ signature :
        void setTransform(IECoreScene::Renderer {lvalue},Imath_3_1::Matrix44<float>)

setTransform( (Renderer)arg1, (object)arg2) -> None :

    C++ signature :
        void setTransform(IECoreScene::Renderer {lvalue},std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)'''
    ...
    def shader (self, *args, **kwargs):
      '''
shader( (Renderer)arg1, (object)arg2, (object)arg3, (dict)arg4) -> None :

    C++ signature :
        void shader(IECoreScene::Renderer {lvalue},std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >,std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >,boost::python::dict)'''
    ...
    def sphere (self, *args, **kwargs):
      '''
sphere( (Renderer)arg1, (float)arg2, (float)arg3, (float)arg4, (float)arg5, (dict)arg6) -> None :

    C++ signature :
        void sphere(IECoreScene::Renderer {lvalue},float,float,float,float,boost::python::dict)'''
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
    def text (self, *args, **kwargs):
      '''
text( (Renderer)arg1, (object)arg2, (object)arg3, (float)arg4, (dict)arg5) -> None :

    C++ signature :
        void text(IECoreScene::Renderer {lvalue},std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >,std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >,float,boost::python::dict)'''
    ...
    def transformBegin (self, *args, **kwargs):
      '''
transformBegin( (Renderer)arg1) -> None :

    C++ signature :
        void transformBegin(IECoreScene::Renderer {lvalue})'''
    ...
    def transformEnd (self, *args, **kwargs):
      '''
transformEnd( (Renderer)arg1) -> None :

    C++ signature :
        void transformEnd(IECoreScene::Renderer {lvalue})'''
    ...
    def typeId (self, *args, **kwargs):
      '''
typeId( (Renderer)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreScene::Renderer {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (Renderer)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreScene::Renderer {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...
    def worldBegin (self, *args, **kwargs):
      '''
worldBegin( (Renderer)arg1) -> None :

    C++ signature :
        void worldBegin(IECoreScene::Renderer {lvalue})'''
    ...
    def worldEnd (self, *args, **kwargs):
      '''
worldEnd( (Renderer)arg1) -> None :

    C++ signature :
        void worldEnd(IECoreScene::Renderer {lvalue})'''
    ...

def ReorderSmoothSkinningInfluencesOp (*args):
      '''
__init__(_object*)

'''      
    ...

class ReorderSmoothSkinningInfluencesOp:
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
isInstanceOf( (ReorderSmoothSkinningInfluencesOp)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::ReorderSmoothSkinningInfluencesOp {lvalue},IECore::TypeId)

isInstanceOf( (ReorderSmoothSkinningInfluencesOp)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::ReorderSmoothSkinningInfluencesOp {lvalue},char const*)'''
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
typeId( (ReorderSmoothSkinningInfluencesOp)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreScene::ReorderSmoothSkinningInfluencesOp {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (ReorderSmoothSkinningInfluencesOp)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreScene::ReorderSmoothSkinningInfluencesOp {lvalue})'''
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

def SWAReader (*args):
      '''

'''      
    ...

class SWAReader:
    def baseTypeId ():
      '''None'''
    ...
    def baseTypeIds (self, *args, **kwargs):
      '''
baseTypeIds( (TypeId)arg1) -> list :

    C++ signature :
        boost::python::list baseTypeIds(IECore::TypeId)'''
    ...
    def baseTypeName ():
      '''None'''
    ...
    def canRead (fileName):
      '''None'''
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
    def derivedTypeIds (self, *args, **kwargs):
      '''
derivedTypeIds( (TypeId)arg1) -> list :

    C++ signature :
        boost::python::list derivedTypeIds(IECore::TypeId)'''
    ...
    def description (self, *args, **kwargs):
      '''None'''
    ...
    def doOperation (self, args):
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
    def inheritsFrom (t):
      '''None'''
    ...
    def isInstanceOf (self, t):
      '''None'''
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
read( (Reader)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::Object> read(IECore::Reader {lvalue})'''
    ...
    def readHeader (self, *args, **kwargs):
      '''
readHeader( (Reader)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::CompoundObject> readHeader(IECore::Reader {lvalue})'''
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
    def staticTypeId ():
      '''None'''
    ...
    def staticTypeName ():
      '''None'''
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
    def typeId (x):
      '''None'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (x):
      '''None'''
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

def SampledSceneInterface (*args):
      '''

'''      
    ...

class SampledSceneInterface:
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
isInstanceOf( (SampledSceneInterface)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::SampledSceneInterface {lvalue},IECore::TypeId)

isInstanceOf( (SampledSceneInterface)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::SampledSceneInterface {lvalue},char const*)'''
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
typeId( (SampledSceneInterface)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreScene::SampledSceneInterface {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (SampledSceneInterface)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreScene::SampledSceneInterface {lvalue})'''
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

def SceneAlgo (*args):
      '''

'''      
    ...

def SceneCache (*args):
      '''
__init__(boost::python::api::object, boost::intrusive_ptr<IECore::IndexedIO>)
__init__(boost::python::api::object, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, unsigned int)

'''      
    ...

class SceneCache:
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
isInstanceOf( (SceneCache)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::SceneCache {lvalue},IECore::TypeId)

isInstanceOf( (SceneCache)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::SceneCache {lvalue},char const*)'''
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
typeId( (SceneCache)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreScene::SceneCache {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (SceneCache)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreScene::SceneCache {lvalue})'''
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

def SceneInterface (*args):
      '''

'''      
    ...

class SceneInterface:
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
isInstanceOf( (SceneInterface)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::SceneInterface {lvalue},IECore::TypeId)

isInstanceOf( (SceneInterface)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::SceneInterface {lvalue},char const*)'''
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
    def numWrappedInstances (self, *args, **kwargs):
      '''
numWrappedInstances() -> int :

    C++ signature :
        unsigned long numWrappedInstances()'''
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
    def readBound (self, *args, **kwargs):
      '''
readBound( (SceneInterface)arg1, (float)arg2) -> Box3d :

    C++ signature :
        Imath_3_1::Box<Imath_3_1::Vec3<double> > readBound(IECoreScene::SceneInterface {lvalue},double)'''
    ...
    def readObject (self, *args, **kwargs):
      '''
readObject( (SceneInterface)arg1, (float)time [, (Canceller)canceller=None [, (bool)_copy=True]]) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::Object> readObject(IECoreScene::SceneInterface {lvalue},double [,IECore::Canceller const*=None [,bool=True]])'''
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
    def typeId (self, *args, **kwargs):
      '''
typeId( (SceneInterface)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreScene::SceneInterface {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (SceneInterface)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreScene::SceneInterface {lvalue})'''
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

def Shader (*args):
      '''
__init__(boost::python::api::object, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > name='defaultsurface', std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > type='surface', boost::intrusive_ptr<IECore::CompoundData> parameters=0)
__init__(_object*)
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::map<IECore::InternedString, boost::intrusive_ptr<IECore::Data>, std::less<IECore::InternedString>, std::allocator<std::pair<IECore::InternedString const, boost::intrusive_ptr<IECore::Data> > > >)
__init__(_object*)

'''      
    ...

class Shader:
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
isInstanceOf( (Shader)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::Shader {lvalue},IECore::TypeId)

isInstanceOf( (Shader)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::Shader {lvalue},char const*)'''
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
    def name (self, *args, **kwargs):
      '''None'''
    ...
    def numWrappedInstances (self, *args, **kwargs):
      '''
numWrappedInstances() -> int :

    C++ signature :
        unsigned long numWrappedInstances()'''
    ...
    def parameters (self, *args, **kwargs):
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
registerType( (TypeId)typeId, (object)typeName [, (object)creator=None]) -> None :

    C++ signature :
        void registerType(IECore::TypeId,std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > [,boost::python::api::object=None])'''
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
    def type (self, *args, **kwargs):
      '''None'''
    ...
    def typeId (self, *args, **kwargs):
      '''
typeId( (Shader)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreScene::Shader {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (Shader)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreScene::Shader {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...

def ShaderNetwork (*args):
      '''
__init__(boost::python::api::object, boost::python::dict shaders={}, boost::python::list connections=[], boost::python::api::object output=None)
__init__(_object*)

'''      
    ...

class ShaderNetwork:
    def Connection (self, *args, **kwargs):
      '''None'''
    ...
    def Parameter (self, *args, **kwargs):
      '''None'''
    ...
    def addConnection (self, *args, **kwargs):
      '''
addConnection( (ShaderNetwork)arg1, (Connection)arg2) -> None :

    C++ signature :
        void addConnection(IECoreScene::ShaderNetwork {lvalue},IECoreScene::ShaderNetwork::Connection)'''
    ...
    def addShader (self, *args, **kwargs):
      '''
addShader( (ShaderNetwork)arg1, (InternedString)handle, (Shader)shader) -> str :

    C++ signature :
        char const* addShader(IECoreScene::ShaderNetwork {lvalue},IECore::InternedString,IECoreScene::Shader)'''
    ...
    def applySubstitutions (self, *args, **kwargs):
      '''
applySubstitutions( (ShaderNetwork)arg1, (CompoundObject)arg2) -> None :

    C++ signature :
        void applySubstitutions(IECoreScene::ShaderNetwork {lvalue},IECore::CompoundObject const*)'''
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
    def getOutput (self, *args, **kwargs):
      '''
getOutput( (ShaderNetwork)arg1) -> Parameter :

    C++ signature :
        IECoreScene::ShaderNetwork::Parameter getOutput(IECoreScene::ShaderNetwork {lvalue})'''
    ...
    def getShader (self, *args, **kwargs):
      '''
getShader( (ShaderNetwork)arg1, (InternedString)handle [, (bool)_copy=True]) -> object :

    C++ signature :
        boost::intrusive_ptr<IECoreScene::Shader> getShader(IECoreScene::ShaderNetwork,IECore::InternedString [,bool=True])'''
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
    def hashSubstitutions (self, *args, **kwargs):
      '''
hashSubstitutions( (ShaderNetwork)arg1, (CompoundObject)arg2, (MurmurHash)arg3) -> None :

    C++ signature :
        void hashSubstitutions(IECoreScene::ShaderNetwork {lvalue},IECore::CompoundObject const*,IECore::MurmurHash {lvalue})'''
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
    def input (self, *args, **kwargs):
      '''
input( (ShaderNetwork)arg1, (Parameter)arg2) -> Parameter :

    C++ signature :
        IECoreScene::ShaderNetwork::Parameter input(IECoreScene::ShaderNetwork {lvalue},IECoreScene::ShaderNetwork::Parameter)'''
    ...
    def inputConnections (self, *args, **kwargs):
      '''
inputConnections( (ShaderNetwork)arg1, (InternedString)arg2) -> list :

    C++ signature :
        boost::python::list inputConnections(IECoreScene::ShaderNetwork,IECore::InternedString)'''
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
isInstanceOf( (ShaderNetwork)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::ShaderNetwork {lvalue},IECore::TypeId)

isInstanceOf( (ShaderNetwork)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::ShaderNetwork {lvalue},char const*)'''
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
    def numWrappedInstances (self, *args, **kwargs):
      '''
numWrappedInstances() -> int :

    C++ signature :
        unsigned long numWrappedInstances()'''
    ...
    def outputConnections (self, *args, **kwargs):
      '''
outputConnections( (ShaderNetwork)arg1, (InternedString)arg2) -> list :

    C++ signature :
        boost::python::list outputConnections(IECoreScene::ShaderNetwork,IECore::InternedString)'''
    ...
    def outputShader (self, *args, **kwargs):
      '''
outputShader( (ShaderNetwork)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECoreScene::Shader> outputShader(IECoreScene::ShaderNetwork)'''
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
    def removeConnection (self, *args, **kwargs):
      '''
removeConnection( (ShaderNetwork)arg1, (Connection)arg2) -> None :

    C++ signature :
        void removeConnection(IECoreScene::ShaderNetwork {lvalue},IECoreScene::ShaderNetwork::Connection)'''
    ...
    def removeShader (self, *args, **kwargs):
      '''
removeShader( (ShaderNetwork)arg1, (InternedString)arg2) -> None :

    C++ signature :
        void removeShader(IECoreScene::ShaderNetwork {lvalue},IECore::InternedString)'''
    ...
    def save (self, *args, **kwargs):
      '''
save( (Object)arg1, (object)arg2, (InternedString)arg3) -> None :

    C++ signature :
        void save(IECore::Object {lvalue},boost::intrusive_ptr<IECore::IndexedIO>,IECore::InternedString)'''
    ...
    def setOutput (self, *args, **kwargs):
      '''
setOutput( (ShaderNetwork)arg1, (Parameter)arg2) -> None :

    C++ signature :
        void setOutput(IECoreScene::ShaderNetwork {lvalue},IECoreScene::ShaderNetwork::Parameter)'''
    ...
    def setShader (self, *args, **kwargs):
      '''
setShader( (ShaderNetwork)arg1, (InternedString)handle, (Shader)shader) -> None :

    C++ signature :
        void setShader(IECoreScene::ShaderNetwork {lvalue},IECore::InternedString,IECoreScene::Shader)'''
    ...
    def shaders (self, *args, **kwargs):
      '''
shaders( (ShaderNetwork)arg1) -> dict :

    C++ signature :
        boost::python::dict shaders(IECoreScene::ShaderNetwork {lvalue})'''
    ...
    def size (self, *args, **kwargs):
      '''
size( (ShaderNetwork)arg1) -> int :

    C++ signature :
        unsigned long size(IECoreScene::ShaderNetwork {lvalue})'''
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
typeId( (ShaderNetwork)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreScene::ShaderNetwork {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (ShaderNetwork)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreScene::ShaderNetwork {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...

def ShaderNetworkAlgo (*args):
      '''

'''      
    ...

def ShaderParameter (*args):
      '''
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > name, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > description, boost::intrusive_ptr<IECoreScene::Shader> defaultValue)
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > name, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > description, boost::intrusive_ptr<IECoreScene::Shader> defaultValue, boost::python::api::object presets=())
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > name, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > description, boost::intrusive_ptr<IECoreScene::Shader> defaultValue, boost::python::api::object presets=(), bool presetsOnly=False)
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > name, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > description, boost::intrusive_ptr<IECoreScene::Shader> defaultValue, boost::python::api::object presets=(), bool presetsOnly=False, boost::intrusive_ptr<IECore::CompoundObject> userData=None)

'''      
    ...

class ShaderParameter:
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
isInstanceOf( (ShaderParameter)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECore::TypedObjectParameter<IECoreScene::Shader> {lvalue},IECore::TypeId)

isInstanceOf( (ShaderParameter)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECore::TypedObjectParameter<IECoreScene::Shader> {lvalue},char const*)'''
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
typeId( (ShaderParameter)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECore::TypedObjectParameter<IECoreScene::Shader> {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (ShaderParameter)arg1) -> str :

    C++ signature :
        char const* typeName(IECore::TypedObjectParameter<IECoreScene::Shader> {lvalue})'''
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
valueValid( (ShaderParameter)arg1, (object)arg2) -> tuple :
    Returns a tuple containing a bool specifying validity and a string giving a reason for invalidity.

    C++ signature :
        boost::python::tuple valueValid(IECore::TypedObjectParameter<IECoreScene::Shader>,boost::intrusive_ptr<IECore::Object const>)

valueValid( (Parameter)arg1) -> tuple :
    Returns a tuple containing a bool specifying validity and a string giving a reason for invalidity.

    C++ signature :
        boost::python::tuple valueValid(IECore::Parameter)'''
    ...

def SharedSceneInterfaces (*args):
      '''
__init__(_object*)

'''      
    ...

class SharedSceneInterfaces:
    def clear (self, *args, **kwargs):
      '''
clear() -> None :

    C++ signature :
        void clear()'''
    ...
    def erase (self, *args, **kwargs):
      '''
erase( (object)arg1) -> None :

    C++ signature :
        void erase(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)'''
    ...
    def get (self, *args, **kwargs):
      '''
get( (object)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECoreScene::SceneInterface> get(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)'''
    ...
    def getMaxScenes (self, *args, **kwargs):
      '''
getMaxScenes() -> int :

    C++ signature :
        unsigned long getMaxScenes()'''
    ...
    def numScenes (self, *args, **kwargs):
      '''
numScenes() -> int :

    C++ signature :
        unsigned long numScenes()'''
    ...
    def setMaxScenes (self, *args, **kwargs):
      '''
setMaxScenes( (int)arg1) -> None :

    C++ signature :
        void setMaxScenes(unsigned long)'''
    ...

def SmoothSkinningData (*args):
      '''
__init__(_object*, boost::intrusive_ptr<IECore::TypedData<std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > > >, boost::intrusive_ptr<IECore::TypedData<std::vector<Imath_3_1::Matrix44<float>, std::allocator<Imath_3_1::Matrix44<float> > > > >, boost::intrusive_ptr<IECore::TypedData<std::vector<int, std::allocator<int> > > >, boost::intrusive_ptr<IECore::TypedData<std::vector<int, std::allocator<int> > > >, boost::intrusive_ptr<IECore::TypedData<std::vector<int, std::allocator<int> > > >, boost::intrusive_ptr<IECore::TypedData<std::vector<float, std::allocator<float> > > >)
__init__(_object*)

'''      
    ...

class SmoothSkinningData:
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
    def hash (self, *args, **kwargs):
      '''
hash( (Object)arg1) -> MurmurHash :

    C++ signature :
        IECore::MurmurHash hash(IECore::Object {lvalue})

hash( (Object)arg1, (MurmurHash)arg2) -> None :

    C++ signature :
        void hash(IECore::Object {lvalue},IECore::MurmurHash {lvalue})'''
    ...
    def influenceNames (self, *args, **kwargs):
      '''
influenceNames( (SmoothSkinningData)arg1) -> object :
    A copy of the list of influence object names

    C++ signature :
        boost::intrusive_ptr<IECore::TypedData<std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > > > influenceNames(IECoreScene::SmoothSkinningData {lvalue})'''
    ...
    def influencePose (self, *args, **kwargs):
      '''
influencePose( (SmoothSkinningData)arg1) -> object :
    A copy of the list of influence pose matrices (bindPose)

    C++ signature :
        boost::intrusive_ptr<IECore::TypedData<std::vector<Imath_3_1::Matrix44<float>, std::allocator<Imath_3_1::Matrix44<float> > > > > influencePose(IECoreScene::SmoothSkinningData {lvalue})'''
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
isInstanceOf( (SmoothSkinningData)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::SmoothSkinningData {lvalue},IECore::TypeId)

isInstanceOf( (SmoothSkinningData)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::SmoothSkinningData {lvalue},char const*)'''
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
    def numWrappedInstances (self, *args, **kwargs):
      '''
numWrappedInstances() -> int :

    C++ signature :
        unsigned long numWrappedInstances()'''
    ...
    def pointIndexOffsets (self, *args, **kwargs):
      '''
pointIndexOffsets( (SmoothSkinningData)arg1) -> object :
    A copy of the list of per point offsets into the influence index and weight data

    C++ signature :
        boost::intrusive_ptr<IECore::TypedData<std::vector<int, std::allocator<int> > > > pointIndexOffsets(IECoreScene::SmoothSkinningData {lvalue})'''
    ...
    def pointInfluenceCounts (self, *args, **kwargs):
      '''
pointInfluenceCounts( (SmoothSkinningData)arg1) -> object :
    A copy of the list of per point number of influence objects

    C++ signature :
        boost::intrusive_ptr<IECore::TypedData<std::vector<int, std::allocator<int> > > > pointInfluenceCounts(IECoreScene::SmoothSkinningData {lvalue})'''
    ...
    def pointInfluenceIndices (self, *args, **kwargs):
      '''
pointInfluenceIndices( (SmoothSkinningData)arg1) -> object :
    A copy of the list of per point per influence indices

    C++ signature :
        boost::intrusive_ptr<IECore::TypedData<std::vector<int, std::allocator<int> > > > pointInfluenceIndices(IECoreScene::SmoothSkinningData {lvalue})'''
    ...
    def pointInfluenceWeights (self, *args, **kwargs):
      '''
pointInfluenceWeights( (SmoothSkinningData)arg1) -> object :
    A copy of the list of per point per influence weights

    C++ signature :
        boost::intrusive_ptr<IECore::TypedData<std::vector<float, std::allocator<float> > > > pointInfluenceWeights(IECoreScene::SmoothSkinningData {lvalue})'''
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
typeId( (SmoothSkinningData)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreScene::SmoothSkinningData {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (SmoothSkinningData)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreScene::SmoothSkinningData {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...
    def validate (self, *args, **kwargs):
      '''
validate( (SmoothSkinningData)arg1) -> None :
    Validate the smooth skinning data in the object

    C++ signature :
        void validate(IECoreScene::SmoothSkinningData {lvalue})'''
    ...

def SmoothSkinningDataParameter (*args):
      '''
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > name, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > description, boost::intrusive_ptr<IECoreScene::SmoothSkinningData> defaultValue)
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > name, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > description, boost::intrusive_ptr<IECoreScene::SmoothSkinningData> defaultValue, boost::python::api::object presets=())
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > name, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > description, boost::intrusive_ptr<IECoreScene::SmoothSkinningData> defaultValue, boost::python::api::object presets=(), bool presetsOnly=False)
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > name, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > description, boost::intrusive_ptr<IECoreScene::SmoothSkinningData> defaultValue, boost::python::api::object presets=(), bool presetsOnly=False, boost::intrusive_ptr<IECore::CompoundObject> userData=None)

'''      
    ...

class SmoothSkinningDataParameter:
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
isInstanceOf( (SmoothSkinningDataParameter)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECore::TypedObjectParameter<IECoreScene::SmoothSkinningData> {lvalue},IECore::TypeId)

isInstanceOf( (SmoothSkinningDataParameter)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECore::TypedObjectParameter<IECoreScene::SmoothSkinningData> {lvalue},char const*)'''
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
typeId( (SmoothSkinningDataParameter)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECore::TypedObjectParameter<IECoreScene::SmoothSkinningData> {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (SmoothSkinningDataParameter)arg1) -> str :

    C++ signature :
        char const* typeName(IECore::TypedObjectParameter<IECoreScene::SmoothSkinningData> {lvalue})'''
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
valueValid( (SmoothSkinningDataParameter)arg1, (object)arg2) -> tuple :
    Returns a tuple containing a bool specifying validity and a string giving a reason for invalidity.

    C++ signature :
        boost::python::tuple valueValid(IECore::TypedObjectParameter<IECoreScene::SmoothSkinningData>,boost::intrusive_ptr<IECore::Object const>)

valueValid( (Parameter)arg1) -> tuple :
    Returns a tuple containing a bool specifying validity and a string giving a reason for invalidity.

    C++ signature :
        boost::python::tuple valueValid(IECore::Parameter)'''
    ...

def SmoothSmoothSkinningWeightsOp (*args):
      '''
__init__(_object*)

'''      
    ...

class SmoothSmoothSkinningWeightsOp:
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
isInstanceOf( (SmoothSmoothSkinningWeightsOp)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::SmoothSmoothSkinningWeightsOp {lvalue},IECore::TypeId)

isInstanceOf( (SmoothSmoothSkinningWeightsOp)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::SmoothSmoothSkinningWeightsOp {lvalue},char const*)'''
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
typeId( (SmoothSmoothSkinningWeightsOp)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreScene::SmoothSmoothSkinningWeightsOp {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (SmoothSmoothSkinningWeightsOp)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreScene::SmoothSmoothSkinningWeightsOp {lvalue})'''
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

def SpherePrimitive (*args):
      '''
__init__(_object*, float)
__init__(_object*, float, float)
__init__(_object*, float, float, float)
__init__(_object*, float, float, float, float)
__init__(_object*)

'''      
    ...

class SpherePrimitive:
    def arePrimitiveVariablesValid (self, *args, **kwargs):
      '''
arePrimitiveVariablesValid( (Primitive)arg1) -> bool :

    C++ signature :
        bool arePrimitiveVariablesValid(IECoreScene::Primitive {lvalue})'''
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
    def hash (self, *args, **kwargs):
      '''
hash( (Object)arg1) -> MurmurHash :

    C++ signature :
        IECore::MurmurHash hash(IECore::Object {lvalue})

hash( (Object)arg1, (MurmurHash)arg2) -> None :

    C++ signature :
        void hash(IECore::Object {lvalue},IECore::MurmurHash {lvalue})'''
    ...
    def inferInterpolation (self, *args, **kwargs):
      '''
inferInterpolation( (Primitive)arg1, (Data)arg2) -> Interpolation :

    C++ signature :
        IECoreScene::PrimitiveVariable::Interpolation inferInterpolation(IECoreScene::Primitive {lvalue},IECore::Data const*)

inferInterpolation( (Primitive)arg1, (int)arg2) -> Interpolation :

    C++ signature :
        IECoreScene::PrimitiveVariable::Interpolation inferInterpolation(IECoreScene::Primitive {lvalue},unsigned long)'''
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
isInstanceOf( (SpherePrimitive)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::SpherePrimitive {lvalue},IECore::TypeId)

isInstanceOf( (SpherePrimitive)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::SpherePrimitive {lvalue},char const*)'''
    ...
    def isPrimitiveVariableValid (self, *args, **kwargs):
      '''
isPrimitiveVariableValid( (Primitive)arg1, (PrimitiveVariable)arg2) -> bool :

    C++ signature :
        bool isPrimitiveVariableValid(IECoreScene::Primitive {lvalue},IECoreScene::PrimitiveVariable)'''
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
keys( (Primitive)arg1) -> list :

    C++ signature :
        boost::python::list keys(IECoreScene::Primitive {lvalue})'''
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
    def numWrappedInstances (self, *args, **kwargs):
      '''
numWrappedInstances() -> int :

    C++ signature :
        unsigned long numWrappedInstances()'''
    ...
    def radius (self, *args, **kwargs):
      '''
radius( (SpherePrimitive)arg1) -> float :

    C++ signature :
        float radius(IECoreScene::SpherePrimitive {lvalue})'''
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
    def setRadius (self, *args, **kwargs):
      '''
setRadius( (SpherePrimitive)arg1, (float)arg2) -> None :

    C++ signature :
        void setRadius(IECoreScene::SpherePrimitive {lvalue},float)'''
    ...
    def setThetaMax (self, *args, **kwargs):
      '''
setThetaMax( (SpherePrimitive)arg1, (float)arg2) -> None :

    C++ signature :
        void setThetaMax(IECoreScene::SpherePrimitive {lvalue},float)'''
    ...
    def setZMax (self, *args, **kwargs):
      '''
setZMax( (SpherePrimitive)arg1, (float)arg2) -> None :

    C++ signature :
        void setZMax(IECoreScene::SpherePrimitive {lvalue},float)'''
    ...
    def setZMin (self, *args, **kwargs):
      '''
setZMin( (SpherePrimitive)arg1, (float)arg2) -> None :

    C++ signature :
        void setZMin(IECoreScene::SpherePrimitive {lvalue},float)'''
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
    def thetaMax (self, *args, **kwargs):
      '''
thetaMax( (SpherePrimitive)arg1) -> float :

    C++ signature :
        float thetaMax(IECoreScene::SpherePrimitive {lvalue})'''
    ...
    def topologyHash (self, *args, **kwargs):
      '''
topologyHash( (Primitive)arg1) -> MurmurHash :

    C++ signature :
        IECore::MurmurHash topologyHash(IECoreScene::Primitive {lvalue})

topologyHash( (Primitive)arg1, (MurmurHash)arg2) -> None :

    C++ signature :
        void topologyHash(IECoreScene::Primitive {lvalue},IECore::MurmurHash {lvalue})'''
    ...
    def typeId (self, *args, **kwargs):
      '''
typeId( (SpherePrimitive)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreScene::SpherePrimitive {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (SpherePrimitive)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreScene::SpherePrimitive {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...
    def values (self, *args, **kwargs):
      '''
values( (Primitive)arg1) -> list :
    Returns a list containing shallow copies of the PrimitiveVariable objects held.

    C++ signature :
        boost::python::list values(IECoreScene::Primitive {lvalue})'''
    ...
    def variableSize (self, *args, **kwargs):
      '''
variableSize( (Primitive)arg1, (Interpolation)arg2) -> int :

    C++ signature :
        unsigned long variableSize(IECoreScene::Primitive {lvalue},IECoreScene::PrimitiveVariable::Interpolation)'''
    ...
    def zMax (self, *args, **kwargs):
      '''
zMax( (SpherePrimitive)arg1) -> float :

    C++ signature :
        float zMax(IECoreScene::SpherePrimitive {lvalue})'''
    ...
    def zMin (self, *args, **kwargs):
      '''
zMin( (SpherePrimitive)arg1) -> float :

    C++ signature :
        float zMin(IECoreScene::SpherePrimitive {lvalue})'''
    ...

def SpherePrimitiveEvaluator (*args):
      '''
__init__(_object*, boost::intrusive_ptr<IECoreScene::SpherePrimitive>)

'''      
    ...

class SpherePrimitiveEvaluator:
    def Result (self, *args, **kwargs):
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
    def centerOfGravity (self, *args, **kwargs):
      '''
centerOfGravity( (PrimitiveEvaluator)arg1) -> V3f :

    C++ signature :
        Imath_3_1::Vec3<float> centerOfGravity(IECoreScene::PrimitiveEvaluator {lvalue})'''
    ...
    def closestPoint (self, *args, **kwargs):
      '''
closestPoint( (PrimitiveEvaluator)arg1, (V3f)arg2, (Result)arg3) -> bool :

    C++ signature :
        bool closestPoint(IECoreScene::PrimitiveEvaluator {lvalue},Imath_3_1::Vec3<float>,IECoreScene::PrimitiveEvaluator::Result*)'''
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
        boost::intrusive_ptr<IECoreScene::PrimitiveEvaluator> create(boost::intrusive_ptr<IECoreScene::Primitive>)'''
    ...
    def createResult (self, *args, **kwargs):
      '''
createResult( (PrimitiveEvaluator)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECoreScene::PrimitiveEvaluator::Result> createResult(IECoreScene::PrimitiveEvaluator {lvalue})'''
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
    def intersectionPoint (self, *args, **kwargs):
      '''
intersectionPoint( (PrimitiveEvaluator)arg1, (V3f)arg2, (V3f)arg3, (Result)arg4) -> bool :

    C++ signature :
        bool intersectionPoint(IECoreScene::PrimitiveEvaluator {lvalue},Imath_3_1::Vec3<float>,Imath_3_1::Vec3<float>,IECoreScene::PrimitiveEvaluator::Result*)

intersectionPoint( (PrimitiveEvaluator)arg1, (V3f)arg2, (V3f)arg3, (Result)arg4, (float)arg5) -> bool :

    C++ signature :
        bool intersectionPoint(IECoreScene::PrimitiveEvaluator {lvalue},Imath_3_1::Vec3<float>,Imath_3_1::Vec3<float>,IECoreScene::PrimitiveEvaluator::Result*,float)'''
    ...
    def intersectionPoints (self, *args, **kwargs):
      '''
intersectionPoints( (PrimitiveEvaluator)arg1, (V3f)arg2, (V3f)arg3) -> list :

    C++ signature :
        boost::python::list intersectionPoints(IECoreScene::PrimitiveEvaluator {lvalue},Imath_3_1::Vec3<float>,Imath_3_1::Vec3<float>)

intersectionPoints( (PrimitiveEvaluator)arg1, (V3f)arg2, (V3f)arg3, (float)arg4) -> list :

    C++ signature :
        boost::python::list intersectionPoints(IECoreScene::PrimitiveEvaluator {lvalue},Imath_3_1::Vec3<float>,Imath_3_1::Vec3<float>,float)'''
    ...
    def isInstanceOf (self, *args, **kwargs):
      '''
isInstanceOf( (SpherePrimitiveEvaluator)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::SpherePrimitiveEvaluator {lvalue},IECore::TypeId)

isInstanceOf( (SpherePrimitiveEvaluator)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::SpherePrimitiveEvaluator {lvalue},char const*)'''
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
    def pointAtUV (self, *args, **kwargs):
      '''
pointAtUV( (PrimitiveEvaluator)arg1, (V2f)arg2, (Result)arg3) -> bool :

    C++ signature :
        bool pointAtUV(IECoreScene::PrimitiveEvaluator {lvalue},Imath_3_1::Vec2<float>,IECoreScene::PrimitiveEvaluator::Result*)'''
    ...
    def primitive (self, *args, **kwargs):
      '''
primitive( (PrimitiveEvaluator)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECoreScene::Primitive> primitive(IECoreScene::PrimitiveEvaluator {lvalue})'''
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
    def signedDistance (self, *args, **kwargs):
      '''
signedDistance( (PrimitiveEvaluator)arg1, (V3f)arg2, (Result)arg3) -> float :

    C++ signature :
        float signedDistance(IECoreScene::PrimitiveEvaluator {lvalue},Imath_3_1::Vec3<float>,IECoreScene::PrimitiveEvaluator::Result*)'''
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
    def surfaceArea (self, *args, **kwargs):
      '''
surfaceArea( (PrimitiveEvaluator)arg1) -> float :

    C++ signature :
        float surfaceArea(IECoreScene::PrimitiveEvaluator {lvalue})'''
    ...
    def typeId (self, *args, **kwargs):
      '''
typeId( (SpherePrimitiveEvaluator)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreScene::SpherePrimitiveEvaluator {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (SpherePrimitiveEvaluator)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreScene::SpherePrimitiveEvaluator {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...
    def validateResult (self, *args, **kwargs):
      '''
validateResult( (PrimitiveEvaluator)arg1, (Result)arg2) -> None :

    C++ signature :
        void validateResult(IECoreScene::PrimitiveEvaluator {lvalue},IECoreScene::PrimitiveEvaluator::Result*)'''
    ...
    def volume (self, *args, **kwargs):
      '''
volume( (PrimitiveEvaluator)arg1) -> float :

    C++ signature :
        float volume(IECoreScene::PrimitiveEvaluator {lvalue})'''
    ...

def StateRenderable (*args):
      '''

'''      
    ...

class StateRenderable:
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
isInstanceOf( (StateRenderable)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::StateRenderable {lvalue},IECore::TypeId)

isInstanceOf( (StateRenderable)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::StateRenderable {lvalue},char const*)'''
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
typeId( (StateRenderable)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreScene::StateRenderable {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (StateRenderable)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreScene::StateRenderable {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...

def StateRenderableParameter (*args):
      '''
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > name, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > description, boost::intrusive_ptr<IECoreScene::StateRenderable> defaultValue)
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > name, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > description, boost::intrusive_ptr<IECoreScene::StateRenderable> defaultValue, boost::python::api::object presets=())
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > name, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > description, boost::intrusive_ptr<IECoreScene::StateRenderable> defaultValue, boost::python::api::object presets=(), bool presetsOnly=False)
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > name, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > description, boost::intrusive_ptr<IECoreScene::StateRenderable> defaultValue, boost::python::api::object presets=(), bool presetsOnly=False, boost::intrusive_ptr<IECore::CompoundObject> userData=None)

'''      
    ...

class StateRenderableParameter:
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
isInstanceOf( (StateRenderableParameter)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECore::TypedObjectParameter<IECoreScene::StateRenderable> {lvalue},IECore::TypeId)

isInstanceOf( (StateRenderableParameter)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECore::TypedObjectParameter<IECoreScene::StateRenderable> {lvalue},char const*)'''
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
typeId( (StateRenderableParameter)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECore::TypedObjectParameter<IECoreScene::StateRenderable> {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (StateRenderableParameter)arg1) -> str :

    C++ signature :
        char const* typeName(IECore::TypedObjectParameter<IECoreScene::StateRenderable> {lvalue})'''
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
valueValid( (StateRenderableParameter)arg1, (object)arg2) -> tuple :
    Returns a tuple containing a bool specifying validity and a string giving a reason for invalidity.

    C++ signature :
        boost::python::tuple valueValid(IECore::TypedObjectParameter<IECoreScene::StateRenderable>,boost::intrusive_ptr<IECore::Object const>)

valueValid( (Parameter)arg1) -> tuple :
    Returns a tuple containing a bool specifying validity and a string giving a reason for invalidity.

    C++ signature :
        boost::python::tuple valueValid(IECore::Parameter)'''
    ...

def TransferSmoothSkinningWeightsOp (*args):
      '''
__init__(_object*)

'''      
    ...

class TransferSmoothSkinningWeightsOp:
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
isInstanceOf( (TransferSmoothSkinningWeightsOp)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::TransferSmoothSkinningWeightsOp {lvalue},IECore::TypeId)

isInstanceOf( (TransferSmoothSkinningWeightsOp)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::TransferSmoothSkinningWeightsOp {lvalue},char const*)'''
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
typeId( (TransferSmoothSkinningWeightsOp)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreScene::TransferSmoothSkinningWeightsOp {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (TransferSmoothSkinningWeightsOp)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreScene::TransferSmoothSkinningWeightsOp {lvalue})'''
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

def Transform (*args):
      '''

'''      
    ...

class Transform:
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
isInstanceOf( (Transform)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::Transform {lvalue},IECore::TypeId)

isInstanceOf( (Transform)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::Transform {lvalue},char const*)'''
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
    def transform (self, *args, **kwargs):
      '''
transform( (Transform)arg1 [, (float)arg2]) -> M44f :

    C++ signature :
        Imath_3_1::Matrix44<float> transform(IECoreScene::Transform {lvalue} [,float])'''
    ...
    def typeId (self, *args, **kwargs):
      '''
typeId( (Transform)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreScene::Transform {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (Transform)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreScene::Transform {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...

def TransformBlock (*args):
      '''

'''      
    ...

class TransformBlock:

def TransformOp (*args):
      '''
__init__(_object*)

'''      
    ...

class TransformOp:
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
isInstanceOf( (TransformOp)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::TransformOp {lvalue},IECore::TypeId)

isInstanceOf( (TransformOp)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::TransformOp {lvalue},char const*)'''
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
typeId( (TransformOp)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreScene::TransformOp {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (TransformOp)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreScene::TransformOp {lvalue})'''
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

def TransformParameter (*args):
      '''
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > name, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > description, boost::intrusive_ptr<IECoreScene::Transform> defaultValue)
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > name, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > description, boost::intrusive_ptr<IECoreScene::Transform> defaultValue, boost::python::api::object presets=())
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > name, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > description, boost::intrusive_ptr<IECoreScene::Transform> defaultValue, boost::python::api::object presets=(), bool presetsOnly=False)
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > name, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > description, boost::intrusive_ptr<IECoreScene::Transform> defaultValue, boost::python::api::object presets=(), bool presetsOnly=False, boost::intrusive_ptr<IECore::CompoundObject> userData=None)

'''      
    ...

class TransformParameter:
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
isInstanceOf( (TransformParameter)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECore::TypedObjectParameter<IECoreScene::Transform> {lvalue},IECore::TypeId)

isInstanceOf( (TransformParameter)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECore::TypedObjectParameter<IECoreScene::Transform> {lvalue},char const*)'''
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
typeId( (TransformParameter)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECore::TypedObjectParameter<IECoreScene::Transform> {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (TransformParameter)arg1) -> str :

    C++ signature :
        char const* typeName(IECore::TypedObjectParameter<IECoreScene::Transform> {lvalue})'''
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
valueValid( (TransformParameter)arg1, (object)arg2) -> tuple :
    Returns a tuple containing a bool specifying validity and a string giving a reason for invalidity.

    C++ signature :
        boost::python::tuple valueValid(IECore::TypedObjectParameter<IECoreScene::Transform>,boost::intrusive_ptr<IECore::Object const>)

valueValid( (Parameter)arg1) -> tuple :
    Returns a tuple containing a bool specifying validity and a string giving a reason for invalidity.

    C++ signature :
        boost::python::tuple valueValid(IECore::Parameter)'''
    ...

def TriangulateOp (*args):
      '''
__init__(_object*)

'''      
    ...

class TriangulateOp:
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
isInstanceOf( (TriangulateOp)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::TriangulateOp {lvalue},IECore::TypeId)

isInstanceOf( (TriangulateOp)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::TriangulateOp {lvalue},char const*)'''
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
typeId( (TriangulateOp)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreScene::TriangulateOp {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (TriangulateOp)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreScene::TriangulateOp {lvalue})'''
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

def TypeId (*args):
      '''

'''      
    ...

class TypeId:
    def AddSmoothSkinningInfluencesOp (self, *args, **kwargs):
      '''None'''
    ...
    def AttributeState (self, *args, **kwargs):
      '''None'''
    ...
    def AttributeStateParameter (self, *args, **kwargs):
      '''None'''
    ...
    def Camera (self, *args, **kwargs):
      '''None'''
    ...
    def ClippingPlane (self, *args, **kwargs):
      '''None'''
    ...
    def CompressSmoothSkinningDataOp (self, *args, **kwargs):
      '''None'''
    ...
    def ContrastSmoothSkinningWeightsOp (self, *args, **kwargs):
      '''None'''
    ...
    def CoordinateSystem (self, *args, **kwargs):
      '''None'''
    ...
    def CurveExtrudeOp (self, *args, **kwargs):
      '''None'''
    ...
    def CurveLineariser (self, *args, **kwargs):
      '''None'''
    ...
    def CurveTangentsOp (self, *args, **kwargs):
      '''None'''
    ...
    def CurvesMergeOp (self, *args, **kwargs):
      '''None'''
    ...
    def CurvesPrimitive (self, *args, **kwargs):
      '''None'''
    ...
    def CurvesPrimitiveEvaluator (self, *args, **kwargs):
      '''None'''
    ...
    def CurvesPrimitiveOp (self, *args, **kwargs):
      '''None'''
    ...
    def CurvesPrimitiveParameter (self, *args, **kwargs):
      '''None'''
    ...
    def DecompressSmoothSkinningDataOp (self, *args, **kwargs):
      '''None'''
    ...
    def DiskPrimitive (self, *args, **kwargs):
      '''None'''
    ...
    def ExternalProcedural (self, *args, **kwargs):
      '''None'''
    ...
    def FaceVaryingPromotionOp (self, *args, **kwargs):
      '''None'''
    ...
    def Font (self, *args, **kwargs):
      '''None'''
    ...
    def Group (self, *args, **kwargs):
      '''None'''
    ...
    def GroupParameter (self, *args, **kwargs):
      '''None'''
    ...
    def LastCoreScene (self, *args, **kwargs):
      '''None'''
    ...
    def Light (self, *args, **kwargs):
      '''None'''
    ...
    def LimitSmoothSkinningInfluencesOp (self, *args, **kwargs):
      '''None'''
    ...
    def LinkedScene (self, *args, **kwargs):
      '''None'''
    ...
    def MatrixMotionTransform (self, *args, **kwargs):
      '''None'''
    ...
    def MatrixMotionTransformParameter (self, *args, **kwargs):
      '''None'''
    ...
    def MatrixTransform (self, *args, **kwargs):
      '''None'''
    ...
    def MatrixTransformParameter (self, *args, **kwargs):
      '''None'''
    ...
    def MeshDistortionsOp (self, *args, **kwargs):
      '''None'''
    ...
    def MeshFaceFilterOp (self, *args, **kwargs):
      '''None'''
    ...
    def MeshMergeOp (self, *args, **kwargs):
      '''None'''
    ...
    def MeshNormalsOp (self, *args, **kwargs):
      '''None'''
    ...
    def MeshPrimitive (self, *args, **kwargs):
      '''None'''
    ...
    def MeshPrimitiveEvaluator (self, *args, **kwargs):
      '''None'''
    ...
    def MeshPrimitiveOp (self, *args, **kwargs):
      '''None'''
    ...
    def MeshPrimitiveParameter (self, *args, **kwargs):
      '''None'''
    ...
    def MeshPrimitiveShrinkWrapOp (self, *args, **kwargs):
      '''None'''
    ...
    def MeshTangentsOp (self, *args, **kwargs):
      '''None'''
    ...
    def MeshVertexReorderOp (self, *args, **kwargs):
      '''None'''
    ...
    def MixSmoothSkinningWeightsOp (self, *args, **kwargs):
      '''None'''
    ...
    def MotionPrimitive (self, *args, **kwargs):
      '''None'''
    ...
    def MotionPrimitiveParameter (self, *args, **kwargs):
      '''None'''
    ...
    def MotionTransform (self, *args, **kwargs):
      '''None'''
    ...
    def NParticleReader (self, *args, **kwargs):
      '''None'''
    ...
    def NURBSPrimitive (self, *args, **kwargs):
      '''None'''
    ...
    def NormalizeSmoothSkinningWeightsOp (self, *args, **kwargs):
      '''None'''
    ...
    def OBJReader (self, *args, **kwargs):
      '''None'''
    ...
    def Options (self, *args, **kwargs):
      '''None'''
    ...
    def Output (self, *args, **kwargs):
      '''None'''
    ...
    def PDCParticleReader (self, *args, **kwargs):
      '''None'''
    ...
    def PDCParticleWriter (self, *args, **kwargs):
      '''None'''
    ...
    def ParameterisedProcedural (self, *args, **kwargs):
      '''None'''
    ...
    def ParticleReader (self, *args, **kwargs):
      '''None'''
    ...
    def ParticleWriter (self, *args, **kwargs):
      '''None'''
    ...
    def PatchMeshPrimitive (self, *args, **kwargs):
      '''None'''
    ...
    def PointBoundsOp (self, *args, **kwargs):
      '''None'''
    ...
    def PointDensitiesOp (self, *args, **kwargs):
      '''None'''
    ...
    def PointDistributionOp (self, *args, **kwargs):
      '''None'''
    ...
    def PointNormalsOp (self, *args, **kwargs):
      '''None'''
    ...
    def PointSmoothSkinningOp (self, *args, **kwargs):
      '''None'''
    ...
    def PointVelocityDisplaceOp (self, *args, **kwargs):
      '''None'''
    ...
    def PointsMotionOp (self, *args, **kwargs):
      '''None'''
    ...
    def PointsPrimitive (self, *args, **kwargs):
      '''None'''
    ...
    def PointsPrimitiveEvaluator (self, *args, **kwargs):
      '''None'''
    ...
    def PointsPrimitiveParameter (self, *args, **kwargs):
      '''None'''
    ...
    def PreWorldRenderable (self, *args, **kwargs):
      '''None'''
    ...
    def Primitive (self, *args, **kwargs):
      '''None'''
    ...
    def PrimitiveEvaluator (self, *args, **kwargs):
      '''None'''
    ...
    def PrimitiveOp (self, *args, **kwargs):
      '''None'''
    ...
    def PrimitiveParameter (self, *args, **kwargs):
      '''None'''
    ...
    def RandomRotationOp (self, *args, **kwargs):
      '''None'''
    ...
    def RemoveSmoothSkinningInfluencesOp (self, *args, **kwargs):
      '''None'''
    ...
    def Renderable (self, *args, **kwargs):
      '''None'''
    ...
    def Renderer (self, *args, **kwargs):
      '''None'''
    ...
    def ReorderSmoothSkinningInfluencesOp (self, *args, **kwargs):
      '''None'''
    ...
    def SampledSceneInterface (self, *args, **kwargs):
      '''None'''
    ...
    def SceneCache (self, *args, **kwargs):
      '''None'''
    ...
    def SceneInterface (self, *args, **kwargs):
      '''None'''
    ...
    def Shader (self, *args, **kwargs):
      '''None'''
    ...
    def ShaderNetwork (self, *args, **kwargs):
      '''None'''
    ...
    def ShaderParameter (self, *args, **kwargs):
      '''None'''
    ...
    def SmoothSkinningData (self, *args, **kwargs):
      '''None'''
    ...
    def SmoothSkinningDataParameter (self, *args, **kwargs):
      '''None'''
    ...
    def SmoothSmoothSkinningWeightsOp (self, *args, **kwargs):
      '''None'''
    ...
    def SpherePrimitive (self, *args, **kwargs):
      '''None'''
    ...
    def SpherePrimitiveEvaluator (self, *args, **kwargs):
      '''None'''
    ...
    def StateRenderable (self, *args, **kwargs):
      '''None'''
    ...
    def StateRenderableParameter (self, *args, **kwargs):
      '''None'''
    ...
    def TransferSmoothSkinningWeightsOp (self, *args, **kwargs):
      '''None'''
    ...
    def Transform (self, *args, **kwargs):
      '''None'''
    ...
    def TransformOp (self, *args, **kwargs):
      '''None'''
    ...
    def TransformParameter (self, *args, **kwargs):
      '''None'''
    ...
    def TriangulateOp (self, *args, **kwargs):
      '''None'''
    ...
    def VisibleRenderable (self, *args, **kwargs):
      '''None'''
    ...
    def VisibleRenderableParameter (self, *args, **kwargs):
      '''None'''
    ...
    def as_integer_ratio (self, /):
      '''Return integer ratio.

Return a pair of integers, whose ratio is exactly equal to the original int
and with a positive denominator.

>>> (10).as_integer_ratio()
(10, 1)
>>> (-10).as_integer_ratio()
(-10, 1)
>>> (0).as_integer_ratio()
(0, 1)'''
    ...
    def bit_count (self, /):
      '''Number of ones in the binary representation of the absolute value of self.

Also known as the population count.

>>> bin(13)
'0b1101'
>>> (13).bit_count()
3'''
    ...
    def bit_length (self, /):
      '''Number of bits necessary to represent self in binary.

>>> bin(37)
'0b100101'
>>> (37).bit_length()
6'''
    ...
    def conjugate (self, *args, **kwargs):
      '''Returns self, the complex conjugate of any int.'''
    ...
    def denominator (self, *args, **kwargs):
      '''the denominator of a rational number in lowest terms'''
    ...
    def from_bytes (bytes, byteorder, *, signed=False):
      '''Return the integer represented by the given array of bytes.

  bytes
    Holds the array of bytes to convert.  The argument must either
    support the buffer protocol or be an iterable object producing bytes.
    Bytes and bytearray are examples of built-in objects that support the
    buffer protocol.
  byteorder
    The byte order used to represent the integer.  If byteorder is 'big',
    the most significant byte is at the beginning of the byte array.  If
    byteorder is 'little', the most significant byte is at the end of the
    byte array.  To request the native byte order of the host system, use
    `sys.byteorder' as the byte order value.
  signed
    Indicates whether two's complement is used to represent the integer.'''
    ...
    def imag (self, *args, **kwargs):
      '''the imaginary part of a complex number'''
    ...
    def name (self, *args, **kwargs):
      '''None'''
    ...
    def names (self, *args, **kwargs):
      '''dict() -> new empty dictionary
dict(mapping) -> new dictionary initialized from a mapping object's
    (key, value) pairs
dict(iterable) -> new dictionary initialized as if via:
    d = {}
    for k, v in iterable:
        d[k] = v
dict(**kwargs) -> new dictionary initialized with the name=value pairs
    in the keyword argument list.  For example:  dict(one=1, two=2)'''
    ...
    def numerator (self, *args, **kwargs):
      '''the numerator of a rational number in lowest terms'''
    ...
    def real (self, *args, **kwargs):
      '''the real part of a complex number'''
    ...
    def to_bytes (self, /, length, byteorder, *, signed=False):
      '''Return an array of bytes representing an integer.

  length
    Length of bytes object to use.  An OverflowError is raised if the
    integer is not representable with the given number of bytes.
  byteorder
    The byte order used to represent the integer.  If byteorder is 'big',
    the most significant byte is at the beginning of the byte array.  If
    byteorder is 'little', the most significant byte is at the end of the
    byte array.  To request the native byte order of the host system, use
    `sys.byteorder' as the byte order value.
  signed
    Determines whether two's complement is used to represent the integer.
    If signed is False and a negative integer is given, an OverflowError
    is raised.'''
    ...
    def values (self, *args, **kwargs):
      '''dict() -> new empty dictionary
dict(mapping) -> new dictionary initialized from a mapping object's
    (key, value) pairs
dict(iterable) -> new dictionary initialized as if via:
    d = {}
    for k, v in iterable:
        d[k] = v
dict(**kwargs) -> new dictionary initialized with the name=value pairs
    in the keyword argument list.  For example:  dict(one=1, two=2)'''
    ...

def V3fTriangulator (*args):
      '''
__init__(_object*, boost::intrusive_ptr<IECoreScene::MeshPrimitiveBuilder>)

'''      
    ...

class V3fTriangulator:
    def collectGarbage (self, *args, **kwargs):
      '''
collectGarbage() -> None :

    C++ signature :
        void collectGarbage()'''
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
    def triangulate (self, *args, **kwargs):
      '''
triangulate( (V3fTriangulator)arg1, (object)arg2) -> None :

    C++ signature :
        void triangulate(IECoreScene::Triangulator<__gnu_cxx::__normal_iterator<Imath_3_1::Vec3<float> const*, std::vector<Imath_3_1::Vec3<float>, std::allocator<Imath_3_1::Vec3<float> > > >, IECoreScene::MeshPrimitiveBuilder> {lvalue},boost::intrusive_ptr<IECore::TypedData<std::vector<Imath_3_1::Vec3<float>, std::allocator<Imath_3_1::Vec3<float> > > > const>)

triangulate( (V3fTriangulator)arg1, (list)arg2) -> None :

    C++ signature :
        void triangulate(IECoreScene::Triangulator<__gnu_cxx::__normal_iterator<Imath_3_1::Vec3<float> const*, std::vector<Imath_3_1::Vec3<float>, std::allocator<Imath_3_1::Vec3<float> > > >, IECoreScene::MeshPrimitiveBuilder> {lvalue},boost::python::list)'''
    ...

def VisibleRenderable (*args):
      '''

'''      
    ...

class VisibleRenderable:
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
isInstanceOf( (VisibleRenderable)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::VisibleRenderable {lvalue},IECore::TypeId)

isInstanceOf( (VisibleRenderable)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreScene::VisibleRenderable {lvalue},char const*)'''
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
typeId( (VisibleRenderable)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreScene::VisibleRenderable {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (VisibleRenderable)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreScene::VisibleRenderable {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...

def VisibleRenderableParameter (*args):
      '''
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > name, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > description, boost::intrusive_ptr<IECoreScene::VisibleRenderable> defaultValue)
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > name, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > description, boost::intrusive_ptr<IECoreScene::VisibleRenderable> defaultValue, boost::python::api::object presets=())
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > name, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > description, boost::intrusive_ptr<IECoreScene::VisibleRenderable> defaultValue, boost::python::api::object presets=(), bool presetsOnly=False)
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > name, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > description, boost::intrusive_ptr<IECoreScene::VisibleRenderable> defaultValue, boost::python::api::object presets=(), bool presetsOnly=False, boost::intrusive_ptr<IECore::CompoundObject> userData=None)

'''      
    ...

class VisibleRenderableParameter:
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
isInstanceOf( (VisibleRenderableParameter)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECore::TypedObjectParameter<IECoreScene::VisibleRenderable> {lvalue},IECore::TypeId)

isInstanceOf( (VisibleRenderableParameter)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECore::TypedObjectParameter<IECoreScene::VisibleRenderable> {lvalue},char const*)'''
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
typeId( (VisibleRenderableParameter)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECore::TypedObjectParameter<IECoreScene::VisibleRenderable> {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (VisibleRenderableParameter)arg1) -> str :

    C++ signature :
        char const* typeName(IECore::TypedObjectParameter<IECoreScene::VisibleRenderable> {lvalue})'''
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
valueValid( (VisibleRenderableParameter)arg1, (object)arg2) -> tuple :
    Returns a tuple containing a bool specifying validity and a string giving a reason for invalidity.

    C++ signature :
        boost::python::tuple valueValid(IECore::TypedObjectParameter<IECoreScene::VisibleRenderable>,boost::intrusive_ptr<IECore::Object const>)

valueValid( (Parameter)arg1) -> tuple :
    Returns a tuple containing a bool specifying validity and a string giving a reason for invalidity.

    C++ signature :
        boost::python::tuple valueValid(IECore::Parameter)'''
    ...

def WorldBlock (*args):
      '''

'''      
    ...

class WorldBlock:

def _IECoreScene (*args):
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

def testCurvesPrimitiveEvaluatorParallelClosestPoint (*args):
      '''

'''      
    ...

def testCurvesPrimitiveEvaluatorParallelResultCreation (*args):
      '''

'''      
    ...

def testPrimitiveVariableBoolIndexedView (*args):
      '''

'''      
    ...

def testPrimitiveVariableIndexedView (*args):
      '''

'''      
    ...

def testSceneCacheParallelAttributeRead (*args):
      '''

'''      
    ...

def testSceneCacheParallelFakeAttributeRead (*args):
      '''

'''      
    ...

def testShaderNetworkMove (*args):
      '''

'''      
    ...

def testVariableIndexedView (*args):
      '''

'''      
    ...
