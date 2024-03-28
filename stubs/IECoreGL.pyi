
def AlphaTexture (*args):
      '''
__init__(_object*, IECoreImage::ImagePrimitive const*, bool)
__init__(_object*, unsigned int, unsigned int, IECore::Data const*, bool)

'''      
    ...

class AlphaTexture:
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
    def bind (self, *args, **kwargs):
      '''
bind( (Bindable)arg1) -> None :

    C++ signature :
        void bind(IECoreGL::Bindable {lvalue})'''
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
    def imagePrimitive (self, *args, **kwargs):
      '''
imagePrimitive( (Texture)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECoreImage::ImagePrimitive> imagePrimitive(IECoreGL::Texture {lvalue})'''
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
isInstanceOf( (AlphaTexture)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::AlphaTexture {lvalue},IECore::TypeId)

isInstanceOf( (AlphaTexture)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::AlphaTexture {lvalue},char const*)'''
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
typeId( (AlphaTexture)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreGL::AlphaTexture {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (AlphaTexture)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreGL::AlphaTexture {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...

def AutomaticInstancingStateComponent (*args):
      '''
__init__(_object*, bool)

'''      
    ...

class AutomaticInstancingStateComponent:
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
    def bind (self, *args, **kwargs):
      '''
bind( (Bindable)arg1) -> None :

    C++ signature :
        void bind(IECoreGL::Bindable {lvalue})'''
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
isInstanceOf( (AutomaticInstancingStateComponent)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::TypedStateComponent<bool, 105076u> {lvalue},IECore::TypeId)

isInstanceOf( (AutomaticInstancingStateComponent)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::TypedStateComponent<bool, 105076u> {lvalue},char const*)'''
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
typeId( (AutomaticInstancingStateComponent)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreGL::TypedStateComponent<bool, 105076u> {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (AutomaticInstancingStateComponent)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreGL::TypedStateComponent<bool, 105076u> {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...
    def value (self, *args, **kwargs):
      '''None'''
    ...

def Bindable (*args):
      '''

'''      
    ...

class Bindable:
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
    def bind (self, *args, **kwargs):
      '''
bind( (Bindable)arg1) -> None :

    C++ signature :
        void bind(IECoreGL::Bindable {lvalue})'''
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
isInstanceOf( (Bindable)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::Bindable {lvalue},IECore::TypeId)

isInstanceOf( (Bindable)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::Bindable {lvalue},char const*)'''
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
typeId( (Bindable)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreGL::Bindable {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (Bindable)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreGL::Bindable {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...

def BlendColorStateComponent (*args):
      '''
__init__(_object*, Imath_3_1::Color4<float>)

'''      
    ...

class BlendColorStateComponent:
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
    def bind (self, *args, **kwargs):
      '''
bind( (Bindable)arg1) -> None :

    C++ signature :
        void bind(IECoreGL::Bindable {lvalue})'''
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
isInstanceOf( (BlendColorStateComponent)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::TypedStateComponent<Imath_3_1::Color4<float>, 105031u> {lvalue},IECore::TypeId)

isInstanceOf( (BlendColorStateComponent)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::TypedStateComponent<Imath_3_1::Color4<float>, 105031u> {lvalue},char const*)'''
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
typeId( (BlendColorStateComponent)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreGL::TypedStateComponent<Imath_3_1::Color4<float>, 105031u> {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (BlendColorStateComponent)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreGL::TypedStateComponent<Imath_3_1::Color4<float>, 105031u> {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...
    def value (self, *args, **kwargs):
      '''None'''
    ...

def BlendEquationStateComponent (*args):
      '''
__init__(_object*, unsigned int)

'''      
    ...

class BlendEquationStateComponent:
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
    def bind (self, *args, **kwargs):
      '''
bind( (Bindable)arg1) -> None :

    C++ signature :
        void bind(IECoreGL::Bindable {lvalue})'''
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
isInstanceOf( (BlendEquationStateComponent)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::TypedStateComponent<unsigned int, 105032u> {lvalue},IECore::TypeId)

isInstanceOf( (BlendEquationStateComponent)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::TypedStateComponent<unsigned int, 105032u> {lvalue},char const*)'''
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
typeId( (BlendEquationStateComponent)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreGL::TypedStateComponent<unsigned int, 105032u> {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (BlendEquationStateComponent)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreGL::TypedStateComponent<unsigned int, 105032u> {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...
    def value (self, *args, **kwargs):
      '''None'''
    ...

def BlendFuncStateComponent (*args):
      '''
__init__(_object*, IECoreGL::BlendFactors)

'''      
    ...

class BlendFuncStateComponent:
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
    def bind (self, *args, **kwargs):
      '''
bind( (Bindable)arg1) -> None :

    C++ signature :
        void bind(IECoreGL::Bindable {lvalue})'''
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
isInstanceOf( (BlendFuncStateComponent)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::TypedStateComponent<IECoreGL::BlendFactors, 105030u> {lvalue},IECore::TypeId)

isInstanceOf( (BlendFuncStateComponent)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::TypedStateComponent<IECoreGL::BlendFactors, 105030u> {lvalue},char const*)'''
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
typeId( (BlendFuncStateComponent)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreGL::TypedStateComponent<IECoreGL::BlendFactors, 105030u> {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (BlendFuncStateComponent)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreGL::TypedStateComponent<IECoreGL::BlendFactors, 105030u> {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...
    def value (self, *args, **kwargs):
      '''None'''
    ...

def BoundColorStateComponent (*args):
      '''
__init__(_object*, Imath_3_1::Color4<float>)

'''      
    ...

class BoundColorStateComponent:
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
    def bind (self, *args, **kwargs):
      '''
bind( (Bindable)arg1) -> None :

    C++ signature :
        void bind(IECoreGL::Bindable {lvalue})'''
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
isInstanceOf( (BoundColorStateComponent)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::TypedStateComponent<Imath_3_1::Color4<float>, 105035u> {lvalue},IECore::TypeId)

isInstanceOf( (BoundColorStateComponent)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::TypedStateComponent<Imath_3_1::Color4<float>, 105035u> {lvalue},char const*)'''
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
typeId( (BoundColorStateComponent)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreGL::TypedStateComponent<Imath_3_1::Color4<float>, 105035u> {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (BoundColorStateComponent)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreGL::TypedStateComponent<Imath_3_1::Color4<float>, 105035u> {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...
    def value (self, *args, **kwargs):
      '''None'''
    ...

def Buffer (*args):
      '''
__init__(_object*, unsigned int)

'''      
    ...

class Buffer:
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
isInstanceOf( (Buffer)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::Buffer {lvalue},IECore::TypeId)

isInstanceOf( (Buffer)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::Buffer {lvalue},char const*)'''
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
    def size (self, *args, **kwargs):
      '''
size( (Buffer)arg1) -> int :

    C++ signature :
        unsigned long size(IECoreGL::Buffer {lvalue})'''
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
typeId( (Buffer)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreGL::Buffer {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (Buffer)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreGL::Buffer {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...

def CachedConverter (*args):
      '''
__init__(_object*, unsigned long)

'''      
    ...

class CachedConverter:
    def clearUnused (self, *args, **kwargs):
      '''
clearUnused( (CachedConverter)arg1) -> None :

    C++ signature :
        void clearUnused(IECoreGL::CachedConverter {lvalue})'''
    ...
    def collectGarbage (self, *args, **kwargs):
      '''
collectGarbage() -> None :

    C++ signature :
        void collectGarbage()'''
    ...
    def convert (self, *args, **kwargs):
      '''
convert( (CachedConverter)arg1, (object)arg2) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::RunTimeTyped> convert(IECoreGL::CachedConverter {lvalue},boost::intrusive_ptr<IECore::Object>)'''
    ...
    def defaultCachedConverter (self, *args, **kwargs):
      '''
defaultCachedConverter() -> object :

    C++ signature :
        IECoreGL::CachedConverter* defaultCachedConverter()'''
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
    def getMaxMemory (self, *args, **kwargs):
      '''
getMaxMemory( (CachedConverter)arg1) -> int :

    C++ signature :
        unsigned long getMaxMemory(IECoreGL::CachedConverter {lvalue})'''
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
    def setMaxMemory (self, *args, **kwargs):
      '''
setMaxMemory( (CachedConverter)arg1, (int)arg2) -> None :

    C++ signature :
        void setMaxMemory(IECoreGL::CachedConverter {lvalue},unsigned long)'''
    ...

def Camera (*args):
      '''
__init__(_object*, Imath_3_1::Matrix44<float> transform=M44f((1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)), bool orthographic=True, Imath_3_1::Vec2<int> resolution=V2i(640, 480), Imath_3_1::Box<Imath_3_1::Vec2<float> > frustum=Box2f(V2f(-1, -1), V2f(1, 1)), Imath_3_1::Vec2<float> clippingPlanes=V2f(0.100000001, 1000))

'''      
    ...

class Camera:
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
bound( (Renderable)arg1) -> Box3f :

    C++ signature :
        Imath_3_1::Box<Imath_3_1::Vec3<float> > bound(IECoreGL::Renderable {lvalue})'''
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
    def getClippingPlanes (self, *args, **kwargs):
      '''
getClippingPlanes( (Camera)arg1) -> V2f :

    C++ signature :
        Imath_3_1::Vec2<float> getClippingPlanes(IECoreGL::Camera {lvalue})'''
    ...
    def getNormalizedScreenWindow (self, *args, **kwargs):
      '''
getNormalizedScreenWindow( (Camera)arg1) -> Box2f :

    C++ signature :
        Imath_3_1::Box<Imath_3_1::Vec2<float> > getNormalizedScreenWindow(IECoreGL::Camera {lvalue})'''
    ...
    def getResolution (self, *args, **kwargs):
      '''
getResolution( (Camera)arg1) -> V2i :

    C++ signature :
        Imath_3_1::Vec2<int> getResolution(IECoreGL::Camera {lvalue})'''
    ...
    def getTransform (self, *args, **kwargs):
      '''
getTransform( (Camera)arg1) -> M44f :

    C++ signature :
        Imath_3_1::Matrix44<float> getTransform(IECoreGL::Camera {lvalue})'''
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
isInstanceOf( (Camera)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::Camera {lvalue},IECore::TypeId)

isInstanceOf( (Camera)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::Camera {lvalue},char const*)'''
    ...
    def isSame (self, *args, **kwargs):
      '''
isSame( (RefCounted)arg1, (RefCounted)arg2) -> bool :

    C++ signature :
        bool isSame(IECore::RefCounted const*,IECore::RefCounted const*)'''
    ...
    def matrix (self, *args, **kwargs):
      '''
matrix() -> M44f :

    C++ signature :
        Imath_3_1::Matrix44<float> matrix()'''
    ...
    def numWrappedInstances (self, *args, **kwargs):
      '''
numWrappedInstances() -> int :

    C++ signature :
        unsigned long numWrappedInstances()'''
    ...
    def perspectiveProjection (self, *args, **kwargs):
      '''
perspectiveProjection() -> bool :

    C++ signature :
        bool perspectiveProjection()'''
    ...
    def positionInObjectSpace (self, *args, **kwargs):
      '''
positionInObjectSpace() -> V3f :

    C++ signature :
        Imath_3_1::Vec3<float> positionInObjectSpace()'''
    ...
    def projectionMatrix (self, *args, **kwargs):
      '''
projectionMatrix() -> M44f :

    C++ signature :
        Imath_3_1::Matrix44<float> projectionMatrix()'''
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
    def render (self, *args, **kwargs):
      '''
render( (Renderable)arg1, (State)arg2) -> None :

    C++ signature :
        void render(IECoreGL::Renderable {lvalue},IECoreGL::State*)'''
    ...
    def setClippingPlanes (self, *args, **kwargs):
      '''
setClippingPlanes( (Camera)arg1, (V2f)arg2) -> None :

    C++ signature :
        void setClippingPlanes(IECoreGL::Camera {lvalue},Imath_3_1::Vec2<float>)'''
    ...
    def setNormalizedScreenWindow (self, *args, **kwargs):
      '''
setNormalizedScreenWindow( (Camera)arg1, (Box2f)arg2) -> None :

    C++ signature :
        void setNormalizedScreenWindow(IECoreGL::Camera {lvalue},Imath_3_1::Box<Imath_3_1::Vec2<float> >)'''
    ...
    def setResolution (self, *args, **kwargs):
      '''
setResolution( (Camera)arg1, (V2i)arg2) -> None :

    C++ signature :
        void setResolution(IECoreGL::Camera {lvalue},Imath_3_1::Vec2<int>)'''
    ...
    def setTransform (self, *args, **kwargs):
      '''
setTransform( (Camera)arg1, (M44f)arg2) -> None :

    C++ signature :
        void setTransform(IECoreGL::Camera {lvalue},Imath_3_1::Matrix44<float>)'''
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
        IECore::TypeId typeId(IECoreGL::Camera {lvalue})'''
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
        char const* typeName(IECoreGL::Camera {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...
    def upInObjectSpace (self, *args, **kwargs):
      '''
upInObjectSpace() -> V3f :

    C++ signature :
        Imath_3_1::Vec3<float> upInObjectSpace()'''
    ...
    def viewDirectionInObjectSpace (self, *args, **kwargs):
      '''
viewDirectionInObjectSpace() -> V3f :

    C++ signature :
        Imath_3_1::Vec3<float> viewDirectionInObjectSpace()'''
    ...

def CameraVisibilityStateComponent (*args):
      '''
__init__(_object*, bool)

'''      
    ...

class CameraVisibilityStateComponent:
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
    def bind (self, *args, **kwargs):
      '''
bind( (Bindable)arg1) -> None :

    C++ signature :
        void bind(IECoreGL::Bindable {lvalue})'''
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
isInstanceOf( (CameraVisibilityStateComponent)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::TypedStateComponent<bool, 105072u> {lvalue},IECore::TypeId)

isInstanceOf( (CameraVisibilityStateComponent)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::TypedStateComponent<bool, 105072u> {lvalue},char const*)'''
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
typeId( (CameraVisibilityStateComponent)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreGL::TypedStateComponent<bool, 105072u> {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (CameraVisibilityStateComponent)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreGL::TypedStateComponent<bool, 105072u> {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...
    def value (self, *args, **kwargs):
      '''None'''
    ...

def Color (*args):
      '''
__init__(_object*, Imath_3_1::Color4<float>)

'''      
    ...

class Color:
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
    def bind (self, *args, **kwargs):
      '''
bind( (Bindable)arg1) -> None :

    C++ signature :
        void bind(IECoreGL::Bindable {lvalue})'''
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
isInstanceOf( (Color)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::TypedStateComponent<Imath_3_1::Color4<float>, 105024u> {lvalue},IECore::TypeId)

isInstanceOf( (Color)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::TypedStateComponent<Imath_3_1::Color4<float>, 105024u> {lvalue},char const*)'''
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
typeId( (Color)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreGL::TypedStateComponent<Imath_3_1::Color4<float>, 105024u> {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (Color)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreGL::TypedStateComponent<Imath_3_1::Color4<float>, 105024u> {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...
    def value (self, *args, **kwargs):
      '''None'''
    ...

def ColorTexture (*args):
      '''
__init__(_object*, IECoreImage::ImagePrimitive const*)
__init__(_object*, unsigned int, unsigned int, IECore::Data const*, IECore::Data const*, IECore::Data const*, IECore::Data const*)
__init__(_object*, unsigned int, unsigned int, int)
__init__(_object*, unsigned int, unsigned int)

'''      
    ...

class ColorTexture:
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
    def bind (self, *args, **kwargs):
      '''
bind( (Bindable)arg1) -> None :

    C++ signature :
        void bind(IECoreGL::Bindable {lvalue})'''
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
    def imagePrimitive (self, *args, **kwargs):
      '''
imagePrimitive( (Texture)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECoreImage::ImagePrimitive> imagePrimitive(IECoreGL::Texture {lvalue})'''
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
isInstanceOf( (ColorTexture)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::ColorTexture {lvalue},IECore::TypeId)

isInstanceOf( (ColorTexture)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::ColorTexture {lvalue},char const*)'''
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
typeId( (ColorTexture)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreGL::ColorTexture {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (ColorTexture)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreGL::ColorTexture {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...

def CullingBoxStateComponent (*args):
      '''
__init__(_object*, Imath_3_1::Box<Imath_3_1::Vec3<float> >)

'''      
    ...

class CullingBoxStateComponent:
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
    def bind (self, *args, **kwargs):
      '''
bind( (Bindable)arg1) -> None :

    C++ signature :
        void bind(IECoreGL::Bindable {lvalue})'''
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
isInstanceOf( (CullingBoxStateComponent)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::TypedStateComponent<Imath_3_1::Box<Imath_3_1::Vec3<float> >, 105068u> {lvalue},IECore::TypeId)

isInstanceOf( (CullingBoxStateComponent)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::TypedStateComponent<Imath_3_1::Box<Imath_3_1::Vec3<float> >, 105068u> {lvalue},char const*)'''
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
typeId( (CullingBoxStateComponent)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreGL::TypedStateComponent<Imath_3_1::Box<Imath_3_1::Vec3<float> >, 105068u> {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (CullingBoxStateComponent)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreGL::TypedStateComponent<Imath_3_1::Box<Imath_3_1::Vec3<float> >, 105068u> {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...
    def value (self, *args, **kwargs):
      '''None'''
    ...

def CullingSpaceStateComponent (*args):
      '''
__init__(_object*, IECoreGL::RendererSpace)

'''      
    ...

class CullingSpaceStateComponent:
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
    def bind (self, *args, **kwargs):
      '''
bind( (Bindable)arg1) -> None :

    C++ signature :
        void bind(IECoreGL::Bindable {lvalue})'''
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
isInstanceOf( (CullingSpaceStateComponent)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::TypedStateComponent<IECoreGL::RendererSpace, 105067u> {lvalue},IECore::TypeId)

isInstanceOf( (CullingSpaceStateComponent)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::TypedStateComponent<IECoreGL::RendererSpace, 105067u> {lvalue},char const*)'''
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
typeId( (CullingSpaceStateComponent)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreGL::TypedStateComponent<IECoreGL::RendererSpace, 105067u> {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (CullingSpaceStateComponent)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreGL::TypedStateComponent<IECoreGL::RendererSpace, 105067u> {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...
    def value (self, *args, **kwargs):
      '''None'''
    ...

def CurvesPrimitive (*args):
      '''
__init__(_object*, IECore::CubicBasis<float> basis, bool periodic, boost::intrusive_ptr<IECore::TypedData<std::vector<int, std::allocator<int> > > const> vertsPerCurve, float width=1.0)

'''      
    ...

class CurvesPrimitive:
    def DrawBound (self, *args, **kwargs):
      '''None'''
    ...
    def DrawOutline (self, *args, **kwargs):
      '''None'''
    ...
    def DrawPoints (self, *args, **kwargs):
      '''None'''
    ...
    def DrawSolid (self, *args, **kwargs):
      '''None'''
    ...
    def DrawWireframe (self, *args, **kwargs):
      '''None'''
    ...
    def GLLineWidth (self, *args, **kwargs):
      '''None'''
    ...
    def IgnoreBasis (self, *args, **kwargs):
      '''None'''
    ...
    def OutlineWidth (self, *args, **kwargs):
      '''None'''
    ...
    def PointWidth (self, *args, **kwargs):
      '''None'''
    ...
    def Selectable (self, *args, **kwargs):
      '''None'''
    ...
    def TransparencySort (self, *args, **kwargs):
      '''None'''
    ...
    def UseGLLines (self, *args, **kwargs):
      '''None'''
    ...
    def WireframeWidth (self, *args, **kwargs):
      '''None'''
    ...
    def addPrimitiveVariable (self, *args, **kwargs):
      '''
addPrimitiveVariable( (Primitive)arg1, (object)arg2, (PrimitiveVariable)arg3) -> None :

    C++ signature :
        void addPrimitiveVariable(IECoreGL::Primitive {lvalue},std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >,IECoreScene::PrimitiveVariable)'''
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
bound( (Renderable)arg1) -> Box3f :

    C++ signature :
        Imath_3_1::Box<Imath_3_1::Vec3<float> > bound(IECoreGL::Renderable {lvalue})'''
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
isInstanceOf( (CurvesPrimitive)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::CurvesPrimitive {lvalue},IECore::TypeId)

isInstanceOf( (CurvesPrimitive)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::CurvesPrimitive {lvalue},char const*)'''
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
    def render (self, *args, **kwargs):
      '''
render( (Renderable)arg1, (State)arg2) -> None :

    C++ signature :
        void render(IECoreGL::Renderable {lvalue},IECoreGL::State*)'''
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
typeId( (CurvesPrimitive)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreGL::CurvesPrimitive {lvalue})'''
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
        char const* typeName(IECoreGL::CurvesPrimitive {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...

def DepthTexture (*args):
      '''
__init__(_object*, unsigned int, unsigned int, IECore::Data const*)
__init__(_object*, unsigned int, unsigned int)

'''      
    ...

class DepthTexture:
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
    def bind (self, *args, **kwargs):
      '''
bind( (Bindable)arg1) -> None :

    C++ signature :
        void bind(IECoreGL::Bindable {lvalue})'''
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
    def imagePrimitive (self, *args, **kwargs):
      '''
imagePrimitive( (Texture)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECoreImage::ImagePrimitive> imagePrimitive(IECoreGL::Texture {lvalue})'''
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
isInstanceOf( (DepthTexture)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::DepthTexture {lvalue},IECore::TypeId)

isInstanceOf( (DepthTexture)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::DepthTexture {lvalue},char const*)'''
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
typeId( (DepthTexture)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreGL::DepthTexture {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (DepthTexture)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreGL::DepthTexture {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...

def DoubleSidedStateComponent (*args):
      '''
__init__(_object*, bool)

'''      
    ...

class DoubleSidedStateComponent:
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
    def bind (self, *args, **kwargs):
      '''
bind( (Bindable)arg1) -> None :

    C++ signature :
        void bind(IECoreGL::Bindable {lvalue})'''
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
isInstanceOf( (DoubleSidedStateComponent)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::TypedStateComponent<bool, 105047u> {lvalue},IECore::TypeId)

isInstanceOf( (DoubleSidedStateComponent)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::TypedStateComponent<bool, 105047u> {lvalue},char const*)'''
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
typeId( (DoubleSidedStateComponent)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreGL::TypedStateComponent<bool, 105047u> {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (DoubleSidedStateComponent)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreGL::TypedStateComponent<bool, 105047u> {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...
    def value (self, *args, **kwargs):
      '''None'''
    ...

def Font (*args):
      '''
__init__(_object*, boost::intrusive_ptr<IECoreScene::Font>)

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
    def coreFont (self, *args, **kwargs):
      '''
coreFont( (Font)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECoreScene::Font> coreFont(IECoreGL::Font {lvalue})'''
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
    def isInstanceOf (self, *args, **kwargs):
      '''
isInstanceOf( (Font)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::Font {lvalue},IECore::TypeId)

isInstanceOf( (Font)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::Font {lvalue},char const*)'''
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
        boost::intrusive_ptr<IECoreGL::MeshPrimitive> mesh(IECoreGL::Font {lvalue},char)'''
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
    def renderSprites (self, *args, **kwargs):
      '''
renderSprites( (Font)arg1, (object)arg2) -> None :

    C++ signature :
        void renderSprites(IECoreGL::Font {lvalue},std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)'''
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
    def texture (self, *args, **kwargs):
      '''
texture( (Font)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECoreGL::AlphaTexture> texture(IECoreGL::Font {lvalue})'''
    ...
    def typeId (self, *args, **kwargs):
      '''
typeId( (Font)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreGL::Font {lvalue})'''
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
        char const* typeName(IECoreGL::Font {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...

def FontLoader (*args):
      '''
__init__(_object*, IECore::SearchPath)

'''      
    ...

class FontLoader:
    def clear (self, *args, **kwargs):
      '''
clear( (FontLoader)arg1) -> None :

    C++ signature :
        void clear(IECoreGL::FontLoader {lvalue})'''
    ...
    def collectGarbage (self, *args, **kwargs):
      '''
collectGarbage() -> None :

    C++ signature :
        void collectGarbage()'''
    ...
    def defaultFontLoader (self, *args, **kwargs):
      '''
defaultFontLoader() -> object :

    C++ signature :
        IECoreGL::FontLoader* defaultFontLoader()'''
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
    def load (self, *args, **kwargs):
      '''
load( (FontLoader)arg1, (object)arg2) -> object :

    C++ signature :
        boost::intrusive_ptr<IECoreGL::Font> load(IECoreGL::FontLoader {lvalue},std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)'''
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

def FrameBuffer (*args):
      '''
__init__(_object*)

'''      
    ...

class FrameBuffer:
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
    def getColor (self, *args, **kwargs):
      '''
getColor( (FrameBuffer)arg1, (int)arg2) -> object :

    C++ signature :
        boost::intrusive_ptr<IECoreGL::Texture> getColor(IECoreGL::FrameBuffer {lvalue},unsigned int)'''
    ...
    def getDepth (self, *args, **kwargs):
      '''
getDepth( (FrameBuffer)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECoreGL::DepthTexture> getDepth(IECoreGL::FrameBuffer {lvalue})'''
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
isInstanceOf( (FrameBuffer)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::FrameBuffer {lvalue},IECore::TypeId)

isInstanceOf( (FrameBuffer)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::FrameBuffer {lvalue},char const*)'''
    ...
    def isSame (self, *args, **kwargs):
      '''
isSame( (RefCounted)arg1, (RefCounted)arg2) -> bool :

    C++ signature :
        bool isSame(IECore::RefCounted const*,IECore::RefCounted const*)'''
    ...
    def maxColors (self, *args, **kwargs):
      '''
maxColors() -> int :

    C++ signature :
        unsigned int maxColors()'''
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
    def setColor (self, *args, **kwargs):
      '''
setColor( (FrameBuffer)arg1, (object)arg2, (int)arg3) -> None :

    C++ signature :
        void setColor(IECoreGL::FrameBuffer {lvalue},boost::intrusive_ptr<IECoreGL::Texture>,unsigned int)'''
    ...
    def setDepth (self, *args, **kwargs):
      '''
setDepth( (FrameBuffer)arg1, (object)arg2) -> None :

    C++ signature :
        void setDepth(IECoreGL::FrameBuffer {lvalue},boost::intrusive_ptr<IECoreGL::DepthTexture>)'''
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
typeId( (FrameBuffer)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreGL::FrameBuffer {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (FrameBuffer)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreGL::FrameBuffer {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...
    def validate (self, *args, **kwargs):
      '''
validate( (FrameBuffer)arg1) -> None :

    C++ signature :
        void validate(IECoreGL::FrameBuffer {lvalue})'''
    ...

def GLPointsUsage (*args):
      '''

'''      
    ...

class GLPointsUsage:
    def ForAll (self, *args, **kwargs):
      '''None'''
    ...
    def ForPointsAndDisks (self, *args, **kwargs):
      '''None'''
    ...
    def ForPointsOnly (self, *args, **kwargs):
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
        void addChild(IECoreGL::Group {lvalue},boost::intrusive_ptr<IECoreGL::Renderable>)'''
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
bound( (Group)arg1) -> Box3f :

    C++ signature :
        Imath_3_1::Box<Imath_3_1::Vec3<float> > bound(IECoreGL::Group {lvalue})'''
    ...
    def children (self, *args, **kwargs):
      '''
children( (Group)arg1) -> list :
    Returns a list referencing the children of the group - modifying the list has no effect on the Group.

    C++ signature :
        boost::python::list children(IECoreGL::Group)'''
    ...
    def clearChildren (self, *args, **kwargs):
      '''
clearChildren( (Group)arg1) -> None :

    C++ signature :
        void clearChildren(IECoreGL::Group {lvalue})'''
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
    def getState (self, *args, **kwargs):
      '''
getState( (Group)arg1) -> object :

    C++ signature :
        IECoreGL::State* getState(IECoreGL::Group {lvalue})'''
    ...
    def getTransform (self, *args, **kwargs):
      '''
getTransform( (Group)arg1) -> M44f :

    C++ signature :
        Imath_3_1::Matrix44<float> getTransform(IECoreGL::Group {lvalue})'''
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
isInstanceOf( (Group)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::Group {lvalue},IECore::TypeId)

isInstanceOf( (Group)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::Group {lvalue},char const*)'''
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
    def removeChild (self, *args, **kwargs):
      '''
removeChild( (Group)arg1, (Renderable)arg2) -> None :

    C++ signature :
        void removeChild(IECoreGL::Group {lvalue},IECoreGL::Renderable*)'''
    ...
    def render (self, *args, **kwargs):
      '''
render( (Renderable)arg1, (State)arg2) -> None :

    C++ signature :
        void render(IECoreGL::Renderable {lvalue},IECoreGL::State*)'''
    ...
    def setState (self, *args, **kwargs):
      '''
setState( (Group)arg1, (object)arg2) -> None :

    C++ signature :
        void setState(IECoreGL::Group {lvalue},boost::intrusive_ptr<IECoreGL::State>)'''
    ...
    def setTransform (self, *args, **kwargs):
      '''
setTransform( (Group)arg1, (M44f)arg2) -> None :

    C++ signature :
        void setTransform(IECoreGL::Group {lvalue},Imath_3_1::Matrix44<float>)'''
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
typeId( (Group)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreGL::Group {lvalue})'''
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
        char const* typeName(IECoreGL::Group {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...

def HitRecord (*args):
      '''
__init__(_object*, float, float, unsigned int)
__init__(_object*, unsigned int const*)

'''      
    ...

class HitRecord:
    def depthMax (self, *args, **kwargs):
      '''None'''
    ...
    def depthMin (self, *args, **kwargs):
      '''None'''
    ...
    def name (self, *args, **kwargs):
      '''None'''
    ...
    def offsetToNext (self, *args, **kwargs):
      '''
offsetToNext( (HitRecord)arg1) -> int :

    C++ signature :
        unsigned long offsetToNext(IECoreGL::HitRecord {lvalue})'''
    ...

def LineSmoothingStateComponent (*args):
      '''
__init__(_object*, bool)

'''      
    ...

class LineSmoothingStateComponent:
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
    def bind (self, *args, **kwargs):
      '''
bind( (Bindable)arg1) -> None :

    C++ signature :
        void bind(IECoreGL::Bindable {lvalue})'''
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
isInstanceOf( (LineSmoothingStateComponent)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::TypedStateComponent<bool, 105057u> {lvalue},IECore::TypeId)

isInstanceOf( (LineSmoothingStateComponent)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::TypedStateComponent<bool, 105057u> {lvalue},char const*)'''
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
typeId( (LineSmoothingStateComponent)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreGL::TypedStateComponent<bool, 105057u> {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (LineSmoothingStateComponent)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreGL::TypedStateComponent<bool, 105057u> {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...
    def value (self, *args, **kwargs):
      '''None'''
    ...

def LuminanceTexture (*args):
      '''
__init__(_object*, IECoreImage::ImagePrimitive const*, bool)
__init__(_object*, unsigned int, unsigned int, IECore::Data const*, IECore::Data const*, bool)

'''      
    ...

class LuminanceTexture:
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
    def bind (self, *args, **kwargs):
      '''
bind( (Bindable)arg1) -> None :

    C++ signature :
        void bind(IECoreGL::Bindable {lvalue})'''
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
    def imagePrimitive (self, *args, **kwargs):
      '''
imagePrimitive( (Texture)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECoreImage::ImagePrimitive> imagePrimitive(IECoreGL::Texture {lvalue})'''
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
isInstanceOf( (LuminanceTexture)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::LuminanceTexture {lvalue},IECore::TypeId)

isInstanceOf( (LuminanceTexture)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::LuminanceTexture {lvalue},char const*)'''
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
typeId( (LuminanceTexture)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreGL::LuminanceTexture {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (LuminanceTexture)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreGL::LuminanceTexture {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...

def MeshPrimitive (*args):
      '''

'''      
    ...

class MeshPrimitive:
    def DrawBound (self, *args, **kwargs):
      '''None'''
    ...
    def DrawOutline (self, *args, **kwargs):
      '''None'''
    ...
    def DrawPoints (self, *args, **kwargs):
      '''None'''
    ...
    def DrawSolid (self, *args, **kwargs):
      '''None'''
    ...
    def DrawWireframe (self, *args, **kwargs):
      '''None'''
    ...
    def OutlineWidth (self, *args, **kwargs):
      '''None'''
    ...
    def PointWidth (self, *args, **kwargs):
      '''None'''
    ...
    def Selectable (self, *args, **kwargs):
      '''None'''
    ...
    def TransparencySort (self, *args, **kwargs):
      '''None'''
    ...
    def WireframeWidth (self, *args, **kwargs):
      '''None'''
    ...
    def addPrimitiveVariable (self, *args, **kwargs):
      '''
addPrimitiveVariable( (Primitive)arg1, (object)arg2, (PrimitiveVariable)arg3) -> None :

    C++ signature :
        void addPrimitiveVariable(IECoreGL::Primitive {lvalue},std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >,IECoreScene::PrimitiveVariable)'''
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
bound( (Renderable)arg1) -> Box3f :

    C++ signature :
        Imath_3_1::Box<Imath_3_1::Vec3<float> > bound(IECoreGL::Renderable {lvalue})'''
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
isInstanceOf( (MeshPrimitive)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::MeshPrimitive {lvalue},IECore::TypeId)

isInstanceOf( (MeshPrimitive)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::MeshPrimitive {lvalue},char const*)'''
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
    def render (self, *args, **kwargs):
      '''
render( (Renderable)arg1, (State)arg2) -> None :

    C++ signature :
        void render(IECoreGL::Renderable {lvalue},IECoreGL::State*)'''
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
typeId( (MeshPrimitive)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreGL::MeshPrimitive {lvalue})'''
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
        char const* typeName(IECoreGL::MeshPrimitive {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...

def NameStateComponent (*args):
      '''
__init__(_object*)
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)

'''      
    ...

class NameStateComponent:
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
    def bind (self, *args, **kwargs):
      '''
bind( (Bindable)arg1) -> None :

    C++ signature :
        void bind(IECoreGL::Bindable {lvalue})'''
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
    def glName (self, *args, **kwargs):
      '''
glName( (NameStateComponent)arg1) -> int :

    C++ signature :
        unsigned int glName(IECoreGL::NameStateComponent {lvalue})'''
    ...
    def glNameFromName (self, *args, **kwargs):
      '''
glNameFromName( (object)name [, (bool)createIfMissing=False]) -> int :

    C++ signature :
        unsigned int glNameFromName(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > [,bool=False])'''
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
isInstanceOf( (NameStateComponent)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::NameStateComponent {lvalue},IECore::TypeId)

isInstanceOf( (NameStateComponent)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::NameStateComponent {lvalue},char const*)'''
    ...
    def isSame (self, *args, **kwargs):
      '''
isSame( (RefCounted)arg1, (RefCounted)arg2) -> bool :

    C++ signature :
        bool isSame(IECore::RefCounted const*,IECore::RefCounted const*)'''
    ...
    def name (self, *args, **kwargs):
      '''
name( (NameStateComponent)arg1) -> str :

    C++ signature :
        std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > name(IECoreGL::NameStateComponent {lvalue})'''
    ...
    def nameFromGLName (self, *args, **kwargs):
      '''
nameFromGLName( (int)arg1) -> str :

    C++ signature :
        std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > nameFromGLName(unsigned int)'''
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
typeId( (NameStateComponent)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreGL::NameStateComponent {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (NameStateComponent)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreGL::NameStateComponent {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...

def OutlineColorStateComponent (*args):
      '''
__init__(_object*, Imath_3_1::Color4<float>)

'''      
    ...

class OutlineColorStateComponent:
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
    def bind (self, *args, **kwargs):
      '''
bind( (Bindable)arg1) -> None :

    C++ signature :
        void bind(IECoreGL::Bindable {lvalue})'''
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
isInstanceOf( (OutlineColorStateComponent)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::TypedStateComponent<Imath_3_1::Color4<float>, 105037u> {lvalue},IECore::TypeId)

isInstanceOf( (OutlineColorStateComponent)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::TypedStateComponent<Imath_3_1::Color4<float>, 105037u> {lvalue},char const*)'''
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
typeId( (OutlineColorStateComponent)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreGL::TypedStateComponent<Imath_3_1::Color4<float>, 105037u> {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (OutlineColorStateComponent)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreGL::TypedStateComponent<Imath_3_1::Color4<float>, 105037u> {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...
    def value (self, *args, **kwargs):
      '''None'''
    ...

def PointColorStateComponent (*args):
      '''
__init__(_object*, Imath_3_1::Color4<float>)

'''      
    ...

class PointColorStateComponent:
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
    def bind (self, *args, **kwargs):
      '''
bind( (Bindable)arg1) -> None :

    C++ signature :
        void bind(IECoreGL::Bindable {lvalue})'''
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
isInstanceOf( (PointColorStateComponent)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::TypedStateComponent<Imath_3_1::Color4<float>, 105038u> {lvalue},IECore::TypeId)

isInstanceOf( (PointColorStateComponent)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::TypedStateComponent<Imath_3_1::Color4<float>, 105038u> {lvalue},char const*)'''
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
typeId( (PointColorStateComponent)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreGL::TypedStateComponent<Imath_3_1::Color4<float>, 105038u> {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (PointColorStateComponent)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreGL::TypedStateComponent<Imath_3_1::Color4<float>, 105038u> {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...
    def value (self, *args, **kwargs):
      '''None'''
    ...

def PointSmoothingStateComponent (*args):
      '''
__init__(_object*, bool)

'''      
    ...

class PointSmoothingStateComponent:
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
    def bind (self, *args, **kwargs):
      '''
bind( (Bindable)arg1) -> None :

    C++ signature :
        void bind(IECoreGL::Bindable {lvalue})'''
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
isInstanceOf( (PointSmoothingStateComponent)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::TypedStateComponent<bool, 105056u> {lvalue},IECore::TypeId)

isInstanceOf( (PointSmoothingStateComponent)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::TypedStateComponent<bool, 105056u> {lvalue},char const*)'''
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
typeId( (PointSmoothingStateComponent)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreGL::TypedStateComponent<bool, 105056u> {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (PointSmoothingStateComponent)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreGL::TypedStateComponent<bool, 105056u> {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...
    def value (self, *args, **kwargs):
      '''None'''
    ...

def PointsPrimitive (*args):
      '''
__init__(_object*, IECoreGL::PointsPrimitive::Type)

'''      
    ...

class PointsPrimitive:
    def DrawBound (self, *args, **kwargs):
      '''None'''
    ...
    def DrawOutline (self, *args, **kwargs):
      '''None'''
    ...
    def DrawPoints (self, *args, **kwargs):
      '''None'''
    ...
    def DrawSolid (self, *args, **kwargs):
      '''None'''
    ...
    def DrawWireframe (self, *args, **kwargs):
      '''None'''
    ...
    def GLPointWidth (self, *args, **kwargs):
      '''None'''
    ...
    def OutlineWidth (self, *args, **kwargs):
      '''None'''
    ...
    def PointWidth (self, *args, **kwargs):
      '''None'''
    ...
    def Selectable (self, *args, **kwargs):
      '''None'''
    ...
    def TransparencySort (self, *args, **kwargs):
      '''None'''
    ...
    def Type (self, *args, **kwargs):
      '''None'''
    ...
    def UseGLPoints (self, *args, **kwargs):
      '''None'''
    ...
    def WireframeWidth (self, *args, **kwargs):
      '''None'''
    ...
    def addPrimitiveVariable (self, *args, **kwargs):
      '''
addPrimitiveVariable( (Primitive)arg1, (object)arg2, (PrimitiveVariable)arg3) -> None :

    C++ signature :
        void addPrimitiveVariable(IECoreGL::Primitive {lvalue},std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >,IECoreScene::PrimitiveVariable)'''
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
bound( (Renderable)arg1) -> Box3f :

    C++ signature :
        Imath_3_1::Box<Imath_3_1::Vec3<float> > bound(IECoreGL::Renderable {lvalue})'''
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
isInstanceOf( (PointsPrimitive)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::PointsPrimitive {lvalue},IECore::TypeId)

isInstanceOf( (PointsPrimitive)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::PointsPrimitive {lvalue},char const*)'''
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
    def render (self, *args, **kwargs):
      '''
render( (Renderable)arg1, (State)arg2) -> None :

    C++ signature :
        void render(IECoreGL::Renderable {lvalue},IECoreGL::State*)'''
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
typeId( (PointsPrimitive)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreGL::PointsPrimitive {lvalue})'''
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
        char const* typeName(IECoreGL::PointsPrimitive {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...

def PolygonSmoothingStateComponent (*args):
      '''
__init__(_object*, bool)

'''      
    ...

class PolygonSmoothingStateComponent:
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
    def bind (self, *args, **kwargs):
      '''
bind( (Bindable)arg1) -> None :

    C++ signature :
        void bind(IECoreGL::Bindable {lvalue})'''
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
isInstanceOf( (PolygonSmoothingStateComponent)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::TypedStateComponent<bool, 105058u> {lvalue},IECore::TypeId)

isInstanceOf( (PolygonSmoothingStateComponent)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::TypedStateComponent<bool, 105058u> {lvalue},char const*)'''
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
typeId( (PolygonSmoothingStateComponent)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreGL::TypedStateComponent<bool, 105058u> {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (PolygonSmoothingStateComponent)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreGL::TypedStateComponent<bool, 105058u> {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...
    def value (self, *args, **kwargs):
      '''None'''
    ...

def Primitive (*args):
      '''

'''      
    ...

class Primitive:
    def DrawBound (self, *args, **kwargs):
      '''None'''
    ...
    def DrawOutline (self, *args, **kwargs):
      '''None'''
    ...
    def DrawPoints (self, *args, **kwargs):
      '''None'''
    ...
    def DrawSolid (self, *args, **kwargs):
      '''None'''
    ...
    def DrawWireframe (self, *args, **kwargs):
      '''None'''
    ...
    def OutlineWidth (self, *args, **kwargs):
      '''None'''
    ...
    def PointWidth (self, *args, **kwargs):
      '''None'''
    ...
    def Selectable (self, *args, **kwargs):
      '''None'''
    ...
    def TransparencySort (self, *args, **kwargs):
      '''None'''
    ...
    def WireframeWidth (self, *args, **kwargs):
      '''None'''
    ...
    def addPrimitiveVariable (self, *args, **kwargs):
      '''
addPrimitiveVariable( (Primitive)arg1, (object)arg2, (PrimitiveVariable)arg3) -> None :

    C++ signature :
        void addPrimitiveVariable(IECoreGL::Primitive {lvalue},std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >,IECoreScene::PrimitiveVariable)'''
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
bound( (Renderable)arg1) -> Box3f :

    C++ signature :
        Imath_3_1::Box<Imath_3_1::Vec3<float> > bound(IECoreGL::Renderable {lvalue})'''
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
isInstanceOf( (Primitive)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::Primitive {lvalue},IECore::TypeId)

isInstanceOf( (Primitive)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::Primitive {lvalue},char const*)'''
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
    def render (self, *args, **kwargs):
      '''
render( (Renderable)arg1, (State)arg2) -> None :

    C++ signature :
        void render(IECoreGL::Renderable {lvalue},IECoreGL::State*)'''
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
typeId( (Primitive)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreGL::Primitive {lvalue})'''
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
        char const* typeName(IECoreGL::Primitive {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...

def ProceduralThreadingStateComponent (*args):
      '''
__init__(_object*, bool)

'''      
    ...

class ProceduralThreadingStateComponent:
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
    def bind (self, *args, **kwargs):
      '''
bind( (Bindable)arg1) -> None :

    C++ signature :
        void bind(IECoreGL::Bindable {lvalue})'''
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
isInstanceOf( (ProceduralThreadingStateComponent)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::TypedStateComponent<bool, 105070u> {lvalue},IECore::TypeId)

isInstanceOf( (ProceduralThreadingStateComponent)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::TypedStateComponent<bool, 105070u> {lvalue},char const*)'''
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
typeId( (ProceduralThreadingStateComponent)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreGL::TypedStateComponent<bool, 105070u> {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (ProceduralThreadingStateComponent)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreGL::TypedStateComponent<bool, 105070u> {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...
    def value (self, *args, **kwargs):
      '''None'''
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
    def bound (self, *args, **kwargs):
      '''
bound( (Renderable)arg1) -> Box3f :

    C++ signature :
        Imath_3_1::Box<Imath_3_1::Vec3<float> > bound(IECoreGL::Renderable {lvalue})'''
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
isInstanceOf( (Renderable)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::Renderable {lvalue},IECore::TypeId)

isInstanceOf( (Renderable)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::Renderable {lvalue},char const*)'''
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
    def render (self, *args, **kwargs):
      '''
render( (Renderable)arg1, (State)arg2) -> None :

    C++ signature :
        void render(IECoreGL::Renderable {lvalue},IECoreGL::State*)'''
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
        IECore::TypeId typeId(IECoreGL::Renderable {lvalue})'''
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
        char const* typeName(IECoreGL::Renderable {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...

def Renderer (*args):
      '''
__init__(_object*)

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
        bool isInstanceOf(IECoreGL::Renderer {lvalue},IECore::TypeId)

isInstanceOf( (Renderer)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::Renderer {lvalue},char const*)'''
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
    def scene (self, *args, **kwargs):
      '''
scene( (Renderer)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECoreGL::Scene> scene(IECoreGL::Renderer {lvalue})'''
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
    def shaderLoader (self, *args, **kwargs):
      '''
shaderLoader( (Renderer)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECoreGL::ShaderLoader> shaderLoader(IECoreGL::Renderer {lvalue})'''
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
    def textureLoader (self, *args, **kwargs):
      '''
textureLoader( (Renderer)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECoreGL::TextureLoader> textureLoader(IECoreGL::Renderer {lvalue})'''
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
        IECore::TypeId typeId(IECoreGL::Renderer {lvalue})'''
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
        char const* typeName(IECoreGL::Renderer {lvalue})'''
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
        void worldBegin(IECoreGL::Renderer {lvalue})'''
    ...
    def worldEnd (self, *args, **kwargs):
      '''
worldEnd( (Renderer)arg1) -> None :

    C++ signature :
        void worldEnd(IECoreScene::Renderer {lvalue})'''
    ...

def RendererSpace (*args):
      '''

'''      
    ...

class RendererSpace:
    def ObjectSpace (self, *args, **kwargs):
      '''None'''
    ...
    def WorldSpace (self, *args, **kwargs):
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

def RightHandedOrientationStateComponent (*args):
      '''
__init__(_object*, bool)

'''      
    ...

class RightHandedOrientationStateComponent:
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
    def bind (self, *args, **kwargs):
      '''
bind( (Bindable)arg1) -> None :

    C++ signature :
        void bind(IECoreGL::Bindable {lvalue})'''
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
isInstanceOf( (RightHandedOrientationStateComponent)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::TypedStateComponent<bool, 105048u> {lvalue},IECore::TypeId)

isInstanceOf( (RightHandedOrientationStateComponent)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::TypedStateComponent<bool, 105048u> {lvalue},char const*)'''
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
typeId( (RightHandedOrientationStateComponent)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreGL::TypedStateComponent<bool, 105048u> {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (RightHandedOrientationStateComponent)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreGL::TypedStateComponent<bool, 105048u> {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...
    def value (self, *args, **kwargs):
      '''None'''
    ...

def Scene (*args):
      '''
__init__(_object*)

'''      
    ...

class Scene:
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
bound( (Renderable)arg1) -> Box3f :

    C++ signature :
        Imath_3_1::Box<Imath_3_1::Vec3<float> > bound(IECoreGL::Renderable {lvalue})'''
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
    def getCamera (self, *args, **kwargs):
      '''
getCamera( (Scene)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECoreGL::Camera> getCamera(IECoreGL::Scene {lvalue})'''
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
isInstanceOf( (Scene)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::Scene {lvalue},IECore::TypeId)

isInstanceOf( (Scene)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::Scene {lvalue},char const*)'''
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
    def render (self, *args, **kwargs):
      '''
render( (Scene)arg1) -> None :

    C++ signature :
        void render(IECoreGL::Scene {lvalue})

render( (Scene)arg1, (State)arg2) -> None :

    C++ signature :
        void render(IECoreGL::Scene {lvalue},IECoreGL::State*)'''
    ...
    def root (self, *args, **kwargs):
      '''
root( (Scene)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECoreGL::Group> root(IECoreGL::Scene {lvalue})'''
    ...
    def select (self, *args, **kwargs):
      '''
select( (Scene)arg1, (Mode)arg2, (Box2f)arg3) -> list :

    C++ signature :
        boost::python::list select(IECoreGL::Scene {lvalue},IECoreGL::Selector::Mode,Imath_3_1::Box<Imath_3_1::Vec2<float> >)'''
    ...
    def setCamera (self, *args, **kwargs):
      '''
setCamera( (Scene)arg1, (object)arg2) -> None :

    C++ signature :
        void setCamera(IECoreGL::Scene {lvalue},boost::intrusive_ptr<IECoreGL::Camera>)'''
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
typeId( (Scene)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreGL::Scene {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (Scene)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreGL::Scene {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...

def Selector (*args):
      '''
__init__(_object*, Imath_3_1::Box<Imath_3_1::Vec2<float> >, IECoreGL::Selector::Mode, boost::python::list)

'''      
    ...

class Selector:
    def Mode (self, *args, **kwargs):
      '''None'''
    ...
    def baseState (self, *args, **kwargs):
      '''
baseState( (Selector)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECoreGL::State> baseState(IECoreGL::SelectorContext {lvalue})'''
    ...
    def loadName (self, *args, **kwargs):
      '''
loadName( (Selector)arg1, (int)arg2) -> None :

    C++ signature :
        void loadName(IECoreGL::SelectorContext {lvalue},unsigned int)'''
    ...

def Shader (*args):
      '''
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)

'''      
    ...

class Shader:
    def Parameter (self, *args, **kwargs):
      '''None'''
    ...
    def Setup (self, *args, **kwargs):
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
    def constant (self, *args, **kwargs):
      '''
constant() -> object :

    C++ signature :
        IECoreGL::Shader* constant()'''
    ...
    def csParameter (self, *args, **kwargs):
      '''
csParameter( (Shader)arg1) -> object :

    C++ signature :
        boost::python::api::object csParameter(IECoreGL::Shader)'''
    ...
    def defaultFragmentSource (self, *args, **kwargs):
      '''
defaultFragmentSource() -> str :

    C++ signature :
        std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > defaultFragmentSource()'''
    ...
    def defaultVertexSource (self, *args, **kwargs):
      '''
defaultVertexSource() -> str :

    C++ signature :
        std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > defaultVertexSource()'''
    ...
    def derivedTypeIds (self, *args, **kwargs):
      '''
derivedTypeIds( (TypeId)arg1) -> list :

    C++ signature :
        boost::python::list derivedTypeIds(IECore::TypeId)'''
    ...
    def facingRatio (self, *args, **kwargs):
      '''
facingRatio() -> object :

    C++ signature :
        IECoreGL::Shader* facingRatio()'''
    ...
    def fragmentSource (self, *args, **kwargs):
      '''
fragmentSource( (Shader)arg1) -> str :

    C++ signature :
        std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > fragmentSource(IECoreGL::Shader {lvalue})'''
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
    def geometrySource (self, *args, **kwargs):
      '''
geometrySource( (Shader)arg1) -> str :

    C++ signature :
        std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > geometrySource(IECoreGL::Shader {lvalue})'''
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
isInstanceOf( (Shader)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::Shader {lvalue},IECore::TypeId)

isInstanceOf( (Shader)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::Shader {lvalue},char const*)'''
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
    def program (self, *args, **kwargs):
      '''
program( (Shader)arg1) -> int :

    C++ signature :
        unsigned int program(IECoreGL::Shader {lvalue})'''
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
typeId( (Shader)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreGL::Shader {lvalue})'''
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
        char const* typeName(IECoreGL::Shader {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...
    def uniformParameter (self, *args, **kwargs):
      '''
uniformParameter( (Shader)arg1, (object)arg2) -> object :

    C++ signature :
        boost::python::api::object uniformParameter(IECoreGL::Shader,std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)'''
    ...
    def uniformParameterNames (self, *args, **kwargs):
      '''
uniformParameterNames( (Shader)arg1) -> list :

    C++ signature :
        boost::python::list uniformParameterNames(IECoreGL::Shader)'''
    ...
    def vertexAttribute (self, *args, **kwargs):
      '''
vertexAttribute( (Shader)arg1, (object)arg2) -> object :

    C++ signature :
        boost::python::api::object vertexAttribute(IECoreGL::Shader,std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)'''
    ...
    def vertexAttributeNames (self, *args, **kwargs):
      '''
vertexAttributeNames( (Shader)arg1) -> list :

    C++ signature :
        boost::python::list vertexAttributeNames(IECoreGL::Shader)'''
    ...
    def vertexSource (self, *args, **kwargs):
      '''
vertexSource( (Shader)arg1) -> str :

    C++ signature :
        std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > vertexSource(IECoreGL::Shader {lvalue})'''
    ...

def ShaderLoader (*args):
      '''
__init__(_object*, IECore::SearchPath, IECore::SearchPath const*)
__init__(_object*, IECore::SearchPath)

'''      
    ...

class ShaderLoader:
    def clear (self, *args, **kwargs):
      '''
clear( (ShaderLoader)arg1) -> None :

    C++ signature :
        void clear(IECoreGL::ShaderLoader {lvalue})'''
    ...
    def collectGarbage (self, *args, **kwargs):
      '''
collectGarbage() -> None :

    C++ signature :
        void collectGarbage()'''
    ...
    def create (self, *args, **kwargs):
      '''
create( (ShaderLoader)arg1, (object)arg2, (object)arg3, (object)arg4) -> object :

    C++ signature :
        boost::intrusive_ptr<IECoreGL::Shader> create(IECoreGL::ShaderLoader {lvalue},std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >,std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >,std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)'''
    ...
    def defaultShaderLoader (self, *args, **kwargs):
      '''
defaultShaderLoader() -> object :

    C++ signature :
        IECoreGL::ShaderLoader* defaultShaderLoader()'''
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
    def load (self, *args, **kwargs):
      '''
load( (ShaderLoader)arg1, (object)arg2) -> object :

    C++ signature :
        boost::intrusive_ptr<IECoreGL::Shader> load(IECoreGL::ShaderLoader {lvalue},std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)'''
    ...
    def loadSource (self, *args, **kwargs):
      '''
loadSource( (ShaderLoader)arg1, (object)arg2) -> tuple :

    C++ signature :
        boost::python::tuple loadSource(IECoreGL::ShaderLoader {lvalue},std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)'''
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

def ShaderStateComponent (*args):
      '''
__init__(_object*, boost::intrusive_ptr<IECoreGL::ShaderLoader>, boost::intrusive_ptr<IECoreGL::TextureLoader>, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, boost::intrusive_ptr<IECore::CompoundObject const>)
__init__(_object*)

'''      
    ...

class ShaderStateComponent:
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
    def bind (self, *args, **kwargs):
      '''
bind( (Bindable)arg1) -> None :

    C++ signature :
        void bind(IECoreGL::Bindable {lvalue})'''
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
hash( (ShaderStateComponent)arg1) -> MurmurHash :

    C++ signature :
        IECore::MurmurHash hash(IECoreGL::ShaderStateComponent {lvalue})'''
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
isInstanceOf( (ShaderStateComponent)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::ShaderStateComponent {lvalue},IECore::TypeId)

isInstanceOf( (ShaderStateComponent)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::ShaderStateComponent {lvalue},char const*)'''
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
    def shaderLoader (self, *args, **kwargs):
      '''
shaderLoader( (ShaderStateComponent)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECoreGL::ShaderLoader> shaderLoader(IECoreGL::ShaderStateComponent {lvalue})'''
    ...
    def shaderSetup (self, *args, **kwargs):
      '''
shaderSetup( (ShaderStateComponent)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECoreGL::Shader::Setup> shaderSetup(IECoreGL::ShaderStateComponent {lvalue})'''
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
    def textureLoader (self, *args, **kwargs):
      '''
textureLoader( (ShaderStateComponent)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECoreGL::TextureLoader> textureLoader(IECoreGL::ShaderStateComponent {lvalue})'''
    ...
    def typeId (self, *args, **kwargs):
      '''
typeId( (ShaderStateComponent)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreGL::ShaderStateComponent {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (ShaderStateComponent)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreGL::ShaderStateComponent {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...

def SplineToGLTextureConverter (*args):
      '''
__init__(_object*, boost::intrusive_ptr<IECore::Object const>)

'''      
    ...

class SplineToGLTextureConverter:
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
    def convert (self, *args, **kwargs):
      '''
convert( (ToGLConverter)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::RunTimeTyped> convert(IECoreGL::ToGLConverter {lvalue})'''
    ...
    def create (self, *args, **kwargs):
      '''
create( (object)object [, (TypeId)resultType=IECore._IECore.TypeId.RunTimeTyped]) -> object :

    C++ signature :
        boost::intrusive_ptr<IECoreGL::ToGLConverter> create(boost::intrusive_ptr<IECore::Object const> [,IECore::TypeId=IECore._IECore.TypeId.RunTimeTyped])'''
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
isInstanceOf( (SplineToGLTextureConverter)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::SplineToGLTextureConverter {lvalue},IECore::TypeId)

isInstanceOf( (SplineToGLTextureConverter)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::SplineToGLTextureConverter {lvalue},char const*)'''
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
    def srcParameter (self, *args, **kwargs):
      '''
srcParameter( (FromCoreConverter)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::ObjectParameter> srcParameter(IECore::FromCoreConverter {lvalue})'''
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
typeId( (SplineToGLTextureConverter)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreGL::SplineToGLTextureConverter {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (SplineToGLTextureConverter)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreGL::SplineToGLTextureConverter {lvalue})'''
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

def State (*args):
      '''
__init__(_object*, IECoreGL::State)
__init__(_object*, bool)

'''      
    ...

class State:
    def ScopedBinding (state, currentState):
      '''None'''
    ...
    def _ScopedBinding (self, *args, **kwargs):
      '''None'''
    ...
    def add (self, *args, **kwargs):
      '''
add( (State)arg1, (object)arg2) -> None :

    C++ signature :
        void add(IECoreGL::State {lvalue},boost::intrusive_ptr<IECoreGL::State>)

add( (State)arg1, (object)component [, (bool)override=False]) -> None :

    C++ signature :
        void add(IECoreGL::State {lvalue},boost::intrusive_ptr<IECoreGL::StateComponent> [,bool=False])'''
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
    def bind (self, *args, **kwargs):
      '''
bind( (Bindable)arg1) -> None :

    C++ signature :
        void bind(IECoreGL::Bindable {lvalue})'''
    ...
    def bindBaseState (self, *args, **kwargs):
      '''
bindBaseState() -> None :

    C++ signature :
        void bindBaseState()'''
    ...
    def collectGarbage (self, *args, **kwargs):
      '''
collectGarbage() -> None :

    C++ signature :
        void collectGarbage()'''
    ...
    def defaultState (self, *args, **kwargs):
      '''
defaultState() -> object :

    C++ signature :
        boost::intrusive_ptr<IECoreGL::State> defaultState()'''
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
    def get (self, *args, **kwargs):
      '''
get( (State)arg1, (TypeId)arg2) -> object :

    C++ signature :
        boost::intrusive_ptr<IECoreGL::StateComponent> get(IECoreGL::State {lvalue},IECore::TypeId)'''
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
isComplete( (State)arg1) -> bool :

    C++ signature :
        bool isComplete(IECoreGL::State {lvalue})'''
    ...
    def isInstanceOf (self, *args, **kwargs):
      '''
isInstanceOf( (State)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::State {lvalue},IECore::TypeId)

isInstanceOf( (State)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::State {lvalue},char const*)'''
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
    def remove (self, *args, **kwargs):
      '''
remove( (State)arg1, (TypeId)arg2) -> None :

    C++ signature :
        void remove(IECoreGL::State {lvalue},IECore::TypeId)'''
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
typeId( (State)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreGL::State {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (State)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreGL::State {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...
    def userAttributes (self, *args, **kwargs):
      '''
userAttributes( (State)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::CompoundData> userAttributes(IECoreGL::State {lvalue})'''
    ...

def StateComponent (*args):
      '''

'''      
    ...

class StateComponent:
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
    def bind (self, *args, **kwargs):
      '''
bind( (Bindable)arg1) -> None :

    C++ signature :
        void bind(IECoreGL::Bindable {lvalue})'''
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
isInstanceOf( (StateComponent)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::StateComponent {lvalue},IECore::TypeId)

isInstanceOf( (StateComponent)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::StateComponent {lvalue},char const*)'''
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
typeId( (StateComponent)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreGL::StateComponent {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (StateComponent)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreGL::StateComponent {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...

def Texture (*args):
      '''
__init__(_object*, unsigned int)

'''      
    ...

class Texture:
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
    def bind (self, *args, **kwargs):
      '''
bind( (Bindable)arg1) -> None :

    C++ signature :
        void bind(IECoreGL::Bindable {lvalue})'''
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
    def imagePrimitive (self, *args, **kwargs):
      '''
imagePrimitive( (Texture)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECoreImage::ImagePrimitive> imagePrimitive(IECoreGL::Texture {lvalue})'''
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
isInstanceOf( (Texture)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::Texture {lvalue},IECore::TypeId)

isInstanceOf( (Texture)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::Texture {lvalue},char const*)'''
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
typeId( (Texture)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreGL::Texture {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (Texture)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreGL::Texture {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...

def TextureLoader (*args):
      '''
__init__(_object*, IECore::SearchPath)

'''      
    ...

class TextureLoader:
    def clear (self, *args, **kwargs):
      '''
clear( (TextureLoader)arg1) -> None :

    C++ signature :
        void clear(IECoreGL::TextureLoader {lvalue})'''
    ...
    def collectGarbage (self, *args, **kwargs):
      '''
collectGarbage() -> None :

    C++ signature :
        void collectGarbage()'''
    ...
    def defaultTextureLoader (self, *args, **kwargs):
      '''
defaultTextureLoader() -> object :

    C++ signature :
        IECoreGL::TextureLoader* defaultTextureLoader()'''
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
    def load (self, *args, **kwargs):
      '''
load( (TextureLoader)arg1, (object)fileName [, (int)maximumResolution=2147483647]) -> object :

    C++ signature :
        boost::intrusive_ptr<IECoreGL::Texture> load(IECoreGL::TextureLoader {lvalue},std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > [,int=2147483647])'''
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

def ToGLCameraConverter (*args):
      '''
__init__(_object*, boost::intrusive_ptr<IECoreScene::Camera const>)

'''      
    ...

class ToGLCameraConverter:
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
    def convert (self, *args, **kwargs):
      '''
convert( (ToGLConverter)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::RunTimeTyped> convert(IECoreGL::ToGLConverter {lvalue})'''
    ...
    def create (self, *args, **kwargs):
      '''
create( (object)object [, (TypeId)resultType=IECore._IECore.TypeId.RunTimeTyped]) -> object :

    C++ signature :
        boost::intrusive_ptr<IECoreGL::ToGLConverter> create(boost::intrusive_ptr<IECore::Object const> [,IECore::TypeId=IECore._IECore.TypeId.RunTimeTyped])'''
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
isInstanceOf( (ToGLCameraConverter)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::ToGLCameraConverter {lvalue},IECore::TypeId)

isInstanceOf( (ToGLCameraConverter)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::ToGLCameraConverter {lvalue},char const*)'''
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
    def srcParameter (self, *args, **kwargs):
      '''
srcParameter( (FromCoreConverter)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::ObjectParameter> srcParameter(IECore::FromCoreConverter {lvalue})'''
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
typeId( (ToGLCameraConverter)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreGL::ToGLCameraConverter {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (ToGLCameraConverter)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreGL::ToGLCameraConverter {lvalue})'''
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

def ToGLConverter (*args):
      '''

'''      
    ...

class ToGLConverter:
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
    def convert (self, *args, **kwargs):
      '''
convert( (ToGLConverter)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::RunTimeTyped> convert(IECoreGL::ToGLConverter {lvalue})'''
    ...
    def create (self, *args, **kwargs):
      '''
create( (object)object [, (TypeId)resultType=IECore._IECore.TypeId.RunTimeTyped]) -> object :

    C++ signature :
        boost::intrusive_ptr<IECoreGL::ToGLConverter> create(boost::intrusive_ptr<IECore::Object const> [,IECore::TypeId=IECore._IECore.TypeId.RunTimeTyped])'''
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
isInstanceOf( (ToGLConverter)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::ToGLConverter {lvalue},IECore::TypeId)

isInstanceOf( (ToGLConverter)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::ToGLConverter {lvalue},char const*)'''
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
    def srcParameter (self, *args, **kwargs):
      '''
srcParameter( (FromCoreConverter)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::ObjectParameter> srcParameter(IECore::FromCoreConverter {lvalue})'''
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
typeId( (ToGLConverter)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreGL::ToGLConverter {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (ToGLConverter)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreGL::ToGLConverter {lvalue})'''
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

def ToGLCurvesConverter (*args):
      '''
__init__(_object*, boost::intrusive_ptr<IECoreScene::CurvesPrimitive const>)

'''      
    ...

class ToGLCurvesConverter:
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
    def convert (self, *args, **kwargs):
      '''
convert( (ToGLConverter)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::RunTimeTyped> convert(IECoreGL::ToGLConverter {lvalue})'''
    ...
    def create (self, *args, **kwargs):
      '''
create( (object)object [, (TypeId)resultType=IECore._IECore.TypeId.RunTimeTyped]) -> object :

    C++ signature :
        boost::intrusive_ptr<IECoreGL::ToGLConverter> create(boost::intrusive_ptr<IECore::Object const> [,IECore::TypeId=IECore._IECore.TypeId.RunTimeTyped])'''
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
isInstanceOf( (ToGLCurvesConverter)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::ToGLCurvesConverter {lvalue},IECore::TypeId)

isInstanceOf( (ToGLCurvesConverter)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::ToGLCurvesConverter {lvalue},char const*)'''
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
    def srcParameter (self, *args, **kwargs):
      '''
srcParameter( (FromCoreConverter)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::ObjectParameter> srcParameter(IECore::FromCoreConverter {lvalue})'''
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
typeId( (ToGLCurvesConverter)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreGL::ToGLCurvesConverter {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (ToGLCurvesConverter)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreGL::ToGLCurvesConverter {lvalue})'''
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

def ToGLMeshConverter (*args):
      '''
__init__(_object*, boost::intrusive_ptr<IECoreScene::MeshPrimitive const>)

'''      
    ...

class ToGLMeshConverter:
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
    def convert (self, *args, **kwargs):
      '''
convert( (ToGLConverter)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::RunTimeTyped> convert(IECoreGL::ToGLConverter {lvalue})'''
    ...
    def create (self, *args, **kwargs):
      '''
create( (object)object [, (TypeId)resultType=IECore._IECore.TypeId.RunTimeTyped]) -> object :

    C++ signature :
        boost::intrusive_ptr<IECoreGL::ToGLConverter> create(boost::intrusive_ptr<IECore::Object const> [,IECore::TypeId=IECore._IECore.TypeId.RunTimeTyped])'''
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
isInstanceOf( (ToGLMeshConverter)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::ToGLMeshConverter {lvalue},IECore::TypeId)

isInstanceOf( (ToGLMeshConverter)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::ToGLMeshConverter {lvalue},char const*)'''
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
    def srcParameter (self, *args, **kwargs):
      '''
srcParameter( (FromCoreConverter)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::ObjectParameter> srcParameter(IECore::FromCoreConverter {lvalue})'''
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
typeId( (ToGLMeshConverter)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreGL::ToGLMeshConverter {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (ToGLMeshConverter)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreGL::ToGLMeshConverter {lvalue})'''
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

def ToGLPointsConverter (*args):
      '''
__init__(_object*, boost::intrusive_ptr<IECoreScene::PointsPrimitive const>)

'''      
    ...

class ToGLPointsConverter:
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
    def convert (self, *args, **kwargs):
      '''
convert( (ToGLConverter)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::RunTimeTyped> convert(IECoreGL::ToGLConverter {lvalue})'''
    ...
    def create (self, *args, **kwargs):
      '''
create( (object)object [, (TypeId)resultType=IECore._IECore.TypeId.RunTimeTyped]) -> object :

    C++ signature :
        boost::intrusive_ptr<IECoreGL::ToGLConverter> create(boost::intrusive_ptr<IECore::Object const> [,IECore::TypeId=IECore._IECore.TypeId.RunTimeTyped])'''
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
isInstanceOf( (ToGLPointsConverter)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::ToGLPointsConverter {lvalue},IECore::TypeId)

isInstanceOf( (ToGLPointsConverter)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::ToGLPointsConverter {lvalue},char const*)'''
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
    def srcParameter (self, *args, **kwargs):
      '''
srcParameter( (FromCoreConverter)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::ObjectParameter> srcParameter(IECore::FromCoreConverter {lvalue})'''
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
typeId( (ToGLPointsConverter)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreGL::ToGLPointsConverter {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (ToGLPointsConverter)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreGL::ToGLPointsConverter {lvalue})'''
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

def ToGLStateConverter (*args):
      '''
__init__(_object*, boost::intrusive_ptr<IECore::CompoundObject const>)

'''      
    ...

class ToGLStateConverter:
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
    def convert (self, *args, **kwargs):
      '''
convert( (ToGLConverter)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::RunTimeTyped> convert(IECoreGL::ToGLConverter {lvalue})'''
    ...
    def create (self, *args, **kwargs):
      '''
create( (object)object [, (TypeId)resultType=IECore._IECore.TypeId.RunTimeTyped]) -> object :

    C++ signature :
        boost::intrusive_ptr<IECoreGL::ToGLConverter> create(boost::intrusive_ptr<IECore::Object const> [,IECore::TypeId=IECore._IECore.TypeId.RunTimeTyped])'''
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
isInstanceOf( (ToGLStateConverter)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::ToGLStateConverter {lvalue},IECore::TypeId)

isInstanceOf( (ToGLStateConverter)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::ToGLStateConverter {lvalue},char const*)'''
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
    def srcParameter (self, *args, **kwargs):
      '''
srcParameter( (FromCoreConverter)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::ObjectParameter> srcParameter(IECore::FromCoreConverter {lvalue})'''
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
typeId( (ToGLStateConverter)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreGL::ToGLStateConverter {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (ToGLStateConverter)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreGL::ToGLStateConverter {lvalue})'''
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

def ToGLTextureConverter (*args):
      '''
__init__(_object*, boost::intrusive_ptr<IECore::Object const>, bool createMissingRGBChannels=False)

'''      
    ...

class ToGLTextureConverter:
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
    def convert (self, *args, **kwargs):
      '''
convert( (ToGLConverter)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::RunTimeTyped> convert(IECoreGL::ToGLConverter {lvalue})'''
    ...
    def create (self, *args, **kwargs):
      '''
create( (object)object [, (TypeId)resultType=IECore._IECore.TypeId.RunTimeTyped]) -> object :

    C++ signature :
        boost::intrusive_ptr<IECoreGL::ToGLConverter> create(boost::intrusive_ptr<IECore::Object const> [,IECore::TypeId=IECore._IECore.TypeId.RunTimeTyped])'''
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
isInstanceOf( (ToGLTextureConverter)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::ToGLTextureConverter {lvalue},IECore::TypeId)

isInstanceOf( (ToGLTextureConverter)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::ToGLTextureConverter {lvalue},char const*)'''
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
    def srcParameter (self, *args, **kwargs):
      '''
srcParameter( (FromCoreConverter)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::ObjectParameter> srcParameter(IECore::FromCoreConverter {lvalue})'''
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
typeId( (ToGLTextureConverter)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreGL::ToGLTextureConverter {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (ToGLTextureConverter)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreGL::ToGLTextureConverter {lvalue})'''
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

def TransparentShadingStateComponent (*args):
      '''
__init__(_object*, bool)

'''      
    ...

class TransparentShadingStateComponent:
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
    def bind (self, *args, **kwargs):
      '''
bind( (Bindable)arg1) -> None :

    C++ signature :
        void bind(IECoreGL::Bindable {lvalue})'''
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
isInstanceOf( (TransparentShadingStateComponent)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::TypedStateComponent<bool, 105033u> {lvalue},IECore::TypeId)

isInstanceOf( (TransparentShadingStateComponent)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::TypedStateComponent<bool, 105033u> {lvalue},char const*)'''
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
typeId( (TransparentShadingStateComponent)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreGL::TypedStateComponent<bool, 105033u> {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (TransparentShadingStateComponent)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreGL::TypedStateComponent<bool, 105033u> {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...
    def value (self, *args, **kwargs):
      '''None'''
    ...

def WireframeColorStateComponent (*args):
      '''
__init__(_object*, Imath_3_1::Color4<float>)

'''      
    ...

class WireframeColorStateComponent:
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
    def bind (self, *args, **kwargs):
      '''
bind( (Bindable)arg1) -> None :

    C++ signature :
        void bind(IECoreGL::Bindable {lvalue})'''
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
isInstanceOf( (WireframeColorStateComponent)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::TypedStateComponent<Imath_3_1::Color4<float>, 105036u> {lvalue},IECore::TypeId)

isInstanceOf( (WireframeColorStateComponent)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(IECoreGL::TypedStateComponent<Imath_3_1::Color4<float>, 105036u> {lvalue},char const*)'''
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
typeId( (WireframeColorStateComponent)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(IECoreGL::TypedStateComponent<Imath_3_1::Color4<float>, 105036u> {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (WireframeColorStateComponent)arg1) -> str :

    C++ signature :
        char const* typeName(IECoreGL::TypedStateComponent<Imath_3_1::Color4<float>, 105036u> {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...
    def value (self, *args, **kwargs):
      '''None'''
    ...

def _IECoreGL (*args):
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

def glslVersion (*args):
      '''

'''      
    ...

def init (*args):
      '''

'''      
    ...
