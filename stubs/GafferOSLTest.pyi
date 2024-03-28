
def ClosurePlugTest (*args):
      '''

'''      
    ...

class ClosurePlugTest:
    def _SceneTestCase__formatPaths (self, path1, path2):
      '''None'''
    ...
    def _SceneTestCase__pathToString (self, path):
      '''None'''
    ...
    def _SceneTestCase__uniqueInts (self, *args, **kwargs):
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
    def allPathChecks (self, *args, **kwargs):
      '''set() -> new empty set object
set(iterable) -> new set object

Build an unordered collection of unique elements.'''
    ...
    def allSceneChecks (self, *args, **kwargs):
      '''set() -> new empty set object
set(iterable) -> new set object

Build an unordered collection of unique elements.'''
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
    def assertBoxesAlmostEqual (self, box1, box2, places):
      '''None'''
    ...
    def assertBoxesEqual (self, box1, box2):
      '''None'''
    ...
    def assertBuiltInSetsComplete (self, scenePlug):
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
    def assertImageHashesEqual (self, imageA, imageB):
      '''None'''
    ...
    def assertImagesEqual (self, imageA, imageB, maxDifference=0.0, ignoreMetadata=False, ignoreDataWindow=False, ignoreChannelNamesOrder=False, ignoreViewNamesOrder=False, metadataBlacklist=[]):
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
    def assertParallelGetValueComputesObjectOnce (self, scene, path):
      '''None'''
    ...
    def assertPathExists (self, scenePlug, path):
      '''None'''
    ...
    def assertPathHashesEqual (self, scenePlug1, scenePath1, scenePlug2, scenePath2, checks={'object', 'attributes', 'bound', 'childNames', 'transform'}):
      '''None'''
    ...
    def assertPathHashesNotEqual (self, scenePlug1, scenePath1, scenePlug2, scenePath2, checks={'object', 'attributes', 'bound', 'childNames', 'transform'}):
      '''None'''
    ...
    def assertPathsEqual (self, scenePlug1, scenePath1, scenePlug2, scenePath2, checks={'object', 'attributes', 'bound', 'childNames', 'transform'}):
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
    def assertRaisesDeepNotSupported (self, node):
      '''None'''
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
    def assertSceneHashesEqual (self, scenePlug1, scenePlug2, scenePlug2PathPrefix='', pathsToPrune=(), checks={'sets', 'object', 'attributes', 'bound', 'childNames', 'transform', 'globals'}):
      '''None'''
    ...
    def assertSceneHashesNotEqual (self, scenePlug1, scenePlug2, scenePlug2PathPrefix='', pathsToPrune=(), checks={'sets', 'object', 'attributes', 'bound', 'childNames', 'transform', 'globals'}):
      '''None'''
    ...
    def assertSceneValid (self, scenePlug, assertBuiltInSetsComplete=True):
      '''None'''
    ...
    def assertScenesEqual (self, scenePlug1, scenePlug2, scenePlug2PathPrefix='', pathsToPrune=(), checks={'sets', 'object', 'attributes', 'bound', 'childNames', 'transform', 'globals'}):
      '''None'''
    ...
    def assertScenesRenderSame (plugA, plugB, expandProcedurals=False, ignoreLinks=False):
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
    def assertSetsValid (self, scenePlug):
      '''None'''
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
    def channelTestImage (self):
      '''None'''
    ...
    def channelTestImageMultiView (self):
      '''None'''
    ...
    def compileShader (self, sourceFileName):
      '''None'''
    ...
    def countTestCases (self):
      '''None'''
    ...
    def debug (self):
      '''Run the test without collecting errors in a TestResult'''
    ...
    def deepImage (self):
      '''None'''
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
    def emptyImage (self):
      '''None'''
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
    def imagesPath ():
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
    def openColorIOPath ():
      '''None'''
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
    def uniqueInt (key):
      '''None'''
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
    def testNamespacePollution (self):
      '''None'''
    ...

def OSLCodeTest (*args):
      '''

'''      
    ...

class OSLCodeTest:
    def _OSLCodeTest__assertError (self, oslCode, fn, *args, **kw):
      '''None'''
    ...
    def _OSLCodeTest__assertNoError (self, oslCode, fn, *args, **kw):
      '''None'''
    ...
    def _OSLCodeTest__osoFileName (self, oslCode):
      '''None'''
    ...
    def _SceneTestCase__formatPaths (self, path1, path2):
      '''None'''
    ...
    def _SceneTestCase__pathToString (self, path):
      '''None'''
    ...
    def _SceneTestCase__uniqueInts (self, *args, **kwargs):
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
    def allPathChecks (self, *args, **kwargs):
      '''set() -> new empty set object
set(iterable) -> new set object

Build an unordered collection of unique elements.'''
    ...
    def allSceneChecks (self, *args, **kwargs):
      '''set() -> new empty set object
set(iterable) -> new set object

Build an unordered collection of unique elements.'''
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
    def assertBoxesAlmostEqual (self, box1, box2, places):
      '''None'''
    ...
    def assertBoxesEqual (self, box1, box2):
      '''None'''
    ...
    def assertBuiltInSetsComplete (self, scenePlug):
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
    def assertImageHashesEqual (self, imageA, imageB):
      '''None'''
    ...
    def assertImagesEqual (self, imageA, imageB, maxDifference=0.0, ignoreMetadata=False, ignoreDataWindow=False, ignoreChannelNamesOrder=False, ignoreViewNamesOrder=False, metadataBlacklist=[]):
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
    def assertParallelGetValueComputesObjectOnce (self, scene, path):
      '''None'''
    ...
    def assertPathExists (self, scenePlug, path):
      '''None'''
    ...
    def assertPathHashesEqual (self, scenePlug1, scenePath1, scenePlug2, scenePath2, checks={'object', 'attributes', 'bound', 'childNames', 'transform'}):
      '''None'''
    ...
    def assertPathHashesNotEqual (self, scenePlug1, scenePath1, scenePlug2, scenePath2, checks={'object', 'attributes', 'bound', 'childNames', 'transform'}):
      '''None'''
    ...
    def assertPathsEqual (self, scenePlug1, scenePath1, scenePlug2, scenePath2, checks={'object', 'attributes', 'bound', 'childNames', 'transform'}):
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
    def assertRaisesDeepNotSupported (self, node):
      '''None'''
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
    def assertSceneHashesEqual (self, scenePlug1, scenePlug2, scenePlug2PathPrefix='', pathsToPrune=(), checks={'sets', 'object', 'attributes', 'bound', 'childNames', 'transform', 'globals'}):
      '''None'''
    ...
    def assertSceneHashesNotEqual (self, scenePlug1, scenePlug2, scenePlug2PathPrefix='', pathsToPrune=(), checks={'sets', 'object', 'attributes', 'bound', 'childNames', 'transform', 'globals'}):
      '''None'''
    ...
    def assertSceneValid (self, scenePlug, assertBuiltInSetsComplete=True):
      '''None'''
    ...
    def assertScenesEqual (self, scenePlug1, scenePlug2, scenePlug2PathPrefix='', pathsToPrune=(), checks={'sets', 'object', 'attributes', 'bound', 'childNames', 'transform', 'globals'}):
      '''None'''
    ...
    def assertScenesRenderSame (plugA, plugB, expandProcedurals=False, ignoreLinks=False):
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
    def assertSetsValid (self, scenePlug):
      '''None'''
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
    def channelTestImage (self):
      '''None'''
    ...
    def channelTestImageMultiView (self):
      '''None'''
    ...
    def compileShader (self, sourceFileName):
      '''None'''
    ...
    def countTestCases (self):
      '''None'''
    ...
    def debug (self):
      '''Run the test without collecting errors in a TestResult'''
    ...
    def deepImage (self):
      '''None'''
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
    def emptyImage (self):
      '''None'''
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
    def imagesPath ():
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
    def openColorIOPath ():
      '''None'''
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
    def testAddingAndRemovingPlugsUpdatesShader (self):
      '''None'''
    ...
    def testChildAddedSignalNotSuppressedByError (self):
      '''None'''
    ...
    def testColorSpline (self):
      '''None'''
    ...
    def testEmpty (self):
      '''None'''
    ...
    def testImageProcessingFunctions (self):
      '''None'''
    ...
    def testMissingSemiColon (self):
      '''None'''
    ...
    def testMoveCodeDirectory (self):
      '''None'''
    ...
    def testObjectProcessingFunctions (self):
      '''None'''
    ...
    def testParameterRenaming (self):
      '''None'''
    ...
    def testParseError (self):
      '''None'''
    ...
    def testParseErrorDoesntDestroyExistingPlugs (self):
      '''None'''
    ...
    def testPlugTypes (self):
      '''None'''
    ...
    def testRenameRemovedParameter (self):
      '''None'''
    ...
    def testSerialisation (self):
      '''None'''
    ...
    def testShaderNameMatchesFileName (self):
      '''None'''
    ...
    def testSource (self):
      '''None'''
    ...
    def testSourceUsesRequestedName (self):
      '''None'''
    ...
    def testUndo (self):
      '''None'''
    ...
    def uniqueInt (key):
      '''None'''
    ...

def OSLExpressionEngineTest (*args):
      '''

'''      
    ...

class OSLExpressionEngineTest:
    def _SceneTestCase__formatPaths (self, path1, path2):
      '''None'''
    ...
    def _SceneTestCase__pathToString (self, path):
      '''None'''
    ...
    def _SceneTestCase__uniqueInts (self, *args, **kwargs):
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
    def allPathChecks (self, *args, **kwargs):
      '''set() -> new empty set object
set(iterable) -> new set object

Build an unordered collection of unique elements.'''
    ...
    def allSceneChecks (self, *args, **kwargs):
      '''set() -> new empty set object
set(iterable) -> new set object

Build an unordered collection of unique elements.'''
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
    def assertBoxesAlmostEqual (self, box1, box2, places):
      '''None'''
    ...
    def assertBoxesEqual (self, box1, box2):
      '''None'''
    ...
    def assertBuiltInSetsComplete (self, scenePlug):
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
    def assertImageHashesEqual (self, imageA, imageB):
      '''None'''
    ...
    def assertImagesEqual (self, imageA, imageB, maxDifference=0.0, ignoreMetadata=False, ignoreDataWindow=False, ignoreChannelNamesOrder=False, ignoreViewNamesOrder=False, metadataBlacklist=[]):
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
    def assertParallelGetValueComputesObjectOnce (self, scene, path):
      '''None'''
    ...
    def assertPathExists (self, scenePlug, path):
      '''None'''
    ...
    def assertPathHashesEqual (self, scenePlug1, scenePath1, scenePlug2, scenePath2, checks={'object', 'attributes', 'bound', 'childNames', 'transform'}):
      '''None'''
    ...
    def assertPathHashesNotEqual (self, scenePlug1, scenePath1, scenePlug2, scenePath2, checks={'object', 'attributes', 'bound', 'childNames', 'transform'}):
      '''None'''
    ...
    def assertPathsEqual (self, scenePlug1, scenePath1, scenePlug2, scenePath2, checks={'object', 'attributes', 'bound', 'childNames', 'transform'}):
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
    def assertRaisesDeepNotSupported (self, node):
      '''None'''
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
    def assertSceneHashesEqual (self, scenePlug1, scenePlug2, scenePlug2PathPrefix='', pathsToPrune=(), checks={'sets', 'object', 'attributes', 'bound', 'childNames', 'transform', 'globals'}):
      '''None'''
    ...
    def assertSceneHashesNotEqual (self, scenePlug1, scenePlug2, scenePlug2PathPrefix='', pathsToPrune=(), checks={'sets', 'object', 'attributes', 'bound', 'childNames', 'transform', 'globals'}):
      '''None'''
    ...
    def assertSceneValid (self, scenePlug, assertBuiltInSetsComplete=True):
      '''None'''
    ...
    def assertScenesEqual (self, scenePlug1, scenePlug2, scenePlug2PathPrefix='', pathsToPrune=(), checks={'sets', 'object', 'attributes', 'bound', 'childNames', 'transform', 'globals'}):
      '''None'''
    ...
    def assertScenesRenderSame (plugA, plugB, expandProcedurals=False, ignoreLinks=False):
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
    def assertSetsValid (self, scenePlug):
      '''None'''
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
    def channelTestImage (self):
      '''None'''
    ...
    def channelTestImageMultiView (self):
      '''None'''
    ...
    def compileShader (self, sourceFileName):
      '''None'''
    ...
    def countTestCases (self):
      '''None'''
    ...
    def debug (self):
      '''Run the test without collecting errors in a TestResult'''
    ...
    def deepImage (self):
      '''None'''
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
    def emptyImage (self):
      '''None'''
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
    def imagesPath ():
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
    def openColorIOPath ():
      '''None'''
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
    def testBackgroundDispatch (self):
      '''None'''
    ...
    def testBoolPlugs (self):
      '''None'''
    ...
    def testColorPlugs (self):
      '''None'''
    ...
    def testComparisonIsNotAssignment (self):
      '''None'''
    ...
    def testContextFrame (self):
      '''None'''
    ...
    def testContextTypes (self):
      '''None'''
    ...
    def testContextVectorTypes (self):
      '''None'''
    ...
    def testDefaultExpression (self):
      '''None'''
    ...
    def testDeleteInputPlug (self):
      '''None'''
    ...
    def testDeleteOutputPlug (self):
      '''None'''
    ...
    def testDuplicateDeserialise (self):
      '''None'''
    ...
    def testEmptyExpression (self):
      '''None'''
    ...
    def testException (self):
      '''None'''
    ...
    def testFloatPlugs (self):
      '''None'''
    ...
    def testIdentifier (self):
      '''None'''
    ...
    def testIgnoresTimeWhenTimeNotReferenced (self):
      '''None'''
    ...
    def testIndependentOfOrderOfPlugNames (self):
      '''None'''
    ...
    def testIntPlugs (self):
      '''None'''
    ...
    def testInvalidExpression (self):
      '''None'''
    ...
    def testM44fPlugs (self):
      '''None'''
    ...
    def testMoreThanTenPlugs (self):
      '''None'''
    ...
    def testNoSemiColon (self):
      '''None'''
    ...
    def testPlugNamesWithCommonPrefixes (self):
      '''None'''
    ...
    def testRenamePlugs (self):
      '''None'''
    ...
    def testRevertToPreviousExpression (self):
      '''None'''
    ...
    def testScenePathContext (self):
      '''None'''
    ...
    def testSerialisation (self):
      '''None'''
    ...
    def testStdOSL (self):
      '''None'''
    ...
    def testStringComparison (self):
      '''None'''
    ...
    def testStringContextVariableComparison (self):
      '''None'''
    ...
    def testStringPlugs (self):
      '''None'''
    ...
    def testTimeGlobalVariable (self):
      '''None'''
    ...
    def testUnsupportedPlugs (self):
      '''None'''
    ...
    def testV3fPlugs (self):
      '''None'''
    ...
    def uniqueInt (key):
      '''None'''
    ...

def OSLImageTest (*args):
      '''

'''      
    ...

class OSLImageTest:
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
    def assertImageHashesEqual (self, imageA, imageB):
      '''None'''
    ...
    def assertImagesEqual (self, imageA, imageB, maxDifference=0.0, ignoreMetadata=False, ignoreDataWindow=False, ignoreChannelNamesOrder=False, ignoreViewNamesOrder=False, metadataBlacklist=[]):
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
    def assertRaisesDeepNotSupported (self, node):
      '''None'''
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
    def channelTestImage (self):
      '''None'''
    ...
    def channelTestImageMultiView (self):
      '''None'''
    ...
    def countTestCases (self):
      '''None'''
    ...
    def debug (self):
      '''Run the test without collecting errors in a TestResult'''
    ...
    def deepImage (self):
      '''None'''
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
    def emptyImage (self):
      '''None'''
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
    def imagesPath ():
      '''None'''
    ...
    def longMessage (self, *args, **kwargs):
      '''bool(x) -> bool

Returns True when the argument x is true, False otherwise.
The builtins True and False are the only two instances of the class bool.
The class bool is a subclass of the class int, and cannot be subclassed.'''
    ...
    def mandelbrotNode (self):
      '''None'''
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
    def openColorIOPath ():
      '''None'''
    ...
    def representativeDeepImagePath (self, *args, **kwargs):
      '''Path subclass for non-Windows systems.

    On a POSIX system, instantiating a Path should return this object.
    '''
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
    def testAcceptsDot (self):
      '''None'''
    ...
    def testAcceptsShaderSwitch (self):
      '''None'''
    ...
    def testAllTypes (self):
      '''None'''
    ...
    def testBadCachePolicyHang (self):
      '''None'''
    ...
    def testChannelWithZeroValue (self):
      '''None'''
    ...
    def testClosure (self):
      '''None'''
    ...
    def testCollaboratePerf (self):
      '''None'''
    ...
    def testDeep (self):
      '''None'''
    ...
    def testDefaultFormat (self):
      '''None'''
    ...
    def testDirtyPropagation (self):
      '''None'''
    ...
    def testGlobals (self):
      '''None'''
    ...
    def testMinimalPerf (self):
      '''None'''
    ...
    def testNegativeTileCoordinates (self):
      '''None'''
    ...
    def testOSLSplineConnections (self):
      '''None'''
    ...
    def testOSLSplineMatch (self):
      '''None'''
    ...
    def testPassThrough (self):
      '''None'''
    ...
    def testPullsMinimalSetOfInputChannels (self):
      '''None'''
    ...
    def testReferencePromotedPlug (self):
      '''None'''
    ...
    def testShaderNetworkGeneratedInGlobalContext (self):
      '''None'''
    ...
    def testTextureOrientation (self):
      '''None'''
    ...
    def testUndo (self):
      '''None'''
    ...

def OSLLightTest (*args):
      '''

'''      
    ...

class OSLLightTest:
    def _SceneTestCase__formatPaths (self, path1, path2):
      '''None'''
    ...
    def _SceneTestCase__pathToString (self, path):
      '''None'''
    ...
    def _SceneTestCase__uniqueInts (self, *args, **kwargs):
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
    def allPathChecks (self, *args, **kwargs):
      '''set() -> new empty set object
set(iterable) -> new set object

Build an unordered collection of unique elements.'''
    ...
    def allSceneChecks (self, *args, **kwargs):
      '''set() -> new empty set object
set(iterable) -> new set object

Build an unordered collection of unique elements.'''
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
    def assertBoxesAlmostEqual (self, box1, box2, places):
      '''None'''
    ...
    def assertBoxesEqual (self, box1, box2):
      '''None'''
    ...
    def assertBuiltInSetsComplete (self, scenePlug):
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
    def assertImageHashesEqual (self, imageA, imageB):
      '''None'''
    ...
    def assertImagesEqual (self, imageA, imageB, maxDifference=0.0, ignoreMetadata=False, ignoreDataWindow=False, ignoreChannelNamesOrder=False, ignoreViewNamesOrder=False, metadataBlacklist=[]):
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
    def assertParallelGetValueComputesObjectOnce (self, scene, path):
      '''None'''
    ...
    def assertPathExists (self, scenePlug, path):
      '''None'''
    ...
    def assertPathHashesEqual (self, scenePlug1, scenePath1, scenePlug2, scenePath2, checks={'object', 'attributes', 'bound', 'childNames', 'transform'}):
      '''None'''
    ...
    def assertPathHashesNotEqual (self, scenePlug1, scenePath1, scenePlug2, scenePath2, checks={'object', 'attributes', 'bound', 'childNames', 'transform'}):
      '''None'''
    ...
    def assertPathsEqual (self, scenePlug1, scenePath1, scenePlug2, scenePath2, checks={'object', 'attributes', 'bound', 'childNames', 'transform'}):
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
    def assertRaisesDeepNotSupported (self, node):
      '''None'''
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
    def assertSceneHashesEqual (self, scenePlug1, scenePlug2, scenePlug2PathPrefix='', pathsToPrune=(), checks={'sets', 'object', 'attributes', 'bound', 'childNames', 'transform', 'globals'}):
      '''None'''
    ...
    def assertSceneHashesNotEqual (self, scenePlug1, scenePlug2, scenePlug2PathPrefix='', pathsToPrune=(), checks={'sets', 'object', 'attributes', 'bound', 'childNames', 'transform', 'globals'}):
      '''None'''
    ...
    def assertSceneValid (self, scenePlug, assertBuiltInSetsComplete=True):
      '''None'''
    ...
    def assertScenesEqual (self, scenePlug1, scenePlug2, scenePlug2PathPrefix='', pathsToPrune=(), checks={'sets', 'object', 'attributes', 'bound', 'childNames', 'transform', 'globals'}):
      '''None'''
    ...
    def assertScenesRenderSame (plugA, plugB, expandProcedurals=False, ignoreLinks=False):
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
    def assertSetsValid (self, scenePlug):
      '''None'''
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
    def channelTestImage (self):
      '''None'''
    ...
    def channelTestImageMultiView (self):
      '''None'''
    ...
    def compileShader (self, sourceFileName):
      '''None'''
    ...
    def countTestCases (self):
      '''None'''
    ...
    def debug (self):
      '''Run the test without collecting errors in a TestResult'''
    ...
    def deepImage (self):
      '''None'''
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
    def emptyImage (self):
      '''None'''
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
    def imagesPath ():
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
    def openColorIOPath ():
      '''None'''
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
    def testAttributes (self):
      '''None'''
    ...
    def testNetwork (self):
      '''None'''
    ...
    def testSerialisation (self):
      '''None'''
    ...
    def testShader (self):
      '''None'''
    ...
    def testShape (self):
      '''None'''
    ...
    def uniqueInt (key):
      '''None'''
    ...

def OSLObjectTest (*args):
      '''

'''      
    ...

class OSLObjectTest:
    def _SceneTestCase__formatPaths (self, path1, path2):
      '''None'''
    ...
    def _SceneTestCase__pathToString (self, path):
      '''None'''
    ...
    def _SceneTestCase__uniqueInts (self, *args, **kwargs):
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
    def allPathChecks (self, *args, **kwargs):
      '''set() -> new empty set object
set(iterable) -> new set object

Build an unordered collection of unique elements.'''
    ...
    def allSceneChecks (self, *args, **kwargs):
      '''set() -> new empty set object
set(iterable) -> new set object

Build an unordered collection of unique elements.'''
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
    def assertBoxesAlmostEqual (self, box1, box2, places):
      '''None'''
    ...
    def assertBoxesEqual (self, box1, box2):
      '''None'''
    ...
    def assertBuiltInSetsComplete (self, scenePlug):
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
    def assertImageHashesEqual (self, imageA, imageB):
      '''None'''
    ...
    def assertImagesEqual (self, imageA, imageB, maxDifference=0.0, ignoreMetadata=False, ignoreDataWindow=False, ignoreChannelNamesOrder=False, ignoreViewNamesOrder=False, metadataBlacklist=[]):
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
    def assertParallelGetValueComputesObjectOnce (self, scene, path):
      '''None'''
    ...
    def assertPathExists (self, scenePlug, path):
      '''None'''
    ...
    def assertPathHashesEqual (self, scenePlug1, scenePath1, scenePlug2, scenePath2, checks={'object', 'attributes', 'bound', 'childNames', 'transform'}):
      '''None'''
    ...
    def assertPathHashesNotEqual (self, scenePlug1, scenePath1, scenePlug2, scenePath2, checks={'object', 'attributes', 'bound', 'childNames', 'transform'}):
      '''None'''
    ...
    def assertPathsEqual (self, scenePlug1, scenePath1, scenePlug2, scenePath2, checks={'object', 'attributes', 'bound', 'childNames', 'transform'}):
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
    def assertRaisesDeepNotSupported (self, node):
      '''None'''
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
    def assertSceneHashesEqual (self, scenePlug1, scenePlug2, scenePlug2PathPrefix='', pathsToPrune=(), checks={'sets', 'object', 'attributes', 'bound', 'childNames', 'transform', 'globals'}):
      '''None'''
    ...
    def assertSceneHashesNotEqual (self, scenePlug1, scenePlug2, scenePlug2PathPrefix='', pathsToPrune=(), checks={'sets', 'object', 'attributes', 'bound', 'childNames', 'transform', 'globals'}):
      '''None'''
    ...
    def assertSceneValid (self, scenePlug, assertBuiltInSetsComplete=True):
      '''None'''
    ...
    def assertScenesEqual (self, scenePlug1, scenePlug2, scenePlug2PathPrefix='', pathsToPrune=(), checks={'sets', 'object', 'attributes', 'bound', 'childNames', 'transform', 'globals'}):
      '''None'''
    ...
    def assertScenesRenderSame (plugA, plugB, expandProcedurals=False, ignoreLinks=False):
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
    def assertSetsValid (self, scenePlug):
      '''None'''
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
    def channelTestImage (self):
      '''None'''
    ...
    def channelTestImageMultiView (self):
      '''None'''
    ...
    def compileShader (self, sourceFileName):
      '''None'''
    ...
    def countTestCases (self):
      '''None'''
    ...
    def debug (self):
      '''Run the test without collecting errors in a TestResult'''
    ...
    def deepImage (self):
      '''None'''
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
    def emptyImage (self):
      '''None'''
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
    def imagesPath ():
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
    def openColorIOPath ():
      '''None'''
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
    def testAcceptsDot (self):
      '''None'''
    ...
    def testAcceptsShaderSwitch (self):
      '''None'''
    ...
    def testAffects (self):
      '''None'''
    ...
    def testAllTypes (self):
      '''None'''
    ...
    def testAttributeStringSubstitutions (self):
      '''None'''
    ...
    def testAttributeStringSubstitutionsPerf (self):
      '''None'''
    ...
    def testAttributes (self):
      '''None'''
    ...
    def testBoundsUpdate (self):
      '''None'''
    ...
    def testCanReadAndWriteMatrices (self):
      '''None'''
    ...
    def testCanReadFromConstantPrimitiveVariables (self):
      '''None'''
    ...
    def testCanShadeFaceVaryingInterpolatedPrimitiveVariablesAsVertex (self):
      '''None'''
    ...
    def testCanShadeIndexedPrimVar (self):
      '''None'''
    ...
    def testCanShadeVertexInterpolatedPrimitiveVariablesAsUniform (self):
      '''None'''
    ...
    def testCanWriteStringPrimvar (self):
      '''None'''
    ...
    def testClosure (self):
      '''None'''
    ...
    def testColor4fInput (self):
      '''None'''
    ...
    def testContextCompatibility (self):
      '''None'''
    ...
    def testLoadFrom0_55 (self):
      '''None'''
    ...
    def testPrimitiveVariableWithZeroValue (self):
      '''None'''
    ...
    def testReferencePromotedPlug (self):
      '''None'''
    ...
    def testShaderAffectsBoundAndObject (self):
      '''None'''
    ...
    def testShaderSerialisation (self):
      '''None'''
    ...
    def testTextureOrientation (self):
      '''None'''
    ...
    def testTransform (self):
      '''None'''
    ...
    def testUndo (self):
      '''None'''
    ...
    def testWriteUV (self):
      '''None'''
    ...
    def uniqueInt (key):
      '''None'''
    ...

def OSLShaderTest (*args):
      '''

'''      
    ...

class OSLShaderTest:
    def _SceneTestCase__formatPaths (self, path1, path2):
      '''None'''
    ...
    def _SceneTestCase__pathToString (self, path):
      '''None'''
    ...
    def _SceneTestCase__uniqueInts (self, *args, **kwargs):
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
    def allPathChecks (self, *args, **kwargs):
      '''set() -> new empty set object
set(iterable) -> new set object

Build an unordered collection of unique elements.'''
    ...
    def allSceneChecks (self, *args, **kwargs):
      '''set() -> new empty set object
set(iterable) -> new set object

Build an unordered collection of unique elements.'''
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
    def assertBoxesAlmostEqual (self, box1, box2, places):
      '''None'''
    ...
    def assertBoxesEqual (self, box1, box2):
      '''None'''
    ...
    def assertBuiltInSetsComplete (self, scenePlug):
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
    def assertImageHashesEqual (self, imageA, imageB):
      '''None'''
    ...
    def assertImagesEqual (self, imageA, imageB, maxDifference=0.0, ignoreMetadata=False, ignoreDataWindow=False, ignoreChannelNamesOrder=False, ignoreViewNamesOrder=False, metadataBlacklist=[]):
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
    def assertParallelGetValueComputesObjectOnce (self, scene, path):
      '''None'''
    ...
    def assertPathExists (self, scenePlug, path):
      '''None'''
    ...
    def assertPathHashesEqual (self, scenePlug1, scenePath1, scenePlug2, scenePath2, checks={'object', 'attributes', 'bound', 'childNames', 'transform'}):
      '''None'''
    ...
    def assertPathHashesNotEqual (self, scenePlug1, scenePath1, scenePlug2, scenePath2, checks={'object', 'attributes', 'bound', 'childNames', 'transform'}):
      '''None'''
    ...
    def assertPathsEqual (self, scenePlug1, scenePath1, scenePlug2, scenePath2, checks={'object', 'attributes', 'bound', 'childNames', 'transform'}):
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
    def assertRaisesDeepNotSupported (self, node):
      '''None'''
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
    def assertSceneHashesEqual (self, scenePlug1, scenePlug2, scenePlug2PathPrefix='', pathsToPrune=(), checks={'sets', 'object', 'attributes', 'bound', 'childNames', 'transform', 'globals'}):
      '''None'''
    ...
    def assertSceneHashesNotEqual (self, scenePlug1, scenePlug2, scenePlug2PathPrefix='', pathsToPrune=(), checks={'sets', 'object', 'attributes', 'bound', 'childNames', 'transform', 'globals'}):
      '''None'''
    ...
    def assertSceneValid (self, scenePlug, assertBuiltInSetsComplete=True):
      '''None'''
    ...
    def assertScenesEqual (self, scenePlug1, scenePlug2, scenePlug2PathPrefix='', pathsToPrune=(), checks={'sets', 'object', 'attributes', 'bound', 'childNames', 'transform', 'globals'}):
      '''None'''
    ...
    def assertScenesRenderSame (plugA, plugB, expandProcedurals=False, ignoreLinks=False):
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
    def assertSetsValid (self, scenePlug):
      '''None'''
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
    def channelTestImage (self):
      '''None'''
    ...
    def channelTestImageMultiView (self):
      '''None'''
    ...
    def compileShader (self, sourceFileName):
      '''None'''
    ...
    def countTestCases (self):
      '''None'''
    ...
    def debug (self):
      '''Run the test without collecting errors in a TestResult'''
    ...
    def deepImage (self):
      '''None'''
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
    def emptyImage (self):
      '''None'''
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
    def imagesPath ():
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
    def openColorIOPath ():
      '''None'''
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
    def test3delightSplineParameters (self):
      '''None'''
    ...
    def testAcceptsNoneInput (self):
      '''None'''
    ...
    def testActivatorMetadata (self):
      '''None'''
    ...
    def testArrays (self):
      '''None'''
    ...
    def testCanConnectVectorToColor (self):
      '''None'''
    ...
    def testClosureParameters (self):
      '''None'''
    ...
    def testClosureParametersInputAcceptance (self):
      '''None'''
    ...
    def testComponentToComponentConnections (self):
      '''None'''
    ...
    def testDisabledShaderEvaluatesStateCorrectly (self):
      '''None'''
    ...
    def testDisabledShaderPassesThroughExternalValue (self):
      '''None'''
    ...
    def testDisablingShader (self):
      '''None'''
    ...
    def testGetConnectedParameterValueInsideSceneNode (self):
      '''None'''
    ...
    def testHandlesAreHumanReadable (self):
      '''None'''
    ...
    def testHandlesAreUniqueEvenIfNodeNamesArent (self):
      '''None'''
    ...
    def testLoadColorToVectorFromVersion1_3 (self):
      '''None'''
    ...
    def testLoadNetworkFromVersion0_23 (self):
      '''None'''
    ...
    def testLoadNonexistentShader (self):
      '''None'''
    ...
    def testLoadSurfaceAfterShader (self):
      '''None'''
    ...
    def testLoadSurfaceWithOutputParameters (self):
      '''None'''
    ...
    def testMetadataReuse (self):
      '''None'''
    ...
    def testNetwork (self):
      '''None'''
    ...
    def testNoConnectionToParametersPlug (self):
      '''None'''
    ...
    def testOutputClosureDirtying (self):
      '''None'''
    ...
    def testOutputNameIncludedInNetwork (self):
      '''None'''
    ...
    def testOutputPlugAffectsHash (self):
      '''None'''
    ...
    def testOutputTypes (self):
      '''None'''
    ...
    def testOverzealousCycleDetection (self):
      '''None'''
    ...
    def testParameterArrayMetadata (self):
      '''None'''
    ...
    def testParameterMetadata (self):
      '''None'''
    ...
    def testParameterMinMaxMetadata (self):
      '''None'''
    ...
    def testParameterSplineMetadata (self):
      '''None'''
    ...
    def testReconnectionOfChildPlugShader (self):
      '''None'''
    ...
    def testReload (self):
      '''None'''
    ...
    def testRepeatability (self):
      '''None'''
    ...
    def testSearchPaths (self):
      '''None'''
    ...
    def testSerialiation (self):
      '''None'''
    ...
    def testShaderMetadata (self):
      '''None'''
    ...
    def testShaderSerialisation (self):
      '''None'''
    ...
    def testShaderTypeAssignsAsSurfaceType (self):
      '''None'''
    ...
    def testShadingEngineDeduplicate (self):
      '''None'''
    ...
    def testSplineParameterEvaluation (self):
      '''None'''
    ...
    def testSplineParameterSerialisation (self):
      '''None'''
    ...
    def testSplineParameters (self):
      '''None'''
    ...
    def testStructs (self):
      '''None'''
    ...
    def testSurfaceShaderOutParameters (self):
      '''None'''
    ...
    def testUnload (self):
      '''None'''
    ...
    def testVdbVolumeType (self):
      '''None'''
    ...
    def uniqueInt (key):
      '''None'''
    ...

def OSLTestCase (*args):
      '''

'''      
    ...

class OSLTestCase:
    def _SceneTestCase__formatPaths (self, path1, path2):
      '''None'''
    ...
    def _SceneTestCase__pathToString (self, path):
      '''None'''
    ...
    def _SceneTestCase__uniqueInts (self, *args, **kwargs):
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
    def allPathChecks (self, *args, **kwargs):
      '''set() -> new empty set object
set(iterable) -> new set object

Build an unordered collection of unique elements.'''
    ...
    def allSceneChecks (self, *args, **kwargs):
      '''set() -> new empty set object
set(iterable) -> new set object

Build an unordered collection of unique elements.'''
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
    def assertBoxesAlmostEqual (self, box1, box2, places):
      '''None'''
    ...
    def assertBoxesEqual (self, box1, box2):
      '''None'''
    ...
    def assertBuiltInSetsComplete (self, scenePlug):
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
    def assertImageHashesEqual (self, imageA, imageB):
      '''None'''
    ...
    def assertImagesEqual (self, imageA, imageB, maxDifference=0.0, ignoreMetadata=False, ignoreDataWindow=False, ignoreChannelNamesOrder=False, ignoreViewNamesOrder=False, metadataBlacklist=[]):
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
    def assertParallelGetValueComputesObjectOnce (self, scene, path):
      '''None'''
    ...
    def assertPathExists (self, scenePlug, path):
      '''None'''
    ...
    def assertPathHashesEqual (self, scenePlug1, scenePath1, scenePlug2, scenePath2, checks={'object', 'attributes', 'bound', 'childNames', 'transform'}):
      '''None'''
    ...
    def assertPathHashesNotEqual (self, scenePlug1, scenePath1, scenePlug2, scenePath2, checks={'object', 'attributes', 'bound', 'childNames', 'transform'}):
      '''None'''
    ...
    def assertPathsEqual (self, scenePlug1, scenePath1, scenePlug2, scenePath2, checks={'object', 'attributes', 'bound', 'childNames', 'transform'}):
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
    def assertRaisesDeepNotSupported (self, node):
      '''None'''
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
    def assertSceneHashesEqual (self, scenePlug1, scenePlug2, scenePlug2PathPrefix='', pathsToPrune=(), checks={'sets', 'object', 'attributes', 'bound', 'childNames', 'transform', 'globals'}):
      '''None'''
    ...
    def assertSceneHashesNotEqual (self, scenePlug1, scenePlug2, scenePlug2PathPrefix='', pathsToPrune=(), checks={'sets', 'object', 'attributes', 'bound', 'childNames', 'transform', 'globals'}):
      '''None'''
    ...
    def assertSceneValid (self, scenePlug, assertBuiltInSetsComplete=True):
      '''None'''
    ...
    def assertScenesEqual (self, scenePlug1, scenePlug2, scenePlug2PathPrefix='', pathsToPrune=(), checks={'sets', 'object', 'attributes', 'bound', 'childNames', 'transform', 'globals'}):
      '''None'''
    ...
    def assertScenesRenderSame (plugA, plugB, expandProcedurals=False, ignoreLinks=False):
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
    def assertSetsValid (self, scenePlug):
      '''None'''
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
    def channelTestImage (self):
      '''None'''
    ...
    def channelTestImageMultiView (self):
      '''None'''
    ...
    def compileShader (self, sourceFileName):
      '''None'''
    ...
    def countTestCases (self):
      '''None'''
    ...
    def debug (self):
      '''Run the test without collecting errors in a TestResult'''
    ...
    def deepImage (self):
      '''None'''
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
    def emptyImage (self):
      '''None'''
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
    def imagesPath ():
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
    def openColorIOPath ():
      '''None'''
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
    def uniqueInt (key):
      '''None'''
    ...

def ShadingEngineAlgoTest (*args):
      '''

'''      
    ...

class ShadingEngineAlgoTest:
    def _SceneTestCase__formatPaths (self, path1, path2):
      '''None'''
    ...
    def _SceneTestCase__pathToString (self, path):
      '''None'''
    ...
    def _SceneTestCase__uniqueInts (self, *args, **kwargs):
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
    def allPathChecks (self, *args, **kwargs):
      '''set() -> new empty set object
set(iterable) -> new set object

Build an unordered collection of unique elements.'''
    ...
    def allSceneChecks (self, *args, **kwargs):
      '''set() -> new empty set object
set(iterable) -> new set object

Build an unordered collection of unique elements.'''
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
    def assertBoxesAlmostEqual (self, box1, box2, places):
      '''None'''
    ...
    def assertBoxesEqual (self, box1, box2):
      '''None'''
    ...
    def assertBuiltInSetsComplete (self, scenePlug):
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
    def assertImageHashesEqual (self, imageA, imageB):
      '''None'''
    ...
    def assertImagesEqual (self, imageA, imageB, maxDifference=0.0, ignoreMetadata=False, ignoreDataWindow=False, ignoreChannelNamesOrder=False, ignoreViewNamesOrder=False, metadataBlacklist=[]):
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
    def assertParallelGetValueComputesObjectOnce (self, scene, path):
      '''None'''
    ...
    def assertPathExists (self, scenePlug, path):
      '''None'''
    ...
    def assertPathHashesEqual (self, scenePlug1, scenePath1, scenePlug2, scenePath2, checks={'object', 'attributes', 'bound', 'childNames', 'transform'}):
      '''None'''
    ...
    def assertPathHashesNotEqual (self, scenePlug1, scenePath1, scenePlug2, scenePath2, checks={'object', 'attributes', 'bound', 'childNames', 'transform'}):
      '''None'''
    ...
    def assertPathsEqual (self, scenePlug1, scenePath1, scenePlug2, scenePath2, checks={'object', 'attributes', 'bound', 'childNames', 'transform'}):
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
    def assertRaisesDeepNotSupported (self, node):
      '''None'''
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
    def assertSceneHashesEqual (self, scenePlug1, scenePlug2, scenePlug2PathPrefix='', pathsToPrune=(), checks={'sets', 'object', 'attributes', 'bound', 'childNames', 'transform', 'globals'}):
      '''None'''
    ...
    def assertSceneHashesNotEqual (self, scenePlug1, scenePlug2, scenePlug2PathPrefix='', pathsToPrune=(), checks={'sets', 'object', 'attributes', 'bound', 'childNames', 'transform', 'globals'}):
      '''None'''
    ...
    def assertSceneValid (self, scenePlug, assertBuiltInSetsComplete=True):
      '''None'''
    ...
    def assertScenesEqual (self, scenePlug1, scenePlug2, scenePlug2PathPrefix='', pathsToPrune=(), checks={'sets', 'object', 'attributes', 'bound', 'childNames', 'transform', 'globals'}):
      '''None'''
    ...
    def assertScenesRenderSame (plugA, plugB, expandProcedurals=False, ignoreLinks=False):
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
    def assertSetsValid (self, scenePlug):
      '''None'''
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
    def channelTestImage (self):
      '''None'''
    ...
    def channelTestImageMultiView (self):
      '''None'''
    ...
    def compileShader (self, sourceFileName):
      '''None'''
    ...
    def countTestCases (self):
      '''None'''
    ...
    def debug (self):
      '''Run the test without collecting errors in a TestResult'''
    ...
    def deepImage (self):
      '''None'''
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
    def emptyImage (self):
      '''None'''
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
    def imagesPath ():
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
    def openColorIOPath ():
      '''None'''
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
    def testShadeTexture (self):
      '''None'''
    ...
    def uniqueInt (key):
      '''None'''
    ...

def ShadingEngineTest (*args):
      '''

'''      
    ...

class ShadingEngineTest:
    def _SceneTestCase__formatPaths (self, path1, path2):
      '''None'''
    ...
    def _SceneTestCase__pathToString (self, path):
      '''None'''
    ...
    def _SceneTestCase__uniqueInts (self, *args, **kwargs):
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
    def allPathChecks (self, *args, **kwargs):
      '''set() -> new empty set object
set(iterable) -> new set object

Build an unordered collection of unique elements.'''
    ...
    def allSceneChecks (self, *args, **kwargs):
      '''set() -> new empty set object
set(iterable) -> new set object

Build an unordered collection of unique elements.'''
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
    def assertBoxesAlmostEqual (self, box1, box2, places):
      '''None'''
    ...
    def assertBoxesEqual (self, box1, box2):
      '''None'''
    ...
    def assertBuiltInSetsComplete (self, scenePlug):
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
    def assertImageHashesEqual (self, imageA, imageB):
      '''None'''
    ...
    def assertImagesEqual (self, imageA, imageB, maxDifference=0.0, ignoreMetadata=False, ignoreDataWindow=False, ignoreChannelNamesOrder=False, ignoreViewNamesOrder=False, metadataBlacklist=[]):
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
    def assertParallelGetValueComputesObjectOnce (self, scene, path):
      '''None'''
    ...
    def assertPathExists (self, scenePlug, path):
      '''None'''
    ...
    def assertPathHashesEqual (self, scenePlug1, scenePath1, scenePlug2, scenePath2, checks={'object', 'attributes', 'bound', 'childNames', 'transform'}):
      '''None'''
    ...
    def assertPathHashesNotEqual (self, scenePlug1, scenePath1, scenePlug2, scenePath2, checks={'object', 'attributes', 'bound', 'childNames', 'transform'}):
      '''None'''
    ...
    def assertPathsEqual (self, scenePlug1, scenePath1, scenePlug2, scenePath2, checks={'object', 'attributes', 'bound', 'childNames', 'transform'}):
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
    def assertRaisesDeepNotSupported (self, node):
      '''None'''
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
    def assertSceneHashesEqual (self, scenePlug1, scenePlug2, scenePlug2PathPrefix='', pathsToPrune=(), checks={'sets', 'object', 'attributes', 'bound', 'childNames', 'transform', 'globals'}):
      '''None'''
    ...
    def assertSceneHashesNotEqual (self, scenePlug1, scenePlug2, scenePlug2PathPrefix='', pathsToPrune=(), checks={'sets', 'object', 'attributes', 'bound', 'childNames', 'transform', 'globals'}):
      '''None'''
    ...
    def assertSceneValid (self, scenePlug, assertBuiltInSetsComplete=True):
      '''None'''
    ...
    def assertScenesEqual (self, scenePlug1, scenePlug2, scenePlug2PathPrefix='', pathsToPrune=(), checks={'sets', 'object', 'attributes', 'bound', 'childNames', 'transform', 'globals'}):
      '''None'''
    ...
    def assertScenesRenderSame (plugA, plugB, expandProcedurals=False, ignoreLinks=False):
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
    def assertSetsValid (self, scenePlug):
      '''None'''
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
    def channelTestImage (self):
      '''None'''
    ...
    def channelTestImageMultiView (self):
      '''None'''
    ...
    def compileShader (self, sourceFileName):
      '''None'''
    ...
    def countTestCases (self):
      '''None'''
    ...
    def debug (self):
      '''Run the test without collecting errors in a TestResult'''
    ...
    def deepImage (self):
      '''None'''
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
    def emptyImage (self):
      '''None'''
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
    def imagesPath ():
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
    def openColorIOPath ():
      '''None'''
    ...
    def rectanglePoints (self, bound=Box2f(V2f(-1, -1), V2f(1, 1)), divisions=V2i(10, 10)):
      '''None'''
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
    def testCanReadStringData (self):
      '''None'''
    ...
    def testCanReadV3iArrayUserData (self):
      '''None'''
    ...
    def testClosureParameters (self):
      '''None'''
    ...
    def testCompareFloat (self):
      '''None'''
    ...
    def testComponentConnections (self):
      '''None'''
    ...
    def testContextVariable (self):
      '''None'''
    ...
    def testDebugClosure (self):
      '''None'''
    ...
    def testDebugClosureWithInternalValue (self):
      '''None'''
    ...
    def testDebugClosureWithZeroValue (self):
      '''None'''
    ...
    def testDerivatives (self):
      '''None'''
    ...
    def testDoubleAsIntViaGetAttribute (self):
      '''None'''
    ...
    def testDynamicAttributesAllAttributesAreNeeded (self):
      '''None'''
    ...
    def testGlobalAsNeededAttribute (self):
      '''None'''
    ...
    def testGlobals (self):
      '''None'''
    ...
    def testHasDeformation (self):
      '''None'''
    ...
    def testMatrixInput (self):
      '''None'''
    ...
    def testMultipleDebugClosures (self):
      '''None'''
    ...
    def testNetwork (self):
      '''None'''
    ...
    def testParameters (self):
      '''None'''
    ...
    def testReadConstantArraySize1 (self):
      '''None'''
    ...
    def testReadV2fUserData (self):
      '''None'''
    ...
    def testSpline (self):
      '''None'''
    ...
    def testStructs (self):
      '''None'''
    ...
    def testTextureOrientation (self):
      '''None'''
    ...
    def testTime (self):
      '''None'''
    ...
    def testTransform (self):
      '''None'''
    ...
    def testTypedDebugClosure (self):
      '''None'''
    ...
    def testUVProvidedAsV2f (self):
      '''None'''
    ...
    def testUserDataViaGetAttribute (self):
      '''None'''
    ...
    def testVectorToColorConnections (self):
      '''None'''
    ...
    def testWarningForInvalidShaders (self):
      '''None'''
    ...
    def uniqueInt (key):
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
