
def AimConstraintUI (*args):
      '''

'''      
    ...

def AttributeQueryUI (*args):
      '''

'''      
    ...

def AttributeTweaksUI (*args):
      '''

'''      
    ...

def AttributeVisualiserUI (*args):
      '''

'''      
    ...

def AttributesUI (*args):
      '''

'''      
    ...

def BoundQueryUI (*args):
      '''

'''      
    ...

def BranchCreatorUI (*args):
      '''

'''      
    ...

def CameraTool (*args):
      '''
__init__(_object*, GafferSceneUI::SceneView*)

'''      
    ...

class CameraTool:
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
acceptsChild( (CameraTool)arg1, (GraphComponent)arg2) -> bool :

    C++ signature :
        bool acceptsChild(GafferSceneUI::CameraTool,Gaffer::GraphComponent const*)'''
    ...
    def acceptsParent (self, *args, **kwargs):
      '''
acceptsParent( (CameraTool)arg1, (GraphComponent)arg2) -> bool :

    C++ signature :
        bool acceptsParent(GafferSceneUI::CameraTool,Gaffer::GraphComponent const*)'''
    ...
    def addChild (self, *args, **kwargs):
      '''
addChild( (GraphComponent)arg1, (GraphComponent)arg2) -> None :

    C++ signature :
        void addChild(Gaffer::GraphComponent {lvalue},Gaffer::GraphComponent {lvalue})'''
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
    def create (self, *args, **kwargs):
      '''
create( (object)arg1, (View)arg2) -> object :

    C++ signature :
        boost::intrusive_ptr<GafferUI::Tool> create(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >,GafferUI::View {lvalue})'''
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
isInstanceOf( (CameraTool)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(GafferSceneUI::CameraTool {lvalue},IECore::TypeId)

isInstanceOf( (CameraTool)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(GafferSceneUI::CameraTool {lvalue},char const*)'''
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
    def registerTool (self, *args, **kwargs):
      '''
registerTool( (object)arg1, (TypeId)arg2, (object)arg3) -> None :

    C++ signature :
        void registerTool(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >,IECore::TypeId,boost::python::api::object)'''
    ...
    def registerType (self, *args, **kwargs):
      '''
registerType( (TypeId)arg1, (str)arg2, (TypeId)arg3) -> None :

    C++ signature :
        void registerType(IECore::TypeId,char const*,IECore::TypeId)'''
    ...
    def registeredTools (self, *args, **kwargs):
      '''
registeredTools( (TypeId)arg1) -> list :

    C++ signature :
        boost::python::list registeredTools(IECore::TypeId)'''
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
typeId( (CameraTool)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(GafferSceneUI::CameraTool {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (CameraTool)arg1) -> str :

    C++ signature :
        char const* typeName(GafferSceneUI::CameraTool {lvalue})'''
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
    def view (self, *args, **kwargs):
      '''
view( (Tool)arg1) -> object :

    C++ signature :
        GafferUI::View* view(GafferUI::Tool {lvalue})'''
    ...

def CameraToolUI (*args):
      '''

'''      
    ...

def CameraTweaksUI (*args):
      '''

'''      
    ...

def CameraUI (*args):
      '''

'''      
    ...

def ClippingPlaneUI (*args):
      '''

'''      
    ...

def ClosestPointSamplerUI (*args):
      '''

'''      
    ...

def CollectPrimitiveVariablesUI (*args):
      '''

'''      
    ...

def CollectScenesUI (*args):
      '''

'''      
    ...

def CollectTransformsUI (*args):
      '''

'''      
    ...

def ConstraintUI (*args):
      '''

'''      
    ...

def ContextAlgo (*args):
      '''

'''      
    ...

def CoordinateSystemUI (*args):
      '''

'''      
    ...

def CopyAttributesUI (*args):
      '''

'''      
    ...

def CopyOptionsUI (*args):
      '''

'''      
    ...

def CopyPrimitiveVariablesUI (*args):
      '''

'''      
    ...

def CropWindowTool (*args):
      '''
__init__(_object*, GafferUI::View*)

'''      
    ...

class CropWindowTool:
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
acceptsChild( (CropWindowTool)arg1, (GraphComponent)arg2) -> bool :

    C++ signature :
        bool acceptsChild(GafferSceneUI::CropWindowTool,Gaffer::GraphComponent const*)'''
    ...
    def acceptsParent (self, *args, **kwargs):
      '''
acceptsParent( (CropWindowTool)arg1, (GraphComponent)arg2) -> bool :

    C++ signature :
        bool acceptsParent(GafferSceneUI::CropWindowTool,Gaffer::GraphComponent const*)'''
    ...
    def addChild (self, *args, **kwargs):
      '''
addChild( (GraphComponent)arg1, (GraphComponent)arg2) -> None :

    C++ signature :
        void addChild(Gaffer::GraphComponent {lvalue},Gaffer::GraphComponent {lvalue})'''
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
    def create (self, *args, **kwargs):
      '''
create( (object)arg1, (View)arg2) -> object :

    C++ signature :
        boost::intrusive_ptr<GafferUI::Tool> create(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >,GafferUI::View {lvalue})'''
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
enabledPlug( (CropWindowTool)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<Gaffer::TypedPlug<bool> > enabledPlug(GafferSceneUI::CropWindowTool {lvalue})'''
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
isInstanceOf( (CropWindowTool)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(GafferSceneUI::CropWindowTool {lvalue},IECore::TypeId)

isInstanceOf( (CropWindowTool)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(GafferSceneUI::CropWindowTool {lvalue},char const*)'''
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
    def plug (self, *args, **kwargs):
      '''
plug( (CropWindowTool)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<Gaffer::BoxPlug<Imath_3_1::Box<Imath_3_1::Vec2<float> > > > plug(GafferSceneUI::CropWindowTool {lvalue})'''
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
    def registerTool (self, *args, **kwargs):
      '''
registerTool( (object)arg1, (TypeId)arg2, (object)arg3) -> None :

    C++ signature :
        void registerTool(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >,IECore::TypeId,boost::python::api::object)'''
    ...
    def registerType (self, *args, **kwargs):
      '''
registerType( (TypeId)arg1, (str)arg2, (TypeId)arg3) -> None :

    C++ signature :
        void registerType(IECore::TypeId,char const*,IECore::TypeId)'''
    ...
    def registeredTools (self, *args, **kwargs):
      '''
registeredTools( (TypeId)arg1) -> list :

    C++ signature :
        boost::python::list registeredTools(IECore::TypeId)'''
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
    def status (self, *args, **kwargs):
      '''
status( (CropWindowTool)arg1) -> str :

    C++ signature :
        std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > status(GafferSceneUI::CropWindowTool {lvalue})'''
    ...
    def statusChangedSignal (self, *args, **kwargs):
      '''
statusChangedSignal( (CropWindowTool)arg1) -> StatusChangedSignal :

    C++ signature :
        Gaffer::Signals::Signal<void (GafferSceneUI::CropWindowTool&), Gaffer::Signals::DefaultCombiner<void> > {lvalue} statusChangedSignal(GafferSceneUI::CropWindowTool {lvalue})'''
    ...
    def typeId (self, *args, **kwargs):
      '''
typeId( (CropWindowTool)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(GafferSceneUI::CropWindowTool {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (CropWindowTool)arg1) -> str :

    C++ signature :
        char const* typeName(GafferSceneUI::CropWindowTool {lvalue})'''
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
    def view (self, *args, **kwargs):
      '''
view( (Tool)arg1) -> object :

    C++ signature :
        GafferUI::View* view(GafferUI::Tool {lvalue})'''
    ...

def CropWindowToolUI (*args):
      '''

'''      
    ...

def CryptomatteUI (*args):
      '''

'''      
    ...

def CubeUI (*args):
      '''

'''      
    ...

def CurveSamplerUI (*args):
      '''

'''      
    ...

def CustomAttributesUI (*args):
      '''

'''      
    ...

def CustomOptionsUI (*args):
      '''

'''      
    ...

def DeformerUI (*args):
      '''

'''      
    ...

def DeleteAttributesUI (*args):
      '''

'''      
    ...

def DeleteCurvesUI (*args):
      '''

'''      
    ...

def DeleteFacesUI (*args):
      '''

'''      
    ...

def DeleteGlobalsUI (*args):
      '''

'''      
    ...

def DeleteObjectUI (*args):
      '''

'''      
    ...

def DeleteOptionsUI (*args):
      '''

'''      
    ...

def DeleteOutputsUI (*args):
      '''

'''      
    ...

def DeletePointsUI (*args):
      '''

'''      
    ...

def DeletePrimitiveVariablesUI (*args):
      '''

'''      
    ...

def DeleteRenderPassesUI (*args):
      '''

'''      
    ...

def DeleteSetsUI (*args):
      '''

'''      
    ...

def DuplicateUI (*args):
      '''

'''      
    ...

def EditScopeUI (*args):
      '''

'''      
    ...

def EncapsulateUI (*args):
      '''

'''      
    ...

def ExistenceQueryUI (*args):
      '''

'''      
    ...

def ExternalProceduralUI (*args):
      '''

'''      
    ...

def FilterPlugValueWidget (*args):
      '''

'''      
    ...

class FilterPlugValueWidget:
    def MultiplePlugTypesError (self, *args, **kwargs):
      '''None'''
    ...
    def MultiplePlugsError (self, *args, **kwargs):
      '''None'''
    ...
    def MultipleWidgetCreatorsError (self, *args, **kwargs):
      '''None'''
    ...
    def _FilterPlugValueWidget__addFilter (self, filterType):
      '''None'''
    ...
    def _FilterPlugValueWidget__filterNode (plug):
      '''None'''
    ...
    def _FilterPlugValueWidget__filterTypes ():
      '''None'''
    ...
    def _FilterPlugValueWidget__menuDefinition (self):
      '''None'''
    ...
    def _FilterPlugValueWidget__removeFilter (self):
      '''None'''
    ...
    def _PlugValueWidget__applyPreset (self, presetName, *unused):
      '''None'''
    ...
    def _PlugValueWidget__applyReadOnly (self, readOnly):
      '''None'''
    ...
    def _PlugValueWidget__applyUserDefaults (self):
      '''None'''
    ...
    def _PlugValueWidget__auxiliaryPlugDirtied (self, plug):
      '''None'''
    ...
    def _PlugValueWidget__buttonPress (self, widget, event, buttonMask):
      '''None'''
    ...
    def _PlugValueWidget__callLegacyUpdateMethods (self):
      '''None'''
    ...
    def _PlugValueWidget__callUpdateFromValues (self):
      '''None'''
    ...
    def _PlugValueWidget__contextChanged (self, context, key):
      '''None'''
    ...
    def _PlugValueWidget__contextMenu (self, *unused):
      '''None'''
    ...
    def _PlugValueWidget__copyValue (self):
      '''None'''
    ...
    def _PlugValueWidget__creator (plug, typeMetadata):
      '''None'''
    ...
    def _PlugValueWidget__defaultContext (graphComponent):
      '''None'''
    ...
    def _PlugValueWidget__dragEnter (self, widget, event):
      '''None'''
    ...
    def _PlugValueWidget__dragLeave (self, widget, event):
      '''None'''
    ...
    def _PlugValueWidget__drop (self, widget, event):
      '''None'''
    ...
    def _PlugValueWidget__editInputs (self):
      '''None'''
    ...
    def _PlugValueWidget__fallbackContext (self, *args, **kwargs):
      '''None'''
    ...
    def _PlugValueWidget__nodeMetadataChanged (self, nodeTypeId, key, node):
      '''None'''
    ...
    def _PlugValueWidget__plugDirtied (self, plug):
      '''None'''
    ...
    def _PlugValueWidget__plugInputChanged (self, plug):
      '''None'''
    ...
    def _PlugValueWidget__plugMetadataChanged (self, plug, key, reason):
      '''None'''
    ...
    def _PlugValueWidget__plugTypesToCreators (self, *args, **kwargs):
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
    def _PlugValueWidget__popupMenuSignal (self, *args, **kwargs):
      '''None'''
    ...
    def _PlugValueWidget__presetsSubMenu (self):
      '''None'''
    ...
    def _PlugValueWidget__removeInputs (self):
      '''None'''
    ...
    def _PlugValueWidget__setPlugsInternal (self, plugs, callUpdateMethods):
      '''None'''
    ...
    def _PlugValueWidget__setValues (self, values):
      '''None'''
    ...
    def _PlugValueWidget__updateContextConnection (self):
      '''None'''
    ...
    def _PlugValueWidget__updateFromValuesInBackground (self, plugs, auxiliaryPlugs):
      '''None'''
    ...
    def _PlugValueWidget__updateFromValuesInBackgroundPlug (self, *args, **kwargs):
      '''None'''
    ...
    def _PlugValueWidget__updateFromValuesInBackgroundPostCall (self, *args, **kwargs):
      '''None'''
    ...
    def _PlugValueWidget__updateFromValuesInBackgroundPreCall (self, *args, **kwargs):
      '''None'''
    ...
    def _Widget__applyQWidgetStyleClasses (self):
      '''None'''
    ...
    def _Widget__ensureEventFilter (self):
      '''None'''
    ...
    def _Widget__ensureFocusChangedConnection ():
      '''None'''
    ...
    def _Widget__ensureMouseTracking (self):
      '''None'''
    ...
    def _Widget__focusChanged (oldWidget, newWidget):
      '''None'''
    ...
    def _Widget__focusChangedConnected (self, *args, **kwargs):
      '''bool(x) -> bool

Returns True when the argument x is true, False otherwise.
The builtins True and False are the only two instances of the class bool.
The class bool is a subclass of the class int, and cannot be subclassed.'''
    ...
    def _Widget__focusChangedSignal (self, *args, **kwargs):
      '''None'''
    ...
    def _Widget__initNesting ():
      '''None'''
    ...
    def _Widget__keyMapping (self, *args, **kwargs):
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
    def _Widget__parentStack (self, *args, **kwargs):
      '''Built-in mutable sequence.

If no argument is given, the constructor creates a new empty list.
The argument must be an iterable if specified.'''
    ...
    def _Widget__propagateDisplayTransformChange (self):
      '''None'''
    ...
    def _Widget__qtWidgetOwners (self, *args, **kwargs):
      ''' Mapping class that references keys weakly.

    Entries in the dictionary will be discarded when there is no
    longer a strong reference to the key. This can be used to
    associate additional data with an object owned by other parts of
    an application without adding attributes to those objects. This
    can be especially useful with objects that override attribute
    accesses.
    '''
    ...
    def _Widget__styleClassName ():
      '''None'''
    ...
    def _addPopupMenu (self, widget=None, buttons=GafferUI._GafferUI.Buttons.Right):
      '''None'''
    ...
    def _applyVisibility (self):
      '''None'''
    ...
    def _auxiliaryPlugs (self, plug):
      '''None'''
    ...
    def _blockedUpdateFromValues (self):
      '''None'''
    ...
    def _buttons (qtButtons):
      '''None'''
    ...
    def _convertValue (self, value):
      '''None'''
    ...
    def _disconnectTrackedConnections (self, *args, **kwargs):
      '''
_disconnectTrackedConnections( (Trackable)arg1) -> None :

    C++ signature :
        void _disconnectTrackedConnections(Gaffer::Signals::Trackable {lvalue})'''
    ...
    def _displayTransformChanged (self):
      '''None'''
    ...
    def _editable (self, canEditAnimation=False):
      '''None'''
    ...
    def _key (qtKey):
      '''None'''
    ...
    def _modifiers (qtModifiers):
      '''None'''
    ...
    def _owner (qtWidget):
      '''None'''
    ...
    def _plugConnections (self):
      '''None'''
    ...
    def _popParent ():
      '''None'''
    ...
    def _popupMenuDefinition (self):
      '''None'''
    ...
    def _postConstructor (self):
      '''None'''
    ...
    def _pushParent (container):
      '''None'''
    ...
    def _qtColor (color):
      '''None'''
    ...
    def _qtWidget (self):
      '''None'''
    ...
    def _repolish (self, qtWidget=None):
      '''None'''
    ...
    def _requestUpdateFromValues (self, lazy=True):
      '''None'''
    ...
    def _setStyleSheet (self):
      '''None'''
    ...
    def _updateFromEditable (self):
      '''None'''
    ...
    def _updateFromMetadata (self):
      '''None'''
    ...
    def _updateFromValues (self, values, exception):
      '''None'''
    ...
    def _valuesDependOnContext (self):
      '''None'''
    ...
    def _valuesForUpdate (plugs, auxiliaryPlugs):
      '''None'''
    ...
    def acquire (plug):
      '''None'''
    ...
    def ancestor (self, type):
      '''None'''
    ...
    def bound (self, relativeTo=None):
      '''None'''
    ...
    def buttonDoubleClickSignal (self):
      '''None'''
    ...
    def buttonPressSignal (self):
      '''None'''
    ...
    def buttonReleaseSignal (self):
      '''None'''
    ...
    def childPlugValueWidget (self, childPlug):
      '''None'''
    ...
    def contextMenuSignal (self):
      '''None'''
    ...
    def create (plugs, typeMetadata='plugValueWidget:type'):
      '''None'''
    ...
    def currentModifiers ():
      '''None'''
    ...
    def displayTransform (self):
      '''None'''
    ...
    def dragBeginSignal (self):
      '''None'''
    ...
    def dragEndSignal (self):
      '''None'''
    ...
    def dragEnterSignal (self):
      '''None'''
    ...
    def dragLeaveSignal (self):
      '''None'''
    ...
    def dragMoveSignal (self):
      '''None'''
    ...
    def dropSignal (self):
      '''None'''
    ...
    def enabled (self, relativeTo=None):
      '''None'''
    ...
    def enterSignal (self):
      '''None'''
    ...
    def focusChangedSignal ():
      '''None'''
    ...
    def getContext (self):
      '''None'''
    ...
    def getDisplayTransform (self):
      '''None'''
    ...
    def getEnabled (self):
      '''None'''
    ...
    def getHighlighted (self):
      '''None'''
    ...
    def getPlug (self):
      '''None'''
    ...
    def getPlugs (self):
      '''None'''
    ...
    def getToolTip (self):
      '''None'''
    ...
    def getVisible (self):
      '''None'''
    ...
    def hasLabel (self):
      '''None'''
    ...
    def identityDisplayTransform (x):
      '''None'''
    ...
    def isAncestorOf (self, other):
      '''None'''
    ...
    def keyPressSignal (self):
      '''None'''
    ...
    def keyReleaseSignal (self):
      '''None'''
    ...
    def leaveSignal (self):
      '''None'''
    ...
    def mouseMoveSignal (self):
      '''None'''
    ...
    def mousePosition (relativeTo=None):
      '''None'''
    ...
    def parent (self):
      '''None'''
    ...
    def parentChangedSignal (self):
      '''None'''
    ...
    def popupMenuSignal ():
      '''None'''
    ...
    def registerType (plugClassOrTypeId, creator):
      '''None'''
    ...
    def reveal (self):
      '''None'''
    ...
    def setContext (self, context):
      '''None'''
    ...
    def setDisplayTransform (self, displayTransform):
      '''None'''
    ...
    def setEnabled (self, enabled):
      '''None'''
    ...
    def setHighlighted (self, highlighted):
      '''None'''
    ...
    def setPlug (self, plug):
      '''None'''
    ...
    def setPlugs (self, plugs):
      '''None'''
    ...
    def setToolTip (self, toolTip):
      '''None'''
    ...
    def setVisible (self, visible):
      '''None'''
    ...
    def size (self):
      '''None'''
    ...
    def visibilityChangedSignal (self):
      '''None'''
    ...
    def visible (self, relativeTo=None):
      '''None'''
    ...
    def wheelSignal (self):
      '''None'''
    ...
    def widgetAt (position, widgetType=None):
      '''None'''
    ...

def FilterProcessorUI (*args):
      '''

'''      
    ...

def FilterQueryUI (*args):
      '''

'''      
    ...

def FilterResultsUI (*args):
      '''

'''      
    ...

def FilterUI (*args):
      '''

'''      
    ...

def FilteredSceneProcessorUI (*args):
      '''

'''      
    ...

def FramingConstraintUI (*args):
      '''

'''      
    ...

def FreezeTransformUI (*args):
      '''

'''      
    ...

def GlobalShaderUI (*args):
      '''

'''      
    ...

def GridUI (*args):
      '''

'''      
    ...

def GroupUI (*args):
      '''

'''      
    ...

def HierarchyView (*args):
      '''

'''      
    ...

class HierarchyView:
    def Settings (name, script):
      '''None'''
    ...
    def _Editor__contextChanged (self, context, key):
      '''None'''
    ...
    def _Editor__enter (self, widget):
      '''None'''
    ...
    def _Editor__leave (self, widget):
      '''None'''
    ...
    def _Editor__namesToCreators (self, *args, **kwargs):
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
    def _Editor__setContextInternal (self, context, callUpdate):
      '''None'''
    ...
    def _HierarchyView__contextMenuSignal (self, widget):
      '''None'''
    ...
    def _HierarchyView__copySelectedPaths (self, *unused):
      '''None'''
    ...
    def _HierarchyView__expansionChanged (self, pathListing):
      '''None'''
    ...
    def _HierarchyView__frameSelectedPaths (self):
      '''None'''
    ...
    def _HierarchyView__keyPressSignal (self, widget, event):
      '''None'''
    ...
    def _HierarchyView__plugParentChanged (self, plug, oldParent):
      '''None'''
    ...
    def _HierarchyView__selectionChanged (self, pathListing):
      '''None'''
    ...
    def _HierarchyView__setPathListingPath (self):
      '''None'''
    ...
    def _HierarchyView__transferExpansionFromContext (self):
      '''None'''
    ...
    def _HierarchyView__transferSelectionFromContext (self):
      '''None'''
    ...
    def _NodeSetEditor__dirtyTitle (self):
      '''None'''
    ...
    def _NodeSetEditor__lazyUpdate (self):
      '''None'''
    ...
    def _NodeSetEditor__membersChanged (self, set, member):
      '''None'''
    ...
    def _NodeSetEditor__nameChanged (self, node, oldName):
      '''None'''
    ...
    def _NodeSetEditor__setNodeSetInternal (self, nodeSet, callUpdateFromSet):
      '''None'''
    ...
    def _Widget__applyQWidgetStyleClasses (self):
      '''None'''
    ...
    def _Widget__ensureEventFilter (self):
      '''None'''
    ...
    def _Widget__ensureFocusChangedConnection ():
      '''None'''
    ...
    def _Widget__ensureMouseTracking (self):
      '''None'''
    ...
    def _Widget__focusChanged (oldWidget, newWidget):
      '''None'''
    ...
    def _Widget__focusChangedConnected (self, *args, **kwargs):
      '''bool(x) -> bool

Returns True when the argument x is true, False otherwise.
The builtins True and False are the only two instances of the class bool.
The class bool is a subclass of the class int, and cannot be subclassed.'''
    ...
    def _Widget__focusChangedSignal (self, *args, **kwargs):
      '''None'''
    ...
    def _Widget__initNesting ():
      '''None'''
    ...
    def _Widget__keyMapping (self, *args, **kwargs):
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
    def _Widget__parentStack (self, *args, **kwargs):
      '''Built-in mutable sequence.

If no argument is given, the constructor creates a new empty list.
The argument must be an iterable if specified.'''
    ...
    def _Widget__propagateDisplayTransformChange (self):
      '''None'''
    ...
    def _Widget__qtWidgetOwners (self, *args, **kwargs):
      ''' Mapping class that references keys weakly.

    Entries in the dictionary will be discarded when there is no
    longer a strong reference to the key. This can be used to
    associate additional data with an object owned by other parts of
    an application without adding attributes to those objects. This
    can be especially useful with objects that override attribute
    accesses.
    '''
    ...
    def _Widget__styleClassName ():
      '''None'''
    ...
    def _applyVisibility (self):
      '''None'''
    ...
    def _buttons (qtButtons):
      '''None'''
    ...
    def _contextChangedConnection (self):
      '''None'''
    ...
    def _disconnectTrackedConnections (self, *args, **kwargs):
      '''
_disconnectTrackedConnections( (Trackable)arg1) -> None :

    C++ signature :
        void _disconnectTrackedConnections(Gaffer::Signals::Trackable {lvalue})'''
    ...
    def _displayTransformChanged (self):
      '''None'''
    ...
    def _doPendingUpdate (self):
      '''None'''
    ...
    def _key (qtKey):
      '''None'''
    ...
    def _lastAddedNode (self):
      '''None'''
    ...
    def _modifiers (qtModifiers):
      '''None'''
    ...
    def _owner (qtWidget):
      '''None'''
    ...
    def _popParent ():
      '''None'''
    ...
    def _postConstructor (self):
      '''None'''
    ...
    def _pushParent (container):
      '''None'''
    ...
    def _qtColor (color):
      '''None'''
    ...
    def _qtWidget (self):
      '''None'''
    ...
    def _repolish (self, qtWidget=None):
      '''None'''
    ...
    def _setStyleSheet (self):
      '''None'''
    ...
    def _titleFormat (self):
      '''None'''
    ...
    def _updateFromContext (self, modifiedItems):
      '''None'''
    ...
    def _updateFromSet (self):
      '''None'''
    ...
    def acquire (node, floating=None):
      '''None'''
    ...
    def ancestor (self, type):
      '''None'''
    ...
    def bound (self, relativeTo=None):
      '''None'''
    ...
    def buttonDoubleClickSignal (self):
      '''None'''
    ...
    def buttonPressSignal (self):
      '''None'''
    ...
    def buttonReleaseSignal (self):
      '''None'''
    ...
    def contextMenuSignal (self):
      '''None'''
    ...
    def create (name, scriptNode):
      '''None'''
    ...
    def currentModifiers ():
      '''None'''
    ...
    def displayTransform (self):
      '''None'''
    ...
    def dragBeginSignal (self):
      '''None'''
    ...
    def dragEndSignal (self):
      '''None'''
    ...
    def dragEnterSignal (self):
      '''None'''
    ...
    def dragLeaveSignal (self):
      '''None'''
    ...
    def dragMoveSignal (self):
      '''None'''
    ...
    def dropSignal (self):
      '''None'''
    ...
    def enabled (self, relativeTo=None):
      '''None'''
    ...
    def enterSignal (self):
      '''None'''
    ...
    def focusChangedSignal ():
      '''None'''
    ...
    def getContext (self):
      '''None'''
    ...
    def getDisplayTransform (self):
      '''None'''
    ...
    def getEnabled (self):
      '''None'''
    ...
    def getHighlighted (self):
      '''None'''
    ...
    def getNodeSet (self):
      '''None'''
    ...
    def getTitle (self):
      '''None'''
    ...
    def getToolTip (self):
      '''None'''
    ...
    def getVisible (self):
      '''None'''
    ...
    def identityDisplayTransform (x):
      '''None'''
    ...
    def instanceCreatedSignal ():
      '''None'''
    ...
    def isAncestorOf (self, other):
      '''None'''
    ...
    def keyPressSignal (self):
      '''None'''
    ...
    def keyReleaseSignal (self):
      '''None'''
    ...
    def leaveSignal (self):
      '''None'''
    ...
    def mouseMoveSignal (self):
      '''None'''
    ...
    def mousePosition (relativeTo=None):
      '''None'''
    ...
    def nodeSetChangedSignal (self):
      '''None'''
    ...
    def parent (self):
      '''None'''
    ...
    def parentChangedSignal (self):
      '''None'''
    ...
    def registerType (name, creator):
      '''None'''
    ...
    def reveal (self):
      '''None'''
    ...
    def scene (self):
      '''None'''
    ...
    def scriptNode (self):
      '''None'''
    ...
    def setContext (self, context):
      '''None'''
    ...
    def setDisplayTransform (self, displayTransform):
      '''None'''
    ...
    def setEnabled (self, enabled):
      '''None'''
    ...
    def setHighlighted (self, highlighted):
      '''None'''
    ...
    def setNodeSet (self, nodeSet):
      '''None'''
    ...
    def setTitle (self, title):
      '''None'''
    ...
    def setToolTip (self, toolTip):
      '''None'''
    ...
    def setVisible (self, visible):
      '''None'''
    ...
    def size (self):
      '''None'''
    ...
    def titleChangedSignal (self):
      '''None'''
    ...
    def types ():
      '''None'''
    ...
    def visibilityChangedSignal (self):
      '''None'''
    ...
    def visible (self, relativeTo=None):
      '''None'''
    ...
    def wheelSignal (self):
      '''None'''
    ...
    def widgetAt (position, widgetType=None):
      '''None'''
    ...

def ImageScatterUI (*args):
      '''

'''      
    ...

def ImageToPointsUI (*args):
      '''

'''      
    ...

def InstancerUI (*args):
      '''

'''      
    ...

def InteractiveRenderUI (*args):
      '''

'''      
    ...

def IsolateUI (*args):
      '''

'''      
    ...

def LightEditor (*args):
      '''

'''      
    ...

class LightEditor:
    def Settings (script):
      '''None'''
    ...
    def _Editor__contextChanged (self, context, key):
      '''None'''
    ...
    def _Editor__enter (self, widget):
      '''None'''
    ...
    def _Editor__leave (self, widget):
      '''None'''
    ...
    def _Editor__namesToCreators (self, *args, **kwargs):
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
    def _Editor__setContextInternal (self, context, callUpdate):
      '''None'''
    ...
    def _LightEditor__buttonDoubleClick (self, pathListing, event):
      '''None'''
    ...
    def _LightEditor__buttonPress (self, pathListing, event):
      '''None'''
    ...
    def _LightEditor__columnRegistry (self, *args, **kwargs):
      '''Dictionary that remembers insertion order'''
    ...
    def _LightEditor__deleteLights (self, *unused):
      '''None'''
    ...
    def _LightEditor__disablableInspectionTweaks (self, pathListing):
      '''None'''
    ...
    def _LightEditor__disableEdits (self, pathListing):
      '''None'''
    ...
    def _LightEditor__editSelectedCells (self, pathListing, quickBoolean=True):
      '''None'''
    ...
    def _LightEditor__keyPress (self, pathListing, event):
      '''None'''
    ...
    def _LightEditor__plugParentChanged (self, plug, oldParent):
      '''None'''
    ...
    def _LightEditor__removableAttributeInspections (self, pathListing):
      '''None'''
    ...
    def _LightEditor__removeAttributes (self, pathListing):
      '''None'''
    ...
    def _LightEditor__selectLinked (self, *unused):
      '''None'''
    ...
    def _LightEditor__selectionChanged (self, pathListing):
      '''None'''
    ...
    def _LightEditor__setPathListingPath (self):
      '''None'''
    ...
    def _LightEditor__settingsPlugSet (self, plug):
      '''None'''
    ...
    def _LightEditor__showHistory (self, *unused):
      '''None'''
    ...
    def _LightEditor__toggleBoolean (self, inspectors, inspections):
      '''None'''
    ...
    def _LightEditor__transferSelectionFromContext (self):
      '''None'''
    ...
    def _LightEditor__updateColumns (self):
      '''None'''
    ...
    def _NodeSetEditor__dirtyTitle (self):
      '''None'''
    ...
    def _NodeSetEditor__lazyUpdate (self):
      '''None'''
    ...
    def _NodeSetEditor__membersChanged (self, set, member):
      '''None'''
    ...
    def _NodeSetEditor__nameChanged (self, node, oldName):
      '''None'''
    ...
    def _NodeSetEditor__setNodeSetInternal (self, nodeSet, callUpdateFromSet):
      '''None'''
    ...
    def _SectionPlugValueWidget (*args, **kw):
      '''None'''
    ...
    def _Spacer (*args, **kw):
      '''None'''
    ...
    def _Widget__applyQWidgetStyleClasses (self):
      '''None'''
    ...
    def _Widget__ensureEventFilter (self):
      '''None'''
    ...
    def _Widget__ensureFocusChangedConnection ():
      '''None'''
    ...
    def _Widget__ensureMouseTracking (self):
      '''None'''
    ...
    def _Widget__focusChanged (oldWidget, newWidget):
      '''None'''
    ...
    def _Widget__focusChangedConnected (self, *args, **kwargs):
      '''bool(x) -> bool

Returns True when the argument x is true, False otherwise.
The builtins True and False are the only two instances of the class bool.
The class bool is a subclass of the class int, and cannot be subclassed.'''
    ...
    def _Widget__focusChangedSignal (self, *args, **kwargs):
      '''None'''
    ...
    def _Widget__initNesting ():
      '''None'''
    ...
    def _Widget__keyMapping (self, *args, **kwargs):
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
    def _Widget__parentStack (self, *args, **kwargs):
      '''Built-in mutable sequence.

If no argument is given, the constructor creates a new empty list.
The argument must be an iterable if specified.'''
    ...
    def _Widget__propagateDisplayTransformChange (self):
      '''None'''
    ...
    def _Widget__qtWidgetOwners (self, *args, **kwargs):
      ''' Mapping class that references keys weakly.

    Entries in the dictionary will be discarded when there is no
    longer a strong reference to the key. This can be used to
    associate additional data with an object owned by other parts of
    an application without adding attributes to those objects. This
    can be especially useful with objects that override attribute
    accesses.
    '''
    ...
    def _Widget__styleClassName ():
      '''None'''
    ...
    def _applyVisibility (self):
      '''None'''
    ...
    def _buttons (qtButtons):
      '''None'''
    ...
    def _contextChangedConnection (self):
      '''None'''
    ...
    def _disconnectTrackedConnections (self, *args, **kwargs):
      '''
_disconnectTrackedConnections( (Trackable)arg1) -> None :

    C++ signature :
        void _disconnectTrackedConnections(Gaffer::Signals::Trackable {lvalue})'''
    ...
    def _displayTransformChanged (self):
      '''None'''
    ...
    def _doPendingUpdate (self):
      '''None'''
    ...
    def _key (qtKey):
      '''None'''
    ...
    def _lastAddedNode (self):
      '''None'''
    ...
    def _modifiers (qtModifiers):
      '''None'''
    ...
    def _owner (qtWidget):
      '''None'''
    ...
    def _popParent ():
      '''None'''
    ...
    def _postConstructor (self):
      '''None'''
    ...
    def _pushParent (container):
      '''None'''
    ...
    def _qtColor (color):
      '''None'''
    ...
    def _qtWidget (self):
      '''None'''
    ...
    def _repolish (self, qtWidget=None):
      '''None'''
    ...
    def _setStyleSheet (self):
      '''None'''
    ...
    def _titleFormat (self):
      '''None'''
    ...
    def _updateFromContext (self, modifiedItems):
      '''None'''
    ...
    def _updateFromSet (self):
      '''None'''
    ...
    def acquire (node, floating=None):
      '''None'''
    ...
    def ancestor (self, type):
      '''None'''
    ...
    def bound (self, relativeTo=None):
      '''None'''
    ...
    def buttonDoubleClickSignal (self):
      '''None'''
    ...
    def buttonPressSignal (self):
      '''None'''
    ...
    def buttonReleaseSignal (self):
      '''None'''
    ...
    def contextMenuSignal (self):
      '''None'''
    ...
    def create (name, scriptNode):
      '''None'''
    ...
    def currentModifiers ():
      '''None'''
    ...
    def displayTransform (self):
      '''None'''
    ...
    def dragBeginSignal (self):
      '''None'''
    ...
    def dragEndSignal (self):
      '''None'''
    ...
    def dragEnterSignal (self):
      '''None'''
    ...
    def dragLeaveSignal (self):
      '''None'''
    ...
    def dragMoveSignal (self):
      '''None'''
    ...
    def dropSignal (self):
      '''None'''
    ...
    def enabled (self, relativeTo=None):
      '''None'''
    ...
    def enterSignal (self):
      '''None'''
    ...
    def focusChangedSignal ():
      '''None'''
    ...
    def getContext (self):
      '''None'''
    ...
    def getDisplayTransform (self):
      '''None'''
    ...
    def getEnabled (self):
      '''None'''
    ...
    def getHighlighted (self):
      '''None'''
    ...
    def getNodeSet (self):
      '''None'''
    ...
    def getTitle (self):
      '''None'''
    ...
    def getToolTip (self):
      '''None'''
    ...
    def getVisible (self):
      '''None'''
    ...
    def identityDisplayTransform (x):
      '''None'''
    ...
    def instanceCreatedSignal ():
      '''None'''
    ...
    def isAncestorOf (self, other):
      '''None'''
    ...
    def keyPressSignal (self):
      '''None'''
    ...
    def keyReleaseSignal (self):
      '''None'''
    ...
    def leaveSignal (self):
      '''None'''
    ...
    def mouseMoveSignal (self):
      '''None'''
    ...
    def mousePosition (relativeTo=None):
      '''None'''
    ...
    def nodeSetChangedSignal (self):
      '''None'''
    ...
    def parent (self):
      '''None'''
    ...
    def parentChangedSignal (self):
      '''None'''
    ...
    def registerAttribute (rendererKey, attributeName, section=None):
      '''None'''
    ...
    def registerColumn (rendererKey, columnKey, inspectorFunction, section=None):
      '''None'''
    ...
    def registerParameter (rendererKey, parameter, section=None):
      '''None'''
    ...
    def registerType (name, creator):
      '''None'''
    ...
    def reveal (self):
      '''None'''
    ...
    def scene (self):
      '''None'''
    ...
    def scriptNode (self):
      '''None'''
    ...
    def setContext (self, context):
      '''None'''
    ...
    def setDisplayTransform (self, displayTransform):
      '''None'''
    ...
    def setEnabled (self, enabled):
      '''None'''
    ...
    def setHighlighted (self, highlighted):
      '''None'''
    ...
    def setNodeSet (self, nodeSet):
      '''None'''
    ...
    def setTitle (self, title):
      '''None'''
    ...
    def setToolTip (self, toolTip):
      '''None'''
    ...
    def setVisible (self, visible):
      '''None'''
    ...
    def size (self):
      '''None'''
    ...
    def titleChangedSignal (self):
      '''None'''
    ...
    def types ():
      '''None'''
    ...
    def visibilityChangedSignal (self):
      '''None'''
    ...
    def visible (self, relativeTo=None):
      '''None'''
    ...
    def wheelSignal (self):
      '''None'''
    ...
    def widgetAt (position, widgetType=None):
      '''None'''
    ...

def LightFilterUI (*args):
      '''

'''      
    ...

def LightPositionTool (*args):
      '''
__init__(_object*, GafferSceneUI::SceneView*)

'''      
    ...

class LightPositionTool:
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
    def Orientation (self, *args, **kwargs):
      '''None'''
    ...
    def Range (parent):
      '''None'''
    ...
    def RecursiveRange (parent):
      '''None'''
    ...
    def Selection (self, *args, **kwargs):
      '''None'''
    ...
    def SelectionChangedSignal (self, *args, **kwargs):
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
acceptsChild( (LightPositionTool)arg1, (GraphComponent)arg2) -> bool :

    C++ signature :
        bool acceptsChild(GafferSceneUI::LightPositionTool,Gaffer::GraphComponent const*)'''
    ...
    def acceptsParent (self, *args, **kwargs):
      '''
acceptsParent( (LightPositionTool)arg1, (GraphComponent)arg2) -> bool :

    C++ signature :
        bool acceptsParent(GafferSceneUI::LightPositionTool,Gaffer::GraphComponent const*)'''
    ...
    def addChild (self, *args, **kwargs):
      '''
addChild( (GraphComponent)arg1, (GraphComponent)arg2) -> None :

    C++ signature :
        void addChild(Gaffer::GraphComponent {lvalue},Gaffer::GraphComponent {lvalue})'''
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
    def create (self, *args, **kwargs):
      '''
create( (object)arg1, (View)arg2) -> object :

    C++ signature :
        boost::intrusive_ptr<GafferUI::Tool> create(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >,GafferUI::View {lvalue})'''
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
    def handlesTransform (self, *args, **kwargs):
      '''
handlesTransform( (TransformTool)arg1) -> M44f :

    C++ signature :
        Imath_3_1::Matrix44<float> handlesTransform(GafferSceneUI::TransformTool {lvalue})'''
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
isInstanceOf( (LightPositionTool)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(GafferSceneUI::LightPositionTool {lvalue},IECore::TypeId)

isInstanceOf( (LightPositionTool)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(GafferSceneUI::LightPositionTool {lvalue},char const*)'''
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
    def positionHighlight (self, *args, **kwargs):
      '''
positionHighlight( (LightPositionTool)arg1, (V3f)arg2, (V3f)arg3, (V3f)arg4, (float)arg5) -> None :

    C++ signature :
        void positionHighlight(GafferSceneUI::LightPositionTool {lvalue},Imath_3_1::Vec3<float>,Imath_3_1::Vec3<float>,Imath_3_1::Vec3<float>,float)'''
    ...
    def positionShadow (self, *args, **kwargs):
      '''
positionShadow( (LightPositionTool)arg1, (V3f)arg2, (V3f)arg3, (float)arg4) -> None :

    C++ signature :
        void positionShadow(GafferSceneUI::LightPositionTool {lvalue},Imath_3_1::Vec3<float>,Imath_3_1::Vec3<float>,float)'''
    ...
    def refCount (self, *args, **kwargs):
      '''
refCount( (RefCounted)arg1) -> int :

    C++ signature :
        unsigned long refCount(IECore::RefCounted {lvalue})'''
    ...
    def registerTool (self, *args, **kwargs):
      '''
registerTool( (object)arg1, (TypeId)arg2, (object)arg3) -> None :

    C++ signature :
        void registerTool(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >,IECore::TypeId,boost::python::api::object)'''
    ...
    def registerType (self, *args, **kwargs):
      '''
registerType( (TypeId)arg1, (str)arg2, (TypeId)arg3) -> None :

    C++ signature :
        void registerType(IECore::TypeId,char const*,IECore::TypeId)'''
    ...
    def registeredTools (self, *args, **kwargs):
      '''
registeredTools( (TypeId)arg1) -> list :

    C++ signature :
        boost::python::list registeredTools(IECore::TypeId)'''
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
    def selection (self, *args, **kwargs):
      '''
selection( (TransformTool)arg1) -> list :

    C++ signature :
        boost::python::list selection(GafferSceneUI::TransformTool)'''
    ...
    def selectionChangedSignal (self, *args, **kwargs):
      '''
selectionChangedSignal( (TransformTool)arg1) -> SelectionChangedSignal :

    C++ signature :
        Gaffer::Signals::Signal<void (GafferSceneUI::TransformTool&), Gaffer::Signals::DefaultCombiner<void> > {lvalue} selectionChangedSignal(GafferSceneUI::TransformTool {lvalue})'''
    ...
    def selectionEditable (self, *args, **kwargs):
      '''
selectionEditable( (TransformTool)arg1) -> bool :

    C++ signature :
        bool selectionEditable(GafferSceneUI::TransformTool)'''
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
typeId( (LightPositionTool)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(GafferSceneUI::LightPositionTool {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (LightPositionTool)arg1) -> str :

    C++ signature :
        char const* typeName(GafferSceneUI::LightPositionTool {lvalue})'''
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
    def view (self, *args, **kwargs):
      '''
view( (Tool)arg1) -> object :

    C++ signature :
        GafferUI::View* view(GafferUI::Tool {lvalue})'''
    ...

def LightPositionToolUI (*args):
      '''

'''      
    ...

def LightToCameraUI (*args):
      '''

'''      
    ...

def LightTool (*args):
      '''
__init__(_object*, GafferSceneUI::SceneView*)

'''      
    ...

class LightTool:
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
    def SelectionChangedSignal (self, *args, **kwargs):
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
acceptsChild( (LightTool)arg1, (GraphComponent)arg2) -> bool :

    C++ signature :
        bool acceptsChild(GafferSceneUI::LightTool,Gaffer::GraphComponent const*)'''
    ...
    def acceptsParent (self, *args, **kwargs):
      '''
acceptsParent( (LightTool)arg1, (GraphComponent)arg2) -> bool :

    C++ signature :
        bool acceptsParent(GafferSceneUI::LightTool,Gaffer::GraphComponent const*)'''
    ...
    def addChild (self, *args, **kwargs):
      '''
addChild( (GraphComponent)arg1, (GraphComponent)arg2) -> None :

    C++ signature :
        void addChild(Gaffer::GraphComponent {lvalue},Gaffer::GraphComponent {lvalue})'''
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
    def create (self, *args, **kwargs):
      '''
create( (object)arg1, (View)arg2) -> object :

    C++ signature :
        boost::intrusive_ptr<GafferUI::Tool> create(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >,GafferUI::View {lvalue})'''
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
isInstanceOf( (LightTool)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(GafferSceneUI::LightTool {lvalue},IECore::TypeId)

isInstanceOf( (LightTool)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(GafferSceneUI::LightTool {lvalue},char const*)'''
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
    def registerTool (self, *args, **kwargs):
      '''
registerTool( (object)arg1, (TypeId)arg2, (object)arg3) -> None :

    C++ signature :
        void registerTool(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >,IECore::TypeId,boost::python::api::object)'''
    ...
    def registerType (self, *args, **kwargs):
      '''
registerType( (TypeId)arg1, (str)arg2, (TypeId)arg3) -> None :

    C++ signature :
        void registerType(IECore::TypeId,char const*,IECore::TypeId)'''
    ...
    def registeredTools (self, *args, **kwargs):
      '''
registeredTools( (TypeId)arg1) -> list :

    C++ signature :
        boost::python::list registeredTools(IECore::TypeId)'''
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
    def selection (self, *args, **kwargs):
      '''
selection( (LightTool)arg1) -> PathMatcher :

    C++ signature :
        IECore::PathMatcher selection(GafferSceneUI::LightTool)'''
    ...
    def selectionChangedSignal (self, *args, **kwargs):
      '''
selectionChangedSignal( (LightTool)arg1) -> SelectionChangedSignal :

    C++ signature :
        Gaffer::Signals::Signal<void (GafferSceneUI::LightTool&), Gaffer::Signals::DefaultCombiner<void> > {lvalue} selectionChangedSignal(GafferSceneUI::LightTool {lvalue})'''
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
typeId( (LightTool)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(GafferSceneUI::LightTool {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (LightTool)arg1) -> str :

    C++ signature :
        char const* typeName(GafferSceneUI::LightTool {lvalue})'''
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
    def view (self, *args, **kwargs):
      '''
view( (Tool)arg1) -> object :

    C++ signature :
        GafferUI::View* view(GafferUI::Tool {lvalue})'''
    ...

def LightToolUI (*args):
      '''

'''      
    ...

def LightUI (*args):
      '''

'''      
    ...

def LocaliseAttributesUI (*args):
      '''

'''      
    ...

def MapOffsetUI (*args):
      '''

'''      
    ...

def MapProjectionUI (*args):
      '''

'''      
    ...

def MergeScenesUI (*args):
      '''

'''      
    ...

def MeshDistortionUI (*args):
      '''

'''      
    ...

def MeshNormalsUI (*args):
      '''

'''      
    ...

def MeshSegmentsUI (*args):
      '''

'''      
    ...

def MeshSplitUI (*args):
      '''

'''      
    ...

def MeshTangentsUI (*args):
      '''

'''      
    ...

def MeshToPointsUI (*args):
      '''

'''      
    ...

def MeshTypeUI (*args):
      '''

'''      
    ...

def MotionPathUI (*args):
      '''

'''      
    ...

def ObjectSourceUI (*args):
      '''

'''      
    ...

def ObjectToSceneUI (*args):
      '''

'''      
    ...

def OpenGLAttributesUI (*args):
      '''

'''      
    ...

def OpenGLRenderUI (*args):
      '''

'''      
    ...

def OpenGLShaderUI (*args):
      '''

'''      
    ...

def OptionQueryUI (*args):
      '''

'''      
    ...

def OptionTweaksUI (*args):
      '''

'''      
    ...

def OptionsUI (*args):
      '''

'''      
    ...

def OrientationUI (*args):
      '''

'''      
    ...

def OutputsUI (*args):
      '''

'''      
    ...

def ParametersUI (*args):
      '''

'''      
    ...

def ParentConstraintUI (*args):
      '''

'''      
    ...

def ParentUI (*args):
      '''

'''      
    ...

def PathFilterUI (*args):
      '''

'''      
    ...

def PlaneUI (*args):
      '''

'''      
    ...

def PointConstraintUI (*args):
      '''

'''      
    ...

def PointsTypeUI (*args):
      '''

'''      
    ...

def PrimitiveInspector (*args):
      '''

'''      
    ...

class PrimitiveInspector:
    def Settings (name, script):
      '''None'''
    ...
    def _Editor__contextChanged (self, context, key):
      '''None'''
    ...
    def _Editor__enter (self, widget):
      '''None'''
    ...
    def _Editor__leave (self, widget):
      '''None'''
    ...
    def _Editor__namesToCreators (self, *args, **kwargs):
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
    def _Editor__setContextInternal (self, context, callUpdate):
      '''None'''
    ...
    def _NodeSetEditor__dirtyTitle (self):
      '''None'''
    ...
    def _NodeSetEditor__lazyUpdate (self):
      '''None'''
    ...
    def _NodeSetEditor__membersChanged (self, set, member):
      '''None'''
    ...
    def _NodeSetEditor__nameChanged (self, node, oldName):
      '''None'''
    ...
    def _NodeSetEditor__setNodeSetInternal (self, nodeSet, callUpdateFromSet):
      '''None'''
    ...
    def _PrimitiveInspector__backgroundUpdate (self):
      '''None'''
    ...
    def _PrimitiveInspector__backgroundUpdatePlug (self, *args, **kwargs):
      '''None'''
    ...
    def _PrimitiveInspector__backgroundUpdatePostCall (self, *args, **kwargs):
      '''None'''
    ...
    def _PrimitiveInspector__backgroundUpdatePreCall (self, *args, **kwargs):
      '''None'''
    ...
    def _PrimitiveInspector__plugDirtied (self, plug):
      '''None'''
    ...
    def _PrimitiveInspector__plugParentChanged (self, plug, oldParent):
      '''None'''
    ...
    def _PrimitiveInspector__updateLazily (self):
      '''None'''
    ...
    def _Widget__applyQWidgetStyleClasses (self):
      '''None'''
    ...
    def _Widget__ensureEventFilter (self):
      '''None'''
    ...
    def _Widget__ensureFocusChangedConnection ():
      '''None'''
    ...
    def _Widget__ensureMouseTracking (self):
      '''None'''
    ...
    def _Widget__focusChanged (oldWidget, newWidget):
      '''None'''
    ...
    def _Widget__focusChangedConnected (self, *args, **kwargs):
      '''bool(x) -> bool

Returns True when the argument x is true, False otherwise.
The builtins True and False are the only two instances of the class bool.
The class bool is a subclass of the class int, and cannot be subclassed.'''
    ...
    def _Widget__focusChangedSignal (self, *args, **kwargs):
      '''None'''
    ...
    def _Widget__initNesting ():
      '''None'''
    ...
    def _Widget__keyMapping (self, *args, **kwargs):
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
    def _Widget__parentStack (self, *args, **kwargs):
      '''Built-in mutable sequence.

If no argument is given, the constructor creates a new empty list.
The argument must be an iterable if specified.'''
    ...
    def _Widget__propagateDisplayTransformChange (self):
      '''None'''
    ...
    def _Widget__qtWidgetOwners (self, *args, **kwargs):
      ''' Mapping class that references keys weakly.

    Entries in the dictionary will be discarded when there is no
    longer a strong reference to the key. This can be used to
    associate additional data with an object owned by other parts of
    an application without adding attributes to those objects. This
    can be especially useful with objects that override attribute
    accesses.
    '''
    ...
    def _Widget__styleClassName ():
      '''None'''
    ...
    def _applyVisibility (self):
      '''None'''
    ...
    def _buttons (qtButtons):
      '''None'''
    ...
    def _contextChangedConnection (self):
      '''None'''
    ...
    def _disconnectTrackedConnections (self, *args, **kwargs):
      '''
_disconnectTrackedConnections( (Trackable)arg1) -> None :

    C++ signature :
        void _disconnectTrackedConnections(Gaffer::Signals::Trackable {lvalue})'''
    ...
    def _displayTransformChanged (self):
      '''None'''
    ...
    def _doPendingUpdate (self):
      '''None'''
    ...
    def _key (qtKey):
      '''None'''
    ...
    def _lastAddedNode (self):
      '''None'''
    ...
    def _modifiers (qtModifiers):
      '''None'''
    ...
    def _owner (qtWidget):
      '''None'''
    ...
    def _popParent ():
      '''None'''
    ...
    def _postConstructor (self):
      '''None'''
    ...
    def _pushParent (container):
      '''None'''
    ...
    def _qtColor (color):
      '''None'''
    ...
    def _qtWidget (self):
      '''None'''
    ...
    def _repolish (self, qtWidget=None):
      '''None'''
    ...
    def _setStyleSheet (self):
      '''None'''
    ...
    def _titleFormat (self, _prefix=None, _maxNodes=2, _reverseNodes=False, _ellipsis=True):
      '''None'''
    ...
    def _updateFromContext (self, modifiedItems):
      '''None'''
    ...
    def _updateFromSet (self):
      '''None'''
    ...
    def acquire (node, floating=None):
      '''None'''
    ...
    def ancestor (self, type):
      '''None'''
    ...
    def bound (self, relativeTo=None):
      '''None'''
    ...
    def buttonDoubleClickSignal (self):
      '''None'''
    ...
    def buttonPressSignal (self):
      '''None'''
    ...
    def buttonReleaseSignal (self):
      '''None'''
    ...
    def contextMenuSignal (self):
      '''None'''
    ...
    def create (name, scriptNode):
      '''None'''
    ...
    def currentModifiers ():
      '''None'''
    ...
    def displayTransform (self):
      '''None'''
    ...
    def dragBeginSignal (self):
      '''None'''
    ...
    def dragEndSignal (self):
      '''None'''
    ...
    def dragEnterSignal (self):
      '''None'''
    ...
    def dragLeaveSignal (self):
      '''None'''
    ...
    def dragMoveSignal (self):
      '''None'''
    ...
    def dropSignal (self):
      '''None'''
    ...
    def enabled (self, relativeTo=None):
      '''None'''
    ...
    def enterSignal (self):
      '''None'''
    ...
    def focusChangedSignal ():
      '''None'''
    ...
    def getContext (self):
      '''None'''
    ...
    def getDisplayTransform (self):
      '''None'''
    ...
    def getEnabled (self):
      '''None'''
    ...
    def getHighlighted (self):
      '''None'''
    ...
    def getNodeSet (self):
      '''None'''
    ...
    def getTitle (self):
      '''None'''
    ...
    def getToolTip (self):
      '''None'''
    ...
    def getVisible (self):
      '''None'''
    ...
    def identityDisplayTransform (x):
      '''None'''
    ...
    def instanceCreatedSignal ():
      '''None'''
    ...
    def isAncestorOf (self, other):
      '''None'''
    ...
    def keyPressSignal (self):
      '''None'''
    ...
    def keyReleaseSignal (self):
      '''None'''
    ...
    def leaveSignal (self):
      '''None'''
    ...
    def mouseMoveSignal (self):
      '''None'''
    ...
    def mousePosition (relativeTo=None):
      '''None'''
    ...
    def nodeSetChangedSignal (self):
      '''None'''
    ...
    def parent (self):
      '''None'''
    ...
    def parentChangedSignal (self):
      '''None'''
    ...
    def registerType (name, creator):
      '''None'''
    ...
    def reveal (self):
      '''None'''
    ...
    def scriptNode (self):
      '''None'''
    ...
    def setContext (self, context):
      '''None'''
    ...
    def setDisplayTransform (self, displayTransform):
      '''None'''
    ...
    def setEnabled (self, enabled):
      '''None'''
    ...
    def setHighlighted (self, highlighted):
      '''None'''
    ...
    def setNodeSet (self, nodeSet):
      '''None'''
    ...
    def setTitle (self, title):
      '''None'''
    ...
    def setToolTip (self, toolTip):
      '''None'''
    ...
    def setVisible (self, visible):
      '''None'''
    ...
    def size (self):
      '''None'''
    ...
    def titleChangedSignal (self):
      '''None'''
    ...
    def types ():
      '''None'''
    ...
    def visibilityChangedSignal (self):
      '''None'''
    ...
    def visible (self, relativeTo=None):
      '''None'''
    ...
    def wheelSignal (self):
      '''None'''
    ...
    def widgetAt (position, widgetType=None):
      '''None'''
    ...

def PrimitiveSamplerUI (*args):
      '''

'''      
    ...

def PrimitiveVariableExistsUI (*args):
      '''

'''      
    ...

def PrimitiveVariableProcessorUI (*args):
      '''

'''      
    ...

def PrimitiveVariableQueryUI (*args):
      '''

'''      
    ...

def PrimitiveVariablesUI (*args):
      '''

'''      
    ...

def Private (*args):
      '''

'''      
    ...

def PruneUI (*args):
      '''

'''      
    ...

def RenameUI (*args):
      '''

'''      
    ...

def RenderPassEditor (*args):
      '''

'''      
    ...

class RenderPassEditor:
    def Settings ():
      '''None'''
    ...
    def _Editor__contextChanged (self, context, key):
      '''None'''
    ...
    def _Editor__enter (self, widget):
      '''None'''
    ...
    def _Editor__leave (self, widget):
      '''None'''
    ...
    def _Editor__namesToCreators (self, *args, **kwargs):
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
    def _Editor__setContextInternal (self, context, callUpdate):
      '''None'''
    ...
    def _NodeSetEditor__dirtyTitle (self):
      '''None'''
    ...
    def _NodeSetEditor__lazyUpdate (self):
      '''None'''
    ...
    def _NodeSetEditor__membersChanged (self, set, member):
      '''None'''
    ...
    def _NodeSetEditor__nameChanged (self, node, oldName):
      '''None'''
    ...
    def _NodeSetEditor__setNodeSetInternal (self, nodeSet, callUpdateFromSet):
      '''None'''
    ...
    def _RenderPassEditor__addButtonClicked (self, button):
      '''None'''
    ...
    def _RenderPassEditor__addRenderPass (self, renderPass, editScope):
      '''None'''
    ...
    def _RenderPassEditor__addRenderPassButtonMenuSignal (self, *args, **kwargs):
      '''None'''
    ...
    def _RenderPassEditor__buttonDoubleClick (self, pathListing, event):
      '''None'''
    ...
    def _RenderPassEditor__buttonPress (self, pathListing, event):
      '''None'''
    ...
    def _RenderPassEditor__canEditRenderPasses (self, editScope=None):
      '''None'''
    ...
    def _RenderPassEditor__columnRegistry (self, *args, **kwargs):
      '''Dictionary that remembers insertion order'''
    ...
    def _RenderPassEditor__deleteSelectedRenderPasses (self):
      '''None'''
    ...
    def _RenderPassEditor__disablableInspectionTweaks (self, pathListing):
      '''None'''
    ...
    def _RenderPassEditor__disableEdits (self, pathListing):
      '''None'''
    ...
    def _RenderPassEditor__disableRenderPasses (self, renderPasses, editScope):
      '''None'''
    ...
    def _RenderPassEditor__displayGroupedChanged (self):
      '''None'''
    ...
    def _RenderPassEditor__dragBegin (self, widget, event):
      '''None'''
    ...
    def _RenderPassEditor__editSelectedCells (self, pathListing, quickBoolean=True):
      '''None'''
    ...
    def _RenderPassEditor__firstValidScenePlug (self, node):
      '''None'''
    ...
    def _RenderPassEditor__keyPress (self, pathListing, event):
      '''None'''
    ...
    def _RenderPassEditor__metadataChanged (self, nodeTypeId, key, node):
      '''None'''
    ...
    def _RenderPassEditor__plugParentChanged (self, plug, oldParent):
      '''None'''
    ...
    def _RenderPassEditor__removeButtonClicked (self, button):
      '''None'''
    ...
    def _RenderPassEditor__renderPassCreationDialogue (self):
      '''None'''
    ...
    def _RenderPassEditor__renderPassNames (self, plug):
      '''None'''
    ...
    def _RenderPassEditor__selectedRenderPasses (self, columns=[0]):
      '''None'''
    ...
    def _RenderPassEditor__selectionChanged (self, pathListing):
      '''None'''
    ...
    def _RenderPassEditor__setActiveRenderPass (self, pathListing):
      '''None'''
    ...
    def _RenderPassEditor__setPathListingPath (self):
      '''None'''
    ...
    def _RenderPassEditor__settingsPlugInputChanged (self, plug):
      '''None'''
    ...
    def _RenderPassEditor__settingsPlugSet (self, plug):
      '''None'''
    ...
    def _RenderPassEditor__showEditHistory (self, *unused):
      '''None'''
    ...
    def _RenderPassEditor__toggleBoolean (self, inspectors, inspections):
      '''None'''
    ...
    def _RenderPassEditor__updateButtonStatus (self, *unused):
      '''None'''
    ...
    def _RenderPassEditor__updateColumns (self):
      '''None'''
    ...
    def _SectionPlugValueWidget (*args, **kw):
      '''None'''
    ...
    def _Spacer (*args, **kw):
      '''None'''
    ...
    def _ToggleGroupingPlugValueWidget (*args, **kw):
      '''None'''
    ...
    def _Widget__applyQWidgetStyleClasses (self):
      '''None'''
    ...
    def _Widget__ensureEventFilter (self):
      '''None'''
    ...
    def _Widget__ensureFocusChangedConnection ():
      '''None'''
    ...
    def _Widget__ensureMouseTracking (self):
      '''None'''
    ...
    def _Widget__focusChanged (oldWidget, newWidget):
      '''None'''
    ...
    def _Widget__focusChangedConnected (self, *args, **kwargs):
      '''bool(x) -> bool

Returns True when the argument x is true, False otherwise.
The builtins True and False are the only two instances of the class bool.
The class bool is a subclass of the class int, and cannot be subclassed.'''
    ...
    def _Widget__focusChangedSignal (self, *args, **kwargs):
      '''None'''
    ...
    def _Widget__initNesting ():
      '''None'''
    ...
    def _Widget__keyMapping (self, *args, **kwargs):
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
    def _Widget__parentStack (self, *args, **kwargs):
      '''Built-in mutable sequence.

If no argument is given, the constructor creates a new empty list.
The argument must be an iterable if specified.'''
    ...
    def _Widget__propagateDisplayTransformChange (self):
      '''None'''
    ...
    def _Widget__qtWidgetOwners (self, *args, **kwargs):
      ''' Mapping class that references keys weakly.

    Entries in the dictionary will be discarded when there is no
    longer a strong reference to the key. This can be used to
    associate additional data with an object owned by other parts of
    an application without adding attributes to those objects. This
    can be especially useful with objects that override attribute
    accesses.
    '''
    ...
    def _Widget__styleClassName ():
      '''None'''
    ...
    def _applyVisibility (self):
      '''None'''
    ...
    def _buttons (qtButtons):
      '''None'''
    ...
    def _contextChangedConnection (self):
      '''None'''
    ...
    def _disconnectTrackedConnections (self, *args, **kwargs):
      '''
_disconnectTrackedConnections( (Trackable)arg1) -> None :

    C++ signature :
        void _disconnectTrackedConnections(Gaffer::Signals::Trackable {lvalue})'''
    ...
    def _displayTransformChanged (self):
      '''None'''
    ...
    def _doPendingUpdate (self):
      '''None'''
    ...
    def _key (qtKey):
      '''None'''
    ...
    def _lastAddedNode (self):
      '''None'''
    ...
    def _modifiers (qtModifiers):
      '''None'''
    ...
    def _owner (qtWidget):
      '''None'''
    ...
    def _popParent ():
      '''None'''
    ...
    def _postConstructor (self):
      '''None'''
    ...
    def _pushParent (container):
      '''None'''
    ...
    def _qtColor (color):
      '''None'''
    ...
    def _qtWidget (self):
      '''None'''
    ...
    def _repolish (self, qtWidget=None):
      '''None'''
    ...
    def _setStyleSheet (self):
      '''None'''
    ...
    def _titleFormat (self):
      '''None'''
    ...
    def _updateFromContext (self, modifiedItems):
      '''None'''
    ...
    def _updateFromSet (self):
      '''None'''
    ...
    def acquire (node, floating=None):
      '''None'''
    ...
    def addRenderPassButtonMenuSignal ():
      '''None'''
    ...
    def ancestor (self, type):
      '''None'''
    ...
    def bound (self, relativeTo=None):
      '''None'''
    ...
    def buttonDoubleClickSignal (self):
      '''None'''
    ...
    def buttonPressSignal (self):
      '''None'''
    ...
    def buttonReleaseSignal (self):
      '''None'''
    ...
    def contextMenuSignal (self):
      '''None'''
    ...
    def create (name, scriptNode):
      '''None'''
    ...
    def currentModifiers ():
      '''None'''
    ...
    def displayTransform (self):
      '''None'''
    ...
    def dragBeginSignal (self):
      '''None'''
    ...
    def dragEndSignal (self):
      '''None'''
    ...
    def dragEnterSignal (self):
      '''None'''
    ...
    def dragLeaveSignal (self):
      '''None'''
    ...
    def dragMoveSignal (self):
      '''None'''
    ...
    def dropSignal (self):
      '''None'''
    ...
    def enabled (self, relativeTo=None):
      '''None'''
    ...
    def enterSignal (self):
      '''None'''
    ...
    def focusChangedSignal ():
      '''None'''
    ...
    def getContext (self):
      '''None'''
    ...
    def getDisplayTransform (self):
      '''None'''
    ...
    def getEnabled (self):
      '''None'''
    ...
    def getHighlighted (self):
      '''None'''
    ...
    def getNodeSet (self):
      '''None'''
    ...
    def getTitle (self):
      '''None'''
    ...
    def getToolTip (self):
      '''None'''
    ...
    def getVisible (self):
      '''None'''
    ...
    def identityDisplayTransform (x):
      '''None'''
    ...
    def instanceCreatedSignal ():
      '''None'''
    ...
    def isAncestorOf (self, other):
      '''None'''
    ...
    def keyPressSignal (self):
      '''None'''
    ...
    def keyReleaseSignal (self):
      '''None'''
    ...
    def leaveSignal (self):
      '''None'''
    ...
    def mouseMoveSignal (self):
      '''None'''
    ...
    def mousePosition (relativeTo=None):
      '''None'''
    ...
    def nodeSetChangedSignal (self):
      '''None'''
    ...
    def parent (self):
      '''None'''
    ...
    def parentChangedSignal (self):
      '''None'''
    ...
    def pathGroupingFunction ():
      '''None'''
    ...
    def registerColumn (groupKey, columnKey, inspectorFunction, section='Main'):
      '''None'''
    ...
    def registerOption (groupKey, optionName, section='Main', columnName=None):
      '''None'''
    ...
    def registerPathGroupingFunction (f):
      '''None'''
    ...
    def registerType (name, creator):
      '''None'''
    ...
    def reveal (self):
      '''None'''
    ...
    def scriptNode (self):
      '''None'''
    ...
    def setContext (self, context):
      '''None'''
    ...
    def setDisplayTransform (self, displayTransform):
      '''None'''
    ...
    def setEnabled (self, enabled):
      '''None'''
    ...
    def setHighlighted (self, highlighted):
      '''None'''
    ...
    def setNodeSet (self, nodeSet):
      '''None'''
    ...
    def setTitle (self, title):
      '''None'''
    ...
    def setToolTip (self, toolTip):
      '''None'''
    ...
    def setVisible (self, visible):
      '''None'''
    ...
    def size (self):
      '''None'''
    ...
    def titleChangedSignal (self):
      '''None'''
    ...
    def types ():
      '''None'''
    ...
    def visibilityChangedSignal (self):
      '''None'''
    ...
    def visible (self, relativeTo=None):
      '''None'''
    ...
    def wheelSignal (self):
      '''None'''
    ...
    def widgetAt (position, widgetType=None):
      '''None'''
    ...

def RenderPassWedgeUI (*args):
      '''

'''      
    ...

def RenderPassesUI (*args):
      '''

'''      
    ...

def RenderUI (*args):
      '''

'''      
    ...

def ResamplePrimitiveVariablesUI (*args):
      '''

'''      
    ...

def ReverseWindingUI (*args):
      '''

'''      
    ...

def RotateTool (*args):
      '''
__init__(_object*, GafferSceneUI::SceneView*)

'''      
    ...

class RotateTool:
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
    def Orientation (self, *args, **kwargs):
      '''None'''
    ...
    def Range (parent):
      '''None'''
    ...
    def RecursiveRange (parent):
      '''None'''
    ...
    def Selection (self, *args, **kwargs):
      '''None'''
    ...
    def SelectionChangedSignal (self, *args, **kwargs):
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
acceptsChild( (RotateTool)arg1, (GraphComponent)arg2) -> bool :

    C++ signature :
        bool acceptsChild(GafferSceneUI::RotateTool,Gaffer::GraphComponent const*)'''
    ...
    def acceptsParent (self, *args, **kwargs):
      '''
acceptsParent( (RotateTool)arg1, (GraphComponent)arg2) -> bool :

    C++ signature :
        bool acceptsParent(GafferSceneUI::RotateTool,Gaffer::GraphComponent const*)'''
    ...
    def addChild (self, *args, **kwargs):
      '''
addChild( (GraphComponent)arg1, (GraphComponent)arg2) -> None :

    C++ signature :
        void addChild(Gaffer::GraphComponent {lvalue},Gaffer::GraphComponent {lvalue})'''
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
    def create (self, *args, **kwargs):
      '''
create( (object)arg1, (View)arg2) -> object :

    C++ signature :
        boost::intrusive_ptr<GafferUI::Tool> create(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >,GafferUI::View {lvalue})'''
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
    def handlesTransform (self, *args, **kwargs):
      '''
handlesTransform( (TransformTool)arg1) -> M44f :

    C++ signature :
        Imath_3_1::Matrix44<float> handlesTransform(GafferSceneUI::TransformTool {lvalue})'''
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
isInstanceOf( (RotateTool)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(GafferSceneUI::RotateTool {lvalue},IECore::TypeId)

isInstanceOf( (RotateTool)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(GafferSceneUI::RotateTool {lvalue},char const*)'''
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
    def registerTool (self, *args, **kwargs):
      '''
registerTool( (object)arg1, (TypeId)arg2, (object)arg3) -> None :

    C++ signature :
        void registerTool(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >,IECore::TypeId,boost::python::api::object)'''
    ...
    def registerType (self, *args, **kwargs):
      '''
registerType( (TypeId)arg1, (str)arg2, (TypeId)arg3) -> None :

    C++ signature :
        void registerType(IECore::TypeId,char const*,IECore::TypeId)'''
    ...
    def registeredTools (self, *args, **kwargs):
      '''
registeredTools( (TypeId)arg1) -> list :

    C++ signature :
        boost::python::list registeredTools(IECore::TypeId)'''
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
    def rotate (self, *args, **kwargs):
      '''
rotate( (RotateTool)arg1, (Eulerf)arg2) -> None :

    C++ signature :
        void rotate(GafferSceneUI::RotateTool {lvalue},Imath_3_1::Euler<float>)'''
    ...
    def scriptNode (self, *args, **kwargs):
      '''
scriptNode( (Node)arg1) -> object :

    C++ signature :
        Gaffer::ScriptNode* scriptNode(Gaffer::Node {lvalue})'''
    ...
    def selection (self, *args, **kwargs):
      '''
selection( (TransformTool)arg1) -> list :

    C++ signature :
        boost::python::list selection(GafferSceneUI::TransformTool)'''
    ...
    def selectionChangedSignal (self, *args, **kwargs):
      '''
selectionChangedSignal( (TransformTool)arg1) -> SelectionChangedSignal :

    C++ signature :
        Gaffer::Signals::Signal<void (GafferSceneUI::TransformTool&), Gaffer::Signals::DefaultCombiner<void> > {lvalue} selectionChangedSignal(GafferSceneUI::TransformTool {lvalue})'''
    ...
    def selectionEditable (self, *args, **kwargs):
      '''
selectionEditable( (TransformTool)arg1) -> bool :

    C++ signature :
        bool selectionEditable(GafferSceneUI::TransformTool)'''
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
typeId( (RotateTool)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(GafferSceneUI::RotateTool {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (RotateTool)arg1) -> str :

    C++ signature :
        char const* typeName(GafferSceneUI::RotateTool {lvalue})'''
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
    def view (self, *args, **kwargs):
      '''
view( (Tool)arg1) -> object :

    C++ signature :
        GafferUI::View* view(GafferUI::Tool {lvalue})'''
    ...

def RotateToolUI (*args):
      '''

'''      
    ...

def ScaleTool (*args):
      '''
__init__(_object*, GafferSceneUI::SceneView*)

'''      
    ...

class ScaleTool:
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
    def Orientation (self, *args, **kwargs):
      '''None'''
    ...
    def Range (parent):
      '''None'''
    ...
    def RecursiveRange (parent):
      '''None'''
    ...
    def Selection (self, *args, **kwargs):
      '''None'''
    ...
    def SelectionChangedSignal (self, *args, **kwargs):
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
acceptsChild( (ScaleTool)arg1, (GraphComponent)arg2) -> bool :

    C++ signature :
        bool acceptsChild(GafferSceneUI::ScaleTool,Gaffer::GraphComponent const*)'''
    ...
    def acceptsParent (self, *args, **kwargs):
      '''
acceptsParent( (ScaleTool)arg1, (GraphComponent)arg2) -> bool :

    C++ signature :
        bool acceptsParent(GafferSceneUI::ScaleTool,Gaffer::GraphComponent const*)'''
    ...
    def addChild (self, *args, **kwargs):
      '''
addChild( (GraphComponent)arg1, (GraphComponent)arg2) -> None :

    C++ signature :
        void addChild(Gaffer::GraphComponent {lvalue},Gaffer::GraphComponent {lvalue})'''
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
    def create (self, *args, **kwargs):
      '''
create( (object)arg1, (View)arg2) -> object :

    C++ signature :
        boost::intrusive_ptr<GafferUI::Tool> create(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >,GafferUI::View {lvalue})'''
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
    def handlesTransform (self, *args, **kwargs):
      '''
handlesTransform( (TransformTool)arg1) -> M44f :

    C++ signature :
        Imath_3_1::Matrix44<float> handlesTransform(GafferSceneUI::TransformTool {lvalue})'''
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
isInstanceOf( (ScaleTool)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(GafferSceneUI::ScaleTool {lvalue},IECore::TypeId)

isInstanceOf( (ScaleTool)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(GafferSceneUI::ScaleTool {lvalue},char const*)'''
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
    def registerTool (self, *args, **kwargs):
      '''
registerTool( (object)arg1, (TypeId)arg2, (object)arg3) -> None :

    C++ signature :
        void registerTool(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >,IECore::TypeId,boost::python::api::object)'''
    ...
    def registerType (self, *args, **kwargs):
      '''
registerType( (TypeId)arg1, (str)arg2, (TypeId)arg3) -> None :

    C++ signature :
        void registerType(IECore::TypeId,char const*,IECore::TypeId)'''
    ...
    def registeredTools (self, *args, **kwargs):
      '''
registeredTools( (TypeId)arg1) -> list :

    C++ signature :
        boost::python::list registeredTools(IECore::TypeId)'''
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
    def scale (self, *args, **kwargs):
      '''
scale( (ScaleTool)arg1, (V3f)arg2) -> None :

    C++ signature :
        void scale(GafferSceneUI::ScaleTool {lvalue},Imath_3_1::Vec3<float>)'''
    ...
    def scriptNode (self, *args, **kwargs):
      '''
scriptNode( (Node)arg1) -> object :

    C++ signature :
        Gaffer::ScriptNode* scriptNode(Gaffer::Node {lvalue})'''
    ...
    def selection (self, *args, **kwargs):
      '''
selection( (TransformTool)arg1) -> list :

    C++ signature :
        boost::python::list selection(GafferSceneUI::TransformTool)'''
    ...
    def selectionChangedSignal (self, *args, **kwargs):
      '''
selectionChangedSignal( (TransformTool)arg1) -> SelectionChangedSignal :

    C++ signature :
        Gaffer::Signals::Signal<void (GafferSceneUI::TransformTool&), Gaffer::Signals::DefaultCombiner<void> > {lvalue} selectionChangedSignal(GafferSceneUI::TransformTool {lvalue})'''
    ...
    def selectionEditable (self, *args, **kwargs):
      '''
selectionEditable( (TransformTool)arg1) -> bool :

    C++ signature :
        bool selectionEditable(GafferSceneUI::TransformTool)'''
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
typeId( (ScaleTool)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(GafferSceneUI::ScaleTool {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (ScaleTool)arg1) -> str :

    C++ signature :
        char const* typeName(GafferSceneUI::ScaleTool {lvalue})'''
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
    def view (self, *args, **kwargs):
      '''
view( (Tool)arg1) -> object :

    C++ signature :
        GafferUI::View* view(GafferUI::Tool {lvalue})'''
    ...

def ScaleToolUI (*args):
      '''

'''      
    ...

def ScatterUI (*args):
      '''

'''      
    ...

def SceneChangedSignal (*args):
      '''
__init__(_object*)

'''      
    ...

class SceneChangedSignal:
    def connect (self, *args, **kwargs):
      '''
connect( (SceneChangedSignal)arg1, (object)slot [, (object)scoped=None]) -> object :

    C++ signature :
        boost::python::api::object connect(Gaffer::Signals::Signal<void (GafferSceneUI::ShaderView*), Gaffer::Signals::DefaultCombiner<void> > {lvalue},boost::python::api::object {lvalue} [,boost::python::api::object=None])'''
    ...
    def connectFront (self, *args, **kwargs):
      '''
connectFront( (SceneChangedSignal)arg1, (object)slot [, (object)scoped=None]) -> object :

    C++ signature :
        boost::python::api::object connectFront(Gaffer::Signals::Signal<void (GafferSceneUI::ShaderView*), Gaffer::Signals::DefaultCombiner<void> > {lvalue},boost::python::api::object {lvalue} [,boost::python::api::object=None])'''
    ...
    def disconnectAllSlots (self, *args, **kwargs):
      '''
disconnectAllSlots( (SceneChangedSignal)arg1) -> None :

    C++ signature :
        void disconnectAllSlots(Gaffer::Signals::Signal<void (GafferSceneUI::ShaderView*), Gaffer::Signals::DefaultCombiner<void> > {lvalue})'''
    ...
    def empty (self, *args, **kwargs):
      '''
empty( (SceneChangedSignal)arg1) -> bool :

    C++ signature :
        bool empty(Gaffer::Signals::Signal<void (GafferSceneUI::ShaderView*), Gaffer::Signals::DefaultCombiner<void> > {lvalue})'''
    ...
    def numSlots (self, *args, **kwargs):
      '''
numSlots( (SceneChangedSignal)arg1) -> int :

    C++ signature :
        unsigned long numSlots(Gaffer::Signals::Signal<void (GafferSceneUI::ShaderView*), Gaffer::Signals::DefaultCombiner<void> > {lvalue})'''
    ...

def SceneElementProcessorUI (*args):
      '''

'''      
    ...

def SceneGadget (*args):
      '''
__init__(_object*)

'''      
    ...

class SceneGadget:
    def BinarySignal (self, *args, **kwargs):
      '''None'''
    ...
    def ButtonSignal (self, *args, **kwargs):
      '''None'''
    ...
    def DirtyType (self, *args, **kwargs):
      '''None'''
    ...
    def DragBeginSignal (self, *args, **kwargs):
      '''None'''
    ...
    def DragDropSignal (self, *args, **kwargs):
      '''None'''
    ...
    def EnterLeaveSignal (self, *args, **kwargs):
      '''None'''
    ...
    def IdleSignal (self, *args, **kwargs):
      '''None'''
    ...
    def ImageGadgetSignal (self, *args, **kwargs):
      '''None'''
    ...
    def KeySignal (self, *args, **kwargs):
      '''None'''
    ...
    def Layer (self, *args, **kwargs):
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
    def RenderReason (self, *args, **kwargs):
      '''None'''
    ...
    def State (self, *args, **kwargs):
      '''None'''
    ...
    def UnarySignal (self, *args, **kwargs):
      '''None'''
    ...
    def VisibilityChangedSignal (self, *args, **kwargs):
      '''None'''
    ...
    def _dirty (self, *args, **kwargs):
      '''
_dirty( (Gadget)arg1, (DirtyType)arg2) -> None :

    C++ signature :
        void _dirty(GafferUI::Gadget {lvalue},GafferUI::Gadget::DirtyType)'''
    ...
    def _idleSignalAccessedSignal (self, *args, **kwargs):
      '''
_idleSignalAccessedSignal() -> IdleSignal :

    C++ signature :
        Gaffer::Signals::Signal<void (), Gaffer::Signals::CatchingCombiner<void> > {lvalue} _idleSignalAccessedSignal()'''
    ...
    def acceptsChild (self, *args, **kwargs):
      '''
acceptsChild( (SceneGadget)arg1, (GraphComponent)arg2) -> bool :

    C++ signature :
        bool acceptsChild(GafferSceneUI::SceneGadget,Gaffer::GraphComponent const*)'''
    ...
    def acceptsParent (self, *args, **kwargs):
      '''
acceptsParent( (SceneGadget)arg1, (GraphComponent)arg2) -> bool :

    C++ signature :
        bool acceptsParent(GafferSceneUI::SceneGadget,Gaffer::GraphComponent const*)'''
    ...
    def addChild (self, *args, **kwargs):
      '''
addChild( (GraphComponent)arg1, (GraphComponent)arg2) -> None :

    C++ signature :
        void addChild(Gaffer::GraphComponent {lvalue},Gaffer::GraphComponent {lvalue})'''
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
    def bound (self, *args, **kwargs):
      '''
bound( (SceneGadget)arg1) -> Box3f :

    C++ signature :
        Imath_3_1::Box<Imath_3_1::Vec3<float> > bound(GafferSceneUI::SceneGadget)

bound( (SceneGadget)arg1, (bool)selected [, (PathMatcher)omitted=None]) -> Box3f :

    C++ signature :
        Imath_3_1::Box<Imath_3_1::Vec3<float> > bound(GafferSceneUI::SceneGadget {lvalue},bool [,IECore::PathMatcher const*=None])'''
    ...
    def buttonDoubleClickSignal (self, *args, **kwargs):
      '''
buttonDoubleClickSignal( (Gadget)arg1) -> ButtonSignal :

    C++ signature :
        Gaffer::Signals::Signal<bool (GafferUI::Gadget*, GafferUI::ButtonEvent const&), GafferUI::EventSignalCombiner<bool> > {lvalue} buttonDoubleClickSignal(GafferUI::Gadget {lvalue})'''
    ...
    def buttonPressSignal (self, *args, **kwargs):
      '''
buttonPressSignal( (Gadget)arg1) -> ButtonSignal :

    C++ signature :
        Gaffer::Signals::Signal<bool (GafferUI::Gadget*, GafferUI::ButtonEvent const&), GafferUI::EventSignalCombiner<bool> > {lvalue} buttonPressSignal(GafferUI::Gadget {lvalue})'''
    ...
    def buttonReleaseSignal (self, *args, **kwargs):
      '''
buttonReleaseSignal( (Gadget)arg1) -> ButtonSignal :

    C++ signature :
        Gaffer::Signals::Signal<bool (GafferUI::Gadget*, GafferUI::ButtonEvent const&), GafferUI::EventSignalCombiner<bool> > {lvalue} buttonReleaseSignal(GafferUI::Gadget {lvalue})'''
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
    def dragBeginSignal (self, *args, **kwargs):
      '''
dragBeginSignal( (Gadget)arg1) -> DragBeginSignal :

    C++ signature :
        Gaffer::Signals::Signal<boost::intrusive_ptr<IECore::RunTimeTyped> (GafferUI::Gadget*, GafferUI::DragDropEvent const&), GafferUI::EventSignalCombiner<boost::intrusive_ptr<IECore::RunTimeTyped> > > {lvalue} dragBeginSignal(GafferUI::Gadget {lvalue})'''
    ...
    def dragEndSignal (self, *args, **kwargs):
      '''
dragEndSignal( (Gadget)arg1) -> DragDropSignal :

    C++ signature :
        Gaffer::Signals::Signal<bool (GafferUI::Gadget*, GafferUI::DragDropEvent const&), GafferUI::EventSignalCombiner<bool> > {lvalue} dragEndSignal(GafferUI::Gadget {lvalue})'''
    ...
    def dragEnterSignal (self, *args, **kwargs):
      '''
dragEnterSignal( (Gadget)arg1) -> DragDropSignal :

    C++ signature :
        Gaffer::Signals::Signal<bool (GafferUI::Gadget*, GafferUI::DragDropEvent const&), GafferUI::EventSignalCombiner<bool> > {lvalue} dragEnterSignal(GafferUI::Gadget {lvalue})'''
    ...
    def dragLeaveSignal (self, *args, **kwargs):
      '''
dragLeaveSignal( (Gadget)arg1) -> DragDropSignal :

    C++ signature :
        Gaffer::Signals::Signal<bool (GafferUI::Gadget*, GafferUI::DragDropEvent const&), GafferUI::EventSignalCombiner<bool> > {lvalue} dragLeaveSignal(GafferUI::Gadget {lvalue})'''
    ...
    def dragMoveSignal (self, *args, **kwargs):
      '''
dragMoveSignal( (Gadget)arg1) -> DragDropSignal :

    C++ signature :
        Gaffer::Signals::Signal<bool (GafferUI::Gadget*, GafferUI::DragDropEvent const&), GafferUI::EventSignalCombiner<bool> > {lvalue} dragMoveSignal(GafferUI::Gadget {lvalue})'''
    ...
    def dropSignal (self, *args, **kwargs):
      '''
dropSignal( (Gadget)arg1) -> DragDropSignal :

    C++ signature :
        Gaffer::Signals::Signal<bool (GafferUI::Gadget*, GafferUI::DragDropEvent const&), GafferUI::EventSignalCombiner<bool> > {lvalue} dropSignal(GafferUI::Gadget {lvalue})'''
    ...
    def enabled (self, *args, **kwargs):
      '''
enabled( (Gadget)arg1 [, (Gadget)relativeTo=None]) -> bool :

    C++ signature :
        bool enabled(GafferUI::Gadget {lvalue} [,GafferUI::Gadget*=None])'''
    ...
    def enterSignal (self, *args, **kwargs):
      '''
enterSignal( (Gadget)arg1) -> EnterLeaveSignal :

    C++ signature :
        Gaffer::Signals::Signal<void (GafferUI::Gadget*, GafferUI::ButtonEvent const&), Gaffer::Signals::CatchingCombiner<void> > {lvalue} enterSignal(GafferUI::Gadget {lvalue})'''
    ...
    def fullName (self, *args, **kwargs):
      '''
fullName( (GraphComponent)arg1) -> str :

    C++ signature :
        std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > fullName(Gaffer::GraphComponent {lvalue})'''
    ...
    def fullTransform (self, *args, **kwargs):
      '''
fullTransform( (Gadget)arg1 [, (Gadget)arg2]) -> M44f :

    C++ signature :
        Imath_3_1::Matrix44<float> fullTransform(GafferUI::Gadget {lvalue} [,GafferUI::Gadget const*])'''
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
getContext( (SceneGadget)arg1) -> object :

    C++ signature :
        Gaffer::Context* getContext(GafferSceneUI::SceneGadget {lvalue})'''
    ...
    def getEnabled (self, *args, **kwargs):
      '''
getEnabled( (Gadget)arg1) -> bool :

    C++ signature :
        bool getEnabled(GafferUI::Gadget {lvalue})'''
    ...
    def getHighlighted (self, *args, **kwargs):
      '''
getHighlighted( (Gadget)arg1) -> bool :

    C++ signature :
        bool getHighlighted(GafferUI::Gadget {lvalue})'''
    ...
    def getLayer (self, *args, **kwargs):
      '''
getLayer( (SceneGadget)arg1) -> Layer :

    C++ signature :
        GafferUI::Gadget::Layer getLayer(GafferSceneUI::SceneGadget {lvalue})'''
    ...
    def getMinimumExpansionDepth (self, *args, **kwargs):
      '''
getMinimumExpansionDepth( (SceneGadget)arg1) -> int :

    C++ signature :
        unsigned long getMinimumExpansionDepth(GafferSceneUI::SceneGadget {lvalue})'''
    ...
    def getName (self, *args, **kwargs):
      '''
getName( (GraphComponent)arg1) -> str :

    C++ signature :
        char const* getName(Gaffer::GraphComponent {lvalue})'''
    ...
    def getOpenGLOptions (self, *args, **kwargs):
      '''
getOpenGLOptions( (SceneGadget)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::CompoundObject> getOpenGLOptions(GafferSceneUI::SceneGadget)'''
    ...
    def getPaused (self, *args, **kwargs):
      '''
getPaused( (SceneGadget)arg1) -> bool :

    C++ signature :
        bool getPaused(GafferSceneUI::SceneGadget {lvalue})'''
    ...
    def getRenderer (self, *args, **kwargs):
      '''
getRenderer( (SceneGadget)arg1) -> str :

    C++ signature :
        std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > getRenderer(GafferSceneUI::SceneGadget {lvalue})'''
    ...
    def getScene (self, *args, **kwargs):
      '''
getScene( (SceneGadget)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<GafferScene::ScenePlug> getScene(GafferSceneUI::SceneGadget {lvalue})'''
    ...
    def getSelection (self, *args, **kwargs):
      '''
getSelection( (SceneGadget)arg1) -> PathMatcher :

    C++ signature :
        IECore::PathMatcher getSelection(GafferSceneUI::SceneGadget {lvalue})'''
    ...
    def getSelectionMask (self, *args, **kwargs):
      '''
getSelectionMask( (SceneGadget)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::TypedData<std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > > > getSelectionMask(GafferSceneUI::SceneGadget)'''
    ...
    def getStyle (self, *args, **kwargs):
      '''
getStyle( (Gadget)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<GafferUI::Style> getStyle(GafferUI::Gadget {lvalue})'''
    ...
    def getToolTip (self, *args, **kwargs):
      '''
getToolTip( (SceneGadget)arg1, (LineSegment3f)arg2) -> str :

    C++ signature :
        std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > getToolTip(GafferSceneUI::SceneGadget,IECore::LineSegment<Imath_3_1::Vec3<float> >)'''
    ...
    def getTransform (self, *args, **kwargs):
      '''
getTransform( (Gadget)arg1) -> M44f :

    C++ signature :
        Imath_3_1::Matrix44<float> getTransform(GafferUI::Gadget {lvalue})'''
    ...
    def getVisible (self, *args, **kwargs):
      '''
getVisible( (Gadget)arg1) -> bool :

    C++ signature :
        bool getVisible(GafferUI::Gadget {lvalue})'''
    ...
    def getVisibleSet (self, *args, **kwargs):
      '''
getVisibleSet( (SceneGadget)arg1) -> VisibleSet :

    C++ signature :
        GafferScene::VisibleSet getVisibleSet(GafferSceneUI::SceneGadget {lvalue})'''
    ...
    def idleSignal (self, *args, **kwargs):
      '''
idleSignal() -> IdleSignal :

    C++ signature :
        Gaffer::Signals::Signal<void (), Gaffer::Signals::CatchingCombiner<void> > {lvalue} idleSignal()'''
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
isInstanceOf( (SceneGadget)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(GafferSceneUI::SceneGadget {lvalue},IECore::TypeId)

isInstanceOf( (SceneGadget)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(GafferSceneUI::SceneGadget {lvalue},char const*)'''
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
    def keyPressSignal (self, *args, **kwargs):
      '''
keyPressSignal( (Gadget)arg1) -> KeySignal :

    C++ signature :
        Gaffer::Signals::Signal<bool (GafferUI::Gadget*, GafferUI::KeyEvent const&), GafferUI::EventSignalCombiner<bool> > {lvalue} keyPressSignal(GafferUI::Gadget {lvalue})'''
    ...
    def keyReleaseSignal (self, *args, **kwargs):
      '''
keyReleaseSignal( (Gadget)arg1) -> KeySignal :

    C++ signature :
        Gaffer::Signals::Signal<bool (GafferUI::Gadget*, GafferUI::KeyEvent const&), GafferUI::EventSignalCombiner<bool> > {lvalue} keyReleaseSignal(GafferUI::Gadget {lvalue})'''
    ...
    def keys (self, *args, **kwargs):
      '''
keys( (GraphComponent)arg1) -> list :

    C++ signature :
        boost::python::list keys(Gaffer::GraphComponent {lvalue})'''
    ...
    def leaveSignal (self, *args, **kwargs):
      '''
leaveSignal( (Gadget)arg1) -> EnterLeaveSignal :

    C++ signature :
        Gaffer::Signals::Signal<void (GafferUI::Gadget*, GafferUI::ButtonEvent const&), Gaffer::Signals::CatchingCombiner<void> > {lvalue} leaveSignal(GafferUI::Gadget {lvalue})'''
    ...
    def mouseMoveSignal (self, *args, **kwargs):
      '''
mouseMoveSignal( (Gadget)arg1) -> ButtonSignal :

    C++ signature :
        Gaffer::Signals::Signal<bool (GafferUI::Gadget*, GafferUI::ButtonEvent const&), GafferUI::EventSignalCombiner<bool> > {lvalue} mouseMoveSignal(GafferUI::Gadget {lvalue})'''
    ...
    def nameChangedSignal (self, *args, **kwargs):
      '''
nameChangedSignal( (GraphComponent)arg1) -> NameChangedSignal :

    C++ signature :
        Gaffer::Signals::Signal<void (Gaffer::GraphComponent*, IECore::InternedString), Gaffer::Signals::CatchingCombiner<void> > {lvalue} nameChangedSignal(Gaffer::GraphComponent {lvalue})'''
    ...
    def normalAt (self, *args, **kwargs):
      '''
normalAt( (SceneGadget)arg1, (LineSegment3f)arg2) -> object :

    C++ signature :
        boost::python::api::object normalAt(GafferSceneUI::SceneGadget {lvalue},IECore::LineSegment<Imath_3_1::Vec3<float> >)'''
    ...
    def numWrappedInstances (self, *args, **kwargs):
      '''
numWrappedInstances() -> int :

    C++ signature :
        unsigned long numWrappedInstances()'''
    ...
    def objectAndIntersectionAt (self, *args, **kwargs):
      '''
objectAndIntersectionAt( (SceneGadget)arg1, (LineSegment3f)arg2) -> tuple :

    C++ signature :
        boost::python::tuple objectAndIntersectionAt(GafferSceneUI::SceneGadget {lvalue},IECore::LineSegment<Imath_3_1::Vec3<float> > {lvalue})'''
    ...
    def objectAt (self, *args, **kwargs):
      '''
objectAt( (SceneGadget)arg1, (LineSegment3f)arg2) -> object :

    C++ signature :
        boost::intrusive_ptr<IECore::TypedData<std::vector<IECore::InternedString, std::allocator<IECore::InternedString> > > > objectAt(GafferSceneUI::SceneGadget {lvalue},IECore::LineSegment<Imath_3_1::Vec3<float> > {lvalue})'''
    ...
    def objectsAt (self, *args, **kwargs):
      '''
objectsAt( (SceneGadget)arg1, (V3f)arg2, (V3f)arg3, (PathMatcher)arg4) -> int :

    C++ signature :
        unsigned long objectsAt(GafferSceneUI::SceneGadget {lvalue},Imath_3_1::Vec3<float>,Imath_3_1::Vec3<float>,IECore::PathMatcher {lvalue})'''
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
    def selectionBound (self, *args, **kwargs):
      '''
selectionBound( (SceneGadget)arg1) -> Box3f :

    C++ signature :
        Imath_3_1::Box<Imath_3_1::Vec3<float> > selectionBound(GafferSceneUI::SceneGadget {lvalue})'''
    ...
    def setChild (self, *args, **kwargs):
      '''
setChild( (GraphComponent)arg1, (InternedString)arg2, (GraphComponent)arg3) -> None :

    C++ signature :
        void setChild(Gaffer::GraphComponent {lvalue},IECore::InternedString,Gaffer::GraphComponent {lvalue})'''
    ...
    def setContext (self, *args, **kwargs):
      '''
setContext( (SceneGadget)arg1, (Context)arg2) -> None :

    C++ signature :
        void setContext(GafferSceneUI::SceneGadget {lvalue},Gaffer::Context {lvalue})'''
    ...
    def setEnabled (self, *args, **kwargs):
      '''
setEnabled( (Gadget)arg1, (bool)arg2) -> None :

    C++ signature :
        void setEnabled(GafferUI::Gadget {lvalue},bool)'''
    ...
    def setHighlighted (self, *args, **kwargs):
      '''
setHighlighted( (SceneGadget)arg1, (bool)arg2) -> None :

    C++ signature :
        void setHighlighted(GafferSceneUI::SceneGadget {lvalue},bool)'''
    ...
    def setLayer (self, *args, **kwargs):
      '''
setLayer( (SceneGadget)arg1, (Layer)arg2) -> None :

    C++ signature :
        void setLayer(GafferSceneUI::SceneGadget {lvalue},GafferUI::Gadget::Layer)'''
    ...
    def setMinimumExpansionDepth (self, *args, **kwargs):
      '''
setMinimumExpansionDepth( (SceneGadget)arg1, (int)arg2) -> None :

    C++ signature :
        void setMinimumExpansionDepth(GafferSceneUI::SceneGadget {lvalue},unsigned long)'''
    ...
    def setName (self, *args, **kwargs):
      '''
setName( (GraphComponent)arg1, (InternedString)arg2) -> str :

    C++ signature :
        char const* setName(Gaffer::GraphComponent {lvalue},IECore::InternedString)'''
    ...
    def setOpenGLOptions (self, *args, **kwargs):
      '''
setOpenGLOptions( (SceneGadget)arg1, (CompoundObject)arg2) -> None :

    C++ signature :
        void setOpenGLOptions(GafferSceneUI::SceneGadget {lvalue},IECore::CompoundObject const*)'''
    ...
    def setPaused (self, *args, **kwargs):
      '''
setPaused( (SceneGadget)arg1, (bool)arg2) -> None :

    C++ signature :
        void setPaused(GafferSceneUI::SceneGadget {lvalue},bool)'''
    ...
    def setRenderer (self, *args, **kwargs):
      '''
setRenderer( (SceneGadget)arg1, (InternedString)arg2) -> None :

    C++ signature :
        void setRenderer(GafferSceneUI::SceneGadget {lvalue},IECore::InternedString)'''
    ...
    def setScene (self, *args, **kwargs):
      '''
setScene( (SceneGadget)arg1, (ScenePlug)arg2) -> None :

    C++ signature :
        void setScene(GafferSceneUI::SceneGadget {lvalue},GafferScene::ScenePlug {lvalue})'''
    ...
    def setSelection (self, *args, **kwargs):
      '''
setSelection( (SceneGadget)arg1, (PathMatcher)arg2) -> None :

    C++ signature :
        void setSelection(GafferSceneUI::SceneGadget {lvalue},IECore::PathMatcher)'''
    ...
    def setSelectionMask (self, *args, **kwargs):
      '''
setSelectionMask( (SceneGadget)arg1, (StringVectorData)arg2) -> None :

    C++ signature :
        void setSelectionMask(GafferSceneUI::SceneGadget {lvalue},IECore::TypedData<std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > > const*)'''
    ...
    def setStyle (self, *args, **kwargs):
      '''
setStyle( (Gadget)arg1, (object)arg2) -> None :

    C++ signature :
        void setStyle(GafferUI::Gadget {lvalue},boost::intrusive_ptr<GafferUI::Style const>)'''
    ...
    def setToolTip (self, *args, **kwargs):
      '''
setToolTip( (Gadget)arg1, (object)arg2) -> None :

    C++ signature :
        void setToolTip(GafferUI::Gadget {lvalue},std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)'''
    ...
    def setTransform (self, *args, **kwargs):
      '''
setTransform( (Gadget)arg1, (M44f)arg2) -> None :

    C++ signature :
        void setTransform(GafferUI::Gadget {lvalue},Imath_3_1::Matrix44<float>)'''
    ...
    def setVisible (self, *args, **kwargs):
      '''
setVisible( (Gadget)arg1, (bool)arg2) -> None :

    C++ signature :
        void setVisible(GafferUI::Gadget {lvalue},bool)'''
    ...
    def setVisibleSet (self, *args, **kwargs):
      '''
setVisibleSet( (SceneGadget)arg1, (VisibleSet)arg2) -> None :

    C++ signature :
        void setVisibleSet(GafferSceneUI::SceneGadget {lvalue},GafferScene::VisibleSet)'''
    ...
    def snapshotToFile (self, *args, **kwargs):
      '''
snapshotToFile( (SceneGadget)arg1, (object)fileName [, (Box2f)resolutionGate=Box2f(V2f(3.40282347e+38, 3.40282347e+38), V2f(-3.40282347e+38, -3.40282347e+38)) [, (CompoundData)metadata=None]]) -> None :

    C++ signature :
        void snapshotToFile(GafferSceneUI::SceneGadget {lvalue},std::filesystem::__cxx11::path [,Imath_3_1::Box<Imath_3_1::Vec2<float> >=Box2f(V2f(3.40282347e+38, 3.40282347e+38), V2f(-3.40282347e+38, -3.40282347e+38)) [,IECore::CompoundData const*=None]])'''
    ...
    def state (self, *args, **kwargs):
      '''
state( (SceneGadget)arg1) -> State :

    C++ signature :
        GafferSceneUI::SceneGadget::State state(GafferSceneUI::SceneGadget {lvalue})'''
    ...
    def stateChangedSignal (self, *args, **kwargs):
      '''
stateChangedSignal( (SceneGadget)arg1) -> ImageGadgetSignal :

    C++ signature :
        Gaffer::Signals::Signal<void (GafferSceneUI::SceneGadget*), Gaffer::Signals::DefaultCombiner<void> > {lvalue} stateChangedSignal(GafferSceneUI::SceneGadget {lvalue})'''
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
    def style (self, *args, **kwargs):
      '''
style( (Gadget)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<GafferUI::Style> style(GafferUI::Gadget {lvalue})'''
    ...
    def transformedBound (self, *args, **kwargs):
      '''
transformedBound( (Gadget)arg1) -> Box3f :

    C++ signature :
        Imath_3_1::Box<Imath_3_1::Vec3<float> > transformedBound(GafferUI::Gadget {lvalue})

transformedBound( (Gadget)arg1, (Gadget)arg2) -> Box3f :

    C++ signature :
        Imath_3_1::Box<Imath_3_1::Vec3<float> > transformedBound(GafferUI::Gadget {lvalue},GafferUI::Gadget const*)'''
    ...
    def typeId (self, *args, **kwargs):
      '''
typeId( (SceneGadget)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(GafferSceneUI::SceneGadget {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (SceneGadget)arg1) -> str :

    C++ signature :
        char const* typeName(GafferSceneUI::SceneGadget {lvalue})'''
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
    def visibilityChangedSignal (self, *args, **kwargs):
      '''
visibilityChangedSignal( (Gadget)arg1) -> VisibilityChangedSignal :

    C++ signature :
        Gaffer::Signals::Signal<void (GafferUI::Gadget*), Gaffer::Signals::CatchingCombiner<void> > {lvalue} visibilityChangedSignal(GafferUI::Gadget {lvalue})'''
    ...
    def visible (self, *args, **kwargs):
      '''
visible( (Gadget)arg1 [, (Gadget)relativeTo=None]) -> bool :

    C++ signature :
        bool visible(GafferUI::Gadget {lvalue} [,GafferUI::Gadget*=None])'''
    ...
    def waitForCompletion (self, *args, **kwargs):
      '''
waitForCompletion( (SceneGadget)arg1) -> None :

    C++ signature :
        void waitForCompletion(GafferSceneUI::SceneGadget {lvalue})'''
    ...
    def wheelSignal (self, *args, **kwargs):
      '''
wheelSignal( (Gadget)arg1) -> ButtonSignal :

    C++ signature :
        Gaffer::Signals::Signal<bool (GafferUI::Gadget*, GafferUI::ButtonEvent const&), GafferUI::EventSignalCombiner<bool> > {lvalue} wheelSignal(GafferUI::Gadget {lvalue})'''
    ...

def SceneHierarchy (*args):
      '''

'''      
    ...

class SceneHierarchy:
    def Settings (name, script):
      '''None'''
    ...
    def _Editor__contextChanged (self, context, key):
      '''None'''
    ...
    def _Editor__enter (self, widget):
      '''None'''
    ...
    def _Editor__leave (self, widget):
      '''None'''
    ...
    def _Editor__namesToCreators (self, *args, **kwargs):
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
    def _Editor__setContextInternal (self, context, callUpdate):
      '''None'''
    ...
    def _HierarchyView__contextMenuSignal (self, widget):
      '''None'''
    ...
    def _HierarchyView__copySelectedPaths (self, *unused):
      '''None'''
    ...
    def _HierarchyView__expansionChanged (self, pathListing):
      '''None'''
    ...
    def _HierarchyView__frameSelectedPaths (self):
      '''None'''
    ...
    def _HierarchyView__keyPressSignal (self, widget, event):
      '''None'''
    ...
    def _HierarchyView__plugParentChanged (self, plug, oldParent):
      '''None'''
    ...
    def _HierarchyView__selectionChanged (self, pathListing):
      '''None'''
    ...
    def _HierarchyView__setPathListingPath (self):
      '''None'''
    ...
    def _HierarchyView__transferExpansionFromContext (self):
      '''None'''
    ...
    def _HierarchyView__transferSelectionFromContext (self):
      '''None'''
    ...
    def _NodeSetEditor__dirtyTitle (self):
      '''None'''
    ...
    def _NodeSetEditor__lazyUpdate (self):
      '''None'''
    ...
    def _NodeSetEditor__membersChanged (self, set, member):
      '''None'''
    ...
    def _NodeSetEditor__nameChanged (self, node, oldName):
      '''None'''
    ...
    def _NodeSetEditor__setNodeSetInternal (self, nodeSet, callUpdateFromSet):
      '''None'''
    ...
    def _Widget__applyQWidgetStyleClasses (self):
      '''None'''
    ...
    def _Widget__ensureEventFilter (self):
      '''None'''
    ...
    def _Widget__ensureFocusChangedConnection ():
      '''None'''
    ...
    def _Widget__ensureMouseTracking (self):
      '''None'''
    ...
    def _Widget__focusChanged (oldWidget, newWidget):
      '''None'''
    ...
    def _Widget__focusChangedConnected (self, *args, **kwargs):
      '''bool(x) -> bool

Returns True when the argument x is true, False otherwise.
The builtins True and False are the only two instances of the class bool.
The class bool is a subclass of the class int, and cannot be subclassed.'''
    ...
    def _Widget__focusChangedSignal (self, *args, **kwargs):
      '''None'''
    ...
    def _Widget__initNesting ():
      '''None'''
    ...
    def _Widget__keyMapping (self, *args, **kwargs):
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
    def _Widget__parentStack (self, *args, **kwargs):
      '''Built-in mutable sequence.

If no argument is given, the constructor creates a new empty list.
The argument must be an iterable if specified.'''
    ...
    def _Widget__propagateDisplayTransformChange (self):
      '''None'''
    ...
    def _Widget__qtWidgetOwners (self, *args, **kwargs):
      ''' Mapping class that references keys weakly.

    Entries in the dictionary will be discarded when there is no
    longer a strong reference to the key. This can be used to
    associate additional data with an object owned by other parts of
    an application without adding attributes to those objects. This
    can be especially useful with objects that override attribute
    accesses.
    '''
    ...
    def _Widget__styleClassName ():
      '''None'''
    ...
    def _applyVisibility (self):
      '''None'''
    ...
    def _buttons (qtButtons):
      '''None'''
    ...
    def _contextChangedConnection (self):
      '''None'''
    ...
    def _disconnectTrackedConnections (self, *args, **kwargs):
      '''
_disconnectTrackedConnections( (Trackable)arg1) -> None :

    C++ signature :
        void _disconnectTrackedConnections(Gaffer::Signals::Trackable {lvalue})'''
    ...
    def _displayTransformChanged (self):
      '''None'''
    ...
    def _doPendingUpdate (self):
      '''None'''
    ...
    def _key (qtKey):
      '''None'''
    ...
    def _lastAddedNode (self):
      '''None'''
    ...
    def _modifiers (qtModifiers):
      '''None'''
    ...
    def _owner (qtWidget):
      '''None'''
    ...
    def _popParent ():
      '''None'''
    ...
    def _postConstructor (self):
      '''None'''
    ...
    def _pushParent (container):
      '''None'''
    ...
    def _qtColor (color):
      '''None'''
    ...
    def _qtWidget (self):
      '''None'''
    ...
    def _repolish (self, qtWidget=None):
      '''None'''
    ...
    def _setStyleSheet (self):
      '''None'''
    ...
    def _titleFormat (self):
      '''None'''
    ...
    def _updateFromContext (self, modifiedItems):
      '''None'''
    ...
    def _updateFromSet (self):
      '''None'''
    ...
    def acquire (node, floating=None):
      '''None'''
    ...
    def ancestor (self, type):
      '''None'''
    ...
    def bound (self, relativeTo=None):
      '''None'''
    ...
    def buttonDoubleClickSignal (self):
      '''None'''
    ...
    def buttonPressSignal (self):
      '''None'''
    ...
    def buttonReleaseSignal (self):
      '''None'''
    ...
    def contextMenuSignal (self):
      '''None'''
    ...
    def create (name, scriptNode):
      '''None'''
    ...
    def currentModifiers ():
      '''None'''
    ...
    def displayTransform (self):
      '''None'''
    ...
    def dragBeginSignal (self):
      '''None'''
    ...
    def dragEndSignal (self):
      '''None'''
    ...
    def dragEnterSignal (self):
      '''None'''
    ...
    def dragLeaveSignal (self):
      '''None'''
    ...
    def dragMoveSignal (self):
      '''None'''
    ...
    def dropSignal (self):
      '''None'''
    ...
    def enabled (self, relativeTo=None):
      '''None'''
    ...
    def enterSignal (self):
      '''None'''
    ...
    def focusChangedSignal ():
      '''None'''
    ...
    def getContext (self):
      '''None'''
    ...
    def getDisplayTransform (self):
      '''None'''
    ...
    def getEnabled (self):
      '''None'''
    ...
    def getHighlighted (self):
      '''None'''
    ...
    def getNodeSet (self):
      '''None'''
    ...
    def getTitle (self):
      '''None'''
    ...
    def getToolTip (self):
      '''None'''
    ...
    def getVisible (self):
      '''None'''
    ...
    def identityDisplayTransform (x):
      '''None'''
    ...
    def instanceCreatedSignal ():
      '''None'''
    ...
    def isAncestorOf (self, other):
      '''None'''
    ...
    def keyPressSignal (self):
      '''None'''
    ...
    def keyReleaseSignal (self):
      '''None'''
    ...
    def leaveSignal (self):
      '''None'''
    ...
    def mouseMoveSignal (self):
      '''None'''
    ...
    def mousePosition (relativeTo=None):
      '''None'''
    ...
    def nodeSetChangedSignal (self):
      '''None'''
    ...
    def parent (self):
      '''None'''
    ...
    def parentChangedSignal (self):
      '''None'''
    ...
    def registerType (name, creator):
      '''None'''
    ...
    def reveal (self):
      '''None'''
    ...
    def scene (self):
      '''None'''
    ...
    def scriptNode (self):
      '''None'''
    ...
    def setContext (self, context):
      '''None'''
    ...
    def setDisplayTransform (self, displayTransform):
      '''None'''
    ...
    def setEnabled (self, enabled):
      '''None'''
    ...
    def setHighlighted (self, highlighted):
      '''None'''
    ...
    def setNodeSet (self, nodeSet):
      '''None'''
    ...
    def setTitle (self, title):
      '''None'''
    ...
    def setToolTip (self, toolTip):
      '''None'''
    ...
    def setVisible (self, visible):
      '''None'''
    ...
    def size (self):
      '''None'''
    ...
    def titleChangedSignal (self):
      '''None'''
    ...
    def types ():
      '''None'''
    ...
    def visibilityChangedSignal (self):
      '''None'''
    ...
    def visible (self, relativeTo=None):
      '''None'''
    ...
    def wheelSignal (self):
      '''None'''
    ...
    def widgetAt (position, widgetType=None):
      '''None'''
    ...

def SceneHistoryUI (*args):
      '''

'''      
    ...

def SceneInspector (*args):
      '''

'''      
    ...

class SceneInspector:
    def Diff (*args, **kw):
      '''None'''
    ...
    def DiffColumn (*args, **kw):
      '''None'''
    ...
    def DiffRow (*args, **kw):
      '''None'''
    ...
    def HistorySection (*args, **kw):
      '''None'''
    ...
    def Inspector ():
      '''None'''
    ...
    def LocationSection (*args, **kw):
      '''None'''
    ...
    def Row (*args, **kw):
      '''None'''
    ...
    def Section (*args, **kw):
      '''None'''
    ...
    def SetsSection (*args, **kw):
      '''None'''
    ...
    def Settings (name, script):
      '''None'''
    ...
    def SideBySideDiff (*args, **kw):
      '''None'''
    ...
    def Target (scene, path):
      '''None'''
    ...
    def TextDiff (*args, **kw):
      '''None'''
    ...
    def _Editor__contextChanged (self, context, key):
      '''None'''
    ...
    def _Editor__enter (self, widget):
      '''None'''
    ...
    def _Editor__leave (self, widget):
      '''None'''
    ...
    def _Editor__namesToCreators (self, *args, **kwargs):
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
    def _Editor__setContextInternal (self, context, callUpdate):
      '''None'''
    ...
    def _NodeSetEditor__dirtyTitle (self):
      '''None'''
    ...
    def _NodeSetEditor__lazyUpdate (self):
      '''None'''
    ...
    def _NodeSetEditor__membersChanged (self, set, member):
      '''None'''
    ...
    def _NodeSetEditor__nameChanged (self, node, oldName):
      '''None'''
    ...
    def _NodeSetEditor__setNodeSetInternal (self, nodeSet, callUpdateFromSet):
      '''None'''
    ...
    def _SceneInspector__SectionRegistration (section, tab):
      '''SectionRegistration(section, tab)'''
    ...
    def _SceneInspector__plugDirtied (self, plug):
      '''None'''
    ...
    def _SceneInspector__plugParentChanged (self, plug, oldParent):
      '''None'''
    ...
    def _SceneInspector__sectionRegistrations (self, *args, **kwargs):
      '''Built-in mutable sequence.

If no argument is given, the constructor creates a new empty list.
The argument must be an iterable if specified.'''
    ...
    def _SceneInspector__update (self):
      '''None'''
    ...
    def _SceneInspector__updateLazily (self):
      '''None'''
    ...
    def _Widget__applyQWidgetStyleClasses (self):
      '''None'''
    ...
    def _Widget__ensureEventFilter (self):
      '''None'''
    ...
    def _Widget__ensureFocusChangedConnection ():
      '''None'''
    ...
    def _Widget__ensureMouseTracking (self):
      '''None'''
    ...
    def _Widget__focusChanged (oldWidget, newWidget):
      '''None'''
    ...
    def _Widget__focusChangedConnected (self, *args, **kwargs):
      '''bool(x) -> bool

Returns True when the argument x is true, False otherwise.
The builtins True and False are the only two instances of the class bool.
The class bool is a subclass of the class int, and cannot be subclassed.'''
    ...
    def _Widget__focusChangedSignal (self, *args, **kwargs):
      '''None'''
    ...
    def _Widget__initNesting ():
      '''None'''
    ...
    def _Widget__keyMapping (self, *args, **kwargs):
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
    def _Widget__parentStack (self, *args, **kwargs):
      '''Built-in mutable sequence.

If no argument is given, the constructor creates a new empty list.
The argument must be an iterable if specified.'''
    ...
    def _Widget__propagateDisplayTransformChange (self):
      '''None'''
    ...
    def _Widget__qtWidgetOwners (self, *args, **kwargs):
      ''' Mapping class that references keys weakly.

    Entries in the dictionary will be discarded when there is no
    longer a strong reference to the key. This can be used to
    associate additional data with an object owned by other parts of
    an application without adding attributes to those objects. This
    can be especially useful with objects that override attribute
    accesses.
    '''
    ...
    def _Widget__styleClassName ():
      '''None'''
    ...
    def _applyVisibility (self):
      '''None'''
    ...
    def _buttons (qtButtons):
      '''None'''
    ...
    def _contextChangedConnection (self):
      '''None'''
    ...
    def _disconnectTrackedConnections (self, *args, **kwargs):
      '''
_disconnectTrackedConnections( (Trackable)arg1) -> None :

    C++ signature :
        void _disconnectTrackedConnections(Gaffer::Signals::Trackable {lvalue})'''
    ...
    def _displayTransformChanged (self):
      '''None'''
    ...
    def _doPendingUpdate (self):
      '''None'''
    ...
    def _key (qtKey):
      '''None'''
    ...
    def _lastAddedNode (self):
      '''None'''
    ...
    def _modifiers (qtModifiers):
      '''None'''
    ...
    def _owner (qtWidget):
      '''None'''
    ...
    def _popParent ():
      '''None'''
    ...
    def _postConstructor (self):
      '''None'''
    ...
    def _pushParent (container):
      '''None'''
    ...
    def _qtColor (color):
      '''None'''
    ...
    def _qtWidget (self):
      '''None'''
    ...
    def _repolish (self, qtWidget=None):
      '''None'''
    ...
    def _setStyleSheet (self):
      '''None'''
    ...
    def _titleFormat (self):
      '''None'''
    ...
    def _updateFromContext (self, modifiedItems):
      '''None'''
    ...
    def _updateFromSet (self):
      '''None'''
    ...
    def acquire (node, floating=None):
      '''None'''
    ...
    def ancestor (self, type):
      '''None'''
    ...
    def bound (self, relativeTo=None):
      '''None'''
    ...
    def buttonDoubleClickSignal (self):
      '''None'''
    ...
    def buttonPressSignal (self):
      '''None'''
    ...
    def buttonReleaseSignal (self):
      '''None'''
    ...
    def contextMenuSignal (self):
      '''None'''
    ...
    def create (name, scriptNode):
      '''None'''
    ...
    def currentModifiers ():
      '''None'''
    ...
    def displayTransform (self):
      '''None'''
    ...
    def dragBeginSignal (self):
      '''None'''
    ...
    def dragEndSignal (self):
      '''None'''
    ...
    def dragEnterSignal (self):
      '''None'''
    ...
    def dragLeaveSignal (self):
      '''None'''
    ...
    def dragMoveSignal (self):
      '''None'''
    ...
    def dropSignal (self):
      '''None'''
    ...
    def enabled (self, relativeTo=None):
      '''None'''
    ...
    def enterSignal (self):
      '''None'''
    ...
    def focusChangedSignal ():
      '''None'''
    ...
    def getContext (self):
      '''None'''
    ...
    def getDisplayTransform (self):
      '''None'''
    ...
    def getEnabled (self):
      '''None'''
    ...
    def getHighlighted (self):
      '''None'''
    ...
    def getNodeSet (self):
      '''None'''
    ...
    def getTargetPaths (self):
      '''None'''
    ...
    def getTitle (self):
      '''None'''
    ...
    def getToolTip (self):
      '''None'''
    ...
    def getVisible (self):
      '''None'''
    ...
    def identityDisplayTransform (x):
      '''None'''
    ...
    def instanceCreatedSignal ():
      '''None'''
    ...
    def isAncestorOf (self, other):
      '''None'''
    ...
    def keyPressSignal (self):
      '''None'''
    ...
    def keyReleaseSignal (self):
      '''None'''
    ...
    def leaveSignal (self):
      '''None'''
    ...
    def mouseMoveSignal (self):
      '''None'''
    ...
    def mousePosition (relativeTo=None):
      '''None'''
    ...
    def nodeSetChangedSignal (self):
      '''None'''
    ...
    def parent (self):
      '''None'''
    ...
    def parentChangedSignal (self):
      '''None'''
    ...
    def registerSection (section, tab):
      '''None'''
    ...
    def registerType (name, creator):
      '''None'''
    ...
    def reveal (self):
      '''None'''
    ...
    def scriptNode (self):
      '''None'''
    ...
    def setContext (self, context):
      '''None'''
    ...
    def setDisplayTransform (self, displayTransform):
      '''None'''
    ...
    def setEnabled (self, enabled):
      '''None'''
    ...
    def setHighlighted (self, highlighted):
      '''None'''
    ...
    def setNodeSet (self, nodeSet):
      '''None'''
    ...
    def setTargetPaths (self, paths):
      '''None'''
    ...
    def setTitle (self, title):
      '''None'''
    ...
    def setToolTip (self, toolTip):
      '''None'''
    ...
    def setVisible (self, visible):
      '''None'''
    ...
    def size (self):
      '''None'''
    ...
    def titleChangedSignal (self):
      '''None'''
    ...
    def types ():
      '''None'''
    ...
    def visibilityChangedSignal (self):
      '''None'''
    ...
    def visible (self, relativeTo=None):
      '''None'''
    ...
    def wheelSignal (self):
      '''None'''
    ...
    def widgetAt (position, widgetType=None):
      '''None'''
    ...

def SceneNodeUI (*args):
      '''

'''      
    ...

def ScenePathPlugValueWidget (*args):
      '''

'''      
    ...

class ScenePathPlugValueWidget:
    def MultiplePlugTypesError (self, *args, **kwargs):
      '''None'''
    ...
    def MultiplePlugsError (self, *args, **kwargs):
      '''None'''
    ...
    def MultipleWidgetCreatorsError (self, *args, **kwargs):
      '''None'''
    ...
    def _PathPlugValueWidget__buttonClicked (self, widget):
      '''None'''
    ...
    def _PathPlugValueWidget__metadataValue (self, name):
      '''None'''
    ...
    def _PathPlugValueWidget__setPlugValue (self, *args):
      '''None'''
    ...
    def _PlugValueWidget__applyPreset (self, presetName, *unused):
      '''None'''
    ...
    def _PlugValueWidget__applyReadOnly (self, readOnly):
      '''None'''
    ...
    def _PlugValueWidget__applyUserDefaults (self):
      '''None'''
    ...
    def _PlugValueWidget__auxiliaryPlugDirtied (self, plug):
      '''None'''
    ...
    def _PlugValueWidget__buttonPress (self, widget, event, buttonMask):
      '''None'''
    ...
    def _PlugValueWidget__callLegacyUpdateMethods (self):
      '''None'''
    ...
    def _PlugValueWidget__callUpdateFromValues (self):
      '''None'''
    ...
    def _PlugValueWidget__contextChanged (self, context, key):
      '''None'''
    ...
    def _PlugValueWidget__contextMenu (self, *unused):
      '''None'''
    ...
    def _PlugValueWidget__copyValue (self):
      '''None'''
    ...
    def _PlugValueWidget__creator (plug, typeMetadata):
      '''None'''
    ...
    def _PlugValueWidget__defaultContext (graphComponent):
      '''None'''
    ...
    def _PlugValueWidget__dragEnter (self, widget, event):
      '''None'''
    ...
    def _PlugValueWidget__dragLeave (self, widget, event):
      '''None'''
    ...
    def _PlugValueWidget__drop (self, widget, event):
      '''None'''
    ...
    def _PlugValueWidget__editInputs (self):
      '''None'''
    ...
    def _PlugValueWidget__fallbackContext (self, *args, **kwargs):
      '''None'''
    ...
    def _PlugValueWidget__nodeMetadataChanged (self, nodeTypeId, key, node):
      '''None'''
    ...
    def _PlugValueWidget__plugDirtied (self, plug):
      '''None'''
    ...
    def _PlugValueWidget__plugInputChanged (self, plug):
      '''None'''
    ...
    def _PlugValueWidget__plugMetadataChanged (self, plug, key, reason):
      '''None'''
    ...
    def _PlugValueWidget__plugTypesToCreators (self, *args, **kwargs):
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
    def _PlugValueWidget__popupMenuSignal (self, *args, **kwargs):
      '''None'''
    ...
    def _PlugValueWidget__presetsSubMenu (self):
      '''None'''
    ...
    def _PlugValueWidget__removeInputs (self):
      '''None'''
    ...
    def _PlugValueWidget__setPlugsInternal (self, plugs, callUpdateMethods):
      '''None'''
    ...
    def _PlugValueWidget__setValues (self, values):
      '''None'''
    ...
    def _PlugValueWidget__updateContextConnection (self):
      '''None'''
    ...
    def _PlugValueWidget__updateFromValuesInBackground (self, plugs, auxiliaryPlugs):
      '''None'''
    ...
    def _PlugValueWidget__updateFromValuesInBackgroundPlug (self, *args, **kwargs):
      '''None'''
    ...
    def _PlugValueWidget__updateFromValuesInBackgroundPostCall (self, *args, **kwargs):
      '''None'''
    ...
    def _PlugValueWidget__updateFromValuesInBackgroundPreCall (self, *args, **kwargs):
      '''None'''
    ...
    def _ScenePathPlugValueWidget__focusChanged (self, scriptNode, node):
      '''None'''
    ...
    def _ScenePathPlugValueWidget__scenePlug (self, plug):
      '''None'''
    ...
    def _Widget__applyQWidgetStyleClasses (self):
      '''None'''
    ...
    def _Widget__ensureEventFilter (self):
      '''None'''
    ...
    def _Widget__ensureFocusChangedConnection ():
      '''None'''
    ...
    def _Widget__ensureMouseTracking (self):
      '''None'''
    ...
    def _Widget__focusChanged (oldWidget, newWidget):
      '''None'''
    ...
    def _Widget__focusChangedConnected (self, *args, **kwargs):
      '''bool(x) -> bool

Returns True when the argument x is true, False otherwise.
The builtins True and False are the only two instances of the class bool.
The class bool is a subclass of the class int, and cannot be subclassed.'''
    ...
    def _Widget__focusChangedSignal (self, *args, **kwargs):
      '''None'''
    ...
    def _Widget__initNesting ():
      '''None'''
    ...
    def _Widget__keyMapping (self, *args, **kwargs):
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
    def _Widget__parentStack (self, *args, **kwargs):
      '''Built-in mutable sequence.

If no argument is given, the constructor creates a new empty list.
The argument must be an iterable if specified.'''
    ...
    def _Widget__propagateDisplayTransformChange (self):
      '''None'''
    ...
    def _Widget__qtWidgetOwners (self, *args, **kwargs):
      ''' Mapping class that references keys weakly.

    Entries in the dictionary will be discarded when there is no
    longer a strong reference to the key. This can be used to
    associate additional data with an object owned by other parts of
    an application without adding attributes to those objects. This
    can be especially useful with objects that override attribute
    accesses.
    '''
    ...
    def _Widget__styleClassName ():
      '''None'''
    ...
    def _addPopupMenu (self, widget=None, buttons=GafferUI._GafferUI.Buttons.Right):
      '''None'''
    ...
    def _applyVisibility (self):
      '''None'''
    ...
    def _auxiliaryPlugs (self, plug):
      '''None'''
    ...
    def _blockedUpdateFromValues (self):
      '''None'''
    ...
    def _buttons (qtButtons):
      '''None'''
    ...
    def _convertValue (self, value):
      '''None'''
    ...
    def _disconnectTrackedConnections (self, *args, **kwargs):
      '''
_disconnectTrackedConnections( (Trackable)arg1) -> None :

    C++ signature :
        void _disconnectTrackedConnections(Gaffer::Signals::Trackable {lvalue})'''
    ...
    def _displayTransformChanged (self):
      '''None'''
    ...
    def _editable (self, canEditAnimation=False):
      '''None'''
    ...
    def _key (qtKey):
      '''None'''
    ...
    def _modifiers (qtModifiers):
      '''None'''
    ...
    def _owner (qtWidget):
      '''None'''
    ...
    def _pathChooserDialogue (self):
      '''None'''
    ...
    def _plugConnections (self):
      '''None'''
    ...
    def _popParent ():
      '''None'''
    ...
    def _popupMenuDefinition (self):
      '''None'''
    ...
    def _postConstructor (self):
      '''None'''
    ...
    def _pushParent (container):
      '''None'''
    ...
    def _qtColor (color):
      '''None'''
    ...
    def _qtWidget (self):
      '''None'''
    ...
    def _repolish (self, qtWidget=None):
      '''None'''
    ...
    def _requestUpdateFromValues (self, lazy=True):
      '''None'''
    ...
    def _setPlugFromPath (self, path):
      '''None'''
    ...
    def _setStyleSheet (self):
      '''None'''
    ...
    def _updateFromEditable (self):
      '''None'''
    ...
    def _updateFromMetadata (self):
      '''None'''
    ...
    def _updateFromValues (self, values, exception):
      '''None'''
    ...
    def _valuesDependOnContext (self):
      '''None'''
    ...
    def _valuesForUpdate (plugs, auxiliaryPlugs):
      '''None'''
    ...
    def acquire (plug):
      '''None'''
    ...
    def ancestor (self, type):
      '''None'''
    ...
    def bound (self, relativeTo=None):
      '''None'''
    ...
    def buttonDoubleClickSignal (self):
      '''None'''
    ...
    def buttonPressSignal (self):
      '''None'''
    ...
    def buttonReleaseSignal (self):
      '''None'''
    ...
    def childPlugValueWidget (self, childPlug):
      '''None'''
    ...
    def contextMenuSignal (self):
      '''None'''
    ...
    def create (plugs, typeMetadata='plugValueWidget:type'):
      '''None'''
    ...
    def currentModifiers ():
      '''None'''
    ...
    def displayTransform (self):
      '''None'''
    ...
    def dragBeginSignal (self):
      '''None'''
    ...
    def dragEndSignal (self):
      '''None'''
    ...
    def dragEnterSignal (self):
      '''None'''
    ...
    def dragLeaveSignal (self):
      '''None'''
    ...
    def dragMoveSignal (self):
      '''None'''
    ...
    def dropSignal (self):
      '''None'''
    ...
    def enabled (self, relativeTo=None):
      '''None'''
    ...
    def enterSignal (self):
      '''None'''
    ...
    def focusChangedSignal ():
      '''None'''
    ...
    def getContext (self):
      '''None'''
    ...
    def getDisplayTransform (self):
      '''None'''
    ...
    def getEnabled (self):
      '''None'''
    ...
    def getHighlighted (self):
      '''None'''
    ...
    def getPlug (self):
      '''None'''
    ...
    def getPlugs (self):
      '''None'''
    ...
    def getToolTip (self):
      '''None'''
    ...
    def getVisible (self):
      '''None'''
    ...
    def hasLabel (self):
      '''None'''
    ...
    def identityDisplayTransform (x):
      '''None'''
    ...
    def isAncestorOf (self, other):
      '''None'''
    ...
    def keyPressSignal (self):
      '''None'''
    ...
    def keyReleaseSignal (self):
      '''None'''
    ...
    def leaveSignal (self):
      '''None'''
    ...
    def mouseMoveSignal (self):
      '''None'''
    ...
    def mousePosition (relativeTo=None):
      '''None'''
    ...
    def parent (self):
      '''None'''
    ...
    def parentChangedSignal (self):
      '''None'''
    ...
    def path (self):
      '''None'''
    ...
    def pathWidget (self):
      '''None'''
    ...
    def popupMenuSignal ():
      '''None'''
    ...
    def registerType (plugClassOrTypeId, creator):
      '''None'''
    ...
    def reveal (self):
      '''None'''
    ...
    def setContext (self, context):
      '''None'''
    ...
    def setDisplayTransform (self, displayTransform):
      '''None'''
    ...
    def setEnabled (self, enabled):
      '''None'''
    ...
    def setHighlighted (self, highlighted):
      '''None'''
    ...
    def setPlug (self, plug):
      '''None'''
    ...
    def setPlugs (self, plugs):
      '''None'''
    ...
    def setToolTip (self, toolTip):
      '''None'''
    ...
    def setVisible (self, visible):
      '''None'''
    ...
    def size (self):
      '''None'''
    ...
    def visibilityChangedSignal (self):
      '''None'''
    ...
    def visible (self, relativeTo=None):
      '''None'''
    ...
    def wheelSignal (self):
      '''None'''
    ...
    def widgetAt (position, widgetType=None):
      '''None'''
    ...

def SceneProcessorUI (*args):
      '''

'''      
    ...

def SceneReaderPathPreview (*args):
      '''

'''      
    ...

class SceneReaderPathPreview:
    def _PathPreviewWidget__namesToCreators (self, *args, **kwargs):
      '''Built-in mutable sequence.

If no argument is given, the constructor creates a new empty list.
The argument must be an iterable if specified.'''
    ...
    def _PathPreviewWidget__pathChanged (self, path):
      '''None'''
    ...
    def _Widget__applyQWidgetStyleClasses (self):
      '''None'''
    ...
    def _Widget__ensureEventFilter (self):
      '''None'''
    ...
    def _Widget__ensureFocusChangedConnection ():
      '''None'''
    ...
    def _Widget__ensureMouseTracking (self):
      '''None'''
    ...
    def _Widget__focusChanged (oldWidget, newWidget):
      '''None'''
    ...
    def _Widget__focusChangedConnected (self, *args, **kwargs):
      '''bool(x) -> bool

Returns True when the argument x is true, False otherwise.
The builtins True and False are the only two instances of the class bool.
The class bool is a subclass of the class int, and cannot be subclassed.'''
    ...
    def _Widget__focusChangedSignal (self, *args, **kwargs):
      '''None'''
    ...
    def _Widget__initNesting ():
      '''None'''
    ...
    def _Widget__keyMapping (self, *args, **kwargs):
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
    def _Widget__parentStack (self, *args, **kwargs):
      '''Built-in mutable sequence.

If no argument is given, the constructor creates a new empty list.
The argument must be an iterable if specified.'''
    ...
    def _Widget__propagateDisplayTransformChange (self):
      '''None'''
    ...
    def _Widget__qtWidgetOwners (self, *args, **kwargs):
      ''' Mapping class that references keys weakly.

    Entries in the dictionary will be discarded when there is no
    longer a strong reference to the key. This can be used to
    associate additional data with an object owned by other parts of
    an application without adding attributes to those objects. This
    can be especially useful with objects that override attribute
    accesses.
    '''
    ...
    def _Widget__styleClassName ():
      '''None'''
    ...
    def _applyVisibility (self):
      '''None'''
    ...
    def _buttons (qtButtons):
      '''None'''
    ...
    def _disconnectTrackedConnections (self, *args, **kwargs):
      '''
_disconnectTrackedConnections( (Trackable)arg1) -> None :

    C++ signature :
        void _disconnectTrackedConnections(Gaffer::Signals::Trackable {lvalue})'''
    ...
    def _displayTransformChanged (self):
      '''None'''
    ...
    def _key (qtKey):
      '''None'''
    ...
    def _modifiers (qtModifiers):
      '''None'''
    ...
    def _owner (qtWidget):
      '''None'''
    ...
    def _popParent ():
      '''None'''
    ...
    def _postConstructor (self):
      '''None'''
    ...
    def _pushParent (container):
      '''None'''
    ...
    def _qtColor (color):
      '''None'''
    ...
    def _qtWidget (self):
      '''None'''
    ...
    def _repolish (self, qtWidget=None):
      '''None'''
    ...
    def _setStyleSheet (self):
      '''None'''
    ...
    def _updateFromPath (self):
      '''None'''
    ...
    def ancestor (self, type):
      '''None'''
    ...
    def bound (self, relativeTo=None):
      '''None'''
    ...
    def buttonDoubleClickSignal (self):
      '''None'''
    ...
    def buttonPressSignal (self):
      '''None'''
    ...
    def buttonReleaseSignal (self):
      '''None'''
    ...
    def contextMenuSignal (self):
      '''None'''
    ...
    def create (name, path):
      '''None'''
    ...
    def currentModifiers ():
      '''None'''
    ...
    def displayTransform (self):
      '''None'''
    ...
    def dragBeginSignal (self):
      '''None'''
    ...
    def dragEndSignal (self):
      '''None'''
    ...
    def dragEnterSignal (self):
      '''None'''
    ...
    def dragLeaveSignal (self):
      '''None'''
    ...
    def dragMoveSignal (self):
      '''None'''
    ...
    def dropSignal (self):
      '''None'''
    ...
    def enabled (self, relativeTo=None):
      '''None'''
    ...
    def enterSignal (self):
      '''None'''
    ...
    def focusChangedSignal ():
      '''None'''
    ...
    def getDisplayTransform (self):
      '''None'''
    ...
    def getEnabled (self):
      '''None'''
    ...
    def getHighlighted (self):
      '''None'''
    ...
    def getPath (self):
      '''None'''
    ...
    def getToolTip (self):
      '''None'''
    ...
    def getVisible (self):
      '''None'''
    ...
    def identityDisplayTransform (x):
      '''None'''
    ...
    def isAncestorOf (self, other):
      '''None'''
    ...
    def isValid (self):
      '''None'''
    ...
    def keyPressSignal (self):
      '''None'''
    ...
    def keyReleaseSignal (self):
      '''None'''
    ...
    def leaveSignal (self):
      '''None'''
    ...
    def mouseMoveSignal (self):
      '''None'''
    ...
    def mousePosition (relativeTo=None):
      '''None'''
    ...
    def parent (self):
      '''None'''
    ...
    def parentChangedSignal (self):
      '''None'''
    ...
    def registerType (name, creator):
      '''None'''
    ...
    def reveal (self):
      '''None'''
    ...
    def setDisplayTransform (self, displayTransform):
      '''None'''
    ...
    def setEnabled (self, enabled):
      '''None'''
    ...
    def setHighlighted (self, highlighted):
      '''None'''
    ...
    def setPath (self, path):
      '''None'''
    ...
    def setToolTip (self, toolTip):
      '''None'''
    ...
    def setVisible (self, visible):
      '''None'''
    ...
    def size (self):
      '''None'''
    ...
    def types ():
      '''None'''
    ...
    def visibilityChangedSignal (self):
      '''None'''
    ...
    def visible (self, relativeTo=None):
      '''None'''
    ...
    def wheelSignal (self):
      '''None'''
    ...
    def widgetAt (position, widgetType=None):
      '''None'''
    ...

def SceneReaderUI (*args):
      '''

'''      
    ...

def SceneView (*args):
      '''
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > name='SceneView')

'''      
    ...

class SceneView:
    def BinaryPlugSignal (self, *args, **kwargs):
      '''None'''
    ...
    def BinarySignal (self, *args, **kwargs):
      '''None'''
    ...
    def DisplayTransform (self, *args, **kwargs):
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
    def _getPreprocessor (self, *args, **kwargs):
      '''
_getPreprocessor( (View)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<Gaffer::Node> _getPreprocessor(GafferUI::View {lvalue})'''
    ...
    def _setPreprocessor (self, *args, **kwargs):
      '''
_setPreprocessor( (View)arg1, (object)arg2) -> None :

    C++ signature :
        void _setPreprocessor(GafferUI::View {lvalue},boost::intrusive_ptr<Gaffer::Node>)'''
    ...
    def acceptsChild (self, *args, **kwargs):
      '''
acceptsChild( (SceneView)arg1, (GraphComponent)arg2) -> bool :

    C++ signature :
        bool acceptsChild(GafferSceneUI::SceneView,Gaffer::GraphComponent const*)'''
    ...
    def acceptsParent (self, *args, **kwargs):
      '''
acceptsParent( (SceneView)arg1, (GraphComponent)arg2) -> bool :

    C++ signature :
        bool acceptsParent(GafferSceneUI::SceneView,Gaffer::GraphComponent const*)'''
    ...
    def addChild (self, *args, **kwargs):
      '''
addChild( (GraphComponent)arg1, (GraphComponent)arg2) -> None :

    C++ signature :
        void addChild(Gaffer::GraphComponent {lvalue},Gaffer::GraphComponent {lvalue})'''
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
    def collapseSelection (self, *args, **kwargs):
      '''
collapseSelection( (SceneView)arg1) -> None :

    C++ signature :
        void collapseSelection(GafferSceneUI::SceneView {lvalue})'''
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
    def contextChangedSignal (self, *args, **kwargs):
      '''
contextChangedSignal( (View)arg1) -> UnarySignal :

    C++ signature :
        Gaffer::Signals::Signal<void (Gaffer::GraphComponent*), Gaffer::Signals::CatchingCombiner<void> > {lvalue} contextChangedSignal(GafferUI::View {lvalue})'''
    ...
    def create (self, *args, **kwargs):
      '''
create( (object)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<GafferUI::View> create(boost::intrusive_ptr<Gaffer::Plug>)'''
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
    def editScope (self, *args, **kwargs):
      '''
editScope( (View)arg1) -> object :

    C++ signature :
        Gaffer::EditScope* editScope(GafferUI::View {lvalue})'''
    ...
    def errorSignal (self, *args, **kwargs):
      '''
errorSignal( (Node)arg1) -> ErrorSignal :

    C++ signature :
        Gaffer::Signals::Signal<void (Gaffer::Plug const*, Gaffer::Plug const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&), Gaffer::Signals::CatchingCombiner<void> > {lvalue} errorSignal(Gaffer::Node {lvalue})'''
    ...
    def expandSelection (self, *args, **kwargs):
      '''
expandSelection( (SceneView)arg1 [, (int)depth=1]) -> None :

    C++ signature :
        void expandSelection(GafferSceneUI::SceneView {lvalue} [,unsigned long=1])'''
    ...
    def frame (self, *args, **kwargs):
      '''
frame( (SceneView)arg1, (PathMatcher)filter [, (V3f)direction=V3f(-0.639999986, -0.421999991, -0.639999986)]) -> None :

    C++ signature :
        void frame(GafferSceneUI::SceneView {lvalue},IECore::PathMatcher {lvalue} [,Imath_3_1::Vec3<float> {lvalue}=V3f(-0.639999986, -0.421999991, -0.639999986)])'''
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
getContext( (View)arg1) -> object :

    C++ signature :
        Gaffer::Context* getContext(GafferUI::View {lvalue})'''
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
isInstanceOf( (SceneView)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(GafferSceneUI::SceneView {lvalue},IECore::TypeId)

isInstanceOf( (SceneView)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(GafferSceneUI::SceneView {lvalue},char const*)'''
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
    def registerRenderer (self, *args, **kwargs):
      '''
registerRenderer( (object)arg1, (object)arg2) -> None :

    C++ signature :
        void registerRenderer(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >,boost::python::api::object)'''
    ...
    def registerShadingMode (self, *args, **kwargs):
      '''
registerShadingMode( (object)arg1, (object)arg2) -> None :

    C++ signature :
        void registerShadingMode(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >,boost::python::api::object)'''
    ...
    def registerType (self, *args, **kwargs):
      '''
registerType( (TypeId)arg1, (str)arg2, (TypeId)arg3) -> None :

    C++ signature :
        void registerType(IECore::TypeId,char const*,IECore::TypeId)'''
    ...
    def registerView (self, *args, **kwargs):
      '''
registerView( (TypeId)arg1, (object)arg2) -> None :

    C++ signature :
        void registerView(IECore::TypeId,boost::python::api::object)

registerView( (TypeId)arg1, (object)arg2, (object)arg3) -> None :

    C++ signature :
        void registerView(IECore::TypeId,std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >,boost::python::api::object)'''
    ...
    def registeredRenderers (self, *args, **kwargs):
      '''
registeredRenderers() -> list :

    C++ signature :
        boost::python::list registeredRenderers()'''
    ...
    def registeredShadingModes (self, *args, **kwargs):
      '''
registeredShadingModes() -> list :

    C++ signature :
        boost::python::list registeredShadingModes()'''
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
    def resolutionGate (self, *args, **kwargs):
      '''
resolutionGate( (SceneView)arg1) -> Box2f :

    C++ signature :
        Imath_3_1::Box<Imath_3_1::Vec2<float> > resolutionGate(GafferSceneUI::SceneView {lvalue})'''
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
setContext( (View)arg1, (object)arg2) -> None :

    C++ signature :
        void setContext(GafferUI::View {lvalue},boost::intrusive_ptr<Gaffer::Context>)'''
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
typeId( (SceneView)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(GafferSceneUI::SceneView {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (SceneView)arg1) -> str :

    C++ signature :
        char const* typeName(GafferSceneUI::SceneView {lvalue})'''
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
    def viewportGadget (self, *args, **kwargs):
      '''
viewportGadget( (View)arg1) -> object :

    C++ signature :
        GafferUI::ViewportGadget* viewportGadget(GafferUI::View {lvalue})'''
    ...

def SceneViewUI (*args):
      '''

'''      
    ...

def SceneWriterUI (*args):
      '''

'''      
    ...

def SelectionTool (*args):
      '''

'''      
    ...

class SelectionTool:
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
acceptsChild( (SelectionTool)arg1, (GraphComponent)arg2) -> bool :

    C++ signature :
        bool acceptsChild(GafferSceneUI::SelectionTool,Gaffer::GraphComponent const*)'''
    ...
    def acceptsParent (self, *args, **kwargs):
      '''
acceptsParent( (SelectionTool)arg1, (GraphComponent)arg2) -> bool :

    C++ signature :
        bool acceptsParent(GafferSceneUI::SelectionTool,Gaffer::GraphComponent const*)'''
    ...
    def addChild (self, *args, **kwargs):
      '''
addChild( (GraphComponent)arg1, (GraphComponent)arg2) -> None :

    C++ signature :
        void addChild(Gaffer::GraphComponent {lvalue},Gaffer::GraphComponent {lvalue})'''
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
    def create (self, *args, **kwargs):
      '''
create( (object)arg1, (View)arg2) -> object :

    C++ signature :
        boost::intrusive_ptr<GafferUI::Tool> create(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >,GafferUI::View {lvalue})'''
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
isInstanceOf( (SelectionTool)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(GafferSceneUI::SelectionTool {lvalue},IECore::TypeId)

isInstanceOf( (SelectionTool)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(GafferSceneUI::SelectionTool {lvalue},char const*)'''
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
    def registerTool (self, *args, **kwargs):
      '''
registerTool( (object)arg1, (TypeId)arg2, (object)arg3) -> None :

    C++ signature :
        void registerTool(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >,IECore::TypeId,boost::python::api::object)'''
    ...
    def registerType (self, *args, **kwargs):
      '''
registerType( (TypeId)arg1, (str)arg2, (TypeId)arg3) -> None :

    C++ signature :
        void registerType(IECore::TypeId,char const*,IECore::TypeId)'''
    ...
    def registeredTools (self, *args, **kwargs):
      '''
registeredTools( (TypeId)arg1) -> list :

    C++ signature :
        boost::python::list registeredTools(IECore::TypeId)'''
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
typeId( (SelectionTool)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(GafferSceneUI::SelectionTool {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (SelectionTool)arg1) -> str :

    C++ signature :
        char const* typeName(GafferSceneUI::SelectionTool {lvalue})'''
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
    def view (self, *args, **kwargs):
      '''
view( (Tool)arg1) -> object :

    C++ signature :
        GafferUI::View* view(GafferUI::Tool {lvalue})'''
    ...

def SelectionToolUI (*args):
      '''

'''      
    ...

def SetEditor (*args):
      '''

'''      
    ...

class SetEditor:
    def Settings (name, script):
      '''None'''
    ...
    def _Editor__contextChanged (self, context, key):
      '''None'''
    ...
    def _Editor__enter (self, widget):
      '''None'''
    ...
    def _Editor__leave (self, widget):
      '''None'''
    ...
    def _Editor__namesToCreators (self, *args, **kwargs):
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
    def _Editor__setContextInternal (self, context, callUpdate):
      '''None'''
    ...
    def _NodeSetEditor__dirtyTitle (self):
      '''None'''
    ...
    def _NodeSetEditor__lazyUpdate (self):
      '''None'''
    ...
    def _NodeSetEditor__membersChanged (self, set, member):
      '''None'''
    ...
    def _NodeSetEditor__nameChanged (self, node, oldName):
      '''None'''
    ...
    def _NodeSetEditor__setNodeSetInternal (self, nodeSet, callUpdateFromSet):
      '''None'''
    ...
    def _SetEditor__contextMenuSignal (self, widget):
      '''None'''
    ...
    def _SetEditor__copySelectedSetNames (self, *unused):
      '''None'''
    ...
    def _SetEditor__copySetMembers (self, *unused):
      '''None'''
    ...
    def _SetEditor__dragBegin (self, widget, event):
      '''None'''
    ...
    def _SetEditor__firstValidScenePlug (self, node):
      '''None'''
    ...
    def _SetEditor__getExcludedSetMembers (self, setNames, *unused):
      '''None'''
    ...
    def _SetEditor__getIncludedSetMembers (self, setNames, *unused):
      '''None'''
    ...
    def _SetEditor__getSelectedSetMembers (self, setNames, *unused):
      '''None'''
    ...
    def _SetEditor__getSetMembers (self, setNames, *unused):
      '''None'''
    ...
    def _SetEditor__keyPressSignal (self, widget, event):
      '''None'''
    ...
    def _SetEditor__plugParentChanged (self, plug, oldParent):
      '''None'''
    ...
    def _SetEditor__selectSetMembers (self, *unused):
      '''None'''
    ...
    def _SetEditor__selectedSetNames (self):
      '''None'''
    ...
    def _SetEditor__updatePathListingPath (self):
      '''None'''
    ...
    def _Widget__applyQWidgetStyleClasses (self):
      '''None'''
    ...
    def _Widget__ensureEventFilter (self):
      '''None'''
    ...
    def _Widget__ensureFocusChangedConnection ():
      '''None'''
    ...
    def _Widget__ensureMouseTracking (self):
      '''None'''
    ...
    def _Widget__focusChanged (oldWidget, newWidget):
      '''None'''
    ...
    def _Widget__focusChangedConnected (self, *args, **kwargs):
      '''bool(x) -> bool

Returns True when the argument x is true, False otherwise.
The builtins True and False are the only two instances of the class bool.
The class bool is a subclass of the class int, and cannot be subclassed.'''
    ...
    def _Widget__focusChangedSignal (self, *args, **kwargs):
      '''None'''
    ...
    def _Widget__initNesting ():
      '''None'''
    ...
    def _Widget__keyMapping (self, *args, **kwargs):
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
    def _Widget__parentStack (self, *args, **kwargs):
      '''Built-in mutable sequence.

If no argument is given, the constructor creates a new empty list.
The argument must be an iterable if specified.'''
    ...
    def _Widget__propagateDisplayTransformChange (self):
      '''None'''
    ...
    def _Widget__qtWidgetOwners (self, *args, **kwargs):
      ''' Mapping class that references keys weakly.

    Entries in the dictionary will be discarded when there is no
    longer a strong reference to the key. This can be used to
    associate additional data with an object owned by other parts of
    an application without adding attributes to those objects. This
    can be especially useful with objects that override attribute
    accesses.
    '''
    ...
    def _Widget__styleClassName ():
      '''None'''
    ...
    def _applyVisibility (self):
      '''None'''
    ...
    def _buttons (qtButtons):
      '''None'''
    ...
    def _contextChangedConnection (self):
      '''None'''
    ...
    def _disconnectTrackedConnections (self, *args, **kwargs):
      '''
_disconnectTrackedConnections( (Trackable)arg1) -> None :

    C++ signature :
        void _disconnectTrackedConnections(Gaffer::Signals::Trackable {lvalue})'''
    ...
    def _displayTransformChanged (self):
      '''None'''
    ...
    def _doPendingUpdate (self):
      '''None'''
    ...
    def _key (qtKey):
      '''None'''
    ...
    def _lastAddedNode (self):
      '''None'''
    ...
    def _modifiers (qtModifiers):
      '''None'''
    ...
    def _owner (qtWidget):
      '''None'''
    ...
    def _popParent ():
      '''None'''
    ...
    def _postConstructor (self):
      '''None'''
    ...
    def _pushParent (container):
      '''None'''
    ...
    def _qtColor (color):
      '''None'''
    ...
    def _qtWidget (self):
      '''None'''
    ...
    def _repolish (self, qtWidget=None):
      '''None'''
    ...
    def _setStyleSheet (self):
      '''None'''
    ...
    def _titleFormat (self):
      '''None'''
    ...
    def _updateFromContext (self, modifiedItems):
      '''None'''
    ...
    def _updateFromSet (self):
      '''None'''
    ...
    def acquire (node, floating=None):
      '''None'''
    ...
    def ancestor (self, type):
      '''None'''
    ...
    def bound (self, relativeTo=None):
      '''None'''
    ...
    def buttonDoubleClickSignal (self):
      '''None'''
    ...
    def buttonPressSignal (self):
      '''None'''
    ...
    def buttonReleaseSignal (self):
      '''None'''
    ...
    def contextMenuSignal (self):
      '''None'''
    ...
    def create (name, scriptNode):
      '''None'''
    ...
    def currentModifiers ():
      '''None'''
    ...
    def displayTransform (self):
      '''None'''
    ...
    def dragBeginSignal (self):
      '''None'''
    ...
    def dragEndSignal (self):
      '''None'''
    ...
    def dragEnterSignal (self):
      '''None'''
    ...
    def dragLeaveSignal (self):
      '''None'''
    ...
    def dragMoveSignal (self):
      '''None'''
    ...
    def dropSignal (self):
      '''None'''
    ...
    def enabled (self, relativeTo=None):
      '''None'''
    ...
    def enterSignal (self):
      '''None'''
    ...
    def focusChangedSignal ():
      '''None'''
    ...
    def getContext (self):
      '''None'''
    ...
    def getDisplayTransform (self):
      '''None'''
    ...
    def getEnabled (self):
      '''None'''
    ...
    def getHighlighted (self):
      '''None'''
    ...
    def getNodeSet (self):
      '''None'''
    ...
    def getTitle (self):
      '''None'''
    ...
    def getToolTip (self):
      '''None'''
    ...
    def getVisible (self):
      '''None'''
    ...
    def identityDisplayTransform (x):
      '''None'''
    ...
    def instanceCreatedSignal ():
      '''None'''
    ...
    def isAncestorOf (self, other):
      '''None'''
    ...
    def keyPressSignal (self):
      '''None'''
    ...
    def keyReleaseSignal (self):
      '''None'''
    ...
    def leaveSignal (self):
      '''None'''
    ...
    def mouseMoveSignal (self):
      '''None'''
    ...
    def mousePosition (relativeTo=None):
      '''None'''
    ...
    def nodeSetChangedSignal (self):
      '''None'''
    ...
    def parent (self):
      '''None'''
    ...
    def parentChangedSignal (self):
      '''None'''
    ...
    def registerType (name, creator):
      '''None'''
    ...
    def reveal (self):
      '''None'''
    ...
    def scriptNode (self):
      '''None'''
    ...
    def setContext (self, context):
      '''None'''
    ...
    def setDisplayTransform (self, displayTransform):
      '''None'''
    ...
    def setEnabled (self, enabled):
      '''None'''
    ...
    def setHighlighted (self, highlighted):
      '''None'''
    ...
    def setNodeSet (self, nodeSet):
      '''None'''
    ...
    def setTitle (self, title):
      '''None'''
    ...
    def setToolTip (self, toolTip):
      '''None'''
    ...
    def setVisible (self, visible):
      '''None'''
    ...
    def size (self):
      '''None'''
    ...
    def titleChangedSignal (self):
      '''None'''
    ...
    def types ():
      '''None'''
    ...
    def visibilityChangedSignal (self):
      '''None'''
    ...
    def visible (self, relativeTo=None):
      '''None'''
    ...
    def wheelSignal (self):
      '''None'''
    ...
    def widgetAt (position, widgetType=None):
      '''None'''
    ...

def SetFilterUI (*args):
      '''

'''      
    ...

def SetQueryUI (*args):
      '''

'''      
    ...

def SetUI (*args):
      '''

'''      
    ...

def SetVisualiserUI (*args):
      '''

'''      
    ...

def ShaderAssignmentUI (*args):
      '''

'''      
    ...

def ShaderBallUI (*args):
      '''

'''      
    ...

def ShaderQueryUI (*args):
      '''

'''      
    ...

def ShaderTweaksUI (*args):
      '''

'''      
    ...

def ShaderUI (*args):
      '''

'''      
    ...

def ShaderView (*args):
      '''
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > name='ShaderView')

'''      
    ...

class ShaderView:
    def BinaryPlugSignal (self, *args, **kwargs):
      '''None'''
    ...
    def BinarySignal (self, *args, **kwargs):
      '''None'''
    ...
    def ColorInspectorPlug (self, *args, **kwargs):
      '''None'''
    ...
    def DisplayTransform (self, *args, **kwargs):
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
    def _getPreprocessor (self, *args, **kwargs):
      '''
_getPreprocessor( (View)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<Gaffer::Node> _getPreprocessor(GafferUI::View {lvalue})'''
    ...
    def _insertConverter (self, *args, **kwargs):
      '''
_insertConverter( (ImageView)arg1, (object)arg2) -> None :

    C++ signature :
        void _insertConverter((anonymous namespace)::ImageViewWrapper {lvalue},boost::intrusive_ptr<Gaffer::Node>)'''
    ...
    def _setPreprocessor (self, *args, **kwargs):
      '''
_setPreprocessor( (View)arg1, (object)arg2) -> None :

    C++ signature :
        void _setPreprocessor(GafferUI::View {lvalue},boost::intrusive_ptr<Gaffer::Node>)'''
    ...
    def acceptsChild (self, *args, **kwargs):
      '''
acceptsChild( (ShaderView)arg1, (GraphComponent)arg2) -> bool :

    C++ signature :
        bool acceptsChild(GafferSceneUI::ShaderView,Gaffer::GraphComponent const*)'''
    ...
    def acceptsParent (self, *args, **kwargs):
      '''
acceptsParent( (ShaderView)arg1, (GraphComponent)arg2) -> bool :

    C++ signature :
        bool acceptsParent(GafferSceneUI::ShaderView,Gaffer::GraphComponent const*)'''
    ...
    def addChild (self, *args, **kwargs):
      '''
addChild( (GraphComponent)arg1, (GraphComponent)arg2) -> None :

    C++ signature :
        void addChild(Gaffer::GraphComponent {lvalue},Gaffer::GraphComponent {lvalue})'''
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
    def contextChangedSignal (self, *args, **kwargs):
      '''
contextChangedSignal( (View)arg1) -> UnarySignal :

    C++ signature :
        Gaffer::Signals::Signal<void (Gaffer::GraphComponent*), Gaffer::Signals::CatchingCombiner<void> > {lvalue} contextChangedSignal(GafferUI::View {lvalue})'''
    ...
    def create (self, *args, **kwargs):
      '''
create( (object)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<GafferUI::View> create(boost::intrusive_ptr<Gaffer::Plug>)'''
    ...
    def deregisterRenderer (self, *args, **kwargs):
      '''
deregisterRenderer( (object)arg1) -> None :

    C++ signature :
        void deregisterRenderer(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)'''
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
    def editScope (self, *args, **kwargs):
      '''
editScope( (View)arg1) -> object :

    C++ signature :
        Gaffer::EditScope* editScope(GafferUI::View {lvalue})'''
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
getContext( (View)arg1) -> object :

    C++ signature :
        Gaffer::Context* getContext(GafferUI::View {lvalue})'''
    ...
    def getName (self, *args, **kwargs):
      '''
getName( (GraphComponent)arg1) -> str :

    C++ signature :
        char const* getName(Gaffer::GraphComponent {lvalue})'''
    ...
    def imageGadget (self, *args, **kwargs):
      '''
imageGadget( (ImageView)arg1) -> object :

    C++ signature :
        GafferImageUI::ImageGadget* imageGadget(GafferImageUI::ImageView {lvalue})'''
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
isInstanceOf( (ShaderView)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(GafferSceneUI::ShaderView {lvalue},IECore::TypeId)

isInstanceOf( (ShaderView)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(GafferSceneUI::ShaderView {lvalue},char const*)'''
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
    def registerRenderer (self, *args, **kwargs):
      '''
registerRenderer( (object)arg1, (object)arg2) -> None :

    C++ signature :
        void registerRenderer(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >,boost::python::api::object)'''
    ...
    def registerScene (self, *args, **kwargs):
      '''
registerScene( (object)arg1, (object)arg2, (object)arg3) -> None :

    C++ signature :
        void registerScene(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >,std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >,boost::python::api::object)

registerScene( (object)arg1, (object)arg2, (object)arg3) -> None :

    C++ signature :
        void registerScene(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >,std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >,std::filesystem::__cxx11::path)'''
    ...
    def registerType (self, *args, **kwargs):
      '''
registerType( (TypeId)arg1, (str)arg2, (TypeId)arg3) -> None :

    C++ signature :
        void registerType(IECore::TypeId,char const*,IECore::TypeId)'''
    ...
    def registerView (self, *args, **kwargs):
      '''
registerView( (TypeId)arg1, (object)arg2) -> None :

    C++ signature :
        void registerView(IECore::TypeId,boost::python::api::object)

registerView( (TypeId)arg1, (object)arg2, (object)arg3) -> None :

    C++ signature :
        void registerView(IECore::TypeId,std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >,boost::python::api::object)'''
    ...
    def registeredScenes (self, *args, **kwargs):
      '''
registeredScenes( (InternedString)arg1) -> list :

    C++ signature :
        boost::python::list registeredScenes(IECore::InternedString)'''
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
    def scene (self, *args, **kwargs):
      '''
scene( (ShaderView)arg1) -> object :

    C++ signature :
        Gaffer::Node* scene(GafferSceneUI::ShaderView {lvalue})'''
    ...
    def sceneChangedSignal (self, *args, **kwargs):
      '''
sceneChangedSignal( (ShaderView)arg1) -> SceneChangedSignal :

    C++ signature :
        Gaffer::Signals::Signal<void (GafferSceneUI::ShaderView*), Gaffer::Signals::DefaultCombiner<void> > {lvalue} sceneChangedSignal(GafferSceneUI::ShaderView {lvalue})'''
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
setContext( (View)arg1, (object)arg2) -> None :

    C++ signature :
        void setContext(GafferUI::View {lvalue},boost::intrusive_ptr<Gaffer::Context>)'''
    ...
    def setName (self, *args, **kwargs):
      '''
setName( (GraphComponent)arg1, (InternedString)arg2) -> str :

    C++ signature :
        char const* setName(Gaffer::GraphComponent {lvalue},IECore::InternedString)'''
    ...
    def shaderPrefix (self, *args, **kwargs):
      '''
shaderPrefix( (ShaderView)arg1) -> str :

    C++ signature :
        std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > shaderPrefix(GafferSceneUI::ShaderView {lvalue})'''
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
typeId( (ShaderView)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(GafferSceneUI::ShaderView {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (ShaderView)arg1) -> str :

    C++ signature :
        char const* typeName(GafferSceneUI::ShaderView {lvalue})'''
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
    def viewportGadget (self, *args, **kwargs):
      '''
viewportGadget( (View)arg1) -> object :

    C++ signature :
        GafferUI::ViewportGadget* viewportGadget(GafferUI::View {lvalue})'''
    ...

def ShaderViewUI (*args):
      '''

'''      
    ...

def ShuffleAttributesUI (*args):
      '''

'''      
    ...

def ShufflePrimitiveVariablesUI (*args):
      '''

'''      
    ...

def SphereUI (*args):
      '''

'''      
    ...

def StandardAttributesUI (*args):
      '''

'''      
    ...

def StandardLightVisualiser (*args):
      '''

'''      
    ...

class StandardLightVisualiser:
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
    def registerLightVisualiser (self, *args, **kwargs):
      '''
registerLightVisualiser( (InternedString)arg1, (InternedString)arg2, (object)arg3) -> None :

    C++ signature :
        void registerLightVisualiser(IECore::InternedString,IECore::InternedString,boost::intrusive_ptr<IECoreGLPreview::LightVisualiser const>)'''
    ...

def StandardOptionsUI (*args):
      '''

'''      
    ...

def StatusChangedSignal (*args):
      '''
__init__(_object*)

'''      
    ...

class StatusChangedSignal:
    def connect (self, *args, **kwargs):
      '''
connect( (StatusChangedSignal)arg1, (object)slot [, (object)scoped=None]) -> object :

    C++ signature :
        boost::python::api::object connect(Gaffer::Signals::Signal<void (GafferSceneUI::CropWindowTool&), Gaffer::Signals::DefaultCombiner<void> > {lvalue},boost::python::api::object {lvalue} [,boost::python::api::object=None])'''
    ...
    def connectFront (self, *args, **kwargs):
      '''
connectFront( (StatusChangedSignal)arg1, (object)slot [, (object)scoped=None]) -> object :

    C++ signature :
        boost::python::api::object connectFront(Gaffer::Signals::Signal<void (GafferSceneUI::CropWindowTool&), Gaffer::Signals::DefaultCombiner<void> > {lvalue},boost::python::api::object {lvalue} [,boost::python::api::object=None])'''
    ...
    def disconnectAllSlots (self, *args, **kwargs):
      '''
disconnectAllSlots( (StatusChangedSignal)arg1) -> None :

    C++ signature :
        void disconnectAllSlots(Gaffer::Signals::Signal<void (GafferSceneUI::CropWindowTool&), Gaffer::Signals::DefaultCombiner<void> > {lvalue})'''
    ...
    def empty (self, *args, **kwargs):
      '''
empty( (StatusChangedSignal)arg1) -> bool :

    C++ signature :
        bool empty(Gaffer::Signals::Signal<void (GafferSceneUI::CropWindowTool&), Gaffer::Signals::DefaultCombiner<void> > {lvalue})'''
    ...
    def numSlots (self, *args, **kwargs):
      '''
numSlots( (StatusChangedSignal)arg1) -> int :

    C++ signature :
        unsigned long numSlots(Gaffer::Signals::Signal<void (GafferSceneUI::CropWindowTool&), Gaffer::Signals::DefaultCombiner<void> > {lvalue})'''
    ...

def SubTreeUI (*args):
      '''

'''      
    ...

def TextUI (*args):
      '''

'''      
    ...

def TransformQueryUI (*args):
      '''

'''      
    ...

def TransformTool (*args):
      '''

'''      
    ...

class TransformTool:
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
    def Orientation (self, *args, **kwargs):
      '''None'''
    ...
    def Range (parent):
      '''None'''
    ...
    def RecursiveRange (parent):
      '''None'''
    ...
    def Selection (self, *args, **kwargs):
      '''None'''
    ...
    def SelectionChangedSignal (self, *args, **kwargs):
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
acceptsChild( (TransformTool)arg1, (GraphComponent)arg2) -> bool :

    C++ signature :
        bool acceptsChild(GafferSceneUI::TransformTool,Gaffer::GraphComponent const*)'''
    ...
    def acceptsParent (self, *args, **kwargs):
      '''
acceptsParent( (TransformTool)arg1, (GraphComponent)arg2) -> bool :

    C++ signature :
        bool acceptsParent(GafferSceneUI::TransformTool,Gaffer::GraphComponent const*)'''
    ...
    def addChild (self, *args, **kwargs):
      '''
addChild( (GraphComponent)arg1, (GraphComponent)arg2) -> None :

    C++ signature :
        void addChild(Gaffer::GraphComponent {lvalue},Gaffer::GraphComponent {lvalue})'''
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
    def create (self, *args, **kwargs):
      '''
create( (object)arg1, (View)arg2) -> object :

    C++ signature :
        boost::intrusive_ptr<GafferUI::Tool> create(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >,GafferUI::View {lvalue})'''
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
    def handlesTransform (self, *args, **kwargs):
      '''
handlesTransform( (TransformTool)arg1) -> M44f :

    C++ signature :
        Imath_3_1::Matrix44<float> handlesTransform(GafferSceneUI::TransformTool {lvalue})'''
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
isInstanceOf( (TransformTool)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(GafferSceneUI::TransformTool {lvalue},IECore::TypeId)

isInstanceOf( (TransformTool)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(GafferSceneUI::TransformTool {lvalue},char const*)'''
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
    def registerTool (self, *args, **kwargs):
      '''
registerTool( (object)arg1, (TypeId)arg2, (object)arg3) -> None :

    C++ signature :
        void registerTool(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >,IECore::TypeId,boost::python::api::object)'''
    ...
    def registerType (self, *args, **kwargs):
      '''
registerType( (TypeId)arg1, (str)arg2, (TypeId)arg3) -> None :

    C++ signature :
        void registerType(IECore::TypeId,char const*,IECore::TypeId)'''
    ...
    def registeredTools (self, *args, **kwargs):
      '''
registeredTools( (TypeId)arg1) -> list :

    C++ signature :
        boost::python::list registeredTools(IECore::TypeId)'''
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
    def selection (self, *args, **kwargs):
      '''
selection( (TransformTool)arg1) -> list :

    C++ signature :
        boost::python::list selection(GafferSceneUI::TransformTool)'''
    ...
    def selectionChangedSignal (self, *args, **kwargs):
      '''
selectionChangedSignal( (TransformTool)arg1) -> SelectionChangedSignal :

    C++ signature :
        Gaffer::Signals::Signal<void (GafferSceneUI::TransformTool&), Gaffer::Signals::DefaultCombiner<void> > {lvalue} selectionChangedSignal(GafferSceneUI::TransformTool {lvalue})'''
    ...
    def selectionEditable (self, *args, **kwargs):
      '''
selectionEditable( (TransformTool)arg1) -> bool :

    C++ signature :
        bool selectionEditable(GafferSceneUI::TransformTool)'''
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
typeId( (TransformTool)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(GafferSceneUI::TransformTool {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (TransformTool)arg1) -> str :

    C++ signature :
        char const* typeName(GafferSceneUI::TransformTool {lvalue})'''
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
    def view (self, *args, **kwargs):
      '''
view( (Tool)arg1) -> object :

    C++ signature :
        GafferUI::View* view(GafferUI::Tool {lvalue})'''
    ...

def TransformToolUI (*args):
      '''

'''      
    ...

def TransformUI (*args):
      '''

'''      
    ...

def TranslateTool (*args):
      '''
__init__(_object*, GafferSceneUI::SceneView*)

'''      
    ...

class TranslateTool:
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
    def Orientation (self, *args, **kwargs):
      '''None'''
    ...
    def Range (parent):
      '''None'''
    ...
    def RecursiveRange (parent):
      '''None'''
    ...
    def Selection (self, *args, **kwargs):
      '''None'''
    ...
    def SelectionChangedSignal (self, *args, **kwargs):
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
acceptsChild( (TranslateTool)arg1, (GraphComponent)arg2) -> bool :

    C++ signature :
        bool acceptsChild(GafferSceneUI::TranslateTool,Gaffer::GraphComponent const*)'''
    ...
    def acceptsParent (self, *args, **kwargs):
      '''
acceptsParent( (TranslateTool)arg1, (GraphComponent)arg2) -> bool :

    C++ signature :
        bool acceptsParent(GafferSceneUI::TranslateTool,Gaffer::GraphComponent const*)'''
    ...
    def addChild (self, *args, **kwargs):
      '''
addChild( (GraphComponent)arg1, (GraphComponent)arg2) -> None :

    C++ signature :
        void addChild(Gaffer::GraphComponent {lvalue},Gaffer::GraphComponent {lvalue})'''
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
    def create (self, *args, **kwargs):
      '''
create( (object)arg1, (View)arg2) -> object :

    C++ signature :
        boost::intrusive_ptr<GafferUI::Tool> create(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >,GafferUI::View {lvalue})'''
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
    def handlesTransform (self, *args, **kwargs):
      '''
handlesTransform( (TransformTool)arg1) -> M44f :

    C++ signature :
        Imath_3_1::Matrix44<float> handlesTransform(GafferSceneUI::TransformTool {lvalue})'''
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
isInstanceOf( (TranslateTool)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(GafferSceneUI::TranslateTool {lvalue},IECore::TypeId)

isInstanceOf( (TranslateTool)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(GafferSceneUI::TranslateTool {lvalue},char const*)'''
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
    def registerTool (self, *args, **kwargs):
      '''
registerTool( (object)arg1, (TypeId)arg2, (object)arg3) -> None :

    C++ signature :
        void registerTool(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >,IECore::TypeId,boost::python::api::object)'''
    ...
    def registerType (self, *args, **kwargs):
      '''
registerType( (TypeId)arg1, (str)arg2, (TypeId)arg3) -> None :

    C++ signature :
        void registerType(IECore::TypeId,char const*,IECore::TypeId)'''
    ...
    def registeredTools (self, *args, **kwargs):
      '''
registeredTools( (TypeId)arg1) -> list :

    C++ signature :
        boost::python::list registeredTools(IECore::TypeId)'''
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
    def selection (self, *args, **kwargs):
      '''
selection( (TransformTool)arg1) -> list :

    C++ signature :
        boost::python::list selection(GafferSceneUI::TransformTool)'''
    ...
    def selectionChangedSignal (self, *args, **kwargs):
      '''
selectionChangedSignal( (TransformTool)arg1) -> SelectionChangedSignal :

    C++ signature :
        Gaffer::Signals::Signal<void (GafferSceneUI::TransformTool&), Gaffer::Signals::DefaultCombiner<void> > {lvalue} selectionChangedSignal(GafferSceneUI::TransformTool {lvalue})'''
    ...
    def selectionEditable (self, *args, **kwargs):
      '''
selectionEditable( (TransformTool)arg1) -> bool :

    C++ signature :
        bool selectionEditable(GafferSceneUI::TransformTool)'''
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
    def translate (self, *args, **kwargs):
      '''
translate( (TranslateTool)arg1, (V3f)arg2) -> None :

    C++ signature :
        void translate(GafferSceneUI::TranslateTool {lvalue},Imath_3_1::Vec3<float>)'''
    ...
    def typeId (self, *args, **kwargs):
      '''
typeId( (TranslateTool)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(GafferSceneUI::TranslateTool {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (TranslateTool)arg1) -> str :

    C++ signature :
        char const* typeName(GafferSceneUI::TranslateTool {lvalue})'''
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
    def view (self, *args, **kwargs):
      '''
view( (Tool)arg1) -> object :

    C++ signature :
        GafferUI::View* view(GafferUI::Tool {lvalue})'''
    ...

def TranslateToolUI (*args):
      '''

'''      
    ...

def UDIMQueryUI (*args):
      '''

'''      
    ...

def UVInspector (*args):
      '''

'''      
    ...

class UVInspector:
    def Settings (name, script):
      '''None'''
    ...
    def _Editor__contextChanged (self, context, key):
      '''None'''
    ...
    def _Editor__enter (self, widget):
      '''None'''
    ...
    def _Editor__leave (self, widget):
      '''None'''
    ...
    def _Editor__namesToCreators (self, *args, **kwargs):
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
    def _Editor__setContextInternal (self, context, callUpdate):
      '''None'''
    ...
    def _NodeSetEditor__dirtyTitle (self):
      '''None'''
    ...
    def _NodeSetEditor__lazyUpdate (self):
      '''None'''
    ...
    def _NodeSetEditor__membersChanged (self, set, member):
      '''None'''
    ...
    def _NodeSetEditor__nameChanged (self, node, oldName):
      '''None'''
    ...
    def _NodeSetEditor__setNodeSetInternal (self, nodeSet, callUpdateFromSet):
      '''None'''
    ...
    def _StateWidget (*args, **kw):
      '''None'''
    ...
    def _UVInspector__buttonPress (self, viewportGadget, event):
      '''None'''
    ...
    def _UVInspector__dragBegin (self, viewportGadget, event):
      '''None'''
    ...
    def _UVInspector__dragEnd (self, viewportGadget, event):
      '''None'''
    ...
    def _UVInspector__keyPress (self, widget, event):
      '''None'''
    ...
    def _Widget__applyQWidgetStyleClasses (self):
      '''None'''
    ...
    def _Widget__ensureEventFilter (self):
      '''None'''
    ...
    def _Widget__ensureFocusChangedConnection ():
      '''None'''
    ...
    def _Widget__ensureMouseTracking (self):
      '''None'''
    ...
    def _Widget__focusChanged (oldWidget, newWidget):
      '''None'''
    ...
    def _Widget__focusChangedConnected (self, *args, **kwargs):
      '''bool(x) -> bool

Returns True when the argument x is true, False otherwise.
The builtins True and False are the only two instances of the class bool.
The class bool is a subclass of the class int, and cannot be subclassed.'''
    ...
    def _Widget__focusChangedSignal (self, *args, **kwargs):
      '''None'''
    ...
    def _Widget__initNesting ():
      '''None'''
    ...
    def _Widget__keyMapping (self, *args, **kwargs):
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
    def _Widget__parentStack (self, *args, **kwargs):
      '''Built-in mutable sequence.

If no argument is given, the constructor creates a new empty list.
The argument must be an iterable if specified.'''
    ...
    def _Widget__propagateDisplayTransformChange (self):
      '''None'''
    ...
    def _Widget__qtWidgetOwners (self, *args, **kwargs):
      ''' Mapping class that references keys weakly.

    Entries in the dictionary will be discarded when there is no
    longer a strong reference to the key. This can be used to
    associate additional data with an object owned by other parts of
    an application without adding attributes to those objects. This
    can be especially useful with objects that override attribute
    accesses.
    '''
    ...
    def _Widget__styleClassName ():
      '''None'''
    ...
    def _applyVisibility (self):
      '''None'''
    ...
    def _buttons (qtButtons):
      '''None'''
    ...
    def _contextChangedConnection (self):
      '''None'''
    ...
    def _disconnectTrackedConnections (self, *args, **kwargs):
      '''
_disconnectTrackedConnections( (Trackable)arg1) -> None :

    C++ signature :
        void _disconnectTrackedConnections(Gaffer::Signals::Trackable {lvalue})'''
    ...
    def _displayTransformChanged (self):
      '''None'''
    ...
    def _doPendingUpdate (self):
      '''None'''
    ...
    def _key (qtKey):
      '''None'''
    ...
    def _lastAddedNode (self):
      '''None'''
    ...
    def _modifiers (qtModifiers):
      '''None'''
    ...
    def _owner (qtWidget):
      '''None'''
    ...
    def _popParent ():
      '''None'''
    ...
    def _postConstructor (self):
      '''None'''
    ...
    def _pushParent (container):
      '''None'''
    ...
    def _qtColor (color):
      '''None'''
    ...
    def _qtWidget (self):
      '''None'''
    ...
    def _repolish (self, qtWidget=None):
      '''None'''
    ...
    def _setStyleSheet (self):
      '''None'''
    ...
    def _titleFormat (self, _prefix=None, _maxNodes=2, _reverseNodes=False, _ellipsis=True):
      '''None'''
    ...
    def _updateFromContext (self, modifiedItems):
      '''None'''
    ...
    def _updateFromSet (self):
      '''None'''
    ...
    def acquire (node, floating=None):
      '''None'''
    ...
    def ancestor (self, type):
      '''None'''
    ...
    def bound (self, relativeTo=None):
      '''None'''
    ...
    def buttonDoubleClickSignal (self):
      '''None'''
    ...
    def buttonPressSignal (self):
      '''None'''
    ...
    def buttonReleaseSignal (self):
      '''None'''
    ...
    def contextMenuSignal (self):
      '''None'''
    ...
    def create (name, scriptNode):
      '''None'''
    ...
    def currentModifiers ():
      '''None'''
    ...
    def displayTransform (self):
      '''None'''
    ...
    def dragBeginSignal (self):
      '''None'''
    ...
    def dragEndSignal (self):
      '''None'''
    ...
    def dragEnterSignal (self):
      '''None'''
    ...
    def dragLeaveSignal (self):
      '''None'''
    ...
    def dragMoveSignal (self):
      '''None'''
    ...
    def dropSignal (self):
      '''None'''
    ...
    def enabled (self, relativeTo=None):
      '''None'''
    ...
    def enterSignal (self):
      '''None'''
    ...
    def focusChangedSignal ():
      '''None'''
    ...
    def getContext (self):
      '''None'''
    ...
    def getDisplayTransform (self):
      '''None'''
    ...
    def getEnabled (self):
      '''None'''
    ...
    def getHighlighted (self):
      '''None'''
    ...
    def getNodeSet (self):
      '''None'''
    ...
    def getTitle (self):
      '''None'''
    ...
    def getToolTip (self):
      '''None'''
    ...
    def getVisible (self):
      '''None'''
    ...
    def identityDisplayTransform (x):
      '''None'''
    ...
    def instanceCreatedSignal ():
      '''None'''
    ...
    def isAncestorOf (self, other):
      '''None'''
    ...
    def keyPressSignal (self):
      '''None'''
    ...
    def keyReleaseSignal (self):
      '''None'''
    ...
    def leaveSignal (self):
      '''None'''
    ...
    def mouseMoveSignal (self):
      '''None'''
    ...
    def mousePosition (relativeTo=None):
      '''None'''
    ...
    def nodeSetChangedSignal (self):
      '''None'''
    ...
    def parent (self):
      '''None'''
    ...
    def parentChangedSignal (self):
      '''None'''
    ...
    def registerType (name, creator):
      '''None'''
    ...
    def reveal (self):
      '''None'''
    ...
    def scriptNode (self):
      '''None'''
    ...
    def setContext (self, context):
      '''None'''
    ...
    def setDisplayTransform (self, displayTransform):
      '''None'''
    ...
    def setEnabled (self, enabled):
      '''None'''
    ...
    def setHighlighted (self, highlighted):
      '''None'''
    ...
    def setNodeSet (self, nodeSet):
      '''None'''
    ...
    def setTitle (self, title):
      '''None'''
    ...
    def setToolTip (self, toolTip):
      '''None'''
    ...
    def setVisible (self, visible):
      '''None'''
    ...
    def size (self):
      '''None'''
    ...
    def titleChangedSignal (self):
      '''None'''
    ...
    def types ():
      '''None'''
    ...
    def visibilityChangedSignal (self):
      '''None'''
    ...
    def visible (self, relativeTo=None):
      '''None'''
    ...
    def wheelSignal (self):
      '''None'''
    ...
    def widgetAt (position, widgetType=None):
      '''None'''
    ...

def UVSamplerUI (*args):
      '''

'''      
    ...

def UVView (*args):
      '''
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > name='UVView')

'''      
    ...

class UVView:
    def BinaryPlugSignal (self, *args, **kwargs):
      '''None'''
    ...
    def BinarySignal (self, *args, **kwargs):
      '''None'''
    ...
    def DisplayTransform (self, *args, **kwargs):
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
    def UVViewSignal (self, *args, **kwargs):
      '''None'''
    ...
    def UnaryPlugSignal (self, *args, **kwargs):
      '''None'''
    ...
    def UnarySignal (self, *args, **kwargs):
      '''None'''
    ...
    def _getPreprocessor (self, *args, **kwargs):
      '''
_getPreprocessor( (View)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<Gaffer::Node> _getPreprocessor(GafferUI::View {lvalue})'''
    ...
    def _setPreprocessor (self, *args, **kwargs):
      '''
_setPreprocessor( (View)arg1, (object)arg2) -> None :

    C++ signature :
        void _setPreprocessor(GafferUI::View {lvalue},boost::intrusive_ptr<Gaffer::Node>)'''
    ...
    def acceptsChild (self, *args, **kwargs):
      '''
acceptsChild( (UVView)arg1, (GraphComponent)arg2) -> bool :

    C++ signature :
        bool acceptsChild(GafferSceneUI::UVView,Gaffer::GraphComponent const*)'''
    ...
    def acceptsParent (self, *args, **kwargs):
      '''
acceptsParent( (UVView)arg1, (GraphComponent)arg2) -> bool :

    C++ signature :
        bool acceptsParent(GafferSceneUI::UVView,Gaffer::GraphComponent const*)'''
    ...
    def addChild (self, *args, **kwargs):
      '''
addChild( (GraphComponent)arg1, (GraphComponent)arg2) -> None :

    C++ signature :
        void addChild(Gaffer::GraphComponent {lvalue},Gaffer::GraphComponent {lvalue})'''
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
    def contextChangedSignal (self, *args, **kwargs):
      '''
contextChangedSignal( (View)arg1) -> UnarySignal :

    C++ signature :
        Gaffer::Signals::Signal<void (Gaffer::GraphComponent*), Gaffer::Signals::CatchingCombiner<void> > {lvalue} contextChangedSignal(GafferUI::View {lvalue})'''
    ...
    def create (self, *args, **kwargs):
      '''
create( (object)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<GafferUI::View> create(boost::intrusive_ptr<Gaffer::Plug>)'''
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
    def editScope (self, *args, **kwargs):
      '''
editScope( (View)arg1) -> object :

    C++ signature :
        Gaffer::EditScope* editScope(GafferUI::View {lvalue})'''
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
getContext( (View)arg1) -> object :

    C++ signature :
        Gaffer::Context* getContext(GafferUI::View {lvalue})'''
    ...
    def getName (self, *args, **kwargs):
      '''
getName( (GraphComponent)arg1) -> str :

    C++ signature :
        char const* getName(Gaffer::GraphComponent {lvalue})'''
    ...
    def getPaused (self, *args, **kwargs):
      '''
getPaused( (UVView)arg1) -> bool :

    C++ signature :
        bool getPaused(GafferSceneUI::UVView {lvalue})'''
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
isInstanceOf( (UVView)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(GafferSceneUI::UVView {lvalue},IECore::TypeId)

isInstanceOf( (UVView)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(GafferSceneUI::UVView {lvalue},char const*)'''
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
    def registerView (self, *args, **kwargs):
      '''
registerView( (TypeId)arg1, (object)arg2) -> None :

    C++ signature :
        void registerView(IECore::TypeId,boost::python::api::object)

registerView( (TypeId)arg1, (object)arg2, (object)arg3) -> None :

    C++ signature :
        void registerView(IECore::TypeId,std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >,boost::python::api::object)'''
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
setContext( (View)arg1, (object)arg2) -> None :

    C++ signature :
        void setContext(GafferUI::View {lvalue},boost::intrusive_ptr<Gaffer::Context>)'''
    ...
    def setName (self, *args, **kwargs):
      '''
setName( (GraphComponent)arg1, (InternedString)arg2) -> str :

    C++ signature :
        char const* setName(Gaffer::GraphComponent {lvalue},IECore::InternedString)'''
    ...
    def setPaused (self, *args, **kwargs):
      '''
setPaused( (UVView)arg1, (bool)arg2) -> None :

    C++ signature :
        void setPaused(GafferSceneUI::UVView {lvalue},bool)'''
    ...
    def state (self, *args, **kwargs):
      '''
state( (UVView)arg1) -> State :

    C++ signature :
        GafferSceneUI::UVView::State state(GafferSceneUI::UVView {lvalue})'''
    ...
    def stateChangedSignal (self, *args, **kwargs):
      '''
stateChangedSignal( (UVView)arg1) -> UVViewSignal :

    C++ signature :
        Gaffer::Signals::Signal<void (GafferSceneUI::UVView*), Gaffer::Signals::DefaultCombiner<void> > {lvalue} stateChangedSignal(GafferSceneUI::UVView {lvalue})'''
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
typeId( (UVView)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(GafferSceneUI::UVView {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (UVView)arg1) -> str :

    C++ signature :
        char const* typeName(GafferSceneUI::UVView {lvalue})'''
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
    def viewportGadget (self, *args, **kwargs):
      '''
viewportGadget( (View)arg1) -> object :

    C++ signature :
        GafferUI::ViewportGadget* viewportGadget(GafferUI::View {lvalue})'''
    ...

def UnencapsulateUI (*args):
      '''

'''      
    ...

def UnionFilterUI (*args):
      '''

'''      
    ...

def WireframeUI (*args):
      '''

'''      
    ...

def _GafferSceneUI (*args):
      '''

'''      
    ...

def _HistoryWindow (*args):
      '''

'''      
    ...

def _SceneViewInspector (*args):
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
