
def AnaglyphUI (*args):
      '''

'''      
    ...

def BleedFillUI (*args):
      '''

'''      
    ...

def BlurUI (*args):
      '''

'''      
    ...

def CDLUI (*args):
      '''

'''      
    ...

def CatalogueSelectUI (*args):
      '''

'''      
    ...

def CatalogueUI (*args):
      '''

'''      
    ...

def ChannelDataProcessorUI (*args):
      '''

'''      
    ...

def ChannelMaskPlugValueWidget (*args):
      '''

'''      
    ...

class ChannelMaskPlugValueWidget:
    def MultiplePlugTypesError (self, *args, **kwargs):
      '''None'''
    ...
    def MultiplePlugsError (self, *args, **kwargs):
      '''None'''
    ...
    def MultipleWidgetCreatorsError (self, *args, **kwargs):
      '''None'''
    ...
    def _ChannelMaskPlugValueWidget__customMetadataName (self, *args, **kwargs):
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
    def _ChannelMaskPlugValueWidget__menuDefinition (self):
      '''None'''
    ...
    def _ChannelMaskPlugValueWidget__setValue (self, unused, value):
      '''None'''
    ...
    def _ChannelMaskPlugValueWidget__toggleCustom (self, checked):
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

def ChannelPlugValueWidget (*args):
      '''

'''      
    ...

class ChannelPlugValueWidget:
    def MultiplePlugTypesError (self, *args, **kwargs):
      '''None'''
    ...
    def MultiplePlugsError (self, *args, **kwargs):
      '''None'''
    ...
    def MultipleWidgetCreatorsError (self, *args, **kwargs):
      '''None'''
    ...
    def _ChannelPlugValueWidget__applyCustom (self, unused):
      '''None'''
    ...
    def _ChannelPlugValueWidget__extraChannels (self):
      '''None'''
    ...
    def _ChannelPlugValueWidget__isCustom (self):
      '''None'''
    ...
    def _ChannelPlugValueWidget__menuDefinition (self):
      '''None'''
    ...
    def _ChannelPlugValueWidget__setValue (self, unused, value):
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

def CheckerboardUI (*args):
      '''

'''      
    ...

def ClampUI (*args):
      '''

'''      
    ...

def CollectImagesUI (*args):
      '''

'''      
    ...

def ColorProcessorUI (*args):
      '''

'''      
    ...

def ColorSpaceUI (*args):
      '''

'''      
    ...

def ConstantUI (*args):
      '''

'''      
    ...

def CopyChannelsUI (*args):
      '''

'''      
    ...

def CopyImageMetadataUI (*args):
      '''

'''      
    ...

def CopyViewsUI (*args):
      '''

'''      
    ...

def CreateViewsUI (*args):
      '''

'''      
    ...

def CropUI (*args):
      '''

'''      
    ...

def DeepHoldoutUI (*args):
      '''

'''      
    ...

def DeepMergeUI (*args):
      '''

'''      
    ...

def DeepRecolorUI (*args):
      '''

'''      
    ...

def DeepSampleCountsUI (*args):
      '''

'''      
    ...

def DeepSamplerUI (*args):
      '''

'''      
    ...

def DeepSliceUI (*args):
      '''

'''      
    ...

def DeepStateUI (*args):
      '''

'''      
    ...

def DeepTidyUI (*args):
      '''

'''      
    ...

def DeepToFlatUI (*args):
      '''

'''      
    ...

def DeleteChannelsUI (*args):
      '''

'''      
    ...

def DeleteImageMetadataUI (*args):
      '''

'''      
    ...

def DeleteViewsUI (*args):
      '''

'''      
    ...

def DilateUI (*args):
      '''

'''      
    ...

def DisplayTransformUI (*args):
      '''

'''      
    ...

def DisplayUI (*args):
      '''

'''      
    ...

def EmptyUI (*args):
      '''

'''      
    ...

def ErodeUI (*args):
      '''

'''      
    ...

def FlatImageProcessorUI (*args):
      '''

'''      
    ...

def FlatImageSourceUI (*args):
      '''

'''      
    ...

def FlatToDeepUI (*args):
      '''

'''      
    ...

def FormatPlugValueWidget (*args):
      '''

'''      
    ...

class FormatPlugValueWidget:
    def MultiplePlugTypesError (self, *args, **kwargs):
      '''None'''
    ...
    def MultiplePlugsError (self, *args, **kwargs):
      '''None'''
    ...
    def MultipleWidgetCreatorsError (self, *args, **kwargs):
      '''None'''
    ...
    def _FormatPlugValueWidget__applyCustomFormat (self, unused):
      '''None'''
    ...
    def _FormatPlugValueWidget__applyFormat (self, unused, fmt):
      '''None'''
    ...
    def _FormatPlugValueWidget__attachChildPlugValueWidgets (self):
      '''None'''
    ...
    def _FormatPlugValueWidget__contextChanged (self, context, key):
      '''None'''
    ...
    def _FormatPlugValueWidget__menuDefinition (self):
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

def FormatQueryUI (*args):
      '''

'''      
    ...

def GradeUI (*args):
      '''

'''      
    ...

def ImageGadget (*args):
      '''
__init__(_object*)

'''      
    ...

class ImageGadget:
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
acceptsChild( (ImageGadget)arg1, (GraphComponent)arg2) -> bool :

    C++ signature :
        bool acceptsChild(GafferImageUI::ImageGadget,Gaffer::GraphComponent const*)'''
    ...
    def acceptsParent (self, *args, **kwargs):
      '''
acceptsParent( (ImageGadget)arg1, (GraphComponent)arg2) -> bool :

    C++ signature :
        bool acceptsParent(GafferImageUI::ImageGadget,Gaffer::GraphComponent const*)'''
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
bound( (ImageGadget)arg1) -> Box3f :

    C++ signature :
        Imath_3_1::Box<Imath_3_1::Vec3<float> > bound(GafferImageUI::ImageGadget)'''
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
getContext( (ImageGadget)arg1) -> object :

    C++ signature :
        Gaffer::Context* getContext(GafferImageUI::ImageGadget {lvalue})'''
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
    def getImage (self, *args, **kwargs):
      '''
getImage( (ImageGadget)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<GafferImage::ImagePlug> getImage(GafferImageUI::ImageGadget)'''
    ...
    def getName (self, *args, **kwargs):
      '''
getName( (GraphComponent)arg1) -> str :

    C++ signature :
        char const* getName(Gaffer::GraphComponent {lvalue})'''
    ...
    def getPaused (self, *args, **kwargs):
      '''
getPaused( (ImageGadget)arg1) -> bool :

    C++ signature :
        bool getPaused(GafferImageUI::ImageGadget {lvalue})'''
    ...
    def getSoloChannel (self, *args, **kwargs):
      '''
getSoloChannel( (ImageGadget)arg1) -> int :

    C++ signature :
        int getSoloChannel(GafferImageUI::ImageGadget {lvalue})'''
    ...
    def getStyle (self, *args, **kwargs):
      '''
getStyle( (Gadget)arg1) -> object :

    C++ signature :
        boost::intrusive_ptr<GafferUI::Style> getStyle(GafferUI::Gadget {lvalue})'''
    ...
    def getToolTip (self, *args, **kwargs):
      '''
getToolTip( (ImageGadget)arg1, (LineSegment3f)arg2) -> str :

    C++ signature :
        std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > getToolTip(GafferImageUI::ImageGadget,IECore::LineSegment<Imath_3_1::Vec3<float> >)'''
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
    def getWipeAngle (self, *args, **kwargs):
      '''
getWipeAngle( (ImageGadget)arg1) -> float :

    C++ signature :
        float getWipeAngle(GafferImageUI::ImageGadget {lvalue})'''
    ...
    def getWipeEnabled (self, *args, **kwargs):
      '''
getWipeEnabled( (ImageGadget)arg1) -> bool :

    C++ signature :
        bool getWipeEnabled(GafferImageUI::ImageGadget {lvalue})'''
    ...
    def getWipePosition (self, *args, **kwargs):
      '''
getWipePosition( (ImageGadget)arg1) -> V2f :

    C++ signature :
        Imath_3_1::Vec2<float> getWipePosition(GafferImageUI::ImageGadget)'''
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
isInstanceOf( (ImageGadget)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(GafferImageUI::ImageGadget {lvalue},IECore::TypeId)

isInstanceOf( (ImageGadget)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(GafferImageUI::ImageGadget {lvalue},char const*)'''
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
    def pixelAt (self, *args, **kwargs):
      '''
pixelAt( (ImageGadget)arg1, (LineSegment3f)arg2) -> V2f :

    C++ signature :
        Imath_3_1::Vec2<float> pixelAt(GafferImageUI::ImageGadget,IECore::LineSegment<Imath_3_1::Vec3<float> >)'''
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
    def resetTileUpdateCount (self, *args, **kwargs):
      '''
resetTileUpdateCount() -> None :

    C++ signature :
        void resetTileUpdateCount()'''
    ...
    def setChild (self, *args, **kwargs):
      '''
setChild( (GraphComponent)arg1, (InternedString)arg2, (GraphComponent)arg3) -> None :

    C++ signature :
        void setChild(Gaffer::GraphComponent {lvalue},IECore::InternedString,Gaffer::GraphComponent {lvalue})'''
    ...
    def setContext (self, *args, **kwargs):
      '''
setContext( (ImageGadget)arg1, (object)arg2) -> None :

    C++ signature :
        void setContext(GafferImageUI::ImageGadget {lvalue},boost::intrusive_ptr<Gaffer::Context>)'''
    ...
    def setEnabled (self, *args, **kwargs):
      '''
setEnabled( (Gadget)arg1, (bool)arg2) -> None :

    C++ signature :
        void setEnabled(GafferUI::Gadget {lvalue},bool)'''
    ...
    def setHighlighted (self, *args, **kwargs):
      '''
setHighlighted( (ImageGadget)arg1, (bool)arg2) -> None :

    C++ signature :
        void setHighlighted(GafferImageUI::ImageGadget {lvalue},bool)'''
    ...
    def setImage (self, *args, **kwargs):
      '''
setImage( (ImageGadget)arg1, (object)arg2) -> None :

    C++ signature :
        void setImage(GafferImageUI::ImageGadget {lvalue},boost::intrusive_ptr<GafferImage::ImagePlug>)'''
    ...
    def setName (self, *args, **kwargs):
      '''
setName( (GraphComponent)arg1, (InternedString)arg2) -> str :

    C++ signature :
        char const* setName(Gaffer::GraphComponent {lvalue},IECore::InternedString)'''
    ...
    def setPaused (self, *args, **kwargs):
      '''
setPaused( (ImageGadget)arg1, (bool)arg2) -> None :

    C++ signature :
        void setPaused(GafferImageUI::ImageGadget {lvalue},bool)'''
    ...
    def setSoloChannel (self, *args, **kwargs):
      '''
setSoloChannel( (ImageGadget)arg1, (int)arg2) -> None :

    C++ signature :
        void setSoloChannel(GafferImageUI::ImageGadget {lvalue},int)'''
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
    def setWipeAngle (self, *args, **kwargs):
      '''
setWipeAngle( (ImageGadget)arg1, (float)arg2) -> None :

    C++ signature :
        void setWipeAngle(GafferImageUI::ImageGadget {lvalue},float)'''
    ...
    def setWipeEnabled (self, *args, **kwargs):
      '''
setWipeEnabled( (ImageGadget)arg1, (bool)arg2) -> None :

    C++ signature :
        void setWipeEnabled(GafferImageUI::ImageGadget {lvalue},bool)'''
    ...
    def setWipePosition (self, *args, **kwargs):
      '''
setWipePosition( (ImageGadget)arg1, (V2f)arg2) -> None :

    C++ signature :
        void setWipePosition(GafferImageUI::ImageGadget {lvalue},Imath_3_1::Vec2<float>)'''
    ...
    def state (self, *args, **kwargs):
      '''
state( (ImageGadget)arg1) -> State :

    C++ signature :
        GafferImageUI::ImageGadget::State state(GafferImageUI::ImageGadget {lvalue})'''
    ...
    def stateChangedSignal (self, *args, **kwargs):
      '''
stateChangedSignal( (ImageGadget)arg1) -> ImageGadgetSignal :

    C++ signature :
        Gaffer::Signals::Signal<void (GafferImageUI::ImageGadget*), Gaffer::Signals::DefaultCombiner<void> > {lvalue} stateChangedSignal(GafferImageUI::ImageGadget {lvalue})'''
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
    def tileUpdateCount (self, *args, **kwargs):
      '''
tileUpdateCount() -> int :

    C++ signature :
        unsigned long tileUpdateCount()'''
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
typeId( (ImageGadget)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(GafferImageUI::ImageGadget {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (ImageGadget)arg1) -> str :

    C++ signature :
        char const* typeName(GafferImageUI::ImageGadget {lvalue})'''
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
    def wheelSignal (self, *args, **kwargs):
      '''
wheelSignal( (Gadget)arg1) -> ButtonSignal :

    C++ signature :
        Gaffer::Signals::Signal<bool (GafferUI::Gadget*, GafferUI::ButtonEvent const&), GafferUI::EventSignalCombiner<bool> > {lvalue} wheelSignal(GafferUI::Gadget {lvalue})'''
    ...

def ImageInspector (*args):
      '''

'''      
    ...

class ImageInspector:
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
    def _ImageInspector__plugParentChanged (self, plug, oldParent):
      '''None'''
    ...
    def _ImageInspector__setPathListingPaths (self):
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

def ImageMetadataUI (*args):
      '''

'''      
    ...

def ImageNodeUI (*args):
      '''

'''      
    ...

def ImageProcessorUI (*args):
      '''

'''      
    ...

def ImageReaderPathPreview (*args):
      '''

'''      
    ...

def ImageReaderUI (*args):
      '''

'''      
    ...

def ImageSamplerUI (*args):
      '''

'''      
    ...

def ImageStatsUI (*args):
      '''

'''      
    ...

def ImageTransformUI (*args):
      '''

'''      
    ...

def ImageView (*args):
      '''
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)
__init__(_object*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > name='ImageView')

'''      
    ...

class ImageView:
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
acceptsChild( (ImageView)arg1, (GraphComponent)arg2) -> bool :

    C++ signature :
        bool acceptsChild(GafferImageUI::ImageView,Gaffer::GraphComponent const*)'''
    ...
    def acceptsParent (self, *args, **kwargs):
      '''
acceptsParent( (ImageView)arg1, (GraphComponent)arg2) -> bool :

    C++ signature :
        bool acceptsParent(GafferImageUI::ImageView,Gaffer::GraphComponent const*)'''
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
isInstanceOf( (ImageView)arg1, (TypeId)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(GafferImageUI::ImageView {lvalue},IECore::TypeId)

isInstanceOf( (ImageView)arg1, (str)arg2) -> bool :

    C++ signature :
        bool isInstanceOf(GafferImageUI::ImageView {lvalue},char const*)'''
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
typeId( (ImageView)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeId(GafferImageUI::ImageView {lvalue})'''
    ...
    def typeIdFromTypeName (self, *args, **kwargs):
      '''
typeIdFromTypeName( (str)arg1) -> TypeId :

    C++ signature :
        IECore::TypeId typeIdFromTypeName(char const*)'''
    ...
    def typeName (self, *args, **kwargs):
      '''
typeName( (ImageView)arg1) -> str :

    C++ signature :
        char const* typeName(GafferImageUI::ImageView {lvalue})'''
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

def ImageViewUI (*args):
      '''

'''      
    ...

def ImageWriterUI (*args):
      '''

'''      
    ...

def LUTUI (*args):
      '''

'''      
    ...

def LookTransformUI (*args):
      '''

'''      
    ...

def MedianUI (*args):
      '''

'''      
    ...

def MergeUI (*args):
      '''

'''      
    ...

def MirrorUI (*args):
      '''

'''      
    ...

def MixUI (*args):
      '''

'''      
    ...

def OffsetUI (*args):
      '''

'''      
    ...

def OpenColorIOAlgo (*args):
      '''

'''      
    ...

def OpenColorIOConfigPlugUI (*args):
      '''

'''      
    ...

def OpenColorIOContextUI (*args):
      '''

'''      
    ...

def OpenColorIOTransformUI (*args):
      '''

'''      
    ...

def OpenImageIOReaderUI (*args):
      '''

'''      
    ...

def PremultiplyUI (*args):
      '''

'''      
    ...

def RGBAChannelsPlugValueWidget (*args):
      '''

'''      
    ...

class RGBAChannelsPlugValueWidget:
    def MultiplePlugTypesError (self, *args, **kwargs):
      '''None'''
    ...
    def MultiplePlugsError (self, *args, **kwargs):
      '''None'''
    ...
    def MultipleWidgetCreatorsError (self, *args, **kwargs):
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
    def _RGBAChannelsPlugValueWidget__setValue (self, unused, value):
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
    def _menuDefinition (self):
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
    def _rgbaChannels (self):
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

def RampUI (*args):
      '''

'''      
    ...

def RankFilterUI (*args):
      '''

'''      
    ...

def RectangleUI (*args):
      '''

'''      
    ...

def ResampleUI (*args):
      '''

'''      
    ...

def ResizeUI (*args):
      '''

'''      
    ...

def SaturationUI (*args):
      '''

'''      
    ...

def SelectViewUI (*args):
      '''

'''      
    ...

def ShapeUI (*args):
      '''

'''      
    ...

def ShuffleUI (*args):
      '''

'''      
    ...

def TextUI (*args):
      '''

'''      
    ...

def UnpremultiplyUI (*args):
      '''

'''      
    ...

def VectorWarpUI (*args):
      '''

'''      
    ...

def ViewPlugValueWidget (*args):
      '''

'''      
    ...

class ViewPlugValueWidget:
    def MultiplePlugTypesError (self, *args, **kwargs):
      '''None'''
    ...
    def MultiplePlugsError (self, *args, **kwargs):
      '''None'''
    ...
    def MultipleWidgetCreatorsError (self, *args, **kwargs):
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
    def _ViewPlugValueWidget__setValue (self, unused, value):
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
    def _menuDefinition (self):
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
    def _views (self):
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

def WarpUI (*args):
      '''

'''      
    ...

def _GafferImageUI (*args):
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
