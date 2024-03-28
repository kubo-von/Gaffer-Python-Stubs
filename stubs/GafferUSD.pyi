
def USDAttributes (*args):
      '''
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > name='USDAttributes')

'''      
    ...

class USDAttributes:
    def BinaryPlugSignal (self, *args, **kwargs):
      '''None'''
    ...
    def BinarySignal (self, *args, **kwargs):
      '''None'''
    ...
    def ErrorSignal (self, *args, **kwargs):
      '''None'''
    ...
    def NameChangedSignal (self, *args, **kwargs):
      '''None'''
    ...
    def Range (parent):
      '''None'''
    ...
    def RecursiveRange (parent):
      '''None'''
    ...
    def UnaryPlugSignal (self, *args, **kwargs):
      '''None'''
    ...
    def UnarySignal (self, *args, **kwargs):
      '''None'''
    ...
    def acceptsChild (self, *args, **kwargs):
      '''
acceptsChild( (USDAttributes)arg1, (GraphComponent)arg2) -> bool :

    C++ signature :
        bool acceptsChild(GafferUSD::USDAttributes,Gaffer::GraphComponent const*)'''
    ...
    def acceptsParent (self, *args, **kwargs):
      '''
acceptsParent( (USDAttributes)arg1, (GraphComponent)arg2) -> bool :

    C++ signature :
        bool acceptsParent(GafferUSD::USDAttributes,Gaffer::GraphComponent const*)'''
    ...
    def addChild (self, *args, **kwargs):
      '''
addChild( (GraphComponent)arg1, (GraphComponent)arg2) -> None :

    C++ signature :
        void addChild(Gaffer::GraphComponent {lvalue},Gaffer::GraphComponent {lvalue})'''
    ...
    def affects (self, *args, **kwargs):
      '''
affects( (USDAttributes)arg1, (Plug)arg2) -> list :

    C++ signature :
        boost::python::list affects(GafferUSD::USDAttributes,Gaffer::Plug const*)'''
    ...
    def ancestor (self, *args, **kwargs):
      '''
ancestor( (GraphComponent)arg1, (TypeId)arg2) -> object :

    C++ signature :
        boost::intrusive_ptr<Gaffer::GraphComponent> ancestor(Gaffer::GraphComponent {lvalue},IECore::TypeId)'''
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
    def childAddedSignal (self, *args, **kwargs):
      '''
childAddedSignal( (GraphComponent)arg1) -> BinarySignal :

    C++ signature :
        Gaffer::Signals::Signal<void (Gaffer::GraphComponent*, Gaffer::GraphComponent*), Gaffer::Signals::CatchingCombiner<void> > {lvalue} childAddedSignal(Gaffer::GraphComponent {lvalue})'''
    ...
    def childRemovedSignal (self, *args, **kwargs):
      '''
childRemovedSignal( (GraphComponent)arg1) -> BinarySignal :

    C++ signature :
        Gaffer::Signals::Signal<void (Gaffer::GraphComponent*, Gaffer::GraphComponent*), Gaffer::Signals::CatchingCombiner<void> > {lvalue} childRemovedSignal(Gaffer::GraphComponent {lvalue})'''
    ...
    def children (self, *args, **kwargs):
      '''
children( (GraphComponent)self [, (TypeId)typeId=IECore._IECore.TypeId(110000)]) -> tuple :

    C++ signature :
        boost::python::tuple children(Gaffer::GraphComponent {lvalue} [,IECore::TypeId=IECore._IECore.TypeId(110000)])'''
    ...
    def childrenReorderedSignal (self, *args, **kwargs):
      '''
childrenReorderedSignal( (GraphComponent)arg1) -> BinarySignal :

    C++ signature :
        Gaffer::Signals::Signal<void (Gaffer::GraphComponent*, std::vector<unsigned long, std::allocator<unsigned long> > const&), Gaffer::Signals::CatchingCombiner<void> > {lvalue} childrenReorderedSignal(Gaffer::GraphComponent {lvalue})'''
    ...
    def clearChildren (self, *args, **kwargs):
      '''
clearChildren( (GraphComponent)arg1) -> None :

    C++ signature :
        void clearChildren(Gaffer::GraphComponent {lvalue})'''
    ...
    def collectGarbage (self, *args, **kwargs):
      '''
collectGarbage() -> None :

    C++ signature :
        void collectGarbage()'''
    ...
    def commonAncestor (self, *args, **kwargs):
      '''
commonAncestor( (GraphComponent)self, (GraphComponent)other [, (TypeId)ancestorType=IECore._IECore.TypeId(110000)]) -> object :

    C++ signature :
        boost::intrusive_ptr<Gaffer::GraphComponent> commonAncestor(Gaffer::GraphComponent {lvalue},Gaffer::GraphComponent const* [,IECore::TypeId=IECore._IECore.TypeId(110000)])'''
    ...
    def correspondingInput (self, *args, **kwargs):
      '''
correspondingInput( (USDAttributes)arg1, (Plug)arg2) -> object :

    C++ signature :
        boost::intrusive_ptr<Gaffer::Plug> correspondingInput(GafferUSD::USDAttributes {lvalue},Gaffer::Plug const*)'''
    ...
    def derivedTypeIds (self, *args, **kwargs):
      '''
derivedTypeIds( (TypeId)arg1) -> list :

    C++ signature :
        boost::python::list derivedTypeIds(IECore::TypeId)'''
    ...
    def descendant (self, *args, **kwargs):
      '''
descendant( (GraphComponent)arg1, (object)arg2) -> object :

    C++ signature :
        boost::intrusive_ptr<Gaffer::GraphComponent> descendant(Gaffer::GraphComponent {lvalue},std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)'''
    ...
    def enabledPlug (self, *args, **kwargs):
      '''
enabledPlug( (USDAttributes)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<Gaffer::TypedPlug<bool> > enabledPlug(GafferUSD::USDAttributes {lvalue})'''
    ...
    def errorSignal (self, *args, **kwargs):
      '''
errorSignal( (Node)arg1) -> ErrorSignal :

    C++ signature :
        Gaffer::Signals::Signal<void (Gaffer::Plug const*, Gaffer::Plug const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&), Gaffer::Signals::CatchingCombiner<void> > {lvalue} errorSignal(Gaffer::Node {lvalue})'''
    ...
    def fullName (self, *args, **kwargs):
      '''
fullName( (GraphComponent)arg1) -> str :

    C++ signature :
        std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > fullName(Gaffer::GraphComponent {lvalue})'''
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
    def getChild (self, *args, **kwargs):
      '''
getChild( (GraphComponent)arg1, (InternedString)arg2) -> object :

    C++ signature :
        boost::intrusive_ptr<Gaffer::GraphComponent> getChild(Gaffer::GraphComponent {lvalue},IECore::InternedString)'''
    ...
    def getName (self, *args, **kwargs):
      '''
getName( (GraphComponent)arg1) -> str :

    C++ signature :
        char const* getName(Gaffer::GraphComponent {lvalue})'''
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
    def isAncestorOf (self, *args, **kwargs):
      '''
isAncestorOf( (GraphComponent)arg1, (GraphComponent)arg2) -> bool :

    C++ signature :
        bool isAncestorOf(Gaffer::GraphComponent {lvalue},Gaffer::GraphComponent const*)'''
    ...
    def isInstanceOf (self, *args, **kwargs):
      '''
isInstanceOf( (USDAttributes)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(GafferUSD::USDAttributes {lvalue},IECore::TypeId)

isInstanceOf( (USDAttributes)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(GafferUSD::USDAttributes {lvalue},char const*)'''
    ...
    def isSame (self, *args, **kwargs):
      '''
isSame( (RefCounted)arg1, (RefCounted)arg2) -> bool :

    C++ signature :
        bool isSame(IECore::RefCounted const*,IECore::RefCounted const*)'''
    ...
    def items (self, *args, **kwargs):
      '''
items( (GraphComponent)arg1) -> list :

    C++ signature :
        boost::python::list items(Gaffer::GraphComponent {lvalue})'''
    ...
    def keys (self, *args, **kwargs):
      '''
keys( (GraphComponent)arg1) -> list :

    C++ signature :
        boost::python::list keys(Gaffer::GraphComponent {lvalue})'''
    ...
    def nameChangedSignal (self, *args, **kwargs):
      '''
nameChangedSignal( (GraphComponent)arg1) -> NameChangedSignal :

    C++ signature :
        Gaffer::Signals::Signal<void (Gaffer::GraphComponent*, IECore::InternedString), Gaffer::Signals::CatchingCombiner<void> > {lvalue} nameChangedSignal(Gaffer::GraphComponent {lvalue})'''
    ...
    def numWrappedInstances (self, *args, **kwargs):
      '''
numWrappedInstances() -> int :

    C++ signature :
        unsigned long numWrappedInstances()'''
    ...
    def parent (self, *args, **kwargs):
      '''
parent( (GraphComponent)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<Gaffer::GraphComponent> parent(Gaffer::GraphComponent {lvalue})'''
    ...
    def parentChangedSignal (self, *args, **kwargs):
      '''
parentChangedSignal( (GraphComponent)arg1) -> BinarySignal :

    C++ signature :
        Gaffer::Signals::Signal<void (Gaffer::GraphComponent*, Gaffer::GraphComponent*), Gaffer::Signals::CatchingCombiner<void> > {lvalue} parentChangedSignal(Gaffer::GraphComponent {lvalue})'''
    ...
    def plugDirtiedSignal (self, *args, **kwargs):
      '''
plugDirtiedSignal( (Node)arg1) -> UnaryPlugSignal :

    C++ signature :
        Gaffer::Signals::Signal<void (Gaffer::Plug*), Gaffer::Signals::CatchingCombiner<void> > {lvalue} plugDirtiedSignal(Gaffer::Node {lvalue})'''
    ...
    def plugInputChangedSignal (self, *args, **kwargs):
      '''
plugInputChangedSignal( (Node)arg1) -> UnaryPlugSignal :

    C++ signature :
        Gaffer::Signals::Signal<void (Gaffer::Plug*), Gaffer::Signals::CatchingCombiner<void> > {lvalue} plugInputChangedSignal(Gaffer::Node {lvalue})'''
    ...
    def plugSetSignal (self, *args, **kwargs):
      '''
plugSetSignal( (Node)arg1) -> UnaryPlugSignal :

    C++ signature :
        Gaffer::Signals::Signal<void (Gaffer::Plug*), Gaffer::Signals::CatchingCombiner<void> > {lvalue} plugSetSignal(Gaffer::Node {lvalue})'''
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
    def relativeName (self, *args, **kwargs):
      '''
relativeName( (GraphComponent)arg1, (GraphComponent)arg2) -> str :

    C++ signature :
        std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > relativeName(Gaffer::GraphComponent {lvalue},Gaffer::GraphComponent const*)'''
    ...
    def removeChild (self, *args, **kwargs):
      '''
removeChild( (GraphComponent)arg1, (GraphComponent)arg2) -> None :

    C++ signature :
        void removeChild(Gaffer::GraphComponent {lvalue},Gaffer::GraphComponent {lvalue})'''
    ...
    def reorderChildren (self, *args, **kwargs):
      '''
reorderChildren( (GraphComponent)arg1, (object)arg2) -> None :

    C++ signature :
        void reorderChildren(Gaffer::GraphComponent {lvalue},boost::python::api::object)'''
    ...
    def scriptNode (self, *args, **kwargs):
      '''
scriptNode( (Node)arg1) -> object :

    C++ signature :
        Gaffer::ScriptNode* scriptNode(Gaffer::Node {lvalue})'''
    ...
    def setChild (self, *args, **kwargs):
      '''
setChild( (GraphComponent)arg1, (InternedString)arg2, (GraphComponent)arg3) -> None :

    C++ signature :
        void setChild(Gaffer::GraphComponent {lvalue},IECore::InternedString,Gaffer::GraphComponent {lvalue})'''
    ...
    def setName (self, *args, **kwargs):
      '''
setName( (GraphComponent)arg1, (InternedString)arg2) -> str :

    C++ signature :
        char const* setName(Gaffer::GraphComponent {lvalue},IECore::InternedString)'''
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
typeId( (USDAttributes)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(GafferUSD::USDAttributes {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (USDAttributes)arg1) -> str :

    C++ signature :
        char const* typeName(GafferUSD::USDAttributes {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...
    def values (self, *args, **kwargs):
      '''
values( (GraphComponent)arg1) -> list :

    C++ signature :
        boost::python::list values(Gaffer::GraphComponent {lvalue})'''
    ...

def USDLayerWriter (*args):
      '''
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > name='USDLayerWriter')

'''      
    ...

class USDLayerWriter:
    def BinaryPlugSignal (self, *args, **kwargs):
      '''None'''
    ...
    def BinarySignal (self, *args, **kwargs):
      '''None'''
    ...
    def ErrorSignal (self, *args, **kwargs):
      '''None'''
    ...
    def NameChangedSignal (self, *args, **kwargs):
      '''None'''
    ...
    def Range (parent):
      '''None'''
    ...
    def RecursiveRange (parent):
      '''None'''
    ...
    def Task (self, *args, **kwargs):
      '''None'''
    ...
    def TaskPlug (self, *args, **kwargs):
      '''None'''
    ...
    def UnaryPlugSignal (self, *args, **kwargs):
      '''None'''
    ...
    def UnarySignal (self, *args, **kwargs):
      '''None'''
    ...
    def acceptsChild (self, *args, **kwargs):
      '''
acceptsChild( (USDLayerWriter)arg1, (GraphComponent)arg2) -> bool :

    C++ signature :
        bool acceptsChild(GafferUSD::USDLayerWriter,Gaffer::GraphComponent const*)'''
    ...
    def acceptsParent (self, *args, **kwargs):
      '''
acceptsParent( (USDLayerWriter)arg1, (GraphComponent)arg2) -> bool :

    C++ signature :
        bool acceptsParent(GafferUSD::USDLayerWriter,Gaffer::GraphComponent const*)'''
    ...
    def addChild (self, *args, **kwargs):
      '''
addChild( (GraphComponent)arg1, (GraphComponent)arg2) -> None :

    C++ signature :
        void addChild(Gaffer::GraphComponent {lvalue},Gaffer::GraphComponent {lvalue})'''
    ...
    def affects (self, *args, **kwargs):
      '''
affects( (USDLayerWriter)arg1, (Plug)arg2) -> list :

    C++ signature :
        boost::python::list affects(GafferUSD::USDLayerWriter,Gaffer::Plug const*)'''
    ...
    def affectsTask (self, *args, **kwargs):
      '''
affectsTask( (USDLayerWriter)arg1, (Plug)arg2) -> bool :

    C++ signature :
        bool affectsTask(GafferUSD::USDLayerWriter {lvalue},Gaffer::Plug const*)'''
    ...
    def ancestor (self, *args, **kwargs):
      '''
ancestor( (GraphComponent)arg1, (TypeId)arg2) -> object :

    C++ signature :
        boost::intrusive_ptr<Gaffer::GraphComponent> ancestor(Gaffer::GraphComponent {lvalue},IECore::TypeId)'''
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
    def childAddedSignal (self, *args, **kwargs):
      '''
childAddedSignal( (GraphComponent)arg1) -> BinarySignal :

    C++ signature :
        Gaffer::Signals::Signal<void (Gaffer::GraphComponent*, Gaffer::GraphComponent*), Gaffer::Signals::CatchingCombiner<void> > {lvalue} childAddedSignal(Gaffer::GraphComponent {lvalue})'''
    ...
    def childRemovedSignal (self, *args, **kwargs):
      '''
childRemovedSignal( (GraphComponent)arg1) -> BinarySignal :

    C++ signature :
        Gaffer::Signals::Signal<void (Gaffer::GraphComponent*, Gaffer::GraphComponent*), Gaffer::Signals::CatchingCombiner<void> > {lvalue} childRemovedSignal(Gaffer::GraphComponent {lvalue})'''
    ...
    def children (self, *args, **kwargs):
      '''
children( (GraphComponent)self [, (TypeId)typeId=IECore._IECore.TypeId(110000)]) -> tuple :

    C++ signature :
        boost::python::tuple children(Gaffer::GraphComponent {lvalue} [,IECore::TypeId=IECore._IECore.TypeId(110000)])'''
    ...
    def childrenReorderedSignal (self, *args, **kwargs):
      '''
childrenReorderedSignal( (GraphComponent)arg1) -> BinarySignal :

    C++ signature :
        Gaffer::Signals::Signal<void (Gaffer::GraphComponent*, std::vector<unsigned long, std::allocator<unsigned long> > const&), Gaffer::Signals::CatchingCombiner<void> > {lvalue} childrenReorderedSignal(Gaffer::GraphComponent {lvalue})'''
    ...
    def clearChildren (self, *args, **kwargs):
      '''
clearChildren( (GraphComponent)arg1) -> None :

    C++ signature :
        void clearChildren(Gaffer::GraphComponent {lvalue})'''
    ...
    def collectGarbage (self, *args, **kwargs):
      '''
collectGarbage() -> None :

    C++ signature :
        void collectGarbage()'''
    ...
    def commonAncestor (self, *args, **kwargs):
      '''
commonAncestor( (GraphComponent)self, (GraphComponent)other [, (TypeId)ancestorType=IECore._IECore.TypeId(110000)]) -> object :

    C++ signature :
        boost::intrusive_ptr<Gaffer::GraphComponent> commonAncestor(Gaffer::GraphComponent {lvalue},Gaffer::GraphComponent const* [,IECore::TypeId=IECore._IECore.TypeId(110000)])'''
    ...
    def correspondingInput (self, *args, **kwargs):
      '''
correspondingInput( (USDLayerWriter)arg1, (Plug)arg2) -> object :

    C++ signature :
        boost::intrusive_ptr<Gaffer::Plug> correspondingInput(GafferUSD::USDLayerWriter {lvalue},Gaffer::Plug const*)'''
    ...
    def derivedTypeIds (self, *args, **kwargs):
      '''
derivedTypeIds( (TypeId)arg1) -> list :

    C++ signature :
        boost::python::list derivedTypeIds(IECore::TypeId)'''
    ...
    def descendant (self, *args, **kwargs):
      '''
descendant( (GraphComponent)arg1, (object)arg2) -> object :

    C++ signature :
        boost::intrusive_ptr<Gaffer::GraphComponent> descendant(Gaffer::GraphComponent {lvalue},std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)'''
    ...
    def enabledPlug (self, *args, **kwargs):
      '''
enabledPlug( (USDLayerWriter)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<Gaffer::TypedPlug<bool> > enabledPlug(GafferUSD::USDLayerWriter {lvalue})'''
    ...
    def errorSignal (self, *args, **kwargs):
      '''
errorSignal( (Node)arg1) -> ErrorSignal :

    C++ signature :
        Gaffer::Signals::Signal<void (Gaffer::Plug const*, Gaffer::Plug const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&), Gaffer::Signals::CatchingCombiner<void> > {lvalue} errorSignal(Gaffer::Node {lvalue})'''
    ...
    def execute (self, *args, **kwargs):
      '''
execute( (USDLayerWriter)arg1) -> None :

    C++ signature :
        void execute(GafferUSD::USDLayerWriter {lvalue})'''
    ...
    def executeSequence (self, *args, **kwargs):
      '''
executeSequence( (USDLayerWriter)arg1, (object)arg2) -> None :

    C++ signature :
        void executeSequence(GafferUSD::USDLayerWriter {lvalue},boost::python::api::object)'''
    ...
    def fullName (self, *args, **kwargs):
      '''
fullName( (GraphComponent)arg1) -> str :

    C++ signature :
        std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > fullName(Gaffer::GraphComponent {lvalue})'''
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
    def getChild (self, *args, **kwargs):
      '''
getChild( (GraphComponent)arg1, (InternedString)arg2) -> object :

    C++ signature :
        boost::intrusive_ptr<Gaffer::GraphComponent> getChild(Gaffer::GraphComponent {lvalue},IECore::InternedString)'''
    ...
    def getName (self, *args, **kwargs):
      '''
getName( (GraphComponent)arg1) -> str :

    C++ signature :
        char const* getName(Gaffer::GraphComponent {lvalue})'''
    ...
    def hash (self, *args, **kwargs):
      '''
hash( (USDLayerWriter)arg1, (Context)arg2) -> MurmurHash :

    C++ signature :
        IECore::MurmurHash hash(GafferUSD::USDLayerWriter {lvalue},Gaffer::Context const*)'''
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
    def isAncestorOf (self, *args, **kwargs):
      '''
isAncestorOf( (GraphComponent)arg1, (GraphComponent)arg2) -> bool :

    C++ signature :
        bool isAncestorOf(Gaffer::GraphComponent {lvalue},Gaffer::GraphComponent const*)'''
    ...
    def isInstanceOf (self, *args, **kwargs):
      '''
isInstanceOf( (USDLayerWriter)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(GafferUSD::USDLayerWriter {lvalue},IECore::TypeId)

isInstanceOf( (USDLayerWriter)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(GafferUSD::USDLayerWriter {lvalue},char const*)'''
    ...
    def isSame (self, *args, **kwargs):
      '''
isSame( (RefCounted)arg1, (RefCounted)arg2) -> bool :

    C++ signature :
        bool isSame(IECore::RefCounted const*,IECore::RefCounted const*)'''
    ...
    def items (self, *args, **kwargs):
      '''
items( (GraphComponent)arg1) -> list :

    C++ signature :
        boost::python::list items(Gaffer::GraphComponent {lvalue})'''
    ...
    def keys (self, *args, **kwargs):
      '''
keys( (GraphComponent)arg1) -> list :

    C++ signature :
        boost::python::list keys(Gaffer::GraphComponent {lvalue})'''
    ...
    def nameChangedSignal (self, *args, **kwargs):
      '''
nameChangedSignal( (GraphComponent)arg1) -> NameChangedSignal :

    C++ signature :
        Gaffer::Signals::Signal<void (Gaffer::GraphComponent*, IECore::InternedString), Gaffer::Signals::CatchingCombiner<void> > {lvalue} nameChangedSignal(Gaffer::GraphComponent {lvalue})'''
    ...
    def numWrappedInstances (self, *args, **kwargs):
      '''
numWrappedInstances() -> int :

    C++ signature :
        unsigned long numWrappedInstances()'''
    ...
    def parent (self, *args, **kwargs):
      '''
parent( (GraphComponent)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<Gaffer::GraphComponent> parent(Gaffer::GraphComponent {lvalue})'''
    ...
    def parentChangedSignal (self, *args, **kwargs):
      '''
parentChangedSignal( (GraphComponent)arg1) -> BinarySignal :

    C++ signature :
        Gaffer::Signals::Signal<void (Gaffer::GraphComponent*, Gaffer::GraphComponent*), Gaffer::Signals::CatchingCombiner<void> > {lvalue} parentChangedSignal(Gaffer::GraphComponent {lvalue})'''
    ...
    def plugDirtiedSignal (self, *args, **kwargs):
      '''
plugDirtiedSignal( (Node)arg1) -> UnaryPlugSignal :

    C++ signature :
        Gaffer::Signals::Signal<void (Gaffer::Plug*), Gaffer::Signals::CatchingCombiner<void> > {lvalue} plugDirtiedSignal(Gaffer::Node {lvalue})'''
    ...
    def plugInputChangedSignal (self, *args, **kwargs):
      '''
plugInputChangedSignal( (Node)arg1) -> UnaryPlugSignal :

    C++ signature :
        Gaffer::Signals::Signal<void (Gaffer::Plug*), Gaffer::Signals::CatchingCombiner<void> > {lvalue} plugInputChangedSignal(Gaffer::Node {lvalue})'''
    ...
    def plugSetSignal (self, *args, **kwargs):
      '''
plugSetSignal( (Node)arg1) -> UnaryPlugSignal :

    C++ signature :
        Gaffer::Signals::Signal<void (Gaffer::Plug*), Gaffer::Signals::CatchingCombiner<void> > {lvalue} plugSetSignal(Gaffer::Node {lvalue})'''
    ...
    def postTasks (self, *args, **kwargs):
      '''
postTasks( (USDLayerWriter)arg1, (Context)arg2) -> list :

    C++ signature :
        boost::python::list postTasks(GafferUSD::USDLayerWriter {lvalue},Gaffer::Context*)'''
    ...
    def preTasks (self, *args, **kwargs):
      '''
preTasks( (USDLayerWriter)arg1, (Context)arg2) -> list :

    C++ signature :
        boost::python::list preTasks(GafferUSD::USDLayerWriter {lvalue},Gaffer::Context*)'''
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
    def relativeName (self, *args, **kwargs):
      '''
relativeName( (GraphComponent)arg1, (GraphComponent)arg2) -> str :

    C++ signature :
        std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > relativeName(Gaffer::GraphComponent {lvalue},Gaffer::GraphComponent const*)'''
    ...
    def removeChild (self, *args, **kwargs):
      '''
removeChild( (GraphComponent)arg1, (GraphComponent)arg2) -> None :

    C++ signature :
        void removeChild(Gaffer::GraphComponent {lvalue},Gaffer::GraphComponent {lvalue})'''
    ...
    def reorderChildren (self, *args, **kwargs):
      '''
reorderChildren( (GraphComponent)arg1, (object)arg2) -> None :

    C++ signature :
        void reorderChildren(Gaffer::GraphComponent {lvalue},boost::python::api::object)'''
    ...
    def requiresSequenceExecution (self, *args, **kwargs):
      '''
requiresSequenceExecution( (USDLayerWriter)arg1) -> bool :

    C++ signature :
        bool requiresSequenceExecution(GafferUSD::USDLayerWriter {lvalue})'''
    ...
    def scriptNode (self, *args, **kwargs):
      '''
scriptNode( (Node)arg1) -> object :

    C++ signature :
        Gaffer::ScriptNode* scriptNode(Gaffer::Node {lvalue})'''
    ...
    def setChild (self, *args, **kwargs):
      '''
setChild( (GraphComponent)arg1, (InternedString)arg2, (GraphComponent)arg3) -> None :

    C++ signature :
        void setChild(Gaffer::GraphComponent {lvalue},IECore::InternedString,Gaffer::GraphComponent {lvalue})'''
    ...
    def setName (self, *args, **kwargs):
      '''
setName( (GraphComponent)arg1, (InternedString)arg2) -> str :

    C++ signature :
        char const* setName(Gaffer::GraphComponent {lvalue},IECore::InternedString)'''
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
typeId( (USDLayerWriter)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(GafferUSD::USDLayerWriter {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (USDLayerWriter)arg1) -> str :

    C++ signature :
        char const* typeName(GafferUSD::USDLayerWriter {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...
    def values (self, *args, **kwargs):
      '''
values( (GraphComponent)arg1) -> list :

    C++ signature :
        boost::python::list values(Gaffer::GraphComponent {lvalue})'''
    ...

def USDLight (*args):
      '''
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > name='USDLight')

'''      
    ...

class USDLight:
    def BinaryPlugSignal (self, *args, **kwargs):
      '''None'''
    ...
    def BinarySignal (self, *args, **kwargs):
      '''None'''
    ...
    def ErrorSignal (self, *args, **kwargs):
      '''None'''
    ...
    def NameChangedSignal (self, *args, **kwargs):
      '''None'''
    ...
    def Range (parent):
      '''None'''
    ...
    def RecursiveRange (parent):
      '''None'''
    ...
    def UnaryPlugSignal (self, *args, **kwargs):
      '''None'''
    ...
    def UnarySignal (self, *args, **kwargs):
      '''None'''
    ...
    def acceptsChild (self, *args, **kwargs):
      '''
acceptsChild( (USDLight)arg1, (GraphComponent)arg2) -> bool :

    C++ signature :
        bool acceptsChild(GafferUSD::USDLight,Gaffer::GraphComponent const*)'''
    ...
    def acceptsParent (self, *args, **kwargs):
      '''
acceptsParent( (USDLight)arg1, (GraphComponent)arg2) -> bool :

    C++ signature :
        bool acceptsParent(GafferUSD::USDLight,Gaffer::GraphComponent const*)'''
    ...
    def addChild (self, *args, **kwargs):
      '''
addChild( (GraphComponent)arg1, (GraphComponent)arg2) -> None :

    C++ signature :
        void addChild(Gaffer::GraphComponent {lvalue},Gaffer::GraphComponent {lvalue})'''
    ...
    def affects (self, *args, **kwargs):
      '''
affects( (USDLight)arg1, (Plug)arg2) -> list :

    C++ signature :
        boost::python::list affects(GafferUSD::USDLight,Gaffer::Plug const*)'''
    ...
    def ancestor (self, *args, **kwargs):
      '''
ancestor( (GraphComponent)arg1, (TypeId)arg2) -> object :

    C++ signature :
        boost::intrusive_ptr<Gaffer::GraphComponent> ancestor(Gaffer::GraphComponent {lvalue},IECore::TypeId)'''
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
    def childAddedSignal (self, *args, **kwargs):
      '''
childAddedSignal( (GraphComponent)arg1) -> BinarySignal :

    C++ signature :
        Gaffer::Signals::Signal<void (Gaffer::GraphComponent*, Gaffer::GraphComponent*), Gaffer::Signals::CatchingCombiner<void> > {lvalue} childAddedSignal(Gaffer::GraphComponent {lvalue})'''
    ...
    def childRemovedSignal (self, *args, **kwargs):
      '''
childRemovedSignal( (GraphComponent)arg1) -> BinarySignal :

    C++ signature :
        Gaffer::Signals::Signal<void (Gaffer::GraphComponent*, Gaffer::GraphComponent*), Gaffer::Signals::CatchingCombiner<void> > {lvalue} childRemovedSignal(Gaffer::GraphComponent {lvalue})'''
    ...
    def children (self, *args, **kwargs):
      '''
children( (GraphComponent)self [, (TypeId)typeId=IECore._IECore.TypeId(110000)]) -> tuple :

    C++ signature :
        boost::python::tuple children(Gaffer::GraphComponent {lvalue} [,IECore::TypeId=IECore._IECore.TypeId(110000)])'''
    ...
    def childrenReorderedSignal (self, *args, **kwargs):
      '''
childrenReorderedSignal( (GraphComponent)arg1) -> BinarySignal :

    C++ signature :
        Gaffer::Signals::Signal<void (Gaffer::GraphComponent*, std::vector<unsigned long, std::allocator<unsigned long> > const&), Gaffer::Signals::CatchingCombiner<void> > {lvalue} childrenReorderedSignal(Gaffer::GraphComponent {lvalue})'''
    ...
    def clearChildren (self, *args, **kwargs):
      '''
clearChildren( (GraphComponent)arg1) -> None :

    C++ signature :
        void clearChildren(Gaffer::GraphComponent {lvalue})'''
    ...
    def collectGarbage (self, *args, **kwargs):
      '''
collectGarbage() -> None :

    C++ signature :
        void collectGarbage()'''
    ...
    def commonAncestor (self, *args, **kwargs):
      '''
commonAncestor( (GraphComponent)self, (GraphComponent)other [, (TypeId)ancestorType=IECore._IECore.TypeId(110000)]) -> object :

    C++ signature :
        boost::intrusive_ptr<Gaffer::GraphComponent> commonAncestor(Gaffer::GraphComponent {lvalue},Gaffer::GraphComponent const* [,IECore::TypeId=IECore._IECore.TypeId(110000)])'''
    ...
    def correspondingInput (self, *args, **kwargs):
      '''
correspondingInput( (USDLight)arg1, (Plug)arg2) -> object :

    C++ signature :
        boost::intrusive_ptr<Gaffer::Plug> correspondingInput(GafferUSD::USDLight {lvalue},Gaffer::Plug const*)'''
    ...
    def derivedTypeIds (self, *args, **kwargs):
      '''
derivedTypeIds( (TypeId)arg1) -> list :

    C++ signature :
        boost::python::list derivedTypeIds(IECore::TypeId)'''
    ...
    def descendant (self, *args, **kwargs):
      '''
descendant( (GraphComponent)arg1, (object)arg2) -> object :

    C++ signature :
        boost::intrusive_ptr<Gaffer::GraphComponent> descendant(Gaffer::GraphComponent {lvalue},std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)'''
    ...
    def enabledPlug (self, *args, **kwargs):
      '''
enabledPlug( (USDLight)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<Gaffer::TypedPlug<bool> > enabledPlug(GafferUSD::USDLight {lvalue})'''
    ...
    def errorSignal (self, *args, **kwargs):
      '''
errorSignal( (Node)arg1) -> ErrorSignal :

    C++ signature :
        Gaffer::Signals::Signal<void (Gaffer::Plug const*, Gaffer::Plug const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&), Gaffer::Signals::CatchingCombiner<void> > {lvalue} errorSignal(Gaffer::Node {lvalue})'''
    ...
    def fullName (self, *args, **kwargs):
      '''
fullName( (GraphComponent)arg1) -> str :

    C++ signature :
        std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > fullName(Gaffer::GraphComponent {lvalue})'''
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
    def getChild (self, *args, **kwargs):
      '''
getChild( (GraphComponent)arg1, (InternedString)arg2) -> object :

    C++ signature :
        boost::intrusive_ptr<Gaffer::GraphComponent> getChild(Gaffer::GraphComponent {lvalue},IECore::InternedString)'''
    ...
    def getName (self, *args, **kwargs):
      '''
getName( (GraphComponent)arg1) -> str :

    C++ signature :
        char const* getName(Gaffer::GraphComponent {lvalue})'''
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
    def isAncestorOf (self, *args, **kwargs):
      '''
isAncestorOf( (GraphComponent)arg1, (GraphComponent)arg2) -> bool :

    C++ signature :
        bool isAncestorOf(Gaffer::GraphComponent {lvalue},Gaffer::GraphComponent const*)'''
    ...
    def isInstanceOf (self, *args, **kwargs):
      '''
isInstanceOf( (USDLight)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(GafferUSD::USDLight {lvalue},IECore::TypeId)

isInstanceOf( (USDLight)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(GafferUSD::USDLight {lvalue},char const*)'''
    ...
    def isSame (self, *args, **kwargs):
      '''
isSame( (RefCounted)arg1, (RefCounted)arg2) -> bool :

    C++ signature :
        bool isSame(IECore::RefCounted const*,IECore::RefCounted const*)'''
    ...
    def items (self, *args, **kwargs):
      '''
items( (GraphComponent)arg1) -> list :

    C++ signature :
        boost::python::list items(Gaffer::GraphComponent {lvalue})'''
    ...
    def keys (self, *args, **kwargs):
      '''
keys( (GraphComponent)arg1) -> list :

    C++ signature :
        boost::python::list keys(Gaffer::GraphComponent {lvalue})'''
    ...
    def loadShader (self, *args, **kwargs):
      '''
loadShader( (USDLight)arg1, (object)shader [, (bool)keepExistingValues=True]) -> None :

    C++ signature :
        void loadShader(GafferUSD::USDLight {lvalue},std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > [,bool=True])'''
    ...
    def nameChangedSignal (self, *args, **kwargs):
      '''
nameChangedSignal( (GraphComponent)arg1) -> NameChangedSignal :

    C++ signature :
        Gaffer::Signals::Signal<void (Gaffer::GraphComponent*, IECore::InternedString), Gaffer::Signals::CatchingCombiner<void> > {lvalue} nameChangedSignal(Gaffer::GraphComponent {lvalue})'''
    ...
    def numWrappedInstances (self, *args, **kwargs):
      '''
numWrappedInstances() -> int :

    C++ signature :
        unsigned long numWrappedInstances()'''
    ...
    def parent (self, *args, **kwargs):
      '''
parent( (GraphComponent)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<Gaffer::GraphComponent> parent(Gaffer::GraphComponent {lvalue})'''
    ...
    def parentChangedSignal (self, *args, **kwargs):
      '''
parentChangedSignal( (GraphComponent)arg1) -> BinarySignal :

    C++ signature :
        Gaffer::Signals::Signal<void (Gaffer::GraphComponent*, Gaffer::GraphComponent*), Gaffer::Signals::CatchingCombiner<void> > {lvalue} parentChangedSignal(Gaffer::GraphComponent {lvalue})'''
    ...
    def plugDirtiedSignal (self, *args, **kwargs):
      '''
plugDirtiedSignal( (Node)arg1) -> UnaryPlugSignal :

    C++ signature :
        Gaffer::Signals::Signal<void (Gaffer::Plug*), Gaffer::Signals::CatchingCombiner<void> > {lvalue} plugDirtiedSignal(Gaffer::Node {lvalue})'''
    ...
    def plugInputChangedSignal (self, *args, **kwargs):
      '''
plugInputChangedSignal( (Node)arg1) -> UnaryPlugSignal :

    C++ signature :
        Gaffer::Signals::Signal<void (Gaffer::Plug*), Gaffer::Signals::CatchingCombiner<void> > {lvalue} plugInputChangedSignal(Gaffer::Node {lvalue})'''
    ...
    def plugSetSignal (self, *args, **kwargs):
      '''
plugSetSignal( (Node)arg1) -> UnaryPlugSignal :

    C++ signature :
        Gaffer::Signals::Signal<void (Gaffer::Plug*), Gaffer::Signals::CatchingCombiner<void> > {lvalue} plugSetSignal(Gaffer::Node {lvalue})'''
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
    def relativeName (self, *args, **kwargs):
      '''
relativeName( (GraphComponent)arg1, (GraphComponent)arg2) -> str :

    C++ signature :
        std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > relativeName(Gaffer::GraphComponent {lvalue},Gaffer::GraphComponent const*)'''
    ...
    def removeChild (self, *args, **kwargs):
      '''
removeChild( (GraphComponent)arg1, (GraphComponent)arg2) -> None :

    C++ signature :
        void removeChild(Gaffer::GraphComponent {lvalue},Gaffer::GraphComponent {lvalue})'''
    ...
    def reorderChildren (self, *args, **kwargs):
      '''
reorderChildren( (GraphComponent)arg1, (object)arg2) -> None :

    C++ signature :
        void reorderChildren(Gaffer::GraphComponent {lvalue},boost::python::api::object)'''
    ...
    def scriptNode (self, *args, **kwargs):
      '''
scriptNode( (Node)arg1) -> object :

    C++ signature :
        Gaffer::ScriptNode* scriptNode(Gaffer::Node {lvalue})'''
    ...
    def setChild (self, *args, **kwargs):
      '''
setChild( (GraphComponent)arg1, (InternedString)arg2, (GraphComponent)arg3) -> None :

    C++ signature :
        void setChild(Gaffer::GraphComponent {lvalue},IECore::InternedString,Gaffer::GraphComponent {lvalue})'''
    ...
    def setName (self, *args, **kwargs):
      '''
setName( (GraphComponent)arg1, (InternedString)arg2) -> str :

    C++ signature :
        char const* setName(Gaffer::GraphComponent {lvalue},IECore::InternedString)'''
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
typeId( (USDLight)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(GafferUSD::USDLight {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (USDLight)arg1) -> str :

    C++ signature :
        char const* typeName(GafferUSD::USDLight {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...
    def values (self, *args, **kwargs):
      '''
values( (GraphComponent)arg1) -> list :

    C++ signature :
        boost::python::list values(Gaffer::GraphComponent {lvalue})'''
    ...

def USDShader (*args):
      '''
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > name='USDShader')

'''      
    ...

class USDShader:
    def BinaryPlugSignal (self, *args, **kwargs):
      '''None'''
    ...
    def BinarySignal (self, *args, **kwargs):
      '''None'''
    ...
    def ErrorSignal (self, *args, **kwargs):
      '''None'''
    ...
    def NameChangedSignal (self, *args, **kwargs):
      '''None'''
    ...
    def Range (parent):
      '''None'''
    ...
    def RecursiveRange (parent):
      '''None'''
    ...
    def UnaryPlugSignal (self, *args, **kwargs):
      '''None'''
    ...
    def UnarySignal (self, *args, **kwargs):
      '''None'''
    ...
    def acceptsChild (self, *args, **kwargs):
      '''
acceptsChild( (USDShader)arg1, (GraphComponent)arg2) -> bool :

    C++ signature :
        bool acceptsChild(GafferUSD::USDShader,Gaffer::GraphComponent const*)'''
    ...
    def acceptsParent (self, *args, **kwargs):
      '''
acceptsParent( (USDShader)arg1, (GraphComponent)arg2) -> bool :

    C++ signature :
        bool acceptsParent(GafferUSD::USDShader,Gaffer::GraphComponent const*)'''
    ...
    def addChild (self, *args, **kwargs):
      '''
addChild( (GraphComponent)arg1, (GraphComponent)arg2) -> None :

    C++ signature :
        void addChild(Gaffer::GraphComponent {lvalue},Gaffer::GraphComponent {lvalue})'''
    ...
    def affects (self, *args, **kwargs):
      '''
affects( (USDShader)arg1, (Plug)arg2) -> list :

    C++ signature :
        boost::python::list affects(GafferUSD::USDShader,Gaffer::Plug const*)'''
    ...
    def ancestor (self, *args, **kwargs):
      '''
ancestor( (GraphComponent)arg1, (TypeId)arg2) -> object :

    C++ signature :
        boost::intrusive_ptr<Gaffer::GraphComponent> ancestor(Gaffer::GraphComponent {lvalue},IECore::TypeId)'''
    ...
    def attributes (self, *args, **kwargs):
      '''
attributes( (Shader)arg1 [, (bool)_copy=True]) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::CompoundObject> attributes(GafferScene::Shader [,bool=True])'''
    ...
    def attributesHash (self, *args, **kwargs):
      '''
attributesHash( (Shader)arg1) -> MurmurHash :

    C++ signature :
        IECore::MurmurHash attributesHash(GafferScene::Shader)

attributesHash( (Shader)arg1, (MurmurHash)arg2) -> None :

    C++ signature :
        void attributesHash(GafferScene::Shader,IECore::MurmurHash {lvalue})'''
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
    def childAddedSignal (self, *args, **kwargs):
      '''
childAddedSignal( (GraphComponent)arg1) -> BinarySignal :

    C++ signature :
        Gaffer::Signals::Signal<void (Gaffer::GraphComponent*, Gaffer::GraphComponent*), Gaffer::Signals::CatchingCombiner<void> > {lvalue} childAddedSignal(Gaffer::GraphComponent {lvalue})'''
    ...
    def childRemovedSignal (self, *args, **kwargs):
      '''
childRemovedSignal( (GraphComponent)arg1) -> BinarySignal :

    C++ signature :
        Gaffer::Signals::Signal<void (Gaffer::GraphComponent*, Gaffer::GraphComponent*), Gaffer::Signals::CatchingCombiner<void> > {lvalue} childRemovedSignal(Gaffer::GraphComponent {lvalue})'''
    ...
    def children (self, *args, **kwargs):
      '''
children( (GraphComponent)self [, (TypeId)typeId=IECore._IECore.TypeId(110000)]) -> tuple :

    C++ signature :
        boost::python::tuple children(Gaffer::GraphComponent {lvalue} [,IECore::TypeId=IECore._IECore.TypeId(110000)])'''
    ...
    def childrenReorderedSignal (self, *args, **kwargs):
      '''
childrenReorderedSignal( (GraphComponent)arg1) -> BinarySignal :

    C++ signature :
        Gaffer::Signals::Signal<void (Gaffer::GraphComponent*, std::vector<unsigned long, std::allocator<unsigned long> > const&), Gaffer::Signals::CatchingCombiner<void> > {lvalue} childrenReorderedSignal(Gaffer::GraphComponent {lvalue})'''
    ...
    def clearChildren (self, *args, **kwargs):
      '''
clearChildren( (GraphComponent)arg1) -> None :

    C++ signature :
        void clearChildren(Gaffer::GraphComponent {lvalue})'''
    ...
    def collectGarbage (self, *args, **kwargs):
      '''
collectGarbage() -> None :

    C++ signature :
        void collectGarbage()'''
    ...
    def commonAncestor (self, *args, **kwargs):
      '''
commonAncestor( (GraphComponent)self, (GraphComponent)other [, (TypeId)ancestorType=IECore._IECore.TypeId(110000)]) -> object :

    C++ signature :
        boost::intrusive_ptr<Gaffer::GraphComponent> commonAncestor(Gaffer::GraphComponent {lvalue},Gaffer::GraphComponent const* [,IECore::TypeId=IECore._IECore.TypeId(110000)])'''
    ...
    def correspondingInput (self, *args, **kwargs):
      '''
correspondingInput( (USDShader)arg1, (Plug)arg2) -> object :

    C++ signature :
        boost::intrusive_ptr<Gaffer::Plug> correspondingInput(GafferUSD::USDShader {lvalue},Gaffer::Plug const*)'''
    ...
    def derivedTypeIds (self, *args, **kwargs):
      '''
derivedTypeIds( (TypeId)arg1) -> list :

    C++ signature :
        boost::python::list derivedTypeIds(IECore::TypeId)'''
    ...
    def descendant (self, *args, **kwargs):
      '''
descendant( (GraphComponent)arg1, (object)arg2) -> object :

    C++ signature :
        boost::intrusive_ptr<Gaffer::GraphComponent> descendant(Gaffer::GraphComponent {lvalue},std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)'''
    ...
    def enabledPlug (self, *args, **kwargs):
      '''
enabledPlug( (USDShader)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<Gaffer::TypedPlug<bool> > enabledPlug(GafferUSD::USDShader {lvalue})'''
    ...
    def errorSignal (self, *args, **kwargs):
      '''
errorSignal( (Node)arg1) -> ErrorSignal :

    C++ signature :
        Gaffer::Signals::Signal<void (Gaffer::Plug const*, Gaffer::Plug const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&), Gaffer::Signals::CatchingCombiner<void> > {lvalue} errorSignal(Gaffer::Node {lvalue})'''
    ...
    def fullName (self, *args, **kwargs):
      '''
fullName( (GraphComponent)arg1) -> str :

    C++ signature :
        std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > fullName(Gaffer::GraphComponent {lvalue})'''
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
    def getChild (self, *args, **kwargs):
      '''
getChild( (GraphComponent)arg1, (InternedString)arg2) -> object :

    C++ signature :
        boost::intrusive_ptr<Gaffer::GraphComponent> getChild(Gaffer::GraphComponent {lvalue},IECore::InternedString)'''
    ...
    def getName (self, *args, **kwargs):
      '''
getName( (GraphComponent)arg1) -> str :

    C++ signature :
        char const* getName(Gaffer::GraphComponent {lvalue})'''
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
    def isAncestorOf (self, *args, **kwargs):
      '''
isAncestorOf( (GraphComponent)arg1, (GraphComponent)arg2) -> bool :

    C++ signature :
        bool isAncestorOf(Gaffer::GraphComponent {lvalue},Gaffer::GraphComponent const*)'''
    ...
    def isInstanceOf (self, *args, **kwargs):
      '''
isInstanceOf( (USDShader)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(GafferUSD::USDShader {lvalue},IECore::TypeId)

isInstanceOf( (USDShader)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(GafferUSD::USDShader {lvalue},char const*)'''
    ...
    def isSame (self, *args, **kwargs):
      '''
isSame( (RefCounted)arg1, (RefCounted)arg2) -> bool :

    C++ signature :
        bool isSame(IECore::RefCounted const*,IECore::RefCounted const*)'''
    ...
    def items (self, *args, **kwargs):
      '''
items( (GraphComponent)arg1) -> list :

    C++ signature :
        boost::python::list items(Gaffer::GraphComponent {lvalue})'''
    ...
    def keys (self, *args, **kwargs):
      '''
keys( (GraphComponent)arg1) -> list :

    C++ signature :
        boost::python::list keys(Gaffer::GraphComponent {lvalue})'''
    ...
    def loadShader (self, *args, **kwargs):
      '''
loadShader( (Shader)arg1, (object)shaderName [, (bool)keepExistingValues=False]) -> None :

    C++ signature :
        void loadShader(GafferScene::Shader {lvalue},std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > [,bool=False])'''
    ...
    def nameChangedSignal (self, *args, **kwargs):
      '''
nameChangedSignal( (GraphComponent)arg1) -> NameChangedSignal :

    C++ signature :
        Gaffer::Signals::Signal<void (Gaffer::GraphComponent*, IECore::InternedString), Gaffer::Signals::CatchingCombiner<void> > {lvalue} nameChangedSignal(Gaffer::GraphComponent {lvalue})'''
    ...
    def numWrappedInstances (self, *args, **kwargs):
      '''
numWrappedInstances() -> int :

    C++ signature :
        unsigned long numWrappedInstances()'''
    ...
    def parent (self, *args, **kwargs):
      '''
parent( (GraphComponent)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<Gaffer::GraphComponent> parent(Gaffer::GraphComponent {lvalue})'''
    ...
    def parentChangedSignal (self, *args, **kwargs):
      '''
parentChangedSignal( (GraphComponent)arg1) -> BinarySignal :

    C++ signature :
        Gaffer::Signals::Signal<void (Gaffer::GraphComponent*, Gaffer::GraphComponent*), Gaffer::Signals::CatchingCombiner<void> > {lvalue} parentChangedSignal(Gaffer::GraphComponent {lvalue})'''
    ...
    def plugDirtiedSignal (self, *args, **kwargs):
      '''
plugDirtiedSignal( (Node)arg1) -> UnaryPlugSignal :

    C++ signature :
        Gaffer::Signals::Signal<void (Gaffer::Plug*), Gaffer::Signals::CatchingCombiner<void> > {lvalue} plugDirtiedSignal(Gaffer::Node {lvalue})'''
    ...
    def plugInputChangedSignal (self, *args, **kwargs):
      '''
plugInputChangedSignal( (Node)arg1) -> UnaryPlugSignal :

    C++ signature :
        Gaffer::Signals::Signal<void (Gaffer::Plug*), Gaffer::Signals::CatchingCombiner<void> > {lvalue} plugInputChangedSignal(Gaffer::Node {lvalue})'''
    ...
    def plugSetSignal (self, *args, **kwargs):
      '''
plugSetSignal( (Node)arg1) -> UnaryPlugSignal :

    C++ signature :
        Gaffer::Signals::Signal<void (Gaffer::Plug*), Gaffer::Signals::CatchingCombiner<void> > {lvalue} plugSetSignal(Gaffer::Node {lvalue})'''
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
    def relativeName (self, *args, **kwargs):
      '''
relativeName( (GraphComponent)arg1, (GraphComponent)arg2) -> str :

    C++ signature :
        std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > relativeName(Gaffer::GraphComponent {lvalue},Gaffer::GraphComponent const*)'''
    ...
    def reloadShader (self, *args, **kwargs):
      '''
reloadShader( (Shader)arg1) -> None :

    C++ signature :
        void reloadShader(GafferScene::Shader {lvalue})'''
    ...
    def removeChild (self, *args, **kwargs):
      '''
removeChild( (GraphComponent)arg1, (GraphComponent)arg2) -> None :

    C++ signature :
        void removeChild(Gaffer::GraphComponent {lvalue},Gaffer::GraphComponent {lvalue})'''
    ...
    def reorderChildren (self, *args, **kwargs):
      '''
reorderChildren( (GraphComponent)arg1, (object)arg2) -> None :

    C++ signature :
        void reorderChildren(Gaffer::GraphComponent {lvalue},boost::python::api::object)'''
    ...
    def scriptNode (self, *args, **kwargs):
      '''
scriptNode( (Node)arg1) -> object :

    C++ signature :
        Gaffer::ScriptNode* scriptNode(Gaffer::Node {lvalue})'''
    ...
    def setChild (self, *args, **kwargs):
      '''
setChild( (GraphComponent)arg1, (InternedString)arg2, (GraphComponent)arg3) -> None :

    C++ signature :
        void setChild(Gaffer::GraphComponent {lvalue},IECore::InternedString,Gaffer::GraphComponent {lvalue})'''
    ...
    def setName (self, *args, **kwargs):
      '''
setName( (GraphComponent)arg1, (InternedString)arg2) -> str :

    C++ signature :
        char const* setName(Gaffer::GraphComponent {lvalue},IECore::InternedString)'''
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
typeId( (USDShader)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(GafferUSD::USDShader {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (USDShader)arg1) -> str :

    C++ signature :
        char const* typeName(GafferUSD::USDShader {lvalue})'''
    ...
    def typeNameFromTypeId (self, *args, **kwargs):
      '''
typeNameFromTypeId( (TypeId)arg1) -> str :

    C++ signature :
        char const* typeNameFromTypeId(IECore::TypeId)'''
    ...
    def values (self, *args, **kwargs):
      '''
values( (GraphComponent)arg1) -> list :

    C++ signature :
        boost::python::list values(Gaffer::GraphComponent {lvalue})'''
    ...

def _GafferUSD (*args):
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
