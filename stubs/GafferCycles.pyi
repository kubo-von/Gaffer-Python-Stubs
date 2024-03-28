
def CyclesAttributes (*args):
      '''
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > name='CyclesAttributes')

'''      
    ...

class CyclesAttributes:
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
acceptsChild( (CyclesAttributes)arg1, (GraphComponent)arg2) -> bool :

    C++ signature :
        bool acceptsChild(GafferCycles::CyclesAttributes,Gaffer::GraphComponent const*)'''
    ...
    def acceptsParent (self, *args, **kwargs):
      '''
acceptsParent( (CyclesAttributes)arg1, (GraphComponent)arg2) -> bool :

    C++ signature :
        bool acceptsParent(GafferCycles::CyclesAttributes,Gaffer::GraphComponent const*)'''
    ...
    def addChild (self, *args, **kwargs):
      '''
addChild( (GraphComponent)arg1, (GraphComponent)arg2) -> None :

    C++ signature :
        void addChild(Gaffer::GraphComponent {lvalue},Gaffer::GraphComponent {lvalue})'''
    ...
    def affects (self, *args, **kwargs):
      '''
affects( (CyclesAttributes)arg1, (Plug)arg2) -> list :

    C++ signature :
        boost::python::list affects(GafferCycles::CyclesAttributes,Gaffer::Plug const*)'''
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
correspondingInput( (CyclesAttributes)arg1, (Plug)arg2) -> object :

    C++ signature :
        boost::intrusive_ptr<Gaffer::Plug> correspondingInput(GafferCycles::CyclesAttributes {lvalue},Gaffer::Plug const*)'''
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
enabledPlug( (CyclesAttributes)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<Gaffer::TypedPlug<bool> > enabledPlug(GafferCycles::CyclesAttributes {lvalue})'''
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
isInstanceOf( (CyclesAttributes)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(GafferCycles::CyclesAttributes {lvalue},IECore::TypeId)

isInstanceOf( (CyclesAttributes)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(GafferCycles::CyclesAttributes {lvalue},char const*)'''
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
typeId( (CyclesAttributes)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(GafferCycles::CyclesAttributes {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (CyclesAttributes)arg1) -> str :

    C++ signature :
        char const* typeName(GafferCycles::CyclesAttributes {lvalue})'''
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

def CyclesBackground (*args):
      '''
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > name='CyclesBackground')

'''      
    ...

class CyclesBackground:
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
acceptsChild( (CyclesBackground)arg1, (GraphComponent)arg2) -> bool :

    C++ signature :
        bool acceptsChild(GafferCycles::CyclesBackground,Gaffer::GraphComponent const*)'''
    ...
    def acceptsParent (self, *args, **kwargs):
      '''
acceptsParent( (CyclesBackground)arg1, (GraphComponent)arg2) -> bool :

    C++ signature :
        bool acceptsParent(GafferCycles::CyclesBackground,Gaffer::GraphComponent const*)'''
    ...
    def addChild (self, *args, **kwargs):
      '''
addChild( (GraphComponent)arg1, (GraphComponent)arg2) -> None :

    C++ signature :
        void addChild(Gaffer::GraphComponent {lvalue},Gaffer::GraphComponent {lvalue})'''
    ...
    def affects (self, *args, **kwargs):
      '''
affects( (CyclesBackground)arg1, (Plug)arg2) -> list :

    C++ signature :
        boost::python::list affects(GafferCycles::CyclesBackground,Gaffer::Plug const*)'''
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
correspondingInput( (CyclesBackground)arg1, (Plug)arg2) -> object :

    C++ signature :
        boost::intrusive_ptr<Gaffer::Plug> correspondingInput(GafferCycles::CyclesBackground {lvalue},Gaffer::Plug const*)'''
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
enabledPlug( (CyclesBackground)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<Gaffer::TypedPlug<bool> > enabledPlug(GafferCycles::CyclesBackground {lvalue})'''
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
isInstanceOf( (CyclesBackground)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(GafferCycles::CyclesBackground {lvalue},IECore::TypeId)

isInstanceOf( (CyclesBackground)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(GafferCycles::CyclesBackground {lvalue},char const*)'''
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
typeId( (CyclesBackground)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(GafferCycles::CyclesBackground {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (CyclesBackground)arg1) -> str :

    C++ signature :
        char const* typeName(GafferCycles::CyclesBackground {lvalue})'''
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

def CyclesLight (*args):
      '''
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > name='CyclesLight')

'''      
    ...

class CyclesLight:
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
acceptsChild( (CyclesLight)arg1, (GraphComponent)arg2) -> bool :

    C++ signature :
        bool acceptsChild(GafferCycles::CyclesLight,Gaffer::GraphComponent const*)'''
    ...
    def acceptsParent (self, *args, **kwargs):
      '''
acceptsParent( (CyclesLight)arg1, (GraphComponent)arg2) -> bool :

    C++ signature :
        bool acceptsParent(GafferCycles::CyclesLight,Gaffer::GraphComponent const*)'''
    ...
    def addChild (self, *args, **kwargs):
      '''
addChild( (GraphComponent)arg1, (GraphComponent)arg2) -> None :

    C++ signature :
        void addChild(Gaffer::GraphComponent {lvalue},Gaffer::GraphComponent {lvalue})'''
    ...
    def affects (self, *args, **kwargs):
      '''
affects( (CyclesLight)arg1, (Plug)arg2) -> list :

    C++ signature :
        boost::python::list affects(GafferCycles::CyclesLight,Gaffer::Plug const*)'''
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
correspondingInput( (CyclesLight)arg1, (Plug)arg2) -> object :

    C++ signature :
        boost::intrusive_ptr<Gaffer::Plug> correspondingInput(GafferCycles::CyclesLight {lvalue},Gaffer::Plug const*)'''
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
enabledPlug( (CyclesLight)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<Gaffer::TypedPlug<bool> > enabledPlug(GafferCycles::CyclesLight {lvalue})'''
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
isInstanceOf( (CyclesLight)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(GafferCycles::CyclesLight {lvalue},IECore::TypeId)

isInstanceOf( (CyclesLight)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(GafferCycles::CyclesLight {lvalue},char const*)'''
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
loadShader( (CyclesLight)arg1, (object)arg2) -> None :

    C++ signature :
        void loadShader(GafferCycles::CyclesLight {lvalue},std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)'''
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
typeId( (CyclesLight)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(GafferCycles::CyclesLight {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (CyclesLight)arg1) -> str :

    C++ signature :
        char const* typeName(GafferCycles::CyclesLight {lvalue})'''
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

def CyclesMeshLight (*args):
      '''
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > name='CyclesMeshLight')

'''      
    ...

class CyclesMeshLight:
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
acceptsChild( (CyclesMeshLight)arg1, (GraphComponent)arg2) -> bool :

    C++ signature :
        bool acceptsChild(GafferCycles::CyclesMeshLight,Gaffer::GraphComponent const*)'''
    ...
    def acceptsParent (self, *args, **kwargs):
      '''
acceptsParent( (CyclesMeshLight)arg1, (GraphComponent)arg2) -> bool :

    C++ signature :
        bool acceptsParent(GafferCycles::CyclesMeshLight,Gaffer::GraphComponent const*)'''
    ...
    def addChild (self, *args, **kwargs):
      '''
addChild( (GraphComponent)arg1, (GraphComponent)arg2) -> None :

    C++ signature :
        void addChild(Gaffer::GraphComponent {lvalue},Gaffer::GraphComponent {lvalue})'''
    ...
    def affects (self, *args, **kwargs):
      '''
affects( (CyclesMeshLight)arg1, (Plug)arg2) -> list :

    C++ signature :
        boost::python::list affects(GafferCycles::CyclesMeshLight,Gaffer::Plug const*)'''
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
correspondingInput( (CyclesMeshLight)arg1, (Plug)arg2) -> object :

    C++ signature :
        boost::intrusive_ptr<Gaffer::Plug> correspondingInput(GafferCycles::CyclesMeshLight {lvalue},Gaffer::Plug const*)'''
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
enabledPlug( (CyclesMeshLight)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<Gaffer::TypedPlug<bool> > enabledPlug(GafferCycles::CyclesMeshLight {lvalue})'''
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
isInstanceOf( (CyclesMeshLight)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(GafferCycles::CyclesMeshLight {lvalue},IECore::TypeId)

isInstanceOf( (CyclesMeshLight)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(GafferCycles::CyclesMeshLight {lvalue},char const*)'''
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
typeId( (CyclesMeshLight)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(GafferCycles::CyclesMeshLight {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (CyclesMeshLight)arg1) -> str :

    C++ signature :
        char const* typeName(GafferCycles::CyclesMeshLight {lvalue})'''
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

def CyclesOptions (*args):
      '''
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > name='CyclesOptions')

'''      
    ...

class CyclesOptions:
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
acceptsChild( (CyclesOptions)arg1, (GraphComponent)arg2) -> bool :

    C++ signature :
        bool acceptsChild(GafferCycles::CyclesOptions,Gaffer::GraphComponent const*)'''
    ...
    def acceptsParent (self, *args, **kwargs):
      '''
acceptsParent( (CyclesOptions)arg1, (GraphComponent)arg2) -> bool :

    C++ signature :
        bool acceptsParent(GafferCycles::CyclesOptions,Gaffer::GraphComponent const*)'''
    ...
    def addChild (self, *args, **kwargs):
      '''
addChild( (GraphComponent)arg1, (GraphComponent)arg2) -> None :

    C++ signature :
        void addChild(Gaffer::GraphComponent {lvalue},Gaffer::GraphComponent {lvalue})'''
    ...
    def affects (self, *args, **kwargs):
      '''
affects( (CyclesOptions)arg1, (Plug)arg2) -> list :

    C++ signature :
        boost::python::list affects(GafferCycles::CyclesOptions,Gaffer::Plug const*)'''
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
correspondingInput( (CyclesOptions)arg1, (Plug)arg2) -> object :

    C++ signature :
        boost::intrusive_ptr<Gaffer::Plug> correspondingInput(GafferCycles::CyclesOptions {lvalue},Gaffer::Plug const*)'''
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
enabledPlug( (CyclesOptions)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<Gaffer::TypedPlug<bool> > enabledPlug(GafferCycles::CyclesOptions {lvalue})'''
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
isInstanceOf( (CyclesOptions)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(GafferCycles::CyclesOptions {lvalue},IECore::TypeId)

isInstanceOf( (CyclesOptions)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(GafferCycles::CyclesOptions {lvalue},char const*)'''
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
typeId( (CyclesOptions)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(GafferCycles::CyclesOptions {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (CyclesOptions)arg1) -> str :

    C++ signature :
        char const* typeName(GafferCycles::CyclesOptions {lvalue})'''
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

def CyclesRender (*args):
      '''
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > name='CyclesRender')

'''      
    ...

class CyclesRender:
    def BinaryPlugSignal (self, *args, **kwargs):
      '''None'''
    ...
    def BinarySignal (self, *args, **kwargs):
      '''None'''
    ...
    def ErrorSignal (self, *args, **kwargs):
      '''None'''
    ...
    def Mode (self, *args, **kwargs):
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
acceptsChild( (CyclesRender)arg1, (GraphComponent)arg2) -> bool :

    C++ signature :
        bool acceptsChild(GafferCycles::CyclesRender,Gaffer::GraphComponent const*)'''
    ...
    def acceptsParent (self, *args, **kwargs):
      '''
acceptsParent( (CyclesRender)arg1, (GraphComponent)arg2) -> bool :

    C++ signature :
        bool acceptsParent(GafferCycles::CyclesRender,Gaffer::GraphComponent const*)'''
    ...
    def addChild (self, *args, **kwargs):
      '''
addChild( (GraphComponent)arg1, (GraphComponent)arg2) -> None :

    C++ signature :
        void addChild(Gaffer::GraphComponent {lvalue},Gaffer::GraphComponent {lvalue})'''
    ...
    def affects (self, *args, **kwargs):
      '''
affects( (CyclesRender)arg1, (Plug)arg2) -> list :

    C++ signature :
        boost::python::list affects(GafferCycles::CyclesRender,Gaffer::Plug const*)'''
    ...
    def affectsTask (self, *args, **kwargs):
      '''
affectsTask( (CyclesRender)arg1, (Plug)arg2) -> bool :

    C++ signature :
        bool affectsTask(GafferCycles::CyclesRender {lvalue},Gaffer::Plug const*)'''
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
correspondingInput( (CyclesRender)arg1, (Plug)arg2) -> object :

    C++ signature :
        boost::intrusive_ptr<Gaffer::Plug> correspondingInput(GafferCycles::CyclesRender {lvalue},Gaffer::Plug const*)'''
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
enabledPlug( (CyclesRender)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<Gaffer::TypedPlug<bool> > enabledPlug(GafferCycles::CyclesRender {lvalue})'''
    ...
    def errorSignal (self, *args, **kwargs):
      '''
errorSignal( (Node)arg1) -> ErrorSignal :

    C++ signature :
        Gaffer::Signals::Signal<void (Gaffer::Plug const*, Gaffer::Plug const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&), Gaffer::Signals::CatchingCombiner<void> > {lvalue} errorSignal(Gaffer::Node {lvalue})'''
    ...
    def execute (self, *args, **kwargs):
      '''
execute( (CyclesRender)arg1) -> None :

    C++ signature :
        void execute(GafferCycles::CyclesRender {lvalue})'''
    ...
    def executeSequence (self, *args, **kwargs):
      '''
executeSequence( (CyclesRender)arg1, (object)arg2) -> None :

    C++ signature :
        void executeSequence(GafferCycles::CyclesRender {lvalue},boost::python::api::object)'''
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
hash( (CyclesRender)arg1, (Context)arg2) -> MurmurHash :

    C++ signature :
        IECore::MurmurHash hash(GafferCycles::CyclesRender {lvalue},Gaffer::Context const*)'''
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
isInstanceOf( (CyclesRender)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(GafferCycles::CyclesRender {lvalue},IECore::TypeId)

isInstanceOf( (CyclesRender)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(GafferCycles::CyclesRender {lvalue},char const*)'''
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
postTasks( (CyclesRender)arg1, (Context)arg2) -> list :

    C++ signature :
        boost::python::list postTasks(GafferCycles::CyclesRender {lvalue},Gaffer::Context*)'''
    ...
    def preTasks (self, *args, **kwargs):
      '''
preTasks( (CyclesRender)arg1, (Context)arg2) -> list :

    C++ signature :
        boost::python::list preTasks(GafferCycles::CyclesRender {lvalue},Gaffer::Context*)'''
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
requiresSequenceExecution( (CyclesRender)arg1) -> bool :

    C++ signature :
        bool requiresSequenceExecution(GafferCycles::CyclesRender {lvalue})'''
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
typeId( (CyclesRender)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(GafferCycles::CyclesRender {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (CyclesRender)arg1) -> str :

    C++ signature :
        char const* typeName(GafferCycles::CyclesRender {lvalue})'''
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

def CyclesShader (*args):
      '''
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > name='CyclesShader')

'''      
    ...

class CyclesShader:
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
acceptsChild( (CyclesShader)arg1, (GraphComponent)arg2) -> bool :

    C++ signature :
        bool acceptsChild(GafferCycles::CyclesShader,Gaffer::GraphComponent const*)'''
    ...
    def acceptsParent (self, *args, **kwargs):
      '''
acceptsParent( (CyclesShader)arg1, (GraphComponent)arg2) -> bool :

    C++ signature :
        bool acceptsParent(GafferCycles::CyclesShader,Gaffer::GraphComponent const*)'''
    ...
    def addChild (self, *args, **kwargs):
      '''
addChild( (GraphComponent)arg1, (GraphComponent)arg2) -> None :

    C++ signature :
        void addChild(Gaffer::GraphComponent {lvalue},Gaffer::GraphComponent {lvalue})'''
    ...
    def affects (self, *args, **kwargs):
      '''
affects( (CyclesShader)arg1, (Plug)arg2) -> list :

    C++ signature :
        boost::python::list affects(GafferCycles::CyclesShader,Gaffer::Plug const*)'''
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
correspondingInput( (CyclesShader)arg1, (Plug)arg2) -> object :

    C++ signature :
        boost::intrusive_ptr<Gaffer::Plug> correspondingInput(GafferCycles::CyclesShader {lvalue},Gaffer::Plug const*)'''
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
enabledPlug( (CyclesShader)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<Gaffer::TypedPlug<bool> > enabledPlug(GafferCycles::CyclesShader {lvalue})'''
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
isInstanceOf( (CyclesShader)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(GafferCycles::CyclesShader {lvalue},IECore::TypeId)

isInstanceOf( (CyclesShader)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(GafferCycles::CyclesShader {lvalue},char const*)'''
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
typeId( (CyclesShader)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(GafferCycles::CyclesShader {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (CyclesShader)arg1) -> str :

    C++ signature :
        char const* typeName(GafferCycles::CyclesShader {lvalue})'''
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

def CyclesShaderBall (*args):
      '''

'''      
    ...

class CyclesShaderBall:
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
    def _outPlug (self):
      '''None'''
    ...
    def acceptsChild (self, *args, **kwargs):
      '''
acceptsChild( (SceneNode)arg1, (GraphComponent)arg2) -> bool :

    C++ signature :
        bool acceptsChild(GafferScene::SceneNode,Gaffer::GraphComponent const*)'''
    ...
    def acceptsParent (self, *args, **kwargs):
      '''
acceptsParent( (SceneNode)arg1, (GraphComponent)arg2) -> bool :

    C++ signature :
        bool acceptsParent(GafferScene::SceneNode,Gaffer::GraphComponent const*)'''
    ...
    def addChild (self, *args, **kwargs):
      '''
addChild( (GraphComponent)arg1, (GraphComponent)arg2) -> None :

    C++ signature :
        void addChild(Gaffer::GraphComponent {lvalue},Gaffer::GraphComponent {lvalue})'''
    ...
    def affects (self, *args, **kwargs):
      '''
affects( (SceneNode)arg1, (Plug)arg2) -> list :

    C++ signature :
        boost::python::list affects(GafferScene::SceneNode,Gaffer::Plug const*)'''
    ...
    def ancestor (self, *args, **kwargs):
      '''
ancestor( (GraphComponent)arg1, (TypeId)arg2) -> object :

    C++ signature :
        boost::intrusive_ptr<Gaffer::GraphComponent> ancestor(Gaffer::GraphComponent {lvalue},IECore::TypeId)'''
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
correspondingInput( (SceneNode)arg1, (Plug)arg2) -> object :

    C++ signature :
        boost::intrusive_ptr<Gaffer::Plug> correspondingInput(GafferScene::SceneNode {lvalue},Gaffer::Plug const*)'''
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
enabledPlug( (SceneNode)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<Gaffer::TypedPlug<bool> > enabledPlug(GafferScene::SceneNode {lvalue})'''
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
    def inheritsFrom (t):
      '''None'''
    ...
    def isAncestorOf (self, *args, **kwargs):
      '''
isAncestorOf( (GraphComponent)arg1, (GraphComponent)arg2) -> bool :

    C++ signature :
        bool isAncestorOf(Gaffer::GraphComponent {lvalue},Gaffer::GraphComponent const*)'''
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
    def values (self, *args, **kwargs):
      '''
values( (GraphComponent)arg1) -> list :

    C++ signature :
        boost::python::list values(Gaffer::GraphComponent {lvalue})'''
    ...

def IECoreCyclesPreview (*args):
      '''

'''      
    ...

def InteractiveCyclesRender (*args):
      '''
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > name='InteractiveCyclesRender')

'''      
    ...

class InteractiveCyclesRender:
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
    def State (self, *args, **kwargs):
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
acceptsChild( (InteractiveCyclesRender)arg1, (GraphComponent)arg2) -> bool :

    C++ signature :
        bool acceptsChild(GafferCycles::InteractiveCyclesRender,Gaffer::GraphComponent const*)'''
    ...
    def acceptsParent (self, *args, **kwargs):
      '''
acceptsParent( (InteractiveCyclesRender)arg1, (GraphComponent)arg2) -> bool :

    C++ signature :
        bool acceptsParent(GafferCycles::InteractiveCyclesRender,Gaffer::GraphComponent const*)'''
    ...
    def addChild (self, *args, **kwargs):
      '''
addChild( (GraphComponent)arg1, (GraphComponent)arg2) -> None :

    C++ signature :
        void addChild(Gaffer::GraphComponent {lvalue},Gaffer::GraphComponent {lvalue})'''
    ...
    def affects (self, *args, **kwargs):
      '''
affects( (ComputeNode)arg1, (Plug)arg2) -> list :

    C++ signature :
        boost::python::list affects(Gaffer::ComputeNode,Gaffer::Plug const*)'''
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
correspondingInput( (ComputeNode)arg1, (Plug)arg2) -> object :

    C++ signature :
        boost::intrusive_ptr<Gaffer::Plug> correspondingInput(Gaffer::ComputeNode {lvalue},Gaffer::Plug const*)'''
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
enabledPlug( (ComputeNode)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<Gaffer::TypedPlug<bool> > enabledPlug(Gaffer::ComputeNode {lvalue})'''
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
    def getContext (self, *args, **kwargs):
      '''
getContext( (InteractiveRender)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<Gaffer::Context> getContext(GafferScene::InteractiveRender {lvalue})'''
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
isInstanceOf( (InteractiveCyclesRender)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(GafferCycles::InteractiveCyclesRender {lvalue},IECore::TypeId)

isInstanceOf( (InteractiveCyclesRender)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(GafferCycles::InteractiveCyclesRender {lvalue},char const*)'''
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
    def setContext (self, *args, **kwargs):
      '''
setContext( (InteractiveRender)arg1, (Context)arg2) -> None :

    C++ signature :
        void setContext(GafferScene::InteractiveRender {lvalue},Gaffer::Context {lvalue})'''
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
typeId( (InteractiveCyclesRender)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(GafferCycles::InteractiveCyclesRender {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (InteractiveCyclesRender)arg1) -> str :

    C++ signature :
        char const* typeName(GafferCycles::InteractiveCyclesRender {lvalue})'''
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

def _GafferCycles (*args):
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

def devices (*args):
      '''

'''      
    ...

def hasOpenImageDenoise (*args):
      '''

'''      
    ...

def hasOptixDenoise (*args):
      '''

'''      
    ...

def lights (*args):
      '''

'''      
    ...

def nodes (*args):
      '''

'''      
    ...

def passes (*args):
      '''

'''      
    ...

def shaders (*args):
      '''

'''      
    ...
