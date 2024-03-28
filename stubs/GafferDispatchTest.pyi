
def DebugDispatcher (*args):
      '''

'''      
    ...

class DebugDispatcher:
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
    def _DebugDispatcher__acquireNode (self, batch, dispatchData):
      '''None'''
    ...
    def _DebugDispatcher__buildGraphWalk (self, parentNode, batch, dispatchData):
      '''None'''
    ...
    def _DebugDispatcher__createNode (name):
      '''None'''
    ...
    def _TaskBatch (self, *args, **kwargs):
      '''None'''
    ...
    def _doDispatch (self, rootBatch):
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

def DispatchApplicationTest (*args):
      '''

'''      
    ...

class DispatchApplicationTest:
    def _TestCase__nodeHasDescription (self, node):
      '''None'''
    ...
    def _TestCase__undocumentedPlugs (self, node, additionalTerminalPlugTypes=()):
      '''None'''
    ...
    def _addExpectedFailure (self, result, exc_info):
      '''None'''
    ...
    def _addSkip (self, result, test_case, reason):
      '''None'''
    ...
    def _addUnexpectedSuccess (self, result):
      '''None'''
    ...
    def _baseAssertEqual (self, first, second, msg=None):
      '''The default assertEqual implementation, not type specific.'''
    ...
    def _callCleanup (self, function, /, *args, **kwargs):
      '''None'''
    ...
    def _callSetUp (self):
      '''None'''
    ...
    def _callTearDown (self):
      '''None'''
    ...
    def _callTestMethod (self, method):
      '''None'''
    ...
    def _classSetupFailed (self, *args, **kwargs):
      '''bool(x) -> bool

Returns True when the argument x is true, False otherwise.
The builtins True and False are the only two instances of the class bool.
The class bool is a subclass of the class int, and cannot be subclassed.'''
    ...
    def _class_cleanups (self, *args, **kwargs):
      '''Built-in mutable sequence.

If no argument is given, the constructor creates a new empty list.
The argument must be an iterable if specified.'''
    ...
    def _deprecate (original_func):
      '''None'''
    ...
    def _diffThreshold (self, *args, **kwargs):
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
    def _feedErrorsToResult (self, result, errors):
      '''None'''
    ...
    def _formatMessage (self, msg, standardMsg):
      '''Honour the longMessage attribute when generating failure messages.
        If longMessage is False this means:
        * Use only an explicit message if it is provided
        * Otherwise use the standard message for the assert

        If longMessage is True:
        * Use the standard message
        * If an explicit message is provided, plus ' : ' and the explicit message
        '''
    ...
    def _getAssertEqualityFunc (self, first, second):
      '''Get a detailed comparison function for the types of the two args.

        Returns: A callable accepting (first, second, msg=None) that will
        raise a failure exception if first != second with a useful human
        readable error message for those types.
        '''
    ...
    def _truncateMessage (self, message, diff):
      '''None'''
    ...
    def addClassCleanup (function, /, *args, **kwargs):
      '''Same as addCleanup, except the cleanup items are called even if
        setUpClass fails (unlike tearDownClass).'''
    ...
    def addCleanup (self, function, /, *args, **kwargs):
      '''Add a function, with arguments, to be called when the test is
        completed. Functions added are called on a LIFO basis and are
        called after tearDown on test failure or success.

        Cleanup items are called even if setUp fails (unlike tearDown).'''
    ...
    def addTypeEqualityFunc (self, typeobj, function):
      '''Add a type specific assertEqual style function to compare a type.

        This method is for use by TestCase subclasses that need to register
        their own type equality functions to provide nicer error messages.

        Args:
            typeobj: The data type to call this function on when both values
                    are of the same type in assertEqual().
            function: The callable taking two arguments and an optional
                    msg= argument that raises self.failureException with a
                    useful error message when the two arguments are not equal.
        '''
    ...
    def assertAlmostEqual (self, first, second, places=None, msg=None, delta=None):
      '''Fail if the two objects are unequal as determined by their
           difference rounded to the given number of decimal places
           (default 7) and comparing to zero, or by comparing that the
           difference between the two objects is more than the given
           delta.

           Note that decimal places (from zero) are usually not the same
           as significant digits (measured from the most significant digit).

           If the two objects compare equal then they will automatically
           compare almost equal.
        '''
    ...
    def assertAlmostEquals (*args, **kwargs):
      '''None'''
    ...
    def assertCountEqual (self, first, second, msg=None):
      '''Asserts that two iterables have the same elements, the same number of
        times, without regard to order.

            self.assertEqual(Counter(list(first)),
                             Counter(list(second)))

         Example:
            - [0, 1, 1] and [1, 0, 1] compare equal.
            - [0, 0, 1] and [0, 1] compare unequal.

        '''
    ...
    def assertDefaultNamesAreCorrect (self, module, namesToIgnore=()):
      '''None'''
    ...
    def assertDictContainsSubset (self, subset, dictionary, msg=None):
      '''Checks whether dictionary is a superset of subset.'''
    ...
    def assertDictEqual (self, d1, d2, msg=None):
      '''None'''
    ...
    def assertEqual (self, first, second, msg=None):
      '''Fail if the two objects are unequal as determined by the '=='
           operator.
        '''
    ...
    def assertEquals (*args, **kwargs):
      '''None'''
    ...
    def assertFalse (self, expr, msg=None):
      '''Check that the expression is false.'''
    ...
    def assertFloat32Equal (self, value0, value1):
      '''None'''
    ...
    def assertGreater (self, a, b, msg=None):
      '''Just like self.assertTrue(a > b), but with a nicer default message.'''
    ...
    def assertGreaterEqual (self, a, b, msg=None):
      '''Just like self.assertTrue(a >= b), but with a nicer default message.'''
    ...
    def assertHashesValid (self, node, inputsToIgnore=[], outputsToIgnore=[]):
      '''None'''
    ...
    def assertIn (self, member, container, msg=None):
      '''Just like self.assertTrue(a in b), but with a nicer default message.'''
    ...
    def assertIs (self, expr1, expr2, msg=None):
      '''Just like self.assertTrue(a is b), but with a nicer default message.'''
    ...
    def assertIsInstance (self, obj, cls, msg=None):
      '''Same as self.assertTrue(isinstance(obj, cls)), with a nicer
        default message.'''
    ...
    def assertIsNone (self, obj, msg=None):
      '''Same as self.assertTrue(obj is None), with a nicer default message.'''
    ...
    def assertIsNot (self, expr1, expr2, msg=None):
      '''Just like self.assertTrue(a is not b), but with a nicer default message.'''
    ...
    def assertIsNotNone (self, obj, msg=None):
      '''Included for symmetry with assertIsNone.'''
    ...
    def assertLess (self, a, b, msg=None):
      '''Just like self.assertTrue(a < b), but with a nicer default message.'''
    ...
    def assertLessEqual (self, a, b, msg=None):
      '''Just like self.assertTrue(a <= b), but with a nicer default message.'''
    ...
    def assertListEqual (self, list1, list2, msg=None):
      '''A list-specific equality assertion.

        Args:
            list1: The first list to compare.
            list2: The second list to compare.
            msg: Optional message to use on failure instead of a list of
                    differences.

        '''
    ...
    def assertLogs (self, logger=None, level=None):
      '''Fail unless a log message of level *level* or higher is emitted
        on *logger_name* or its children.  If omitted, *level* defaults to
        INFO and *logger* defaults to the root logger.

        This method must be used as a context manager, and will yield
        a recording object with two attributes: `output` and `records`.
        At the end of the context manager, the `output` attribute will
        be a list of the matching formatted log messages and the
        `records` attribute will be a list of the corresponding LogRecord
        objects.

        Example::

            with self.assertLogs('foo', level='INFO') as cm:
                logging.getLogger('foo').info('first message')
                logging.getLogger('foo.bar').error('second message')
            self.assertEqual(cm.output, ['INFO:foo:first message',
                                         'ERROR:foo.bar:second message'])
        '''
    ...
    def assertModuleDoesNotImportUI (self, moduleName):
      '''None'''
    ...
    def assertMultiLineEqual (self, first, second, msg=None):
      '''Assert that two multi-line strings are equal.'''
    ...
    def assertNoLogs (self, logger=None, level=None):
      ''' Fail unless no log messages of level *level* or higher are emitted
        on *logger_name* or its children.

        This method must be used as a context manager.
        '''
    ...
    def assertNodeIsDocumented (self, node, additionalTerminalPlugTypes=()):
      '''None'''
    ...
    def assertNodesAreDocumented (self, module, additionalTerminalPlugTypes=(), nodesToIgnore=None):
      '''None'''
    ...
    def assertNodesConstructWithDefaultValues (self, module, nodesToIgnore=None, plugsToIgnore=None):
      '''None'''
    ...
    def assertNotAlmostEqual (self, first, second, places=None, msg=None, delta=None):
      '''Fail if the two objects are equal as determined by their
           difference rounded to the given number of decimal places
           (default 7) and comparing to zero, or by comparing that the
           difference between the two objects is less than the given delta.

           Note that decimal places (from zero) are usually not the same
           as significant digits (measured from the most significant digit).

           Objects that are equal automatically fail.
        '''
    ...
    def assertNotAlmostEquals (*args, **kwargs):
      '''None'''
    ...
    def assertNotEqual (self, first, second, msg=None):
      '''Fail if the two objects are equal as determined by the '!='
           operator.
        '''
    ...
    def assertNotEquals (*args, **kwargs):
      '''None'''
    ...
    def assertNotIn (self, member, container, msg=None):
      '''Just like self.assertTrue(a not in b), but with a nicer default message.'''
    ...
    def assertNotIsInstance (self, obj, cls, msg=None):
      '''Included for symmetry with assertIsInstance.'''
    ...
    def assertNotRegex (self, text, unexpected_regex, msg=None):
      '''Fail the test if the text matches the regular expression.'''
    ...
    def assertNotRegexpMatches (*args, **kwargs):
      '''None'''
    ...
    def assertRaises (self, expected_exception, *args, **kwargs):
      '''Fail unless an exception of class expected_exception is raised
           by the callable when invoked with specified positional and
           keyword arguments. If a different type of exception is
           raised, it will not be caught, and the test case will be
           deemed to have suffered an error, exactly as for an
           unexpected exception.

           If called with the callable and arguments omitted, will return a
           context object used like this::

                with self.assertRaises(SomeException):
                    do_something()

           An optional keyword argument 'msg' can be provided when assertRaises
           is used as a context object.

           The context manager keeps a reference to the exception as
           the 'exception' attribute. This allows you to inspect the
           exception after the assertion::

               with self.assertRaises(SomeException) as cm:
                   do_something()
               the_exception = cm.exception
               self.assertEqual(the_exception.error_code, 3)
        '''
    ...
    def assertRaisesRegex (self, expected_exception, expected_regex, *args, **kwargs):
      '''Asserts that the message in a raised exception matches a regex.

        Args:
            expected_exception: Exception class expected to be raised.
            expected_regex: Regex (re.Pattern object or string) expected
                    to be found in error message.
            args: Function to be called and extra positional args.
            kwargs: Extra kwargs.
            msg: Optional message used in case of failure. Can only be used
                    when assertRaisesRegex is used as a context manager.
        '''
    ...
    def assertRaisesRegexp (*args, **kwargs):
      '''None'''
    ...
    def assertRegex (self, text, expected_regex, msg=None):
      '''Fail the test unless the text matches the regular expression.'''
    ...
    def assertRegexpMatches (*args, **kwargs):
      '''None'''
    ...
    def assertSequenceEqual (self, seq1, seq2, msg=None, seq_type=None):
      '''An equality assertion for ordered sequences (like lists and tuples).

        For the purposes of this function, a valid ordered sequence type is one
        which can be indexed, has a length, and has an equality operator.

        Args:
            seq1: The first sequence to compare.
            seq2: The second sequence to compare.
            seq_type: The expected datatype of the sequences, or None if no
                    datatype should be enforced.
            msg: Optional message to use on failure instead of a list of
                    differences.
        '''
    ...
    def assertSetEqual (self, set1, set2, msg=None):
      '''A set-specific equality assertion.

        Args:
            set1: The first set to compare.
            set2: The second set to compare.
            msg: Optional message to use on failure instead of a list of
                    differences.

        assertSetEqual uses ducktyping to support different types of sets, and
        is optimized for sets specifically (parameters must support a
        difference method).
        '''
    ...
    def assertTrue (self, expr, msg=None):
      '''Check that the expression is true.'''
    ...
    def assertTupleEqual (self, tuple1, tuple2, msg=None):
      '''A tuple-specific equality assertion.

        Args:
            tuple1: The first tuple to compare.
            tuple2: The second tuple to compare.
            msg: Optional message to use on failure instead of a list of
                    differences.
        '''
    ...
    def assertTypeNamesArePrefixed (self, module, namesToIgnore=()):
      '''None'''
    ...
    def assertWarns (self, expected_warning, *args, **kwargs):
      '''Fail unless a warning of class warnClass is triggered
           by the callable when invoked with specified positional and
           keyword arguments.  If a different type of warning is
           triggered, it will not be handled: depending on the other
           warning filtering rules in effect, it might be silenced, printed
           out, or raised as an exception.

           If called with the callable and arguments omitted, will return a
           context object used like this::

                with self.assertWarns(SomeWarning):
                    do_something()

           An optional keyword argument 'msg' can be provided when assertWarns
           is used as a context object.

           The context manager keeps a reference to the first matching
           warning as the 'warning' attribute; similarly, the 'filename'
           and 'lineno' attributes give you information about the line
           of Python code from which the warning was triggered.
           This allows you to inspect the warning after the assertion::

               with self.assertWarns(SomeWarning) as cm:
                   do_something()
               the_warning = cm.warning
               self.assertEqual(the_warning.some_attribute, 147)
        '''
    ...
    def assertWarnsRegex (self, expected_warning, expected_regex, *args, **kwargs):
      '''Asserts that the message in a triggered warning matches a regexp.
        Basic functioning is similar to assertWarns() with the addition
        that only warnings whose messages also match the regular expression
        are considered successful matches.

        Args:
            expected_warning: Warning class expected to be triggered.
            expected_regex: Regex (re.Pattern object or string) expected
                    to be found in error message.
            args: Function to be called and extra positional args.
            kwargs: Extra kwargs.
            msg: Optional message used in case of failure. Can only be used
                    when assertWarnsRegex is used as a context manager.
        '''
    ...
    def assert_ (*args, **kwargs):
      '''None'''
    ...
    def countTestCases (self):
      '''None'''
    ...
    def debug (self):
      '''Run the test without collecting errors in a TestResult'''
    ...
    def defaultTestResult (self):
      '''None'''
    ...
    def doClassCleanups ():
      '''Execute all class cleanup functions. Normally called for you after
        tearDownClass.'''
    ...
    def doCleanups (self):
      '''Execute all cleanup functions. Normally called for you after
        tearDown.'''
    ...
    def fail (self, msg=None):
      '''Fail immediately, with the given message.'''
    ...
    def failIf (*args, **kwargs):
      '''None'''
    ...
    def failIfAlmostEqual (*args, **kwargs):
      '''None'''
    ...
    def failIfEqual (*args, **kwargs):
      '''None'''
    ...
    def failUnless (*args, **kwargs):
      '''None'''
    ...
    def failUnlessAlmostEqual (*args, **kwargs):
      '''None'''
    ...
    def failUnlessEqual (*args, **kwargs):
      '''None'''
    ...
    def failUnlessRaises (*args, **kwargs):
      '''None'''
    ...
    def failureException (self, *args, **kwargs):
      '''Assertion failed.'''
    ...
    def failureMessageLevel (self, *args, **kwargs):
      '''None'''
    ...
    def id (self):
      '''None'''
    ...
    def ignoreMessage (self, level, context, message):
      '''None'''
    ...
    def longMessage (self, *args, **kwargs):
      '''bool(x) -> bool

Returns True when the argument x is true, False otherwise.
The builtins True and False are the only two instances of the class bool.
The class bool is a subclass of the class int, and cannot be subclassed.'''
    ...
    def maxDiff (self, *args, **kwargs):
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
    def run (self, result=None):
      '''None'''
    ...
    def scopedLocale (l, category=0):
      '''None'''
    ...
    def setUp (self):
      '''None'''
    ...
    def setUpClass ():
      '''Hook method for setting up class fixture before running tests in the class.'''
    ...
    def shortDescription (self):
      '''Returns a one-line description of the test, or None if no
        description has been provided.

        The default implementation of this method returns the first line of
        the specified test method's docstring.
        '''
    ...
    def skipTest (self, reason):
      '''Skip this test.'''
    ...
    def subTest (self, msg=<object object at 0x7fb108120c10>, **params):
      '''Return a context manager that will return the enclosed block
        of code in a subtest identified by the optional message and
        keyword parameters.  A failure in the subtest marks the test
        case as failed but resumes execution at the end of the enclosed
        block, allowing further test code to be executed.
        '''
    ...
    def tearDown (self):
      '''None'''
    ...
    def tearDownClass ():
      '''Hook method for deconstructing the class fixture after running all tests in the class.'''
    ...
    def temporaryDirectory (self):
      '''None'''
    ...
    def testApplyUserDefaults (self):
      '''None'''
    ...
    def testBox (self):
      '''None'''
    ...
    def testContextVariables (self):
      '''None'''
    ...
    def testDispatcherOverrides (self):
      '''None'''
    ...
    def testErrorReturnStatus (self):
      '''None'''
    ...
    def testMultipleNodes (self):
      '''None'''
    ...
    def testNodesWithoutScript (self):
      '''None'''
    ...
    def testScript (self):
      '''None'''
    ...
    def testScriptLoadErrors (self):
      '''None'''
    ...
    def waitForCommand (self, command):
      '''None'''
    ...
    def writeSimpleScript (self):
      '''None'''
    ...

def DispatcherTest (*args):
      '''

'''      
    ...

class DispatcherTest:
    def NullDispatcher ():
      '''None'''
    ...
    def TestDispatcher ():
      '''None'''
    ...
    def _TestCase__nodeHasDescription (self, node):
      '''None'''
    ...
    def _TestCase__undocumentedPlugs (self, node, additionalTerminalPlugTypes=()):
      '''None'''
    ...
    def _addExpectedFailure (self, result, exc_info):
      '''None'''
    ...
    def _addSkip (self, result, test_case, reason):
      '''None'''
    ...
    def _addUnexpectedSuccess (self, result):
      '''None'''
    ...
    def _baseAssertEqual (self, first, second, msg=None):
      '''The default assertEqual implementation, not type specific.'''
    ...
    def _callCleanup (self, function, /, *args, **kwargs):
      '''None'''
    ...
    def _callSetUp (self):
      '''None'''
    ...
    def _callTearDown (self):
      '''None'''
    ...
    def _callTestMethod (self, method):
      '''None'''
    ...
    def _classSetupFailed (self, *args, **kwargs):
      '''bool(x) -> bool

Returns True when the argument x is true, False otherwise.
The builtins True and False are the only two instances of the class bool.
The class bool is a subclass of the class int, and cannot be subclassed.'''
    ...
    def _class_cleanups (self, *args, **kwargs):
      '''Built-in mutable sequence.

If no argument is given, the constructor creates a new empty list.
The argument must be an iterable if specified.'''
    ...
    def _deprecate (original_func):
      '''None'''
    ...
    def _diffThreshold (self, *args, **kwargs):
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
    def _feedErrorsToResult (self, result, errors):
      '''None'''
    ...
    def _formatMessage (self, msg, standardMsg):
      '''Honour the longMessage attribute when generating failure messages.
        If longMessage is False this means:
        * Use only an explicit message if it is provided
        * Otherwise use the standard message for the assert

        If longMessage is True:
        * Use the standard message
        * If an explicit message is provided, plus ' : ' and the explicit message
        '''
    ...
    def _getAssertEqualityFunc (self, first, second):
      '''Get a detailed comparison function for the types of the two args.

        Returns: A callable accepting (first, second, msg=None) that will
        raise a failure exception if first != second with a useful human
        readable error message for those types.
        '''
    ...
    def _truncateMessage (self, message, diff):
      '''None'''
    ...
    def addClassCleanup (function, /, *args, **kwargs):
      '''Same as addCleanup, except the cleanup items are called even if
        setUpClass fails (unlike tearDownClass).'''
    ...
    def addCleanup (self, function, /, *args, **kwargs):
      '''Add a function, with arguments, to be called when the test is
        completed. Functions added are called on a LIFO basis and are
        called after tearDown on test failure or success.

        Cleanup items are called even if setUp fails (unlike tearDown).'''
    ...
    def addTypeEqualityFunc (self, typeobj, function):
      '''Add a type specific assertEqual style function to compare a type.

        This method is for use by TestCase subclasses that need to register
        their own type equality functions to provide nicer error messages.

        Args:
            typeobj: The data type to call this function on when both values
                    are of the same type in assertEqual().
            function: The callable taking two arguments and an optional
                    msg= argument that raises self.failureException with a
                    useful error message when the two arguments are not equal.
        '''
    ...
    def assertAlmostEqual (self, first, second, places=None, msg=None, delta=None):
      '''Fail if the two objects are unequal as determined by their
           difference rounded to the given number of decimal places
           (default 7) and comparing to zero, or by comparing that the
           difference between the two objects is more than the given
           delta.

           Note that decimal places (from zero) are usually not the same
           as significant digits (measured from the most significant digit).

           If the two objects compare equal then they will automatically
           compare almost equal.
        '''
    ...
    def assertAlmostEquals (*args, **kwargs):
      '''None'''
    ...
    def assertCountEqual (self, first, second, msg=None):
      '''Asserts that two iterables have the same elements, the same number of
        times, without regard to order.

            self.assertEqual(Counter(list(first)),
                             Counter(list(second)))

         Example:
            - [0, 1, 1] and [1, 0, 1] compare equal.
            - [0, 0, 1] and [0, 1] compare unequal.

        '''
    ...
    def assertDefaultNamesAreCorrect (self, module, namesToIgnore=()):
      '''None'''
    ...
    def assertDictContainsSubset (self, subset, dictionary, msg=None):
      '''Checks whether dictionary is a superset of subset.'''
    ...
    def assertDictEqual (self, d1, d2, msg=None):
      '''None'''
    ...
    def assertEqual (self, first, second, msg=None):
      '''Fail if the two objects are unequal as determined by the '=='
           operator.
        '''
    ...
    def assertEquals (*args, **kwargs):
      '''None'''
    ...
    def assertFalse (self, expr, msg=None):
      '''Check that the expression is false.'''
    ...
    def assertFloat32Equal (self, value0, value1):
      '''None'''
    ...
    def assertGreater (self, a, b, msg=None):
      '''Just like self.assertTrue(a > b), but with a nicer default message.'''
    ...
    def assertGreaterEqual (self, a, b, msg=None):
      '''Just like self.assertTrue(a >= b), but with a nicer default message.'''
    ...
    def assertHashesValid (self, node, inputsToIgnore=[], outputsToIgnore=[]):
      '''None'''
    ...
    def assertIn (self, member, container, msg=None):
      '''Just like self.assertTrue(a in b), but with a nicer default message.'''
    ...
    def assertIs (self, expr1, expr2, msg=None):
      '''Just like self.assertTrue(a is b), but with a nicer default message.'''
    ...
    def assertIsInstance (self, obj, cls, msg=None):
      '''Same as self.assertTrue(isinstance(obj, cls)), with a nicer
        default message.'''
    ...
    def assertIsNone (self, obj, msg=None):
      '''Same as self.assertTrue(obj is None), with a nicer default message.'''
    ...
    def assertIsNot (self, expr1, expr2, msg=None):
      '''Just like self.assertTrue(a is not b), but with a nicer default message.'''
    ...
    def assertIsNotNone (self, obj, msg=None):
      '''Included for symmetry with assertIsNone.'''
    ...
    def assertLess (self, a, b, msg=None):
      '''Just like self.assertTrue(a < b), but with a nicer default message.'''
    ...
    def assertLessEqual (self, a, b, msg=None):
      '''Just like self.assertTrue(a <= b), but with a nicer default message.'''
    ...
    def assertListEqual (self, list1, list2, msg=None):
      '''A list-specific equality assertion.

        Args:
            list1: The first list to compare.
            list2: The second list to compare.
            msg: Optional message to use on failure instead of a list of
                    differences.

        '''
    ...
    def assertLogs (self, logger=None, level=None):
      '''Fail unless a log message of level *level* or higher is emitted
        on *logger_name* or its children.  If omitted, *level* defaults to
        INFO and *logger* defaults to the root logger.

        This method must be used as a context manager, and will yield
        a recording object with two attributes: `output` and `records`.
        At the end of the context manager, the `output` attribute will
        be a list of the matching formatted log messages and the
        `records` attribute will be a list of the corresponding LogRecord
        objects.

        Example::

            with self.assertLogs('foo', level='INFO') as cm:
                logging.getLogger('foo').info('first message')
                logging.getLogger('foo.bar').error('second message')
            self.assertEqual(cm.output, ['INFO:foo:first message',
                                         'ERROR:foo.bar:second message'])
        '''
    ...
    def assertModuleDoesNotImportUI (self, moduleName):
      '''None'''
    ...
    def assertMultiLineEqual (self, first, second, msg=None):
      '''Assert that two multi-line strings are equal.'''
    ...
    def assertNoLogs (self, logger=None, level=None):
      ''' Fail unless no log messages of level *level* or higher are emitted
        on *logger_name* or its children.

        This method must be used as a context manager.
        '''
    ...
    def assertNodeIsDocumented (self, node, additionalTerminalPlugTypes=()):
      '''None'''
    ...
    def assertNodesAreDocumented (self, module, additionalTerminalPlugTypes=(), nodesToIgnore=None):
      '''None'''
    ...
    def assertNodesConstructWithDefaultValues (self, module, nodesToIgnore=None, plugsToIgnore=None):
      '''None'''
    ...
    def assertNotAlmostEqual (self, first, second, places=None, msg=None, delta=None):
      '''Fail if the two objects are equal as determined by their
           difference rounded to the given number of decimal places
           (default 7) and comparing to zero, or by comparing that the
           difference between the two objects is less than the given delta.

           Note that decimal places (from zero) are usually not the same
           as significant digits (measured from the most significant digit).

           Objects that are equal automatically fail.
        '''
    ...
    def assertNotAlmostEquals (*args, **kwargs):
      '''None'''
    ...
    def assertNotEqual (self, first, second, msg=None):
      '''Fail if the two objects are equal as determined by the '!='
           operator.
        '''
    ...
    def assertNotEquals (*args, **kwargs):
      '''None'''
    ...
    def assertNotIn (self, member, container, msg=None):
      '''Just like self.assertTrue(a not in b), but with a nicer default message.'''
    ...
    def assertNotIsInstance (self, obj, cls, msg=None):
      '''Included for symmetry with assertIsInstance.'''
    ...
    def assertNotRegex (self, text, unexpected_regex, msg=None):
      '''Fail the test if the text matches the regular expression.'''
    ...
    def assertNotRegexpMatches (*args, **kwargs):
      '''None'''
    ...
    def assertRaises (self, expected_exception, *args, **kwargs):
      '''Fail unless an exception of class expected_exception is raised
           by the callable when invoked with specified positional and
           keyword arguments. If a different type of exception is
           raised, it will not be caught, and the test case will be
           deemed to have suffered an error, exactly as for an
           unexpected exception.

           If called with the callable and arguments omitted, will return a
           context object used like this::

                with self.assertRaises(SomeException):
                    do_something()

           An optional keyword argument 'msg' can be provided when assertRaises
           is used as a context object.

           The context manager keeps a reference to the exception as
           the 'exception' attribute. This allows you to inspect the
           exception after the assertion::

               with self.assertRaises(SomeException) as cm:
                   do_something()
               the_exception = cm.exception
               self.assertEqual(the_exception.error_code, 3)
        '''
    ...
    def assertRaisesRegex (self, expected_exception, expected_regex, *args, **kwargs):
      '''Asserts that the message in a raised exception matches a regex.

        Args:
            expected_exception: Exception class expected to be raised.
            expected_regex: Regex (re.Pattern object or string) expected
                    to be found in error message.
            args: Function to be called and extra positional args.
            kwargs: Extra kwargs.
            msg: Optional message used in case of failure. Can only be used
                    when assertRaisesRegex is used as a context manager.
        '''
    ...
    def assertRaisesRegexp (*args, **kwargs):
      '''None'''
    ...
    def assertRegex (self, text, expected_regex, msg=None):
      '''Fail the test unless the text matches the regular expression.'''
    ...
    def assertRegexpMatches (*args, **kwargs):
      '''None'''
    ...
    def assertSequenceEqual (self, seq1, seq2, msg=None, seq_type=None):
      '''An equality assertion for ordered sequences (like lists and tuples).

        For the purposes of this function, a valid ordered sequence type is one
        which can be indexed, has a length, and has an equality operator.

        Args:
            seq1: The first sequence to compare.
            seq2: The second sequence to compare.
            seq_type: The expected datatype of the sequences, or None if no
                    datatype should be enforced.
            msg: Optional message to use on failure instead of a list of
                    differences.
        '''
    ...
    def assertSetEqual (self, set1, set2, msg=None):
      '''A set-specific equality assertion.

        Args:
            set1: The first set to compare.
            set2: The second set to compare.
            msg: Optional message to use on failure instead of a list of
                    differences.

        assertSetEqual uses ducktyping to support different types of sets, and
        is optimized for sets specifically (parameters must support a
        difference method).
        '''
    ...
    def assertTrue (self, expr, msg=None):
      '''Check that the expression is true.'''
    ...
    def assertTupleEqual (self, tuple1, tuple2, msg=None):
      '''A tuple-specific equality assertion.

        Args:
            tuple1: The first tuple to compare.
            tuple2: The second tuple to compare.
            msg: Optional message to use on failure instead of a list of
                    differences.
        '''
    ...
    def assertTypeNamesArePrefixed (self, module, namesToIgnore=()):
      '''None'''
    ...
    def assertWarns (self, expected_warning, *args, **kwargs):
      '''Fail unless a warning of class warnClass is triggered
           by the callable when invoked with specified positional and
           keyword arguments.  If a different type of warning is
           triggered, it will not be handled: depending on the other
           warning filtering rules in effect, it might be silenced, printed
           out, or raised as an exception.

           If called with the callable and arguments omitted, will return a
           context object used like this::

                with self.assertWarns(SomeWarning):
                    do_something()

           An optional keyword argument 'msg' can be provided when assertWarns
           is used as a context object.

           The context manager keeps a reference to the first matching
           warning as the 'warning' attribute; similarly, the 'filename'
           and 'lineno' attributes give you information about the line
           of Python code from which the warning was triggered.
           This allows you to inspect the warning after the assertion::

               with self.assertWarns(SomeWarning) as cm:
                   do_something()
               the_warning = cm.warning
               self.assertEqual(the_warning.some_attribute, 147)
        '''
    ...
    def assertWarnsRegex (self, expected_warning, expected_regex, *args, **kwargs):
      '''Asserts that the message in a triggered warning matches a regexp.
        Basic functioning is similar to assertWarns() with the addition
        that only warnings whose messages also match the regular expression
        are considered successful matches.

        Args:
            expected_warning: Warning class expected to be triggered.
            expected_regex: Regex (re.Pattern object or string) expected
                    to be found in error message.
            args: Function to be called and extra positional args.
            kwargs: Extra kwargs.
            msg: Optional message used in case of failure. Can only be used
                    when assertWarnsRegex is used as a context manager.
        '''
    ...
    def assert_ (*args, **kwargs):
      '''None'''
    ...
    def countTestCases (self):
      '''None'''
    ...
    def debug (self):
      '''Run the test without collecting errors in a TestResult'''
    ...
    def defaultTestResult (self):
      '''None'''
    ...
    def doClassCleanups ():
      '''Execute all class cleanup functions. Normally called for you after
        tearDownClass.'''
    ...
    def doCleanups (self):
      '''Execute all cleanup functions. Normally called for you after
        tearDown.'''
    ...
    def fail (self, msg=None):
      '''Fail immediately, with the given message.'''
    ...
    def failIf (*args, **kwargs):
      '''None'''
    ...
    def failIfAlmostEqual (*args, **kwargs):
      '''None'''
    ...
    def failIfEqual (*args, **kwargs):
      '''None'''
    ...
    def failUnless (*args, **kwargs):
      '''None'''
    ...
    def failUnlessAlmostEqual (*args, **kwargs):
      '''None'''
    ...
    def failUnlessEqual (*args, **kwargs):
      '''None'''
    ...
    def failUnlessRaises (*args, **kwargs):
      '''None'''
    ...
    def failureException (self, *args, **kwargs):
      '''Assertion failed.'''
    ...
    def failureMessageLevel (self, *args, **kwargs):
      '''None'''
    ...
    def id (self):
      '''None'''
    ...
    def ignoreMessage (self, level, context, message):
      '''None'''
    ...
    def longMessage (self, *args, **kwargs):
      '''bool(x) -> bool

Returns True when the argument x is true, False otherwise.
The builtins True and False are the only two instances of the class bool.
The class bool is a subclass of the class int, and cannot be subclassed.'''
    ...
    def maxDiff (self, *args, **kwargs):
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
    def run (self, result=None):
      '''None'''
    ...
    def scopedLocale (l, category=0):
      '''None'''
    ...
    def setUp (self):
      '''None'''
    ...
    def setUpClass ():
      '''Hook method for setting up class fixture before running tests in the class.'''
    ...
    def shortDescription (self):
      '''Returns a one-line description of the test, or None if no
        description has been provided.

        The default implementation of this method returns the first line of
        the specified test method's docstring.
        '''
    ...
    def skipTest (self, reason):
      '''Skip this test.'''
    ...
    def subTest (self, msg=<object object at 0x7fb108120c10>, **params):
      '''Return a context manager that will return the enclosed block
        of code in a subtest identified by the optional message and
        keyword parameters.  A failure in the subtest marks the test
        case as failed but resumes execution at the end of the enclosed
        block, allowing further test code to be executed.
        '''
    ...
    def tearDown (self):
      '''None'''
    ...
    def tearDownClass ():
      '''Hook method for deconstructing the class fixture after running all tests in the class.'''
    ...
    def temporaryDirectory (self):
      '''None'''
    ...
    def testBadJobDirectory (self):
      '''None'''
    ...
    def testBasicBatcherPerformance (self):
      '''None'''
    ...
    def testBatchContextsAreIdentical (self):
      '''None'''
    ...
    def testBatchSize (self):
      '''None'''
    ...
    def testBatchesCanAccessJobDirectory (self):
      '''None'''
    ...
    def testCancelDispatch (self):
      '''None'''
    ...
    def testCatchThrowingSlots (self):
      '''None'''
    ...
    def testContextChange (self):
      '''None'''
    ...
    def testContextDrivingDispatcherPlugs (self):
      '''None'''
    ...
    def testContextProcessor (self):
      '''None'''
    ...
    def testCyclesThrow (self):
      '''None'''
    ...
    def testDefaultDispatcher (self):
      '''None'''
    ...
    def testDerivedClass (self):
      '''None'''
    ...
    def testDifferentScripts (self):
      '''None'''
    ...
    def testDirectCyles (self):
      '''None'''
    ...
    def testDispatch (self):
      '''None'''
    ...
    def testDispatchBadCustomRange (self):
      '''None'''
    ...
    def testDispatchCustomRange (self):
      '''None'''
    ...
    def testDispatchDifferentFrame (self):
      '''None'''
    ...
    def testDispatchFullRange (self):
      '''None'''
    ...
    def testDispatchIdenticalTasks (self):
      '''None'''
    ...
    def testDispatchIterable (self):
      '''None'''
    ...
    def testDispatchThroughSubgraphs (self):
      '''None'''
    ...
    def testDispatcherRegistration (self):
      '''None'''
    ...
    def testDispatcherSignals (self):
      '''None'''
    ...
    def testDoesNotRequireSequenceExecution (self):
      '''None'''
    ...
    def testFrameOrderWithPostTask (self):
      '''None'''
    ...
    def testFrameOrderWithSequencePostTask (self):
      '''None'''
    ...
    def testFrameOrderWithStaticPostTask (self):
      '''None'''
    ...
    def testFrameRangeOverride (self):
      '''None'''
    ...
    def testImmediateDispatch (self):
      '''None'''
    ...
    def testImmediateDispatchWithSharedBatches (self):
      '''None'''
    ...
    def testImmediateDispatchWithSplitSharedBatches (self):
      '''None'''
    ...
    def testJobDirectoryNotCreatedForCancelledDispatch (self):
      '''None'''
    ...
    def testLegacyDispatcherSignals (self):
      '''None'''
    ...
    def testLegacyFrameRange (self):
      '''None'''
    ...
    def testManyFrames (self):
      '''None'''
    ...
    def testNameSwitch (self):
      '''None'''
    ...
    def testNestedDispatch (self):
      '''None'''
    ...
    def testNoOpDoesntBreakFrameParallelism (self):
      '''None'''
    ...
    def testNoScript (self):
      '''None'''
    ...
    def testNoSignalsForNestedDispatch (self):
      '''None'''
    ...
    def testNoTask (self):
      '''None'''
    ...
    def testNonTaskNodes (self):
      '''None'''
    ...
    def testNotACycle (self):
      '''None'''
    ...
    def testPlugs (self):
      '''None'''
    ...
    def testPostDispatchSignalSuccess (self):
      '''None'''
    ...
    def testPostTaskCycles (self):
      '''None'''
    ...
    def testPostTaskWithDownstreamTasks (self):
      '''None'''
    ...
    def testPostTaskWithPreTasks (self):
      '''None'''
    ...
    def testPostTasks (self):
      '''None'''
    ...
    def testPreAndPostTasks (self):
      '''None'''
    ...
    def testPreTasksOverride (self):
      '''None'''
    ...
    def testRequiresSequenceExecution (self):
      '''None'''
    ...
    def testScaling (self):
      '''None'''
    ...
    def testSerialPostTasks (self):
      '''None'''
    ...
    def testStaticPostTask (self):
      '''None'''
    ...
    def testSwitch (self):
      '''None'''
    ...
    def testTaskListBatchSize (self):
      '''None'''
    ...
    def testTaskListWaitForSequence (self):
      '''None'''
    ...
    def testTaskListWedging (self):
      '''None'''
    ...
    def testTaskPlugsWithoutTaskNodes (self):
      '''None'''
    ...
    def testTwoContextProcessors (self):
      '''None'''
    ...
    def testTwoNameSwitches (self):
      '''None'''
    ...
    def testWedgedDispatchWithVaryingFrameRange (self):
      '''None'''
    ...

def ErroringTaskNode (*args):
      '''

'''      
    ...

class ErroringTaskNode:
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
acceptsChild( (TaskNode)arg1, (GraphComponent)arg2) -> bool :

    C++ signature :
        bool acceptsChild(GafferDispatch::TaskNode,Gaffer::GraphComponent const*)'''
    ...
    def acceptsParent (self, *args, **kwargs):
      '''
acceptsParent( (TaskNode)arg1, (GraphComponent)arg2) -> bool :

    C++ signature :
        bool acceptsParent(GafferDispatch::TaskNode,Gaffer::GraphComponent const*)'''
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
    def execute (self):
      '''None'''
    ...
    def executeSequence (self, frames):
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
    def getName (self, *args, **kwargs):
      '''
getName( (GraphComponent)arg1) -> str :

    C++ signature :
        char const* getName(Gaffer::GraphComponent {lvalue})'''
    ...
    def hash (self, context):
      '''None'''
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
    def postTasks (self, context):
      '''None'''
    ...
    def preTasks (self, context):
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
    def requiresSequenceExecution (self):
      '''None'''
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

def ExecuteApplicationTest (*args):
      '''

'''      
    ...

class ExecuteApplicationTest:
    def _TestCase__nodeHasDescription (self, node):
      '''None'''
    ...
    def _TestCase__undocumentedPlugs (self, node, additionalTerminalPlugTypes=()):
      '''None'''
    ...
    def _addExpectedFailure (self, result, exc_info):
      '''None'''
    ...
    def _addSkip (self, result, test_case, reason):
      '''None'''
    ...
    def _addUnexpectedSuccess (self, result):
      '''None'''
    ...
    def _baseAssertEqual (self, first, second, msg=None):
      '''The default assertEqual implementation, not type specific.'''
    ...
    def _callCleanup (self, function, /, *args, **kwargs):
      '''None'''
    ...
    def _callSetUp (self):
      '''None'''
    ...
    def _callTearDown (self):
      '''None'''
    ...
    def _callTestMethod (self, method):
      '''None'''
    ...
    def _classSetupFailed (self, *args, **kwargs):
      '''bool(x) -> bool

Returns True when the argument x is true, False otherwise.
The builtins True and False are the only two instances of the class bool.
The class bool is a subclass of the class int, and cannot be subclassed.'''
    ...
    def _class_cleanups (self, *args, **kwargs):
      '''Built-in mutable sequence.

If no argument is given, the constructor creates a new empty list.
The argument must be an iterable if specified.'''
    ...
    def _deprecate (original_func):
      '''None'''
    ...
    def _diffThreshold (self, *args, **kwargs):
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
    def _feedErrorsToResult (self, result, errors):
      '''None'''
    ...
    def _formatMessage (self, msg, standardMsg):
      '''Honour the longMessage attribute when generating failure messages.
        If longMessage is False this means:
        * Use only an explicit message if it is provided
        * Otherwise use the standard message for the assert

        If longMessage is True:
        * Use the standard message
        * If an explicit message is provided, plus ' : ' and the explicit message
        '''
    ...
    def _getAssertEqualityFunc (self, first, second):
      '''Get a detailed comparison function for the types of the two args.

        Returns: A callable accepting (first, second, msg=None) that will
        raise a failure exception if first != second with a useful human
        readable error message for those types.
        '''
    ...
    def _truncateMessage (self, message, diff):
      '''None'''
    ...
    def addClassCleanup (function, /, *args, **kwargs):
      '''Same as addCleanup, except the cleanup items are called even if
        setUpClass fails (unlike tearDownClass).'''
    ...
    def addCleanup (self, function, /, *args, **kwargs):
      '''Add a function, with arguments, to be called when the test is
        completed. Functions added are called on a LIFO basis and are
        called after tearDown on test failure or success.

        Cleanup items are called even if setUp fails (unlike tearDown).'''
    ...
    def addTypeEqualityFunc (self, typeobj, function):
      '''Add a type specific assertEqual style function to compare a type.

        This method is for use by TestCase subclasses that need to register
        their own type equality functions to provide nicer error messages.

        Args:
            typeobj: The data type to call this function on when both values
                    are of the same type in assertEqual().
            function: The callable taking two arguments and an optional
                    msg= argument that raises self.failureException with a
                    useful error message when the two arguments are not equal.
        '''
    ...
    def assertAlmostEqual (self, first, second, places=None, msg=None, delta=None):
      '''Fail if the two objects are unequal as determined by their
           difference rounded to the given number of decimal places
           (default 7) and comparing to zero, or by comparing that the
           difference between the two objects is more than the given
           delta.

           Note that decimal places (from zero) are usually not the same
           as significant digits (measured from the most significant digit).

           If the two objects compare equal then they will automatically
           compare almost equal.
        '''
    ...
    def assertAlmostEquals (*args, **kwargs):
      '''None'''
    ...
    def assertCountEqual (self, first, second, msg=None):
      '''Asserts that two iterables have the same elements, the same number of
        times, without regard to order.

            self.assertEqual(Counter(list(first)),
                             Counter(list(second)))

         Example:
            - [0, 1, 1] and [1, 0, 1] compare equal.
            - [0, 0, 1] and [0, 1] compare unequal.

        '''
    ...
    def assertDefaultNamesAreCorrect (self, module, namesToIgnore=()):
      '''None'''
    ...
    def assertDictContainsSubset (self, subset, dictionary, msg=None):
      '''Checks whether dictionary is a superset of subset.'''
    ...
    def assertDictEqual (self, d1, d2, msg=None):
      '''None'''
    ...
    def assertEqual (self, first, second, msg=None):
      '''Fail if the two objects are unequal as determined by the '=='
           operator.
        '''
    ...
    def assertEquals (*args, **kwargs):
      '''None'''
    ...
    def assertFalse (self, expr, msg=None):
      '''Check that the expression is false.'''
    ...
    def assertFloat32Equal (self, value0, value1):
      '''None'''
    ...
    def assertGreater (self, a, b, msg=None):
      '''Just like self.assertTrue(a > b), but with a nicer default message.'''
    ...
    def assertGreaterEqual (self, a, b, msg=None):
      '''Just like self.assertTrue(a >= b), but with a nicer default message.'''
    ...
    def assertHashesValid (self, node, inputsToIgnore=[], outputsToIgnore=[]):
      '''None'''
    ...
    def assertIn (self, member, container, msg=None):
      '''Just like self.assertTrue(a in b), but with a nicer default message.'''
    ...
    def assertIs (self, expr1, expr2, msg=None):
      '''Just like self.assertTrue(a is b), but with a nicer default message.'''
    ...
    def assertIsInstance (self, obj, cls, msg=None):
      '''Same as self.assertTrue(isinstance(obj, cls)), with a nicer
        default message.'''
    ...
    def assertIsNone (self, obj, msg=None):
      '''Same as self.assertTrue(obj is None), with a nicer default message.'''
    ...
    def assertIsNot (self, expr1, expr2, msg=None):
      '''Just like self.assertTrue(a is not b), but with a nicer default message.'''
    ...
    def assertIsNotNone (self, obj, msg=None):
      '''Included for symmetry with assertIsNone.'''
    ...
    def assertLess (self, a, b, msg=None):
      '''Just like self.assertTrue(a < b), but with a nicer default message.'''
    ...
    def assertLessEqual (self, a, b, msg=None):
      '''Just like self.assertTrue(a <= b), but with a nicer default message.'''
    ...
    def assertListEqual (self, list1, list2, msg=None):
      '''A list-specific equality assertion.

        Args:
            list1: The first list to compare.
            list2: The second list to compare.
            msg: Optional message to use on failure instead of a list of
                    differences.

        '''
    ...
    def assertLogs (self, logger=None, level=None):
      '''Fail unless a log message of level *level* or higher is emitted
        on *logger_name* or its children.  If omitted, *level* defaults to
        INFO and *logger* defaults to the root logger.

        This method must be used as a context manager, and will yield
        a recording object with two attributes: `output` and `records`.
        At the end of the context manager, the `output` attribute will
        be a list of the matching formatted log messages and the
        `records` attribute will be a list of the corresponding LogRecord
        objects.

        Example::

            with self.assertLogs('foo', level='INFO') as cm:
                logging.getLogger('foo').info('first message')
                logging.getLogger('foo.bar').error('second message')
            self.assertEqual(cm.output, ['INFO:foo:first message',
                                         'ERROR:foo.bar:second message'])
        '''
    ...
    def assertModuleDoesNotImportUI (self, moduleName):
      '''None'''
    ...
    def assertMultiLineEqual (self, first, second, msg=None):
      '''Assert that two multi-line strings are equal.'''
    ...
    def assertNoLogs (self, logger=None, level=None):
      ''' Fail unless no log messages of level *level* or higher are emitted
        on *logger_name* or its children.

        This method must be used as a context manager.
        '''
    ...
    def assertNodeIsDocumented (self, node, additionalTerminalPlugTypes=()):
      '''None'''
    ...
    def assertNodesAreDocumented (self, module, additionalTerminalPlugTypes=(), nodesToIgnore=None):
      '''None'''
    ...
    def assertNodesConstructWithDefaultValues (self, module, nodesToIgnore=None, plugsToIgnore=None):
      '''None'''
    ...
    def assertNotAlmostEqual (self, first, second, places=None, msg=None, delta=None):
      '''Fail if the two objects are equal as determined by their
           difference rounded to the given number of decimal places
           (default 7) and comparing to zero, or by comparing that the
           difference between the two objects is less than the given delta.

           Note that decimal places (from zero) are usually not the same
           as significant digits (measured from the most significant digit).

           Objects that are equal automatically fail.
        '''
    ...
    def assertNotAlmostEquals (*args, **kwargs):
      '''None'''
    ...
    def assertNotEqual (self, first, second, msg=None):
      '''Fail if the two objects are equal as determined by the '!='
           operator.
        '''
    ...
    def assertNotEquals (*args, **kwargs):
      '''None'''
    ...
    def assertNotIn (self, member, container, msg=None):
      '''Just like self.assertTrue(a not in b), but with a nicer default message.'''
    ...
    def assertNotIsInstance (self, obj, cls, msg=None):
      '''Included for symmetry with assertIsInstance.'''
    ...
    def assertNotRegex (self, text, unexpected_regex, msg=None):
      '''Fail the test if the text matches the regular expression.'''
    ...
    def assertNotRegexpMatches (*args, **kwargs):
      '''None'''
    ...
    def assertRaises (self, expected_exception, *args, **kwargs):
      '''Fail unless an exception of class expected_exception is raised
           by the callable when invoked with specified positional and
           keyword arguments. If a different type of exception is
           raised, it will not be caught, and the test case will be
           deemed to have suffered an error, exactly as for an
           unexpected exception.

           If called with the callable and arguments omitted, will return a
           context object used like this::

                with self.assertRaises(SomeException):
                    do_something()

           An optional keyword argument 'msg' can be provided when assertRaises
           is used as a context object.

           The context manager keeps a reference to the exception as
           the 'exception' attribute. This allows you to inspect the
           exception after the assertion::

               with self.assertRaises(SomeException) as cm:
                   do_something()
               the_exception = cm.exception
               self.assertEqual(the_exception.error_code, 3)
        '''
    ...
    def assertRaisesRegex (self, expected_exception, expected_regex, *args, **kwargs):
      '''Asserts that the message in a raised exception matches a regex.

        Args:
            expected_exception: Exception class expected to be raised.
            expected_regex: Regex (re.Pattern object or string) expected
                    to be found in error message.
            args: Function to be called and extra positional args.
            kwargs: Extra kwargs.
            msg: Optional message used in case of failure. Can only be used
                    when assertRaisesRegex is used as a context manager.
        '''
    ...
    def assertRaisesRegexp (*args, **kwargs):
      '''None'''
    ...
    def assertRegex (self, text, expected_regex, msg=None):
      '''Fail the test unless the text matches the regular expression.'''
    ...
    def assertRegexpMatches (*args, **kwargs):
      '''None'''
    ...
    def assertSequenceEqual (self, seq1, seq2, msg=None, seq_type=None):
      '''An equality assertion for ordered sequences (like lists and tuples).

        For the purposes of this function, a valid ordered sequence type is one
        which can be indexed, has a length, and has an equality operator.

        Args:
            seq1: The first sequence to compare.
            seq2: The second sequence to compare.
            seq_type: The expected datatype of the sequences, or None if no
                    datatype should be enforced.
            msg: Optional message to use on failure instead of a list of
                    differences.
        '''
    ...
    def assertSetEqual (self, set1, set2, msg=None):
      '''A set-specific equality assertion.

        Args:
            set1: The first set to compare.
            set2: The second set to compare.
            msg: Optional message to use on failure instead of a list of
                    differences.

        assertSetEqual uses ducktyping to support different types of sets, and
        is optimized for sets specifically (parameters must support a
        difference method).
        '''
    ...
    def assertTrue (self, expr, msg=None):
      '''Check that the expression is true.'''
    ...
    def assertTupleEqual (self, tuple1, tuple2, msg=None):
      '''A tuple-specific equality assertion.

        Args:
            tuple1: The first tuple to compare.
            tuple2: The second tuple to compare.
            msg: Optional message to use on failure instead of a list of
                    differences.
        '''
    ...
    def assertTypeNamesArePrefixed (self, module, namesToIgnore=()):
      '''None'''
    ...
    def assertWarns (self, expected_warning, *args, **kwargs):
      '''Fail unless a warning of class warnClass is triggered
           by the callable when invoked with specified positional and
           keyword arguments.  If a different type of warning is
           triggered, it will not be handled: depending on the other
           warning filtering rules in effect, it might be silenced, printed
           out, or raised as an exception.

           If called with the callable and arguments omitted, will return a
           context object used like this::

                with self.assertWarns(SomeWarning):
                    do_something()

           An optional keyword argument 'msg' can be provided when assertWarns
           is used as a context object.

           The context manager keeps a reference to the first matching
           warning as the 'warning' attribute; similarly, the 'filename'
           and 'lineno' attributes give you information about the line
           of Python code from which the warning was triggered.
           This allows you to inspect the warning after the assertion::

               with self.assertWarns(SomeWarning) as cm:
                   do_something()
               the_warning = cm.warning
               self.assertEqual(the_warning.some_attribute, 147)
        '''
    ...
    def assertWarnsRegex (self, expected_warning, expected_regex, *args, **kwargs):
      '''Asserts that the message in a triggered warning matches a regexp.
        Basic functioning is similar to assertWarns() with the addition
        that only warnings whose messages also match the regular expression
        are considered successful matches.

        Args:
            expected_warning: Warning class expected to be triggered.
            expected_regex: Regex (re.Pattern object or string) expected
                    to be found in error message.
            args: Function to be called and extra positional args.
            kwargs: Extra kwargs.
            msg: Optional message used in case of failure. Can only be used
                    when assertWarnsRegex is used as a context manager.
        '''
    ...
    def assert_ (*args, **kwargs):
      '''None'''
    ...
    def countTestCases (self):
      '''None'''
    ...
    def debug (self):
      '''Run the test without collecting errors in a TestResult'''
    ...
    def defaultTestResult (self):
      '''None'''
    ...
    def doClassCleanups ():
      '''Execute all class cleanup functions. Normally called for you after
        tearDownClass.'''
    ...
    def doCleanups (self):
      '''Execute all cleanup functions. Normally called for you after
        tearDown.'''
    ...
    def fail (self, msg=None):
      '''Fail immediately, with the given message.'''
    ...
    def failIf (*args, **kwargs):
      '''None'''
    ...
    def failIfAlmostEqual (*args, **kwargs):
      '''None'''
    ...
    def failIfEqual (*args, **kwargs):
      '''None'''
    ...
    def failUnless (*args, **kwargs):
      '''None'''
    ...
    def failUnlessAlmostEqual (*args, **kwargs):
      '''None'''
    ...
    def failUnlessEqual (*args, **kwargs):
      '''None'''
    ...
    def failUnlessRaises (*args, **kwargs):
      '''None'''
    ...
    def failureException (self, *args, **kwargs):
      '''Assertion failed.'''
    ...
    def failureMessageLevel (self, *args, **kwargs):
      '''None'''
    ...
    def id (self):
      '''None'''
    ...
    def ignoreMessage (self, level, context, message):
      '''None'''
    ...
    def longMessage (self, *args, **kwargs):
      '''bool(x) -> bool

Returns True when the argument x is true, False otherwise.
The builtins True and False are the only two instances of the class bool.
The class bool is a subclass of the class int, and cannot be subclassed.'''
    ...
    def maxDiff (self, *args, **kwargs):
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
    def run (self, result=None):
      '''None'''
    ...
    def scopedLocale (l, category=0):
      '''None'''
    ...
    def setUp (self):
      '''None'''
    ...
    def setUpClass ():
      '''Hook method for setting up class fixture before running tests in the class.'''
    ...
    def shortDescription (self):
      '''Returns a one-line description of the test, or None if no
        description has been provided.

        The default implementation of this method returns the first line of
        the specified test method's docstring.
        '''
    ...
    def skipTest (self, reason):
      '''Skip this test.'''
    ...
    def subTest (self, msg=<object object at 0x7fb108120c10>, **params):
      '''Return a context manager that will return the enclosed block
        of code in a subtest identified by the optional message and
        keyword parameters.  A failure in the subtest marks the test
        case as failed but resumes execution at the end of the enclosed
        block, allowing further test code to be executed.
        '''
    ...
    def tearDown (self):
      '''None'''
    ...
    def tearDownClass ():
      '''Hook method for deconstructing the class fixture after running all tests in the class.'''
    ...
    def temporaryDirectory (self):
      '''None'''
    ...
    def testCanSerialiseFrameDependentPlugs (self):
      '''None'''
    ...
    def testContextParameter (self):
      '''None'''
    ...
    def testDefaultFrame (self):
      '''None'''
    ...
    def testErrorMessagesIncludeNodeName (self):
      '''None'''
    ...
    def testErrorReturnStatusForBadContext (self):
      '''None'''
    ...
    def testErrorReturnStatusForExceptionDuringExecution (self):
      '''None'''
    ...
    def testErrorReturnStatusForMissingScript (self):
      '''None'''
    ...
    def testExecuteTextWriter (self):
      '''None'''
    ...
    def testFramesParameter (self):
      '''None'''
    ...
    def testIgnoreScriptLoadErrors (self):
      '''None'''
    ...
    def testImathContextVariable (self):
      '''None'''
    ...
    def testSpecialCharactersInScriptFileName (self):
      '''None'''
    ...

def FrameMaskTest (*args):
      '''

'''      
    ...

class FrameMaskTest:
    def _TestCase__nodeHasDescription (self, node):
      '''None'''
    ...
    def _TestCase__undocumentedPlugs (self, node, additionalTerminalPlugTypes=()):
      '''None'''
    ...
    def _addExpectedFailure (self, result, exc_info):
      '''None'''
    ...
    def _addSkip (self, result, test_case, reason):
      '''None'''
    ...
    def _addUnexpectedSuccess (self, result):
      '''None'''
    ...
    def _baseAssertEqual (self, first, second, msg=None):
      '''The default assertEqual implementation, not type specific.'''
    ...
    def _callCleanup (self, function, /, *args, **kwargs):
      '''None'''
    ...
    def _callSetUp (self):
      '''None'''
    ...
    def _callTearDown (self):
      '''None'''
    ...
    def _callTestMethod (self, method):
      '''None'''
    ...
    def _classSetupFailed (self, *args, **kwargs):
      '''bool(x) -> bool

Returns True when the argument x is true, False otherwise.
The builtins True and False are the only two instances of the class bool.
The class bool is a subclass of the class int, and cannot be subclassed.'''
    ...
    def _class_cleanups (self, *args, **kwargs):
      '''Built-in mutable sequence.

If no argument is given, the constructor creates a new empty list.
The argument must be an iterable if specified.'''
    ...
    def _deprecate (original_func):
      '''None'''
    ...
    def _diffThreshold (self, *args, **kwargs):
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
    def _feedErrorsToResult (self, result, errors):
      '''None'''
    ...
    def _formatMessage (self, msg, standardMsg):
      '''Honour the longMessage attribute when generating failure messages.
        If longMessage is False this means:
        * Use only an explicit message if it is provided
        * Otherwise use the standard message for the assert

        If longMessage is True:
        * Use the standard message
        * If an explicit message is provided, plus ' : ' and the explicit message
        '''
    ...
    def _getAssertEqualityFunc (self, first, second):
      '''Get a detailed comparison function for the types of the two args.

        Returns: A callable accepting (first, second, msg=None) that will
        raise a failure exception if first != second with a useful human
        readable error message for those types.
        '''
    ...
    def _truncateMessage (self, message, diff):
      '''None'''
    ...
    def addClassCleanup (function, /, *args, **kwargs):
      '''Same as addCleanup, except the cleanup items are called even if
        setUpClass fails (unlike tearDownClass).'''
    ...
    def addCleanup (self, function, /, *args, **kwargs):
      '''Add a function, with arguments, to be called when the test is
        completed. Functions added are called on a LIFO basis and are
        called after tearDown on test failure or success.

        Cleanup items are called even if setUp fails (unlike tearDown).'''
    ...
    def addTypeEqualityFunc (self, typeobj, function):
      '''Add a type specific assertEqual style function to compare a type.

        This method is for use by TestCase subclasses that need to register
        their own type equality functions to provide nicer error messages.

        Args:
            typeobj: The data type to call this function on when both values
                    are of the same type in assertEqual().
            function: The callable taking two arguments and an optional
                    msg= argument that raises self.failureException with a
                    useful error message when the two arguments are not equal.
        '''
    ...
    def assertAlmostEqual (self, first, second, places=None, msg=None, delta=None):
      '''Fail if the two objects are unequal as determined by their
           difference rounded to the given number of decimal places
           (default 7) and comparing to zero, or by comparing that the
           difference between the two objects is more than the given
           delta.

           Note that decimal places (from zero) are usually not the same
           as significant digits (measured from the most significant digit).

           If the two objects compare equal then they will automatically
           compare almost equal.
        '''
    ...
    def assertAlmostEquals (*args, **kwargs):
      '''None'''
    ...
    def assertCountEqual (self, first, second, msg=None):
      '''Asserts that two iterables have the same elements, the same number of
        times, without regard to order.

            self.assertEqual(Counter(list(first)),
                             Counter(list(second)))

         Example:
            - [0, 1, 1] and [1, 0, 1] compare equal.
            - [0, 0, 1] and [0, 1] compare unequal.

        '''
    ...
    def assertDefaultNamesAreCorrect (self, module, namesToIgnore=()):
      '''None'''
    ...
    def assertDictContainsSubset (self, subset, dictionary, msg=None):
      '''Checks whether dictionary is a superset of subset.'''
    ...
    def assertDictEqual (self, d1, d2, msg=None):
      '''None'''
    ...
    def assertEqual (self, first, second, msg=None):
      '''Fail if the two objects are unequal as determined by the '=='
           operator.
        '''
    ...
    def assertEquals (*args, **kwargs):
      '''None'''
    ...
    def assertFalse (self, expr, msg=None):
      '''Check that the expression is false.'''
    ...
    def assertFloat32Equal (self, value0, value1):
      '''None'''
    ...
    def assertGreater (self, a, b, msg=None):
      '''Just like self.assertTrue(a > b), but with a nicer default message.'''
    ...
    def assertGreaterEqual (self, a, b, msg=None):
      '''Just like self.assertTrue(a >= b), but with a nicer default message.'''
    ...
    def assertHashesValid (self, node, inputsToIgnore=[], outputsToIgnore=[]):
      '''None'''
    ...
    def assertIn (self, member, container, msg=None):
      '''Just like self.assertTrue(a in b), but with a nicer default message.'''
    ...
    def assertIs (self, expr1, expr2, msg=None):
      '''Just like self.assertTrue(a is b), but with a nicer default message.'''
    ...
    def assertIsInstance (self, obj, cls, msg=None):
      '''Same as self.assertTrue(isinstance(obj, cls)), with a nicer
        default message.'''
    ...
    def assertIsNone (self, obj, msg=None):
      '''Same as self.assertTrue(obj is None), with a nicer default message.'''
    ...
    def assertIsNot (self, expr1, expr2, msg=None):
      '''Just like self.assertTrue(a is not b), but with a nicer default message.'''
    ...
    def assertIsNotNone (self, obj, msg=None):
      '''Included for symmetry with assertIsNone.'''
    ...
    def assertLess (self, a, b, msg=None):
      '''Just like self.assertTrue(a < b), but with a nicer default message.'''
    ...
    def assertLessEqual (self, a, b, msg=None):
      '''Just like self.assertTrue(a <= b), but with a nicer default message.'''
    ...
    def assertListEqual (self, list1, list2, msg=None):
      '''A list-specific equality assertion.

        Args:
            list1: The first list to compare.
            list2: The second list to compare.
            msg: Optional message to use on failure instead of a list of
                    differences.

        '''
    ...
    def assertLogs (self, logger=None, level=None):
      '''Fail unless a log message of level *level* or higher is emitted
        on *logger_name* or its children.  If omitted, *level* defaults to
        INFO and *logger* defaults to the root logger.

        This method must be used as a context manager, and will yield
        a recording object with two attributes: `output` and `records`.
        At the end of the context manager, the `output` attribute will
        be a list of the matching formatted log messages and the
        `records` attribute will be a list of the corresponding LogRecord
        objects.

        Example::

            with self.assertLogs('foo', level='INFO') as cm:
                logging.getLogger('foo').info('first message')
                logging.getLogger('foo.bar').error('second message')
            self.assertEqual(cm.output, ['INFO:foo:first message',
                                         'ERROR:foo.bar:second message'])
        '''
    ...
    def assertModuleDoesNotImportUI (self, moduleName):
      '''None'''
    ...
    def assertMultiLineEqual (self, first, second, msg=None):
      '''Assert that two multi-line strings are equal.'''
    ...
    def assertNoLogs (self, logger=None, level=None):
      ''' Fail unless no log messages of level *level* or higher are emitted
        on *logger_name* or its children.

        This method must be used as a context manager.
        '''
    ...
    def assertNodeIsDocumented (self, node, additionalTerminalPlugTypes=()):
      '''None'''
    ...
    def assertNodesAreDocumented (self, module, additionalTerminalPlugTypes=(), nodesToIgnore=None):
      '''None'''
    ...
    def assertNodesConstructWithDefaultValues (self, module, nodesToIgnore=None, plugsToIgnore=None):
      '''None'''
    ...
    def assertNotAlmostEqual (self, first, second, places=None, msg=None, delta=None):
      '''Fail if the two objects are equal as determined by their
           difference rounded to the given number of decimal places
           (default 7) and comparing to zero, or by comparing that the
           difference between the two objects is less than the given delta.

           Note that decimal places (from zero) are usually not the same
           as significant digits (measured from the most significant digit).

           Objects that are equal automatically fail.
        '''
    ...
    def assertNotAlmostEquals (*args, **kwargs):
      '''None'''
    ...
    def assertNotEqual (self, first, second, msg=None):
      '''Fail if the two objects are equal as determined by the '!='
           operator.
        '''
    ...
    def assertNotEquals (*args, **kwargs):
      '''None'''
    ...
    def assertNotIn (self, member, container, msg=None):
      '''Just like self.assertTrue(a not in b), but with a nicer default message.'''
    ...
    def assertNotIsInstance (self, obj, cls, msg=None):
      '''Included for symmetry with assertIsInstance.'''
    ...
    def assertNotRegex (self, text, unexpected_regex, msg=None):
      '''Fail the test if the text matches the regular expression.'''
    ...
    def assertNotRegexpMatches (*args, **kwargs):
      '''None'''
    ...
    def assertRaises (self, expected_exception, *args, **kwargs):
      '''Fail unless an exception of class expected_exception is raised
           by the callable when invoked with specified positional and
           keyword arguments. If a different type of exception is
           raised, it will not be caught, and the test case will be
           deemed to have suffered an error, exactly as for an
           unexpected exception.

           If called with the callable and arguments omitted, will return a
           context object used like this::

                with self.assertRaises(SomeException):
                    do_something()

           An optional keyword argument 'msg' can be provided when assertRaises
           is used as a context object.

           The context manager keeps a reference to the exception as
           the 'exception' attribute. This allows you to inspect the
           exception after the assertion::

               with self.assertRaises(SomeException) as cm:
                   do_something()
               the_exception = cm.exception
               self.assertEqual(the_exception.error_code, 3)
        '''
    ...
    def assertRaisesRegex (self, expected_exception, expected_regex, *args, **kwargs):
      '''Asserts that the message in a raised exception matches a regex.

        Args:
            expected_exception: Exception class expected to be raised.
            expected_regex: Regex (re.Pattern object or string) expected
                    to be found in error message.
            args: Function to be called and extra positional args.
            kwargs: Extra kwargs.
            msg: Optional message used in case of failure. Can only be used
                    when assertRaisesRegex is used as a context manager.
        '''
    ...
    def assertRaisesRegexp (*args, **kwargs):
      '''None'''
    ...
    def assertRegex (self, text, expected_regex, msg=None):
      '''Fail the test unless the text matches the regular expression.'''
    ...
    def assertRegexpMatches (*args, **kwargs):
      '''None'''
    ...
    def assertSequenceEqual (self, seq1, seq2, msg=None, seq_type=None):
      '''An equality assertion for ordered sequences (like lists and tuples).

        For the purposes of this function, a valid ordered sequence type is one
        which can be indexed, has a length, and has an equality operator.

        Args:
            seq1: The first sequence to compare.
            seq2: The second sequence to compare.
            seq_type: The expected datatype of the sequences, or None if no
                    datatype should be enforced.
            msg: Optional message to use on failure instead of a list of
                    differences.
        '''
    ...
    def assertSetEqual (self, set1, set2, msg=None):
      '''A set-specific equality assertion.

        Args:
            set1: The first set to compare.
            set2: The second set to compare.
            msg: Optional message to use on failure instead of a list of
                    differences.

        assertSetEqual uses ducktyping to support different types of sets, and
        is optimized for sets specifically (parameters must support a
        difference method).
        '''
    ...
    def assertTrue (self, expr, msg=None):
      '''Check that the expression is true.'''
    ...
    def assertTupleEqual (self, tuple1, tuple2, msg=None):
      '''A tuple-specific equality assertion.

        Args:
            tuple1: The first tuple to compare.
            tuple2: The second tuple to compare.
            msg: Optional message to use on failure instead of a list of
                    differences.
        '''
    ...
    def assertTypeNamesArePrefixed (self, module, namesToIgnore=()):
      '''None'''
    ...
    def assertWarns (self, expected_warning, *args, **kwargs):
      '''Fail unless a warning of class warnClass is triggered
           by the callable when invoked with specified positional and
           keyword arguments.  If a different type of warning is
           triggered, it will not be handled: depending on the other
           warning filtering rules in effect, it might be silenced, printed
           out, or raised as an exception.

           If called with the callable and arguments omitted, will return a
           context object used like this::

                with self.assertWarns(SomeWarning):
                    do_something()

           An optional keyword argument 'msg' can be provided when assertWarns
           is used as a context object.

           The context manager keeps a reference to the first matching
           warning as the 'warning' attribute; similarly, the 'filename'
           and 'lineno' attributes give you information about the line
           of Python code from which the warning was triggered.
           This allows you to inspect the warning after the assertion::

               with self.assertWarns(SomeWarning) as cm:
                   do_something()
               the_warning = cm.warning
               self.assertEqual(the_warning.some_attribute, 147)
        '''
    ...
    def assertWarnsRegex (self, expected_warning, expected_regex, *args, **kwargs):
      '''Asserts that the message in a triggered warning matches a regexp.
        Basic functioning is similar to assertWarns() with the addition
        that only warnings whose messages also match the regular expression
        are considered successful matches.

        Args:
            expected_warning: Warning class expected to be triggered.
            expected_regex: Regex (re.Pattern object or string) expected
                    to be found in error message.
            args: Function to be called and extra positional args.
            kwargs: Extra kwargs.
            msg: Optional message used in case of failure. Can only be used
                    when assertWarnsRegex is used as a context manager.
        '''
    ...
    def assert_ (*args, **kwargs):
      '''None'''
    ...
    def countTestCases (self):
      '''None'''
    ...
    def debug (self):
      '''Run the test without collecting errors in a TestResult'''
    ...
    def defaultTestResult (self):
      '''None'''
    ...
    def doClassCleanups ():
      '''Execute all class cleanup functions. Normally called for you after
        tearDownClass.'''
    ...
    def doCleanups (self):
      '''Execute all cleanup functions. Normally called for you after
        tearDown.'''
    ...
    def fail (self, msg=None):
      '''Fail immediately, with the given message.'''
    ...
    def failIf (*args, **kwargs):
      '''None'''
    ...
    def failIfAlmostEqual (*args, **kwargs):
      '''None'''
    ...
    def failIfEqual (*args, **kwargs):
      '''None'''
    ...
    def failUnless (*args, **kwargs):
      '''None'''
    ...
    def failUnlessAlmostEqual (*args, **kwargs):
      '''None'''
    ...
    def failUnlessEqual (*args, **kwargs):
      '''None'''
    ...
    def failUnlessRaises (*args, **kwargs):
      '''None'''
    ...
    def failureException (self, *args, **kwargs):
      '''Assertion failed.'''
    ...
    def failureMessageLevel (self, *args, **kwargs):
      '''None'''
    ...
    def id (self):
      '''None'''
    ...
    def ignoreMessage (self, level, context, message):
      '''None'''
    ...
    def longMessage (self, *args, **kwargs):
      '''bool(x) -> bool

Returns True when the argument x is true, False otherwise.
The builtins True and False are the only two instances of the class bool.
The class bool is a subclass of the class int, and cannot be subclassed.'''
    ...
    def maxDiff (self, *args, **kwargs):
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
    def run (self, result=None):
      '''None'''
    ...
    def scopedLocale (l, category=0):
      '''None'''
    ...
    def setUp (self):
      '''None'''
    ...
    def setUpClass ():
      '''Hook method for setting up class fixture before running tests in the class.'''
    ...
    def shortDescription (self):
      '''Returns a one-line description of the test, or None if no
        description has been provided.

        The default implementation of this method returns the first line of
        the specified test method's docstring.
        '''
    ...
    def skipTest (self, reason):
      '''Skip this test.'''
    ...
    def subTest (self, msg=<object object at 0x7fb108120c10>, **params):
      '''Return a context manager that will return the enclosed block
        of code in a subtest identified by the optional message and
        keyword parameters.  A failure in the subtest marks the test
        case as failed but resumes execution at the end of the enclosed
        block, allowing further test code to be executed.
        '''
    ...
    def tearDown (self):
      '''None'''
    ...
    def tearDownClass ():
      '''Hook method for deconstructing the class fixture after running all tests in the class.'''
    ...
    def temporaryDirectory (self):
      '''None'''
    ...
    def test (self):
      '''None'''
    ...

def LocalDispatcherTest (*args):
      '''

'''      
    ...

class LocalDispatcherTest:
    def _LocalDispatcherTest__createLocalDispatcher (self, jobPool=None):
      '''None'''
    ...
    def _TestCase__nodeHasDescription (self, node):
      '''None'''
    ...
    def _TestCase__undocumentedPlugs (self, node, additionalTerminalPlugTypes=()):
      '''None'''
    ...
    def _addExpectedFailure (self, result, exc_info):
      '''None'''
    ...
    def _addSkip (self, result, test_case, reason):
      '''None'''
    ...
    def _addUnexpectedSuccess (self, result):
      '''None'''
    ...
    def _baseAssertEqual (self, first, second, msg=None):
      '''The default assertEqual implementation, not type specific.'''
    ...
    def _callCleanup (self, function, /, *args, **kwargs):
      '''None'''
    ...
    def _callSetUp (self):
      '''None'''
    ...
    def _callTearDown (self):
      '''None'''
    ...
    def _callTestMethod (self, method):
      '''None'''
    ...
    def _classSetupFailed (self, *args, **kwargs):
      '''bool(x) -> bool

Returns True when the argument x is true, False otherwise.
The builtins True and False are the only two instances of the class bool.
The class bool is a subclass of the class int, and cannot be subclassed.'''
    ...
    def _class_cleanups (self, *args, **kwargs):
      '''Built-in mutable sequence.

If no argument is given, the constructor creates a new empty list.
The argument must be an iterable if specified.'''
    ...
    def _deprecate (original_func):
      '''None'''
    ...
    def _diffThreshold (self, *args, **kwargs):
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
    def _feedErrorsToResult (self, result, errors):
      '''None'''
    ...
    def _formatMessage (self, msg, standardMsg):
      '''Honour the longMessage attribute when generating failure messages.
        If longMessage is False this means:
        * Use only an explicit message if it is provided
        * Otherwise use the standard message for the assert

        If longMessage is True:
        * Use the standard message
        * If an explicit message is provided, plus ' : ' and the explicit message
        '''
    ...
    def _getAssertEqualityFunc (self, first, second):
      '''Get a detailed comparison function for the types of the two args.

        Returns: A callable accepting (first, second, msg=None) that will
        raise a failure exception if first != second with a useful human
        readable error message for those types.
        '''
    ...
    def _shutdownDuringBackgroundDispatch ():
      '''None'''
    ...
    def _truncateMessage (self, message, diff):
      '''None'''
    ...
    def addClassCleanup (function, /, *args, **kwargs):
      '''Same as addCleanup, except the cleanup items are called even if
        setUpClass fails (unlike tearDownClass).'''
    ...
    def addCleanup (self, function, /, *args, **kwargs):
      '''Add a function, with arguments, to be called when the test is
        completed. Functions added are called on a LIFO basis and are
        called after tearDown on test failure or success.

        Cleanup items are called even if setUp fails (unlike tearDown).'''
    ...
    def addTypeEqualityFunc (self, typeobj, function):
      '''Add a type specific assertEqual style function to compare a type.

        This method is for use by TestCase subclasses that need to register
        their own type equality functions to provide nicer error messages.

        Args:
            typeobj: The data type to call this function on when both values
                    are of the same type in assertEqual().
            function: The callable taking two arguments and an optional
                    msg= argument that raises self.failureException with a
                    useful error message when the two arguments are not equal.
        '''
    ...
    def assertAlmostEqual (self, first, second, places=None, msg=None, delta=None):
      '''Fail if the two objects are unequal as determined by their
           difference rounded to the given number of decimal places
           (default 7) and comparing to zero, or by comparing that the
           difference between the two objects is more than the given
           delta.

           Note that decimal places (from zero) are usually not the same
           as significant digits (measured from the most significant digit).

           If the two objects compare equal then they will automatically
           compare almost equal.
        '''
    ...
    def assertAlmostEquals (*args, **kwargs):
      '''None'''
    ...
    def assertCountEqual (self, first, second, msg=None):
      '''Asserts that two iterables have the same elements, the same number of
        times, without regard to order.

            self.assertEqual(Counter(list(first)),
                             Counter(list(second)))

         Example:
            - [0, 1, 1] and [1, 0, 1] compare equal.
            - [0, 0, 1] and [0, 1] compare unequal.

        '''
    ...
    def assertDefaultNamesAreCorrect (self, module, namesToIgnore=()):
      '''None'''
    ...
    def assertDictContainsSubset (self, subset, dictionary, msg=None):
      '''Checks whether dictionary is a superset of subset.'''
    ...
    def assertDictEqual (self, d1, d2, msg=None):
      '''None'''
    ...
    def assertEqual (self, first, second, msg=None):
      '''Fail if the two objects are unequal as determined by the '=='
           operator.
        '''
    ...
    def assertEquals (*args, **kwargs):
      '''None'''
    ...
    def assertFalse (self, expr, msg=None):
      '''Check that the expression is false.'''
    ...
    def assertFloat32Equal (self, value0, value1):
      '''None'''
    ...
    def assertGreater (self, a, b, msg=None):
      '''Just like self.assertTrue(a > b), but with a nicer default message.'''
    ...
    def assertGreaterEqual (self, a, b, msg=None):
      '''Just like self.assertTrue(a >= b), but with a nicer default message.'''
    ...
    def assertHashesValid (self, node, inputsToIgnore=[], outputsToIgnore=[]):
      '''None'''
    ...
    def assertIn (self, member, container, msg=None):
      '''Just like self.assertTrue(a in b), but with a nicer default message.'''
    ...
    def assertIs (self, expr1, expr2, msg=None):
      '''Just like self.assertTrue(a is b), but with a nicer default message.'''
    ...
    def assertIsInstance (self, obj, cls, msg=None):
      '''Same as self.assertTrue(isinstance(obj, cls)), with a nicer
        default message.'''
    ...
    def assertIsNone (self, obj, msg=None):
      '''Same as self.assertTrue(obj is None), with a nicer default message.'''
    ...
    def assertIsNot (self, expr1, expr2, msg=None):
      '''Just like self.assertTrue(a is not b), but with a nicer default message.'''
    ...
    def assertIsNotNone (self, obj, msg=None):
      '''Included for symmetry with assertIsNone.'''
    ...
    def assertLess (self, a, b, msg=None):
      '''Just like self.assertTrue(a < b), but with a nicer default message.'''
    ...
    def assertLessEqual (self, a, b, msg=None):
      '''Just like self.assertTrue(a <= b), but with a nicer default message.'''
    ...
    def assertListEqual (self, list1, list2, msg=None):
      '''A list-specific equality assertion.

        Args:
            list1: The first list to compare.
            list2: The second list to compare.
            msg: Optional message to use on failure instead of a list of
                    differences.

        '''
    ...
    def assertLogs (self, logger=None, level=None):
      '''Fail unless a log message of level *level* or higher is emitted
        on *logger_name* or its children.  If omitted, *level* defaults to
        INFO and *logger* defaults to the root logger.

        This method must be used as a context manager, and will yield
        a recording object with two attributes: `output` and `records`.
        At the end of the context manager, the `output` attribute will
        be a list of the matching formatted log messages and the
        `records` attribute will be a list of the corresponding LogRecord
        objects.

        Example::

            with self.assertLogs('foo', level='INFO') as cm:
                logging.getLogger('foo').info('first message')
                logging.getLogger('foo.bar').error('second message')
            self.assertEqual(cm.output, ['INFO:foo:first message',
                                         'ERROR:foo.bar:second message'])
        '''
    ...
    def assertModuleDoesNotImportUI (self, moduleName):
      '''None'''
    ...
    def assertMultiLineEqual (self, first, second, msg=None):
      '''Assert that two multi-line strings are equal.'''
    ...
    def assertNoLogs (self, logger=None, level=None):
      ''' Fail unless no log messages of level *level* or higher are emitted
        on *logger_name* or its children.

        This method must be used as a context manager.
        '''
    ...
    def assertNodeIsDocumented (self, node, additionalTerminalPlugTypes=()):
      '''None'''
    ...
    def assertNodesAreDocumented (self, module, additionalTerminalPlugTypes=(), nodesToIgnore=None):
      '''None'''
    ...
    def assertNodesConstructWithDefaultValues (self, module, nodesToIgnore=None, plugsToIgnore=None):
      '''None'''
    ...
    def assertNotAlmostEqual (self, first, second, places=None, msg=None, delta=None):
      '''Fail if the two objects are equal as determined by their
           difference rounded to the given number of decimal places
           (default 7) and comparing to zero, or by comparing that the
           difference between the two objects is less than the given delta.

           Note that decimal places (from zero) are usually not the same
           as significant digits (measured from the most significant digit).

           Objects that are equal automatically fail.
        '''
    ...
    def assertNotAlmostEquals (*args, **kwargs):
      '''None'''
    ...
    def assertNotEqual (self, first, second, msg=None):
      '''Fail if the two objects are equal as determined by the '!='
           operator.
        '''
    ...
    def assertNotEquals (*args, **kwargs):
      '''None'''
    ...
    def assertNotIn (self, member, container, msg=None):
      '''Just like self.assertTrue(a not in b), but with a nicer default message.'''
    ...
    def assertNotIsInstance (self, obj, cls, msg=None):
      '''Included for symmetry with assertIsInstance.'''
    ...
    def assertNotRegex (self, text, unexpected_regex, msg=None):
      '''Fail the test if the text matches the regular expression.'''
    ...
    def assertNotRegexpMatches (*args, **kwargs):
      '''None'''
    ...
    def assertRaises (self, expected_exception, *args, **kwargs):
      '''Fail unless an exception of class expected_exception is raised
           by the callable when invoked with specified positional and
           keyword arguments. If a different type of exception is
           raised, it will not be caught, and the test case will be
           deemed to have suffered an error, exactly as for an
           unexpected exception.

           If called with the callable and arguments omitted, will return a
           context object used like this::

                with self.assertRaises(SomeException):
                    do_something()

           An optional keyword argument 'msg' can be provided when assertRaises
           is used as a context object.

           The context manager keeps a reference to the exception as
           the 'exception' attribute. This allows you to inspect the
           exception after the assertion::

               with self.assertRaises(SomeException) as cm:
                   do_something()
               the_exception = cm.exception
               self.assertEqual(the_exception.error_code, 3)
        '''
    ...
    def assertRaisesRegex (self, expected_exception, expected_regex, *args, **kwargs):
      '''Asserts that the message in a raised exception matches a regex.

        Args:
            expected_exception: Exception class expected to be raised.
            expected_regex: Regex (re.Pattern object or string) expected
                    to be found in error message.
            args: Function to be called and extra positional args.
            kwargs: Extra kwargs.
            msg: Optional message used in case of failure. Can only be used
                    when assertRaisesRegex is used as a context manager.
        '''
    ...
    def assertRaisesRegexp (*args, **kwargs):
      '''None'''
    ...
    def assertRegex (self, text, expected_regex, msg=None):
      '''Fail the test unless the text matches the regular expression.'''
    ...
    def assertRegexpMatches (*args, **kwargs):
      '''None'''
    ...
    def assertSequenceEqual (self, seq1, seq2, msg=None, seq_type=None):
      '''An equality assertion for ordered sequences (like lists and tuples).

        For the purposes of this function, a valid ordered sequence type is one
        which can be indexed, has a length, and has an equality operator.

        Args:
            seq1: The first sequence to compare.
            seq2: The second sequence to compare.
            seq_type: The expected datatype of the sequences, or None if no
                    datatype should be enforced.
            msg: Optional message to use on failure instead of a list of
                    differences.
        '''
    ...
    def assertSetEqual (self, set1, set2, msg=None):
      '''A set-specific equality assertion.

        Args:
            set1: The first set to compare.
            set2: The second set to compare.
            msg: Optional message to use on failure instead of a list of
                    differences.

        assertSetEqual uses ducktyping to support different types of sets, and
        is optimized for sets specifically (parameters must support a
        difference method).
        '''
    ...
    def assertTrue (self, expr, msg=None):
      '''Check that the expression is true.'''
    ...
    def assertTupleEqual (self, tuple1, tuple2, msg=None):
      '''A tuple-specific equality assertion.

        Args:
            tuple1: The first tuple to compare.
            tuple2: The second tuple to compare.
            msg: Optional message to use on failure instead of a list of
                    differences.
        '''
    ...
    def assertTypeNamesArePrefixed (self, module, namesToIgnore=()):
      '''None'''
    ...
    def assertWarns (self, expected_warning, *args, **kwargs):
      '''Fail unless a warning of class warnClass is triggered
           by the callable when invoked with specified positional and
           keyword arguments.  If a different type of warning is
           triggered, it will not be handled: depending on the other
           warning filtering rules in effect, it might be silenced, printed
           out, or raised as an exception.

           If called with the callable and arguments omitted, will return a
           context object used like this::

                with self.assertWarns(SomeWarning):
                    do_something()

           An optional keyword argument 'msg' can be provided when assertWarns
           is used as a context object.

           The context manager keeps a reference to the first matching
           warning as the 'warning' attribute; similarly, the 'filename'
           and 'lineno' attributes give you information about the line
           of Python code from which the warning was triggered.
           This allows you to inspect the warning after the assertion::

               with self.assertWarns(SomeWarning) as cm:
                   do_something()
               the_warning = cm.warning
               self.assertEqual(the_warning.some_attribute, 147)
        '''
    ...
    def assertWarnsRegex (self, expected_warning, expected_regex, *args, **kwargs):
      '''Asserts that the message in a triggered warning matches a regexp.
        Basic functioning is similar to assertWarns() with the addition
        that only warnings whose messages also match the regular expression
        are considered successful matches.

        Args:
            expected_warning: Warning class expected to be triggered.
            expected_regex: Regex (re.Pattern object or string) expected
                    to be found in error message.
            args: Function to be called and extra positional args.
            kwargs: Extra kwargs.
            msg: Optional message used in case of failure. Can only be used
                    when assertWarnsRegex is used as a context manager.
        '''
    ...
    def assert_ (*args, **kwargs):
      '''None'''
    ...
    def countTestCases (self):
      '''None'''
    ...
    def debug (self):
      '''Run the test without collecting errors in a TestResult'''
    ...
    def defaultTestResult (self):
      '''None'''
    ...
    def doClassCleanups ():
      '''Execute all class cleanup functions. Normally called for you after
        tearDownClass.'''
    ...
    def doCleanups (self):
      '''Execute all cleanup functions. Normally called for you after
        tearDown.'''
    ...
    def fail (self, msg=None):
      '''Fail immediately, with the given message.'''
    ...
    def failIf (*args, **kwargs):
      '''None'''
    ...
    def failIfAlmostEqual (*args, **kwargs):
      '''None'''
    ...
    def failIfEqual (*args, **kwargs):
      '''None'''
    ...
    def failUnless (*args, **kwargs):
      '''None'''
    ...
    def failUnlessAlmostEqual (*args, **kwargs):
      '''None'''
    ...
    def failUnlessEqual (*args, **kwargs):
      '''None'''
    ...
    def failUnlessRaises (*args, **kwargs):
      '''None'''
    ...
    def failureException (self, *args, **kwargs):
      '''Assertion failed.'''
    ...
    def failureMessageLevel (self, *args, **kwargs):
      '''None'''
    ...
    def id (self):
      '''None'''
    ...
    def ignoreMessage (self, level, context, message):
      '''None'''
    ...
    def longMessage (self, *args, **kwargs):
      '''bool(x) -> bool

Returns True when the argument x is true, False otherwise.
The builtins True and False are the only two instances of the class bool.
The class bool is a subclass of the class int, and cannot be subclassed.'''
    ...
    def maxDiff (self, *args, **kwargs):
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
    def run (self, result=None):
      '''None'''
    ...
    def scopedLocale (l, category=0):
      '''None'''
    ...
    def setUp (self):
      '''None'''
    ...
    def setUpClass ():
      '''Hook method for setting up class fixture before running tests in the class.'''
    ...
    def shortDescription (self):
      '''Returns a one-line description of the test, or None if no
        description has been provided.

        The default implementation of this method returns the first line of
        the specified test method's docstring.
        '''
    ...
    def skipTest (self, reason):
      '''Skip this test.'''
    ...
    def subTest (self, msg=<object object at 0x7fb108120c10>, **params):
      '''Return a context manager that will return the enclosed block
        of code in a subtest identified by the optional message and
        keyword parameters.  A failure in the subtest marks the test
        case as failed but resumes execution at the end of the enclosed
        block, allowing further test code to be executed.
        '''
    ...
    def tearDown (self):
      '''None'''
    ...
    def tearDownClass ():
      '''Hook method for deconstructing the class fixture after running all tests in the class.'''
    ...
    def temporaryDirectory (self):
      '''None'''
    ...
    def testBackgroundBatchesCanAccessJobDirectory (self):
      '''None'''
    ...
    def testBackgroundJobFailureStatus (self):
      '''None'''
    ...
    def testContextLockedDuringBackgroundDispatch (self):
      '''None'''
    ...
    def testContextVariation (self):
      '''None'''
    ...
    def testDispatch (self):
      '''None'''
    ...
    def testDispatchBadCustomRange (self):
      '''None'''
    ...
    def testDispatchCustomRange (self):
      '''None'''
    ...
    def testDispatchDifferentFrame (self):
      '''None'''
    ...
    def testDispatchFullRange (self):
      '''None'''
    ...
    def testDispatcherRegistration (self):
      '''None'''
    ...
    def testDispatcherSignals (self):
      '''None'''
    ...
    def testEnvironmentCommand (self):
      '''None'''
    ...
    def testEnvironmentCommandSubstitutions (self):
      '''None'''
    ...
    def testExecuteInBackground (self):
      '''None'''
    ...
    def testFailure (self):
      '''None'''
    ...
    def testIgnoreScriptLoadErrors (self):
      '''None'''
    ...
    def testImathContextVariable (self):
      '''None'''
    ...
    def testJobPoolSignals (self):
      '''None'''
    ...
    def testJobStatusChangedSignal (self):
      '''None'''
    ...
    def testKill (self):
      '''None'''
    ...
    def testMessageLevels (self):
      '''None'''
    ...
    def testMixedImmediateAndBackground (self):
      '''None'''
    ...
    def testMultipleDispatchers (self):
      '''None'''
    ...
    def testNestedDispatchBorrowingOuterJobDirectory (self):
      '''None'''
    ...
    def testNoNestedBackgroundDispatch (self):
      '''None'''
    ...
    def testNodeNamesLockedDuringBackgroundDispatch (self):
      '''None'''
    ...
    def testRunningTime (self):
      '''None'''
    ...
    def testScaling (self):
      '''None'''
    ...
    def testShutdownDuringBackgroundDispatch (self):
      '''None'''
    ...
    def testSpacesInContext (self):
      '''None'''
    ...
    def testSubprocessMessages (self):
      '''None'''
    ...
    def testUIContextEntriesIgnored (self):
      '''None'''
    ...
    def testUpstreamDispatchJobDirectory (self):
      '''None'''
    ...

def LoggingTaskNode (*args):
      '''

'''      
    ...

class LoggingTaskNode:
    def BinaryPlugSignal (self, *args, **kwargs):
      '''None'''
    ...
    def BinarySignal (self, *args, **kwargs):
      '''None'''
    ...
    def ErrorSignal (self, *args, **kwargs):
      '''None'''
    ...
    def LogEntry (node, context, frames):
      '''LogEntry(node, context, frames)'''
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
acceptsChild( (TaskNode)arg1, (GraphComponent)arg2) -> bool :

    C++ signature :
        bool acceptsChild(GafferDispatch::TaskNode,Gaffer::GraphComponent const*)'''
    ...
    def acceptsParent (self, *args, **kwargs):
      '''
acceptsParent( (TaskNode)arg1, (GraphComponent)arg2) -> bool :

    C++ signature :
        bool acceptsParent(GafferDispatch::TaskNode,Gaffer::GraphComponent const*)'''
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
    def execute (self):
      '''None'''
    ...
    def executeSequence (self, frames):
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
    def getName (self, *args, **kwargs):
      '''
getName( (GraphComponent)arg1) -> str :

    C++ signature :
        char const* getName(Gaffer::GraphComponent {lvalue})'''
    ...
    def hash (self, context):
      '''None'''
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
    def postTasks (self, *args, **kwargs):
      '''
postTasks( (TaskNode)arg1, (Context)arg2) -> list :

    C++ signature :
        boost::python::list postTasks(GafferDispatch::TaskNode {lvalue},Gaffer::Context*)'''
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
    def requiresSequenceExecution (self):
      '''None'''
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

def ModuleTest (*args):
      '''

'''      
    ...

class ModuleTest:
    def _TestCase__nodeHasDescription (self, node):
      '''None'''
    ...
    def _TestCase__undocumentedPlugs (self, node, additionalTerminalPlugTypes=()):
      '''None'''
    ...
    def _addExpectedFailure (self, result, exc_info):
      '''None'''
    ...
    def _addSkip (self, result, test_case, reason):
      '''None'''
    ...
    def _addUnexpectedSuccess (self, result):
      '''None'''
    ...
    def _baseAssertEqual (self, first, second, msg=None):
      '''The default assertEqual implementation, not type specific.'''
    ...
    def _callCleanup (self, function, /, *args, **kwargs):
      '''None'''
    ...
    def _callSetUp (self):
      '''None'''
    ...
    def _callTearDown (self):
      '''None'''
    ...
    def _callTestMethod (self, method):
      '''None'''
    ...
    def _classSetupFailed (self, *args, **kwargs):
      '''bool(x) -> bool

Returns True when the argument x is true, False otherwise.
The builtins True and False are the only two instances of the class bool.
The class bool is a subclass of the class int, and cannot be subclassed.'''
    ...
    def _class_cleanups (self, *args, **kwargs):
      '''Built-in mutable sequence.

If no argument is given, the constructor creates a new empty list.
The argument must be an iterable if specified.'''
    ...
    def _deprecate (original_func):
      '''None'''
    ...
    def _diffThreshold (self, *args, **kwargs):
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
    def _feedErrorsToResult (self, result, errors):
      '''None'''
    ...
    def _formatMessage (self, msg, standardMsg):
      '''Honour the longMessage attribute when generating failure messages.
        If longMessage is False this means:
        * Use only an explicit message if it is provided
        * Otherwise use the standard message for the assert

        If longMessage is True:
        * Use the standard message
        * If an explicit message is provided, plus ' : ' and the explicit message
        '''
    ...
    def _getAssertEqualityFunc (self, first, second):
      '''Get a detailed comparison function for the types of the two args.

        Returns: A callable accepting (first, second, msg=None) that will
        raise a failure exception if first != second with a useful human
        readable error message for those types.
        '''
    ...
    def _truncateMessage (self, message, diff):
      '''None'''
    ...
    def addClassCleanup (function, /, *args, **kwargs):
      '''Same as addCleanup, except the cleanup items are called even if
        setUpClass fails (unlike tearDownClass).'''
    ...
    def addCleanup (self, function, /, *args, **kwargs):
      '''Add a function, with arguments, to be called when the test is
        completed. Functions added are called on a LIFO basis and are
        called after tearDown on test failure or success.

        Cleanup items are called even if setUp fails (unlike tearDown).'''
    ...
    def addTypeEqualityFunc (self, typeobj, function):
      '''Add a type specific assertEqual style function to compare a type.

        This method is for use by TestCase subclasses that need to register
        their own type equality functions to provide nicer error messages.

        Args:
            typeobj: The data type to call this function on when both values
                    are of the same type in assertEqual().
            function: The callable taking two arguments and an optional
                    msg= argument that raises self.failureException with a
                    useful error message when the two arguments are not equal.
        '''
    ...
    def assertAlmostEqual (self, first, second, places=None, msg=None, delta=None):
      '''Fail if the two objects are unequal as determined by their
           difference rounded to the given number of decimal places
           (default 7) and comparing to zero, or by comparing that the
           difference between the two objects is more than the given
           delta.

           Note that decimal places (from zero) are usually not the same
           as significant digits (measured from the most significant digit).

           If the two objects compare equal then they will automatically
           compare almost equal.
        '''
    ...
    def assertAlmostEquals (*args, **kwargs):
      '''None'''
    ...
    def assertCountEqual (self, first, second, msg=None):
      '''Asserts that two iterables have the same elements, the same number of
        times, without regard to order.

            self.assertEqual(Counter(list(first)),
                             Counter(list(second)))

         Example:
            - [0, 1, 1] and [1, 0, 1] compare equal.
            - [0, 0, 1] and [0, 1] compare unequal.

        '''
    ...
    def assertDefaultNamesAreCorrect (self, module, namesToIgnore=()):
      '''None'''
    ...
    def assertDictContainsSubset (self, subset, dictionary, msg=None):
      '''Checks whether dictionary is a superset of subset.'''
    ...
    def assertDictEqual (self, d1, d2, msg=None):
      '''None'''
    ...
    def assertEqual (self, first, second, msg=None):
      '''Fail if the two objects are unequal as determined by the '=='
           operator.
        '''
    ...
    def assertEquals (*args, **kwargs):
      '''None'''
    ...
    def assertFalse (self, expr, msg=None):
      '''Check that the expression is false.'''
    ...
    def assertFloat32Equal (self, value0, value1):
      '''None'''
    ...
    def assertGreater (self, a, b, msg=None):
      '''Just like self.assertTrue(a > b), but with a nicer default message.'''
    ...
    def assertGreaterEqual (self, a, b, msg=None):
      '''Just like self.assertTrue(a >= b), but with a nicer default message.'''
    ...
    def assertHashesValid (self, node, inputsToIgnore=[], outputsToIgnore=[]):
      '''None'''
    ...
    def assertIn (self, member, container, msg=None):
      '''Just like self.assertTrue(a in b), but with a nicer default message.'''
    ...
    def assertIs (self, expr1, expr2, msg=None):
      '''Just like self.assertTrue(a is b), but with a nicer default message.'''
    ...
    def assertIsInstance (self, obj, cls, msg=None):
      '''Same as self.assertTrue(isinstance(obj, cls)), with a nicer
        default message.'''
    ...
    def assertIsNone (self, obj, msg=None):
      '''Same as self.assertTrue(obj is None), with a nicer default message.'''
    ...
    def assertIsNot (self, expr1, expr2, msg=None):
      '''Just like self.assertTrue(a is not b), but with a nicer default message.'''
    ...
    def assertIsNotNone (self, obj, msg=None):
      '''Included for symmetry with assertIsNone.'''
    ...
    def assertLess (self, a, b, msg=None):
      '''Just like self.assertTrue(a < b), but with a nicer default message.'''
    ...
    def assertLessEqual (self, a, b, msg=None):
      '''Just like self.assertTrue(a <= b), but with a nicer default message.'''
    ...
    def assertListEqual (self, list1, list2, msg=None):
      '''A list-specific equality assertion.

        Args:
            list1: The first list to compare.
            list2: The second list to compare.
            msg: Optional message to use on failure instead of a list of
                    differences.

        '''
    ...
    def assertLogs (self, logger=None, level=None):
      '''Fail unless a log message of level *level* or higher is emitted
        on *logger_name* or its children.  If omitted, *level* defaults to
        INFO and *logger* defaults to the root logger.

        This method must be used as a context manager, and will yield
        a recording object with two attributes: `output` and `records`.
        At the end of the context manager, the `output` attribute will
        be a list of the matching formatted log messages and the
        `records` attribute will be a list of the corresponding LogRecord
        objects.

        Example::

            with self.assertLogs('foo', level='INFO') as cm:
                logging.getLogger('foo').info('first message')
                logging.getLogger('foo.bar').error('second message')
            self.assertEqual(cm.output, ['INFO:foo:first message',
                                         'ERROR:foo.bar:second message'])
        '''
    ...
    def assertModuleDoesNotImportUI (self, moduleName):
      '''None'''
    ...
    def assertMultiLineEqual (self, first, second, msg=None):
      '''Assert that two multi-line strings are equal.'''
    ...
    def assertNoLogs (self, logger=None, level=None):
      ''' Fail unless no log messages of level *level* or higher are emitted
        on *logger_name* or its children.

        This method must be used as a context manager.
        '''
    ...
    def assertNodeIsDocumented (self, node, additionalTerminalPlugTypes=()):
      '''None'''
    ...
    def assertNodesAreDocumented (self, module, additionalTerminalPlugTypes=(), nodesToIgnore=None):
      '''None'''
    ...
    def assertNodesConstructWithDefaultValues (self, module, nodesToIgnore=None, plugsToIgnore=None):
      '''None'''
    ...
    def assertNotAlmostEqual (self, first, second, places=None, msg=None, delta=None):
      '''Fail if the two objects are equal as determined by their
           difference rounded to the given number of decimal places
           (default 7) and comparing to zero, or by comparing that the
           difference between the two objects is less than the given delta.

           Note that decimal places (from zero) are usually not the same
           as significant digits (measured from the most significant digit).

           Objects that are equal automatically fail.
        '''
    ...
    def assertNotAlmostEquals (*args, **kwargs):
      '''None'''
    ...
    def assertNotEqual (self, first, second, msg=None):
      '''Fail if the two objects are equal as determined by the '!='
           operator.
        '''
    ...
    def assertNotEquals (*args, **kwargs):
      '''None'''
    ...
    def assertNotIn (self, member, container, msg=None):
      '''Just like self.assertTrue(a not in b), but with a nicer default message.'''
    ...
    def assertNotIsInstance (self, obj, cls, msg=None):
      '''Included for symmetry with assertIsInstance.'''
    ...
    def assertNotRegex (self, text, unexpected_regex, msg=None):
      '''Fail the test if the text matches the regular expression.'''
    ...
    def assertNotRegexpMatches (*args, **kwargs):
      '''None'''
    ...
    def assertRaises (self, expected_exception, *args, **kwargs):
      '''Fail unless an exception of class expected_exception is raised
           by the callable when invoked with specified positional and
           keyword arguments. If a different type of exception is
           raised, it will not be caught, and the test case will be
           deemed to have suffered an error, exactly as for an
           unexpected exception.

           If called with the callable and arguments omitted, will return a
           context object used like this::

                with self.assertRaises(SomeException):
                    do_something()

           An optional keyword argument 'msg' can be provided when assertRaises
           is used as a context object.

           The context manager keeps a reference to the exception as
           the 'exception' attribute. This allows you to inspect the
           exception after the assertion::

               with self.assertRaises(SomeException) as cm:
                   do_something()
               the_exception = cm.exception
               self.assertEqual(the_exception.error_code, 3)
        '''
    ...
    def assertRaisesRegex (self, expected_exception, expected_regex, *args, **kwargs):
      '''Asserts that the message in a raised exception matches a regex.

        Args:
            expected_exception: Exception class expected to be raised.
            expected_regex: Regex (re.Pattern object or string) expected
                    to be found in error message.
            args: Function to be called and extra positional args.
            kwargs: Extra kwargs.
            msg: Optional message used in case of failure. Can only be used
                    when assertRaisesRegex is used as a context manager.
        '''
    ...
    def assertRaisesRegexp (*args, **kwargs):
      '''None'''
    ...
    def assertRegex (self, text, expected_regex, msg=None):
      '''Fail the test unless the text matches the regular expression.'''
    ...
    def assertRegexpMatches (*args, **kwargs):
      '''None'''
    ...
    def assertSequenceEqual (self, seq1, seq2, msg=None, seq_type=None):
      '''An equality assertion for ordered sequences (like lists and tuples).

        For the purposes of this function, a valid ordered sequence type is one
        which can be indexed, has a length, and has an equality operator.

        Args:
            seq1: The first sequence to compare.
            seq2: The second sequence to compare.
            seq_type: The expected datatype of the sequences, or None if no
                    datatype should be enforced.
            msg: Optional message to use on failure instead of a list of
                    differences.
        '''
    ...
    def assertSetEqual (self, set1, set2, msg=None):
      '''A set-specific equality assertion.

        Args:
            set1: The first set to compare.
            set2: The second set to compare.
            msg: Optional message to use on failure instead of a list of
                    differences.

        assertSetEqual uses ducktyping to support different types of sets, and
        is optimized for sets specifically (parameters must support a
        difference method).
        '''
    ...
    def assertTrue (self, expr, msg=None):
      '''Check that the expression is true.'''
    ...
    def assertTupleEqual (self, tuple1, tuple2, msg=None):
      '''A tuple-specific equality assertion.

        Args:
            tuple1: The first tuple to compare.
            tuple2: The second tuple to compare.
            msg: Optional message to use on failure instead of a list of
                    differences.
        '''
    ...
    def assertTypeNamesArePrefixed (self, module, namesToIgnore=()):
      '''None'''
    ...
    def assertWarns (self, expected_warning, *args, **kwargs):
      '''Fail unless a warning of class warnClass is triggered
           by the callable when invoked with specified positional and
           keyword arguments.  If a different type of warning is
           triggered, it will not be handled: depending on the other
           warning filtering rules in effect, it might be silenced, printed
           out, or raised as an exception.

           If called with the callable and arguments omitted, will return a
           context object used like this::

                with self.assertWarns(SomeWarning):
                    do_something()

           An optional keyword argument 'msg' can be provided when assertWarns
           is used as a context object.

           The context manager keeps a reference to the first matching
           warning as the 'warning' attribute; similarly, the 'filename'
           and 'lineno' attributes give you information about the line
           of Python code from which the warning was triggered.
           This allows you to inspect the warning after the assertion::

               with self.assertWarns(SomeWarning) as cm:
                   do_something()
               the_warning = cm.warning
               self.assertEqual(the_warning.some_attribute, 147)
        '''
    ...
    def assertWarnsRegex (self, expected_warning, expected_regex, *args, **kwargs):
      '''Asserts that the message in a triggered warning matches a regexp.
        Basic functioning is similar to assertWarns() with the addition
        that only warnings whose messages also match the regular expression
        are considered successful matches.

        Args:
            expected_warning: Warning class expected to be triggered.
            expected_regex: Regex (re.Pattern object or string) expected
                    to be found in error message.
            args: Function to be called and extra positional args.
            kwargs: Extra kwargs.
            msg: Optional message used in case of failure. Can only be used
                    when assertWarnsRegex is used as a context manager.
        '''
    ...
    def assert_ (*args, **kwargs):
      '''None'''
    ...
    def countTestCases (self):
      '''None'''
    ...
    def debug (self):
      '''Run the test without collecting errors in a TestResult'''
    ...
    def defaultTestResult (self):
      '''None'''
    ...
    def doClassCleanups ():
      '''Execute all class cleanup functions. Normally called for you after
        tearDownClass.'''
    ...
    def doCleanups (self):
      '''Execute all cleanup functions. Normally called for you after
        tearDown.'''
    ...
    def fail (self, msg=None):
      '''Fail immediately, with the given message.'''
    ...
    def failIf (*args, **kwargs):
      '''None'''
    ...
    def failIfAlmostEqual (*args, **kwargs):
      '''None'''
    ...
    def failIfEqual (*args, **kwargs):
      '''None'''
    ...
    def failUnless (*args, **kwargs):
      '''None'''
    ...
    def failUnlessAlmostEqual (*args, **kwargs):
      '''None'''
    ...
    def failUnlessEqual (*args, **kwargs):
      '''None'''
    ...
    def failUnlessRaises (*args, **kwargs):
      '''None'''
    ...
    def failureException (self, *args, **kwargs):
      '''Assertion failed.'''
    ...
    def failureMessageLevel (self, *args, **kwargs):
      '''None'''
    ...
    def id (self):
      '''None'''
    ...
    def ignoreMessage (self, level, context, message):
      '''None'''
    ...
    def longMessage (self, *args, **kwargs):
      '''bool(x) -> bool

Returns True when the argument x is true, False otherwise.
The builtins True and False are the only two instances of the class bool.
The class bool is a subclass of the class int, and cannot be subclassed.'''
    ...
    def maxDiff (self, *args, **kwargs):
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
    def run (self, result=None):
      '''None'''
    ...
    def scopedLocale (l, category=0):
      '''None'''
    ...
    def setUp (self):
      '''None'''
    ...
    def setUpClass ():
      '''Hook method for setting up class fixture before running tests in the class.'''
    ...
    def shortDescription (self):
      '''Returns a one-line description of the test, or None if no
        description has been provided.

        The default implementation of this method returns the first line of
        the specified test method's docstring.
        '''
    ...
    def skipTest (self, reason):
      '''Skip this test.'''
    ...
    def subTest (self, msg=<object object at 0x7fb108120c10>, **params):
      '''Return a context manager that will return the enclosed block
        of code in a subtest identified by the optional message and
        keyword parameters.  A failure in the subtest marks the test
        case as failed but resumes execution at the end of the enclosed
        block, allowing further test code to be executed.
        '''
    ...
    def tearDown (self):
      '''None'''
    ...
    def tearDownClass ():
      '''Hook method for deconstructing the class fixture after running all tests in the class.'''
    ...
    def temporaryDirectory (self):
      '''None'''
    ...
    def testDoesNotImportUI (self):
      '''None'''
    ...

def PythonCommandTest (*args):
      '''

'''      
    ...

class PythonCommandTest:
    def _PythonCommandTest__dispatcher (self, frameRange=None):
      '''None'''
    ...
    def _TestCase__nodeHasDescription (self, node):
      '''None'''
    ...
    def _TestCase__undocumentedPlugs (self, node, additionalTerminalPlugTypes=()):
      '''None'''
    ...
    def _addExpectedFailure (self, result, exc_info):
      '''None'''
    ...
    def _addSkip (self, result, test_case, reason):
      '''None'''
    ...
    def _addUnexpectedSuccess (self, result):
      '''None'''
    ...
    def _baseAssertEqual (self, first, second, msg=None):
      '''The default assertEqual implementation, not type specific.'''
    ...
    def _callCleanup (self, function, /, *args, **kwargs):
      '''None'''
    ...
    def _callSetUp (self):
      '''None'''
    ...
    def _callTearDown (self):
      '''None'''
    ...
    def _callTestMethod (self, method):
      '''None'''
    ...
    def _classSetupFailed (self, *args, **kwargs):
      '''bool(x) -> bool

Returns True when the argument x is true, False otherwise.
The builtins True and False are the only two instances of the class bool.
The class bool is a subclass of the class int, and cannot be subclassed.'''
    ...
    def _class_cleanups (self, *args, **kwargs):
      '''Built-in mutable sequence.

If no argument is given, the constructor creates a new empty list.
The argument must be an iterable if specified.'''
    ...
    def _deprecate (original_func):
      '''None'''
    ...
    def _diffThreshold (self, *args, **kwargs):
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
    def _feedErrorsToResult (self, result, errors):
      '''None'''
    ...
    def _formatMessage (self, msg, standardMsg):
      '''Honour the longMessage attribute when generating failure messages.
        If longMessage is False this means:
        * Use only an explicit message if it is provided
        * Otherwise use the standard message for the assert

        If longMessage is True:
        * Use the standard message
        * If an explicit message is provided, plus ' : ' and the explicit message
        '''
    ...
    def _getAssertEqualityFunc (self, first, second):
      '''Get a detailed comparison function for the types of the two args.

        Returns: A callable accepting (first, second, msg=None) that will
        raise a failure exception if first != second with a useful human
        readable error message for those types.
        '''
    ...
    def _truncateMessage (self, message, diff):
      '''None'''
    ...
    def addClassCleanup (function, /, *args, **kwargs):
      '''Same as addCleanup, except the cleanup items are called even if
        setUpClass fails (unlike tearDownClass).'''
    ...
    def addCleanup (self, function, /, *args, **kwargs):
      '''Add a function, with arguments, to be called when the test is
        completed. Functions added are called on a LIFO basis and are
        called after tearDown on test failure or success.

        Cleanup items are called even if setUp fails (unlike tearDown).'''
    ...
    def addTypeEqualityFunc (self, typeobj, function):
      '''Add a type specific assertEqual style function to compare a type.

        This method is for use by TestCase subclasses that need to register
        their own type equality functions to provide nicer error messages.

        Args:
            typeobj: The data type to call this function on when both values
                    are of the same type in assertEqual().
            function: The callable taking two arguments and an optional
                    msg= argument that raises self.failureException with a
                    useful error message when the two arguments are not equal.
        '''
    ...
    def assertAlmostEqual (self, first, second, places=None, msg=None, delta=None):
      '''Fail if the two objects are unequal as determined by their
           difference rounded to the given number of decimal places
           (default 7) and comparing to zero, or by comparing that the
           difference between the two objects is more than the given
           delta.

           Note that decimal places (from zero) are usually not the same
           as significant digits (measured from the most significant digit).

           If the two objects compare equal then they will automatically
           compare almost equal.
        '''
    ...
    def assertAlmostEquals (*args, **kwargs):
      '''None'''
    ...
    def assertCountEqual (self, first, second, msg=None):
      '''Asserts that two iterables have the same elements, the same number of
        times, without regard to order.

            self.assertEqual(Counter(list(first)),
                             Counter(list(second)))

         Example:
            - [0, 1, 1] and [1, 0, 1] compare equal.
            - [0, 0, 1] and [0, 1] compare unequal.

        '''
    ...
    def assertDefaultNamesAreCorrect (self, module, namesToIgnore=()):
      '''None'''
    ...
    def assertDictContainsSubset (self, subset, dictionary, msg=None):
      '''Checks whether dictionary is a superset of subset.'''
    ...
    def assertDictEqual (self, d1, d2, msg=None):
      '''None'''
    ...
    def assertEqual (self, first, second, msg=None):
      '''Fail if the two objects are unequal as determined by the '=='
           operator.
        '''
    ...
    def assertEquals (*args, **kwargs):
      '''None'''
    ...
    def assertFalse (self, expr, msg=None):
      '''Check that the expression is false.'''
    ...
    def assertFloat32Equal (self, value0, value1):
      '''None'''
    ...
    def assertGreater (self, a, b, msg=None):
      '''Just like self.assertTrue(a > b), but with a nicer default message.'''
    ...
    def assertGreaterEqual (self, a, b, msg=None):
      '''Just like self.assertTrue(a >= b), but with a nicer default message.'''
    ...
    def assertHashesValid (self, node, inputsToIgnore=[], outputsToIgnore=[]):
      '''None'''
    ...
    def assertIn (self, member, container, msg=None):
      '''Just like self.assertTrue(a in b), but with a nicer default message.'''
    ...
    def assertIs (self, expr1, expr2, msg=None):
      '''Just like self.assertTrue(a is b), but with a nicer default message.'''
    ...
    def assertIsInstance (self, obj, cls, msg=None):
      '''Same as self.assertTrue(isinstance(obj, cls)), with a nicer
        default message.'''
    ...
    def assertIsNone (self, obj, msg=None):
      '''Same as self.assertTrue(obj is None), with a nicer default message.'''
    ...
    def assertIsNot (self, expr1, expr2, msg=None):
      '''Just like self.assertTrue(a is not b), but with a nicer default message.'''
    ...
    def assertIsNotNone (self, obj, msg=None):
      '''Included for symmetry with assertIsNone.'''
    ...
    def assertLess (self, a, b, msg=None):
      '''Just like self.assertTrue(a < b), but with a nicer default message.'''
    ...
    def assertLessEqual (self, a, b, msg=None):
      '''Just like self.assertTrue(a <= b), but with a nicer default message.'''
    ...
    def assertListEqual (self, list1, list2, msg=None):
      '''A list-specific equality assertion.

        Args:
            list1: The first list to compare.
            list2: The second list to compare.
            msg: Optional message to use on failure instead of a list of
                    differences.

        '''
    ...
    def assertLogs (self, logger=None, level=None):
      '''Fail unless a log message of level *level* or higher is emitted
        on *logger_name* or its children.  If omitted, *level* defaults to
        INFO and *logger* defaults to the root logger.

        This method must be used as a context manager, and will yield
        a recording object with two attributes: `output` and `records`.
        At the end of the context manager, the `output` attribute will
        be a list of the matching formatted log messages and the
        `records` attribute will be a list of the corresponding LogRecord
        objects.

        Example::

            with self.assertLogs('foo', level='INFO') as cm:
                logging.getLogger('foo').info('first message')
                logging.getLogger('foo.bar').error('second message')
            self.assertEqual(cm.output, ['INFO:foo:first message',
                                         'ERROR:foo.bar:second message'])
        '''
    ...
    def assertModuleDoesNotImportUI (self, moduleName):
      '''None'''
    ...
    def assertMultiLineEqual (self, first, second, msg=None):
      '''Assert that two multi-line strings are equal.'''
    ...
    def assertNoLogs (self, logger=None, level=None):
      ''' Fail unless no log messages of level *level* or higher are emitted
        on *logger_name* or its children.

        This method must be used as a context manager.
        '''
    ...
    def assertNodeIsDocumented (self, node, additionalTerminalPlugTypes=()):
      '''None'''
    ...
    def assertNodesAreDocumented (self, module, additionalTerminalPlugTypes=(), nodesToIgnore=None):
      '''None'''
    ...
    def assertNodesConstructWithDefaultValues (self, module, nodesToIgnore=None, plugsToIgnore=None):
      '''None'''
    ...
    def assertNotAlmostEqual (self, first, second, places=None, msg=None, delta=None):
      '''Fail if the two objects are equal as determined by their
           difference rounded to the given number of decimal places
           (default 7) and comparing to zero, or by comparing that the
           difference between the two objects is less than the given delta.

           Note that decimal places (from zero) are usually not the same
           as significant digits (measured from the most significant digit).

           Objects that are equal automatically fail.
        '''
    ...
    def assertNotAlmostEquals (*args, **kwargs):
      '''None'''
    ...
    def assertNotEqual (self, first, second, msg=None):
      '''Fail if the two objects are equal as determined by the '!='
           operator.
        '''
    ...
    def assertNotEquals (*args, **kwargs):
      '''None'''
    ...
    def assertNotIn (self, member, container, msg=None):
      '''Just like self.assertTrue(a not in b), but with a nicer default message.'''
    ...
    def assertNotIsInstance (self, obj, cls, msg=None):
      '''Included for symmetry with assertIsInstance.'''
    ...
    def assertNotRegex (self, text, unexpected_regex, msg=None):
      '''Fail the test if the text matches the regular expression.'''
    ...
    def assertNotRegexpMatches (*args, **kwargs):
      '''None'''
    ...
    def assertRaises (self, expected_exception, *args, **kwargs):
      '''Fail unless an exception of class expected_exception is raised
           by the callable when invoked with specified positional and
           keyword arguments. If a different type of exception is
           raised, it will not be caught, and the test case will be
           deemed to have suffered an error, exactly as for an
           unexpected exception.

           If called with the callable and arguments omitted, will return a
           context object used like this::

                with self.assertRaises(SomeException):
                    do_something()

           An optional keyword argument 'msg' can be provided when assertRaises
           is used as a context object.

           The context manager keeps a reference to the exception as
           the 'exception' attribute. This allows you to inspect the
           exception after the assertion::

               with self.assertRaises(SomeException) as cm:
                   do_something()
               the_exception = cm.exception
               self.assertEqual(the_exception.error_code, 3)
        '''
    ...
    def assertRaisesRegex (self, expected_exception, expected_regex, *args, **kwargs):
      '''Asserts that the message in a raised exception matches a regex.

        Args:
            expected_exception: Exception class expected to be raised.
            expected_regex: Regex (re.Pattern object or string) expected
                    to be found in error message.
            args: Function to be called and extra positional args.
            kwargs: Extra kwargs.
            msg: Optional message used in case of failure. Can only be used
                    when assertRaisesRegex is used as a context manager.
        '''
    ...
    def assertRaisesRegexp (*args, **kwargs):
      '''None'''
    ...
    def assertRegex (self, text, expected_regex, msg=None):
      '''Fail the test unless the text matches the regular expression.'''
    ...
    def assertRegexpMatches (*args, **kwargs):
      '''None'''
    ...
    def assertSequenceEqual (self, seq1, seq2, msg=None, seq_type=None):
      '''An equality assertion for ordered sequences (like lists and tuples).

        For the purposes of this function, a valid ordered sequence type is one
        which can be indexed, has a length, and has an equality operator.

        Args:
            seq1: The first sequence to compare.
            seq2: The second sequence to compare.
            seq_type: The expected datatype of the sequences, or None if no
                    datatype should be enforced.
            msg: Optional message to use on failure instead of a list of
                    differences.
        '''
    ...
    def assertSetEqual (self, set1, set2, msg=None):
      '''A set-specific equality assertion.

        Args:
            set1: The first set to compare.
            set2: The second set to compare.
            msg: Optional message to use on failure instead of a list of
                    differences.

        assertSetEqual uses ducktyping to support different types of sets, and
        is optimized for sets specifically (parameters must support a
        difference method).
        '''
    ...
    def assertTrue (self, expr, msg=None):
      '''Check that the expression is true.'''
    ...
    def assertTupleEqual (self, tuple1, tuple2, msg=None):
      '''A tuple-specific equality assertion.

        Args:
            tuple1: The first tuple to compare.
            tuple2: The second tuple to compare.
            msg: Optional message to use on failure instead of a list of
                    differences.
        '''
    ...
    def assertTypeNamesArePrefixed (self, module, namesToIgnore=()):
      '''None'''
    ...
    def assertWarns (self, expected_warning, *args, **kwargs):
      '''Fail unless a warning of class warnClass is triggered
           by the callable when invoked with specified positional and
           keyword arguments.  If a different type of warning is
           triggered, it will not be handled: depending on the other
           warning filtering rules in effect, it might be silenced, printed
           out, or raised as an exception.

           If called with the callable and arguments omitted, will return a
           context object used like this::

                with self.assertWarns(SomeWarning):
                    do_something()

           An optional keyword argument 'msg' can be provided when assertWarns
           is used as a context object.

           The context manager keeps a reference to the first matching
           warning as the 'warning' attribute; similarly, the 'filename'
           and 'lineno' attributes give you information about the line
           of Python code from which the warning was triggered.
           This allows you to inspect the warning after the assertion::

               with self.assertWarns(SomeWarning) as cm:
                   do_something()
               the_warning = cm.warning
               self.assertEqual(the_warning.some_attribute, 147)
        '''
    ...
    def assertWarnsRegex (self, expected_warning, expected_regex, *args, **kwargs):
      '''Asserts that the message in a triggered warning matches a regexp.
        Basic functioning is similar to assertWarns() with the addition
        that only warnings whose messages also match the regular expression
        are considered successful matches.

        Args:
            expected_warning: Warning class expected to be triggered.
            expected_regex: Regex (re.Pattern object or string) expected
                    to be found in error message.
            args: Function to be called and extra positional args.
            kwargs: Extra kwargs.
            msg: Optional message used in case of failure. Can only be used
                    when assertWarnsRegex is used as a context manager.
        '''
    ...
    def assert_ (*args, **kwargs):
      '''None'''
    ...
    def countTestCases (self):
      '''None'''
    ...
    def debug (self):
      '''Run the test without collecting errors in a TestResult'''
    ...
    def defaultTestResult (self):
      '''None'''
    ...
    def doClassCleanups ():
      '''Execute all class cleanup functions. Normally called for you after
        tearDownClass.'''
    ...
    def doCleanups (self):
      '''Execute all cleanup functions. Normally called for you after
        tearDown.'''
    ...
    def fail (self, msg=None):
      '''Fail immediately, with the given message.'''
    ...
    def failIf (*args, **kwargs):
      '''None'''
    ...
    def failIfAlmostEqual (*args, **kwargs):
      '''None'''
    ...
    def failIfEqual (*args, **kwargs):
      '''None'''
    ...
    def failUnless (*args, **kwargs):
      '''None'''
    ...
    def failUnlessAlmostEqual (*args, **kwargs):
      '''None'''
    ...
    def failUnlessEqual (*args, **kwargs):
      '''None'''
    ...
    def failUnlessRaises (*args, **kwargs):
      '''None'''
    ...
    def failureException (self, *args, **kwargs):
      '''Assertion failed.'''
    ...
    def failureMessageLevel (self, *args, **kwargs):
      '''None'''
    ...
    def id (self):
      '''None'''
    ...
    def ignoreMessage (self, level, context, message):
      '''None'''
    ...
    def longMessage (self, *args, **kwargs):
      '''bool(x) -> bool

Returns True when the argument x is true, False otherwise.
The builtins True and False are the only two instances of the class bool.
The class bool is a subclass of the class int, and cannot be subclassed.'''
    ...
    def maxDiff (self, *args, **kwargs):
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
    def run (self, result=None):
      '''None'''
    ...
    def scopedLocale (l, category=0):
      '''None'''
    ...
    def setUp (self):
      '''None'''
    ...
    def setUpClass ():
      '''Hook method for setting up class fixture before running tests in the class.'''
    ...
    def shortDescription (self):
      '''Returns a one-line description of the test, or None if no
        description has been provided.

        The default implementation of this method returns the first line of
        the specified test method's docstring.
        '''
    ...
    def skipTest (self, reason):
      '''Skip this test.'''
    ...
    def subTest (self, msg=<object object at 0x7fb108120c10>, **params):
      '''Return a context manager that will return the enclosed block
        of code in a subtest identified by the optional message and
        keyword parameters.  A failure in the subtest marks the test
        case as failed but resumes execution at the end of the enclosed
        block, allowing further test code to be executed.
        '''
    ...
    def tearDown (self):
      '''None'''
    ...
    def tearDownClass ():
      '''Hook method for deconstructing the class fixture after running all tests in the class.'''
    ...
    def temporaryDirectory (self):
      '''None'''
    ...
    def testAlternateMissingContextVariables (self):
      '''None'''
    ...
    def testCannotAccessVariablesOutsideFrameRange (self):
      '''None'''
    ...
    def testComments (self):
      '''None'''
    ...
    def testContextAccess (self):
      '''None'''
    ...
    def testContextAffectsHash (self):
      '''None'''
    ...
    def testContextGetNone (self):
      '''None'''
    ...
    def testContextModificationsDontLeak (self):
      '''None'''
    ...
    def testEmptyCommand (self):
      '''None'''
    ...
    def testFramesNotAvailableInNonSequenceMode (self):
      '''None'''
    ...
    def testImath (self):
      '''None'''
    ...
    def testNonSequenceDispatch (self):
      '''None'''
    ...
    def testRequiresSequenceExecution (self):
      '''None'''
    ...
    def testSelf (self):
      '''None'''
    ...
    def testSequenceMode (self):
      '''None'''
    ...
    def testSequenceModeStaticVariable (self):
      '''None'''
    ...
    def testSequenceModeVariable (self):
      '''None'''
    ...
    def testStringSubstitutions (self):
      '''None'''
    ...
    def testVariables (self):
      '''None'''
    ...
    def testVariablesRepr (self):
      '''None'''
    ...

def StatsApplicationTest (*args):
      '''

'''      
    ...

class StatsApplicationTest:
    def _TestCase__nodeHasDescription (self, node):
      '''None'''
    ...
    def _TestCase__undocumentedPlugs (self, node, additionalTerminalPlugTypes=()):
      '''None'''
    ...
    def _addExpectedFailure (self, result, exc_info):
      '''None'''
    ...
    def _addSkip (self, result, test_case, reason):
      '''None'''
    ...
    def _addUnexpectedSuccess (self, result):
      '''None'''
    ...
    def _baseAssertEqual (self, first, second, msg=None):
      '''The default assertEqual implementation, not type specific.'''
    ...
    def _callCleanup (self, function, /, *args, **kwargs):
      '''None'''
    ...
    def _callSetUp (self):
      '''None'''
    ...
    def _callTearDown (self):
      '''None'''
    ...
    def _callTestMethod (self, method):
      '''None'''
    ...
    def _classSetupFailed (self, *args, **kwargs):
      '''bool(x) -> bool

Returns True when the argument x is true, False otherwise.
The builtins True and False are the only two instances of the class bool.
The class bool is a subclass of the class int, and cannot be subclassed.'''
    ...
    def _class_cleanups (self, *args, **kwargs):
      '''Built-in mutable sequence.

If no argument is given, the constructor creates a new empty list.
The argument must be an iterable if specified.'''
    ...
    def _deprecate (original_func):
      '''None'''
    ...
    def _diffThreshold (self, *args, **kwargs):
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
    def _feedErrorsToResult (self, result, errors):
      '''None'''
    ...
    def _formatMessage (self, msg, standardMsg):
      '''Honour the longMessage attribute when generating failure messages.
        If longMessage is False this means:
        * Use only an explicit message if it is provided
        * Otherwise use the standard message for the assert

        If longMessage is True:
        * Use the standard message
        * If an explicit message is provided, plus ' : ' and the explicit message
        '''
    ...
    def _getAssertEqualityFunc (self, first, second):
      '''Get a detailed comparison function for the types of the two args.

        Returns: A callable accepting (first, second, msg=None) that will
        raise a failure exception if first != second with a useful human
        readable error message for those types.
        '''
    ...
    def _truncateMessage (self, message, diff):
      '''None'''
    ...
    def addClassCleanup (function, /, *args, **kwargs):
      '''Same as addCleanup, except the cleanup items are called even if
        setUpClass fails (unlike tearDownClass).'''
    ...
    def addCleanup (self, function, /, *args, **kwargs):
      '''Add a function, with arguments, to be called when the test is
        completed. Functions added are called on a LIFO basis and are
        called after tearDown on test failure or success.

        Cleanup items are called even if setUp fails (unlike tearDown).'''
    ...
    def addTypeEqualityFunc (self, typeobj, function):
      '''Add a type specific assertEqual style function to compare a type.

        This method is for use by TestCase subclasses that need to register
        their own type equality functions to provide nicer error messages.

        Args:
            typeobj: The data type to call this function on when both values
                    are of the same type in assertEqual().
            function: The callable taking two arguments and an optional
                    msg= argument that raises self.failureException with a
                    useful error message when the two arguments are not equal.
        '''
    ...
    def assertAlmostEqual (self, first, second, places=None, msg=None, delta=None):
      '''Fail if the two objects are unequal as determined by their
           difference rounded to the given number of decimal places
           (default 7) and comparing to zero, or by comparing that the
           difference between the two objects is more than the given
           delta.

           Note that decimal places (from zero) are usually not the same
           as significant digits (measured from the most significant digit).

           If the two objects compare equal then they will automatically
           compare almost equal.
        '''
    ...
    def assertAlmostEquals (*args, **kwargs):
      '''None'''
    ...
    def assertCountEqual (self, first, second, msg=None):
      '''Asserts that two iterables have the same elements, the same number of
        times, without regard to order.

            self.assertEqual(Counter(list(first)),
                             Counter(list(second)))

         Example:
            - [0, 1, 1] and [1, 0, 1] compare equal.
            - [0, 0, 1] and [0, 1] compare unequal.

        '''
    ...
    def assertDefaultNamesAreCorrect (self, module, namesToIgnore=()):
      '''None'''
    ...
    def assertDictContainsSubset (self, subset, dictionary, msg=None):
      '''Checks whether dictionary is a superset of subset.'''
    ...
    def assertDictEqual (self, d1, d2, msg=None):
      '''None'''
    ...
    def assertEqual (self, first, second, msg=None):
      '''Fail if the two objects are unequal as determined by the '=='
           operator.
        '''
    ...
    def assertEquals (*args, **kwargs):
      '''None'''
    ...
    def assertFalse (self, expr, msg=None):
      '''Check that the expression is false.'''
    ...
    def assertFloat32Equal (self, value0, value1):
      '''None'''
    ...
    def assertGreater (self, a, b, msg=None):
      '''Just like self.assertTrue(a > b), but with a nicer default message.'''
    ...
    def assertGreaterEqual (self, a, b, msg=None):
      '''Just like self.assertTrue(a >= b), but with a nicer default message.'''
    ...
    def assertHashesValid (self, node, inputsToIgnore=[], outputsToIgnore=[]):
      '''None'''
    ...
    def assertIn (self, member, container, msg=None):
      '''Just like self.assertTrue(a in b), but with a nicer default message.'''
    ...
    def assertIs (self, expr1, expr2, msg=None):
      '''Just like self.assertTrue(a is b), but with a nicer default message.'''
    ...
    def assertIsInstance (self, obj, cls, msg=None):
      '''Same as self.assertTrue(isinstance(obj, cls)), with a nicer
        default message.'''
    ...
    def assertIsNone (self, obj, msg=None):
      '''Same as self.assertTrue(obj is None), with a nicer default message.'''
    ...
    def assertIsNot (self, expr1, expr2, msg=None):
      '''Just like self.assertTrue(a is not b), but with a nicer default message.'''
    ...
    def assertIsNotNone (self, obj, msg=None):
      '''Included for symmetry with assertIsNone.'''
    ...
    def assertLess (self, a, b, msg=None):
      '''Just like self.assertTrue(a < b), but with a nicer default message.'''
    ...
    def assertLessEqual (self, a, b, msg=None):
      '''Just like self.assertTrue(a <= b), but with a nicer default message.'''
    ...
    def assertListEqual (self, list1, list2, msg=None):
      '''A list-specific equality assertion.

        Args:
            list1: The first list to compare.
            list2: The second list to compare.
            msg: Optional message to use on failure instead of a list of
                    differences.

        '''
    ...
    def assertLogs (self, logger=None, level=None):
      '''Fail unless a log message of level *level* or higher is emitted
        on *logger_name* or its children.  If omitted, *level* defaults to
        INFO and *logger* defaults to the root logger.

        This method must be used as a context manager, and will yield
        a recording object with two attributes: `output` and `records`.
        At the end of the context manager, the `output` attribute will
        be a list of the matching formatted log messages and the
        `records` attribute will be a list of the corresponding LogRecord
        objects.

        Example::

            with self.assertLogs('foo', level='INFO') as cm:
                logging.getLogger('foo').info('first message')
                logging.getLogger('foo.bar').error('second message')
            self.assertEqual(cm.output, ['INFO:foo:first message',
                                         'ERROR:foo.bar:second message'])
        '''
    ...
    def assertModuleDoesNotImportUI (self, moduleName):
      '''None'''
    ...
    def assertMultiLineEqual (self, first, second, msg=None):
      '''Assert that two multi-line strings are equal.'''
    ...
    def assertNoLogs (self, logger=None, level=None):
      ''' Fail unless no log messages of level *level* or higher are emitted
        on *logger_name* or its children.

        This method must be used as a context manager.
        '''
    ...
    def assertNodeIsDocumented (self, node, additionalTerminalPlugTypes=()):
      '''None'''
    ...
    def assertNodesAreDocumented (self, module, additionalTerminalPlugTypes=(), nodesToIgnore=None):
      '''None'''
    ...
    def assertNodesConstructWithDefaultValues (self, module, nodesToIgnore=None, plugsToIgnore=None):
      '''None'''
    ...
    def assertNotAlmostEqual (self, first, second, places=None, msg=None, delta=None):
      '''Fail if the two objects are equal as determined by their
           difference rounded to the given number of decimal places
           (default 7) and comparing to zero, or by comparing that the
           difference between the two objects is less than the given delta.

           Note that decimal places (from zero) are usually not the same
           as significant digits (measured from the most significant digit).

           Objects that are equal automatically fail.
        '''
    ...
    def assertNotAlmostEquals (*args, **kwargs):
      '''None'''
    ...
    def assertNotEqual (self, first, second, msg=None):
      '''Fail if the two objects are equal as determined by the '!='
           operator.
        '''
    ...
    def assertNotEquals (*args, **kwargs):
      '''None'''
    ...
    def assertNotIn (self, member, container, msg=None):
      '''Just like self.assertTrue(a not in b), but with a nicer default message.'''
    ...
    def assertNotIsInstance (self, obj, cls, msg=None):
      '''Included for symmetry with assertIsInstance.'''
    ...
    def assertNotRegex (self, text, unexpected_regex, msg=None):
      '''Fail the test if the text matches the regular expression.'''
    ...
    def assertNotRegexpMatches (*args, **kwargs):
      '''None'''
    ...
    def assertRaises (self, expected_exception, *args, **kwargs):
      '''Fail unless an exception of class expected_exception is raised
           by the callable when invoked with specified positional and
           keyword arguments. If a different type of exception is
           raised, it will not be caught, and the test case will be
           deemed to have suffered an error, exactly as for an
           unexpected exception.

           If called with the callable and arguments omitted, will return a
           context object used like this::

                with self.assertRaises(SomeException):
                    do_something()

           An optional keyword argument 'msg' can be provided when assertRaises
           is used as a context object.

           The context manager keeps a reference to the exception as
           the 'exception' attribute. This allows you to inspect the
           exception after the assertion::

               with self.assertRaises(SomeException) as cm:
                   do_something()
               the_exception = cm.exception
               self.assertEqual(the_exception.error_code, 3)
        '''
    ...
    def assertRaisesRegex (self, expected_exception, expected_regex, *args, **kwargs):
      '''Asserts that the message in a raised exception matches a regex.

        Args:
            expected_exception: Exception class expected to be raised.
            expected_regex: Regex (re.Pattern object or string) expected
                    to be found in error message.
            args: Function to be called and extra positional args.
            kwargs: Extra kwargs.
            msg: Optional message used in case of failure. Can only be used
                    when assertRaisesRegex is used as a context manager.
        '''
    ...
    def assertRaisesRegexp (*args, **kwargs):
      '''None'''
    ...
    def assertRegex (self, text, expected_regex, msg=None):
      '''Fail the test unless the text matches the regular expression.'''
    ...
    def assertRegexpMatches (*args, **kwargs):
      '''None'''
    ...
    def assertSequenceEqual (self, seq1, seq2, msg=None, seq_type=None):
      '''An equality assertion for ordered sequences (like lists and tuples).

        For the purposes of this function, a valid ordered sequence type is one
        which can be indexed, has a length, and has an equality operator.

        Args:
            seq1: The first sequence to compare.
            seq2: The second sequence to compare.
            seq_type: The expected datatype of the sequences, or None if no
                    datatype should be enforced.
            msg: Optional message to use on failure instead of a list of
                    differences.
        '''
    ...
    def assertSetEqual (self, set1, set2, msg=None):
      '''A set-specific equality assertion.

        Args:
            set1: The first set to compare.
            set2: The second set to compare.
            msg: Optional message to use on failure instead of a list of
                    differences.

        assertSetEqual uses ducktyping to support different types of sets, and
        is optimized for sets specifically (parameters must support a
        difference method).
        '''
    ...
    def assertTrue (self, expr, msg=None):
      '''Check that the expression is true.'''
    ...
    def assertTupleEqual (self, tuple1, tuple2, msg=None):
      '''A tuple-specific equality assertion.

        Args:
            tuple1: The first tuple to compare.
            tuple2: The second tuple to compare.
            msg: Optional message to use on failure instead of a list of
                    differences.
        '''
    ...
    def assertTypeNamesArePrefixed (self, module, namesToIgnore=()):
      '''None'''
    ...
    def assertWarns (self, expected_warning, *args, **kwargs):
      '''Fail unless a warning of class warnClass is triggered
           by the callable when invoked with specified positional and
           keyword arguments.  If a different type of warning is
           triggered, it will not be handled: depending on the other
           warning filtering rules in effect, it might be silenced, printed
           out, or raised as an exception.

           If called with the callable and arguments omitted, will return a
           context object used like this::

                with self.assertWarns(SomeWarning):
                    do_something()

           An optional keyword argument 'msg' can be provided when assertWarns
           is used as a context object.

           The context manager keeps a reference to the first matching
           warning as the 'warning' attribute; similarly, the 'filename'
           and 'lineno' attributes give you information about the line
           of Python code from which the warning was triggered.
           This allows you to inspect the warning after the assertion::

               with self.assertWarns(SomeWarning) as cm:
                   do_something()
               the_warning = cm.warning
               self.assertEqual(the_warning.some_attribute, 147)
        '''
    ...
    def assertWarnsRegex (self, expected_warning, expected_regex, *args, **kwargs):
      '''Asserts that the message in a triggered warning matches a regexp.
        Basic functioning is similar to assertWarns() with the addition
        that only warnings whose messages also match the regular expression
        are considered successful matches.

        Args:
            expected_warning: Warning class expected to be triggered.
            expected_regex: Regex (re.Pattern object or string) expected
                    to be found in error message.
            args: Function to be called and extra positional args.
            kwargs: Extra kwargs.
            msg: Optional message used in case of failure. Can only be used
                    when assertWarnsRegex is used as a context manager.
        '''
    ...
    def assert_ (*args, **kwargs):
      '''None'''
    ...
    def countTestCases (self):
      '''None'''
    ...
    def debug (self):
      '''Run the test without collecting errors in a TestResult'''
    ...
    def defaultTestResult (self):
      '''None'''
    ...
    def doClassCleanups ():
      '''Execute all class cleanup functions. Normally called for you after
        tearDownClass.'''
    ...
    def doCleanups (self):
      '''Execute all cleanup functions. Normally called for you after
        tearDown.'''
    ...
    def fail (self, msg=None):
      '''Fail immediately, with the given message.'''
    ...
    def failIf (*args, **kwargs):
      '''None'''
    ...
    def failIfAlmostEqual (*args, **kwargs):
      '''None'''
    ...
    def failIfEqual (*args, **kwargs):
      '''None'''
    ...
    def failUnless (*args, **kwargs):
      '''None'''
    ...
    def failUnlessAlmostEqual (*args, **kwargs):
      '''None'''
    ...
    def failUnlessEqual (*args, **kwargs):
      '''None'''
    ...
    def failUnlessRaises (*args, **kwargs):
      '''None'''
    ...
    def failureException (self, *args, **kwargs):
      '''Assertion failed.'''
    ...
    def failureMessageLevel (self, *args, **kwargs):
      '''None'''
    ...
    def id (self):
      '''None'''
    ...
    def ignoreMessage (self, level, context, message):
      '''None'''
    ...
    def longMessage (self, *args, **kwargs):
      '''bool(x) -> bool

Returns True when the argument x is true, False otherwise.
The builtins True and False are the only two instances of the class bool.
The class bool is a subclass of the class int, and cannot be subclassed.'''
    ...
    def maxDiff (self, *args, **kwargs):
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
    def run (self, result=None):
      '''None'''
    ...
    def scopedLocale (l, category=0):
      '''None'''
    ...
    def setUp (self):
      '''None'''
    ...
    def setUpClass ():
      '''Hook method for setting up class fixture before running tests in the class.'''
    ...
    def shortDescription (self):
      '''Returns a one-line description of the test, or None if no
        description has been provided.

        The default implementation of this method returns the first line of
        the specified test method's docstring.
        '''
    ...
    def skipTest (self, reason):
      '''Skip this test.'''
    ...
    def subTest (self, msg=<object object at 0x7fb108120c10>, **params):
      '''Return a context manager that will return the enclosed block
        of code in a subtest identified by the optional message and
        keyword parameters.  A failure in the subtest marks the test
        case as failed but resumes execution at the end of the enclosed
        block, allowing further test code to be executed.
        '''
    ...
    def tearDown (self):
      '''None'''
    ...
    def tearDownClass ():
      '''Hook method for deconstructing the class fixture after running all tests in the class.'''
    ...
    def temporaryDirectory (self):
      '''None'''
    ...
    def testContext (self):
      '''None'''
    ...

def SystemCommandTest (*args):
      '''

'''      
    ...

class SystemCommandTest:
    def _TestCase__nodeHasDescription (self, node):
      '''None'''
    ...
    def _TestCase__undocumentedPlugs (self, node, additionalTerminalPlugTypes=()):
      '''None'''
    ...
    def _addExpectedFailure (self, result, exc_info):
      '''None'''
    ...
    def _addSkip (self, result, test_case, reason):
      '''None'''
    ...
    def _addUnexpectedSuccess (self, result):
      '''None'''
    ...
    def _baseAssertEqual (self, first, second, msg=None):
      '''The default assertEqual implementation, not type specific.'''
    ...
    def _callCleanup (self, function, /, *args, **kwargs):
      '''None'''
    ...
    def _callSetUp (self):
      '''None'''
    ...
    def _callTearDown (self):
      '''None'''
    ...
    def _callTestMethod (self, method):
      '''None'''
    ...
    def _classSetupFailed (self, *args, **kwargs):
      '''bool(x) -> bool

Returns True when the argument x is true, False otherwise.
The builtins True and False are the only two instances of the class bool.
The class bool is a subclass of the class int, and cannot be subclassed.'''
    ...
    def _class_cleanups (self, *args, **kwargs):
      '''Built-in mutable sequence.

If no argument is given, the constructor creates a new empty list.
The argument must be an iterable if specified.'''
    ...
    def _deprecate (original_func):
      '''None'''
    ...
    def _diffThreshold (self, *args, **kwargs):
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
    def _feedErrorsToResult (self, result, errors):
      '''None'''
    ...
    def _formatMessage (self, msg, standardMsg):
      '''Honour the longMessage attribute when generating failure messages.
        If longMessage is False this means:
        * Use only an explicit message if it is provided
        * Otherwise use the standard message for the assert

        If longMessage is True:
        * Use the standard message
        * If an explicit message is provided, plus ' : ' and the explicit message
        '''
    ...
    def _getAssertEqualityFunc (self, first, second):
      '''Get a detailed comparison function for the types of the two args.

        Returns: A callable accepting (first, second, msg=None) that will
        raise a failure exception if first != second with a useful human
        readable error message for those types.
        '''
    ...
    def _truncateMessage (self, message, diff):
      '''None'''
    ...
    def addClassCleanup (function, /, *args, **kwargs):
      '''Same as addCleanup, except the cleanup items are called even if
        setUpClass fails (unlike tearDownClass).'''
    ...
    def addCleanup (self, function, /, *args, **kwargs):
      '''Add a function, with arguments, to be called when the test is
        completed. Functions added are called on a LIFO basis and are
        called after tearDown on test failure or success.

        Cleanup items are called even if setUp fails (unlike tearDown).'''
    ...
    def addTypeEqualityFunc (self, typeobj, function):
      '''Add a type specific assertEqual style function to compare a type.

        This method is for use by TestCase subclasses that need to register
        their own type equality functions to provide nicer error messages.

        Args:
            typeobj: The data type to call this function on when both values
                    are of the same type in assertEqual().
            function: The callable taking two arguments and an optional
                    msg= argument that raises self.failureException with a
                    useful error message when the two arguments are not equal.
        '''
    ...
    def assertAlmostEqual (self, first, second, places=None, msg=None, delta=None):
      '''Fail if the two objects are unequal as determined by their
           difference rounded to the given number of decimal places
           (default 7) and comparing to zero, or by comparing that the
           difference between the two objects is more than the given
           delta.

           Note that decimal places (from zero) are usually not the same
           as significant digits (measured from the most significant digit).

           If the two objects compare equal then they will automatically
           compare almost equal.
        '''
    ...
    def assertAlmostEquals (*args, **kwargs):
      '''None'''
    ...
    def assertCountEqual (self, first, second, msg=None):
      '''Asserts that two iterables have the same elements, the same number of
        times, without regard to order.

            self.assertEqual(Counter(list(first)),
                             Counter(list(second)))

         Example:
            - [0, 1, 1] and [1, 0, 1] compare equal.
            - [0, 0, 1] and [0, 1] compare unequal.

        '''
    ...
    def assertDefaultNamesAreCorrect (self, module, namesToIgnore=()):
      '''None'''
    ...
    def assertDictContainsSubset (self, subset, dictionary, msg=None):
      '''Checks whether dictionary is a superset of subset.'''
    ...
    def assertDictEqual (self, d1, d2, msg=None):
      '''None'''
    ...
    def assertEqual (self, first, second, msg=None):
      '''Fail if the two objects are unequal as determined by the '=='
           operator.
        '''
    ...
    def assertEquals (*args, **kwargs):
      '''None'''
    ...
    def assertFalse (self, expr, msg=None):
      '''Check that the expression is false.'''
    ...
    def assertFloat32Equal (self, value0, value1):
      '''None'''
    ...
    def assertGreater (self, a, b, msg=None):
      '''Just like self.assertTrue(a > b), but with a nicer default message.'''
    ...
    def assertGreaterEqual (self, a, b, msg=None):
      '''Just like self.assertTrue(a >= b), but with a nicer default message.'''
    ...
    def assertHashesValid (self, node, inputsToIgnore=[], outputsToIgnore=[]):
      '''None'''
    ...
    def assertIn (self, member, container, msg=None):
      '''Just like self.assertTrue(a in b), but with a nicer default message.'''
    ...
    def assertIs (self, expr1, expr2, msg=None):
      '''Just like self.assertTrue(a is b), but with a nicer default message.'''
    ...
    def assertIsInstance (self, obj, cls, msg=None):
      '''Same as self.assertTrue(isinstance(obj, cls)), with a nicer
        default message.'''
    ...
    def assertIsNone (self, obj, msg=None):
      '''Same as self.assertTrue(obj is None), with a nicer default message.'''
    ...
    def assertIsNot (self, expr1, expr2, msg=None):
      '''Just like self.assertTrue(a is not b), but with a nicer default message.'''
    ...
    def assertIsNotNone (self, obj, msg=None):
      '''Included for symmetry with assertIsNone.'''
    ...
    def assertLess (self, a, b, msg=None):
      '''Just like self.assertTrue(a < b), but with a nicer default message.'''
    ...
    def assertLessEqual (self, a, b, msg=None):
      '''Just like self.assertTrue(a <= b), but with a nicer default message.'''
    ...
    def assertListEqual (self, list1, list2, msg=None):
      '''A list-specific equality assertion.

        Args:
            list1: The first list to compare.
            list2: The second list to compare.
            msg: Optional message to use on failure instead of a list of
                    differences.

        '''
    ...
    def assertLogs (self, logger=None, level=None):
      '''Fail unless a log message of level *level* or higher is emitted
        on *logger_name* or its children.  If omitted, *level* defaults to
        INFO and *logger* defaults to the root logger.

        This method must be used as a context manager, and will yield
        a recording object with two attributes: `output` and `records`.
        At the end of the context manager, the `output` attribute will
        be a list of the matching formatted log messages and the
        `records` attribute will be a list of the corresponding LogRecord
        objects.

        Example::

            with self.assertLogs('foo', level='INFO') as cm:
                logging.getLogger('foo').info('first message')
                logging.getLogger('foo.bar').error('second message')
            self.assertEqual(cm.output, ['INFO:foo:first message',
                                         'ERROR:foo.bar:second message'])
        '''
    ...
    def assertModuleDoesNotImportUI (self, moduleName):
      '''None'''
    ...
    def assertMultiLineEqual (self, first, second, msg=None):
      '''Assert that two multi-line strings are equal.'''
    ...
    def assertNoLogs (self, logger=None, level=None):
      ''' Fail unless no log messages of level *level* or higher are emitted
        on *logger_name* or its children.

        This method must be used as a context manager.
        '''
    ...
    def assertNodeIsDocumented (self, node, additionalTerminalPlugTypes=()):
      '''None'''
    ...
    def assertNodesAreDocumented (self, module, additionalTerminalPlugTypes=(), nodesToIgnore=None):
      '''None'''
    ...
    def assertNodesConstructWithDefaultValues (self, module, nodesToIgnore=None, plugsToIgnore=None):
      '''None'''
    ...
    def assertNotAlmostEqual (self, first, second, places=None, msg=None, delta=None):
      '''Fail if the two objects are equal as determined by their
           difference rounded to the given number of decimal places
           (default 7) and comparing to zero, or by comparing that the
           difference between the two objects is less than the given delta.

           Note that decimal places (from zero) are usually not the same
           as significant digits (measured from the most significant digit).

           Objects that are equal automatically fail.
        '''
    ...
    def assertNotAlmostEquals (*args, **kwargs):
      '''None'''
    ...
    def assertNotEqual (self, first, second, msg=None):
      '''Fail if the two objects are equal as determined by the '!='
           operator.
        '''
    ...
    def assertNotEquals (*args, **kwargs):
      '''None'''
    ...
    def assertNotIn (self, member, container, msg=None):
      '''Just like self.assertTrue(a not in b), but with a nicer default message.'''
    ...
    def assertNotIsInstance (self, obj, cls, msg=None):
      '''Included for symmetry with assertIsInstance.'''
    ...
    def assertNotRegex (self, text, unexpected_regex, msg=None):
      '''Fail the test if the text matches the regular expression.'''
    ...
    def assertNotRegexpMatches (*args, **kwargs):
      '''None'''
    ...
    def assertRaises (self, expected_exception, *args, **kwargs):
      '''Fail unless an exception of class expected_exception is raised
           by the callable when invoked with specified positional and
           keyword arguments. If a different type of exception is
           raised, it will not be caught, and the test case will be
           deemed to have suffered an error, exactly as for an
           unexpected exception.

           If called with the callable and arguments omitted, will return a
           context object used like this::

                with self.assertRaises(SomeException):
                    do_something()

           An optional keyword argument 'msg' can be provided when assertRaises
           is used as a context object.

           The context manager keeps a reference to the exception as
           the 'exception' attribute. This allows you to inspect the
           exception after the assertion::

               with self.assertRaises(SomeException) as cm:
                   do_something()
               the_exception = cm.exception
               self.assertEqual(the_exception.error_code, 3)
        '''
    ...
    def assertRaisesRegex (self, expected_exception, expected_regex, *args, **kwargs):
      '''Asserts that the message in a raised exception matches a regex.

        Args:
            expected_exception: Exception class expected to be raised.
            expected_regex: Regex (re.Pattern object or string) expected
                    to be found in error message.
            args: Function to be called and extra positional args.
            kwargs: Extra kwargs.
            msg: Optional message used in case of failure. Can only be used
                    when assertRaisesRegex is used as a context manager.
        '''
    ...
    def assertRaisesRegexp (*args, **kwargs):
      '''None'''
    ...
    def assertRegex (self, text, expected_regex, msg=None):
      '''Fail the test unless the text matches the regular expression.'''
    ...
    def assertRegexpMatches (*args, **kwargs):
      '''None'''
    ...
    def assertSequenceEqual (self, seq1, seq2, msg=None, seq_type=None):
      '''An equality assertion for ordered sequences (like lists and tuples).

        For the purposes of this function, a valid ordered sequence type is one
        which can be indexed, has a length, and has an equality operator.

        Args:
            seq1: The first sequence to compare.
            seq2: The second sequence to compare.
            seq_type: The expected datatype of the sequences, or None if no
                    datatype should be enforced.
            msg: Optional message to use on failure instead of a list of
                    differences.
        '''
    ...
    def assertSetEqual (self, set1, set2, msg=None):
      '''A set-specific equality assertion.

        Args:
            set1: The first set to compare.
            set2: The second set to compare.
            msg: Optional message to use on failure instead of a list of
                    differences.

        assertSetEqual uses ducktyping to support different types of sets, and
        is optimized for sets specifically (parameters must support a
        difference method).
        '''
    ...
    def assertTrue (self, expr, msg=None):
      '''Check that the expression is true.'''
    ...
    def assertTupleEqual (self, tuple1, tuple2, msg=None):
      '''A tuple-specific equality assertion.

        Args:
            tuple1: The first tuple to compare.
            tuple2: The second tuple to compare.
            msg: Optional message to use on failure instead of a list of
                    differences.
        '''
    ...
    def assertTypeNamesArePrefixed (self, module, namesToIgnore=()):
      '''None'''
    ...
    def assertWarns (self, expected_warning, *args, **kwargs):
      '''Fail unless a warning of class warnClass is triggered
           by the callable when invoked with specified positional and
           keyword arguments.  If a different type of warning is
           triggered, it will not be handled: depending on the other
           warning filtering rules in effect, it might be silenced, printed
           out, or raised as an exception.

           If called with the callable and arguments omitted, will return a
           context object used like this::

                with self.assertWarns(SomeWarning):
                    do_something()

           An optional keyword argument 'msg' can be provided when assertWarns
           is used as a context object.

           The context manager keeps a reference to the first matching
           warning as the 'warning' attribute; similarly, the 'filename'
           and 'lineno' attributes give you information about the line
           of Python code from which the warning was triggered.
           This allows you to inspect the warning after the assertion::

               with self.assertWarns(SomeWarning) as cm:
                   do_something()
               the_warning = cm.warning
               self.assertEqual(the_warning.some_attribute, 147)
        '''
    ...
    def assertWarnsRegex (self, expected_warning, expected_regex, *args, **kwargs):
      '''Asserts that the message in a triggered warning matches a regexp.
        Basic functioning is similar to assertWarns() with the addition
        that only warnings whose messages also match the regular expression
        are considered successful matches.

        Args:
            expected_warning: Warning class expected to be triggered.
            expected_regex: Regex (re.Pattern object or string) expected
                    to be found in error message.
            args: Function to be called and extra positional args.
            kwargs: Extra kwargs.
            msg: Optional message used in case of failure. Can only be used
                    when assertWarnsRegex is used as a context manager.
        '''
    ...
    def assert_ (*args, **kwargs):
      '''None'''
    ...
    def countTestCases (self):
      '''None'''
    ...
    def debug (self):
      '''Run the test without collecting errors in a TestResult'''
    ...
    def defaultTestResult (self):
      '''None'''
    ...
    def doClassCleanups ():
      '''Execute all class cleanup functions. Normally called for you after
        tearDownClass.'''
    ...
    def doCleanups (self):
      '''Execute all cleanup functions. Normally called for you after
        tearDown.'''
    ...
    def fail (self, msg=None):
      '''Fail immediately, with the given message.'''
    ...
    def failIf (*args, **kwargs):
      '''None'''
    ...
    def failIfAlmostEqual (*args, **kwargs):
      '''None'''
    ...
    def failIfEqual (*args, **kwargs):
      '''None'''
    ...
    def failUnless (*args, **kwargs):
      '''None'''
    ...
    def failUnlessAlmostEqual (*args, **kwargs):
      '''None'''
    ...
    def failUnlessEqual (*args, **kwargs):
      '''None'''
    ...
    def failUnlessRaises (*args, **kwargs):
      '''None'''
    ...
    def failureException (self, *args, **kwargs):
      '''Assertion failed.'''
    ...
    def failureMessageLevel (self, *args, **kwargs):
      '''None'''
    ...
    def id (self):
      '''None'''
    ...
    def ignoreMessage (self, level, context, message):
      '''None'''
    ...
    def longMessage (self, *args, **kwargs):
      '''bool(x) -> bool

Returns True when the argument x is true, False otherwise.
The builtins True and False are the only two instances of the class bool.
The class bool is a subclass of the class int, and cannot be subclassed.'''
    ...
    def maxDiff (self, *args, **kwargs):
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
    def run (self, result=None):
      '''None'''
    ...
    def scopedLocale (l, category=0):
      '''None'''
    ...
    def setUp (self):
      '''None'''
    ...
    def setUpClass ():
      '''Hook method for setting up class fixture before running tests in the class.'''
    ...
    def shortDescription (self):
      '''Returns a one-line description of the test, or None if no
        description has been provided.

        The default implementation of this method returns the first line of
        the specified test method's docstring.
        '''
    ...
    def skipTest (self, reason):
      '''Skip this test.'''
    ...
    def subTest (self, msg=<object object at 0x7fb108120c10>, **params):
      '''Return a context manager that will return the enclosed block
        of code in a subtest identified by the optional message and
        keyword parameters.  A failure in the subtest marks the test
        case as failed but resumes execution at the end of the enclosed
        block, allowing further test code to be executed.
        '''
    ...
    def tearDown (self):
      '''None'''
    ...
    def tearDownClass ():
      '''Hook method for deconstructing the class fixture after running all tests in the class.'''
    ...
    def temporaryDirectory (self):
      '''None'''
    ...
    def test (self):
      '''None'''
    ...
    def testEmptyCommand (self):
      '''None'''
    ...
    def testEnvironmentVariables (self):
      '''None'''
    ...
    def testFrameRangeSubstitutions (self):
      '''None'''
    ...
    def testHash (self):
      '''None'''
    ...
    def testShell (self):
      '''None'''
    ...
    def testSubstitutions (self):
      '''None'''
    ...

def TaskContextVariablesTest (*args):
      '''

'''      
    ...

class TaskContextVariablesTest:
    def _TaskContextVariablesTest__dispatcher (self, frameRange=None):
      '''None'''
    ...
    def _TestCase__nodeHasDescription (self, node):
      '''None'''
    ...
    def _TestCase__undocumentedPlugs (self, node, additionalTerminalPlugTypes=()):
      '''None'''
    ...
    def _addExpectedFailure (self, result, exc_info):
      '''None'''
    ...
    def _addSkip (self, result, test_case, reason):
      '''None'''
    ...
    def _addUnexpectedSuccess (self, result):
      '''None'''
    ...
    def _baseAssertEqual (self, first, second, msg=None):
      '''The default assertEqual implementation, not type specific.'''
    ...
    def _callCleanup (self, function, /, *args, **kwargs):
      '''None'''
    ...
    def _callSetUp (self):
      '''None'''
    ...
    def _callTearDown (self):
      '''None'''
    ...
    def _callTestMethod (self, method):
      '''None'''
    ...
    def _classSetupFailed (self, *args, **kwargs):
      '''bool(x) -> bool

Returns True when the argument x is true, False otherwise.
The builtins True and False are the only two instances of the class bool.
The class bool is a subclass of the class int, and cannot be subclassed.'''
    ...
    def _class_cleanups (self, *args, **kwargs):
      '''Built-in mutable sequence.

If no argument is given, the constructor creates a new empty list.
The argument must be an iterable if specified.'''
    ...
    def _deprecate (original_func):
      '''None'''
    ...
    def _diffThreshold (self, *args, **kwargs):
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
    def _feedErrorsToResult (self, result, errors):
      '''None'''
    ...
    def _formatMessage (self, msg, standardMsg):
      '''Honour the longMessage attribute when generating failure messages.
        If longMessage is False this means:
        * Use only an explicit message if it is provided
        * Otherwise use the standard message for the assert

        If longMessage is True:
        * Use the standard message
        * If an explicit message is provided, plus ' : ' and the explicit message
        '''
    ...
    def _getAssertEqualityFunc (self, first, second):
      '''Get a detailed comparison function for the types of the two args.

        Returns: A callable accepting (first, second, msg=None) that will
        raise a failure exception if first != second with a useful human
        readable error message for those types.
        '''
    ...
    def _truncateMessage (self, message, diff):
      '''None'''
    ...
    def addClassCleanup (function, /, *args, **kwargs):
      '''Same as addCleanup, except the cleanup items are called even if
        setUpClass fails (unlike tearDownClass).'''
    ...
    def addCleanup (self, function, /, *args, **kwargs):
      '''Add a function, with arguments, to be called when the test is
        completed. Functions added are called on a LIFO basis and are
        called after tearDown on test failure or success.

        Cleanup items are called even if setUp fails (unlike tearDown).'''
    ...
    def addTypeEqualityFunc (self, typeobj, function):
      '''Add a type specific assertEqual style function to compare a type.

        This method is for use by TestCase subclasses that need to register
        their own type equality functions to provide nicer error messages.

        Args:
            typeobj: The data type to call this function on when both values
                    are of the same type in assertEqual().
            function: The callable taking two arguments and an optional
                    msg= argument that raises self.failureException with a
                    useful error message when the two arguments are not equal.
        '''
    ...
    def assertAlmostEqual (self, first, second, places=None, msg=None, delta=None):
      '''Fail if the two objects are unequal as determined by their
           difference rounded to the given number of decimal places
           (default 7) and comparing to zero, or by comparing that the
           difference between the two objects is more than the given
           delta.

           Note that decimal places (from zero) are usually not the same
           as significant digits (measured from the most significant digit).

           If the two objects compare equal then they will automatically
           compare almost equal.
        '''
    ...
    def assertAlmostEquals (*args, **kwargs):
      '''None'''
    ...
    def assertCountEqual (self, first, second, msg=None):
      '''Asserts that two iterables have the same elements, the same number of
        times, without regard to order.

            self.assertEqual(Counter(list(first)),
                             Counter(list(second)))

         Example:
            - [0, 1, 1] and [1, 0, 1] compare equal.
            - [0, 0, 1] and [0, 1] compare unequal.

        '''
    ...
    def assertDefaultNamesAreCorrect (self, module, namesToIgnore=()):
      '''None'''
    ...
    def assertDictContainsSubset (self, subset, dictionary, msg=None):
      '''Checks whether dictionary is a superset of subset.'''
    ...
    def assertDictEqual (self, d1, d2, msg=None):
      '''None'''
    ...
    def assertEqual (self, first, second, msg=None):
      '''Fail if the two objects are unequal as determined by the '=='
           operator.
        '''
    ...
    def assertEquals (*args, **kwargs):
      '''None'''
    ...
    def assertFalse (self, expr, msg=None):
      '''Check that the expression is false.'''
    ...
    def assertFloat32Equal (self, value0, value1):
      '''None'''
    ...
    def assertGreater (self, a, b, msg=None):
      '''Just like self.assertTrue(a > b), but with a nicer default message.'''
    ...
    def assertGreaterEqual (self, a, b, msg=None):
      '''Just like self.assertTrue(a >= b), but with a nicer default message.'''
    ...
    def assertHashesValid (self, node, inputsToIgnore=[], outputsToIgnore=[]):
      '''None'''
    ...
    def assertIn (self, member, container, msg=None):
      '''Just like self.assertTrue(a in b), but with a nicer default message.'''
    ...
    def assertIs (self, expr1, expr2, msg=None):
      '''Just like self.assertTrue(a is b), but with a nicer default message.'''
    ...
    def assertIsInstance (self, obj, cls, msg=None):
      '''Same as self.assertTrue(isinstance(obj, cls)), with a nicer
        default message.'''
    ...
    def assertIsNone (self, obj, msg=None):
      '''Same as self.assertTrue(obj is None), with a nicer default message.'''
    ...
    def assertIsNot (self, expr1, expr2, msg=None):
      '''Just like self.assertTrue(a is not b), but with a nicer default message.'''
    ...
    def assertIsNotNone (self, obj, msg=None):
      '''Included for symmetry with assertIsNone.'''
    ...
    def assertLess (self, a, b, msg=None):
      '''Just like self.assertTrue(a < b), but with a nicer default message.'''
    ...
    def assertLessEqual (self, a, b, msg=None):
      '''Just like self.assertTrue(a <= b), but with a nicer default message.'''
    ...
    def assertListEqual (self, list1, list2, msg=None):
      '''A list-specific equality assertion.

        Args:
            list1: The first list to compare.
            list2: The second list to compare.
            msg: Optional message to use on failure instead of a list of
                    differences.

        '''
    ...
    def assertLogs (self, logger=None, level=None):
      '''Fail unless a log message of level *level* or higher is emitted
        on *logger_name* or its children.  If omitted, *level* defaults to
        INFO and *logger* defaults to the root logger.

        This method must be used as a context manager, and will yield
        a recording object with two attributes: `output` and `records`.
        At the end of the context manager, the `output` attribute will
        be a list of the matching formatted log messages and the
        `records` attribute will be a list of the corresponding LogRecord
        objects.

        Example::

            with self.assertLogs('foo', level='INFO') as cm:
                logging.getLogger('foo').info('first message')
                logging.getLogger('foo.bar').error('second message')
            self.assertEqual(cm.output, ['INFO:foo:first message',
                                         'ERROR:foo.bar:second message'])
        '''
    ...
    def assertModuleDoesNotImportUI (self, moduleName):
      '''None'''
    ...
    def assertMultiLineEqual (self, first, second, msg=None):
      '''Assert that two multi-line strings are equal.'''
    ...
    def assertNoLogs (self, logger=None, level=None):
      ''' Fail unless no log messages of level *level* or higher are emitted
        on *logger_name* or its children.

        This method must be used as a context manager.
        '''
    ...
    def assertNodeIsDocumented (self, node, additionalTerminalPlugTypes=()):
      '''None'''
    ...
    def assertNodesAreDocumented (self, module, additionalTerminalPlugTypes=(), nodesToIgnore=None):
      '''None'''
    ...
    def assertNodesConstructWithDefaultValues (self, module, nodesToIgnore=None, plugsToIgnore=None):
      '''None'''
    ...
    def assertNotAlmostEqual (self, first, second, places=None, msg=None, delta=None):
      '''Fail if the two objects are equal as determined by their
           difference rounded to the given number of decimal places
           (default 7) and comparing to zero, or by comparing that the
           difference between the two objects is less than the given delta.

           Note that decimal places (from zero) are usually not the same
           as significant digits (measured from the most significant digit).

           Objects that are equal automatically fail.
        '''
    ...
    def assertNotAlmostEquals (*args, **kwargs):
      '''None'''
    ...
    def assertNotEqual (self, first, second, msg=None):
      '''Fail if the two objects are equal as determined by the '!='
           operator.
        '''
    ...
    def assertNotEquals (*args, **kwargs):
      '''None'''
    ...
    def assertNotIn (self, member, container, msg=None):
      '''Just like self.assertTrue(a not in b), but with a nicer default message.'''
    ...
    def assertNotIsInstance (self, obj, cls, msg=None):
      '''Included for symmetry with assertIsInstance.'''
    ...
    def assertNotRegex (self, text, unexpected_regex, msg=None):
      '''Fail the test if the text matches the regular expression.'''
    ...
    def assertNotRegexpMatches (*args, **kwargs):
      '''None'''
    ...
    def assertRaises (self, expected_exception, *args, **kwargs):
      '''Fail unless an exception of class expected_exception is raised
           by the callable when invoked with specified positional and
           keyword arguments. If a different type of exception is
           raised, it will not be caught, and the test case will be
           deemed to have suffered an error, exactly as for an
           unexpected exception.

           If called with the callable and arguments omitted, will return a
           context object used like this::

                with self.assertRaises(SomeException):
                    do_something()

           An optional keyword argument 'msg' can be provided when assertRaises
           is used as a context object.

           The context manager keeps a reference to the exception as
           the 'exception' attribute. This allows you to inspect the
           exception after the assertion::

               with self.assertRaises(SomeException) as cm:
                   do_something()
               the_exception = cm.exception
               self.assertEqual(the_exception.error_code, 3)
        '''
    ...
    def assertRaisesRegex (self, expected_exception, expected_regex, *args, **kwargs):
      '''Asserts that the message in a raised exception matches a regex.

        Args:
            expected_exception: Exception class expected to be raised.
            expected_regex: Regex (re.Pattern object or string) expected
                    to be found in error message.
            args: Function to be called and extra positional args.
            kwargs: Extra kwargs.
            msg: Optional message used in case of failure. Can only be used
                    when assertRaisesRegex is used as a context manager.
        '''
    ...
    def assertRaisesRegexp (*args, **kwargs):
      '''None'''
    ...
    def assertRegex (self, text, expected_regex, msg=None):
      '''Fail the test unless the text matches the regular expression.'''
    ...
    def assertRegexpMatches (*args, **kwargs):
      '''None'''
    ...
    def assertSequenceEqual (self, seq1, seq2, msg=None, seq_type=None):
      '''An equality assertion for ordered sequences (like lists and tuples).

        For the purposes of this function, a valid ordered sequence type is one
        which can be indexed, has a length, and has an equality operator.

        Args:
            seq1: The first sequence to compare.
            seq2: The second sequence to compare.
            seq_type: The expected datatype of the sequences, or None if no
                    datatype should be enforced.
            msg: Optional message to use on failure instead of a list of
                    differences.
        '''
    ...
    def assertSetEqual (self, set1, set2, msg=None):
      '''A set-specific equality assertion.

        Args:
            set1: The first set to compare.
            set2: The second set to compare.
            msg: Optional message to use on failure instead of a list of
                    differences.

        assertSetEqual uses ducktyping to support different types of sets, and
        is optimized for sets specifically (parameters must support a
        difference method).
        '''
    ...
    def assertTrue (self, expr, msg=None):
      '''Check that the expression is true.'''
    ...
    def assertTupleEqual (self, tuple1, tuple2, msg=None):
      '''A tuple-specific equality assertion.

        Args:
            tuple1: The first tuple to compare.
            tuple2: The second tuple to compare.
            msg: Optional message to use on failure instead of a list of
                    differences.
        '''
    ...
    def assertTypeNamesArePrefixed (self, module, namesToIgnore=()):
      '''None'''
    ...
    def assertWarns (self, expected_warning, *args, **kwargs):
      '''Fail unless a warning of class warnClass is triggered
           by the callable when invoked with specified positional and
           keyword arguments.  If a different type of warning is
           triggered, it will not be handled: depending on the other
           warning filtering rules in effect, it might be silenced, printed
           out, or raised as an exception.

           If called with the callable and arguments omitted, will return a
           context object used like this::

                with self.assertWarns(SomeWarning):
                    do_something()

           An optional keyword argument 'msg' can be provided when assertWarns
           is used as a context object.

           The context manager keeps a reference to the first matching
           warning as the 'warning' attribute; similarly, the 'filename'
           and 'lineno' attributes give you information about the line
           of Python code from which the warning was triggered.
           This allows you to inspect the warning after the assertion::

               with self.assertWarns(SomeWarning) as cm:
                   do_something()
               the_warning = cm.warning
               self.assertEqual(the_warning.some_attribute, 147)
        '''
    ...
    def assertWarnsRegex (self, expected_warning, expected_regex, *args, **kwargs):
      '''Asserts that the message in a triggered warning matches a regexp.
        Basic functioning is similar to assertWarns() with the addition
        that only warnings whose messages also match the regular expression
        are considered successful matches.

        Args:
            expected_warning: Warning class expected to be triggered.
            expected_regex: Regex (re.Pattern object or string) expected
                    to be found in error message.
            args: Function to be called and extra positional args.
            kwargs: Extra kwargs.
            msg: Optional message used in case of failure. Can only be used
                    when assertWarnsRegex is used as a context manager.
        '''
    ...
    def assert_ (*args, **kwargs):
      '''None'''
    ...
    def countTestCases (self):
      '''None'''
    ...
    def debug (self):
      '''Run the test without collecting errors in a TestResult'''
    ...
    def defaultTestResult (self):
      '''None'''
    ...
    def doClassCleanups ():
      '''Execute all class cleanup functions. Normally called for you after
        tearDownClass.'''
    ...
    def doCleanups (self):
      '''Execute all cleanup functions. Normally called for you after
        tearDown.'''
    ...
    def fail (self, msg=None):
      '''Fail immediately, with the given message.'''
    ...
    def failIf (*args, **kwargs):
      '''None'''
    ...
    def failIfAlmostEqual (*args, **kwargs):
      '''None'''
    ...
    def failIfEqual (*args, **kwargs):
      '''None'''
    ...
    def failUnless (*args, **kwargs):
      '''None'''
    ...
    def failUnlessAlmostEqual (*args, **kwargs):
      '''None'''
    ...
    def failUnlessEqual (*args, **kwargs):
      '''None'''
    ...
    def failUnlessRaises (*args, **kwargs):
      '''None'''
    ...
    def failureException (self, *args, **kwargs):
      '''Assertion failed.'''
    ...
    def failureMessageLevel (self, *args, **kwargs):
      '''None'''
    ...
    def id (self):
      '''None'''
    ...
    def ignoreMessage (self, level, context, message):
      '''None'''
    ...
    def longMessage (self, *args, **kwargs):
      '''bool(x) -> bool

Returns True when the argument x is true, False otherwise.
The builtins True and False are the only two instances of the class bool.
The class bool is a subclass of the class int, and cannot be subclassed.'''
    ...
    def maxDiff (self, *args, **kwargs):
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
    def run (self, result=None):
      '''None'''
    ...
    def scopedLocale (l, category=0):
      '''None'''
    ...
    def setUp (self):
      '''None'''
    ...
    def setUpClass ():
      '''Hook method for setting up class fixture before running tests in the class.'''
    ...
    def shortDescription (self):
      '''Returns a one-line description of the test, or None if no
        description has been provided.

        The default implementation of this method returns the first line of
        the specified test method's docstring.
        '''
    ...
    def skipTest (self, reason):
      '''Skip this test.'''
    ...
    def subTest (self, msg=<object object at 0x7fb108120c10>, **params):
      '''Return a context manager that will return the enclosed block
        of code in a subtest identified by the optional message and
        keyword parameters.  A failure in the subtest marks the test
        case as failed but resumes execution at the end of the enclosed
        block, allowing further test code to be executed.
        '''
    ...
    def tearDown (self):
      '''None'''
    ...
    def tearDownClass ():
      '''Hook method for deconstructing the class fixture after running all tests in the class.'''
    ...
    def temporaryDirectory (self):
      '''None'''
    ...
    def test (self):
      '''None'''
    ...
    def testBackgroundDispatch (self):
      '''None'''
    ...
    def testDirectCycles (self):
      '''None'''
    ...
    def testDisabledVariable (self):
      '''None'''
    ...
    def testStringSubstitutions (self):
      '''None'''
    ...

def TaskListTest (*args):
      '''

'''      
    ...

class TaskListTest:
    def _TestCase__nodeHasDescription (self, node):
      '''None'''
    ...
    def _TestCase__undocumentedPlugs (self, node, additionalTerminalPlugTypes=()):
      '''None'''
    ...
    def _addExpectedFailure (self, result, exc_info):
      '''None'''
    ...
    def _addSkip (self, result, test_case, reason):
      '''None'''
    ...
    def _addUnexpectedSuccess (self, result):
      '''None'''
    ...
    def _baseAssertEqual (self, first, second, msg=None):
      '''The default assertEqual implementation, not type specific.'''
    ...
    def _callCleanup (self, function, /, *args, **kwargs):
      '''None'''
    ...
    def _callSetUp (self):
      '''None'''
    ...
    def _callTearDown (self):
      '''None'''
    ...
    def _callTestMethod (self, method):
      '''None'''
    ...
    def _classSetupFailed (self, *args, **kwargs):
      '''bool(x) -> bool

Returns True when the argument x is true, False otherwise.
The builtins True and False are the only two instances of the class bool.
The class bool is a subclass of the class int, and cannot be subclassed.'''
    ...
    def _class_cleanups (self, *args, **kwargs):
      '''Built-in mutable sequence.

If no argument is given, the constructor creates a new empty list.
The argument must be an iterable if specified.'''
    ...
    def _deprecate (original_func):
      '''None'''
    ...
    def _diffThreshold (self, *args, **kwargs):
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
    def _feedErrorsToResult (self, result, errors):
      '''None'''
    ...
    def _formatMessage (self, msg, standardMsg):
      '''Honour the longMessage attribute when generating failure messages.
        If longMessage is False this means:
        * Use only an explicit message if it is provided
        * Otherwise use the standard message for the assert

        If longMessage is True:
        * Use the standard message
        * If an explicit message is provided, plus ' : ' and the explicit message
        '''
    ...
    def _getAssertEqualityFunc (self, first, second):
      '''Get a detailed comparison function for the types of the two args.

        Returns: A callable accepting (first, second, msg=None) that will
        raise a failure exception if first != second with a useful human
        readable error message for those types.
        '''
    ...
    def _truncateMessage (self, message, diff):
      '''None'''
    ...
    def addClassCleanup (function, /, *args, **kwargs):
      '''Same as addCleanup, except the cleanup items are called even if
        setUpClass fails (unlike tearDownClass).'''
    ...
    def addCleanup (self, function, /, *args, **kwargs):
      '''Add a function, with arguments, to be called when the test is
        completed. Functions added are called on a LIFO basis and are
        called after tearDown on test failure or success.

        Cleanup items are called even if setUp fails (unlike tearDown).'''
    ...
    def addTypeEqualityFunc (self, typeobj, function):
      '''Add a type specific assertEqual style function to compare a type.

        This method is for use by TestCase subclasses that need to register
        their own type equality functions to provide nicer error messages.

        Args:
            typeobj: The data type to call this function on when both values
                    are of the same type in assertEqual().
            function: The callable taking two arguments and an optional
                    msg= argument that raises self.failureException with a
                    useful error message when the two arguments are not equal.
        '''
    ...
    def assertAlmostEqual (self, first, second, places=None, msg=None, delta=None):
      '''Fail if the two objects are unequal as determined by their
           difference rounded to the given number of decimal places
           (default 7) and comparing to zero, or by comparing that the
           difference between the two objects is more than the given
           delta.

           Note that decimal places (from zero) are usually not the same
           as significant digits (measured from the most significant digit).

           If the two objects compare equal then they will automatically
           compare almost equal.
        '''
    ...
    def assertAlmostEquals (*args, **kwargs):
      '''None'''
    ...
    def assertCountEqual (self, first, second, msg=None):
      '''Asserts that two iterables have the same elements, the same number of
        times, without regard to order.

            self.assertEqual(Counter(list(first)),
                             Counter(list(second)))

         Example:
            - [0, 1, 1] and [1, 0, 1] compare equal.
            - [0, 0, 1] and [0, 1] compare unequal.

        '''
    ...
    def assertDefaultNamesAreCorrect (self, module, namesToIgnore=()):
      '''None'''
    ...
    def assertDictContainsSubset (self, subset, dictionary, msg=None):
      '''Checks whether dictionary is a superset of subset.'''
    ...
    def assertDictEqual (self, d1, d2, msg=None):
      '''None'''
    ...
    def assertEqual (self, first, second, msg=None):
      '''Fail if the two objects are unequal as determined by the '=='
           operator.
        '''
    ...
    def assertEquals (*args, **kwargs):
      '''None'''
    ...
    def assertFalse (self, expr, msg=None):
      '''Check that the expression is false.'''
    ...
    def assertFloat32Equal (self, value0, value1):
      '''None'''
    ...
    def assertGreater (self, a, b, msg=None):
      '''Just like self.assertTrue(a > b), but with a nicer default message.'''
    ...
    def assertGreaterEqual (self, a, b, msg=None):
      '''Just like self.assertTrue(a >= b), but with a nicer default message.'''
    ...
    def assertHashesValid (self, node, inputsToIgnore=[], outputsToIgnore=[]):
      '''None'''
    ...
    def assertIn (self, member, container, msg=None):
      '''Just like self.assertTrue(a in b), but with a nicer default message.'''
    ...
    def assertIs (self, expr1, expr2, msg=None):
      '''Just like self.assertTrue(a is b), but with a nicer default message.'''
    ...
    def assertIsInstance (self, obj, cls, msg=None):
      '''Same as self.assertTrue(isinstance(obj, cls)), with a nicer
        default message.'''
    ...
    def assertIsNone (self, obj, msg=None):
      '''Same as self.assertTrue(obj is None), with a nicer default message.'''
    ...
    def assertIsNot (self, expr1, expr2, msg=None):
      '''Just like self.assertTrue(a is not b), but with a nicer default message.'''
    ...
    def assertIsNotNone (self, obj, msg=None):
      '''Included for symmetry with assertIsNone.'''
    ...
    def assertLess (self, a, b, msg=None):
      '''Just like self.assertTrue(a < b), but with a nicer default message.'''
    ...
    def assertLessEqual (self, a, b, msg=None):
      '''Just like self.assertTrue(a <= b), but with a nicer default message.'''
    ...
    def assertListEqual (self, list1, list2, msg=None):
      '''A list-specific equality assertion.

        Args:
            list1: The first list to compare.
            list2: The second list to compare.
            msg: Optional message to use on failure instead of a list of
                    differences.

        '''
    ...
    def assertLogs (self, logger=None, level=None):
      '''Fail unless a log message of level *level* or higher is emitted
        on *logger_name* or its children.  If omitted, *level* defaults to
        INFO and *logger* defaults to the root logger.

        This method must be used as a context manager, and will yield
        a recording object with two attributes: `output` and `records`.
        At the end of the context manager, the `output` attribute will
        be a list of the matching formatted log messages and the
        `records` attribute will be a list of the corresponding LogRecord
        objects.

        Example::

            with self.assertLogs('foo', level='INFO') as cm:
                logging.getLogger('foo').info('first message')
                logging.getLogger('foo.bar').error('second message')
            self.assertEqual(cm.output, ['INFO:foo:first message',
                                         'ERROR:foo.bar:second message'])
        '''
    ...
    def assertModuleDoesNotImportUI (self, moduleName):
      '''None'''
    ...
    def assertMultiLineEqual (self, first, second, msg=None):
      '''Assert that two multi-line strings are equal.'''
    ...
    def assertNoLogs (self, logger=None, level=None):
      ''' Fail unless no log messages of level *level* or higher are emitted
        on *logger_name* or its children.

        This method must be used as a context manager.
        '''
    ...
    def assertNodeIsDocumented (self, node, additionalTerminalPlugTypes=()):
      '''None'''
    ...
    def assertNodesAreDocumented (self, module, additionalTerminalPlugTypes=(), nodesToIgnore=None):
      '''None'''
    ...
    def assertNodesConstructWithDefaultValues (self, module, nodesToIgnore=None, plugsToIgnore=None):
      '''None'''
    ...
    def assertNotAlmostEqual (self, first, second, places=None, msg=None, delta=None):
      '''Fail if the two objects are equal as determined by their
           difference rounded to the given number of decimal places
           (default 7) and comparing to zero, or by comparing that the
           difference between the two objects is less than the given delta.

           Note that decimal places (from zero) are usually not the same
           as significant digits (measured from the most significant digit).

           Objects that are equal automatically fail.
        '''
    ...
    def assertNotAlmostEquals (*args, **kwargs):
      '''None'''
    ...
    def assertNotEqual (self, first, second, msg=None):
      '''Fail if the two objects are equal as determined by the '!='
           operator.
        '''
    ...
    def assertNotEquals (*args, **kwargs):
      '''None'''
    ...
    def assertNotIn (self, member, container, msg=None):
      '''Just like self.assertTrue(a not in b), but with a nicer default message.'''
    ...
    def assertNotIsInstance (self, obj, cls, msg=None):
      '''Included for symmetry with assertIsInstance.'''
    ...
    def assertNotRegex (self, text, unexpected_regex, msg=None):
      '''Fail the test if the text matches the regular expression.'''
    ...
    def assertNotRegexpMatches (*args, **kwargs):
      '''None'''
    ...
    def assertRaises (self, expected_exception, *args, **kwargs):
      '''Fail unless an exception of class expected_exception is raised
           by the callable when invoked with specified positional and
           keyword arguments. If a different type of exception is
           raised, it will not be caught, and the test case will be
           deemed to have suffered an error, exactly as for an
           unexpected exception.

           If called with the callable and arguments omitted, will return a
           context object used like this::

                with self.assertRaises(SomeException):
                    do_something()

           An optional keyword argument 'msg' can be provided when assertRaises
           is used as a context object.

           The context manager keeps a reference to the exception as
           the 'exception' attribute. This allows you to inspect the
           exception after the assertion::

               with self.assertRaises(SomeException) as cm:
                   do_something()
               the_exception = cm.exception
               self.assertEqual(the_exception.error_code, 3)
        '''
    ...
    def assertRaisesRegex (self, expected_exception, expected_regex, *args, **kwargs):
      '''Asserts that the message in a raised exception matches a regex.

        Args:
            expected_exception: Exception class expected to be raised.
            expected_regex: Regex (re.Pattern object or string) expected
                    to be found in error message.
            args: Function to be called and extra positional args.
            kwargs: Extra kwargs.
            msg: Optional message used in case of failure. Can only be used
                    when assertRaisesRegex is used as a context manager.
        '''
    ...
    def assertRaisesRegexp (*args, **kwargs):
      '''None'''
    ...
    def assertRegex (self, text, expected_regex, msg=None):
      '''Fail the test unless the text matches the regular expression.'''
    ...
    def assertRegexpMatches (*args, **kwargs):
      '''None'''
    ...
    def assertSequenceEqual (self, seq1, seq2, msg=None, seq_type=None):
      '''An equality assertion for ordered sequences (like lists and tuples).

        For the purposes of this function, a valid ordered sequence type is one
        which can be indexed, has a length, and has an equality operator.

        Args:
            seq1: The first sequence to compare.
            seq2: The second sequence to compare.
            seq_type: The expected datatype of the sequences, or None if no
                    datatype should be enforced.
            msg: Optional message to use on failure instead of a list of
                    differences.
        '''
    ...
    def assertSetEqual (self, set1, set2, msg=None):
      '''A set-specific equality assertion.

        Args:
            set1: The first set to compare.
            set2: The second set to compare.
            msg: Optional message to use on failure instead of a list of
                    differences.

        assertSetEqual uses ducktyping to support different types of sets, and
        is optimized for sets specifically (parameters must support a
        difference method).
        '''
    ...
    def assertTrue (self, expr, msg=None):
      '''Check that the expression is true.'''
    ...
    def assertTupleEqual (self, tuple1, tuple2, msg=None):
      '''A tuple-specific equality assertion.

        Args:
            tuple1: The first tuple to compare.
            tuple2: The second tuple to compare.
            msg: Optional message to use on failure instead of a list of
                    differences.
        '''
    ...
    def assertTypeNamesArePrefixed (self, module, namesToIgnore=()):
      '''None'''
    ...
    def assertWarns (self, expected_warning, *args, **kwargs):
      '''Fail unless a warning of class warnClass is triggered
           by the callable when invoked with specified positional and
           keyword arguments.  If a different type of warning is
           triggered, it will not be handled: depending on the other
           warning filtering rules in effect, it might be silenced, printed
           out, or raised as an exception.

           If called with the callable and arguments omitted, will return a
           context object used like this::

                with self.assertWarns(SomeWarning):
                    do_something()

           An optional keyword argument 'msg' can be provided when assertWarns
           is used as a context object.

           The context manager keeps a reference to the first matching
           warning as the 'warning' attribute; similarly, the 'filename'
           and 'lineno' attributes give you information about the line
           of Python code from which the warning was triggered.
           This allows you to inspect the warning after the assertion::

               with self.assertWarns(SomeWarning) as cm:
                   do_something()
               the_warning = cm.warning
               self.assertEqual(the_warning.some_attribute, 147)
        '''
    ...
    def assertWarnsRegex (self, expected_warning, expected_regex, *args, **kwargs):
      '''Asserts that the message in a triggered warning matches a regexp.
        Basic functioning is similar to assertWarns() with the addition
        that only warnings whose messages also match the regular expression
        are considered successful matches.

        Args:
            expected_warning: Warning class expected to be triggered.
            expected_regex: Regex (re.Pattern object or string) expected
                    to be found in error message.
            args: Function to be called and extra positional args.
            kwargs: Extra kwargs.
            msg: Optional message used in case of failure. Can only be used
                    when assertWarnsRegex is used as a context manager.
        '''
    ...
    def assert_ (*args, **kwargs):
      '''None'''
    ...
    def countTestCases (self):
      '''None'''
    ...
    def debug (self):
      '''Run the test without collecting errors in a TestResult'''
    ...
    def defaultTestResult (self):
      '''None'''
    ...
    def doClassCleanups ():
      '''Execute all class cleanup functions. Normally called for you after
        tearDownClass.'''
    ...
    def doCleanups (self):
      '''Execute all cleanup functions. Normally called for you after
        tearDown.'''
    ...
    def fail (self, msg=None):
      '''Fail immediately, with the given message.'''
    ...
    def failIf (*args, **kwargs):
      '''None'''
    ...
    def failIfAlmostEqual (*args, **kwargs):
      '''None'''
    ...
    def failIfEqual (*args, **kwargs):
      '''None'''
    ...
    def failUnless (*args, **kwargs):
      '''None'''
    ...
    def failUnlessAlmostEqual (*args, **kwargs):
      '''None'''
    ...
    def failUnlessEqual (*args, **kwargs):
      '''None'''
    ...
    def failUnlessRaises (*args, **kwargs):
      '''None'''
    ...
    def failureException (self, *args, **kwargs):
      '''Assertion failed.'''
    ...
    def failureMessageLevel (self, *args, **kwargs):
      '''None'''
    ...
    def id (self):
      '''None'''
    ...
    def ignoreMessage (self, level, context, message):
      '''None'''
    ...
    def longMessage (self, *args, **kwargs):
      '''bool(x) -> bool

Returns True when the argument x is true, False otherwise.
The builtins True and False are the only two instances of the class bool.
The class bool is a subclass of the class int, and cannot be subclassed.'''
    ...
    def maxDiff (self, *args, **kwargs):
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
    def run (self, result=None):
      '''None'''
    ...
    def scopedLocale (l, category=0):
      '''None'''
    ...
    def setUp (self):
      '''None'''
    ...
    def setUpClass ():
      '''Hook method for setting up class fixture before running tests in the class.'''
    ...
    def shortDescription (self):
      '''Returns a one-line description of the test, or None if no
        description has been provided.

        The default implementation of this method returns the first line of
        the specified test method's docstring.
        '''
    ...
    def skipTest (self, reason):
      '''Skip this test.'''
    ...
    def subTest (self, msg=<object object at 0x7fb108120c10>, **params):
      '''Return a context manager that will return the enclosed block
        of code in a subtest identified by the optional message and
        keyword parameters.  A failure in the subtest marks the test
        case as failed but resumes execution at the end of the enclosed
        block, allowing further test code to be executed.
        '''
    ...
    def tearDown (self):
      '''None'''
    ...
    def tearDownClass ():
      '''Hook method for deconstructing the class fixture after running all tests in the class.'''
    ...
    def temporaryDirectory (self):
      '''None'''
    ...
    def test (self):
      '''None'''
    ...
    def testSequenceExecution (self):
      '''None'''
    ...

def TaskNodeTest (*args):
      '''

'''      
    ...

class TaskNodeTest:
    def _TestCase__nodeHasDescription (self, node):
      '''None'''
    ...
    def _TestCase__undocumentedPlugs (self, node, additionalTerminalPlugTypes=()):
      '''None'''
    ...
    def _addExpectedFailure (self, result, exc_info):
      '''None'''
    ...
    def _addSkip (self, result, test_case, reason):
      '''None'''
    ...
    def _addUnexpectedSuccess (self, result):
      '''None'''
    ...
    def _baseAssertEqual (self, first, second, msg=None):
      '''The default assertEqual implementation, not type specific.'''
    ...
    def _callCleanup (self, function, /, *args, **kwargs):
      '''None'''
    ...
    def _callSetUp (self):
      '''None'''
    ...
    def _callTearDown (self):
      '''None'''
    ...
    def _callTestMethod (self, method):
      '''None'''
    ...
    def _classSetupFailed (self, *args, **kwargs):
      '''bool(x) -> bool

Returns True when the argument x is true, False otherwise.
The builtins True and False are the only two instances of the class bool.
The class bool is a subclass of the class int, and cannot be subclassed.'''
    ...
    def _class_cleanups (self, *args, **kwargs):
      '''Built-in mutable sequence.

If no argument is given, the constructor creates a new empty list.
The argument must be an iterable if specified.'''
    ...
    def _deprecate (original_func):
      '''None'''
    ...
    def _diffThreshold (self, *args, **kwargs):
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
    def _feedErrorsToResult (self, result, errors):
      '''None'''
    ...
    def _formatMessage (self, msg, standardMsg):
      '''Honour the longMessage attribute when generating failure messages.
        If longMessage is False this means:
        * Use only an explicit message if it is provided
        * Otherwise use the standard message for the assert

        If longMessage is True:
        * Use the standard message
        * If an explicit message is provided, plus ' : ' and the explicit message
        '''
    ...
    def _getAssertEqualityFunc (self, first, second):
      '''Get a detailed comparison function for the types of the two args.

        Returns: A callable accepting (first, second, msg=None) that will
        raise a failure exception if first != second with a useful human
        readable error message for those types.
        '''
    ...
    def _truncateMessage (self, message, diff):
      '''None'''
    ...
    def addClassCleanup (function, /, *args, **kwargs):
      '''Same as addCleanup, except the cleanup items are called even if
        setUpClass fails (unlike tearDownClass).'''
    ...
    def addCleanup (self, function, /, *args, **kwargs):
      '''Add a function, with arguments, to be called when the test is
        completed. Functions added are called on a LIFO basis and are
        called after tearDown on test failure or success.

        Cleanup items are called even if setUp fails (unlike tearDown).'''
    ...
    def addTypeEqualityFunc (self, typeobj, function):
      '''Add a type specific assertEqual style function to compare a type.

        This method is for use by TestCase subclasses that need to register
        their own type equality functions to provide nicer error messages.

        Args:
            typeobj: The data type to call this function on when both values
                    are of the same type in assertEqual().
            function: The callable taking two arguments and an optional
                    msg= argument that raises self.failureException with a
                    useful error message when the two arguments are not equal.
        '''
    ...
    def assertAlmostEqual (self, first, second, places=None, msg=None, delta=None):
      '''Fail if the two objects are unequal as determined by their
           difference rounded to the given number of decimal places
           (default 7) and comparing to zero, or by comparing that the
           difference between the two objects is more than the given
           delta.

           Note that decimal places (from zero) are usually not the same
           as significant digits (measured from the most significant digit).

           If the two objects compare equal then they will automatically
           compare almost equal.
        '''
    ...
    def assertAlmostEquals (*args, **kwargs):
      '''None'''
    ...
    def assertCountEqual (self, first, second, msg=None):
      '''Asserts that two iterables have the same elements, the same number of
        times, without regard to order.

            self.assertEqual(Counter(list(first)),
                             Counter(list(second)))

         Example:
            - [0, 1, 1] and [1, 0, 1] compare equal.
            - [0, 0, 1] and [0, 1] compare unequal.

        '''
    ...
    def assertDefaultNamesAreCorrect (self, module, namesToIgnore=()):
      '''None'''
    ...
    def assertDictContainsSubset (self, subset, dictionary, msg=None):
      '''Checks whether dictionary is a superset of subset.'''
    ...
    def assertDictEqual (self, d1, d2, msg=None):
      '''None'''
    ...
    def assertEqual (self, first, second, msg=None):
      '''Fail if the two objects are unequal as determined by the '=='
           operator.
        '''
    ...
    def assertEquals (*args, **kwargs):
      '''None'''
    ...
    def assertFalse (self, expr, msg=None):
      '''Check that the expression is false.'''
    ...
    def assertFloat32Equal (self, value0, value1):
      '''None'''
    ...
    def assertGreater (self, a, b, msg=None):
      '''Just like self.assertTrue(a > b), but with a nicer default message.'''
    ...
    def assertGreaterEqual (self, a, b, msg=None):
      '''Just like self.assertTrue(a >= b), but with a nicer default message.'''
    ...
    def assertHashesValid (self, node, inputsToIgnore=[], outputsToIgnore=[]):
      '''None'''
    ...
    def assertIn (self, member, container, msg=None):
      '''Just like self.assertTrue(a in b), but with a nicer default message.'''
    ...
    def assertIs (self, expr1, expr2, msg=None):
      '''Just like self.assertTrue(a is b), but with a nicer default message.'''
    ...
    def assertIsInstance (self, obj, cls, msg=None):
      '''Same as self.assertTrue(isinstance(obj, cls)), with a nicer
        default message.'''
    ...
    def assertIsNone (self, obj, msg=None):
      '''Same as self.assertTrue(obj is None), with a nicer default message.'''
    ...
    def assertIsNot (self, expr1, expr2, msg=None):
      '''Just like self.assertTrue(a is not b), but with a nicer default message.'''
    ...
    def assertIsNotNone (self, obj, msg=None):
      '''Included for symmetry with assertIsNone.'''
    ...
    def assertLess (self, a, b, msg=None):
      '''Just like self.assertTrue(a < b), but with a nicer default message.'''
    ...
    def assertLessEqual (self, a, b, msg=None):
      '''Just like self.assertTrue(a <= b), but with a nicer default message.'''
    ...
    def assertListEqual (self, list1, list2, msg=None):
      '''A list-specific equality assertion.

        Args:
            list1: The first list to compare.
            list2: The second list to compare.
            msg: Optional message to use on failure instead of a list of
                    differences.

        '''
    ...
    def assertLogs (self, logger=None, level=None):
      '''Fail unless a log message of level *level* or higher is emitted
        on *logger_name* or its children.  If omitted, *level* defaults to
        INFO and *logger* defaults to the root logger.

        This method must be used as a context manager, and will yield
        a recording object with two attributes: `output` and `records`.
        At the end of the context manager, the `output` attribute will
        be a list of the matching formatted log messages and the
        `records` attribute will be a list of the corresponding LogRecord
        objects.

        Example::

            with self.assertLogs('foo', level='INFO') as cm:
                logging.getLogger('foo').info('first message')
                logging.getLogger('foo.bar').error('second message')
            self.assertEqual(cm.output, ['INFO:foo:first message',
                                         'ERROR:foo.bar:second message'])
        '''
    ...
    def assertModuleDoesNotImportUI (self, moduleName):
      '''None'''
    ...
    def assertMultiLineEqual (self, first, second, msg=None):
      '''Assert that two multi-line strings are equal.'''
    ...
    def assertNoLogs (self, logger=None, level=None):
      ''' Fail unless no log messages of level *level* or higher are emitted
        on *logger_name* or its children.

        This method must be used as a context manager.
        '''
    ...
    def assertNodeIsDocumented (self, node, additionalTerminalPlugTypes=()):
      '''None'''
    ...
    def assertNodesAreDocumented (self, module, additionalTerminalPlugTypes=(), nodesToIgnore=None):
      '''None'''
    ...
    def assertNodesConstructWithDefaultValues (self, module, nodesToIgnore=None, plugsToIgnore=None):
      '''None'''
    ...
    def assertNotAlmostEqual (self, first, second, places=None, msg=None, delta=None):
      '''Fail if the two objects are equal as determined by their
           difference rounded to the given number of decimal places
           (default 7) and comparing to zero, or by comparing that the
           difference between the two objects is less than the given delta.

           Note that decimal places (from zero) are usually not the same
           as significant digits (measured from the most significant digit).

           Objects that are equal automatically fail.
        '''
    ...
    def assertNotAlmostEquals (*args, **kwargs):
      '''None'''
    ...
    def assertNotEqual (self, first, second, msg=None):
      '''Fail if the two objects are equal as determined by the '!='
           operator.
        '''
    ...
    def assertNotEquals (*args, **kwargs):
      '''None'''
    ...
    def assertNotIn (self, member, container, msg=None):
      '''Just like self.assertTrue(a not in b), but with a nicer default message.'''
    ...
    def assertNotIsInstance (self, obj, cls, msg=None):
      '''Included for symmetry with assertIsInstance.'''
    ...
    def assertNotRegex (self, text, unexpected_regex, msg=None):
      '''Fail the test if the text matches the regular expression.'''
    ...
    def assertNotRegexpMatches (*args, **kwargs):
      '''None'''
    ...
    def assertRaises (self, expected_exception, *args, **kwargs):
      '''Fail unless an exception of class expected_exception is raised
           by the callable when invoked with specified positional and
           keyword arguments. If a different type of exception is
           raised, it will not be caught, and the test case will be
           deemed to have suffered an error, exactly as for an
           unexpected exception.

           If called with the callable and arguments omitted, will return a
           context object used like this::

                with self.assertRaises(SomeException):
                    do_something()

           An optional keyword argument 'msg' can be provided when assertRaises
           is used as a context object.

           The context manager keeps a reference to the exception as
           the 'exception' attribute. This allows you to inspect the
           exception after the assertion::

               with self.assertRaises(SomeException) as cm:
                   do_something()
               the_exception = cm.exception
               self.assertEqual(the_exception.error_code, 3)
        '''
    ...
    def assertRaisesRegex (self, expected_exception, expected_regex, *args, **kwargs):
      '''Asserts that the message in a raised exception matches a regex.

        Args:
            expected_exception: Exception class expected to be raised.
            expected_regex: Regex (re.Pattern object or string) expected
                    to be found in error message.
            args: Function to be called and extra positional args.
            kwargs: Extra kwargs.
            msg: Optional message used in case of failure. Can only be used
                    when assertRaisesRegex is used as a context manager.
        '''
    ...
    def assertRaisesRegexp (*args, **kwargs):
      '''None'''
    ...
    def assertRegex (self, text, expected_regex, msg=None):
      '''Fail the test unless the text matches the regular expression.'''
    ...
    def assertRegexpMatches (*args, **kwargs):
      '''None'''
    ...
    def assertSequenceEqual (self, seq1, seq2, msg=None, seq_type=None):
      '''An equality assertion for ordered sequences (like lists and tuples).

        For the purposes of this function, a valid ordered sequence type is one
        which can be indexed, has a length, and has an equality operator.

        Args:
            seq1: The first sequence to compare.
            seq2: The second sequence to compare.
            seq_type: The expected datatype of the sequences, or None if no
                    datatype should be enforced.
            msg: Optional message to use on failure instead of a list of
                    differences.
        '''
    ...
    def assertSetEqual (self, set1, set2, msg=None):
      '''A set-specific equality assertion.

        Args:
            set1: The first set to compare.
            set2: The second set to compare.
            msg: Optional message to use on failure instead of a list of
                    differences.

        assertSetEqual uses ducktyping to support different types of sets, and
        is optimized for sets specifically (parameters must support a
        difference method).
        '''
    ...
    def assertTrue (self, expr, msg=None):
      '''Check that the expression is true.'''
    ...
    def assertTupleEqual (self, tuple1, tuple2, msg=None):
      '''A tuple-specific equality assertion.

        Args:
            tuple1: The first tuple to compare.
            tuple2: The second tuple to compare.
            msg: Optional message to use on failure instead of a list of
                    differences.
        '''
    ...
    def assertTypeNamesArePrefixed (self, module, namesToIgnore=()):
      '''None'''
    ...
    def assertWarns (self, expected_warning, *args, **kwargs):
      '''Fail unless a warning of class warnClass is triggered
           by the callable when invoked with specified positional and
           keyword arguments.  If a different type of warning is
           triggered, it will not be handled: depending on the other
           warning filtering rules in effect, it might be silenced, printed
           out, or raised as an exception.

           If called with the callable and arguments omitted, will return a
           context object used like this::

                with self.assertWarns(SomeWarning):
                    do_something()

           An optional keyword argument 'msg' can be provided when assertWarns
           is used as a context object.

           The context manager keeps a reference to the first matching
           warning as the 'warning' attribute; similarly, the 'filename'
           and 'lineno' attributes give you information about the line
           of Python code from which the warning was triggered.
           This allows you to inspect the warning after the assertion::

               with self.assertWarns(SomeWarning) as cm:
                   do_something()
               the_warning = cm.warning
               self.assertEqual(the_warning.some_attribute, 147)
        '''
    ...
    def assertWarnsRegex (self, expected_warning, expected_regex, *args, **kwargs):
      '''Asserts that the message in a triggered warning matches a regexp.
        Basic functioning is similar to assertWarns() with the addition
        that only warnings whose messages also match the regular expression
        are considered successful matches.

        Args:
            expected_warning: Warning class expected to be triggered.
            expected_regex: Regex (re.Pattern object or string) expected
                    to be found in error message.
            args: Function to be called and extra positional args.
            kwargs: Extra kwargs.
            msg: Optional message used in case of failure. Can only be used
                    when assertWarnsRegex is used as a context manager.
        '''
    ...
    def assert_ (*args, **kwargs):
      '''None'''
    ...
    def countTestCases (self):
      '''None'''
    ...
    def debug (self):
      '''Run the test without collecting errors in a TestResult'''
    ...
    def defaultTestResult (self):
      '''None'''
    ...
    def doClassCleanups ():
      '''Execute all class cleanup functions. Normally called for you after
        tearDownClass.'''
    ...
    def doCleanups (self):
      '''Execute all cleanup functions. Normally called for you after
        tearDown.'''
    ...
    def fail (self, msg=None):
      '''Fail immediately, with the given message.'''
    ...
    def failIf (*args, **kwargs):
      '''None'''
    ...
    def failIfAlmostEqual (*args, **kwargs):
      '''None'''
    ...
    def failIfEqual (*args, **kwargs):
      '''None'''
    ...
    def failUnless (*args, **kwargs):
      '''None'''
    ...
    def failUnlessAlmostEqual (*args, **kwargs):
      '''None'''
    ...
    def failUnlessEqual (*args, **kwargs):
      '''None'''
    ...
    def failUnlessRaises (*args, **kwargs):
      '''None'''
    ...
    def failureException (self, *args, **kwargs):
      '''Assertion failed.'''
    ...
    def failureMessageLevel (self, *args, **kwargs):
      '''None'''
    ...
    def id (self):
      '''None'''
    ...
    def ignoreMessage (self, level, context, message):
      '''None'''
    ...
    def longMessage (self, *args, **kwargs):
      '''bool(x) -> bool

Returns True when the argument x is true, False otherwise.
The builtins True and False are the only two instances of the class bool.
The class bool is a subclass of the class int, and cannot be subclassed.'''
    ...
    def maxDiff (self, *args, **kwargs):
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
    def run (self, result=None):
      '''None'''
    ...
    def scopedLocale (l, category=0):
      '''None'''
    ...
    def setUp (self):
      '''None'''
    ...
    def setUpClass ():
      '''Hook method for setting up class fixture before running tests in the class.'''
    ...
    def shortDescription (self):
      '''Returns a one-line description of the test, or None if no
        description has been provided.

        The default implementation of this method returns the first line of
        the specified test method's docstring.
        '''
    ...
    def skipTest (self, reason):
      '''Skip this test.'''
    ...
    def subTest (self, msg=<object object at 0x7fb108120c10>, **params):
      '''Return a context manager that will return the enclosed block
        of code in a subtest identified by the optional message and
        keyword parameters.  A failure in the subtest marks the test
        case as failed but resumes execution at the end of the enclosed
        block, allowing further test code to be executed.
        '''
    ...
    def tearDown (self):
      '''None'''
    ...
    def tearDownClass ():
      '''Hook method for deconstructing the class fixture after running all tests in the class.'''
    ...
    def temporaryDirectory (self):
      '''None'''
    ...
    def testDefaultNames (self):
      '''None'''
    ...
    def testDependencyNode (self):
      '''None'''
    ...
    def testDerivedClasses (self):
      '''None'''
    ...
    def testDirtyPropagation (self):
      '''None'''
    ...
    def testErrorSignal (self):
      '''None'''
    ...
    def testExecute (self):
      '''None'''
    ...
    def testExecuteSequence (self):
      '''None'''
    ...
    def testExecuteSequenceWithIterable (self):
      '''None'''
    ...
    def testHash (self):
      '''None'''
    ...
    def testInputAcceptanceFromBoxes (self):
      '''None'''
    ...
    def testInputAcceptanceFromDots (self):
      '''None'''
    ...
    def testInputAcceptanceInsideBoxes (self):
      '''None'''
    ...
    def testNodesConstructWithDefaultValues (self):
      '''None'''
    ...
    def testOverrideAffectsTask (self):
      '''None'''
    ...
    def testPostTasks (self):
      '''None'''
    ...
    def testPreTasks (self):
      '''None'''
    ...
    def testReferencePromotedPreTasksArrayPlug (self):
      '''None'''
    ...
    def testReferencePromotedPreTasksPlug (self):
      '''None'''
    ...
    def testRequiresSequenceExecution (self):
      '''None'''
    ...
    def testSubclassAndBuildInternalNetwork (self):
      '''None'''
    ...
    def testTaskComparison (self):
      '''None'''
    ...
    def testTaskConstructors (self):
      '''None'''
    ...
    def testTypeNamePrefixes (self):
      '''None'''
    ...

def TaskPlugTest (*args):
      '''

'''      
    ...

class TaskPlugTest:
    def _TestCase__nodeHasDescription (self, node):
      '''None'''
    ...
    def _TestCase__undocumentedPlugs (self, node, additionalTerminalPlugTypes=()):
      '''None'''
    ...
    def _addExpectedFailure (self, result, exc_info):
      '''None'''
    ...
    def _addSkip (self, result, test_case, reason):
      '''None'''
    ...
    def _addUnexpectedSuccess (self, result):
      '''None'''
    ...
    def _baseAssertEqual (self, first, second, msg=None):
      '''The default assertEqual implementation, not type specific.'''
    ...
    def _callCleanup (self, function, /, *args, **kwargs):
      '''None'''
    ...
    def _callSetUp (self):
      '''None'''
    ...
    def _callTearDown (self):
      '''None'''
    ...
    def _callTestMethod (self, method):
      '''None'''
    ...
    def _classSetupFailed (self, *args, **kwargs):
      '''bool(x) -> bool

Returns True when the argument x is true, False otherwise.
The builtins True and False are the only two instances of the class bool.
The class bool is a subclass of the class int, and cannot be subclassed.'''
    ...
    def _class_cleanups (self, *args, **kwargs):
      '''Built-in mutable sequence.

If no argument is given, the constructor creates a new empty list.
The argument must be an iterable if specified.'''
    ...
    def _deprecate (original_func):
      '''None'''
    ...
    def _diffThreshold (self, *args, **kwargs):
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
    def _feedErrorsToResult (self, result, errors):
      '''None'''
    ...
    def _formatMessage (self, msg, standardMsg):
      '''Honour the longMessage attribute when generating failure messages.
        If longMessage is False this means:
        * Use only an explicit message if it is provided
        * Otherwise use the standard message for the assert

        If longMessage is True:
        * Use the standard message
        * If an explicit message is provided, plus ' : ' and the explicit message
        '''
    ...
    def _getAssertEqualityFunc (self, first, second):
      '''Get a detailed comparison function for the types of the two args.

        Returns: A callable accepting (first, second, msg=None) that will
        raise a failure exception if first != second with a useful human
        readable error message for those types.
        '''
    ...
    def _truncateMessage (self, message, diff):
      '''None'''
    ...
    def addClassCleanup (function, /, *args, **kwargs):
      '''Same as addCleanup, except the cleanup items are called even if
        setUpClass fails (unlike tearDownClass).'''
    ...
    def addCleanup (self, function, /, *args, **kwargs):
      '''Add a function, with arguments, to be called when the test is
        completed. Functions added are called on a LIFO basis and are
        called after tearDown on test failure or success.

        Cleanup items are called even if setUp fails (unlike tearDown).'''
    ...
    def addTypeEqualityFunc (self, typeobj, function):
      '''Add a type specific assertEqual style function to compare a type.

        This method is for use by TestCase subclasses that need to register
        their own type equality functions to provide nicer error messages.

        Args:
            typeobj: The data type to call this function on when both values
                    are of the same type in assertEqual().
            function: The callable taking two arguments and an optional
                    msg= argument that raises self.failureException with a
                    useful error message when the two arguments are not equal.
        '''
    ...
    def assertAlmostEqual (self, first, second, places=None, msg=None, delta=None):
      '''Fail if the two objects are unequal as determined by their
           difference rounded to the given number of decimal places
           (default 7) and comparing to zero, or by comparing that the
           difference between the two objects is more than the given
           delta.

           Note that decimal places (from zero) are usually not the same
           as significant digits (measured from the most significant digit).

           If the two objects compare equal then they will automatically
           compare almost equal.
        '''
    ...
    def assertAlmostEquals (*args, **kwargs):
      '''None'''
    ...
    def assertCountEqual (self, first, second, msg=None):
      '''Asserts that two iterables have the same elements, the same number of
        times, without regard to order.

            self.assertEqual(Counter(list(first)),
                             Counter(list(second)))

         Example:
            - [0, 1, 1] and [1, 0, 1] compare equal.
            - [0, 0, 1] and [0, 1] compare unequal.

        '''
    ...
    def assertDefaultNamesAreCorrect (self, module, namesToIgnore=()):
      '''None'''
    ...
    def assertDictContainsSubset (self, subset, dictionary, msg=None):
      '''Checks whether dictionary is a superset of subset.'''
    ...
    def assertDictEqual (self, d1, d2, msg=None):
      '''None'''
    ...
    def assertEqual (self, first, second, msg=None):
      '''Fail if the two objects are unequal as determined by the '=='
           operator.
        '''
    ...
    def assertEquals (*args, **kwargs):
      '''None'''
    ...
    def assertFalse (self, expr, msg=None):
      '''Check that the expression is false.'''
    ...
    def assertFloat32Equal (self, value0, value1):
      '''None'''
    ...
    def assertGreater (self, a, b, msg=None):
      '''Just like self.assertTrue(a > b), but with a nicer default message.'''
    ...
    def assertGreaterEqual (self, a, b, msg=None):
      '''Just like self.assertTrue(a >= b), but with a nicer default message.'''
    ...
    def assertHashesValid (self, node, inputsToIgnore=[], outputsToIgnore=[]):
      '''None'''
    ...
    def assertIn (self, member, container, msg=None):
      '''Just like self.assertTrue(a in b), but with a nicer default message.'''
    ...
    def assertIs (self, expr1, expr2, msg=None):
      '''Just like self.assertTrue(a is b), but with a nicer default message.'''
    ...
    def assertIsInstance (self, obj, cls, msg=None):
      '''Same as self.assertTrue(isinstance(obj, cls)), with a nicer
        default message.'''
    ...
    def assertIsNone (self, obj, msg=None):
      '''Same as self.assertTrue(obj is None), with a nicer default message.'''
    ...
    def assertIsNot (self, expr1, expr2, msg=None):
      '''Just like self.assertTrue(a is not b), but with a nicer default message.'''
    ...
    def assertIsNotNone (self, obj, msg=None):
      '''Included for symmetry with assertIsNone.'''
    ...
    def assertLess (self, a, b, msg=None):
      '''Just like self.assertTrue(a < b), but with a nicer default message.'''
    ...
    def assertLessEqual (self, a, b, msg=None):
      '''Just like self.assertTrue(a <= b), but with a nicer default message.'''
    ...
    def assertListEqual (self, list1, list2, msg=None):
      '''A list-specific equality assertion.

        Args:
            list1: The first list to compare.
            list2: The second list to compare.
            msg: Optional message to use on failure instead of a list of
                    differences.

        '''
    ...
    def assertLogs (self, logger=None, level=None):
      '''Fail unless a log message of level *level* or higher is emitted
        on *logger_name* or its children.  If omitted, *level* defaults to
        INFO and *logger* defaults to the root logger.

        This method must be used as a context manager, and will yield
        a recording object with two attributes: `output` and `records`.
        At the end of the context manager, the `output` attribute will
        be a list of the matching formatted log messages and the
        `records` attribute will be a list of the corresponding LogRecord
        objects.

        Example::

            with self.assertLogs('foo', level='INFO') as cm:
                logging.getLogger('foo').info('first message')
                logging.getLogger('foo.bar').error('second message')
            self.assertEqual(cm.output, ['INFO:foo:first message',
                                         'ERROR:foo.bar:second message'])
        '''
    ...
    def assertModuleDoesNotImportUI (self, moduleName):
      '''None'''
    ...
    def assertMultiLineEqual (self, first, second, msg=None):
      '''Assert that two multi-line strings are equal.'''
    ...
    def assertNoLogs (self, logger=None, level=None):
      ''' Fail unless no log messages of level *level* or higher are emitted
        on *logger_name* or its children.

        This method must be used as a context manager.
        '''
    ...
    def assertNodeIsDocumented (self, node, additionalTerminalPlugTypes=()):
      '''None'''
    ...
    def assertNodesAreDocumented (self, module, additionalTerminalPlugTypes=(), nodesToIgnore=None):
      '''None'''
    ...
    def assertNodesConstructWithDefaultValues (self, module, nodesToIgnore=None, plugsToIgnore=None):
      '''None'''
    ...
    def assertNotAlmostEqual (self, first, second, places=None, msg=None, delta=None):
      '''Fail if the two objects are equal as determined by their
           difference rounded to the given number of decimal places
           (default 7) and comparing to zero, or by comparing that the
           difference between the two objects is less than the given delta.

           Note that decimal places (from zero) are usually not the same
           as significant digits (measured from the most significant digit).

           Objects that are equal automatically fail.
        '''
    ...
    def assertNotAlmostEquals (*args, **kwargs):
      '''None'''
    ...
    def assertNotEqual (self, first, second, msg=None):
      '''Fail if the two objects are equal as determined by the '!='
           operator.
        '''
    ...
    def assertNotEquals (*args, **kwargs):
      '''None'''
    ...
    def assertNotIn (self, member, container, msg=None):
      '''Just like self.assertTrue(a not in b), but with a nicer default message.'''
    ...
    def assertNotIsInstance (self, obj, cls, msg=None):
      '''Included for symmetry with assertIsInstance.'''
    ...
    def assertNotRegex (self, text, unexpected_regex, msg=None):
      '''Fail the test if the text matches the regular expression.'''
    ...
    def assertNotRegexpMatches (*args, **kwargs):
      '''None'''
    ...
    def assertRaises (self, expected_exception, *args, **kwargs):
      '''Fail unless an exception of class expected_exception is raised
           by the callable when invoked with specified positional and
           keyword arguments. If a different type of exception is
           raised, it will not be caught, and the test case will be
           deemed to have suffered an error, exactly as for an
           unexpected exception.

           If called with the callable and arguments omitted, will return a
           context object used like this::

                with self.assertRaises(SomeException):
                    do_something()

           An optional keyword argument 'msg' can be provided when assertRaises
           is used as a context object.

           The context manager keeps a reference to the exception as
           the 'exception' attribute. This allows you to inspect the
           exception after the assertion::

               with self.assertRaises(SomeException) as cm:
                   do_something()
               the_exception = cm.exception
               self.assertEqual(the_exception.error_code, 3)
        '''
    ...
    def assertRaisesRegex (self, expected_exception, expected_regex, *args, **kwargs):
      '''Asserts that the message in a raised exception matches a regex.

        Args:
            expected_exception: Exception class expected to be raised.
            expected_regex: Regex (re.Pattern object or string) expected
                    to be found in error message.
            args: Function to be called and extra positional args.
            kwargs: Extra kwargs.
            msg: Optional message used in case of failure. Can only be used
                    when assertRaisesRegex is used as a context manager.
        '''
    ...
    def assertRaisesRegexp (*args, **kwargs):
      '''None'''
    ...
    def assertRegex (self, text, expected_regex, msg=None):
      '''Fail the test unless the text matches the regular expression.'''
    ...
    def assertRegexpMatches (*args, **kwargs):
      '''None'''
    ...
    def assertSequenceEqual (self, seq1, seq2, msg=None, seq_type=None):
      '''An equality assertion for ordered sequences (like lists and tuples).

        For the purposes of this function, a valid ordered sequence type is one
        which can be indexed, has a length, and has an equality operator.

        Args:
            seq1: The first sequence to compare.
            seq2: The second sequence to compare.
            seq_type: The expected datatype of the sequences, or None if no
                    datatype should be enforced.
            msg: Optional message to use on failure instead of a list of
                    differences.
        '''
    ...
    def assertSetEqual (self, set1, set2, msg=None):
      '''A set-specific equality assertion.

        Args:
            set1: The first set to compare.
            set2: The second set to compare.
            msg: Optional message to use on failure instead of a list of
                    differences.

        assertSetEqual uses ducktyping to support different types of sets, and
        is optimized for sets specifically (parameters must support a
        difference method).
        '''
    ...
    def assertTrue (self, expr, msg=None):
      '''Check that the expression is true.'''
    ...
    def assertTupleEqual (self, tuple1, tuple2, msg=None):
      '''A tuple-specific equality assertion.

        Args:
            tuple1: The first tuple to compare.
            tuple2: The second tuple to compare.
            msg: Optional message to use on failure instead of a list of
                    differences.
        '''
    ...
    def assertTypeNamesArePrefixed (self, module, namesToIgnore=()):
      '''None'''
    ...
    def assertWarns (self, expected_warning, *args, **kwargs):
      '''Fail unless a warning of class warnClass is triggered
           by the callable when invoked with specified positional and
           keyword arguments.  If a different type of warning is
           triggered, it will not be handled: depending on the other
           warning filtering rules in effect, it might be silenced, printed
           out, or raised as an exception.

           If called with the callable and arguments omitted, will return a
           context object used like this::

                with self.assertWarns(SomeWarning):
                    do_something()

           An optional keyword argument 'msg' can be provided when assertWarns
           is used as a context object.

           The context manager keeps a reference to the first matching
           warning as the 'warning' attribute; similarly, the 'filename'
           and 'lineno' attributes give you information about the line
           of Python code from which the warning was triggered.
           This allows you to inspect the warning after the assertion::

               with self.assertWarns(SomeWarning) as cm:
                   do_something()
               the_warning = cm.warning
               self.assertEqual(the_warning.some_attribute, 147)
        '''
    ...
    def assertWarnsRegex (self, expected_warning, expected_regex, *args, **kwargs):
      '''Asserts that the message in a triggered warning matches a regexp.
        Basic functioning is similar to assertWarns() with the addition
        that only warnings whose messages also match the regular expression
        are considered successful matches.

        Args:
            expected_warning: Warning class expected to be triggered.
            expected_regex: Regex (re.Pattern object or string) expected
                    to be found in error message.
            args: Function to be called and extra positional args.
            kwargs: Extra kwargs.
            msg: Optional message used in case of failure. Can only be used
                    when assertWarnsRegex is used as a context manager.
        '''
    ...
    def assert_ (*args, **kwargs):
      '''None'''
    ...
    def countTestCases (self):
      '''None'''
    ...
    def debug (self):
      '''Run the test without collecting errors in a TestResult'''
    ...
    def defaultTestResult (self):
      '''None'''
    ...
    def doClassCleanups ():
      '''Execute all class cleanup functions. Normally called for you after
        tearDownClass.'''
    ...
    def doCleanups (self):
      '''Execute all cleanup functions. Normally called for you after
        tearDown.'''
    ...
    def fail (self, msg=None):
      '''Fail immediately, with the given message.'''
    ...
    def failIf (*args, **kwargs):
      '''None'''
    ...
    def failIfAlmostEqual (*args, **kwargs):
      '''None'''
    ...
    def failIfEqual (*args, **kwargs):
      '''None'''
    ...
    def failUnless (*args, **kwargs):
      '''None'''
    ...
    def failUnlessAlmostEqual (*args, **kwargs):
      '''None'''
    ...
    def failUnlessEqual (*args, **kwargs):
      '''None'''
    ...
    def failUnlessRaises (*args, **kwargs):
      '''None'''
    ...
    def failureException (self, *args, **kwargs):
      '''Assertion failed.'''
    ...
    def failureMessageLevel (self, *args, **kwargs):
      '''None'''
    ...
    def id (self):
      '''None'''
    ...
    def ignoreMessage (self, level, context, message):
      '''None'''
    ...
    def longMessage (self, *args, **kwargs):
      '''bool(x) -> bool

Returns True when the argument x is true, False otherwise.
The builtins True and False are the only two instances of the class bool.
The class bool is a subclass of the class int, and cannot be subclassed.'''
    ...
    def maxDiff (self, *args, **kwargs):
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
    def run (self, result=None):
      '''None'''
    ...
    def scopedLocale (l, category=0):
      '''None'''
    ...
    def setUp (self):
      '''None'''
    ...
    def setUpClass ():
      '''Hook method for setting up class fixture before running tests in the class.'''
    ...
    def shortDescription (self):
      '''Returns a one-line description of the test, or None if no
        description has been provided.

        The default implementation of this method returns the first line of
        the specified test method's docstring.
        '''
    ...
    def skipTest (self, reason):
      '''Skip this test.'''
    ...
    def subTest (self, msg=<object object at 0x7fb108120c10>, **params):
      '''Return a context manager that will return the enclosed block
        of code in a subtest identified by the optional message and
        keyword parameters.  A failure in the subtest marks the test
        case as failed but resumes execution at the end of the enclosed
        block, allowing further test code to be executed.
        '''
    ...
    def tearDown (self):
      '''None'''
    ...
    def tearDownClass ():
      '''Hook method for deconstructing the class fixture after running all tests in the class.'''
    ...
    def temporaryDirectory (self):
      '''None'''
    ...
    def testAcceptsInput (self):
      '''None'''
    ...

def TaskSwitchTest (*args):
      '''

'''      
    ...

class TaskSwitchTest:
    def _TaskSwitchTest__dispatcher (self):
      '''None'''
    ...
    def _TestCase__nodeHasDescription (self, node):
      '''None'''
    ...
    def _TestCase__undocumentedPlugs (self, node, additionalTerminalPlugTypes=()):
      '''None'''
    ...
    def _addExpectedFailure (self, result, exc_info):
      '''None'''
    ...
    def _addSkip (self, result, test_case, reason):
      '''None'''
    ...
    def _addUnexpectedSuccess (self, result):
      '''None'''
    ...
    def _baseAssertEqual (self, first, second, msg=None):
      '''The default assertEqual implementation, not type specific.'''
    ...
    def _callCleanup (self, function, /, *args, **kwargs):
      '''None'''
    ...
    def _callSetUp (self):
      '''None'''
    ...
    def _callTearDown (self):
      '''None'''
    ...
    def _callTestMethod (self, method):
      '''None'''
    ...
    def _classSetupFailed (self, *args, **kwargs):
      '''bool(x) -> bool

Returns True when the argument x is true, False otherwise.
The builtins True and False are the only two instances of the class bool.
The class bool is a subclass of the class int, and cannot be subclassed.'''
    ...
    def _class_cleanups (self, *args, **kwargs):
      '''Built-in mutable sequence.

If no argument is given, the constructor creates a new empty list.
The argument must be an iterable if specified.'''
    ...
    def _deprecate (original_func):
      '''None'''
    ...
    def _diffThreshold (self, *args, **kwargs):
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
    def _feedErrorsToResult (self, result, errors):
      '''None'''
    ...
    def _formatMessage (self, msg, standardMsg):
      '''Honour the longMessage attribute when generating failure messages.
        If longMessage is False this means:
        * Use only an explicit message if it is provided
        * Otherwise use the standard message for the assert

        If longMessage is True:
        * Use the standard message
        * If an explicit message is provided, plus ' : ' and the explicit message
        '''
    ...
    def _getAssertEqualityFunc (self, first, second):
      '''Get a detailed comparison function for the types of the two args.

        Returns: A callable accepting (first, second, msg=None) that will
        raise a failure exception if first != second with a useful human
        readable error message for those types.
        '''
    ...
    def _truncateMessage (self, message, diff):
      '''None'''
    ...
    def addClassCleanup (function, /, *args, **kwargs):
      '''Same as addCleanup, except the cleanup items are called even if
        setUpClass fails (unlike tearDownClass).'''
    ...
    def addCleanup (self, function, /, *args, **kwargs):
      '''Add a function, with arguments, to be called when the test is
        completed. Functions added are called on a LIFO basis and are
        called after tearDown on test failure or success.

        Cleanup items are called even if setUp fails (unlike tearDown).'''
    ...
    def addTypeEqualityFunc (self, typeobj, function):
      '''Add a type specific assertEqual style function to compare a type.

        This method is for use by TestCase subclasses that need to register
        their own type equality functions to provide nicer error messages.

        Args:
            typeobj: The data type to call this function on when both values
                    are of the same type in assertEqual().
            function: The callable taking two arguments and an optional
                    msg= argument that raises self.failureException with a
                    useful error message when the two arguments are not equal.
        '''
    ...
    def assertAlmostEqual (self, first, second, places=None, msg=None, delta=None):
      '''Fail if the two objects are unequal as determined by their
           difference rounded to the given number of decimal places
           (default 7) and comparing to zero, or by comparing that the
           difference between the two objects is more than the given
           delta.

           Note that decimal places (from zero) are usually not the same
           as significant digits (measured from the most significant digit).

           If the two objects compare equal then they will automatically
           compare almost equal.
        '''
    ...
    def assertAlmostEquals (*args, **kwargs):
      '''None'''
    ...
    def assertCountEqual (self, first, second, msg=None):
      '''Asserts that two iterables have the same elements, the same number of
        times, without regard to order.

            self.assertEqual(Counter(list(first)),
                             Counter(list(second)))

         Example:
            - [0, 1, 1] and [1, 0, 1] compare equal.
            - [0, 0, 1] and [0, 1] compare unequal.

        '''
    ...
    def assertDefaultNamesAreCorrect (self, module, namesToIgnore=()):
      '''None'''
    ...
    def assertDictContainsSubset (self, subset, dictionary, msg=None):
      '''Checks whether dictionary is a superset of subset.'''
    ...
    def assertDictEqual (self, d1, d2, msg=None):
      '''None'''
    ...
    def assertEqual (self, first, second, msg=None):
      '''Fail if the two objects are unequal as determined by the '=='
           operator.
        '''
    ...
    def assertEquals (*args, **kwargs):
      '''None'''
    ...
    def assertFalse (self, expr, msg=None):
      '''Check that the expression is false.'''
    ...
    def assertFloat32Equal (self, value0, value1):
      '''None'''
    ...
    def assertGreater (self, a, b, msg=None):
      '''Just like self.assertTrue(a > b), but with a nicer default message.'''
    ...
    def assertGreaterEqual (self, a, b, msg=None):
      '''Just like self.assertTrue(a >= b), but with a nicer default message.'''
    ...
    def assertHashesValid (self, node, inputsToIgnore=[], outputsToIgnore=[]):
      '''None'''
    ...
    def assertIn (self, member, container, msg=None):
      '''Just like self.assertTrue(a in b), but with a nicer default message.'''
    ...
    def assertIs (self, expr1, expr2, msg=None):
      '''Just like self.assertTrue(a is b), but with a nicer default message.'''
    ...
    def assertIsInstance (self, obj, cls, msg=None):
      '''Same as self.assertTrue(isinstance(obj, cls)), with a nicer
        default message.'''
    ...
    def assertIsNone (self, obj, msg=None):
      '''Same as self.assertTrue(obj is None), with a nicer default message.'''
    ...
    def assertIsNot (self, expr1, expr2, msg=None):
      '''Just like self.assertTrue(a is not b), but with a nicer default message.'''
    ...
    def assertIsNotNone (self, obj, msg=None):
      '''Included for symmetry with assertIsNone.'''
    ...
    def assertLess (self, a, b, msg=None):
      '''Just like self.assertTrue(a < b), but with a nicer default message.'''
    ...
    def assertLessEqual (self, a, b, msg=None):
      '''Just like self.assertTrue(a <= b), but with a nicer default message.'''
    ...
    def assertListEqual (self, list1, list2, msg=None):
      '''A list-specific equality assertion.

        Args:
            list1: The first list to compare.
            list2: The second list to compare.
            msg: Optional message to use on failure instead of a list of
                    differences.

        '''
    ...
    def assertLogs (self, logger=None, level=None):
      '''Fail unless a log message of level *level* or higher is emitted
        on *logger_name* or its children.  If omitted, *level* defaults to
        INFO and *logger* defaults to the root logger.

        This method must be used as a context manager, and will yield
        a recording object with two attributes: `output` and `records`.
        At the end of the context manager, the `output` attribute will
        be a list of the matching formatted log messages and the
        `records` attribute will be a list of the corresponding LogRecord
        objects.

        Example::

            with self.assertLogs('foo', level='INFO') as cm:
                logging.getLogger('foo').info('first message')
                logging.getLogger('foo.bar').error('second message')
            self.assertEqual(cm.output, ['INFO:foo:first message',
                                         'ERROR:foo.bar:second message'])
        '''
    ...
    def assertModuleDoesNotImportUI (self, moduleName):
      '''None'''
    ...
    def assertMultiLineEqual (self, first, second, msg=None):
      '''Assert that two multi-line strings are equal.'''
    ...
    def assertNoLogs (self, logger=None, level=None):
      ''' Fail unless no log messages of level *level* or higher are emitted
        on *logger_name* or its children.

        This method must be used as a context manager.
        '''
    ...
    def assertNodeIsDocumented (self, node, additionalTerminalPlugTypes=()):
      '''None'''
    ...
    def assertNodesAreDocumented (self, module, additionalTerminalPlugTypes=(), nodesToIgnore=None):
      '''None'''
    ...
    def assertNodesConstructWithDefaultValues (self, module, nodesToIgnore=None, plugsToIgnore=None):
      '''None'''
    ...
    def assertNotAlmostEqual (self, first, second, places=None, msg=None, delta=None):
      '''Fail if the two objects are equal as determined by their
           difference rounded to the given number of decimal places
           (default 7) and comparing to zero, or by comparing that the
           difference between the two objects is less than the given delta.

           Note that decimal places (from zero) are usually not the same
           as significant digits (measured from the most significant digit).

           Objects that are equal automatically fail.
        '''
    ...
    def assertNotAlmostEquals (*args, **kwargs):
      '''None'''
    ...
    def assertNotEqual (self, first, second, msg=None):
      '''Fail if the two objects are equal as determined by the '!='
           operator.
        '''
    ...
    def assertNotEquals (*args, **kwargs):
      '''None'''
    ...
    def assertNotIn (self, member, container, msg=None):
      '''Just like self.assertTrue(a not in b), but with a nicer default message.'''
    ...
    def assertNotIsInstance (self, obj, cls, msg=None):
      '''Included for symmetry with assertIsInstance.'''
    ...
    def assertNotRegex (self, text, unexpected_regex, msg=None):
      '''Fail the test if the text matches the regular expression.'''
    ...
    def assertNotRegexpMatches (*args, **kwargs):
      '''None'''
    ...
    def assertRaises (self, expected_exception, *args, **kwargs):
      '''Fail unless an exception of class expected_exception is raised
           by the callable when invoked with specified positional and
           keyword arguments. If a different type of exception is
           raised, it will not be caught, and the test case will be
           deemed to have suffered an error, exactly as for an
           unexpected exception.

           If called with the callable and arguments omitted, will return a
           context object used like this::

                with self.assertRaises(SomeException):
                    do_something()

           An optional keyword argument 'msg' can be provided when assertRaises
           is used as a context object.

           The context manager keeps a reference to the exception as
           the 'exception' attribute. This allows you to inspect the
           exception after the assertion::

               with self.assertRaises(SomeException) as cm:
                   do_something()
               the_exception = cm.exception
               self.assertEqual(the_exception.error_code, 3)
        '''
    ...
    def assertRaisesRegex (self, expected_exception, expected_regex, *args, **kwargs):
      '''Asserts that the message in a raised exception matches a regex.

        Args:
            expected_exception: Exception class expected to be raised.
            expected_regex: Regex (re.Pattern object or string) expected
                    to be found in error message.
            args: Function to be called and extra positional args.
            kwargs: Extra kwargs.
            msg: Optional message used in case of failure. Can only be used
                    when assertRaisesRegex is used as a context manager.
        '''
    ...
    def assertRaisesRegexp (*args, **kwargs):
      '''None'''
    ...
    def assertRegex (self, text, expected_regex, msg=None):
      '''Fail the test unless the text matches the regular expression.'''
    ...
    def assertRegexpMatches (*args, **kwargs):
      '''None'''
    ...
    def assertSequenceEqual (self, seq1, seq2, msg=None, seq_type=None):
      '''An equality assertion for ordered sequences (like lists and tuples).

        For the purposes of this function, a valid ordered sequence type is one
        which can be indexed, has a length, and has an equality operator.

        Args:
            seq1: The first sequence to compare.
            seq2: The second sequence to compare.
            seq_type: The expected datatype of the sequences, or None if no
                    datatype should be enforced.
            msg: Optional message to use on failure instead of a list of
                    differences.
        '''
    ...
    def assertSetEqual (self, set1, set2, msg=None):
      '''A set-specific equality assertion.

        Args:
            set1: The first set to compare.
            set2: The second set to compare.
            msg: Optional message to use on failure instead of a list of
                    differences.

        assertSetEqual uses ducktyping to support different types of sets, and
        is optimized for sets specifically (parameters must support a
        difference method).
        '''
    ...
    def assertTrue (self, expr, msg=None):
      '''Check that the expression is true.'''
    ...
    def assertTupleEqual (self, tuple1, tuple2, msg=None):
      '''A tuple-specific equality assertion.

        Args:
            tuple1: The first tuple to compare.
            tuple2: The second tuple to compare.
            msg: Optional message to use on failure instead of a list of
                    differences.
        '''
    ...
    def assertTypeNamesArePrefixed (self, module, namesToIgnore=()):
      '''None'''
    ...
    def assertWarns (self, expected_warning, *args, **kwargs):
      '''Fail unless a warning of class warnClass is triggered
           by the callable when invoked with specified positional and
           keyword arguments.  If a different type of warning is
           triggered, it will not be handled: depending on the other
           warning filtering rules in effect, it might be silenced, printed
           out, or raised as an exception.

           If called with the callable and arguments omitted, will return a
           context object used like this::

                with self.assertWarns(SomeWarning):
                    do_something()

           An optional keyword argument 'msg' can be provided when assertWarns
           is used as a context object.

           The context manager keeps a reference to the first matching
           warning as the 'warning' attribute; similarly, the 'filename'
           and 'lineno' attributes give you information about the line
           of Python code from which the warning was triggered.
           This allows you to inspect the warning after the assertion::

               with self.assertWarns(SomeWarning) as cm:
                   do_something()
               the_warning = cm.warning
               self.assertEqual(the_warning.some_attribute, 147)
        '''
    ...
    def assertWarnsRegex (self, expected_warning, expected_regex, *args, **kwargs):
      '''Asserts that the message in a triggered warning matches a regexp.
        Basic functioning is similar to assertWarns() with the addition
        that only warnings whose messages also match the regular expression
        are considered successful matches.

        Args:
            expected_warning: Warning class expected to be triggered.
            expected_regex: Regex (re.Pattern object or string) expected
                    to be found in error message.
            args: Function to be called and extra positional args.
            kwargs: Extra kwargs.
            msg: Optional message used in case of failure. Can only be used
                    when assertWarnsRegex is used as a context manager.
        '''
    ...
    def assert_ (*args, **kwargs):
      '''None'''
    ...
    def countTestCases (self):
      '''None'''
    ...
    def debug (self):
      '''Run the test without collecting errors in a TestResult'''
    ...
    def defaultTestResult (self):
      '''None'''
    ...
    def doClassCleanups ():
      '''Execute all class cleanup functions. Normally called for you after
        tearDownClass.'''
    ...
    def doCleanups (self):
      '''Execute all cleanup functions. Normally called for you after
        tearDown.'''
    ...
    def fail (self, msg=None):
      '''Fail immediately, with the given message.'''
    ...
    def failIf (*args, **kwargs):
      '''None'''
    ...
    def failIfAlmostEqual (*args, **kwargs):
      '''None'''
    ...
    def failIfEqual (*args, **kwargs):
      '''None'''
    ...
    def failUnless (*args, **kwargs):
      '''None'''
    ...
    def failUnlessAlmostEqual (*args, **kwargs):
      '''None'''
    ...
    def failUnlessEqual (*args, **kwargs):
      '''None'''
    ...
    def failUnlessRaises (*args, **kwargs):
      '''None'''
    ...
    def failureException (self, *args, **kwargs):
      '''Assertion failed.'''
    ...
    def failureMessageLevel (self, *args, **kwargs):
      '''None'''
    ...
    def id (self):
      '''None'''
    ...
    def ignoreMessage (self, level, context, message):
      '''None'''
    ...
    def longMessage (self, *args, **kwargs):
      '''bool(x) -> bool

Returns True when the argument x is true, False otherwise.
The builtins True and False are the only two instances of the class bool.
The class bool is a subclass of the class int, and cannot be subclassed.'''
    ...
    def maxDiff (self, *args, **kwargs):
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
    def run (self, result=None):
      '''None'''
    ...
    def scopedLocale (l, category=0):
      '''None'''
    ...
    def setUp (self):
      '''None'''
    ...
    def setUpClass ():
      '''Hook method for setting up class fixture before running tests in the class.'''
    ...
    def shortDescription (self):
      '''Returns a one-line description of the test, or None if no
        description has been provided.

        The default implementation of this method returns the first line of
        the specified test method's docstring.
        '''
    ...
    def skipTest (self, reason):
      '''Skip this test.'''
    ...
    def subTest (self, msg=<object object at 0x7fb108120c10>, **params):
      '''Return a context manager that will return the enclosed block
        of code in a subtest identified by the optional message and
        keyword parameters.  A failure in the subtest marks the test
        case as failed but resumes execution at the end of the enclosed
        block, allowing further test code to be executed.
        '''
    ...
    def tearDown (self):
      '''None'''
    ...
    def tearDownClass ():
      '''Hook method for deconstructing the class fixture after running all tests in the class.'''
    ...
    def temporaryDirectory (self):
      '''None'''
    ...
    def test (self):
      '''None'''
    ...
    def testDirectCycles (self):
      '''None'''
    ...
    def testIndexExpression (self):
      '''None'''
    ...
    def testUnconnectedIndex (self):
      '''None'''
    ...

def TextWriter (*args):
      '''

'''      
    ...

class TextWriter:
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
    def _TextWriter__processText (self, context):
      '''None'''
    ...
    def acceptsChild (self, *args, **kwargs):
      '''
acceptsChild( (TaskNode)arg1, (GraphComponent)arg2) -> bool :

    C++ signature :
        bool acceptsChild(GafferDispatch::TaskNode,Gaffer::GraphComponent const*)'''
    ...
    def acceptsParent (self, *args, **kwargs):
      '''
acceptsParent( (TaskNode)arg1, (GraphComponent)arg2) -> bool :

    C++ signature :
        bool acceptsParent(GafferDispatch::TaskNode,Gaffer::GraphComponent const*)'''
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
    def execute (self):
      '''None'''
    ...
    def executeSequence (self, frames):
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
    def getName (self, *args, **kwargs):
      '''
getName( (GraphComponent)arg1) -> str :

    C++ signature :
        char const* getName(Gaffer::GraphComponent {lvalue})'''
    ...
    def hash (self, context):
      '''None'''
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
    def postTasks (self, *args, **kwargs):
      '''
postTasks( (TaskNode)arg1, (Context)arg2) -> list :

    C++ signature :
        boost::python::list postTasks(GafferDispatch::TaskNode {lvalue},Gaffer::Context*)'''
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
    def requiresSequenceExecution (self):
      '''None'''
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

def WedgeTest (*args):
      '''

'''      
    ...

class WedgeTest:
    def _TestCase__nodeHasDescription (self, node):
      '''None'''
    ...
    def _TestCase__undocumentedPlugs (self, node, additionalTerminalPlugTypes=()):
      '''None'''
    ...
    def _WedgeTest__dispatcher (self, frameRange=None):
      '''None'''
    ...
    def _addExpectedFailure (self, result, exc_info):
      '''None'''
    ...
    def _addSkip (self, result, test_case, reason):
      '''None'''
    ...
    def _addUnexpectedSuccess (self, result):
      '''None'''
    ...
    def _baseAssertEqual (self, first, second, msg=None):
      '''The default assertEqual implementation, not type specific.'''
    ...
    def _callCleanup (self, function, /, *args, **kwargs):
      '''None'''
    ...
    def _callSetUp (self):
      '''None'''
    ...
    def _callTearDown (self):
      '''None'''
    ...
    def _callTestMethod (self, method):
      '''None'''
    ...
    def _classSetupFailed (self, *args, **kwargs):
      '''bool(x) -> bool

Returns True when the argument x is true, False otherwise.
The builtins True and False are the only two instances of the class bool.
The class bool is a subclass of the class int, and cannot be subclassed.'''
    ...
    def _class_cleanups (self, *args, **kwargs):
      '''Built-in mutable sequence.

If no argument is given, the constructor creates a new empty list.
The argument must be an iterable if specified.'''
    ...
    def _deprecate (original_func):
      '''None'''
    ...
    def _diffThreshold (self, *args, **kwargs):
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
    def _feedErrorsToResult (self, result, errors):
      '''None'''
    ...
    def _formatMessage (self, msg, standardMsg):
      '''Honour the longMessage attribute when generating failure messages.
        If longMessage is False this means:
        * Use only an explicit message if it is provided
        * Otherwise use the standard message for the assert

        If longMessage is True:
        * Use the standard message
        * If an explicit message is provided, plus ' : ' and the explicit message
        '''
    ...
    def _getAssertEqualityFunc (self, first, second):
      '''Get a detailed comparison function for the types of the two args.

        Returns: A callable accepting (first, second, msg=None) that will
        raise a failure exception if first != second with a useful human
        readable error message for those types.
        '''
    ...
    def _truncateMessage (self, message, diff):
      '''None'''
    ...
    def addClassCleanup (function, /, *args, **kwargs):
      '''Same as addCleanup, except the cleanup items are called even if
        setUpClass fails (unlike tearDownClass).'''
    ...
    def addCleanup (self, function, /, *args, **kwargs):
      '''Add a function, with arguments, to be called when the test is
        completed. Functions added are called on a LIFO basis and are
        called after tearDown on test failure or success.

        Cleanup items are called even if setUp fails (unlike tearDown).'''
    ...
    def addTypeEqualityFunc (self, typeobj, function):
      '''Add a type specific assertEqual style function to compare a type.

        This method is for use by TestCase subclasses that need to register
        their own type equality functions to provide nicer error messages.

        Args:
            typeobj: The data type to call this function on when both values
                    are of the same type in assertEqual().
            function: The callable taking two arguments and an optional
                    msg= argument that raises self.failureException with a
                    useful error message when the two arguments are not equal.
        '''
    ...
    def assertAlmostEqual (self, first, second, places=None, msg=None, delta=None):
      '''Fail if the two objects are unequal as determined by their
           difference rounded to the given number of decimal places
           (default 7) and comparing to zero, or by comparing that the
           difference between the two objects is more than the given
           delta.

           Note that decimal places (from zero) are usually not the same
           as significant digits (measured from the most significant digit).

           If the two objects compare equal then they will automatically
           compare almost equal.
        '''
    ...
    def assertAlmostEquals (*args, **kwargs):
      '''None'''
    ...
    def assertCountEqual (self, first, second, msg=None):
      '''Asserts that two iterables have the same elements, the same number of
        times, without regard to order.

            self.assertEqual(Counter(list(first)),
                             Counter(list(second)))

         Example:
            - [0, 1, 1] and [1, 0, 1] compare equal.
            - [0, 0, 1] and [0, 1] compare unequal.

        '''
    ...
    def assertDefaultNamesAreCorrect (self, module, namesToIgnore=()):
      '''None'''
    ...
    def assertDictContainsSubset (self, subset, dictionary, msg=None):
      '''Checks whether dictionary is a superset of subset.'''
    ...
    def assertDictEqual (self, d1, d2, msg=None):
      '''None'''
    ...
    def assertEqual (self, first, second, msg=None):
      '''Fail if the two objects are unequal as determined by the '=='
           operator.
        '''
    ...
    def assertEquals (*args, **kwargs):
      '''None'''
    ...
    def assertFalse (self, expr, msg=None):
      '''Check that the expression is false.'''
    ...
    def assertFloat32Equal (self, value0, value1):
      '''None'''
    ...
    def assertGreater (self, a, b, msg=None):
      '''Just like self.assertTrue(a > b), but with a nicer default message.'''
    ...
    def assertGreaterEqual (self, a, b, msg=None):
      '''Just like self.assertTrue(a >= b), but with a nicer default message.'''
    ...
    def assertHashesValid (self, node, inputsToIgnore=[], outputsToIgnore=[]):
      '''None'''
    ...
    def assertIn (self, member, container, msg=None):
      '''Just like self.assertTrue(a in b), but with a nicer default message.'''
    ...
    def assertIs (self, expr1, expr2, msg=None):
      '''Just like self.assertTrue(a is b), but with a nicer default message.'''
    ...
    def assertIsInstance (self, obj, cls, msg=None):
      '''Same as self.assertTrue(isinstance(obj, cls)), with a nicer
        default message.'''
    ...
    def assertIsNone (self, obj, msg=None):
      '''Same as self.assertTrue(obj is None), with a nicer default message.'''
    ...
    def assertIsNot (self, expr1, expr2, msg=None):
      '''Just like self.assertTrue(a is not b), but with a nicer default message.'''
    ...
    def assertIsNotNone (self, obj, msg=None):
      '''Included for symmetry with assertIsNone.'''
    ...
    def assertLess (self, a, b, msg=None):
      '''Just like self.assertTrue(a < b), but with a nicer default message.'''
    ...
    def assertLessEqual (self, a, b, msg=None):
      '''Just like self.assertTrue(a <= b), but with a nicer default message.'''
    ...
    def assertListEqual (self, list1, list2, msg=None):
      '''A list-specific equality assertion.

        Args:
            list1: The first list to compare.
            list2: The second list to compare.
            msg: Optional message to use on failure instead of a list of
                    differences.

        '''
    ...
    def assertLogs (self, logger=None, level=None):
      '''Fail unless a log message of level *level* or higher is emitted
        on *logger_name* or its children.  If omitted, *level* defaults to
        INFO and *logger* defaults to the root logger.

        This method must be used as a context manager, and will yield
        a recording object with two attributes: `output` and `records`.
        At the end of the context manager, the `output` attribute will
        be a list of the matching formatted log messages and the
        `records` attribute will be a list of the corresponding LogRecord
        objects.

        Example::

            with self.assertLogs('foo', level='INFO') as cm:
                logging.getLogger('foo').info('first message')
                logging.getLogger('foo.bar').error('second message')
            self.assertEqual(cm.output, ['INFO:foo:first message',
                                         'ERROR:foo.bar:second message'])
        '''
    ...
    def assertModuleDoesNotImportUI (self, moduleName):
      '''None'''
    ...
    def assertMultiLineEqual (self, first, second, msg=None):
      '''Assert that two multi-line strings are equal.'''
    ...
    def assertNoLogs (self, logger=None, level=None):
      ''' Fail unless no log messages of level *level* or higher are emitted
        on *logger_name* or its children.

        This method must be used as a context manager.
        '''
    ...
    def assertNodeIsDocumented (self, node, additionalTerminalPlugTypes=()):
      '''None'''
    ...
    def assertNodesAreDocumented (self, module, additionalTerminalPlugTypes=(), nodesToIgnore=None):
      '''None'''
    ...
    def assertNodesConstructWithDefaultValues (self, module, nodesToIgnore=None, plugsToIgnore=None):
      '''None'''
    ...
    def assertNotAlmostEqual (self, first, second, places=None, msg=None, delta=None):
      '''Fail if the two objects are equal as determined by their
           difference rounded to the given number of decimal places
           (default 7) and comparing to zero, or by comparing that the
           difference between the two objects is less than the given delta.

           Note that decimal places (from zero) are usually not the same
           as significant digits (measured from the most significant digit).

           Objects that are equal automatically fail.
        '''
    ...
    def assertNotAlmostEquals (*args, **kwargs):
      '''None'''
    ...
    def assertNotEqual (self, first, second, msg=None):
      '''Fail if the two objects are equal as determined by the '!='
           operator.
        '''
    ...
    def assertNotEquals (*args, **kwargs):
      '''None'''
    ...
    def assertNotIn (self, member, container, msg=None):
      '''Just like self.assertTrue(a not in b), but with a nicer default message.'''
    ...
    def assertNotIsInstance (self, obj, cls, msg=None):
      '''Included for symmetry with assertIsInstance.'''
    ...
    def assertNotRegex (self, text, unexpected_regex, msg=None):
      '''Fail the test if the text matches the regular expression.'''
    ...
    def assertNotRegexpMatches (*args, **kwargs):
      '''None'''
    ...
    def assertRaises (self, expected_exception, *args, **kwargs):
      '''Fail unless an exception of class expected_exception is raised
           by the callable when invoked with specified positional and
           keyword arguments. If a different type of exception is
           raised, it will not be caught, and the test case will be
           deemed to have suffered an error, exactly as for an
           unexpected exception.

           If called with the callable and arguments omitted, will return a
           context object used like this::

                with self.assertRaises(SomeException):
                    do_something()

           An optional keyword argument 'msg' can be provided when assertRaises
           is used as a context object.

           The context manager keeps a reference to the exception as
           the 'exception' attribute. This allows you to inspect the
           exception after the assertion::

               with self.assertRaises(SomeException) as cm:
                   do_something()
               the_exception = cm.exception
               self.assertEqual(the_exception.error_code, 3)
        '''
    ...
    def assertRaisesRegex (self, expected_exception, expected_regex, *args, **kwargs):
      '''Asserts that the message in a raised exception matches a regex.

        Args:
            expected_exception: Exception class expected to be raised.
            expected_regex: Regex (re.Pattern object or string) expected
                    to be found in error message.
            args: Function to be called and extra positional args.
            kwargs: Extra kwargs.
            msg: Optional message used in case of failure. Can only be used
                    when assertRaisesRegex is used as a context manager.
        '''
    ...
    def assertRaisesRegexp (*args, **kwargs):
      '''None'''
    ...
    def assertRegex (self, text, expected_regex, msg=None):
      '''Fail the test unless the text matches the regular expression.'''
    ...
    def assertRegexpMatches (*args, **kwargs):
      '''None'''
    ...
    def assertSequenceEqual (self, seq1, seq2, msg=None, seq_type=None):
      '''An equality assertion for ordered sequences (like lists and tuples).

        For the purposes of this function, a valid ordered sequence type is one
        which can be indexed, has a length, and has an equality operator.

        Args:
            seq1: The first sequence to compare.
            seq2: The second sequence to compare.
            seq_type: The expected datatype of the sequences, or None if no
                    datatype should be enforced.
            msg: Optional message to use on failure instead of a list of
                    differences.
        '''
    ...
    def assertSetEqual (self, set1, set2, msg=None):
      '''A set-specific equality assertion.

        Args:
            set1: The first set to compare.
            set2: The second set to compare.
            msg: Optional message to use on failure instead of a list of
                    differences.

        assertSetEqual uses ducktyping to support different types of sets, and
        is optimized for sets specifically (parameters must support a
        difference method).
        '''
    ...
    def assertTrue (self, expr, msg=None):
      '''Check that the expression is true.'''
    ...
    def assertTupleEqual (self, tuple1, tuple2, msg=None):
      '''A tuple-specific equality assertion.

        Args:
            tuple1: The first tuple to compare.
            tuple2: The second tuple to compare.
            msg: Optional message to use on failure instead of a list of
                    differences.
        '''
    ...
    def assertTypeNamesArePrefixed (self, module, namesToIgnore=()):
      '''None'''
    ...
    def assertWarns (self, expected_warning, *args, **kwargs):
      '''Fail unless a warning of class warnClass is triggered
           by the callable when invoked with specified positional and
           keyword arguments.  If a different type of warning is
           triggered, it will not be handled: depending on the other
           warning filtering rules in effect, it might be silenced, printed
           out, or raised as an exception.

           If called with the callable and arguments omitted, will return a
           context object used like this::

                with self.assertWarns(SomeWarning):
                    do_something()

           An optional keyword argument 'msg' can be provided when assertWarns
           is used as a context object.

           The context manager keeps a reference to the first matching
           warning as the 'warning' attribute; similarly, the 'filename'
           and 'lineno' attributes give you information about the line
           of Python code from which the warning was triggered.
           This allows you to inspect the warning after the assertion::

               with self.assertWarns(SomeWarning) as cm:
                   do_something()
               the_warning = cm.warning
               self.assertEqual(the_warning.some_attribute, 147)
        '''
    ...
    def assertWarnsRegex (self, expected_warning, expected_regex, *args, **kwargs):
      '''Asserts that the message in a triggered warning matches a regexp.
        Basic functioning is similar to assertWarns() with the addition
        that only warnings whose messages also match the regular expression
        are considered successful matches.

        Args:
            expected_warning: Warning class expected to be triggered.
            expected_regex: Regex (re.Pattern object or string) expected
                    to be found in error message.
            args: Function to be called and extra positional args.
            kwargs: Extra kwargs.
            msg: Optional message used in case of failure. Can only be used
                    when assertWarnsRegex is used as a context manager.
        '''
    ...
    def assert_ (*args, **kwargs):
      '''None'''
    ...
    def countTestCases (self):
      '''None'''
    ...
    def debug (self):
      '''Run the test without collecting errors in a TestResult'''
    ...
    def defaultTestResult (self):
      '''None'''
    ...
    def doClassCleanups ():
      '''Execute all class cleanup functions. Normally called for you after
        tearDownClass.'''
    ...
    def doCleanups (self):
      '''Execute all cleanup functions. Normally called for you after
        tearDown.'''
    ...
    def fail (self, msg=None):
      '''Fail immediately, with the given message.'''
    ...
    def failIf (*args, **kwargs):
      '''None'''
    ...
    def failIfAlmostEqual (*args, **kwargs):
      '''None'''
    ...
    def failIfEqual (*args, **kwargs):
      '''None'''
    ...
    def failUnless (*args, **kwargs):
      '''None'''
    ...
    def failUnlessAlmostEqual (*args, **kwargs):
      '''None'''
    ...
    def failUnlessEqual (*args, **kwargs):
      '''None'''
    ...
    def failUnlessRaises (*args, **kwargs):
      '''None'''
    ...
    def failureException (self, *args, **kwargs):
      '''Assertion failed.'''
    ...
    def failureMessageLevel (self, *args, **kwargs):
      '''None'''
    ...
    def id (self):
      '''None'''
    ...
    def ignoreMessage (self, level, context, message):
      '''None'''
    ...
    def longMessage (self, *args, **kwargs):
      '''bool(x) -> bool

Returns True when the argument x is true, False otherwise.
The builtins True and False are the only two instances of the class bool.
The class bool is a subclass of the class int, and cannot be subclassed.'''
    ...
    def maxDiff (self, *args, **kwargs):
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
    def run (self, result=None):
      '''None'''
    ...
    def scopedLocale (l, category=0):
      '''None'''
    ...
    def setUp (self):
      '''None'''
    ...
    def setUpClass ():
      '''Hook method for setting up class fixture before running tests in the class.'''
    ...
    def shortDescription (self):
      '''Returns a one-line description of the test, or None if no
        description has been provided.

        The default implementation of this method returns the first line of
        the specified test method's docstring.
        '''
    ...
    def skipTest (self, reason):
      '''Skip this test.'''
    ...
    def subTest (self, msg=<object object at 0x7fb108120c10>, **params):
      '''Return a context manager that will return the enclosed block
        of code in a subtest identified by the optional message and
        keyword parameters.  A failure in the subtest marks the test
        case as failed but resumes execution at the end of the enclosed
        block, allowing further test code to be executed.
        '''
    ...
    def tearDown (self):
      '''None'''
    ...
    def tearDownClass ():
      '''Hook method for deconstructing the class fixture after running all tests in the class.'''
    ...
    def temporaryDirectory (self):
      '''None'''
    ...
    def test2DRange (self):
      '''None'''
    ...
    def testColorRange (self):
      '''None'''
    ...
    def testContext (self):
      '''None'''
    ...
    def testFloatByPointOne (self):
      '''None'''
    ...
    def testFloatList (self):
      '''None'''
    ...
    def testFloatRange (self):
      '''None'''
    ...
    def testIntList (self):
      '''None'''
    ...
    def testIntRange (self):
      '''None'''
    ...
    def testStringList (self):
      '''None'''
    ...
    def testUpstreamConstant (self):
      '''None'''
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
