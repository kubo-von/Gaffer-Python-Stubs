
def AttributeInspectorTest (*args):
      '''

'''      
    ...

class AttributeInspectorTest:
    def _AttributeInspectorTest__assertExpectedResult (self, result, source, sourceType, editable, nonEditableReason='', edit=None, editWarning=''):
      '''None'''
    ...
    def _AttributeInspectorTest__inspect (scene, path, attribute, editScope=None):
      '''None'''
    ...
    def _TestCase__nodeHasDescription (self, node):
      '''None'''
    ...
    def _TestCase__undocumentedPlugs (self, node, additionalTerminalPlugTypes=()):
      '''None'''
    ...
    def _TestCase__widgetInstances ():
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
    def assertExampleFilesDontReferenceUnstablePaths (self):
      '''None'''
    ...
    def assertExampleFilesExist (self):
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
    def assertNodeUIsHaveExpectedLifetime (self, module):
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
    def testAttributes (self):
      '''None'''
    ...
    def testAttributesWarning (self):
      '''None'''
    ...
    def testCameraAttribute (self):
      '''None'''
    ...
    def testDirtiedSignal (self):
      '''None'''
    ...
    def testDisabledAttribute (self):
      '''None'''
    ...
    def testDisabledTweaks (self):
      '''None'''
    ...
    def testDontEditParentOfInspectedLocation (self):
      '''None'''
    ...
    def testDownstreamSourceType (self):
      '''None'''
    ...
    def testEditScopeNesting (self):
      '''None'''
    ...
    def testEditScopeNotInHistory (self):
      '''None'''
    ...
    def testLightInsideBox (self):
      '''None'''
    ...
    def testName (self):
      '''None'''
    ...
    def testNonExistentAttribute (self):
      '''None'''
    ...
    def testNonExistentLocation (self):
      '''None'''
    ...
    def testReadOnlyMetadataSignalling (self):
      '''None'''
    ...
    def testRegisteredAttribute (self):
      '''None'''
    ...
    def testSourceAndEdits (self):
      '''None'''
    ...
    def testValue (self):
      '''None'''
    ...
    def waitForIdle (self, count=1):
      '''None'''
    ...

def CameraToolTest (*args):
      '''

'''      
    ...

class CameraToolTest:
    def _TestCase__nodeHasDescription (self, node):
      '''None'''
    ...
    def _TestCase__undocumentedPlugs (self, node, additionalTerminalPlugTypes=()):
      '''None'''
    ...
    def _TestCase__widgetInstances ():
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
    def assertCameraEditable (self, view, cameraEditable):
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
    def assertExampleFilesDontReferenceUnstablePaths (self):
      '''None'''
    ...
    def assertExampleFilesExist (self):
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
    def assertNodeUIsHaveExpectedLifetime (self, module):
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
    def testCameraEditability (self):
      '''None'''
    ...
    def testCenterOfInterestAndUndo (self):
      '''None'''
    ...
    def testDontEditParentLocations (self):
      '''None'''
    ...
    def testEditScopes (self):
      '''None'''
    ...
    def testEditTransform (self):
      '''None'''
    ...
    def testNestedTransform (self):
      '''None'''
    ...
    def testNoUnecessaryHistoryCalls (self):
      '''None'''
    ...
    def testSwitchBackToDefaultCamera (self):
      '''None'''
    ...
    def testTransformNode (self):
      '''None'''
    ...
    def waitForIdle (self, count=1):
      '''None'''
    ...

def ContextAlgoTest (*args):
      '''

'''      
    ...

class ContextAlgoTest:
    def _TestCase__nodeHasDescription (self, node):
      '''None'''
    ...
    def _TestCase__undocumentedPlugs (self, node, additionalTerminalPlugTypes=()):
      '''None'''
    ...
    def _TestCase__widgetInstances ():
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
    def assertExampleFilesDontReferenceUnstablePaths (self):
      '''None'''
    ...
    def assertExampleFilesExist (self):
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
    def assertNodeUIsHaveExpectedLifetime (self, module):
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
    def testAffectsExpandedPaths (self):
      '''None'''
    ...
    def testAffectsSelectedPaths (self):
      '''None'''
    ...
    def testAffectsVisibleSet (self):
      '''None'''
    ...
    def testExpandedPaths (self):
      '''None'''
    ...
    def testExpansionAffectsVisibleSet (self):
      '''None'''
    ...
    def testExpansionIsCopied (self):
      '''None'''
    ...
    def testLastSelectedPath (self):
      '''None'''
    ...
    def testSelectedPaths (self):
      '''None'''
    ...
    def testSelectionIsCopied (self):
      '''None'''
    ...
    def testVisibleSet (self):
      '''None'''
    ...
    def testVisibleSetIsCopied (self):
      '''None'''
    ...
    def waitForIdle (self, count=1):
      '''None'''
    ...

def CropWindowToolTest (*args):
      '''

'''      
    ...

class CropWindowToolTest:
    def _TestCase__nodeHasDescription (self, node):
      '''None'''
    ...
    def _TestCase__undocumentedPlugs (self, node, additionalTerminalPlugTypes=()):
      '''None'''
    ...
    def _TestCase__widgetInstances ():
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
    def assertExampleFilesDontReferenceUnstablePaths (self):
      '''None'''
    ...
    def assertExampleFilesExist (self):
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
    def assertNodeUIsHaveExpectedLifetime (self, module):
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
    def testImageViewStatus (self):
      '''None'''
    ...
    def testSceneViewStatus (self):
      '''None'''
    ...
    def waitForIdle (self, count=1):
      '''None'''
    ...

def DocumentationTest (*args):
      '''

'''      
    ...

class DocumentationTest:
    def _TestCase__nodeHasDescription (self, node):
      '''None'''
    ...
    def _TestCase__undocumentedPlugs (self, node, additionalTerminalPlugTypes=()):
      '''None'''
    ...
    def _TestCase__widgetInstances ():
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
    def assertExampleFilesDontReferenceUnstablePaths (self):
      '''None'''
    ...
    def assertExampleFilesExist (self):
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
    def assertNodeUIsHaveExpectedLifetime (self, module):
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
    def waitForIdle (self, count=1):
      '''None'''
    ...

def HierarchyViewTest (*args):
      '''

'''      
    ...

class HierarchyViewTest:
    def _TestCase__nodeHasDescription (self, node):
      '''None'''
    ...
    def _TestCase__undocumentedPlugs (self, node, additionalTerminalPlugTypes=()):
      '''None'''
    ...
    def _TestCase__widgetInstances ():
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
    def assertExampleFilesDontReferenceUnstablePaths (self):
      '''None'''
    ...
    def assertExampleFilesExist (self):
      '''None'''
    ...
    def assertExpanded (self, context, path, expanded):
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
    def assertNodeUIsHaveExpectedLifetime (self, module):
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
    def testDeselectAndReselectNode (self):
      '''None'''
    ...
    def testNoUnwantedExpansion (self):
      '''None'''
    ...
    def waitForIdle (self, count=1):
      '''None'''
    ...

def HistoryPathTest (*args):
      '''

'''      
    ...

class HistoryPathTest:
    def _HistoryPathTest__inspector (scene, parameter, editScope=None, attribute='light'):
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
    def testCopy (self):
      '''None'''
    ...
    def testEmptyHistory (self):
      '''None'''
    ...
    def testInvalidPath (self):
      '''None'''
    ...
    def testPlugClashing (self):
      '''None'''
    ...
    def testProperties (self):
      '''None'''
    ...
    def testPropertyNames (self):
      '''None'''
    ...
    def uniqueInt (key):
      '''None'''
    ...

def LightEditorTest (*args):
      '''

'''      
    ...

class LightEditorTest:
    def _TestCase__nodeHasDescription (self, node):
      '''None'''
    ...
    def _TestCase__undocumentedPlugs (self, node, additionalTerminalPlugTypes=()):
      '''None'''
    ...
    def _TestCase__widgetInstances ():
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
    def assertExampleFilesDontReferenceUnstablePaths (self):
      '''None'''
    ...
    def assertExampleFilesExist (self):
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
    def assertNodeUIsHaveExpectedLifetime (self, module):
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
    def setLightEditorMuteSelection (self, widget, togglePaths):
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
    def testMuteToggle (self):
      '''None'''
    ...
    def testToggleContext (self):
      '''None'''
    ...
    def waitForIdle (self, count=1):
      '''None'''
    ...

def LightPositionToolTest (*args):
      '''

'''      
    ...

class LightPositionToolTest:
    def _LightPositionToolTest__highlightSource (self, lightP, highlightP, viewP, normal):
      '''None'''
    ...
    def _LightPositionToolTest__shadowSource (self, lightP, shadowPivot, shadowPoint):
      '''None'''
    ...
    def _TestCase__nodeHasDescription (self, node):
      '''None'''
    ...
    def _TestCase__undocumentedPlugs (self, node, additionalTerminalPlugTypes=()):
      '''None'''
    ...
    def _TestCase__widgetInstances ():
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
    def assertAnglesAlmostEqual (a, b, places=7):
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
    def assertExampleFilesDontReferenceUnstablePaths (self):
      '''None'''
    ...
    def assertExampleFilesExist (self):
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
    def assertNodeUIsHaveExpectedLifetime (self, module):
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
    def testPositionHighlight (self):
      '''None'''
    ...
    def testPositionShadow (self):
      '''None'''
    ...
    def testPositionShadowWithParentTransform (self):
      '''None'''
    ...
    def waitForIdle (self, count=1):
      '''None'''
    ...

def LightToolTest (*args):
      '''

'''      
    ...

class LightToolTest:
    def _TestCase__nodeHasDescription (self, node):
      '''None'''
    ...
    def _TestCase__undocumentedPlugs (self, node, additionalTerminalPlugTypes=()):
      '''None'''
    ...
    def _TestCase__widgetInstances ():
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
    def assertExampleFilesDontReferenceUnstablePaths (self):
      '''None'''
    ...
    def assertExampleFilesExist (self):
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
    def assertNodeUIsHaveExpectedLifetime (self, module):
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
    def testDeleteNodeCrash (self):
      '''None'''
    ...
    def testSelection (self):
      '''None'''
    ...
    def testSelectionChangedSignal (self):
      '''None'''
    ...
    def testSpotLightHandleVisibility (self):
      '''None'''
    ...
    def waitForIdle (self, count=1):
      '''None'''
    ...

def NodeUITest (*args):
      '''

'''      
    ...

class NodeUITest:
    def _TestCase__nodeHasDescription (self, node):
      '''None'''
    ...
    def _TestCase__undocumentedPlugs (self, node, additionalTerminalPlugTypes=()):
      '''None'''
    ...
    def _TestCase__widgetInstances ():
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
    def assertExampleFilesDontReferenceUnstablePaths (self):
      '''None'''
    ...
    def assertExampleFilesExist (self):
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
    def assertNodeUIsHaveExpectedLifetime (self, module):
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
    def testLifetimes (self):
      '''None'''
    ...
    def waitForIdle (self, count=1):
      '''None'''
    ...

def OptionInspectorTest (*args):
      '''

'''      
    ...

class OptionInspectorTest:
    def _OptionInspectorTest__assertExpectedResult (self, result, source, sourceType, editable, nonEditableReason='', edit=None, editWarning=''):
      '''None'''
    ...
    def _OptionInspectorTest__inspect (scene, optionName, editScope=None, context=<Gaffer._Gaffer.Context object at 0x7fb0dc995080>):
      '''None'''
    ...
    def _TestCase__nodeHasDescription (self, node):
      '''None'''
    ...
    def _TestCase__undocumentedPlugs (self, node, additionalTerminalPlugTypes=()):
      '''None'''
    ...
    def _TestCase__widgetInstances ():
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
    def assertExampleFilesDontReferenceUnstablePaths (self):
      '''None'''
    ...
    def assertExampleFilesExist (self):
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
    def assertNodeUIsHaveExpectedLifetime (self, module):
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
    def testDefaultValueMetadata (self):
      '''None'''
    ...
    def testDirtiedSignal (self):
      '''None'''
    ...
    def testDisabledTweaks (self):
      '''None'''
    ...
    def testMultipleRenderPassOptionEdits (self):
      '''None'''
    ...
    def testName (self):
      '''None'''
    ...
    def testNonExistentOption (self):
      '''None'''
    ...
    def testReadOnlyMetadataSignalling (self):
      '''None'''
    ...
    def testRegisteredOption (self):
      '''None'''
    ...
    def testRenderPassSourceAndEdits (self):
      '''None'''
    ...
    def testRenderPassValues (self):
      '''None'''
    ...
    def testSourceAndEdits (self):
      '''None'''
    ...
    def testValue (self):
      '''None'''
    ...
    def waitForIdle (self, count=1):
      '''None'''
    ...

def ParameterInspectorTest (*args):
      '''

'''      
    ...

class ParameterInspectorTest:
    def _ParameterInspectorTest__assertExpectedResult (self, result, source, sourceType, editable, nonEditableReason='', edit=None, editWarning=''):
      '''None'''
    ...
    def _ParameterInspectorTest__inspect (scene, path, parameter, editScope=None, attribute='light'):
      '''None'''
    ...
    def _TestCase__nodeHasDescription (self, node):
      '''None'''
    ...
    def _TestCase__undocumentedPlugs (self, node, additionalTerminalPlugTypes=()):
      '''None'''
    ...
    def _TestCase__widgetInstances ():
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
    def assertExampleFilesDontReferenceUnstablePaths (self):
      '''None'''
    ...
    def assertExampleFilesExist (self):
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
    def assertNodeUIsHaveExpectedLifetime (self, module):
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
    def testAnimatedPlugEditability (self):
      '''None'''
    ...
    def testDefaultSpreadsheetRow (self):
      '''None'''
    ...
    def testDirtiedSignal (self):
      '''None'''
    ...
    def testDisabledTweaks (self):
      '''None'''
    ...
    def testDownstreamSourceType (self):
      '''None'''
    ...
    def testEditScopeNesting (self):
      '''None'''
    ...
    def testEditScopeNotInHistory (self):
      '''None'''
    ...
    def testInspectorShaderDiscovery (self):
      '''None'''
    ...
    def testLightInsideBox (self):
      '''None'''
    ...
    def testLightOptionalValuePlug (self):
      '''None'''
    ...
    def testName (self):
      '''None'''
    ...
    def testNonExistentAttribute (self):
      '''None'''
    ...
    def testNonExistentLocation (self):
      '''None'''
    ...
    def testNonExistentParameter (self):
      '''None'''
    ...
    def testPlugWithInput (self):
      '''None'''
    ...
    def testReadOnlyMetadataSignalling (self):
      '''None'''
    ...
    def testReadOnlyPlug (self):
      '''None'''
    ...
    def testShaderAssignmentWarning (self):
      '''None'''
    ...
    def testSourceAndEdits (self):
      '''None'''
    ...
    def testUnsupportedSourceNode (self):
      '''None'''
    ...
    def testValue (self):
      '''None'''
    ...
    def testWrongAttributeType (self):
      '''None'''
    ...
    def waitForIdle (self, count=1):
      '''None'''
    ...

def RenderPassEditorTest (*args):
      '''

'''      
    ...

class RenderPassEditorTest:
    def _TestCase__nodeHasDescription (self, node):
      '''None'''
    ...
    def _TestCase__undocumentedPlugs (self, node, additionalTerminalPlugTypes=()):
      '''None'''
    ...
    def _TestCase__widgetInstances ():
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
    def assertExampleFilesDontReferenceUnstablePaths (self):
      '''None'''
    ...
    def assertExampleFilesExist (self):
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
    def assertNodeUIsHaveExpectedLifetime (self, module):
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
    def testDisabledRenderPassFilter (self):
      '''None'''
    ...
    def testDisabledRenderPassFilterWithPathGroupingFunction (self):
      '''None'''
    ...
    def testPathGroupingFunction (self):
      '''None'''
    ...
    def testRenderPassPathCancellation (self):
      '''None'''
    ...
    def testRenderPassPathIsLeaf (self):
      '''None'''
    ...
    def testRenderPassPathIsValid (self):
      '''None'''
    ...
    def testRenderPassPathSimpleChildren (self):
      '''None'''
    ...
    def testSearchFilter (self):
      '''None'''
    ...
    def waitForIdle (self, count=1):
      '''None'''
    ...

def RotateToolTest (*args):
      '''

'''      
    ...

class RotateToolTest:
    def _TestCase__nodeHasDescription (self, node):
      '''None'''
    ...
    def _TestCase__undocumentedPlugs (self, node, additionalTerminalPlugTypes=()):
      '''None'''
    ...
    def _TestCase__widgetInstances ():
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
    def assertExampleFilesDontReferenceUnstablePaths (self):
      '''None'''
    ...
    def assertExampleFilesExist (self):
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
    def assertNodeUIsHaveExpectedLifetime (self, module):
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
    def testEditScopes (self):
      '''None'''
    ...
    def testInteractionWithGroupRotation (self):
      '''None'''
    ...
    def testInteractionWithParentConstraint (self):
      '''None'''
    ...
    def testInteractionWithPointConstraint (self):
      '''None'''
    ...
    def testNegativeLocalScale (self):
      '''None'''
    ...
    def testNegativeParentScale (self):
      '''None'''
    ...
    def testOrientation (self):
      '''None'''
    ...
    def testPivotAffectsHandlesTransform (self):
      '''None'''
    ...
    def testPivotAndExistingTransform (self):
      '''None'''
    ...
    def testRotate (self):
      '''None'''
    ...
    def testTransformWithRotation (self):
      '''None'''
    ...
    def waitForIdle (self, count=1):
      '''None'''
    ...

def ScaleToolTest (*args):
      '''

'''      
    ...

class ScaleToolTest:
    def _TestCase__nodeHasDescription (self, node):
      '''None'''
    ...
    def _TestCase__undocumentedPlugs (self, node, additionalTerminalPlugTypes=()):
      '''None'''
    ...
    def _TestCase__widgetInstances ():
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
    def assertExampleFilesDontReferenceUnstablePaths (self):
      '''None'''
    ...
    def assertExampleFilesExist (self):
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
    def assertNodeUIsHaveExpectedLifetime (self, module):
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
    def testEditIndividualPromotedAxis (self):
      '''None'''
    ...
    def testEditScopes (self):
      '''None'''
    ...
    def testGangedPlugs (self):
      '''None'''
    ...
    def testHandleOriginsRespectPointConstraint (self):
      '''None'''
    ...
    def testHandles (self):
      '''None'''
    ...
    def waitForIdle (self, count=1):
      '''None'''
    ...

def SceneGadgetTest (*args):
      '''

'''      
    ...

class SceneGadgetTest:
    def _SceneGadgetTest__raySphereIntersection (self, origin, direction, center, radius):
      '''None'''
    ...
    def _TestCase__nodeHasDescription (self, node):
      '''None'''
    ...
    def _TestCase__undocumentedPlugs (self, node, additionalTerminalPlugTypes=()):
      '''None'''
    ...
    def _TestCase__widgetInstances ():
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
    def assertExampleFilesDontReferenceUnstablePaths (self):
      '''None'''
    ...
    def assertExampleFilesExist (self):
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
    def assertNodeUIsHaveExpectedLifetime (self, module):
      '''None'''
    ...
    def assertNodesAreDocumented (self, module, additionalTerminalPlugTypes=(), nodesToIgnore=None):
      '''None'''
    ...
    def assertNodesConstructWithDefaultValues (self, module, nodesToIgnore=None, plugsToIgnore=None):
      '''None'''
    ...
    def assertNormalAt (self, gadget, gadgetLine, normal):
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
    def assertObjectAt (self, gadget, ndcPosition, path):
      '''None'''
    ...
    def assertObjectsAt (self, gadget, ndcBox, paths):
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
    def renderer (self, *args, **kwargs):
      '''str(object='') -> str
str(bytes_or_buffer[, encoding[, errors]]) -> str

Create a new string object from the given object. If encoding or
errors is specified, then the object must expose a data buffer
that will be decoded using the given encoding and error handler.
Otherwise, returns the result of object.__str__() (if defined)
or repr(object).
encoding defaults to sys.getdefaultencoding().
errors defaults to 'strict'.'''
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
    def testBound (self):
      '''None'''
    ...
    def testBoundOfUnexpandedEmptyChildren (self):
      '''None'''
    ...
    def testExceptionsDuringCompute (self):
      '''None'''
    ...
    def testExpansion (self):
      '''None'''
    ...
    def testExpressions (self):
      '''None'''
    ...
    def testGLResourceDestruction (self):
      '''None'''
    ...
    def testNormalAt (self):
      '''None'''
    ...
    def testObjectAtLine (self):
      '''None'''
    ...
    def testObjectVisibility (self):
      '''None'''
    ...
    def testObjectsAtBox (self):
      '''None'''
    ...
    def testResizeWindow (self):
      '''None'''
    ...
    def testSelectionMask (self):
      '''None'''
    ...
    def testSelectionMaskAccessors (self):
      '''None'''
    ...
    def testSetAndGetScene (self):
      '''None'''
    ...
    def testSetRenderer (self):
      '''None'''
    ...
    def waitForIdle (self, count=1):
      '''None'''
    ...
    def waitForRender (self, gadget):
      '''None'''
    ...

def SceneInspectorTest (*args):
      '''

'''      
    ...

class SceneInspectorTest:
    def _TestCase__nodeHasDescription (self, node):
      '''None'''
    ...
    def _TestCase__undocumentedPlugs (self, node, additionalTerminalPlugTypes=()):
      '''None'''
    ...
    def _TestCase__widgetInstances ():
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
    def assertExampleFilesDontReferenceUnstablePaths (self):
      '''None'''
    ...
    def assertExampleFilesExist (self):
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
    def assertNodeUIsHaveExpectedLifetime (self, module):
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
    def testTarget (self):
      '''None'''
    ...
    def testTargetPathsAccessors (self):
      '''None'''
    ...
    def waitForIdle (self, count=1):
      '''None'''
    ...

def SceneViewTest (*args):
      '''

'''      
    ...

class SceneViewTest:
    def _TestCase__nodeHasDescription (self, node):
      '''None'''
    ...
    def _TestCase__undocumentedPlugs (self, node, additionalTerminalPlugTypes=()):
      '''None'''
    ...
    def _TestCase__widgetInstances ():
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
    def assertExampleFilesDontReferenceUnstablePaths (self):
      '''None'''
    ...
    def assertExampleFilesExist (self):
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
    def assertNodeUIsHaveExpectedLifetime (self, module):
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
    def testChangingClippingPlanesUpdatesAllFreeCameras (self):
      '''None'''
    ...
    def testClippingPlaneConstraints (self):
      '''None'''
    ...
    def testClippingPlanesAndFOV (self):
      '''None'''
    ...
    def testExpandSelection (self):
      '''None'''
    ...
    def testFactory (self):
      '''None'''
    ...
    def testFrame (self):
      '''None'''
    ...
    def testInitialClippingPlanes (self):
      '''None'''
    ...
    def testLookThrough (self):
      '''None'''
    ...
    def waitForIdle (self, count=1):
      '''None'''
    ...

def SetEditorTest (*args):
      '''

'''      
    ...

class SetEditorTest:
    def _TestCase__nodeHasDescription (self, node):
      '''None'''
    ...
    def _TestCase__undocumentedPlugs (self, node, additionalTerminalPlugTypes=()):
      '''None'''
    ...
    def _TestCase__widgetInstances ():
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
    def assertExampleFilesDontReferenceUnstablePaths (self):
      '''None'''
    ...
    def assertExampleFilesExist (self):
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
    def assertNodeUIsHaveExpectedLifetime (self, module):
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
    def testEmptySetFilter (self):
      '''None'''
    ...
    def testEmptySetFilterWithSelectedMemberCount (self):
      '''None'''
    ...
    def testSearchFilter (self):
      '''None'''
    ...
    def testSearchFilterRemovesEmptyParents (self):
      '''None'''
    ...
    def testSetPathCancellation (self):
      '''None'''
    ...
    def testSetPathIsLeaf (self):
      '''None'''
    ...
    def testSetPathIsValid (self):
      '''None'''
    ...
    def testSetPathMemberCount (self):
      '''None'''
    ...
    def testSetPathNamespacedChildren (self):
      '''None'''
    ...
    def testSetPathSelectedMemberCount (self):
      '''None'''
    ...
    def testSetPathSelectedMemberCountWithInheritance (self):
      '''None'''
    ...
    def testSetPathSimpleChildren (self):
      '''None'''
    ...
    def waitForIdle (self, count=1):
      '''None'''
    ...

def SetMembershipInspectorTest (*args):
      '''

'''      
    ...

class SetMembershipInspectorTest:
    def _SetMembershipInspectorTest__assertExpectedResult (self, result, source, sourceType, editable, nonEditableReason='', edit=None, editWarning=''):
      '''None'''
    ...
    def _SetMembershipInspectorTest__inspect (scene, path, setName, editScope=None):
      '''None'''
    ...
    def _TestCase__nodeHasDescription (self, node):
      '''None'''
    ...
    def _TestCase__undocumentedPlugs (self, node, additionalTerminalPlugTypes=()):
      '''None'''
    ...
    def _TestCase__widgetInstances ():
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
    def assertExampleFilesDontReferenceUnstablePaths (self):
      '''None'''
    ...
    def assertExampleFilesExist (self):
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
    def assertNodeUIsHaveExpectedLifetime (self, module):
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
    def testDirtiedSignal (self):
      '''None'''
    ...
    def testEditScopeEditSetMembership (self):
      '''None'''
    ...
    def testName (self):
      '''None'''
    ...
    def testNonExistentLocation (self):
      '''None'''
    ...
    def testObjectSourceEditSetMembership (self):
      '''None'''
    ...
    def testObjectSourceFallback (self):
      '''None'''
    ...
    def testReadOnlyMetadataSignalling (self):
      '''None'''
    ...
    def testSetNodeEditSetMembership (self):
      '''None'''
    ...
    def testSourceAndEdits (self):
      '''None'''
    ...
    def testValue (self):
      '''None'''
    ...
    def waitForIdle (self, count=1):
      '''None'''
    ...

def ShaderAssignmentUITest (*args):
      '''

'''      
    ...

class ShaderAssignmentUITest:
    def _TestCase__nodeHasDescription (self, node):
      '''None'''
    ...
    def _TestCase__undocumentedPlugs (self, node, additionalTerminalPlugTypes=()):
      '''None'''
    ...
    def _TestCase__widgetInstances ():
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
    def assertExampleFilesDontReferenceUnstablePaths (self):
      '''None'''
    ...
    def assertExampleFilesExist (self):
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
    def assertNodeUIsHaveExpectedLifetime (self, module):
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
    def testBoxNodulePositions (self):
      '''None'''
    ...
    def waitForIdle (self, count=1):
      '''None'''
    ...

def ShaderUITest (*args):
      '''

'''      
    ...

class ShaderUITest:
    def _TestCase__nodeHasDescription (self, node):
      '''None'''
    ...
    def _TestCase__undocumentedPlugs (self, node, additionalTerminalPlugTypes=()):
      '''None'''
    ...
    def _TestCase__widgetInstances ():
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
    def assertExampleFilesDontReferenceUnstablePaths (self):
      '''None'''
    ...
    def assertExampleFilesExist (self):
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
    def assertNodeUIsHaveExpectedLifetime (self, module):
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
    def testNoduleOrdering (self):
      '''None'''
    ...
    def waitForIdle (self, count=1):
      '''None'''
    ...

def ShaderViewTest (*args):
      '''

'''      
    ...

class ShaderViewTest:
    def _TestCase__nodeHasDescription (self, node):
      '''None'''
    ...
    def _TestCase__undocumentedPlugs (self, node, additionalTerminalPlugTypes=()):
      '''None'''
    ...
    def _TestCase__widgetInstances ():
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
    def assertExampleFilesDontReferenceUnstablePaths (self):
      '''None'''
    ...
    def assertExampleFilesExist (self):
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
    def assertNodeUIsHaveExpectedLifetime (self, module):
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
    def testCannotViewCatalogue (self):
      '''None'''
    ...
    def testCannotViewSceneSwitch (self):
      '''None'''
    ...
    def testChangeScene (self):
      '''None'''
    ...
    def testFactory (self):
      '''None'''
    ...
    def testRegisterReferenceScene (self):
      '''None'''
    ...
    def testRegisterScene (self):
      '''None'''
    ...
    def testReregisterScene (self):
      '''None'''
    ...
    def testScenesAreReused (self):
      '''None'''
    ...
    def waitForIdle (self, count=1):
      '''None'''
    ...

def StandardGraphLayoutTest (*args):
      '''

'''      
    ...

class StandardGraphLayoutTest:
    def _TestCase__nodeHasDescription (self, node):
      '''None'''
    ...
    def _TestCase__undocumentedPlugs (self, node, additionalTerminalPlugTypes=()):
      '''None'''
    ...
    def _TestCase__widgetInstances ():
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
    def assertExampleFilesDontReferenceUnstablePaths (self):
      '''None'''
    ...
    def assertExampleFilesExist (self):
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
    def assertNodeUIsHaveExpectedLifetime (self, module):
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
    def testConnectNodeInStream (self):
      '''None'''
    ...
    def testConnectNodeInStreamWithMultipleOutputs (self):
      '''None'''
    ...
    def waitForIdle (self, count=1):
      '''None'''
    ...

def TransformToolTest (*args):
      '''

'''      
    ...

class TransformToolTest:
    def _TestCase__nodeHasDescription (self, node):
      '''None'''
    ...
    def _TestCase__undocumentedPlugs (self, node, additionalTerminalPlugTypes=()):
      '''None'''
    ...
    def _TestCase__widgetInstances ():
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
    def assertExampleFilesDontReferenceUnstablePaths (self):
      '''None'''
    ...
    def assertExampleFilesExist (self):
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
    def assertNodeUIsHaveExpectedLifetime (self, module):
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
    def testAcquireTransformEdit (self):
      '''None'''
    ...
    def testDontEditUpstreamOfReference (self):
      '''None'''
    ...
    def testInvalidSelection (self):
      '''None'''
    ...
    def testNestedEditScopes (self):
      '''None'''
    ...
    def testSceneReaderSelectionEditability (self):
      '''None'''
    ...
    def testSelectionEditScopes (self):
      '''None'''
    ...
    def testSelectionEditability (self):
      '''None'''
    ...
    def waitForIdle (self, count=1):
      '''None'''
    ...

def TranslateToolTest (*args):
      '''

'''      
    ...

class TranslateToolTest:
    def _TestCase__nodeHasDescription (self, node):
      '''None'''
    ...
    def _TestCase__undocumentedPlugs (self, node, additionalTerminalPlugTypes=()):
      '''None'''
    ...
    def _TestCase__widgetInstances ():
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
    def assertExampleFilesDontReferenceUnstablePaths (self):
      '''None'''
    ...
    def assertExampleFilesExist (self):
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
    def assertNodeUIsHaveExpectedLifetime (self, module):
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
    def testAnimationHotkey (self):
      '''None'''
    ...
    def testAnimationHotkeyWithEditScopes (self):
      '''None'''
    ...
    def testContext (self):
      '''None'''
    ...
    def testEditAncestorIfSelectionNotTransformable (self):
      '''None'''
    ...
    def testEditScopes (self):
      '''None'''
    ...
    def testGroup (self):
      '''None'''
    ...
    def testHandlesFollowLastSelected (self):
      '''None'''
    ...
    def testHandlesTransform (self):
      '''None'''
    ...
    def testIndividualComponentConnections (self):
      '''None'''
    ...
    def testInteractionWithAimConstraints (self):
      '''None'''
    ...
    def testInteractionWithGroupRotation (self):
      '''None'''
    ...
    def testInteractionWithGroupTranslation (self):
      '''None'''
    ...
    def testInteractionWithParentConstraints (self):
      '''None'''
    ...
    def testInteractionWithRotation (self):
      '''None'''
    ...
    def testLastSelectedObjectWithSharedTransformPlug (self):
      '''None'''
    ...
    def testMultipleSelection (self):
      '''None'''
    ...
    def testMultipleSelectionDoesntPickSamePlugTwice (self):
      '''None'''
    ...
    def testMultipleSelectionWithEditScope (self):
      '''None'''
    ...
    def testNegativeScale (self):
      '''None'''
    ...
    def testNonEditableSelections (self):
      '''None'''
    ...
    def testOrientation (self):
      '''None'''
    ...
    def testParentAndChildInSameEditScope (self):
      '''None'''
    ...
    def testPivotExpression (self):
      '''None'''
    ...
    def testPromotedPlugs (self):
      '''None'''
    ...
    def testScale (self):
      '''None'''
    ...
    def testSelection (self):
      '''None'''
    ...
    def testSelectionChangedSignal (self):
      '''None'''
    ...
    def testSelectionRefersToCorrectPlug (self):
      '''None'''
    ...
    def testSelectionRefersToFirstPublicPlug (self):
      '''None'''
    ...
    def testSelectionSorting (self):
      '''None'''
    ...
    def testSetFilter (self):
      '''None'''
    ...
    def testSpreadsheetAndCollect (self):
      '''None'''
    ...
    def testTransform (self):
      '''None'''
    ...
    def testTransformInEditScopeButEditScopeOff (self):
      '''None'''
    ...
    def testTransformWithRotation (self):
      '''None'''
    ...
    def testTranslate (self):
      '''None'''
    ...
    def waitForIdle (self, count=1):
      '''None'''
    ...

def VisualiserTest (*args):
      '''

'''      
    ...

class VisualiserTest:
    def _TestCase__nodeHasDescription (self, node):
      '''None'''
    ...
    def _TestCase__undocumentedPlugs (self, node, additionalTerminalPlugTypes=()):
      '''None'''
    ...
    def _TestCase__widgetInstances ():
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
    def assertExampleFilesDontReferenceUnstablePaths (self):
      '''None'''
    ...
    def assertExampleFilesExist (self):
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
    def assertNodeUIsHaveExpectedLifetime (self, module):
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
    def testCameraVisualiserFramingBound (self):
      '''None'''
    ...
    def waitForIdle (self, count=1):
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
