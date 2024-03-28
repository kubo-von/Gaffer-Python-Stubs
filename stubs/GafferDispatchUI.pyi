
def DispatchDialogue (*args):
      '''

'''      
    ...

class DispatchDialogue:
    def PostDispatchBehaviour (value, names=None, *, module=None, qualname=None, type=None, start=1):
      '''An enumeration.'''
    ...
    def SizeMode (value, names=None, *, module=None, qualname=None, type=None, start=1):
      '''An enumeration.'''
    ...
    def _Dialogue__buttonClicked (self, button):
      '''None'''
    ...
    def _Dialogue__close (self, widget):
      '''None'''
    ...
    def _DispatchDialogue__close (self, *unused):
      '''None'''
    ...
    def _DispatchDialogue__dispatch (self):
      '''None'''
    ...
    def _DispatchDialogue__dispatchDialogueMenuDefinition (self, *args, **kwargs):
      '''None'''
    ...
    def _DispatchDialogue__dispatcherChanged (self, menu):
      '''None'''
    ...
    def _DispatchDialogue__finish (self, result):
      '''None'''
    ...
    def _DispatchDialogue__initiateDispatch (self, button):
      '''None'''
    ...
    def _DispatchDialogue__initiateErrorDisplay (self, exceptionInfo):
      '''None'''
    ...
    def _DispatchDialogue__initiateResultDisplay (self):
      '''None'''
    ...
    def _DispatchDialogue__initiateSettings (self, button):
      '''None'''
    ...
    def _DispatchDialogue__messageCollapsibleChanged (self, collapsible):
      '''None'''
    ...
    def _DispatchDialogue__nodeEditor (self, node):
      '''None'''
    ...
    def _DispatchDialogue__setDispatcher (self, dispatcher):
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
    def _Window__caughtKeys ():
      '''None'''
    ...
    def _Window__caughtKeysSet (self, *args, **kwargs):
      '''None'''
    ...
    def _Window__constrainToScreen (self, position):
      '''None'''
    ...
    def _Window__keyPress (self, widget, event):
      '''None'''
    ...
    def _acceptsClose (self):
      '''None'''
    ...
    def _addButton (self, textOrButton):
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
    def _getWidget (self):
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
    def _revealDescendant (self, descendant):
      '''None'''
    ...
    def _setStyleSheet (self):
      '''None'''
    ...
    def _setWidget (self, widget):
      '''None'''
    ...
    def addChild (self, child):
      '''None'''
    ...
    def addChildWindow (self, childWindow, removeOnClose=False):
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
    def childWindows (self):
      '''None'''
    ...
    def close (self):
      '''None'''
    ...
    def closedSignal (self):
      '''None'''
    ...
    def contextMenuSignal (self):
      '''None'''
    ...
    def createWithDefaultDispatchers (tasks, nodesToShow, defaultDispatcherType=None, postDispatchBehaviour=<PostDispatchBehaviour.Confirm: 2>, title='Dispatch Tasks', sizeMode=<SizeMode.Manual: 2>, **kw):
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
    def getChild (self):
      '''None'''
    ...
    def getDisplayTransform (self):
      '''None'''
    ...
    def getEnabled (self):
      '''None'''
    ...
    def getFullScreen (self):
      '''None'''
    ...
    def getHighlighted (self):
      '''None'''
    ...
    def getIcon (self):
      '''None'''
    ...
    def getModal (self):
      '''None'''
    ...
    def getPosition (self):
      '''None'''
    ...
    def getResizeable (self):
      '''None'''
    ...
    def getSizeMode (self):
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
    def menuDefinition ():
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
    def preCloseSignal (self):
      '''None'''
    ...
    def removeChild (self, child):
      '''None'''
    ...
    def resizeToFitChild (self, shrink=True, expand=True):
      '''None'''
    ...
    def reveal (self):
      '''None'''
    ...
    def scriptNode (self):
      '''None'''
    ...
    def setChild (self, child):
      '''None'''
    ...
    def setDisplayTransform (self, displayTransform):
      '''None'''
    ...
    def setEnabled (self, enabled):
      '''None'''
    ...
    def setFullScreen (self, fullScreen):
      '''None'''
    ...
    def setHighlighted (self, highlighted):
      '''None'''
    ...
    def setIcon (self, imageOrImageFileName):
      '''None'''
    ...
    def setModal (self, modal, parentWindow=None):
      '''None'''
    ...
    def setPosition (self, position, forcePosition=False):
      '''None'''
    ...
    def setResizeable (self, resizeable):
      '''None'''
    ...
    def setSizeMode (self, sizeMode):
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
    def visibilityChangedSignal (self):
      '''None'''
    ...
    def visible (self, relativeTo=None):
      '''None'''
    ...
    def waitForButton (self, parentWindow=None):
      '''None'''
    ...
    def wheelSignal (self):
      '''None'''
    ...
    def widgetAt (position, widgetType=None):
      '''None'''
    ...

def DispatcherUI (*args):
      '''

'''      
    ...

def FrameMaskUI (*args):
      '''

'''      
    ...

def LocalDispatcherUI (*args):
      '''

'''      
    ...

def LocalJobs (*args):
      '''

'''      
    ...

class LocalJobs:
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
    def _LocalJobs__jobAdded (self, job):
      '''None'''
    ...
    def _LocalJobs__jobRemoved (self, job):
      '''None'''
    ...
    def _LocalJobs__jobSelectionChanged (self, widget):
      '''None'''
    ...
    def _LocalJobs__jobStatusChanged (self, job):
      '''None'''
    ...
    def _LocalJobs__killClicked (self, button):
      '''None'''
    ...
    def _LocalJobs__messagesChanged (self, job):
      '''None'''
    ...
    def _LocalJobs__removeClicked (self, button):
      '''None'''
    ...
    def _LocalJobs__selectedJobs (self):
      '''None'''
    ...
    def _LocalJobs__statisticsTimeout (self):
      '''None'''
    ...
    def _LocalJobs__updateButtons (self):
      '''None'''
    ...
    def _LocalJobs__visibilityChanged (self, widget):
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
    def _updateFromContext (self, modifiedItems):
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

def PythonCommandUI (*args):
      '''

'''      
    ...

def SystemCommandUI (*args):
      '''

'''      
    ...

def TaskContextProcessorUI (*args):
      '''

'''      
    ...

def TaskContextVariablesUI (*args):
      '''

'''      
    ...

def TaskListUI (*args):
      '''

'''      
    ...

def TaskNodeUI (*args):
      '''

'''      
    ...

def TaskSwitchUI (*args):
      '''

'''      
    ...

def WedgeUI (*args):
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
