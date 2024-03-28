
def TractorDispatcher (*args):
      '''

'''      
    ...

class TractorDispatcher:
    def BinaryPlugSignal (self, *args, **kwargs):
      '''None'''
    ...
    def BinarySignal (self, *args, **kwargs):
      '''None'''
    ...
    def DispatchSignal (self, *args, **kwargs):
      '''None'''
    ...
    def ErrorSignal (self, *args, **kwargs):
      '''None'''
    ...
    def FramesMode (self, *args, **kwargs):
      '''None'''
    ...
    def NameChangedSignal (self, *args, **kwargs):
      '''None'''
    ...
    def PostDispatchSignal (self, *args, **kwargs):
      '''None'''
    ...
    def PreDispatchSignal (self, *args, **kwargs):
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
    def _TaskBatch (self, *args, **kwargs):
      '''None'''
    ...
    def _TractorDispatcher__acquireTask (self, batch, dispatchData):
      '''None'''
    ...
    def _TractorDispatcher__buildJobWalk (self, tractorParent, batch, dispatchData):
      '''None'''
    ...
    def _TractorDispatcher__preSpoolSignal (self, *args, **kwargs):
      '''None'''
    ...
    def _doDispatch (self, rootBatch):
      '''None'''
    ...
    def _setupPlugs (parentPlug):
      '''None'''
    ...
    def acceptsChild (self, *args, **kwargs):
      '''
acceptsChild( (Dispatcher)arg1, (GraphComponent)arg2) -> bool :

    C++ signature :
        bool acceptsChild(GafferDispatch::Dispatcher,Gaffer::GraphComponent const*)'''
    ...
    def acceptsParent (self, *args, **kwargs):
      '''
acceptsParent( (Dispatcher)arg1, (GraphComponent)arg2) -> bool :

    C++ signature :
        bool acceptsParent(GafferDispatch::Dispatcher,Gaffer::GraphComponent const*)'''
    ...
    def addChild (self, *args, **kwargs):
      '''
addChild( (GraphComponent)arg1, (GraphComponent)arg2) -> None :

    C++ signature :
        void addChild(Gaffer::GraphComponent {lvalue},Gaffer::GraphComponent {lvalue})'''
    ...
    def affects (self, *args, **kwargs):
      '''
affects( (TaskNode)arg1, (Plug)arg2) -> list :

    C++ signature :
        boost::python::list affects(GafferDispatch::TaskNode,Gaffer::Plug const*)'''
    ...
    def affectsTask (self, *args, **kwargs):
      '''
affectsTask( (TaskNode)arg1, (Plug)arg2) -> bool :

    C++ signature :
        bool affectsTask(GafferDispatch::TaskNode {lvalue},Gaffer::Plug const*)'''
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
correspondingInput( (TaskNode)arg1, (Plug)arg2) -> object :

    C++ signature :
        boost::intrusive_ptr<Gaffer::Plug> correspondingInput(GafferDispatch::TaskNode {lvalue},Gaffer::Plug const*)'''
    ...
    def create (self, *args, **kwargs):
      '''
create( (object)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<GafferDispatch::Dispatcher> create(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)'''
    ...
    def deregisterDispatcher (self, *args, **kwargs):
      '''
deregisterDispatcher( (object)dispatcherType) -> None :

    C++ signature :
        void deregisterDispatcher(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)'''
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
    def dispatch (self, nodes):
      '''None'''
    ...
    def dispatchSignal (self, *args, **kwargs):
      '''
dispatchSignal() -> DispatchSignal :

    C++ signature :
        Gaffer::Signals::Signal<void (GafferDispatch::Dispatcher const*), Gaffer::Signals::CatchingCombiner<void> > {lvalue} dispatchSignal()'''
    ...
    def enabledPlug (self, *args, **kwargs):
      '''
enabledPlug( (TaskNode)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<Gaffer::TypedPlug<bool> > enabledPlug(GafferDispatch::TaskNode {lvalue})'''
    ...
    def errorSignal (self, *args, **kwargs):
      '''
errorSignal( (Node)arg1) -> ErrorSignal :

    C++ signature :
        Gaffer::Signals::Signal<void (Gaffer::Plug const*, Gaffer::Plug const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&), Gaffer::Signals::CatchingCombiner<void> > {lvalue} errorSignal(Gaffer::Node {lvalue})'''
    ...
    def execute (self, *args, **kwargs):
      '''
execute( (TaskNode)arg1) -> None :

    C++ signature :
        void execute(GafferDispatch::TaskNode {lvalue})'''
    ...
    def executeSequence (self, *args, **kwargs):
      '''
executeSequence( (TaskNode)arg1, (object)arg2) -> None :

    C++ signature :
        void executeSequence(GafferDispatch::TaskNode {lvalue},boost::python::api::object)'''
    ...
    def frameRange (self, script=None, context=None):
      '''None'''
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
    def getDefaultDispatcherType (self, *args, **kwargs):
      '''
getDefaultDispatcherType() -> str :

    C++ signature :
        std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > getDefaultDispatcherType()'''
    ...
    def getName (self, *args, **kwargs):
      '''
getName( (GraphComponent)arg1) -> str :

    C++ signature :
        char const* getName(Gaffer::GraphComponent {lvalue})'''
    ...
    def hash (self, *args, **kwargs):
      '''
hash( (TaskNode)arg1, (Context)arg2) -> MurmurHash :

    C++ signature :
        IECore::MurmurHash hash(GafferDispatch::TaskNode {lvalue},Gaffer::Context const*)'''
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
    def jobDirectory (self, *args, **kwargs):
      '''
jobDirectory( (Dispatcher)arg1) -> object :

    C++ signature :
        std::filesystem::__cxx11::path jobDirectory(GafferDispatch::Dispatcher {lvalue})'''
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
    def postDispatchSignal (self, *args, **kwargs):
      '''
postDispatchSignal() -> PostDispatchSignal :

    C++ signature :
        Gaffer::Signals::Signal<void (GafferDispatch::Dispatcher const*, bool), Gaffer::Signals::CatchingCombiner<void> > {lvalue} postDispatchSignal()'''
    ...
    def postTasks (self, *args, **kwargs):
      '''
postTasks( (TaskNode)arg1, (Context)arg2) -> list :

    C++ signature :
        boost::python::list postTasks(GafferDispatch::TaskNode {lvalue},Gaffer::Context*)'''
    ...
    def preDispatchSignal (self, *args, **kwargs):
      '''
preDispatchSignal() -> PreDispatchSignal :

    C++ signature :
        Gaffer::Signals::Signal<bool (GafferDispatch::Dispatcher const*), GafferDispatch::Detail::PreDispatchSignalCombiner> {lvalue} preDispatchSignal()'''
    ...
    def preSpoolSignal ():
      '''None'''
    ...
    def preTasks (self, *args, **kwargs):
      '''
preTasks( (TaskNode)arg1, (Context)arg2) -> list :

    C++ signature :
        boost::python::list preTasks(GafferDispatch::TaskNode {lvalue},Gaffer::Context*)'''
    ...
    def refCount (self, *args, **kwargs):
      '''
refCount( (RefCounted)arg1) -> int :

    C++ signature :
        unsigned long refCount(IECore::RefCounted {lvalue})'''
    ...
    def registerDispatcher (self, *args, **kwargs):
      '''
registerDispatcher( (object)dispatcherType, (object)creator [, (object)setupPlugsFn=0]) -> None :

    C++ signature :
        void registerDispatcher(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >,boost::python::api::object [,boost::python::api::object=0])'''
    ...
    def registerType (self, *args, **kwargs):
      '''
registerType( (TypeId)arg1, (str)arg2, (TypeId)arg3) -> None :

    C++ signature :
        void registerType(IECore::TypeId,char const*,IECore::TypeId)'''
    ...
    def registeredDispatchers (self, *args, **kwargs):
      '''
registeredDispatchers() -> tuple :

    C++ signature :
        boost::python::tuple registeredDispatchers()'''
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
requiresSequenceExecution( (TaskNode)arg1) -> bool :

    C++ signature :
        bool requiresSequenceExecution(GafferDispatch::TaskNode {lvalue})'''
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
    def setDefaultDispatcherType (self, *args, **kwargs):
      '''
setDefaultDispatcherType( (object)arg1) -> None :

    C++ signature :
        void setDefaultDispatcherType(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)'''
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

def tractorAPI (*args):
      '''

'''      
    ...
