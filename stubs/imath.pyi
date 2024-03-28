
def BoolArray (*args):
      '''
__init__(_object*, bool, unsigned long)
__init__(_object*, PyImath::FixedArray<bool>)
__init__(_object*, unsigned long)

'''      
    ...

class BoolArray:
    def ifelse (self, *args, **kwargs):
      '''
ifelse( (BoolArray)arg1, (IntArray)arg2, (bool)arg3) -> BoolArray :

    C++ signature :
        PyImath::FixedArray<bool> ifelse(PyImath::FixedArray<bool> {lvalue},PyImath::FixedArray<int>,bool)

ifelse( (BoolArray)arg1, (IntArray)arg2, (BoolArray)arg3) -> BoolArray :

    C++ signature :
        PyImath::FixedArray<bool> ifelse(PyImath::FixedArray<bool> {lvalue},PyImath::FixedArray<int>,PyImath::FixedArray<bool>)'''
    ...
    def makeReadOnly (self, *args, **kwargs):
      '''
makeReadOnly( (BoolArray)arg1) -> None :

    C++ signature :
        void makeReadOnly(PyImath::FixedArray<bool> {lvalue})'''
    ...
    def writable (self, *args, **kwargs):
      '''
writable( (BoolArray)arg1) -> bool :

    C++ signature :
        bool writable(PyImath::FixedArray<bool> {lvalue})'''
    ...

def Box2d (*args):
      '''
__init__(boost::python::api::object, Imath_3_1::Box<Imath_3_1::Vec2<long> >)
__init__(boost::python::api::object, Imath_3_1::Box<Imath_3_1::Vec2<int> >)
__init__(boost::python::api::object, Imath_3_1::Box<Imath_3_1::Vec2<double> >)
__init__(boost::python::api::object, Imath_3_1::Box<Imath_3_1::Vec2<float> >)
__init__(boost::python::api::object, boost::python::tuple, boost::python::tuple)
__init__(boost::python::api::object, boost::python::tuple)
__init__(_object*, Imath_3_1::Vec2<double>, Imath_3_1::Vec2<double>)
__init__(_object*, Imath_3_1::Vec2<double>)
__init__(_object*)
__init__(_object*)

'''      
    ...

class Box2d:
    def center (self, *args, **kwargs):
      '''
center( (Box2d)arg1) -> V2d :
    center() center of the box

    C++ signature :
        Imath_3_1::Vec2<double> center(Imath_3_1::Box<Imath_3_1::Vec2<double> > {lvalue})'''
    ...
    def extendBy (self, *args, **kwargs):
      '''
extendBy( (Box2d)arg1, (V2d)arg2) -> None :
    extendBy(point) extend the box by a point

    C++ signature :
        void extendBy(Imath_3_1::Box<Imath_3_1::Vec2<double> > {lvalue},Imath_3_1::Vec2<double>)

extendBy( (Box2d)arg1, (V2dArray)arg2) -> None :
    extendBy(array) extend the box the values in the array

    C++ signature :
        void extendBy(Imath_3_1::Box<Imath_3_1::Vec2<double> > {lvalue},PyImath::FixedArray<Imath_3_1::Vec2<double> >)

extendBy( (Box2d)arg1, (Box2d)arg2) -> None :
    extendBy(box) extend the box by a box

    C++ signature :
        void extendBy(Imath_3_1::Box<Imath_3_1::Vec2<double> > {lvalue},Imath_3_1::Box<Imath_3_1::Vec2<double> >)'''
    ...
    def hasVolume (self, *args, **kwargs):
      '''
hasVolume( (Box2d)arg1) -> bool :
    hasVolume() returns true if the box has volume

    C++ signature :
        bool hasVolume(Imath_3_1::Box<Imath_3_1::Vec2<double> > {lvalue})'''
    ...
    def intersects (self, *args, **kwargs):
      '''
intersects( (Box2d)arg1, (V2d)arg2) -> bool :
    intersects(point) returns true if the box intersects the given point

    C++ signature :
        bool intersects(Imath_3_1::Box<Imath_3_1::Vec2<double> > {lvalue},Imath_3_1::Vec2<double>)

intersects( (Box2d)arg1, (Box2d)arg2) -> bool :
    intersects(box) returns true if the box intersects the given box

    C++ signature :
        bool intersects(Imath_3_1::Box<Imath_3_1::Vec2<double> > {lvalue},Imath_3_1::Box<Imath_3_1::Vec2<double> >)'''
    ...
    def isEmpty (self, *args, **kwargs):
      '''
isEmpty( (Box2d)arg1) -> bool :
    isEmpty() returns true if the box is empty

    C++ signature :
        bool isEmpty(Imath_3_1::Box<Imath_3_1::Vec2<double> > {lvalue})'''
    ...
    def isInfinite (self, *args, **kwargs):
      '''
isInfinite( (Box2d)arg1) -> bool :
    isInfinite() returns true if the box covers all space

    C++ signature :
        bool isInfinite(Imath_3_1::Box<Imath_3_1::Vec2<double> > {lvalue})'''
    ...
    def majorAxis (self, *args, **kwargs):
      '''
majorAxis( (Box2d)arg1) -> int :
    majorAxis() major axis of the box

    C++ signature :
        unsigned int majorAxis(Imath_3_1::Box<Imath_3_1::Vec2<double> > {lvalue})'''
    ...
    def makeEmpty (self, *args, **kwargs):
      '''
makeEmpty( (Box2d)arg1) -> None :
    makeEmpty() make the box empty

    C++ signature :
        void makeEmpty(Imath_3_1::Box<Imath_3_1::Vec2<double> > {lvalue})'''
    ...
    def makeInfinite (self, *args, **kwargs):
      '''
makeInfinite( (Box2d)arg1) -> None :
    makeInfinite() make the box cover all space

    C++ signature :
        void makeInfinite(Imath_3_1::Box<Imath_3_1::Vec2<double> > {lvalue})'''
    ...
    def max (self, *args, **kwargs):
      '''
max( (Box2d)arg1) -> V2d :

    C++ signature :
        Imath_3_1::Vec2<double> max(Imath_3_1::Box<Imath_3_1::Vec2<double> > {lvalue})'''
    ...
    def min (self, *args, **kwargs):
      '''
min( (Box2d)arg1) -> V2d :

    C++ signature :
        Imath_3_1::Vec2<double> min(Imath_3_1::Box<Imath_3_1::Vec2<double> > {lvalue})'''
    ...
    def setMax (self, *args, **kwargs):
      '''
setMax( (Box2d)arg1, (V2d)arg2) -> None :
    setMax() sets the max value of the box

    C++ signature :
        void setMax(Imath_3_1::Box<Imath_3_1::Vec2<double> > {lvalue},Imath_3_1::Vec2<double>)'''
    ...
    def setMin (self, *args, **kwargs):
      '''
setMin( (Box2d)arg1, (V2d)arg2) -> None :
    setMin() sets the min value of the box

    C++ signature :
        void setMin(Imath_3_1::Box<Imath_3_1::Vec2<double> > {lvalue},Imath_3_1::Vec2<double>)'''
    ...
    def size (self, *args, **kwargs):
      '''
size( (Box2d)arg1) -> V2d :
    size() size of the box

    C++ signature :
        Imath_3_1::Vec2<double> size(Imath_3_1::Box<Imath_3_1::Vec2<double> > {lvalue})'''
    ...

def Box2dArray (*args):
      '''
__init__(_object*, Imath_3_1::Box<Imath_3_1::Vec2<double> >, unsigned long)
__init__(_object*, PyImath::FixedArray<Imath_3_1::Box<Imath_3_1::Vec2<double> > >)
__init__(_object*, unsigned long)

'''      
    ...

class Box2dArray:
    def ifelse (self, *args, **kwargs):
      '''
ifelse( (Box2dArray)arg1, (IntArray)arg2, (Box2d)arg3) -> Box2dArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Box<Imath_3_1::Vec2<double> > > ifelse(PyImath::FixedArray<Imath_3_1::Box<Imath_3_1::Vec2<double> > > {lvalue},PyImath::FixedArray<int>,Imath_3_1::Box<Imath_3_1::Vec2<double> >)

ifelse( (Box2dArray)arg1, (IntArray)arg2, (Box2dArray)arg3) -> Box2dArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Box<Imath_3_1::Vec2<double> > > ifelse(PyImath::FixedArray<Imath_3_1::Box<Imath_3_1::Vec2<double> > > {lvalue},PyImath::FixedArray<int>,PyImath::FixedArray<Imath_3_1::Box<Imath_3_1::Vec2<double> > >)'''
    ...
    def makeReadOnly (self, *args, **kwargs):
      '''
makeReadOnly( (Box2dArray)arg1) -> None :

    C++ signature :
        void makeReadOnly(PyImath::FixedArray<Imath_3_1::Box<Imath_3_1::Vec2<double> > > {lvalue})'''
    ...
    def max (self, *args, **kwargs):
      '''None'''
    ...
    def min (self, *args, **kwargs):
      '''None'''
    ...
    def writable (self, *args, **kwargs):
      '''
writable( (Box2dArray)arg1) -> bool :

    C++ signature :
        bool writable(PyImath::FixedArray<Imath_3_1::Box<Imath_3_1::Vec2<double> > > {lvalue})'''
    ...

def Box2f (*args):
      '''
__init__(boost::python::api::object, Imath_3_1::Box<Imath_3_1::Vec2<long> >)
__init__(boost::python::api::object, Imath_3_1::Box<Imath_3_1::Vec2<int> >)
__init__(boost::python::api::object, Imath_3_1::Box<Imath_3_1::Vec2<double> >)
__init__(boost::python::api::object, Imath_3_1::Box<Imath_3_1::Vec2<float> >)
__init__(boost::python::api::object, boost::python::tuple, boost::python::tuple)
__init__(boost::python::api::object, boost::python::tuple)
__init__(_object*, Imath_3_1::Vec2<float>, Imath_3_1::Vec2<float>)
__init__(_object*, Imath_3_1::Vec2<float>)
__init__(_object*)
__init__(_object*)

'''      
    ...

class Box2f:
    def center (self, *args, **kwargs):
      '''
center( (Box2f)arg1) -> V2f :
    center() center of the box

    C++ signature :
        Imath_3_1::Vec2<float> center(Imath_3_1::Box<Imath_3_1::Vec2<float> > {lvalue})'''
    ...
    def extendBy (self, *args, **kwargs):
      '''
extendBy( (Box2f)arg1, (V2f)arg2) -> None :
    extendBy(point) extend the box by a point

    C++ signature :
        void extendBy(Imath_3_1::Box<Imath_3_1::Vec2<float> > {lvalue},Imath_3_1::Vec2<float>)

extendBy( (Box2f)arg1, (V2fArray)arg2) -> None :
    extendBy(array) extend the box the values in the array

    C++ signature :
        void extendBy(Imath_3_1::Box<Imath_3_1::Vec2<float> > {lvalue},PyImath::FixedArray<Imath_3_1::Vec2<float> >)

extendBy( (Box2f)arg1, (Box2f)arg2) -> None :
    extendBy(box) extend the box by a box

    C++ signature :
        void extendBy(Imath_3_1::Box<Imath_3_1::Vec2<float> > {lvalue},Imath_3_1::Box<Imath_3_1::Vec2<float> >)'''
    ...
    def hasVolume (self, *args, **kwargs):
      '''
hasVolume( (Box2f)arg1) -> bool :
    hasVolume() returns true if the box has volume

    C++ signature :
        bool hasVolume(Imath_3_1::Box<Imath_3_1::Vec2<float> > {lvalue})'''
    ...
    def intersects (self, *args, **kwargs):
      '''
intersects( (Box2f)arg1, (V2f)arg2) -> bool :
    intersects(point) returns true if the box intersects the given point

    C++ signature :
        bool intersects(Imath_3_1::Box<Imath_3_1::Vec2<float> > {lvalue},Imath_3_1::Vec2<float>)

intersects( (Box2f)arg1, (Box2f)arg2) -> bool :
    intersects(box) returns true if the box intersects the given box

    C++ signature :
        bool intersects(Imath_3_1::Box<Imath_3_1::Vec2<float> > {lvalue},Imath_3_1::Box<Imath_3_1::Vec2<float> >)'''
    ...
    def isEmpty (self, *args, **kwargs):
      '''
isEmpty( (Box2f)arg1) -> bool :
    isEmpty() returns true if the box is empty

    C++ signature :
        bool isEmpty(Imath_3_1::Box<Imath_3_1::Vec2<float> > {lvalue})'''
    ...
    def isInfinite (self, *args, **kwargs):
      '''
isInfinite( (Box2f)arg1) -> bool :
    isInfinite() returns true if the box covers all space

    C++ signature :
        bool isInfinite(Imath_3_1::Box<Imath_3_1::Vec2<float> > {lvalue})'''
    ...
    def majorAxis (self, *args, **kwargs):
      '''
majorAxis( (Box2f)arg1) -> int :
    majorAxis() major axis of the box

    C++ signature :
        unsigned int majorAxis(Imath_3_1::Box<Imath_3_1::Vec2<float> > {lvalue})'''
    ...
    def makeEmpty (self, *args, **kwargs):
      '''
makeEmpty( (Box2f)arg1) -> None :
    makeEmpty() make the box empty

    C++ signature :
        void makeEmpty(Imath_3_1::Box<Imath_3_1::Vec2<float> > {lvalue})'''
    ...
    def makeInfinite (self, *args, **kwargs):
      '''
makeInfinite( (Box2f)arg1) -> None :
    makeInfinite() make the box cover all space

    C++ signature :
        void makeInfinite(Imath_3_1::Box<Imath_3_1::Vec2<float> > {lvalue})'''
    ...
    def max (self, *args, **kwargs):
      '''
max( (Box2f)arg1) -> V2f :

    C++ signature :
        Imath_3_1::Vec2<float> max(Imath_3_1::Box<Imath_3_1::Vec2<float> > {lvalue})'''
    ...
    def min (self, *args, **kwargs):
      '''
min( (Box2f)arg1) -> V2f :

    C++ signature :
        Imath_3_1::Vec2<float> min(Imath_3_1::Box<Imath_3_1::Vec2<float> > {lvalue})'''
    ...
    def setMax (self, *args, **kwargs):
      '''
setMax( (Box2f)arg1, (V2f)arg2) -> None :
    setMax() sets the max value of the box

    C++ signature :
        void setMax(Imath_3_1::Box<Imath_3_1::Vec2<float> > {lvalue},Imath_3_1::Vec2<float>)'''
    ...
    def setMin (self, *args, **kwargs):
      '''
setMin( (Box2f)arg1, (V2f)arg2) -> None :
    setMin() sets the min value of the box

    C++ signature :
        void setMin(Imath_3_1::Box<Imath_3_1::Vec2<float> > {lvalue},Imath_3_1::Vec2<float>)'''
    ...
    def size (self, *args, **kwargs):
      '''
size( (Box2f)arg1) -> V2f :
    size() size of the box

    C++ signature :
        Imath_3_1::Vec2<float> size(Imath_3_1::Box<Imath_3_1::Vec2<float> > {lvalue})'''
    ...

def Box2fArray (*args):
      '''
__init__(_object*, Imath_3_1::Box<Imath_3_1::Vec2<float> >, unsigned long)
__init__(_object*, PyImath::FixedArray<Imath_3_1::Box<Imath_3_1::Vec2<float> > >)
__init__(_object*, unsigned long)

'''      
    ...

class Box2fArray:
    def ifelse (self, *args, **kwargs):
      '''
ifelse( (Box2fArray)arg1, (IntArray)arg2, (Box2f)arg3) -> Box2fArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Box<Imath_3_1::Vec2<float> > > ifelse(PyImath::FixedArray<Imath_3_1::Box<Imath_3_1::Vec2<float> > > {lvalue},PyImath::FixedArray<int>,Imath_3_1::Box<Imath_3_1::Vec2<float> >)

ifelse( (Box2fArray)arg1, (IntArray)arg2, (Box2fArray)arg3) -> Box2fArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Box<Imath_3_1::Vec2<float> > > ifelse(PyImath::FixedArray<Imath_3_1::Box<Imath_3_1::Vec2<float> > > {lvalue},PyImath::FixedArray<int>,PyImath::FixedArray<Imath_3_1::Box<Imath_3_1::Vec2<float> > >)'''
    ...
    def makeReadOnly (self, *args, **kwargs):
      '''
makeReadOnly( (Box2fArray)arg1) -> None :

    C++ signature :
        void makeReadOnly(PyImath::FixedArray<Imath_3_1::Box<Imath_3_1::Vec2<float> > > {lvalue})'''
    ...
    def max (self, *args, **kwargs):
      '''None'''
    ...
    def min (self, *args, **kwargs):
      '''None'''
    ...
    def writable (self, *args, **kwargs):
      '''
writable( (Box2fArray)arg1) -> bool :

    C++ signature :
        bool writable(PyImath::FixedArray<Imath_3_1::Box<Imath_3_1::Vec2<float> > > {lvalue})'''
    ...

def Box2i (*args):
      '''
__init__(boost::python::api::object, Imath_3_1::Box<Imath_3_1::Vec2<long> >)
__init__(boost::python::api::object, Imath_3_1::Box<Imath_3_1::Vec2<int> >)
__init__(boost::python::api::object, Imath_3_1::Box<Imath_3_1::Vec2<double> >)
__init__(boost::python::api::object, Imath_3_1::Box<Imath_3_1::Vec2<float> >)
__init__(boost::python::api::object, boost::python::tuple, boost::python::tuple)
__init__(boost::python::api::object, boost::python::tuple)
__init__(_object*, Imath_3_1::Vec2<int>, Imath_3_1::Vec2<int>)
__init__(_object*, Imath_3_1::Vec2<int>)
__init__(_object*)
__init__(_object*)

'''      
    ...

class Box2i:
    def center (self, *args, **kwargs):
      '''
center( (Box2i)arg1) -> V2i :
    center() center of the box

    C++ signature :
        Imath_3_1::Vec2<int> center(Imath_3_1::Box<Imath_3_1::Vec2<int> > {lvalue})'''
    ...
    def extendBy (self, *args, **kwargs):
      '''
extendBy( (Box2i)arg1, (V2i)arg2) -> None :
    extendBy(point) extend the box by a point

    C++ signature :
        void extendBy(Imath_3_1::Box<Imath_3_1::Vec2<int> > {lvalue},Imath_3_1::Vec2<int>)

extendBy( (Box2i)arg1, (V2iArray)arg2) -> None :
    extendBy(array) extend the box the values in the array

    C++ signature :
        void extendBy(Imath_3_1::Box<Imath_3_1::Vec2<int> > {lvalue},PyImath::FixedArray<Imath_3_1::Vec2<int> >)

extendBy( (Box2i)arg1, (Box2i)arg2) -> None :
    extendBy(box) extend the box by a box

    C++ signature :
        void extendBy(Imath_3_1::Box<Imath_3_1::Vec2<int> > {lvalue},Imath_3_1::Box<Imath_3_1::Vec2<int> >)'''
    ...
    def hasVolume (self, *args, **kwargs):
      '''
hasVolume( (Box2i)arg1) -> bool :
    hasVolume() returns true if the box has volume

    C++ signature :
        bool hasVolume(Imath_3_1::Box<Imath_3_1::Vec2<int> > {lvalue})'''
    ...
    def intersects (self, *args, **kwargs):
      '''
intersects( (Box2i)arg1, (V2i)arg2) -> bool :
    intersects(point) returns true if the box intersects the given point

    C++ signature :
        bool intersects(Imath_3_1::Box<Imath_3_1::Vec2<int> > {lvalue},Imath_3_1::Vec2<int>)

intersects( (Box2i)arg1, (Box2i)arg2) -> bool :
    intersects(box) returns true if the box intersects the given box

    C++ signature :
        bool intersects(Imath_3_1::Box<Imath_3_1::Vec2<int> > {lvalue},Imath_3_1::Box<Imath_3_1::Vec2<int> >)'''
    ...
    def isEmpty (self, *args, **kwargs):
      '''
isEmpty( (Box2i)arg1) -> bool :
    isEmpty() returns true if the box is empty

    C++ signature :
        bool isEmpty(Imath_3_1::Box<Imath_3_1::Vec2<int> > {lvalue})'''
    ...
    def isInfinite (self, *args, **kwargs):
      '''
isInfinite( (Box2i)arg1) -> bool :
    isInfinite() returns true if the box covers all space

    C++ signature :
        bool isInfinite(Imath_3_1::Box<Imath_3_1::Vec2<int> > {lvalue})'''
    ...
    def majorAxis (self, *args, **kwargs):
      '''
majorAxis( (Box2i)arg1) -> int :
    majorAxis() major axis of the box

    C++ signature :
        unsigned int majorAxis(Imath_3_1::Box<Imath_3_1::Vec2<int> > {lvalue})'''
    ...
    def makeEmpty (self, *args, **kwargs):
      '''
makeEmpty( (Box2i)arg1) -> None :
    makeEmpty() make the box empty

    C++ signature :
        void makeEmpty(Imath_3_1::Box<Imath_3_1::Vec2<int> > {lvalue})'''
    ...
    def makeInfinite (self, *args, **kwargs):
      '''
makeInfinite( (Box2i)arg1) -> None :
    makeInfinite() make the box cover all space

    C++ signature :
        void makeInfinite(Imath_3_1::Box<Imath_3_1::Vec2<int> > {lvalue})'''
    ...
    def max (self, *args, **kwargs):
      '''
max( (Box2i)arg1) -> V2i :

    C++ signature :
        Imath_3_1::Vec2<int> max(Imath_3_1::Box<Imath_3_1::Vec2<int> > {lvalue})'''
    ...
    def min (self, *args, **kwargs):
      '''
min( (Box2i)arg1) -> V2i :

    C++ signature :
        Imath_3_1::Vec2<int> min(Imath_3_1::Box<Imath_3_1::Vec2<int> > {lvalue})'''
    ...
    def setMax (self, *args, **kwargs):
      '''
setMax( (Box2i)arg1, (V2i)arg2) -> None :
    setMax() sets the max value of the box

    C++ signature :
        void setMax(Imath_3_1::Box<Imath_3_1::Vec2<int> > {lvalue},Imath_3_1::Vec2<int>)'''
    ...
    def setMin (self, *args, **kwargs):
      '''
setMin( (Box2i)arg1, (V2i)arg2) -> None :
    setMin() sets the min value of the box

    C++ signature :
        void setMin(Imath_3_1::Box<Imath_3_1::Vec2<int> > {lvalue},Imath_3_1::Vec2<int>)'''
    ...
    def size (self, *args, **kwargs):
      '''
size( (Box2i)arg1) -> V2i :
    size() size of the box

    C++ signature :
        Imath_3_1::Vec2<int> size(Imath_3_1::Box<Imath_3_1::Vec2<int> > {lvalue})'''
    ...

def Box2i64 (*args):
      '''
__init__(boost::python::api::object, Imath_3_1::Box<Imath_3_1::Vec2<long> >)
__init__(boost::python::api::object, Imath_3_1::Box<Imath_3_1::Vec2<int> >)
__init__(boost::python::api::object, Imath_3_1::Box<Imath_3_1::Vec2<double> >)
__init__(boost::python::api::object, Imath_3_1::Box<Imath_3_1::Vec2<float> >)
__init__(boost::python::api::object, boost::python::tuple, boost::python::tuple)
__init__(boost::python::api::object, boost::python::tuple)
__init__(_object*, Imath_3_1::Vec2<long>, Imath_3_1::Vec2<long>)
__init__(_object*, Imath_3_1::Vec2<long>)
__init__(_object*)
__init__(_object*)

'''      
    ...

class Box2i64:
    def center (self, *args, **kwargs):
      '''
center( (Box2i64)arg1) -> V2i64 :
    center() center of the box

    C++ signature :
        Imath_3_1::Vec2<long> center(Imath_3_1::Box<Imath_3_1::Vec2<long> > {lvalue})'''
    ...
    def extendBy (self, *args, **kwargs):
      '''
extendBy( (Box2i64)arg1, (V2i64)arg2) -> None :
    extendBy(point) extend the box by a point

    C++ signature :
        void extendBy(Imath_3_1::Box<Imath_3_1::Vec2<long> > {lvalue},Imath_3_1::Vec2<long>)

extendBy( (Box2i64)arg1, (V2i64Array)arg2) -> None :
    extendBy(array) extend the box the values in the array

    C++ signature :
        void extendBy(Imath_3_1::Box<Imath_3_1::Vec2<long> > {lvalue},PyImath::FixedArray<Imath_3_1::Vec2<long> >)

extendBy( (Box2i64)arg1, (Box2i64)arg2) -> None :
    extendBy(box) extend the box by a box

    C++ signature :
        void extendBy(Imath_3_1::Box<Imath_3_1::Vec2<long> > {lvalue},Imath_3_1::Box<Imath_3_1::Vec2<long> >)'''
    ...
    def hasVolume (self, *args, **kwargs):
      '''
hasVolume( (Box2i64)arg1) -> bool :
    hasVolume() returns true if the box has volume

    C++ signature :
        bool hasVolume(Imath_3_1::Box<Imath_3_1::Vec2<long> > {lvalue})'''
    ...
    def intersects (self, *args, **kwargs):
      '''
intersects( (Box2i64)arg1, (V2i64)arg2) -> bool :
    intersects(point) returns true if the box intersects the given point

    C++ signature :
        bool intersects(Imath_3_1::Box<Imath_3_1::Vec2<long> > {lvalue},Imath_3_1::Vec2<long>)

intersects( (Box2i64)arg1, (Box2i64)arg2) -> bool :
    intersects(box) returns true if the box intersects the given box

    C++ signature :
        bool intersects(Imath_3_1::Box<Imath_3_1::Vec2<long> > {lvalue},Imath_3_1::Box<Imath_3_1::Vec2<long> >)'''
    ...
    def isEmpty (self, *args, **kwargs):
      '''
isEmpty( (Box2i64)arg1) -> bool :
    isEmpty() returns true if the box is empty

    C++ signature :
        bool isEmpty(Imath_3_1::Box<Imath_3_1::Vec2<long> > {lvalue})'''
    ...
    def isInfinite (self, *args, **kwargs):
      '''
isInfinite( (Box2i64)arg1) -> bool :
    isInfinite() returns true if the box covers all space

    C++ signature :
        bool isInfinite(Imath_3_1::Box<Imath_3_1::Vec2<long> > {lvalue})'''
    ...
    def majorAxis (self, *args, **kwargs):
      '''
majorAxis( (Box2i64)arg1) -> int :
    majorAxis() major axis of the box

    C++ signature :
        unsigned int majorAxis(Imath_3_1::Box<Imath_3_1::Vec2<long> > {lvalue})'''
    ...
    def makeEmpty (self, *args, **kwargs):
      '''
makeEmpty( (Box2i64)arg1) -> None :
    makeEmpty() make the box empty

    C++ signature :
        void makeEmpty(Imath_3_1::Box<Imath_3_1::Vec2<long> > {lvalue})'''
    ...
    def makeInfinite (self, *args, **kwargs):
      '''
makeInfinite( (Box2i64)arg1) -> None :
    makeInfinite() make the box cover all space

    C++ signature :
        void makeInfinite(Imath_3_1::Box<Imath_3_1::Vec2<long> > {lvalue})'''
    ...
    def max (self, *args, **kwargs):
      '''
max( (Box2i64)arg1) -> V2i64 :

    C++ signature :
        Imath_3_1::Vec2<long> max(Imath_3_1::Box<Imath_3_1::Vec2<long> > {lvalue})'''
    ...
    def min (self, *args, **kwargs):
      '''
min( (Box2i64)arg1) -> V2i64 :

    C++ signature :
        Imath_3_1::Vec2<long> min(Imath_3_1::Box<Imath_3_1::Vec2<long> > {lvalue})'''
    ...
    def setMax (self, *args, **kwargs):
      '''
setMax( (Box2i64)arg1, (V2i64)arg2) -> None :
    setMax() sets the max value of the box

    C++ signature :
        void setMax(Imath_3_1::Box<Imath_3_1::Vec2<long> > {lvalue},Imath_3_1::Vec2<long>)'''
    ...
    def setMin (self, *args, **kwargs):
      '''
setMin( (Box2i64)arg1, (V2i64)arg2) -> None :
    setMin() sets the min value of the box

    C++ signature :
        void setMin(Imath_3_1::Box<Imath_3_1::Vec2<long> > {lvalue},Imath_3_1::Vec2<long>)'''
    ...
    def size (self, *args, **kwargs):
      '''
size( (Box2i64)arg1) -> V2i64 :
    size() size of the box

    C++ signature :
        Imath_3_1::Vec2<long> size(Imath_3_1::Box<Imath_3_1::Vec2<long> > {lvalue})'''
    ...

def Box2i64Array (*args):
      '''
__init__(_object*, Imath_3_1::Box<Imath_3_1::Vec2<long> >, unsigned long)
__init__(_object*, PyImath::FixedArray<Imath_3_1::Box<Imath_3_1::Vec2<long> > >)
__init__(_object*, unsigned long)

'''      
    ...

class Box2i64Array:
    def ifelse (self, *args, **kwargs):
      '''
ifelse( (Box2i64Array)arg1, (IntArray)arg2, (Box2i64)arg3) -> Box2i64Array :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Box<Imath_3_1::Vec2<long> > > ifelse(PyImath::FixedArray<Imath_3_1::Box<Imath_3_1::Vec2<long> > > {lvalue},PyImath::FixedArray<int>,Imath_3_1::Box<Imath_3_1::Vec2<long> >)

ifelse( (Box2i64Array)arg1, (IntArray)arg2, (Box2i64Array)arg3) -> Box2i64Array :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Box<Imath_3_1::Vec2<long> > > ifelse(PyImath::FixedArray<Imath_3_1::Box<Imath_3_1::Vec2<long> > > {lvalue},PyImath::FixedArray<int>,PyImath::FixedArray<Imath_3_1::Box<Imath_3_1::Vec2<long> > >)'''
    ...
    def makeReadOnly (self, *args, **kwargs):
      '''
makeReadOnly( (Box2i64Array)arg1) -> None :

    C++ signature :
        void makeReadOnly(PyImath::FixedArray<Imath_3_1::Box<Imath_3_1::Vec2<long> > > {lvalue})'''
    ...
    def max (self, *args, **kwargs):
      '''None'''
    ...
    def min (self, *args, **kwargs):
      '''None'''
    ...
    def writable (self, *args, **kwargs):
      '''
writable( (Box2i64Array)arg1) -> bool :

    C++ signature :
        bool writable(PyImath::FixedArray<Imath_3_1::Box<Imath_3_1::Vec2<long> > > {lvalue})'''
    ...

def Box2iArray (*args):
      '''
__init__(_object*, Imath_3_1::Box<Imath_3_1::Vec2<int> >, unsigned long)
__init__(_object*, PyImath::FixedArray<Imath_3_1::Box<Imath_3_1::Vec2<int> > >)
__init__(_object*, unsigned long)

'''      
    ...

class Box2iArray:
    def ifelse (self, *args, **kwargs):
      '''
ifelse( (Box2iArray)arg1, (IntArray)arg2, (Box2i)arg3) -> Box2iArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Box<Imath_3_1::Vec2<int> > > ifelse(PyImath::FixedArray<Imath_3_1::Box<Imath_3_1::Vec2<int> > > {lvalue},PyImath::FixedArray<int>,Imath_3_1::Box<Imath_3_1::Vec2<int> >)

ifelse( (Box2iArray)arg1, (IntArray)arg2, (Box2iArray)arg3) -> Box2iArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Box<Imath_3_1::Vec2<int> > > ifelse(PyImath::FixedArray<Imath_3_1::Box<Imath_3_1::Vec2<int> > > {lvalue},PyImath::FixedArray<int>,PyImath::FixedArray<Imath_3_1::Box<Imath_3_1::Vec2<int> > >)'''
    ...
    def makeReadOnly (self, *args, **kwargs):
      '''
makeReadOnly( (Box2iArray)arg1) -> None :

    C++ signature :
        void makeReadOnly(PyImath::FixedArray<Imath_3_1::Box<Imath_3_1::Vec2<int> > > {lvalue})'''
    ...
    def max (self, *args, **kwargs):
      '''None'''
    ...
    def min (self, *args, **kwargs):
      '''None'''
    ...
    def writable (self, *args, **kwargs):
      '''
writable( (Box2iArray)arg1) -> bool :

    C++ signature :
        bool writable(PyImath::FixedArray<Imath_3_1::Box<Imath_3_1::Vec2<int> > > {lvalue})'''
    ...

def Box2s (*args):
      '''
__init__(boost::python::api::object, Imath_3_1::Box<Imath_3_1::Vec2<long> >)
__init__(boost::python::api::object, Imath_3_1::Box<Imath_3_1::Vec2<int> >)
__init__(boost::python::api::object, Imath_3_1::Box<Imath_3_1::Vec2<double> >)
__init__(boost::python::api::object, Imath_3_1::Box<Imath_3_1::Vec2<float> >)
__init__(boost::python::api::object, boost::python::tuple, boost::python::tuple)
__init__(boost::python::api::object, boost::python::tuple)
__init__(_object*, Imath_3_1::Vec2<short>, Imath_3_1::Vec2<short>)
__init__(_object*, Imath_3_1::Vec2<short>)
__init__(_object*)
__init__(_object*)

'''      
    ...

class Box2s:
    def center (self, *args, **kwargs):
      '''
center( (Box2s)arg1) -> V2s :
    center() center of the box

    C++ signature :
        Imath_3_1::Vec2<short> center(Imath_3_1::Box<Imath_3_1::Vec2<short> > {lvalue})'''
    ...
    def extendBy (self, *args, **kwargs):
      '''
extendBy( (Box2s)arg1, (V2s)arg2) -> None :
    extendBy(point) extend the box by a point

    C++ signature :
        void extendBy(Imath_3_1::Box<Imath_3_1::Vec2<short> > {lvalue},Imath_3_1::Vec2<short>)

extendBy( (Box2s)arg1, (V2sArray)arg2) -> None :
    extendBy(array) extend the box the values in the array

    C++ signature :
        void extendBy(Imath_3_1::Box<Imath_3_1::Vec2<short> > {lvalue},PyImath::FixedArray<Imath_3_1::Vec2<short> >)

extendBy( (Box2s)arg1, (Box2s)arg2) -> None :
    extendBy(box) extend the box by a box

    C++ signature :
        void extendBy(Imath_3_1::Box<Imath_3_1::Vec2<short> > {lvalue},Imath_3_1::Box<Imath_3_1::Vec2<short> >)'''
    ...
    def hasVolume (self, *args, **kwargs):
      '''
hasVolume( (Box2s)arg1) -> bool :
    hasVolume() returns true if the box has volume

    C++ signature :
        bool hasVolume(Imath_3_1::Box<Imath_3_1::Vec2<short> > {lvalue})'''
    ...
    def intersects (self, *args, **kwargs):
      '''
intersects( (Box2s)arg1, (V2s)arg2) -> bool :
    intersects(point) returns true if the box intersects the given point

    C++ signature :
        bool intersects(Imath_3_1::Box<Imath_3_1::Vec2<short> > {lvalue},Imath_3_1::Vec2<short>)

intersects( (Box2s)arg1, (Box2s)arg2) -> bool :
    intersects(box) returns true if the box intersects the given box

    C++ signature :
        bool intersects(Imath_3_1::Box<Imath_3_1::Vec2<short> > {lvalue},Imath_3_1::Box<Imath_3_1::Vec2<short> >)'''
    ...
    def isEmpty (self, *args, **kwargs):
      '''
isEmpty( (Box2s)arg1) -> bool :
    isEmpty() returns true if the box is empty

    C++ signature :
        bool isEmpty(Imath_3_1::Box<Imath_3_1::Vec2<short> > {lvalue})'''
    ...
    def isInfinite (self, *args, **kwargs):
      '''
isInfinite( (Box2s)arg1) -> bool :
    isInfinite() returns true if the box covers all space

    C++ signature :
        bool isInfinite(Imath_3_1::Box<Imath_3_1::Vec2<short> > {lvalue})'''
    ...
    def majorAxis (self, *args, **kwargs):
      '''
majorAxis( (Box2s)arg1) -> int :
    majorAxis() major axis of the box

    C++ signature :
        unsigned int majorAxis(Imath_3_1::Box<Imath_3_1::Vec2<short> > {lvalue})'''
    ...
    def makeEmpty (self, *args, **kwargs):
      '''
makeEmpty( (Box2s)arg1) -> None :
    makeEmpty() make the box empty

    C++ signature :
        void makeEmpty(Imath_3_1::Box<Imath_3_1::Vec2<short> > {lvalue})'''
    ...
    def makeInfinite (self, *args, **kwargs):
      '''
makeInfinite( (Box2s)arg1) -> None :
    makeInfinite() make the box cover all space

    C++ signature :
        void makeInfinite(Imath_3_1::Box<Imath_3_1::Vec2<short> > {lvalue})'''
    ...
    def max (self, *args, **kwargs):
      '''
max( (Box2s)arg1) -> V2s :

    C++ signature :
        Imath_3_1::Vec2<short> max(Imath_3_1::Box<Imath_3_1::Vec2<short> > {lvalue})'''
    ...
    def min (self, *args, **kwargs):
      '''
min( (Box2s)arg1) -> V2s :

    C++ signature :
        Imath_3_1::Vec2<short> min(Imath_3_1::Box<Imath_3_1::Vec2<short> > {lvalue})'''
    ...
    def setMax (self, *args, **kwargs):
      '''
setMax( (Box2s)arg1, (V2s)arg2) -> None :
    setMax() sets the max value of the box

    C++ signature :
        void setMax(Imath_3_1::Box<Imath_3_1::Vec2<short> > {lvalue},Imath_3_1::Vec2<short>)'''
    ...
    def setMin (self, *args, **kwargs):
      '''
setMin( (Box2s)arg1, (V2s)arg2) -> None :
    setMin() sets the min value of the box

    C++ signature :
        void setMin(Imath_3_1::Box<Imath_3_1::Vec2<short> > {lvalue},Imath_3_1::Vec2<short>)'''
    ...
    def size (self, *args, **kwargs):
      '''
size( (Box2s)arg1) -> V2s :
    size() size of the box

    C++ signature :
        Imath_3_1::Vec2<short> size(Imath_3_1::Box<Imath_3_1::Vec2<short> > {lvalue})'''
    ...

def Box2sArray (*args):
      '''
__init__(_object*, Imath_3_1::Box<Imath_3_1::Vec2<short> >, unsigned long)
__init__(_object*, PyImath::FixedArray<Imath_3_1::Box<Imath_3_1::Vec2<short> > >)
__init__(_object*, unsigned long)

'''      
    ...

class Box2sArray:
    def ifelse (self, *args, **kwargs):
      '''
ifelse( (Box2sArray)arg1, (IntArray)arg2, (Box2s)arg3) -> Box2sArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Box<Imath_3_1::Vec2<short> > > ifelse(PyImath::FixedArray<Imath_3_1::Box<Imath_3_1::Vec2<short> > > {lvalue},PyImath::FixedArray<int>,Imath_3_1::Box<Imath_3_1::Vec2<short> >)

ifelse( (Box2sArray)arg1, (IntArray)arg2, (Box2sArray)arg3) -> Box2sArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Box<Imath_3_1::Vec2<short> > > ifelse(PyImath::FixedArray<Imath_3_1::Box<Imath_3_1::Vec2<short> > > {lvalue},PyImath::FixedArray<int>,PyImath::FixedArray<Imath_3_1::Box<Imath_3_1::Vec2<short> > >)'''
    ...
    def makeReadOnly (self, *args, **kwargs):
      '''
makeReadOnly( (Box2sArray)arg1) -> None :

    C++ signature :
        void makeReadOnly(PyImath::FixedArray<Imath_3_1::Box<Imath_3_1::Vec2<short> > > {lvalue})'''
    ...
    def max (self, *args, **kwargs):
      '''None'''
    ...
    def min (self, *args, **kwargs):
      '''None'''
    ...
    def writable (self, *args, **kwargs):
      '''
writable( (Box2sArray)arg1) -> bool :

    C++ signature :
        bool writable(PyImath::FixedArray<Imath_3_1::Box<Imath_3_1::Vec2<short> > > {lvalue})'''
    ...

def Box3d (*args):
      '''
__init__(boost::python::api::object, Imath_3_1::Box<Imath_3_1::Vec3<long> >)
__init__(boost::python::api::object, Imath_3_1::Box<Imath_3_1::Vec3<int> >)
__init__(boost::python::api::object, Imath_3_1::Box<Imath_3_1::Vec3<double> >)
__init__(boost::python::api::object, Imath_3_1::Box<Imath_3_1::Vec3<float> >)
__init__(boost::python::api::object, boost::python::tuple, boost::python::tuple)
__init__(boost::python::api::object, boost::python::tuple)
__init__(_object*, Imath_3_1::Vec3<double>, Imath_3_1::Vec3<double>)
__init__(_object*, Imath_3_1::Vec3<double>)
__init__(_object*)
__init__(_object*)

'''      
    ...

class Box3d:
    def center (self, *args, **kwargs):
      '''
center( (Box3d)arg1) -> V3d :
    center() center of the box

    C++ signature :
        Imath_3_1::Vec3<double> center(Imath_3_1::Box<Imath_3_1::Vec3<double> > {lvalue})'''
    ...
    def extendBy (self, *args, **kwargs):
      '''
extendBy( (Box3d)arg1, (V3d)arg2) -> None :
    extendBy(point) extend the box by a point

    C++ signature :
        void extendBy(Imath_3_1::Box<Imath_3_1::Vec3<double> > {lvalue},Imath_3_1::Vec3<double>)

extendBy( (Box3d)arg1, (V3dArray)arg2) -> None :
    extendBy(array) extend the box the values in the array

    C++ signature :
        void extendBy(Imath_3_1::Box<Imath_3_1::Vec3<double> > {lvalue},PyImath::FixedArray<Imath_3_1::Vec3<double> >)

extendBy( (Box3d)arg1, (Box3d)arg2) -> None :
    extendBy(box) extend the box by a box

    C++ signature :
        void extendBy(Imath_3_1::Box<Imath_3_1::Vec3<double> > {lvalue},Imath_3_1::Box<Imath_3_1::Vec3<double> >)'''
    ...
    def hasVolume (self, *args, **kwargs):
      '''
hasVolume( (Box3d)arg1) -> bool :
    hasVolume() returns true if the box has volume

    C++ signature :
        bool hasVolume(Imath_3_1::Box<Imath_3_1::Vec3<double> > {lvalue})'''
    ...
    def intersects (self, *args, **kwargs):
      '''
intersects( (Box3d)arg1, (V3d)arg2) -> bool :
    intersects(point) returns true if the box intersects the given point

    C++ signature :
        bool intersects(Imath_3_1::Box<Imath_3_1::Vec3<double> > {lvalue},Imath_3_1::Vec3<double>)

intersects( (Box3d)arg1, (Box3d)arg2) -> bool :
    intersects(box) returns true if the box intersects the given box

    C++ signature :
        bool intersects(Imath_3_1::Box<Imath_3_1::Vec3<double> > {lvalue},Imath_3_1::Box<Imath_3_1::Vec3<double> >)

intersects( (Box3d)arg1, (V3dArray)arg2) -> IntArray :
    intersects(array) returns an int array where 0 indicates the point is not in the box and 1 indicates that it is

    C++ signature :
        PyImath::FixedArray<int> intersects(Imath_3_1::Box<Imath_3_1::Vec3<double> > {lvalue},PyImath::FixedArray<Imath_3_1::Vec3<double> >)'''
    ...
    def isEmpty (self, *args, **kwargs):
      '''
isEmpty( (Box3d)arg1) -> bool :
    isEmpty() returns true if the box is empty

    C++ signature :
        bool isEmpty(Imath_3_1::Box<Imath_3_1::Vec3<double> > {lvalue})'''
    ...
    def isInfinite (self, *args, **kwargs):
      '''
isInfinite( (Box3d)arg1) -> bool :
    isInfinite() returns true if the box covers all space

    C++ signature :
        bool isInfinite(Imath_3_1::Box<Imath_3_1::Vec3<double> > {lvalue})'''
    ...
    def majorAxis (self, *args, **kwargs):
      '''
majorAxis( (Box3d)arg1) -> int :
    majorAxis() major axis of the box

    C++ signature :
        unsigned int majorAxis(Imath_3_1::Box<Imath_3_1::Vec3<double> > {lvalue})'''
    ...
    def makeEmpty (self, *args, **kwargs):
      '''
makeEmpty( (Box3d)arg1) -> None :
    makeEmpty() make the box empty

    C++ signature :
        void makeEmpty(Imath_3_1::Box<Imath_3_1::Vec3<double> > {lvalue})'''
    ...
    def makeInfinite (self, *args, **kwargs):
      '''
makeInfinite( (Box3d)arg1) -> None :
    makeInfinite() make the box cover all space

    C++ signature :
        void makeInfinite(Imath_3_1::Box<Imath_3_1::Vec3<double> > {lvalue})'''
    ...
    def max (self, *args, **kwargs):
      '''
max( (Box3d)arg1) -> V3d :

    C++ signature :
        Imath_3_1::Vec3<double> max(Imath_3_1::Box<Imath_3_1::Vec3<double> > {lvalue})'''
    ...
    def min (self, *args, **kwargs):
      '''
min( (Box3d)arg1) -> V3d :

    C++ signature :
        Imath_3_1::Vec3<double> min(Imath_3_1::Box<Imath_3_1::Vec3<double> > {lvalue})'''
    ...
    def setMax (self, *args, **kwargs):
      '''
setMax( (Box3d)arg1, (V3d)arg2) -> None :
    setMax() sets the max value of the box

    C++ signature :
        void setMax(Imath_3_1::Box<Imath_3_1::Vec3<double> > {lvalue},Imath_3_1::Vec3<double>)'''
    ...
    def setMin (self, *args, **kwargs):
      '''
setMin( (Box3d)arg1, (V3d)arg2) -> None :
    setMin() sets the min value of the box

    C++ signature :
        void setMin(Imath_3_1::Box<Imath_3_1::Vec3<double> > {lvalue},Imath_3_1::Vec3<double>)'''
    ...
    def size (self, *args, **kwargs):
      '''
size( (Box3d)arg1) -> V3d :
    size() size of the box

    C++ signature :
        Imath_3_1::Vec3<double> size(Imath_3_1::Box<Imath_3_1::Vec3<double> > {lvalue})'''
    ...

def Box3dArray (*args):
      '''
__init__(_object*, Imath_3_1::Box<Imath_3_1::Vec3<double> >, unsigned long)
__init__(_object*, PyImath::FixedArray<Imath_3_1::Box<Imath_3_1::Vec3<double> > >)
__init__(_object*, unsigned long)

'''      
    ...

class Box3dArray:
    def ifelse (self, *args, **kwargs):
      '''
ifelse( (Box3dArray)arg1, (IntArray)arg2, (Box3d)arg3) -> Box3dArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Box<Imath_3_1::Vec3<double> > > ifelse(PyImath::FixedArray<Imath_3_1::Box<Imath_3_1::Vec3<double> > > {lvalue},PyImath::FixedArray<int>,Imath_3_1::Box<Imath_3_1::Vec3<double> >)

ifelse( (Box3dArray)arg1, (IntArray)arg2, (Box3dArray)arg3) -> Box3dArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Box<Imath_3_1::Vec3<double> > > ifelse(PyImath::FixedArray<Imath_3_1::Box<Imath_3_1::Vec3<double> > > {lvalue},PyImath::FixedArray<int>,PyImath::FixedArray<Imath_3_1::Box<Imath_3_1::Vec3<double> > >)'''
    ...
    def makeReadOnly (self, *args, **kwargs):
      '''
makeReadOnly( (Box3dArray)arg1) -> None :

    C++ signature :
        void makeReadOnly(PyImath::FixedArray<Imath_3_1::Box<Imath_3_1::Vec3<double> > > {lvalue})'''
    ...
    def max (self, *args, **kwargs):
      '''None'''
    ...
    def min (self, *args, **kwargs):
      '''None'''
    ...
    def writable (self, *args, **kwargs):
      '''
writable( (Box3dArray)arg1) -> bool :

    C++ signature :
        bool writable(PyImath::FixedArray<Imath_3_1::Box<Imath_3_1::Vec3<double> > > {lvalue})'''
    ...

def Box3f (*args):
      '''
__init__(boost::python::api::object, Imath_3_1::Box<Imath_3_1::Vec3<long> >)
__init__(boost::python::api::object, Imath_3_1::Box<Imath_3_1::Vec3<int> >)
__init__(boost::python::api::object, Imath_3_1::Box<Imath_3_1::Vec3<double> >)
__init__(boost::python::api::object, Imath_3_1::Box<Imath_3_1::Vec3<float> >)
__init__(boost::python::api::object, boost::python::tuple, boost::python::tuple)
__init__(boost::python::api::object, boost::python::tuple)
__init__(_object*, Imath_3_1::Vec3<float>, Imath_3_1::Vec3<float>)
__init__(_object*, Imath_3_1::Vec3<float>)
__init__(_object*)
__init__(_object*)

'''      
    ...

class Box3f:
    def center (self, *args, **kwargs):
      '''
center( (Box3f)arg1) -> V3f :
    center() center of the box

    C++ signature :
        Imath_3_1::Vec3<float> center(Imath_3_1::Box<Imath_3_1::Vec3<float> > {lvalue})'''
    ...
    def extendBy (self, *args, **kwargs):
      '''
extendBy( (Box3f)arg1, (V3f)arg2) -> None :
    extendBy(point) extend the box by a point

    C++ signature :
        void extendBy(Imath_3_1::Box<Imath_3_1::Vec3<float> > {lvalue},Imath_3_1::Vec3<float>)

extendBy( (Box3f)arg1, (V3fArray)arg2) -> None :
    extendBy(array) extend the box the values in the array

    C++ signature :
        void extendBy(Imath_3_1::Box<Imath_3_1::Vec3<float> > {lvalue},PyImath::FixedArray<Imath_3_1::Vec3<float> >)

extendBy( (Box3f)arg1, (Box3f)arg2) -> None :
    extendBy(box) extend the box by a box

    C++ signature :
        void extendBy(Imath_3_1::Box<Imath_3_1::Vec3<float> > {lvalue},Imath_3_1::Box<Imath_3_1::Vec3<float> >)'''
    ...
    def hasVolume (self, *args, **kwargs):
      '''
hasVolume( (Box3f)arg1) -> bool :
    hasVolume() returns true if the box has volume

    C++ signature :
        bool hasVolume(Imath_3_1::Box<Imath_3_1::Vec3<float> > {lvalue})'''
    ...
    def intersects (self, *args, **kwargs):
      '''
intersects( (Box3f)arg1, (V3f)arg2) -> bool :
    intersects(point) returns true if the box intersects the given point

    C++ signature :
        bool intersects(Imath_3_1::Box<Imath_3_1::Vec3<float> > {lvalue},Imath_3_1::Vec3<float>)

intersects( (Box3f)arg1, (Box3f)arg2) -> bool :
    intersects(box) returns true if the box intersects the given box

    C++ signature :
        bool intersects(Imath_3_1::Box<Imath_3_1::Vec3<float> > {lvalue},Imath_3_1::Box<Imath_3_1::Vec3<float> >)

intersects( (Box3f)arg1, (V3fArray)arg2) -> IntArray :
    intersects(array) returns an int array where 0 indicates the point is not in the box and 1 indicates that it is

    C++ signature :
        PyImath::FixedArray<int> intersects(Imath_3_1::Box<Imath_3_1::Vec3<float> > {lvalue},PyImath::FixedArray<Imath_3_1::Vec3<float> >)'''
    ...
    def isEmpty (self, *args, **kwargs):
      '''
isEmpty( (Box3f)arg1) -> bool :
    isEmpty() returns true if the box is empty

    C++ signature :
        bool isEmpty(Imath_3_1::Box<Imath_3_1::Vec3<float> > {lvalue})'''
    ...
    def isInfinite (self, *args, **kwargs):
      '''
isInfinite( (Box3f)arg1) -> bool :
    isInfinite() returns true if the box covers all space

    C++ signature :
        bool isInfinite(Imath_3_1::Box<Imath_3_1::Vec3<float> > {lvalue})'''
    ...
    def majorAxis (self, *args, **kwargs):
      '''
majorAxis( (Box3f)arg1) -> int :
    majorAxis() major axis of the box

    C++ signature :
        unsigned int majorAxis(Imath_3_1::Box<Imath_3_1::Vec3<float> > {lvalue})'''
    ...
    def makeEmpty (self, *args, **kwargs):
      '''
makeEmpty( (Box3f)arg1) -> None :
    makeEmpty() make the box empty

    C++ signature :
        void makeEmpty(Imath_3_1::Box<Imath_3_1::Vec3<float> > {lvalue})'''
    ...
    def makeInfinite (self, *args, **kwargs):
      '''
makeInfinite( (Box3f)arg1) -> None :
    makeInfinite() make the box cover all space

    C++ signature :
        void makeInfinite(Imath_3_1::Box<Imath_3_1::Vec3<float> > {lvalue})'''
    ...
    def max (self, *args, **kwargs):
      '''
max( (Box3f)arg1) -> V3f :

    C++ signature :
        Imath_3_1::Vec3<float> max(Imath_3_1::Box<Imath_3_1::Vec3<float> > {lvalue})'''
    ...
    def min (self, *args, **kwargs):
      '''
min( (Box3f)arg1) -> V3f :

    C++ signature :
        Imath_3_1::Vec3<float> min(Imath_3_1::Box<Imath_3_1::Vec3<float> > {lvalue})'''
    ...
    def setMax (self, *args, **kwargs):
      '''
setMax( (Box3f)arg1, (V3f)arg2) -> None :
    setMax() sets the max value of the box

    C++ signature :
        void setMax(Imath_3_1::Box<Imath_3_1::Vec3<float> > {lvalue},Imath_3_1::Vec3<float>)'''
    ...
    def setMin (self, *args, **kwargs):
      '''
setMin( (Box3f)arg1, (V3f)arg2) -> None :
    setMin() sets the min value of the box

    C++ signature :
        void setMin(Imath_3_1::Box<Imath_3_1::Vec3<float> > {lvalue},Imath_3_1::Vec3<float>)'''
    ...
    def size (self, *args, **kwargs):
      '''
size( (Box3f)arg1) -> V3f :
    size() size of the box

    C++ signature :
        Imath_3_1::Vec3<float> size(Imath_3_1::Box<Imath_3_1::Vec3<float> > {lvalue})'''
    ...

def Box3fArray (*args):
      '''
__init__(_object*, Imath_3_1::Box<Imath_3_1::Vec3<float> >, unsigned long)
__init__(_object*, PyImath::FixedArray<Imath_3_1::Box<Imath_3_1::Vec3<float> > >)
__init__(_object*, unsigned long)

'''      
    ...

class Box3fArray:
    def ifelse (self, *args, **kwargs):
      '''
ifelse( (Box3fArray)arg1, (IntArray)arg2, (Box3f)arg3) -> Box3fArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Box<Imath_3_1::Vec3<float> > > ifelse(PyImath::FixedArray<Imath_3_1::Box<Imath_3_1::Vec3<float> > > {lvalue},PyImath::FixedArray<int>,Imath_3_1::Box<Imath_3_1::Vec3<float> >)

ifelse( (Box3fArray)arg1, (IntArray)arg2, (Box3fArray)arg3) -> Box3fArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Box<Imath_3_1::Vec3<float> > > ifelse(PyImath::FixedArray<Imath_3_1::Box<Imath_3_1::Vec3<float> > > {lvalue},PyImath::FixedArray<int>,PyImath::FixedArray<Imath_3_1::Box<Imath_3_1::Vec3<float> > >)'''
    ...
    def makeReadOnly (self, *args, **kwargs):
      '''
makeReadOnly( (Box3fArray)arg1) -> None :

    C++ signature :
        void makeReadOnly(PyImath::FixedArray<Imath_3_1::Box<Imath_3_1::Vec3<float> > > {lvalue})'''
    ...
    def max (self, *args, **kwargs):
      '''None'''
    ...
    def min (self, *args, **kwargs):
      '''None'''
    ...
    def writable (self, *args, **kwargs):
      '''
writable( (Box3fArray)arg1) -> bool :

    C++ signature :
        bool writable(PyImath::FixedArray<Imath_3_1::Box<Imath_3_1::Vec3<float> > > {lvalue})'''
    ...

def Box3i (*args):
      '''
__init__(boost::python::api::object, Imath_3_1::Box<Imath_3_1::Vec3<long> >)
__init__(boost::python::api::object, Imath_3_1::Box<Imath_3_1::Vec3<int> >)
__init__(boost::python::api::object, Imath_3_1::Box<Imath_3_1::Vec3<double> >)
__init__(boost::python::api::object, Imath_3_1::Box<Imath_3_1::Vec3<float> >)
__init__(boost::python::api::object, boost::python::tuple, boost::python::tuple)
__init__(boost::python::api::object, boost::python::tuple)
__init__(_object*, Imath_3_1::Vec3<int>, Imath_3_1::Vec3<int>)
__init__(_object*, Imath_3_1::Vec3<int>)
__init__(_object*)
__init__(_object*)

'''      
    ...

class Box3i:
    def center (self, *args, **kwargs):
      '''
center( (Box3i)arg1) -> V3i :
    center() center of the box

    C++ signature :
        Imath_3_1::Vec3<int> center(Imath_3_1::Box<Imath_3_1::Vec3<int> > {lvalue})'''
    ...
    def extendBy (self, *args, **kwargs):
      '''
extendBy( (Box3i)arg1, (V3i)arg2) -> None :
    extendBy(point) extend the box by a point

    C++ signature :
        void extendBy(Imath_3_1::Box<Imath_3_1::Vec3<int> > {lvalue},Imath_3_1::Vec3<int>)

extendBy( (Box3i)arg1, (V3iArray)arg2) -> None :
    extendBy(array) extend the box the values in the array

    C++ signature :
        void extendBy(Imath_3_1::Box<Imath_3_1::Vec3<int> > {lvalue},PyImath::FixedArray<Imath_3_1::Vec3<int> >)

extendBy( (Box3i)arg1, (Box3i)arg2) -> None :
    extendBy(box) extend the box by a box

    C++ signature :
        void extendBy(Imath_3_1::Box<Imath_3_1::Vec3<int> > {lvalue},Imath_3_1::Box<Imath_3_1::Vec3<int> >)'''
    ...
    def hasVolume (self, *args, **kwargs):
      '''
hasVolume( (Box3i)arg1) -> bool :
    hasVolume() returns true if the box has volume

    C++ signature :
        bool hasVolume(Imath_3_1::Box<Imath_3_1::Vec3<int> > {lvalue})'''
    ...
    def intersects (self, *args, **kwargs):
      '''
intersects( (Box3i)arg1, (V3i)arg2) -> bool :
    intersects(point) returns true if the box intersects the given point

    C++ signature :
        bool intersects(Imath_3_1::Box<Imath_3_1::Vec3<int> > {lvalue},Imath_3_1::Vec3<int>)

intersects( (Box3i)arg1, (Box3i)arg2) -> bool :
    intersects(box) returns true if the box intersects the given box

    C++ signature :
        bool intersects(Imath_3_1::Box<Imath_3_1::Vec3<int> > {lvalue},Imath_3_1::Box<Imath_3_1::Vec3<int> >)

intersects( (Box3i)arg1, (V3iArray)arg2) -> IntArray :
    intersects(array) returns an int array where 0 indicates the point is not in the box and 1 indicates that it is

    C++ signature :
        PyImath::FixedArray<int> intersects(Imath_3_1::Box<Imath_3_1::Vec3<int> > {lvalue},PyImath::FixedArray<Imath_3_1::Vec3<int> >)'''
    ...
    def isEmpty (self, *args, **kwargs):
      '''
isEmpty( (Box3i)arg1) -> bool :
    isEmpty() returns true if the box is empty

    C++ signature :
        bool isEmpty(Imath_3_1::Box<Imath_3_1::Vec3<int> > {lvalue})'''
    ...
    def isInfinite (self, *args, **kwargs):
      '''
isInfinite( (Box3i)arg1) -> bool :
    isInfinite() returns true if the box covers all space

    C++ signature :
        bool isInfinite(Imath_3_1::Box<Imath_3_1::Vec3<int> > {lvalue})'''
    ...
    def majorAxis (self, *args, **kwargs):
      '''
majorAxis( (Box3i)arg1) -> int :
    majorAxis() major axis of the box

    C++ signature :
        unsigned int majorAxis(Imath_3_1::Box<Imath_3_1::Vec3<int> > {lvalue})'''
    ...
    def makeEmpty (self, *args, **kwargs):
      '''
makeEmpty( (Box3i)arg1) -> None :
    makeEmpty() make the box empty

    C++ signature :
        void makeEmpty(Imath_3_1::Box<Imath_3_1::Vec3<int> > {lvalue})'''
    ...
    def makeInfinite (self, *args, **kwargs):
      '''
makeInfinite( (Box3i)arg1) -> None :
    makeInfinite() make the box cover all space

    C++ signature :
        void makeInfinite(Imath_3_1::Box<Imath_3_1::Vec3<int> > {lvalue})'''
    ...
    def max (self, *args, **kwargs):
      '''
max( (Box3i)arg1) -> V3i :

    C++ signature :
        Imath_3_1::Vec3<int> max(Imath_3_1::Box<Imath_3_1::Vec3<int> > {lvalue})'''
    ...
    def min (self, *args, **kwargs):
      '''
min( (Box3i)arg1) -> V3i :

    C++ signature :
        Imath_3_1::Vec3<int> min(Imath_3_1::Box<Imath_3_1::Vec3<int> > {lvalue})'''
    ...
    def setMax (self, *args, **kwargs):
      '''
setMax( (Box3i)arg1, (V3i)arg2) -> None :
    setMax() sets the max value of the box

    C++ signature :
        void setMax(Imath_3_1::Box<Imath_3_1::Vec3<int> > {lvalue},Imath_3_1::Vec3<int>)'''
    ...
    def setMin (self, *args, **kwargs):
      '''
setMin( (Box3i)arg1, (V3i)arg2) -> None :
    setMin() sets the min value of the box

    C++ signature :
        void setMin(Imath_3_1::Box<Imath_3_1::Vec3<int> > {lvalue},Imath_3_1::Vec3<int>)'''
    ...
    def size (self, *args, **kwargs):
      '''
size( (Box3i)arg1) -> V3i :
    size() size of the box

    C++ signature :
        Imath_3_1::Vec3<int> size(Imath_3_1::Box<Imath_3_1::Vec3<int> > {lvalue})'''
    ...

def Box3i64 (*args):
      '''
__init__(boost::python::api::object, Imath_3_1::Box<Imath_3_1::Vec3<long> >)
__init__(boost::python::api::object, Imath_3_1::Box<Imath_3_1::Vec3<int> >)
__init__(boost::python::api::object, Imath_3_1::Box<Imath_3_1::Vec3<double> >)
__init__(boost::python::api::object, Imath_3_1::Box<Imath_3_1::Vec3<float> >)
__init__(boost::python::api::object, boost::python::tuple, boost::python::tuple)
__init__(boost::python::api::object, boost::python::tuple)
__init__(_object*, Imath_3_1::Vec3<long>, Imath_3_1::Vec3<long>)
__init__(_object*, Imath_3_1::Vec3<long>)
__init__(_object*)
__init__(_object*)

'''      
    ...

class Box3i64:
    def center (self, *args, **kwargs):
      '''
center( (Box3i64)arg1) -> V3i64 :
    center() center of the box

    C++ signature :
        Imath_3_1::Vec3<long> center(Imath_3_1::Box<Imath_3_1::Vec3<long> > {lvalue})'''
    ...
    def extendBy (self, *args, **kwargs):
      '''
extendBy( (Box3i64)arg1, (V3i64)arg2) -> None :
    extendBy(point) extend the box by a point

    C++ signature :
        void extendBy(Imath_3_1::Box<Imath_3_1::Vec3<long> > {lvalue},Imath_3_1::Vec3<long>)

extendBy( (Box3i64)arg1, (V3i64Array)arg2) -> None :
    extendBy(array) extend the box the values in the array

    C++ signature :
        void extendBy(Imath_3_1::Box<Imath_3_1::Vec3<long> > {lvalue},PyImath::FixedArray<Imath_3_1::Vec3<long> >)

extendBy( (Box3i64)arg1, (Box3i64)arg2) -> None :
    extendBy(box) extend the box by a box

    C++ signature :
        void extendBy(Imath_3_1::Box<Imath_3_1::Vec3<long> > {lvalue},Imath_3_1::Box<Imath_3_1::Vec3<long> >)'''
    ...
    def hasVolume (self, *args, **kwargs):
      '''
hasVolume( (Box3i64)arg1) -> bool :
    hasVolume() returns true if the box has volume

    C++ signature :
        bool hasVolume(Imath_3_1::Box<Imath_3_1::Vec3<long> > {lvalue})'''
    ...
    def intersects (self, *args, **kwargs):
      '''
intersects( (Box3i64)arg1, (V3i64)arg2) -> bool :
    intersects(point) returns true if the box intersects the given point

    C++ signature :
        bool intersects(Imath_3_1::Box<Imath_3_1::Vec3<long> > {lvalue},Imath_3_1::Vec3<long>)

intersects( (Box3i64)arg1, (Box3i64)arg2) -> bool :
    intersects(box) returns true if the box intersects the given box

    C++ signature :
        bool intersects(Imath_3_1::Box<Imath_3_1::Vec3<long> > {lvalue},Imath_3_1::Box<Imath_3_1::Vec3<long> >)

intersects( (Box3i64)arg1, (V3i64Array)arg2) -> IntArray :
    intersects(array) returns an int array where 0 indicates the point is not in the box and 1 indicates that it is

    C++ signature :
        PyImath::FixedArray<int> intersects(Imath_3_1::Box<Imath_3_1::Vec3<long> > {lvalue},PyImath::FixedArray<Imath_3_1::Vec3<long> >)'''
    ...
    def isEmpty (self, *args, **kwargs):
      '''
isEmpty( (Box3i64)arg1) -> bool :
    isEmpty() returns true if the box is empty

    C++ signature :
        bool isEmpty(Imath_3_1::Box<Imath_3_1::Vec3<long> > {lvalue})'''
    ...
    def isInfinite (self, *args, **kwargs):
      '''
isInfinite( (Box3i64)arg1) -> bool :
    isInfinite() returns true if the box covers all space

    C++ signature :
        bool isInfinite(Imath_3_1::Box<Imath_3_1::Vec3<long> > {lvalue})'''
    ...
    def majorAxis (self, *args, **kwargs):
      '''
majorAxis( (Box3i64)arg1) -> int :
    majorAxis() major axis of the box

    C++ signature :
        unsigned int majorAxis(Imath_3_1::Box<Imath_3_1::Vec3<long> > {lvalue})'''
    ...
    def makeEmpty (self, *args, **kwargs):
      '''
makeEmpty( (Box3i64)arg1) -> None :
    makeEmpty() make the box empty

    C++ signature :
        void makeEmpty(Imath_3_1::Box<Imath_3_1::Vec3<long> > {lvalue})'''
    ...
    def makeInfinite (self, *args, **kwargs):
      '''
makeInfinite( (Box3i64)arg1) -> None :
    makeInfinite() make the box cover all space

    C++ signature :
        void makeInfinite(Imath_3_1::Box<Imath_3_1::Vec3<long> > {lvalue})'''
    ...
    def max (self, *args, **kwargs):
      '''
max( (Box3i64)arg1) -> V3i64 :

    C++ signature :
        Imath_3_1::Vec3<long> max(Imath_3_1::Box<Imath_3_1::Vec3<long> > {lvalue})'''
    ...
    def min (self, *args, **kwargs):
      '''
min( (Box3i64)arg1) -> V3i64 :

    C++ signature :
        Imath_3_1::Vec3<long> min(Imath_3_1::Box<Imath_3_1::Vec3<long> > {lvalue})'''
    ...
    def setMax (self, *args, **kwargs):
      '''
setMax( (Box3i64)arg1, (V3i64)arg2) -> None :
    setMax() sets the max value of the box

    C++ signature :
        void setMax(Imath_3_1::Box<Imath_3_1::Vec3<long> > {lvalue},Imath_3_1::Vec3<long>)'''
    ...
    def setMin (self, *args, **kwargs):
      '''
setMin( (Box3i64)arg1, (V3i64)arg2) -> None :
    setMin() sets the min value of the box

    C++ signature :
        void setMin(Imath_3_1::Box<Imath_3_1::Vec3<long> > {lvalue},Imath_3_1::Vec3<long>)'''
    ...
    def size (self, *args, **kwargs):
      '''
size( (Box3i64)arg1) -> V3i64 :
    size() size of the box

    C++ signature :
        Imath_3_1::Vec3<long> size(Imath_3_1::Box<Imath_3_1::Vec3<long> > {lvalue})'''
    ...

def Box3i64Array (*args):
      '''
__init__(_object*, Imath_3_1::Box<Imath_3_1::Vec3<long> >, unsigned long)
__init__(_object*, PyImath::FixedArray<Imath_3_1::Box<Imath_3_1::Vec3<long> > >)
__init__(_object*, unsigned long)

'''      
    ...

class Box3i64Array:
    def ifelse (self, *args, **kwargs):
      '''
ifelse( (Box3i64Array)arg1, (IntArray)arg2, (Box3i64)arg3) -> Box3i64Array :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Box<Imath_3_1::Vec3<long> > > ifelse(PyImath::FixedArray<Imath_3_1::Box<Imath_3_1::Vec3<long> > > {lvalue},PyImath::FixedArray<int>,Imath_3_1::Box<Imath_3_1::Vec3<long> >)

ifelse( (Box3i64Array)arg1, (IntArray)arg2, (Box3i64Array)arg3) -> Box3i64Array :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Box<Imath_3_1::Vec3<long> > > ifelse(PyImath::FixedArray<Imath_3_1::Box<Imath_3_1::Vec3<long> > > {lvalue},PyImath::FixedArray<int>,PyImath::FixedArray<Imath_3_1::Box<Imath_3_1::Vec3<long> > >)'''
    ...
    def makeReadOnly (self, *args, **kwargs):
      '''
makeReadOnly( (Box3i64Array)arg1) -> None :

    C++ signature :
        void makeReadOnly(PyImath::FixedArray<Imath_3_1::Box<Imath_3_1::Vec3<long> > > {lvalue})'''
    ...
    def max (self, *args, **kwargs):
      '''None'''
    ...
    def min (self, *args, **kwargs):
      '''None'''
    ...
    def writable (self, *args, **kwargs):
      '''
writable( (Box3i64Array)arg1) -> bool :

    C++ signature :
        bool writable(PyImath::FixedArray<Imath_3_1::Box<Imath_3_1::Vec3<long> > > {lvalue})'''
    ...

def Box3iArray (*args):
      '''
__init__(_object*, Imath_3_1::Box<Imath_3_1::Vec3<int> >, unsigned long)
__init__(_object*, PyImath::FixedArray<Imath_3_1::Box<Imath_3_1::Vec3<int> > >)
__init__(_object*, unsigned long)

'''      
    ...

class Box3iArray:
    def ifelse (self, *args, **kwargs):
      '''
ifelse( (Box3iArray)arg1, (IntArray)arg2, (Box3i)arg3) -> Box3iArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Box<Imath_3_1::Vec3<int> > > ifelse(PyImath::FixedArray<Imath_3_1::Box<Imath_3_1::Vec3<int> > > {lvalue},PyImath::FixedArray<int>,Imath_3_1::Box<Imath_3_1::Vec3<int> >)

ifelse( (Box3iArray)arg1, (IntArray)arg2, (Box3iArray)arg3) -> Box3iArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Box<Imath_3_1::Vec3<int> > > ifelse(PyImath::FixedArray<Imath_3_1::Box<Imath_3_1::Vec3<int> > > {lvalue},PyImath::FixedArray<int>,PyImath::FixedArray<Imath_3_1::Box<Imath_3_1::Vec3<int> > >)'''
    ...
    def makeReadOnly (self, *args, **kwargs):
      '''
makeReadOnly( (Box3iArray)arg1) -> None :

    C++ signature :
        void makeReadOnly(PyImath::FixedArray<Imath_3_1::Box<Imath_3_1::Vec3<int> > > {lvalue})'''
    ...
    def max (self, *args, **kwargs):
      '''None'''
    ...
    def min (self, *args, **kwargs):
      '''None'''
    ...
    def writable (self, *args, **kwargs):
      '''
writable( (Box3iArray)arg1) -> bool :

    C++ signature :
        bool writable(PyImath::FixedArray<Imath_3_1::Box<Imath_3_1::Vec3<int> > > {lvalue})'''
    ...

def Box3s (*args):
      '''
__init__(boost::python::api::object, Imath_3_1::Box<Imath_3_1::Vec3<long> >)
__init__(boost::python::api::object, Imath_3_1::Box<Imath_3_1::Vec3<int> >)
__init__(boost::python::api::object, Imath_3_1::Box<Imath_3_1::Vec3<double> >)
__init__(boost::python::api::object, Imath_3_1::Box<Imath_3_1::Vec3<float> >)
__init__(boost::python::api::object, boost::python::tuple, boost::python::tuple)
__init__(boost::python::api::object, boost::python::tuple)
__init__(_object*, Imath_3_1::Vec3<short>, Imath_3_1::Vec3<short>)
__init__(_object*, Imath_3_1::Vec3<short>)
__init__(_object*)
__init__(_object*)

'''      
    ...

class Box3s:
    def center (self, *args, **kwargs):
      '''
center( (Box3s)arg1) -> V3s :
    center() center of the box

    C++ signature :
        Imath_3_1::Vec3<short> center(Imath_3_1::Box<Imath_3_1::Vec3<short> > {lvalue})'''
    ...
    def extendBy (self, *args, **kwargs):
      '''
extendBy( (Box3s)arg1, (V3s)arg2) -> None :
    extendBy(point) extend the box by a point

    C++ signature :
        void extendBy(Imath_3_1::Box<Imath_3_1::Vec3<short> > {lvalue},Imath_3_1::Vec3<short>)

extendBy( (Box3s)arg1, (V3sArray)arg2) -> None :
    extendBy(array) extend the box the values in the array

    C++ signature :
        void extendBy(Imath_3_1::Box<Imath_3_1::Vec3<short> > {lvalue},PyImath::FixedArray<Imath_3_1::Vec3<short> >)

extendBy( (Box3s)arg1, (Box3s)arg2) -> None :
    extendBy(box) extend the box by a box

    C++ signature :
        void extendBy(Imath_3_1::Box<Imath_3_1::Vec3<short> > {lvalue},Imath_3_1::Box<Imath_3_1::Vec3<short> >)'''
    ...
    def hasVolume (self, *args, **kwargs):
      '''
hasVolume( (Box3s)arg1) -> bool :
    hasVolume() returns true if the box has volume

    C++ signature :
        bool hasVolume(Imath_3_1::Box<Imath_3_1::Vec3<short> > {lvalue})'''
    ...
    def intersects (self, *args, **kwargs):
      '''
intersects( (Box3s)arg1, (V3s)arg2) -> bool :
    intersects(point) returns true if the box intersects the given point

    C++ signature :
        bool intersects(Imath_3_1::Box<Imath_3_1::Vec3<short> > {lvalue},Imath_3_1::Vec3<short>)

intersects( (Box3s)arg1, (Box3s)arg2) -> bool :
    intersects(box) returns true if the box intersects the given box

    C++ signature :
        bool intersects(Imath_3_1::Box<Imath_3_1::Vec3<short> > {lvalue},Imath_3_1::Box<Imath_3_1::Vec3<short> >)

intersects( (Box3s)arg1, (V3sArray)arg2) -> IntArray :
    intersects(array) returns an int array where 0 indicates the point is not in the box and 1 indicates that it is

    C++ signature :
        PyImath::FixedArray<int> intersects(Imath_3_1::Box<Imath_3_1::Vec3<short> > {lvalue},PyImath::FixedArray<Imath_3_1::Vec3<short> >)'''
    ...
    def isEmpty (self, *args, **kwargs):
      '''
isEmpty( (Box3s)arg1) -> bool :
    isEmpty() returns true if the box is empty

    C++ signature :
        bool isEmpty(Imath_3_1::Box<Imath_3_1::Vec3<short> > {lvalue})'''
    ...
    def isInfinite (self, *args, **kwargs):
      '''
isInfinite( (Box3s)arg1) -> bool :
    isInfinite() returns true if the box covers all space

    C++ signature :
        bool isInfinite(Imath_3_1::Box<Imath_3_1::Vec3<short> > {lvalue})'''
    ...
    def majorAxis (self, *args, **kwargs):
      '''
majorAxis( (Box3s)arg1) -> int :
    majorAxis() major axis of the box

    C++ signature :
        unsigned int majorAxis(Imath_3_1::Box<Imath_3_1::Vec3<short> > {lvalue})'''
    ...
    def makeEmpty (self, *args, **kwargs):
      '''
makeEmpty( (Box3s)arg1) -> None :
    makeEmpty() make the box empty

    C++ signature :
        void makeEmpty(Imath_3_1::Box<Imath_3_1::Vec3<short> > {lvalue})'''
    ...
    def makeInfinite (self, *args, **kwargs):
      '''
makeInfinite( (Box3s)arg1) -> None :
    makeInfinite() make the box cover all space

    C++ signature :
        void makeInfinite(Imath_3_1::Box<Imath_3_1::Vec3<short> > {lvalue})'''
    ...
    def max (self, *args, **kwargs):
      '''
max( (Box3s)arg1) -> V3s :

    C++ signature :
        Imath_3_1::Vec3<short> max(Imath_3_1::Box<Imath_3_1::Vec3<short> > {lvalue})'''
    ...
    def min (self, *args, **kwargs):
      '''
min( (Box3s)arg1) -> V3s :

    C++ signature :
        Imath_3_1::Vec3<short> min(Imath_3_1::Box<Imath_3_1::Vec3<short> > {lvalue})'''
    ...
    def setMax (self, *args, **kwargs):
      '''
setMax( (Box3s)arg1, (V3s)arg2) -> None :
    setMax() sets the max value of the box

    C++ signature :
        void setMax(Imath_3_1::Box<Imath_3_1::Vec3<short> > {lvalue},Imath_3_1::Vec3<short>)'''
    ...
    def setMin (self, *args, **kwargs):
      '''
setMin( (Box3s)arg1, (V3s)arg2) -> None :
    setMin() sets the min value of the box

    C++ signature :
        void setMin(Imath_3_1::Box<Imath_3_1::Vec3<short> > {lvalue},Imath_3_1::Vec3<short>)'''
    ...
    def size (self, *args, **kwargs):
      '''
size( (Box3s)arg1) -> V3s :
    size() size of the box

    C++ signature :
        Imath_3_1::Vec3<short> size(Imath_3_1::Box<Imath_3_1::Vec3<short> > {lvalue})'''
    ...

def Box3sArray (*args):
      '''
__init__(_object*, Imath_3_1::Box<Imath_3_1::Vec3<short> >, unsigned long)
__init__(_object*, PyImath::FixedArray<Imath_3_1::Box<Imath_3_1::Vec3<short> > >)
__init__(_object*, unsigned long)

'''      
    ...

class Box3sArray:
    def ifelse (self, *args, **kwargs):
      '''
ifelse( (Box3sArray)arg1, (IntArray)arg2, (Box3s)arg3) -> Box3sArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Box<Imath_3_1::Vec3<short> > > ifelse(PyImath::FixedArray<Imath_3_1::Box<Imath_3_1::Vec3<short> > > {lvalue},PyImath::FixedArray<int>,Imath_3_1::Box<Imath_3_1::Vec3<short> >)

ifelse( (Box3sArray)arg1, (IntArray)arg2, (Box3sArray)arg3) -> Box3sArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Box<Imath_3_1::Vec3<short> > > ifelse(PyImath::FixedArray<Imath_3_1::Box<Imath_3_1::Vec3<short> > > {lvalue},PyImath::FixedArray<int>,PyImath::FixedArray<Imath_3_1::Box<Imath_3_1::Vec3<short> > >)'''
    ...
    def makeReadOnly (self, *args, **kwargs):
      '''
makeReadOnly( (Box3sArray)arg1) -> None :

    C++ signature :
        void makeReadOnly(PyImath::FixedArray<Imath_3_1::Box<Imath_3_1::Vec3<short> > > {lvalue})'''
    ...
    def max (self, *args, **kwargs):
      '''None'''
    ...
    def min (self, *args, **kwargs):
      '''None'''
    ...
    def writable (self, *args, **kwargs):
      '''
writable( (Box3sArray)arg1) -> bool :

    C++ signature :
        bool writable(PyImath::FixedArray<Imath_3_1::Box<Imath_3_1::Vec3<short> > > {lvalue})'''
    ...

def C3cArray (*args):
      '''
__init__(_object*, Imath_3_1::Color3<unsigned char>, unsigned long)
__init__(_object*, PyImath::FixedArray<Imath_3_1::Color3<unsigned char> >)
__init__(_object*, unsigned long)

'''      
    ...

class C3cArray:
    def b (self, *args, **kwargs):
      '''None'''
    ...
    def g (self, *args, **kwargs):
      '''None'''
    ...
    def ifelse (self, *args, **kwargs):
      '''
ifelse( (C3cArray)arg1, (IntArray)arg2, (Color3c)arg3) -> C3cArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Color3<unsigned char> > ifelse(PyImath::FixedArray<Imath_3_1::Color3<unsigned char> > {lvalue},PyImath::FixedArray<int>,Imath_3_1::Color3<unsigned char>)

ifelse( (C3cArray)arg1, (IntArray)arg2, (C3cArray)arg3) -> C3cArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Color3<unsigned char> > ifelse(PyImath::FixedArray<Imath_3_1::Color3<unsigned char> > {lvalue},PyImath::FixedArray<int>,PyImath::FixedArray<Imath_3_1::Color3<unsigned char> >)'''
    ...
    def makeReadOnly (self, *args, **kwargs):
      '''
makeReadOnly( (C3cArray)arg1) -> None :

    C++ signature :
        void makeReadOnly(PyImath::FixedArray<Imath_3_1::Color3<unsigned char> > {lvalue})'''
    ...
    def r (self, *args, **kwargs):
      '''None'''
    ...
    def writable (self, *args, **kwargs):
      '''
writable( (C3cArray)arg1) -> bool :

    C++ signature :
        bool writable(PyImath::FixedArray<Imath_3_1::Color3<unsigned char> > {lvalue})'''
    ...

def C3fArray (*args):
      '''
__init__(_object*, PyImath::FixedArray<Imath_3_1::Vec3<double> >)
__init__(_object*, PyImath::FixedArray<Imath_3_1::Vec3<float> >)
__init__(_object*, Imath_3_1::Color3<float>, unsigned long)
__init__(_object*, PyImath::FixedArray<Imath_3_1::Color3<float> >)
__init__(_object*, unsigned long)

'''      
    ...

class C3fArray:
    def b (self, *args, **kwargs):
      '''None'''
    ...
    def g (self, *args, **kwargs):
      '''None'''
    ...
    def ifelse (self, *args, **kwargs):
      '''
ifelse( (C3fArray)arg1, (IntArray)arg2, (Color3f)arg3) -> C3fArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Color3<float> > ifelse(PyImath::FixedArray<Imath_3_1::Color3<float> > {lvalue},PyImath::FixedArray<int>,Imath_3_1::Color3<float>)

ifelse( (C3fArray)arg1, (IntArray)arg2, (C3fArray)arg3) -> C3fArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Color3<float> > ifelse(PyImath::FixedArray<Imath_3_1::Color3<float> > {lvalue},PyImath::FixedArray<int>,PyImath::FixedArray<Imath_3_1::Color3<float> >)'''
    ...
    def makeReadOnly (self, *args, **kwargs):
      '''
makeReadOnly( (C3fArray)arg1) -> None :

    C++ signature :
        void makeReadOnly(PyImath::FixedArray<Imath_3_1::Color3<float> > {lvalue})'''
    ...
    def r (self, *args, **kwargs):
      '''None'''
    ...
    def writable (self, *args, **kwargs):
      '''
writable( (C3fArray)arg1) -> bool :

    C++ signature :
        bool writable(PyImath::FixedArray<Imath_3_1::Color3<float> > {lvalue})'''
    ...

def C4cArray (*args):
      '''
__init__(_object*, Imath_3_1::Color4<unsigned char>, unsigned long)
__init__(_object*, PyImath::FixedArray<Imath_3_1::Color4<unsigned char> >)
__init__(_object*, unsigned long)

'''      
    ...

class C4cArray:
    def a (self, *args, **kwargs):
      '''None'''
    ...
    def b (self, *args, **kwargs):
      '''None'''
    ...
    def g (self, *args, **kwargs):
      '''None'''
    ...
    def ifelse (self, *args, **kwargs):
      '''
ifelse( (C4cArray)arg1, (IntArray)arg2, (Color4c)arg3) -> C4cArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Color4<unsigned char> > ifelse(PyImath::FixedArray<Imath_3_1::Color4<unsigned char> > {lvalue},PyImath::FixedArray<int>,Imath_3_1::Color4<unsigned char>)

ifelse( (C4cArray)arg1, (IntArray)arg2, (C4cArray)arg3) -> C4cArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Color4<unsigned char> > ifelse(PyImath::FixedArray<Imath_3_1::Color4<unsigned char> > {lvalue},PyImath::FixedArray<int>,PyImath::FixedArray<Imath_3_1::Color4<unsigned char> >)'''
    ...
    def makeReadOnly (self, *args, **kwargs):
      '''
makeReadOnly( (C4cArray)arg1) -> None :

    C++ signature :
        void makeReadOnly(PyImath::FixedArray<Imath_3_1::Color4<unsigned char> > {lvalue})'''
    ...
    def r (self, *args, **kwargs):
      '''None'''
    ...
    def writable (self, *args, **kwargs):
      '''
writable( (C4cArray)arg1) -> bool :

    C++ signature :
        bool writable(PyImath::FixedArray<Imath_3_1::Color4<unsigned char> > {lvalue})'''
    ...

def C4fArray (*args):
      '''
__init__(_object*, Imath_3_1::Color4<float>, unsigned long)
__init__(_object*, PyImath::FixedArray<Imath_3_1::Color4<float> >)
__init__(_object*, unsigned long)

'''      
    ...

class C4fArray:
    def a (self, *args, **kwargs):
      '''None'''
    ...
    def b (self, *args, **kwargs):
      '''None'''
    ...
    def g (self, *args, **kwargs):
      '''None'''
    ...
    def ifelse (self, *args, **kwargs):
      '''
ifelse( (C4fArray)arg1, (IntArray)arg2, (Color4f)arg3) -> C4fArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Color4<float> > ifelse(PyImath::FixedArray<Imath_3_1::Color4<float> > {lvalue},PyImath::FixedArray<int>,Imath_3_1::Color4<float>)

ifelse( (C4fArray)arg1, (IntArray)arg2, (C4fArray)arg3) -> C4fArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Color4<float> > ifelse(PyImath::FixedArray<Imath_3_1::Color4<float> > {lvalue},PyImath::FixedArray<int>,PyImath::FixedArray<Imath_3_1::Color4<float> >)'''
    ...
    def makeReadOnly (self, *args, **kwargs):
      '''
makeReadOnly( (C4fArray)arg1) -> None :

    C++ signature :
        void makeReadOnly(PyImath::FixedArray<Imath_3_1::Color4<float> > {lvalue})'''
    ...
    def r (self, *args, **kwargs):
      '''None'''
    ...
    def writable (self, *args, **kwargs):
      '''
writable( (C4fArray)arg1) -> bool :

    C++ signature :
        bool writable(PyImath::FixedArray<Imath_3_1::Color4<float> > {lvalue})'''
    ...

def Color3c (*args):
      '''
__init__(boost::python::api::object, Imath_3_1::Vec3<int>)
__init__(boost::python::api::object, Imath_3_1::Vec3<double>)
__init__(boost::python::api::object, Imath_3_1::Vec3<float>)
__init__(boost::python::api::object, Imath_3_1::Color3<unsigned char>)
__init__(boost::python::api::object, Imath_3_1::Color3<int>)
__init__(boost::python::api::object, Imath_3_1::Color3<float>)
__init__(boost::python::api::object, int)
__init__(boost::python::api::object, float)
__init__(boost::python::api::object, int, int, int)
__init__(boost::python::api::object, float, float, float)
__init__(boost::python::api::object, boost::python::list)
__init__(boost::python::api::object, boost::python::tuple)
__init__(boost::python::api::object)
__init__(_object*, Imath_3_1::Color3<unsigned char>)

'''      
    ...

class Color3c:
    def b (self, *args, **kwargs):
      '''None'''
    ...
    def baseTypeEpsilon (self, *args, **kwargs):
      '''
baseTypeEpsilon() -> int :
    baseTypeEpsilon() epsilon value of the base type of the color

    C++ signature :
        unsigned char baseTypeEpsilon()'''
    ...
    def baseTypeLowest (self, *args, **kwargs):
      '''
baseTypeLowest() -> int :
    baseTypeLowest() largest negative value of the base type of the color

    C++ signature :
        unsigned char baseTypeLowest()'''
    ...
    def baseTypeMax (self, *args, **kwargs):
      '''
baseTypeMax() -> int :
    baseTypeMax() max value of the base type of the color

    C++ signature :
        unsigned char baseTypeMax()'''
    ...
    def baseTypeSmallest (self, *args, **kwargs):
      '''
baseTypeSmallest() -> int :
    baseTypeSmallest() smallest value of the base type of the color

    C++ signature :
        unsigned char baseTypeSmallest()'''
    ...
    def closestVertex (self, *args, **kwargs):
      '''
closestVertex( (V3c)arg1, (V3c)arg2, (V3c)arg3, (V3c)arg4) -> V3c :

    C++ signature :
        Imath_3_1::Vec3<unsigned char> closestVertex(Imath_3_1::Vec3<unsigned char> {lvalue},Imath_3_1::Vec3<unsigned char>,Imath_3_1::Vec3<unsigned char>,Imath_3_1::Vec3<unsigned char>)'''
    ...
    def cross (self, *args, **kwargs):
      '''
cross( (V3c)arg1, (V3c)arg2) -> V3c :
    v1.cross(v2) right handed cross product

    C++ signature :
        Imath_3_1::Vec3<unsigned char> cross(Imath_3_1::Vec3<unsigned char>,Imath_3_1::Vec3<unsigned char>)

cross( (V3c)arg1, (object)arg2) -> object :
    v1.cross(v2) right handed array cross product

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec3<unsigned char> > cross(Imath_3_1::Vec3<unsigned char>,PyImath::FixedArray<Imath_3_1::Vec3<unsigned char> >)'''
    ...
    def dimensions (self, *args, **kwargs):
      '''
dimensions() -> int :
    dimensions() number of dimensions in the color

    C++ signature :
        unsigned int dimensions()'''
    ...
    def dot (self, *args, **kwargs):
      '''
dot( (V3c)arg1, (V3c)arg2) -> int :
    v1.dot(v2) inner product of the two vectors

    C++ signature :
        unsigned char dot(Imath_3_1::Vec3<unsigned char>,Imath_3_1::Vec3<unsigned char>)

dot( (V3c)arg1, (object)arg2) -> UnsignedCharArray :
    v1.dot(v2) array inner product

    C++ signature :
        PyImath::FixedArray<unsigned char> dot(Imath_3_1::Vec3<unsigned char>,PyImath::FixedArray<Imath_3_1::Vec3<unsigned char> >)'''
    ...
    def equalWithAbsError (self, *args, **kwargs):
      '''
equalWithAbsError( (V3c)arg1, (V3c)arg2, (int)arg3) -> bool :
    v1.equalWithAbsError(v2) true if the elements of v1 and v2 are the same with an absolute error of no more than e, i.e., abs(v1[i] - v2[i]) <= e

    C++ signature :
        bool equalWithAbsError(Imath_3_1::Vec3<unsigned char> {lvalue},Imath_3_1::Vec3<unsigned char>,unsigned char)

equalWithAbsError( (V3c)arg1, (object)arg2, (object)arg3) -> bool :

    C++ signature :
        bool equalWithAbsError(Imath_3_1::Vec3<unsigned char>,boost::python::api::object,boost::python::api::object)'''
    ...
    def equalWithRelError (self, *args, **kwargs):
      '''
equalWithRelError( (V3c)arg1, (V3c)arg2, (int)arg3) -> bool :
    v1.equalWithAbsError(v2) true if the elements of v1 and v2 are the same with an absolute error of no more than e, i.e., abs(v1[i] - v2[i]) <= e * abs(v1[i])

    C++ signature :
        bool equalWithRelError(Imath_3_1::Vec3<unsigned char> {lvalue},Imath_3_1::Vec3<unsigned char>,unsigned char)

equalWithRelError( (V3c)arg1, (object)arg2, (object)arg3) -> bool :

    C++ signature :
        bool equalWithRelError(Imath_3_1::Vec3<unsigned char>,boost::python::api::object,boost::python::api::object)'''
    ...
    def g (self, *args, **kwargs):
      '''None'''
    ...
    def hsv2rgb (self, *args, **kwargs):
      '''
hsv2rgb( (Color3c)arg1) -> Color3c :
    C.hsv2rgb() -- returns a new color which is C converted from RGB to HSV

    C++ signature :
        Imath_3_1::Color3<unsigned char> hsv2rgb(Imath_3_1::Color3<unsigned char> {lvalue})

hsv2rgb( (tuple)arg1) -> Color3c :

    C++ signature :
        Imath_3_1::Color3<unsigned char> hsv2rgb(boost::python::tuple)'''
    ...
    def length2 (self, *args, **kwargs):
      '''
length2( (V3c)arg1) -> int :
    length2() square magnitude of the vector

    C++ signature :
        unsigned char length2(Imath_3_1::Vec3<unsigned char>)'''
    ...
    def negate (self, *args, **kwargs):
      '''
negate( (Color3c)arg1) -> Color3c :
    component-wise multiplication by -1

    C++ signature :
        Imath_3_1::Color3<unsigned char> negate(Imath_3_1::Color3<unsigned char> {lvalue})'''
    ...
    def r (self, *args, **kwargs):
      '''None'''
    ...
    def rgb2hsv (self, *args, **kwargs):
      '''
rgb2hsv( (Color3c)arg1) -> Color3c :
    C.rgb2hsv() -- returns a new color which is C converted from HSV to RGB

    C++ signature :
        Imath_3_1::Color3<unsigned char> rgb2hsv(Imath_3_1::Color3<unsigned char> {lvalue})

rgb2hsv( (tuple)arg1) -> Color3c :

    C++ signature :
        Imath_3_1::Color3<unsigned char> rgb2hsv(boost::python::tuple)'''
    ...
    def setValue (self, *args, **kwargs):
      '''
setValue( (Color3c)arg1, (int)arg2, (int)arg3, (int)arg4) -> None :
    C1.setValue(C2)
    C1.setValue(a,b,c) -- set C1's  elements

    C++ signature :
        void setValue(Imath_3_1::Color3<unsigned char> {lvalue},unsigned char,unsigned char,unsigned char)

setValue( (Color3c)arg1, (Color3c)arg2) -> None :

    C++ signature :
        void setValue(Imath_3_1::Color3<unsigned char> {lvalue},Imath_3_1::Color3<unsigned char>)

setValue( (Color3c)arg1, (tuple)arg2) -> None :

    C++ signature :
        void setValue(Imath_3_1::Color3<unsigned char> {lvalue},boost::python::tuple)'''
    ...
    def x (self, *args, **kwargs):
      '''None'''
    ...
    def y (self, *args, **kwargs):
      '''None'''
    ...
    def z (self, *args, **kwargs):
      '''None'''
    ...

def Color3f (*args):
      '''
__init__(boost::python::api::object, Imath_3_1::Vec3<int>)
__init__(boost::python::api::object, Imath_3_1::Vec3<double>)
__init__(boost::python::api::object, Imath_3_1::Vec3<float>)
__init__(boost::python::api::object, Imath_3_1::Color3<unsigned char>)
__init__(boost::python::api::object, Imath_3_1::Color3<int>)
__init__(boost::python::api::object, Imath_3_1::Color3<float>)
__init__(boost::python::api::object, int)
__init__(boost::python::api::object, float)
__init__(boost::python::api::object, int, int, int)
__init__(boost::python::api::object, float, float, float)
__init__(boost::python::api::object, boost::python::list)
__init__(boost::python::api::object, boost::python::tuple)
__init__(boost::python::api::object)
__init__(_object*, Imath_3_1::Color3<float>)

'''      
    ...

class Color3f:
    def b (self, *args, **kwargs):
      '''None'''
    ...
    def baseTypeEpsilon (self, *args, **kwargs):
      '''
baseTypeEpsilon() -> float :
    baseTypeEpsilon() epsilon value of the base type of the color

    C++ signature :
        float baseTypeEpsilon()'''
    ...
    def baseTypeLowest (self, *args, **kwargs):
      '''
baseTypeLowest() -> float :
    baseTypeLowest() largest negative value of the base type of the color

    C++ signature :
        float baseTypeLowest()'''
    ...
    def baseTypeMax (self, *args, **kwargs):
      '''
baseTypeMax() -> float :
    baseTypeMax() max value of the base type of the color

    C++ signature :
        float baseTypeMax()'''
    ...
    def baseTypeSmallest (self, *args, **kwargs):
      '''
baseTypeSmallest() -> float :
    baseTypeSmallest() smallest value of the base type of the color

    C++ signature :
        float baseTypeSmallest()'''
    ...
    def closestVertex (self, *args, **kwargs):
      '''
closestVertex( (V3f)arg1, (V3f)arg2, (V3f)arg3, (V3f)arg4) -> V3f :

    C++ signature :
        Imath_3_1::Vec3<float> closestVertex(Imath_3_1::Vec3<float> {lvalue},Imath_3_1::Vec3<float>,Imath_3_1::Vec3<float>,Imath_3_1::Vec3<float>)'''
    ...
    def cross (self, *args, **kwargs):
      '''
cross( (V3f)arg1, (V3f)arg2) -> V3f :
    v1.cross(v2) right handed cross product

    C++ signature :
        Imath_3_1::Vec3<float> cross(Imath_3_1::Vec3<float>,Imath_3_1::Vec3<float>)

cross( (V3f)arg1, (V3fArray)arg2) -> V3fArray :
    v1.cross(v2) right handed array cross product

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec3<float> > cross(Imath_3_1::Vec3<float>,PyImath::FixedArray<Imath_3_1::Vec3<float> >)'''
    ...
    def dimensions (self, *args, **kwargs):
      '''
dimensions() -> int :
    dimensions() number of dimensions in the color

    C++ signature :
        unsigned int dimensions()'''
    ...
    def dot (self, *args, **kwargs):
      '''
dot( (V3f)arg1, (V3f)arg2) -> float :
    v1.dot(v2) inner product of the two vectors

    C++ signature :
        float dot(Imath_3_1::Vec3<float>,Imath_3_1::Vec3<float>)

dot( (V3f)arg1, (V3fArray)arg2) -> FloatArray :
    v1.dot(v2) array inner product

    C++ signature :
        PyImath::FixedArray<float> dot(Imath_3_1::Vec3<float>,PyImath::FixedArray<Imath_3_1::Vec3<float> >)'''
    ...
    def equalWithAbsError (self, *args, **kwargs):
      '''
equalWithAbsError( (V3f)arg1, (V3f)arg2, (float)arg3) -> bool :
    v1.equalWithAbsError(v2) true if the elements of v1 and v2 are the same with an absolute error of no more than e, i.e., abs(v1[i] - v2[i]) <= e

    C++ signature :
        bool equalWithAbsError(Imath_3_1::Vec3<float> {lvalue},Imath_3_1::Vec3<float>,float)

equalWithAbsError( (V3f)arg1, (object)arg2, (object)arg3) -> bool :

    C++ signature :
        bool equalWithAbsError(Imath_3_1::Vec3<float>,boost::python::api::object,boost::python::api::object)'''
    ...
    def equalWithRelError (self, *args, **kwargs):
      '''
equalWithRelError( (V3f)arg1, (V3f)arg2, (float)arg3) -> bool :
    v1.equalWithAbsError(v2) true if the elements of v1 and v2 are the same with an absolute error of no more than e, i.e., abs(v1[i] - v2[i]) <= e * abs(v1[i])

    C++ signature :
        bool equalWithRelError(Imath_3_1::Vec3<float> {lvalue},Imath_3_1::Vec3<float>,float)

equalWithRelError( (V3f)arg1, (object)arg2, (object)arg3) -> bool :

    C++ signature :
        bool equalWithRelError(Imath_3_1::Vec3<float>,boost::python::api::object,boost::python::api::object)'''
    ...
    def g (self, *args, **kwargs):
      '''None'''
    ...
    def hsv2rgb (self, *args, **kwargs):
      '''
hsv2rgb( (Color3f)arg1) -> Color3f :
    C.hsv2rgb() -- returns a new color which is C converted from RGB to HSV

    C++ signature :
        Imath_3_1::Color3<float> hsv2rgb(Imath_3_1::Color3<float> {lvalue})

hsv2rgb( (tuple)arg1) -> Color3f :

    C++ signature :
        Imath_3_1::Color3<float> hsv2rgb(boost::python::tuple)'''
    ...
    def length (self, *args, **kwargs):
      '''
length( (V3f)arg1) -> float :
    length() magnitude of the vector

    C++ signature :
        float length(Imath_3_1::Vec3<float>)'''
    ...
    def length2 (self, *args, **kwargs):
      '''
length2( (V3f)arg1) -> float :
    length2() square magnitude of the vector

    C++ signature :
        float length2(Imath_3_1::Vec3<float>)'''
    ...
    def negate (self, *args, **kwargs):
      '''
negate( (Color3f)arg1) -> Color3f :
    component-wise multiplication by -1

    C++ signature :
        Imath_3_1::Color3<float> negate(Imath_3_1::Color3<float> {lvalue})'''
    ...
    def normalize (self, *args, **kwargs):
      '''
normalize( (V3f)arg1) -> V3f :
    v.normalize() destructively normalizes v and returns a reference to it

    C++ signature :
        Imath_3_1::Vec3<float> normalize(Imath_3_1::Vec3<float> {lvalue})'''
    ...
    def normalizeExc (self, *args, **kwargs):
      '''
normalizeExc( (V3f)arg1) -> V3f :
    v.normalizeExc() destructively normalizes V and returns a reference to it, throwing an exception if length() == 0

    C++ signature :
        Imath_3_1::Vec3<float> normalizeExc(Imath_3_1::Vec3<float> {lvalue})'''
    ...
    def normalizeNonNull (self, *args, **kwargs):
      '''
normalizeNonNull( (V3f)arg1) -> V3f :
    v.normalizeNonNull() destructively normalizes V and returns a reference to it, faster if lngth() != 0

    C++ signature :
        Imath_3_1::Vec3<float> normalizeNonNull(Imath_3_1::Vec3<float> {lvalue})'''
    ...
    def normalized (self, *args, **kwargs):
      '''
normalized( (V3f)arg1) -> V3f :
    v.normalized() returns a normalized copy of v

    C++ signature :
        Imath_3_1::Vec3<float> normalized(Imath_3_1::Vec3<float>)'''
    ...
    def normalizedExc (self, *args, **kwargs):
      '''
normalizedExc( (V3f)arg1) -> V3f :
    v.normalizedExc() returns a normalized copy of v, throwing an exception if length() == 0

    C++ signature :
        Imath_3_1::Vec3<float> normalizedExc(Imath_3_1::Vec3<float>)'''
    ...
    def normalizedNonNull (self, *args, **kwargs):
      '''
normalizedNonNull( (V3f)arg1) -> V3f :
    v.normalizedNonNull() returns a normalized copy of v, faster if lngth() != 0

    C++ signature :
        Imath_3_1::Vec3<float> normalizedNonNull(Imath_3_1::Vec3<float>)'''
    ...
    def orthogonal (self, *args, **kwargs):
      '''
orthogonal( (V3f)arg1, (V3f)arg2) -> V3f :

    C++ signature :
        Imath_3_1::Vec3<float> orthogonal(Imath_3_1::Vec3<float>,Imath_3_1::Vec3<float>)'''
    ...
    def project (self, *args, **kwargs):
      '''
project( (V3f)arg1, (V3f)arg2) -> V3f :

    C++ signature :
        Imath_3_1::Vec3<float> project(Imath_3_1::Vec3<float>,Imath_3_1::Vec3<float>)'''
    ...
    def r (self, *args, **kwargs):
      '''None'''
    ...
    def reflect (self, *args, **kwargs):
      '''
reflect( (V3f)arg1, (V3f)arg2) -> V3f :

    C++ signature :
        Imath_3_1::Vec3<float> reflect(Imath_3_1::Vec3<float>,Imath_3_1::Vec3<float>)'''
    ...
    def rgb2hsv (self, *args, **kwargs):
      '''
rgb2hsv( (Color3f)arg1) -> Color3f :
    C.rgb2hsv() -- returns a new color which is C converted from HSV to RGB

    C++ signature :
        Imath_3_1::Color3<float> rgb2hsv(Imath_3_1::Color3<float> {lvalue})

rgb2hsv( (tuple)arg1) -> Color3f :

    C++ signature :
        Imath_3_1::Color3<float> rgb2hsv(boost::python::tuple)'''
    ...
    def setValue (self, *args, **kwargs):
      '''
setValue( (Color3f)arg1, (float)arg2, (float)arg3, (float)arg4) -> None :
    C1.setValue(C2)
    C1.setValue(a,b,c) -- set C1's  elements

    C++ signature :
        void setValue(Imath_3_1::Color3<float> {lvalue},float,float,float)

setValue( (Color3f)arg1, (Color3f)arg2) -> None :

    C++ signature :
        void setValue(Imath_3_1::Color3<float> {lvalue},Imath_3_1::Color3<float>)

setValue( (Color3f)arg1, (tuple)arg2) -> None :

    C++ signature :
        void setValue(Imath_3_1::Color3<float> {lvalue},boost::python::tuple)'''
    ...
    def x (self, *args, **kwargs):
      '''None'''
    ...
    def y (self, *args, **kwargs):
      '''None'''
    ...
    def z (self, *args, **kwargs):
      '''None'''
    ...

def Color4c (*args):
      '''
__init__(boost::python::api::object, Imath_3_1::Color4<unsigned char>)
__init__(boost::python::api::object, Imath_3_1::Color4<int>)
__init__(boost::python::api::object, Imath_3_1::Color4<float>)
__init__(boost::python::api::object, int)
__init__(boost::python::api::object, float)
__init__(boost::python::api::object, int, int, int, int)
__init__(boost::python::api::object, float, float, float, float)
__init__(boost::python::api::object, boost::python::list)
__init__(boost::python::api::object, boost::python::tuple)
__init__(boost::python::api::object)
__init__(_object*, Imath_3_1::Color4<unsigned char>)

'''      
    ...

class Color4c:
    def a (self, *args, **kwargs):
      '''None'''
    ...
    def b (self, *args, **kwargs):
      '''None'''
    ...
    def baseTypeEpsilon (self, *args, **kwargs):
      '''
baseTypeEpsilon() -> int :
    baseTypeEpsilon() epsilon value of the base type of the color

    C++ signature :
        unsigned char baseTypeEpsilon()'''
    ...
    def baseTypeLowest (self, *args, **kwargs):
      '''
baseTypeLowest() -> int :
    baseTypeLowest() largest negative value of the base type of the color

    C++ signature :
        unsigned char baseTypeLowest()'''
    ...
    def baseTypeMax (self, *args, **kwargs):
      '''
baseTypeMax() -> int :
    baseTypeMax() max value of the base type of the color

    C++ signature :
        unsigned char baseTypeMax()'''
    ...
    def baseTypeSmallest (self, *args, **kwargs):
      '''
baseTypeSmallest() -> int :
    baseTypeSmallest() smallest value of the base type of the color

    C++ signature :
        unsigned char baseTypeSmallest()'''
    ...
    def dimensions (self, *args, **kwargs):
      '''
dimensions() -> int :
    dimensions() number of dimensions in the color

    C++ signature :
        unsigned int dimensions()'''
    ...
    def g (self, *args, **kwargs):
      '''None'''
    ...
    def getValue (self, *args, **kwargs):
      '''
getValue( (Color4c)arg1, (Color4c)arg2) -> None :
    getValue()

    C++ signature :
        void getValue(Imath_3_1::Color4<unsigned char> {lvalue},Imath_3_1::Color4<unsigned char> {lvalue})

getValue( (Color4c)arg1, (int)arg2, (int)arg3, (int)arg4, (int)arg5) -> None :

    C++ signature :
        void getValue(Imath_3_1::Color4<unsigned char> {lvalue},unsigned char {lvalue},unsigned char {lvalue},unsigned char {lvalue},unsigned char {lvalue})'''
    ...
    def hsv2rgb (self, *args, **kwargs):
      '''
hsv2rgb( (Color4c)arg1) -> Color4c :
    C.hsv2rgb() -- returns a new color which is C converted from RGB to HSV

    C++ signature :
        Imath_3_1::Color4<unsigned char> hsv2rgb(Imath_3_1::Color4<unsigned char> {lvalue})

hsv2rgb( (tuple)arg1) -> Color4c :

    C++ signature :
        Imath_3_1::Color4<unsigned char> hsv2rgb(boost::python::tuple)'''
    ...
    def negate (self, *args, **kwargs):
      '''
negate( (Color4c)arg1) -> Color4c :
    component-wise multiplication by -1

    C++ signature :
        Imath_3_1::Color4<unsigned char> negate(Imath_3_1::Color4<unsigned char> {lvalue})'''
    ...
    def r (self, *args, **kwargs):
      '''None'''
    ...
    def rgb2hsv (self, *args, **kwargs):
      '''
rgb2hsv( (Color4c)arg1) -> Color4c :
    C.rgb2hsv() -- returns a new color which is C converted from HSV to RGB

    C++ signature :
        Imath_3_1::Color4<unsigned char> rgb2hsv(Imath_3_1::Color4<unsigned char> {lvalue})

rgb2hsv( (tuple)arg1) -> Color4c :

    C++ signature :
        Imath_3_1::Color4<unsigned char> rgb2hsv(boost::python::tuple)'''
    ...
    def setValue (self, *args, **kwargs):
      '''
setValue( (Color4c)arg1, (int)arg2, (int)arg3, (int)arg4, (int)arg5) -> None :
    C1.setValue(C2)
    C1.setValue(a,b,c) -- set C1's  elements

    C++ signature :
        void setValue(Imath_3_1::Color4<unsigned char> {lvalue},unsigned char,unsigned char,unsigned char,unsigned char)

setValue( (Color4c)arg1, (Color4c)arg2) -> None :

    C++ signature :
        void setValue(Imath_3_1::Color4<unsigned char> {lvalue},Imath_3_1::Color4<unsigned char>)

setValue( (Color4c)arg1, (tuple)arg2) -> None :

    C++ signature :
        void setValue(Imath_3_1::Color4<unsigned char> {lvalue},boost::python::tuple)'''
    ...

def Color4cArray2D (*args):
      '''
__init__(_object*, Imath_3_1::Color4<unsigned char>, unsigned long, unsigned long)
__init__(_object*, PyImath::FixedArray2D<Imath_3_1::Color4<unsigned char> >)
__init__(_object*, unsigned long, unsigned long)

'''      
    ...

class Color4cArray2D:
    def a (self, *args, **kwargs):
      '''None'''
    ...
    def b (self, *args, **kwargs):
      '''None'''
    ...
    def g (self, *args, **kwargs):
      '''None'''
    ...
    def ifelse (self, *args, **kwargs):
      '''
ifelse( (Color4cArray2D)arg1, (IntArray2D)arg2, (Color4c)arg3) -> Color4cArray2D :

    C++ signature :
        PyImath::FixedArray2D<Imath_3_1::Color4<unsigned char> > ifelse(PyImath::FixedArray2D<Imath_3_1::Color4<unsigned char> > {lvalue},PyImath::FixedArray2D<int>,Imath_3_1::Color4<unsigned char>)

ifelse( (Color4cArray2D)arg1, (IntArray2D)arg2, (Color4cArray2D)arg3) -> Color4cArray2D :

    C++ signature :
        PyImath::FixedArray2D<Imath_3_1::Color4<unsigned char> > ifelse(PyImath::FixedArray2D<Imath_3_1::Color4<unsigned char> > {lvalue},PyImath::FixedArray2D<int>,PyImath::FixedArray2D<Imath_3_1::Color4<unsigned char> >)'''
    ...
    def item (self, *args, **kwargs):
      '''
item( (Color4cArray2D)arg1, (int)arg2, (int)arg3) -> Color4c :

    C++ signature :
        Imath_3_1::Color4<unsigned char> {lvalue} item(PyImath::FixedArray2D<Imath_3_1::Color4<unsigned char> > {lvalue},long,long)'''
    ...
    def r (self, *args, **kwargs):
      '''None'''
    ...
    def size (self, *args, **kwargs):
      '''
size( (Color4cArray2D)arg1) -> tuple :

    C++ signature :
        boost::python::tuple size(PyImath::FixedArray2D<Imath_3_1::Color4<unsigned char> > {lvalue})'''
    ...

def Color4f (*args):
      '''
__init__(boost::python::api::object, Imath_3_1::Color4<unsigned char>)
__init__(boost::python::api::object, Imath_3_1::Color4<int>)
__init__(boost::python::api::object, Imath_3_1::Color4<float>)
__init__(boost::python::api::object, int)
__init__(boost::python::api::object, float)
__init__(boost::python::api::object, int, int, int, int)
__init__(boost::python::api::object, float, float, float, float)
__init__(boost::python::api::object, boost::python::list)
__init__(boost::python::api::object, boost::python::tuple)
__init__(boost::python::api::object)
__init__(_object*, Imath_3_1::Color4<float>)

'''      
    ...

class Color4f:
    def a (self, *args, **kwargs):
      '''None'''
    ...
    def b (self, *args, **kwargs):
      '''None'''
    ...
    def baseTypeEpsilon (self, *args, **kwargs):
      '''
baseTypeEpsilon() -> float :
    baseTypeEpsilon() epsilon value of the base type of the color

    C++ signature :
        float baseTypeEpsilon()'''
    ...
    def baseTypeLowest (self, *args, **kwargs):
      '''
baseTypeLowest() -> float :
    baseTypeLowest() largest negative value of the base type of the color

    C++ signature :
        float baseTypeLowest()'''
    ...
    def baseTypeMax (self, *args, **kwargs):
      '''
baseTypeMax() -> float :
    baseTypeMax() max value of the base type of the color

    C++ signature :
        float baseTypeMax()'''
    ...
    def baseTypeSmallest (self, *args, **kwargs):
      '''
baseTypeSmallest() -> float :
    baseTypeSmallest() smallest value of the base type of the color

    C++ signature :
        float baseTypeSmallest()'''
    ...
    def dimensions (self, *args, **kwargs):
      '''
dimensions() -> int :
    dimensions() number of dimensions in the color

    C++ signature :
        unsigned int dimensions()'''
    ...
    def g (self, *args, **kwargs):
      '''None'''
    ...
    def getValue (self, *args, **kwargs):
      '''
getValue( (Color4f)arg1, (Color4f)arg2) -> None :
    getValue()

    C++ signature :
        void getValue(Imath_3_1::Color4<float> {lvalue},Imath_3_1::Color4<float> {lvalue})

getValue( (Color4f)arg1, (float)arg2, (float)arg3, (float)arg4, (float)arg5) -> None :

    C++ signature :
        void getValue(Imath_3_1::Color4<float> {lvalue},float {lvalue},float {lvalue},float {lvalue},float {lvalue})'''
    ...
    def hsv2rgb (self, *args, **kwargs):
      '''
hsv2rgb( (Color4f)arg1) -> Color4f :
    C.hsv2rgb() -- returns a new color which is C converted from RGB to HSV

    C++ signature :
        Imath_3_1::Color4<float> hsv2rgb(Imath_3_1::Color4<float> {lvalue})

hsv2rgb( (tuple)arg1) -> Color4f :

    C++ signature :
        Imath_3_1::Color4<float> hsv2rgb(boost::python::tuple)'''
    ...
    def negate (self, *args, **kwargs):
      '''
negate( (Color4f)arg1) -> Color4f :
    component-wise multiplication by -1

    C++ signature :
        Imath_3_1::Color4<float> negate(Imath_3_1::Color4<float> {lvalue})'''
    ...
    def r (self, *args, **kwargs):
      '''None'''
    ...
    def rgb2hsv (self, *args, **kwargs):
      '''
rgb2hsv( (Color4f)arg1) -> Color4f :
    C.rgb2hsv() -- returns a new color which is C converted from HSV to RGB

    C++ signature :
        Imath_3_1::Color4<float> rgb2hsv(Imath_3_1::Color4<float> {lvalue})

rgb2hsv( (tuple)arg1) -> Color4f :

    C++ signature :
        Imath_3_1::Color4<float> rgb2hsv(boost::python::tuple)'''
    ...
    def setValue (self, *args, **kwargs):
      '''
setValue( (Color4f)arg1, (float)arg2, (float)arg3, (float)arg4, (float)arg5) -> None :
    C1.setValue(C2)
    C1.setValue(a,b,c) -- set C1's  elements

    C++ signature :
        void setValue(Imath_3_1::Color4<float> {lvalue},float,float,float,float)

setValue( (Color4f)arg1, (Color4f)arg2) -> None :

    C++ signature :
        void setValue(Imath_3_1::Color4<float> {lvalue},Imath_3_1::Color4<float>)

setValue( (Color4f)arg1, (tuple)arg2) -> None :

    C++ signature :
        void setValue(Imath_3_1::Color4<float> {lvalue},boost::python::tuple)'''
    ...

def Color4fArray2D (*args):
      '''
__init__(_object*, Imath_3_1::Color4<float>, unsigned long, unsigned long)
__init__(_object*, PyImath::FixedArray2D<Imath_3_1::Color4<float> >)
__init__(_object*, unsigned long, unsigned long)

'''      
    ...

class Color4fArray2D:
    def a (self, *args, **kwargs):
      '''None'''
    ...
    def b (self, *args, **kwargs):
      '''None'''
    ...
    def g (self, *args, **kwargs):
      '''None'''
    ...
    def ifelse (self, *args, **kwargs):
      '''
ifelse( (Color4fArray2D)arg1, (IntArray2D)arg2, (Color4f)arg3) -> Color4fArray2D :

    C++ signature :
        PyImath::FixedArray2D<Imath_3_1::Color4<float> > ifelse(PyImath::FixedArray2D<Imath_3_1::Color4<float> > {lvalue},PyImath::FixedArray2D<int>,Imath_3_1::Color4<float>)

ifelse( (Color4fArray2D)arg1, (IntArray2D)arg2, (Color4fArray2D)arg3) -> Color4fArray2D :

    C++ signature :
        PyImath::FixedArray2D<Imath_3_1::Color4<float> > ifelse(PyImath::FixedArray2D<Imath_3_1::Color4<float> > {lvalue},PyImath::FixedArray2D<int>,PyImath::FixedArray2D<Imath_3_1::Color4<float> >)'''
    ...
    def item (self, *args, **kwargs):
      '''
item( (Color4fArray2D)arg1, (int)arg2, (int)arg3) -> Color4f :

    C++ signature :
        Imath_3_1::Color4<float> {lvalue} item(PyImath::FixedArray2D<Imath_3_1::Color4<float> > {lvalue},long,long)'''
    ...
    def r (self, *args, **kwargs):
      '''None'''
    ...
    def size (self, *args, **kwargs):
      '''
size( (Color4fArray2D)arg1) -> tuple :

    C++ signature :
        boost::python::tuple size(PyImath::FixedArray2D<Imath_3_1::Color4<float> > {lvalue})'''
    ...

def DBL_EPS (*args):
      '''

'''      
    ...

def DBL_LOWEST (*args):
      '''

'''      
    ...

def DBL_MAX (*args):
      '''

'''      
    ...

def DBL_MIN (*args):
      '''

'''      
    ...

def DoubleArray (*args):
      '''
__init__(_object*, PyImath::FixedArray<float>)
__init__(_object*, PyImath::FixedArray<int>)
__init__(_object*, double, unsigned long)
__init__(_object*, PyImath::FixedArray<double>)
__init__(_object*, unsigned long)

'''      
    ...

class DoubleArray:
    def ifelse (self, *args, **kwargs):
      '''
ifelse( (DoubleArray)arg1, (IntArray)arg2, (float)arg3) -> DoubleArray :

    C++ signature :
        PyImath::FixedArray<double> ifelse(PyImath::FixedArray<double> {lvalue},PyImath::FixedArray<int>,double)

ifelse( (DoubleArray)arg1, (IntArray)arg2, (DoubleArray)arg3) -> DoubleArray :

    C++ signature :
        PyImath::FixedArray<double> ifelse(PyImath::FixedArray<double> {lvalue},PyImath::FixedArray<int>,PyImath::FixedArray<double>)'''
    ...
    def makeReadOnly (self, *args, **kwargs):
      '''
makeReadOnly( (DoubleArray)arg1) -> None :

    C++ signature :
        void makeReadOnly(PyImath::FixedArray<double> {lvalue})'''
    ...
    def reduce (self, *args, **kwargs):
      '''
reduce( (DoubleArray)arg1) -> float :

    C++ signature :
        double reduce(PyImath::FixedArray<double>)'''
    ...
    def writable (self, *args, **kwargs):
      '''
writable( (DoubleArray)arg1) -> bool :

    C++ signature :
        bool writable(PyImath::FixedArray<double> {lvalue})'''
    ...

def DoubleArray2D (*args):
      '''
__init__(_object*, PyImath::FixedArray2D<float>)
__init__(_object*, PyImath::FixedArray2D<int>)
__init__(_object*, double, unsigned long, unsigned long)
__init__(_object*, PyImath::FixedArray2D<double>)
__init__(_object*, unsigned long, unsigned long)

'''      
    ...

class DoubleArray2D:
    def ifelse (self, *args, **kwargs):
      '''
ifelse( (DoubleArray2D)arg1, (IntArray2D)arg2, (float)arg3) -> DoubleArray2D :

    C++ signature :
        PyImath::FixedArray2D<double> ifelse(PyImath::FixedArray2D<double> {lvalue},PyImath::FixedArray2D<int>,double)

ifelse( (DoubleArray2D)arg1, (IntArray2D)arg2, (DoubleArray2D)arg3) -> DoubleArray2D :

    C++ signature :
        PyImath::FixedArray2D<double> ifelse(PyImath::FixedArray2D<double> {lvalue},PyImath::FixedArray2D<int>,PyImath::FixedArray2D<double>)'''
    ...
    def item (self, *args, **kwargs):
      '''
item( (DoubleArray2D)arg1, (int)arg2, (int)arg3) -> float :

    C++ signature :
        double item(PyImath::FixedArray2D<double> {lvalue},long,long)'''
    ...
    def size (self, *args, **kwargs):
      '''
size( (DoubleArray2D)arg1) -> tuple :

    C++ signature :
        boost::python::tuple size(PyImath::FixedArray2D<double> {lvalue})'''
    ...

def DoubleArrayFromBuffer (*args):
      '''

'''      
    ...

def DoubleMatrix (*args):
      '''
__init__(_object*, int, int)

'''      
    ...

class DoubleMatrix:
    def columns (self, *args, **kwargs):
      '''
columns( (DoubleMatrix)arg1) -> int :

    C++ signature :
        int columns(PyImath::FixedMatrix<double> {lvalue})'''
    ...
    def rows (self, *args, **kwargs):
      '''
rows( (DoubleMatrix)arg1) -> int :

    C++ signature :
        int rows(PyImath::FixedMatrix<double> {lvalue})'''
    ...

def EULER_XYX (*args):
      '''

'''      
    ...

def EULER_XYXr (*args):
      '''

'''      
    ...

def EULER_XYZ (*args):
      '''

'''      
    ...

def EULER_XYZr (*args):
      '''

'''      
    ...

def EULER_XZX (*args):
      '''

'''      
    ...

def EULER_XZXr (*args):
      '''

'''      
    ...

def EULER_XZY (*args):
      '''

'''      
    ...

def EULER_XZYr (*args):
      '''

'''      
    ...

def EULER_X_AXIS (*args):
      '''

'''      
    ...

def EULER_YXY (*args):
      '''

'''      
    ...

def EULER_YXYr (*args):
      '''

'''      
    ...

def EULER_YXZ (*args):
      '''

'''      
    ...

def EULER_YXZr (*args):
      '''

'''      
    ...

def EULER_YZX (*args):
      '''

'''      
    ...

def EULER_YZXr (*args):
      '''

'''      
    ...

def EULER_YZY (*args):
      '''

'''      
    ...

def EULER_YZYr (*args):
      '''

'''      
    ...

def EULER_Y_AXIS (*args):
      '''

'''      
    ...

def EULER_ZXY (*args):
      '''

'''      
    ...

def EULER_ZXYr (*args):
      '''

'''      
    ...

def EULER_ZXZ (*args):
      '''

'''      
    ...

def EULER_ZXZr (*args):
      '''

'''      
    ...

def EULER_ZYX (*args):
      '''

'''      
    ...

def EULER_ZYXr (*args):
      '''

'''      
    ...

def EULER_ZYZ (*args):
      '''

'''      
    ...

def EULER_ZYZr (*args):
      '''

'''      
    ...

def EULER_Z_AXIS (*args):
      '''

'''      
    ...

def Eulerd (*args):
      '''
__init__(boost::python::api::object, Imath_3_1::Euler<double>)
__init__(boost::python::api::object, Imath_3_1::Euler<float>)
__init__(boost::python::api::object, Imath_3_1::Quat<double>, int)
__init__(boost::python::api::object, Imath_3_1::Quat<double>)
__init__(boost::python::api::object, Imath_3_1::Quat<double>, Imath_3_1::Euler<float>::Order)
__init__(boost::python::api::object, double, double, double)
__init__(boost::python::api::object, int)
__init__(boost::python::api::object)
__init__(boost::python::api::object, Imath_3_1::Euler<float>::Order)
__init__(boost::python::api::object, Imath_3_1::Matrix44<double>, int)
__init__(boost::python::api::object, Imath_3_1::Matrix44<double>)
__init__(boost::python::api::object, Imath_3_1::Matrix44<double>, Imath_3_1::Euler<float>::Order)
__init__(boost::python::api::object, Imath_3_1::Matrix33<double>, int)
__init__(boost::python::api::object, Imath_3_1::Matrix33<double>)
__init__(boost::python::api::object, Imath_3_1::Matrix33<double>, Imath_3_1::Euler<float>::Order)
__init__(boost::python::api::object, double, double, double, int)
__init__(boost::python::api::object, double, double, double)
__init__(boost::python::api::object, double, double, double, Imath_3_1::Euler<float>::Order)
__init__(boost::python::api::object, Imath_3_1::Vec3<double>, int)
__init__(boost::python::api::object, Imath_3_1::Vec3<double>)
__init__(boost::python::api::object, Imath_3_1::Vec3<double>, Imath_3_1::Euler<float>::Order)
__init__(_object*)
__init__(_object*, Imath_3_1::Euler<double>)

'''      
    ...

class Eulerd:
    def Axis (self, *args, **kwargs):
      '''None'''
    ...
    def Default (self, *args, **kwargs):
      '''None'''
    ...
    def IJKLayout (self, *args, **kwargs):
      '''None'''
    ...
    def InputLayout (self, *args, **kwargs):
      '''None'''
    ...
    def Order (self, *args, **kwargs):
      '''None'''
    ...
    def X (self, *args, **kwargs):
      '''None'''
    ...
    def XYX (self, *args, **kwargs):
      '''None'''
    ...
    def XYXr (self, *args, **kwargs):
      '''None'''
    ...
    def XYZ (self, *args, **kwargs):
      '''None'''
    ...
    def XYZLayout (self, *args, **kwargs):
      '''None'''
    ...
    def XYZr (self, *args, **kwargs):
      '''None'''
    ...
    def XZX (self, *args, **kwargs):
      '''None'''
    ...
    def XZXr (self, *args, **kwargs):
      '''None'''
    ...
    def XZY (self, *args, **kwargs):
      '''None'''
    ...
    def XZYr (self, *args, **kwargs):
      '''None'''
    ...
    def Y (self, *args, **kwargs):
      '''None'''
    ...
    def YXY (self, *args, **kwargs):
      '''None'''
    ...
    def YXYr (self, *args, **kwargs):
      '''None'''
    ...
    def YXZ (self, *args, **kwargs):
      '''None'''
    ...
    def YXZr (self, *args, **kwargs):
      '''None'''
    ...
    def YZX (self, *args, **kwargs):
      '''None'''
    ...
    def YZXr (self, *args, **kwargs):
      '''None'''
    ...
    def YZY (self, *args, **kwargs):
      '''None'''
    ...
    def YZYr (self, *args, **kwargs):
      '''None'''
    ...
    def Z (self, *args, **kwargs):
      '''None'''
    ...
    def ZXY (self, *args, **kwargs):
      '''None'''
    ...
    def ZXYr (self, *args, **kwargs):
      '''None'''
    ...
    def ZXZ (self, *args, **kwargs):
      '''None'''
    ...
    def ZXZr (self, *args, **kwargs):
      '''None'''
    ...
    def ZYX (self, *args, **kwargs):
      '''None'''
    ...
    def ZYXr (self, *args, **kwargs):
      '''None'''
    ...
    def ZYZ (self, *args, **kwargs):
      '''None'''
    ...
    def ZYZr (self, *args, **kwargs):
      '''None'''
    ...
    def angleOrder (self, *args, **kwargs):
      '''
angleOrder( (Eulerd)arg1) -> V3i :
    angleOrder() set the angle order

    C++ signature :
        Imath_3_1::Vec3<int> angleOrder(Imath_3_1::Euler<double> {lvalue})'''
    ...
    def baseTypeEpsilon (self, *args, **kwargs):
      '''
baseTypeEpsilon() -> float :
    baseTypeEpsilon() epsilon value of the base type of the vector

    C++ signature :
        double baseTypeEpsilon()'''
    ...
    def baseTypeLowest (self, *args, **kwargs):
      '''
baseTypeLowest() -> float :
    baseTypeLowest() largest negative value of the base type of the vector

    C++ signature :
        double baseTypeLowest()'''
    ...
    def baseTypeMax (self, *args, **kwargs):
      '''
baseTypeMax() -> float :
    baseTypeMax() max value of the base type of the vector

    C++ signature :
        double baseTypeMax()'''
    ...
    def baseTypeSmallest (self, *args, **kwargs):
      '''
baseTypeSmallest() -> float :
    baseTypeSmallest() smallest value of the base type of the vector

    C++ signature :
        double baseTypeSmallest()'''
    ...
    def closestVertex (self, *args, **kwargs):
      '''
closestVertex( (V3d)arg1, (V3d)arg2, (V3d)arg3, (V3d)arg4) -> V3d :

    C++ signature :
        Imath_3_1::Vec3<double> closestVertex(Imath_3_1::Vec3<double> {lvalue},Imath_3_1::Vec3<double>,Imath_3_1::Vec3<double>,Imath_3_1::Vec3<double>)'''
    ...
    def cross (self, *args, **kwargs):
      '''
cross( (V3d)arg1, (V3d)arg2) -> V3d :
    v1.cross(v2) right handed cross product

    C++ signature :
        Imath_3_1::Vec3<double> cross(Imath_3_1::Vec3<double>,Imath_3_1::Vec3<double>)

cross( (V3d)arg1, (V3dArray)arg2) -> V3dArray :
    v1.cross(v2) right handed array cross product

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec3<double> > cross(Imath_3_1::Vec3<double>,PyImath::FixedArray<Imath_3_1::Vec3<double> >)'''
    ...
    def dimensions (self, *args, **kwargs):
      '''
dimensions() -> int :
    dimensions() number of dimensions in the vector

    C++ signature :
        unsigned int dimensions()'''
    ...
    def dot (self, *args, **kwargs):
      '''
dot( (V3d)arg1, (V3d)arg2) -> float :
    v1.dot(v2) inner product of the two vectors

    C++ signature :
        double dot(Imath_3_1::Vec3<double>,Imath_3_1::Vec3<double>)

dot( (V3d)arg1, (V3dArray)arg2) -> DoubleArray :
    v1.dot(v2) array inner product

    C++ signature :
        PyImath::FixedArray<double> dot(Imath_3_1::Vec3<double>,PyImath::FixedArray<Imath_3_1::Vec3<double> >)'''
    ...
    def equalWithAbsError (self, *args, **kwargs):
      '''
equalWithAbsError( (V3d)arg1, (V3d)arg2, (float)arg3) -> bool :
    v1.equalWithAbsError(v2) true if the elements of v1 and v2 are the same with an absolute error of no more than e, i.e., abs(v1[i] - v2[i]) <= e

    C++ signature :
        bool equalWithAbsError(Imath_3_1::Vec3<double> {lvalue},Imath_3_1::Vec3<double>,double)

equalWithAbsError( (V3d)arg1, (object)arg2, (object)arg3) -> bool :

    C++ signature :
        bool equalWithAbsError(Imath_3_1::Vec3<double>,boost::python::api::object,boost::python::api::object)'''
    ...
    def equalWithRelError (self, *args, **kwargs):
      '''
equalWithRelError( (V3d)arg1, (V3d)arg2, (float)arg3) -> bool :
    v1.equalWithAbsError(v2) true if the elements of v1 and v2 are the same with an absolute error of no more than e, i.e., abs(v1[i] - v2[i]) <= e * abs(v1[i])

    C++ signature :
        bool equalWithRelError(Imath_3_1::Vec3<double> {lvalue},Imath_3_1::Vec3<double>,double)

equalWithRelError( (V3d)arg1, (object)arg2, (object)arg3) -> bool :

    C++ signature :
        bool equalWithRelError(Imath_3_1::Vec3<double>,boost::python::api::object,boost::python::api::object)'''
    ...
    def extract (self, *args, **kwargs):
      '''
extract( (Eulerd)arg1, (M33d)arg2) -> None :
    e.extract(m) -- extracts the rotation component
    from 3x3 matrix m and stores the result in e.
    Assumes that m does not contain shear or non-
    uniform scaling.  If necessary, you can fix m
    by calling m.removeScalingAndShear().

    C++ signature :
        void extract(Imath_3_1::Euler<double> {lvalue},Imath_3_1::Matrix33<double>)

extract( (Eulerd)arg1, (M44d)arg2) -> None :
    e.extract(m) -- extracts the rotation component
    from 4x4 matrix m and stores the result in e.
    Assumes that m does not contain shear or non-
    uniform scaling.  If necessary, you can fix m
    by calling m.removeScalingAndShear().

    C++ signature :
        void extract(Imath_3_1::Euler<double> {lvalue},Imath_3_1::Matrix44<double>)

extract( (Eulerd)arg1, (Quatd)arg2) -> None :
    e.extract(q) -- extracts the rotation component
    from quaternion q and stores the result in e

    C++ signature :
        void extract(Imath_3_1::Euler<double> {lvalue},Imath_3_1::Quat<double>)'''
    ...
    def frameStatic (self, *args, **kwargs):
      '''
frameStatic( (Eulerd)arg1) -> bool :
    e.frameStatic() -- returns true if the angles of e
    are measured relative to a set of fixed axes,
    or false if the angles of e are measured relative to
    each other
    

    C++ signature :
        bool frameStatic(Imath_3_1::Euler<double> {lvalue})'''
    ...
    def initialAxis (self, *args, **kwargs):
      '''
initialAxis( (Eulerd)arg1) -> Axis :
    e.initialAxis() -- returns the initial rotation
    axis of e (EULER_X_AXIS, EULER_Y_AXIS, EULER_Z_AXIS)

    C++ signature :
        Imath_3_1::Euler<double>::Axis initialAxis(Imath_3_1::Euler<double> {lvalue})'''
    ...
    def initialRepeated (self, *args, **kwargs):
      '''
initialRepeated( (Eulerd)arg1) -> bool :
    e.initialRepeated() -- returns 1 if the initial
    rotation axis of e is repeated (for example,
    e.order() == EULER_XYX); returns 0 if the initial
    rotation axis is not repeated.
    

    C++ signature :
        bool initialRepeated(Imath_3_1::Euler<double> {lvalue})'''
    ...
    def length (self, *args, **kwargs):
      '''
length( (V3d)arg1) -> float :
    length() magnitude of the vector

    C++ signature :
        double length(Imath_3_1::Vec3<double>)'''
    ...
    def length2 (self, *args, **kwargs):
      '''
length2( (V3d)arg1) -> float :
    length2() square magnitude of the vector

    C++ signature :
        double length2(Imath_3_1::Vec3<double>)'''
    ...
    def makeNear (self, *args, **kwargs):
      '''
makeNear( (Eulerd)arg1, (Eulerd)arg2) -> None :
    e.makeNear(t) -- adjusts Euler e so that it
    represents the same rotation as before, but the
    individual angles of e differ from the angles of
    t by as little as possible.
    This method might not make sense if e.order()
    and t.order() are different
    

    C++ signature :
        void makeNear(Imath_3_1::Euler<double> {lvalue},Imath_3_1::Euler<double> {lvalue})'''
    ...
    def negate (self, *args, **kwargs):
      '''
negate( (V3d)arg1) -> V3d :

    C++ signature :
        Imath_3_1::Vec3<double> negate(Imath_3_1::Vec3<double> {lvalue})'''
    ...
    def normalize (self, *args, **kwargs):
      '''
normalize( (V3d)arg1) -> V3d :
    v.normalize() destructively normalizes v and returns a reference to it

    C++ signature :
        Imath_3_1::Vec3<double> normalize(Imath_3_1::Vec3<double> {lvalue})'''
    ...
    def normalizeExc (self, *args, **kwargs):
      '''
normalizeExc( (V3d)arg1) -> V3d :
    v.normalizeExc() destructively normalizes V and returns a reference to it, throwing an exception if length() == 0

    C++ signature :
        Imath_3_1::Vec3<double> normalizeExc(Imath_3_1::Vec3<double> {lvalue})'''
    ...
    def normalizeNonNull (self, *args, **kwargs):
      '''
normalizeNonNull( (V3d)arg1) -> V3d :
    v.normalizeNonNull() destructively normalizes V and returns a reference to it, faster if lngth() != 0

    C++ signature :
        Imath_3_1::Vec3<double> normalizeNonNull(Imath_3_1::Vec3<double> {lvalue})'''
    ...
    def normalized (self, *args, **kwargs):
      '''
normalized( (V3d)arg1) -> V3d :
    v.normalized() returns a normalized copy of v

    C++ signature :
        Imath_3_1::Vec3<double> normalized(Imath_3_1::Vec3<double>)'''
    ...
    def normalizedExc (self, *args, **kwargs):
      '''
normalizedExc( (V3d)arg1) -> V3d :
    v.normalizedExc() returns a normalized copy of v, throwing an exception if length() == 0

    C++ signature :
        Imath_3_1::Vec3<double> normalizedExc(Imath_3_1::Vec3<double>)'''
    ...
    def normalizedNonNull (self, *args, **kwargs):
      '''
normalizedNonNull( (V3d)arg1) -> V3d :
    v.normalizedNonNull() returns a normalized copy of v, faster if lngth() != 0

    C++ signature :
        Imath_3_1::Vec3<double> normalizedNonNull(Imath_3_1::Vec3<double>)'''
    ...
    def order (self, *args, **kwargs):
      '''
order( (Eulerd)arg1) -> Order :
    e.order() -- returns the rotation order in e
    (EULER_XYZ, EULER_XZY, ...)

    C++ signature :
        Imath_3_1::Euler<double>::Order order(Imath_3_1::Euler<double> {lvalue})'''
    ...
    def orthogonal (self, *args, **kwargs):
      '''
orthogonal( (V3d)arg1, (V3d)arg2) -> V3d :

    C++ signature :
        Imath_3_1::Vec3<double> orthogonal(Imath_3_1::Vec3<double>,Imath_3_1::Vec3<double>)'''
    ...
    def parityEven (self, *args, **kwargs):
      '''
parityEven( (Eulerd)arg1) -> bool :
    e.parityEven() -- returns the parity of the
    axis permutation of e
    

    C++ signature :
        bool parityEven(Imath_3_1::Euler<double> {lvalue})'''
    ...
    def project (self, *args, **kwargs):
      '''
project( (V3d)arg1, (V3d)arg2) -> V3d :

    C++ signature :
        Imath_3_1::Vec3<double> project(Imath_3_1::Vec3<double>,Imath_3_1::Vec3<double>)'''
    ...
    def reflect (self, *args, **kwargs):
      '''
reflect( (V3d)arg1, (V3d)arg2) -> V3d :

    C++ signature :
        Imath_3_1::Vec3<double> reflect(Imath_3_1::Vec3<double>,Imath_3_1::Vec3<double>)'''
    ...
    def set (self, *args, **kwargs):
      '''
set( (Eulerd)arg1, (Axis)arg2, (int)arg3, (int)arg4, (int)arg5) -> None :
    e.set(i,r,p,f) -- sets the rotation order in e
    according to the following flags:
    
       i   initial axis (EULER_X_AXIS,
           EULER_Y_AXIS or EULER_Z_AXIS)
    
       r   rotation angles are measured relative
           to each other (r == 1), or relative to a
           set of fixed axes (r == 0)
    
       p   parity of axis permutation is even (r == 1)
           or odd (r == 0)
    
       f   first rotation axis is repeated (f == 1)
    	or not repeated (f == 0)
    

    C++ signature :
        void set(Imath_3_1::Euler<double> {lvalue},Imath_3_1::Euler<float>::Axis,int,int,int)'''
    ...
    def setOrder (self, *args, **kwargs):
      '''
setOrder( (Eulerd)arg1, (Order)arg2) -> None :
    e.setOrder(o) -- sets the rotation order in e
    to o (EULER_XYZ, EULER_XZY, ...)

    C++ signature :
        void setOrder(Imath_3_1::Euler<double> {lvalue},Imath_3_1::Euler<float>::Order)'''
    ...
    def setValue (self, *args, **kwargs):
      '''
setValue( (V3d)arg1, (float)arg2, (float)arg3, (float)arg4) -> None :

    C++ signature :
        void setValue(Imath_3_1::Vec3<double> {lvalue},double,double,double)'''
    ...
    def setXYZVector (self, *args, **kwargs):
      '''
setXYZVector( (Eulerd)arg1, (V3d)arg2) -> None :
    e.setXYZVector(v) -- sets the three rotation
    angles in e to v[0], v[1], v[2]

    C++ signature :
        void setXYZVector(Imath_3_1::Euler<double> {lvalue},Imath_3_1::Vec3<double>)

setXYZVector( (Eulerd)arg1, (tuple)arg2) -> None :

    C++ signature :
        void setXYZVector(Imath_3_1::Euler<double> {lvalue},boost::python::tuple)'''
    ...
    def toMatrix33 (self, *args, **kwargs):
      '''
toMatrix33( (Eulerd)arg1) -> M33d :
    e.toMatrix33() -- converts e into a 3x3 matrix
    

    C++ signature :
        Imath_3_1::Matrix33<double> toMatrix33(Imath_3_1::Euler<double> {lvalue})'''
    ...
    def toMatrix44 (self, *args, **kwargs):
      '''
toMatrix44( (Eulerd)arg1) -> M44d :
    e.toMatrix44() -- converts e into a 4x4 matrix
    

    C++ signature :
        Imath_3_1::Matrix44<double> toMatrix44(Imath_3_1::Euler<double> {lvalue})'''
    ...
    def toQuat (self, *args, **kwargs):
      '''
toQuat( (Eulerd)arg1) -> Quatd :
    e.toQuat() -- converts e into a quaternion
    

    C++ signature :
        Imath_3_1::Quat<double> toQuat(Imath_3_1::Euler<double> {lvalue})'''
    ...
    def toXYZVector (self, *args, **kwargs):
      '''
toXYZVector( (Eulerd)arg1) -> V3d :
    e.toXYZVector() -- converts e into an XYZ
    rotation vector

    C++ signature :
        Imath_3_1::Vec3<double> toXYZVector(Imath_3_1::Euler<double> {lvalue})'''
    ...
    def x (self, *args, **kwargs):
      '''None'''
    ...
    def y (self, *args, **kwargs):
      '''None'''
    ...
    def z (self, *args, **kwargs):
      '''None'''
    ...

def EulerdArray (*args):
      '''
__init__(_object*, PyImath::FixedArray<Imath_3_1::Euler<float> >)
__init__(_object*, PyImath::FixedArray<Imath_3_1::Matrix44<double> >)
__init__(_object*, PyImath::FixedArray<Imath_3_1::Matrix33<double> >)
__init__(boost::python::api::object, PyImath::FixedArray<Imath_3_1::Vec3<double> >, Imath_3_1::Euler<float>::Order)
__init__(boost::python::api::object, PyImath::FixedArray<Imath_3_1::Vec3<double> >)
__init__(boost::python::api::object, PyImath::FixedArray<Imath_3_1::Quat<double> >)
__init__(_object*, Imath_3_1::Euler<double>, unsigned long)
__init__(_object*, PyImath::FixedArray<Imath_3_1::Euler<double> >)
__init__(_object*, unsigned long)

'''      
    ...

class EulerdArray:
    def ifelse (self, *args, **kwargs):
      '''
ifelse( (EulerdArray)arg1, (IntArray)arg2, (Eulerd)arg3) -> EulerdArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Euler<double> > ifelse(PyImath::FixedArray<Imath_3_1::Euler<double> > {lvalue},PyImath::FixedArray<int>,Imath_3_1::Euler<double>)

ifelse( (EulerdArray)arg1, (IntArray)arg2, (EulerdArray)arg3) -> EulerdArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Euler<double> > ifelse(PyImath::FixedArray<Imath_3_1::Euler<double> > {lvalue},PyImath::FixedArray<int>,PyImath::FixedArray<Imath_3_1::Euler<double> >)'''
    ...
    def makeReadOnly (self, *args, **kwargs):
      '''
makeReadOnly( (EulerdArray)arg1) -> None :

    C++ signature :
        void makeReadOnly(PyImath::FixedArray<Imath_3_1::Euler<double> > {lvalue})'''
    ...
    def toQuat (self, *args, **kwargs):
      '''
toQuat( (EulerdArray)arg1) -> QuatdArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Quat<double> > toQuat(PyImath::FixedArray<Imath_3_1::Euler<double> >)'''
    ...
    def toXYZVector (self, *args, **kwargs):
      '''
toXYZVector( (EulerdArray)arg1) -> V3dArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec3<double> > toXYZVector(PyImath::FixedArray<Imath_3_1::Euler<double> >)'''
    ...
    def writable (self, *args, **kwargs):
      '''
writable( (EulerdArray)arg1) -> bool :

    C++ signature :
        bool writable(PyImath::FixedArray<Imath_3_1::Euler<double> > {lvalue})'''
    ...

def Eulerf (*args):
      '''
__init__(boost::python::api::object, Imath_3_1::Euler<double>)
__init__(boost::python::api::object, Imath_3_1::Euler<float>)
__init__(boost::python::api::object, Imath_3_1::Quat<float>, int)
__init__(boost::python::api::object, Imath_3_1::Quat<float>)
__init__(boost::python::api::object, Imath_3_1::Quat<float>, Imath_3_1::Euler<float>::Order)
__init__(boost::python::api::object, float, float, float)
__init__(boost::python::api::object, int)
__init__(boost::python::api::object)
__init__(boost::python::api::object, Imath_3_1::Euler<float>::Order)
__init__(boost::python::api::object, Imath_3_1::Matrix44<float>, int)
__init__(boost::python::api::object, Imath_3_1::Matrix44<float>)
__init__(boost::python::api::object, Imath_3_1::Matrix44<float>, Imath_3_1::Euler<float>::Order)
__init__(boost::python::api::object, Imath_3_1::Matrix33<float>, int)
__init__(boost::python::api::object, Imath_3_1::Matrix33<float>)
__init__(boost::python::api::object, Imath_3_1::Matrix33<float>, Imath_3_1::Euler<float>::Order)
__init__(boost::python::api::object, float, float, float, int)
__init__(boost::python::api::object, float, float, float)
__init__(boost::python::api::object, float, float, float, Imath_3_1::Euler<float>::Order)
__init__(boost::python::api::object, Imath_3_1::Vec3<float>, int)
__init__(boost::python::api::object, Imath_3_1::Vec3<float>)
__init__(boost::python::api::object, Imath_3_1::Vec3<float>, Imath_3_1::Euler<float>::Order)
__init__(_object*)
__init__(_object*, Imath_3_1::Euler<float>)

'''      
    ...

class Eulerf:
    def Axis (self, *args, **kwargs):
      '''None'''
    ...
    def Default (self, *args, **kwargs):
      '''None'''
    ...
    def IJKLayout (self, *args, **kwargs):
      '''None'''
    ...
    def InputLayout (self, *args, **kwargs):
      '''None'''
    ...
    def Order (self, *args, **kwargs):
      '''None'''
    ...
    def X (self, *args, **kwargs):
      '''None'''
    ...
    def XYX (self, *args, **kwargs):
      '''None'''
    ...
    def XYXr (self, *args, **kwargs):
      '''None'''
    ...
    def XYZ (self, *args, **kwargs):
      '''None'''
    ...
    def XYZLayout (self, *args, **kwargs):
      '''None'''
    ...
    def XYZr (self, *args, **kwargs):
      '''None'''
    ...
    def XZX (self, *args, **kwargs):
      '''None'''
    ...
    def XZXr (self, *args, **kwargs):
      '''None'''
    ...
    def XZY (self, *args, **kwargs):
      '''None'''
    ...
    def XZYr (self, *args, **kwargs):
      '''None'''
    ...
    def Y (self, *args, **kwargs):
      '''None'''
    ...
    def YXY (self, *args, **kwargs):
      '''None'''
    ...
    def YXYr (self, *args, **kwargs):
      '''None'''
    ...
    def YXZ (self, *args, **kwargs):
      '''None'''
    ...
    def YXZr (self, *args, **kwargs):
      '''None'''
    ...
    def YZX (self, *args, **kwargs):
      '''None'''
    ...
    def YZXr (self, *args, **kwargs):
      '''None'''
    ...
    def YZY (self, *args, **kwargs):
      '''None'''
    ...
    def YZYr (self, *args, **kwargs):
      '''None'''
    ...
    def Z (self, *args, **kwargs):
      '''None'''
    ...
    def ZXY (self, *args, **kwargs):
      '''None'''
    ...
    def ZXYr (self, *args, **kwargs):
      '''None'''
    ...
    def ZXZ (self, *args, **kwargs):
      '''None'''
    ...
    def ZXZr (self, *args, **kwargs):
      '''None'''
    ...
    def ZYX (self, *args, **kwargs):
      '''None'''
    ...
    def ZYXr (self, *args, **kwargs):
      '''None'''
    ...
    def ZYZ (self, *args, **kwargs):
      '''None'''
    ...
    def ZYZr (self, *args, **kwargs):
      '''None'''
    ...
    def angleOrder (self, *args, **kwargs):
      '''
angleOrder( (Eulerf)arg1) -> V3i :
    angleOrder() set the angle order

    C++ signature :
        Imath_3_1::Vec3<int> angleOrder(Imath_3_1::Euler<float> {lvalue})'''
    ...
    def baseTypeEpsilon (self, *args, **kwargs):
      '''
baseTypeEpsilon() -> float :
    baseTypeEpsilon() epsilon value of the base type of the vector

    C++ signature :
        float baseTypeEpsilon()'''
    ...
    def baseTypeLowest (self, *args, **kwargs):
      '''
baseTypeLowest() -> float :
    baseTypeLowest() largest negative value of the base type of the vector

    C++ signature :
        float baseTypeLowest()'''
    ...
    def baseTypeMax (self, *args, **kwargs):
      '''
baseTypeMax() -> float :
    baseTypeMax() max value of the base type of the vector

    C++ signature :
        float baseTypeMax()'''
    ...
    def baseTypeSmallest (self, *args, **kwargs):
      '''
baseTypeSmallest() -> float :
    baseTypeSmallest() smallest value of the base type of the vector

    C++ signature :
        float baseTypeSmallest()'''
    ...
    def closestVertex (self, *args, **kwargs):
      '''
closestVertex( (V3f)arg1, (V3f)arg2, (V3f)arg3, (V3f)arg4) -> V3f :

    C++ signature :
        Imath_3_1::Vec3<float> closestVertex(Imath_3_1::Vec3<float> {lvalue},Imath_3_1::Vec3<float>,Imath_3_1::Vec3<float>,Imath_3_1::Vec3<float>)'''
    ...
    def cross (self, *args, **kwargs):
      '''
cross( (V3f)arg1, (V3f)arg2) -> V3f :
    v1.cross(v2) right handed cross product

    C++ signature :
        Imath_3_1::Vec3<float> cross(Imath_3_1::Vec3<float>,Imath_3_1::Vec3<float>)

cross( (V3f)arg1, (V3fArray)arg2) -> V3fArray :
    v1.cross(v2) right handed array cross product

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec3<float> > cross(Imath_3_1::Vec3<float>,PyImath::FixedArray<Imath_3_1::Vec3<float> >)'''
    ...
    def dimensions (self, *args, **kwargs):
      '''
dimensions() -> int :
    dimensions() number of dimensions in the vector

    C++ signature :
        unsigned int dimensions()'''
    ...
    def dot (self, *args, **kwargs):
      '''
dot( (V3f)arg1, (V3f)arg2) -> float :
    v1.dot(v2) inner product of the two vectors

    C++ signature :
        float dot(Imath_3_1::Vec3<float>,Imath_3_1::Vec3<float>)

dot( (V3f)arg1, (V3fArray)arg2) -> FloatArray :
    v1.dot(v2) array inner product

    C++ signature :
        PyImath::FixedArray<float> dot(Imath_3_1::Vec3<float>,PyImath::FixedArray<Imath_3_1::Vec3<float> >)'''
    ...
    def equalWithAbsError (self, *args, **kwargs):
      '''
equalWithAbsError( (V3f)arg1, (V3f)arg2, (float)arg3) -> bool :
    v1.equalWithAbsError(v2) true if the elements of v1 and v2 are the same with an absolute error of no more than e, i.e., abs(v1[i] - v2[i]) <= e

    C++ signature :
        bool equalWithAbsError(Imath_3_1::Vec3<float> {lvalue},Imath_3_1::Vec3<float>,float)

equalWithAbsError( (V3f)arg1, (object)arg2, (object)arg3) -> bool :

    C++ signature :
        bool equalWithAbsError(Imath_3_1::Vec3<float>,boost::python::api::object,boost::python::api::object)'''
    ...
    def equalWithRelError (self, *args, **kwargs):
      '''
equalWithRelError( (V3f)arg1, (V3f)arg2, (float)arg3) -> bool :
    v1.equalWithAbsError(v2) true if the elements of v1 and v2 are the same with an absolute error of no more than e, i.e., abs(v1[i] - v2[i]) <= e * abs(v1[i])

    C++ signature :
        bool equalWithRelError(Imath_3_1::Vec3<float> {lvalue},Imath_3_1::Vec3<float>,float)

equalWithRelError( (V3f)arg1, (object)arg2, (object)arg3) -> bool :

    C++ signature :
        bool equalWithRelError(Imath_3_1::Vec3<float>,boost::python::api::object,boost::python::api::object)'''
    ...
    def extract (self, *args, **kwargs):
      '''
extract( (Eulerf)arg1, (M33f)arg2) -> None :
    e.extract(m) -- extracts the rotation component
    from 3x3 matrix m and stores the result in e.
    Assumes that m does not contain shear or non-
    uniform scaling.  If necessary, you can fix m
    by calling m.removeScalingAndShear().

    C++ signature :
        void extract(Imath_3_1::Euler<float> {lvalue},Imath_3_1::Matrix33<float>)

extract( (Eulerf)arg1, (M44f)arg2) -> None :
    e.extract(m) -- extracts the rotation component
    from 4x4 matrix m and stores the result in e.
    Assumes that m does not contain shear or non-
    uniform scaling.  If necessary, you can fix m
    by calling m.removeScalingAndShear().

    C++ signature :
        void extract(Imath_3_1::Euler<float> {lvalue},Imath_3_1::Matrix44<float>)

extract( (Eulerf)arg1, (Quatf)arg2) -> None :
    e.extract(q) -- extracts the rotation component
    from quaternion q and stores the result in e

    C++ signature :
        void extract(Imath_3_1::Euler<float> {lvalue},Imath_3_1::Quat<float>)'''
    ...
    def frameStatic (self, *args, **kwargs):
      '''
frameStatic( (Eulerf)arg1) -> bool :
    e.frameStatic() -- returns true if the angles of e
    are measured relative to a set of fixed axes,
    or false if the angles of e are measured relative to
    each other
    

    C++ signature :
        bool frameStatic(Imath_3_1::Euler<float> {lvalue})'''
    ...
    def initialAxis (self, *args, **kwargs):
      '''
initialAxis( (Eulerf)arg1) -> Axis :
    e.initialAxis() -- returns the initial rotation
    axis of e (EULER_X_AXIS, EULER_Y_AXIS, EULER_Z_AXIS)

    C++ signature :
        Imath_3_1::Euler<float>::Axis initialAxis(Imath_3_1::Euler<float> {lvalue})'''
    ...
    def initialRepeated (self, *args, **kwargs):
      '''
initialRepeated( (Eulerf)arg1) -> bool :
    e.initialRepeated() -- returns 1 if the initial
    rotation axis of e is repeated (for example,
    e.order() == EULER_XYX); returns 0 if the initial
    rotation axis is not repeated.
    

    C++ signature :
        bool initialRepeated(Imath_3_1::Euler<float> {lvalue})'''
    ...
    def length (self, *args, **kwargs):
      '''
length( (V3f)arg1) -> float :
    length() magnitude of the vector

    C++ signature :
        float length(Imath_3_1::Vec3<float>)'''
    ...
    def length2 (self, *args, **kwargs):
      '''
length2( (V3f)arg1) -> float :
    length2() square magnitude of the vector

    C++ signature :
        float length2(Imath_3_1::Vec3<float>)'''
    ...
    def makeNear (self, *args, **kwargs):
      '''
makeNear( (Eulerf)arg1, (Eulerf)arg2) -> None :
    e.makeNear(t) -- adjusts Euler e so that it
    represents the same rotation as before, but the
    individual angles of e differ from the angles of
    t by as little as possible.
    This method might not make sense if e.order()
    and t.order() are different
    

    C++ signature :
        void makeNear(Imath_3_1::Euler<float> {lvalue},Imath_3_1::Euler<float> {lvalue})'''
    ...
    def negate (self, *args, **kwargs):
      '''
negate( (V3f)arg1) -> V3f :

    C++ signature :
        Imath_3_1::Vec3<float> negate(Imath_3_1::Vec3<float> {lvalue})'''
    ...
    def normalize (self, *args, **kwargs):
      '''
normalize( (V3f)arg1) -> V3f :
    v.normalize() destructively normalizes v and returns a reference to it

    C++ signature :
        Imath_3_1::Vec3<float> normalize(Imath_3_1::Vec3<float> {lvalue})'''
    ...
    def normalizeExc (self, *args, **kwargs):
      '''
normalizeExc( (V3f)arg1) -> V3f :
    v.normalizeExc() destructively normalizes V and returns a reference to it, throwing an exception if length() == 0

    C++ signature :
        Imath_3_1::Vec3<float> normalizeExc(Imath_3_1::Vec3<float> {lvalue})'''
    ...
    def normalizeNonNull (self, *args, **kwargs):
      '''
normalizeNonNull( (V3f)arg1) -> V3f :
    v.normalizeNonNull() destructively normalizes V and returns a reference to it, faster if lngth() != 0

    C++ signature :
        Imath_3_1::Vec3<float> normalizeNonNull(Imath_3_1::Vec3<float> {lvalue})'''
    ...
    def normalized (self, *args, **kwargs):
      '''
normalized( (V3f)arg1) -> V3f :
    v.normalized() returns a normalized copy of v

    C++ signature :
        Imath_3_1::Vec3<float> normalized(Imath_3_1::Vec3<float>)'''
    ...
    def normalizedExc (self, *args, **kwargs):
      '''
normalizedExc( (V3f)arg1) -> V3f :
    v.normalizedExc() returns a normalized copy of v, throwing an exception if length() == 0

    C++ signature :
        Imath_3_1::Vec3<float> normalizedExc(Imath_3_1::Vec3<float>)'''
    ...
    def normalizedNonNull (self, *args, **kwargs):
      '''
normalizedNonNull( (V3f)arg1) -> V3f :
    v.normalizedNonNull() returns a normalized copy of v, faster if lngth() != 0

    C++ signature :
        Imath_3_1::Vec3<float> normalizedNonNull(Imath_3_1::Vec3<float>)'''
    ...
    def order (self, *args, **kwargs):
      '''
order( (Eulerf)arg1) -> Order :
    e.order() -- returns the rotation order in e
    (EULER_XYZ, EULER_XZY, ...)

    C++ signature :
        Imath_3_1::Euler<float>::Order order(Imath_3_1::Euler<float> {lvalue})'''
    ...
    def orthogonal (self, *args, **kwargs):
      '''
orthogonal( (V3f)arg1, (V3f)arg2) -> V3f :

    C++ signature :
        Imath_3_1::Vec3<float> orthogonal(Imath_3_1::Vec3<float>,Imath_3_1::Vec3<float>)'''
    ...
    def parityEven (self, *args, **kwargs):
      '''
parityEven( (Eulerf)arg1) -> bool :
    e.parityEven() -- returns the parity of the
    axis permutation of e
    

    C++ signature :
        bool parityEven(Imath_3_1::Euler<float> {lvalue})'''
    ...
    def project (self, *args, **kwargs):
      '''
project( (V3f)arg1, (V3f)arg2) -> V3f :

    C++ signature :
        Imath_3_1::Vec3<float> project(Imath_3_1::Vec3<float>,Imath_3_1::Vec3<float>)'''
    ...
    def reflect (self, *args, **kwargs):
      '''
reflect( (V3f)arg1, (V3f)arg2) -> V3f :

    C++ signature :
        Imath_3_1::Vec3<float> reflect(Imath_3_1::Vec3<float>,Imath_3_1::Vec3<float>)'''
    ...
    def set (self, *args, **kwargs):
      '''
set( (Eulerf)arg1, (Axis)arg2, (int)arg3, (int)arg4, (int)arg5) -> None :
    e.set(i,r,p,f) -- sets the rotation order in e
    according to the following flags:
    
       i   initial axis (EULER_X_AXIS,
           EULER_Y_AXIS or EULER_Z_AXIS)
    
       r   rotation angles are measured relative
           to each other (r == 1), or relative to a
           set of fixed axes (r == 0)
    
       p   parity of axis permutation is even (r == 1)
           or odd (r == 0)
    
       f   first rotation axis is repeated (f == 1)
    	or not repeated (f == 0)
    

    C++ signature :
        void set(Imath_3_1::Euler<float> {lvalue},Imath_3_1::Euler<float>::Axis,int,int,int)'''
    ...
    def setOrder (self, *args, **kwargs):
      '''
setOrder( (Eulerf)arg1, (Order)arg2) -> None :
    e.setOrder(o) -- sets the rotation order in e
    to o (EULER_XYZ, EULER_XZY, ...)

    C++ signature :
        void setOrder(Imath_3_1::Euler<float> {lvalue},Imath_3_1::Euler<float>::Order)'''
    ...
    def setValue (self, *args, **kwargs):
      '''
setValue( (V3f)arg1, (float)arg2, (float)arg3, (float)arg4) -> None :

    C++ signature :
        void setValue(Imath_3_1::Vec3<float> {lvalue},float,float,float)'''
    ...
    def setXYZVector (self, *args, **kwargs):
      '''
setXYZVector( (Eulerf)arg1, (V3f)arg2) -> None :
    e.setXYZVector(v) -- sets the three rotation
    angles in e to v[0], v[1], v[2]

    C++ signature :
        void setXYZVector(Imath_3_1::Euler<float> {lvalue},Imath_3_1::Vec3<float>)

setXYZVector( (Eulerf)arg1, (tuple)arg2) -> None :

    C++ signature :
        void setXYZVector(Imath_3_1::Euler<float> {lvalue},boost::python::tuple)'''
    ...
    def toMatrix33 (self, *args, **kwargs):
      '''
toMatrix33( (Eulerf)arg1) -> M33f :
    e.toMatrix33() -- converts e into a 3x3 matrix
    

    C++ signature :
        Imath_3_1::Matrix33<float> toMatrix33(Imath_3_1::Euler<float> {lvalue})'''
    ...
    def toMatrix44 (self, *args, **kwargs):
      '''
toMatrix44( (Eulerf)arg1) -> M44f :
    e.toMatrix44() -- converts e into a 4x4 matrix
    

    C++ signature :
        Imath_3_1::Matrix44<float> toMatrix44(Imath_3_1::Euler<float> {lvalue})'''
    ...
    def toQuat (self, *args, **kwargs):
      '''
toQuat( (Eulerf)arg1) -> Quatf :
    e.toQuat() -- converts e into a quaternion
    

    C++ signature :
        Imath_3_1::Quat<float> toQuat(Imath_3_1::Euler<float> {lvalue})'''
    ...
    def toXYZVector (self, *args, **kwargs):
      '''
toXYZVector( (Eulerf)arg1) -> V3f :
    e.toXYZVector() -- converts e into an XYZ
    rotation vector

    C++ signature :
        Imath_3_1::Vec3<float> toXYZVector(Imath_3_1::Euler<float> {lvalue})'''
    ...
    def x (self, *args, **kwargs):
      '''None'''
    ...
    def y (self, *args, **kwargs):
      '''None'''
    ...
    def z (self, *args, **kwargs):
      '''None'''
    ...

def EulerfArray (*args):
      '''
__init__(_object*, PyImath::FixedArray<Imath_3_1::Euler<double> >)
__init__(_object*, PyImath::FixedArray<Imath_3_1::Matrix44<float> >)
__init__(_object*, PyImath::FixedArray<Imath_3_1::Matrix33<float> >)
__init__(boost::python::api::object, PyImath::FixedArray<Imath_3_1::Vec3<float> >, Imath_3_1::Euler<float>::Order)
__init__(boost::python::api::object, PyImath::FixedArray<Imath_3_1::Vec3<float> >)
__init__(boost::python::api::object, PyImath::FixedArray<Imath_3_1::Quat<float> >)
__init__(_object*, Imath_3_1::Euler<float>, unsigned long)
__init__(_object*, PyImath::FixedArray<Imath_3_1::Euler<float> >)
__init__(_object*, unsigned long)

'''      
    ...

class EulerfArray:
    def ifelse (self, *args, **kwargs):
      '''
ifelse( (EulerfArray)arg1, (IntArray)arg2, (Eulerf)arg3) -> EulerfArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Euler<float> > ifelse(PyImath::FixedArray<Imath_3_1::Euler<float> > {lvalue},PyImath::FixedArray<int>,Imath_3_1::Euler<float>)

ifelse( (EulerfArray)arg1, (IntArray)arg2, (EulerfArray)arg3) -> EulerfArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Euler<float> > ifelse(PyImath::FixedArray<Imath_3_1::Euler<float> > {lvalue},PyImath::FixedArray<int>,PyImath::FixedArray<Imath_3_1::Euler<float> >)'''
    ...
    def makeReadOnly (self, *args, **kwargs):
      '''
makeReadOnly( (EulerfArray)arg1) -> None :

    C++ signature :
        void makeReadOnly(PyImath::FixedArray<Imath_3_1::Euler<float> > {lvalue})'''
    ...
    def toQuat (self, *args, **kwargs):
      '''
toQuat( (EulerfArray)arg1) -> QuatfArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Quat<float> > toQuat(PyImath::FixedArray<Imath_3_1::Euler<float> >)'''
    ...
    def toXYZVector (self, *args, **kwargs):
      '''
toXYZVector( (EulerfArray)arg1) -> V3fArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec3<float> > toXYZVector(PyImath::FixedArray<Imath_3_1::Euler<float> >)'''
    ...
    def writable (self, *args, **kwargs):
      '''
writable( (EulerfArray)arg1) -> bool :

    C++ signature :
        bool writable(PyImath::FixedArray<Imath_3_1::Euler<float> > {lvalue})'''
    ...

def FLT_EPS (*args):
      '''

'''      
    ...

def FLT_LOWEST (*args):
      '''

'''      
    ...

def FLT_MAX (*args):
      '''

'''      
    ...

def FLT_MIN (*args):
      '''

'''      
    ...

def FloatArray (*args):
      '''
__init__(_object*, PyImath::FixedArray<double>)
__init__(_object*, PyImath::FixedArray<int>)
__init__(_object*, float, unsigned long)
__init__(_object*, PyImath::FixedArray<float>)
__init__(_object*, unsigned long)

'''      
    ...

class FloatArray:
    def ifelse (self, *args, **kwargs):
      '''
ifelse( (FloatArray)arg1, (IntArray)arg2, (float)arg3) -> FloatArray :

    C++ signature :
        PyImath::FixedArray<float> ifelse(PyImath::FixedArray<float> {lvalue},PyImath::FixedArray<int>,float)

ifelse( (FloatArray)arg1, (IntArray)arg2, (FloatArray)arg3) -> FloatArray :

    C++ signature :
        PyImath::FixedArray<float> ifelse(PyImath::FixedArray<float> {lvalue},PyImath::FixedArray<int>,PyImath::FixedArray<float>)'''
    ...
    def makeReadOnly (self, *args, **kwargs):
      '''
makeReadOnly( (FloatArray)arg1) -> None :

    C++ signature :
        void makeReadOnly(PyImath::FixedArray<float> {lvalue})'''
    ...
    def reduce (self, *args, **kwargs):
      '''
reduce( (FloatArray)arg1) -> float :

    C++ signature :
        float reduce(PyImath::FixedArray<float>)'''
    ...
    def writable (self, *args, **kwargs):
      '''
writable( (FloatArray)arg1) -> bool :

    C++ signature :
        bool writable(PyImath::FixedArray<float> {lvalue})'''
    ...

def FloatArray2D (*args):
      '''
__init__(_object*, PyImath::FixedArray2D<double>)
__init__(_object*, PyImath::FixedArray2D<int>)
__init__(_object*, float, unsigned long, unsigned long)
__init__(_object*, PyImath::FixedArray2D<float>)
__init__(_object*, unsigned long, unsigned long)

'''      
    ...

class FloatArray2D:
    def ifelse (self, *args, **kwargs):
      '''
ifelse( (FloatArray2D)arg1, (IntArray2D)arg2, (float)arg3) -> FloatArray2D :

    C++ signature :
        PyImath::FixedArray2D<float> ifelse(PyImath::FixedArray2D<float> {lvalue},PyImath::FixedArray2D<int>,float)

ifelse( (FloatArray2D)arg1, (IntArray2D)arg2, (FloatArray2D)arg3) -> FloatArray2D :

    C++ signature :
        PyImath::FixedArray2D<float> ifelse(PyImath::FixedArray2D<float> {lvalue},PyImath::FixedArray2D<int>,PyImath::FixedArray2D<float>)'''
    ...
    def item (self, *args, **kwargs):
      '''
item( (FloatArray2D)arg1, (int)arg2, (int)arg3) -> float :

    C++ signature :
        float item(PyImath::FixedArray2D<float> {lvalue},long,long)'''
    ...
    def size (self, *args, **kwargs):
      '''
size( (FloatArray2D)arg1) -> tuple :

    C++ signature :
        boost::python::tuple size(PyImath::FixedArray2D<float> {lvalue})'''
    ...

def FloatArrayFromBuffer (*args):
      '''

'''      
    ...

def FloatMatrix (*args):
      '''
__init__(_object*, int, int)

'''      
    ...

class FloatMatrix:
    def columns (self, *args, **kwargs):
      '''
columns( (FloatMatrix)arg1) -> int :

    C++ signature :
        int columns(PyImath::FixedMatrix<float> {lvalue})'''
    ...
    def rows (self, *args, **kwargs):
      '''
rows( (FloatMatrix)arg1) -> int :

    C++ signature :
        int rows(PyImath::FixedMatrix<float> {lvalue})'''
    ...

def FrustumTestd (*args):
      '''
__init__(_object*, Imath_3_1::Frustum<double>, Imath_3_1::Matrix44<double>)

'''      
    ...

class FrustumTestd:
    def completelyContains (self, *args, **kwargs):
      '''
completelyContains( (FrustumTestd)arg1, (object)arg2) -> bool :

    C++ signature :
        bool completelyContains(Imath_3_1::FrustumTest<double> {lvalue},Imath_3_1::Sphere3<double>)

completelyContains( (FrustumTestd)arg1, (Box3d)arg2) -> bool :

    C++ signature :
        bool completelyContains(Imath_3_1::FrustumTest<double> {lvalue},Imath_3_1::Box<Imath_3_1::Vec3<double> >)'''
    ...
    def isVisible (self, *args, **kwargs):
      '''
isVisible( (FrustumTestd)arg1, (object)arg2) -> bool :

    C++ signature :
        bool isVisible(Imath_3_1::FrustumTest<double> {lvalue},Imath_3_1::Sphere3<double>)

isVisible( (FrustumTestd)arg1, (Box3d)arg2) -> bool :

    C++ signature :
        bool isVisible(Imath_3_1::FrustumTest<double> {lvalue},Imath_3_1::Box<Imath_3_1::Vec3<double> >)

isVisible( (FrustumTestd)arg1, (V3d)arg2) -> bool :

    C++ signature :
        bool isVisible(Imath_3_1::FrustumTest<double> {lvalue},Imath_3_1::Vec3<double>)

isVisible( (FrustumTestd)arg1, (V3fArray)arg2) -> IntArray :

    C++ signature :
        PyImath::FixedArray<int> isVisible(Imath_3_1::FrustumTest<double> {lvalue},PyImath::FixedArray<Imath_3_1::Vec3<float> >)'''
    ...

def FrustumTestf (*args):
      '''
__init__(_object*, Imath_3_1::Frustum<float>, Imath_3_1::Matrix44<float>)

'''      
    ...

class FrustumTestf:
    def completelyContains (self, *args, **kwargs):
      '''
completelyContains( (FrustumTestf)arg1, (object)arg2) -> bool :

    C++ signature :
        bool completelyContains(Imath_3_1::FrustumTest<float> {lvalue},Imath_3_1::Sphere3<float>)

completelyContains( (FrustumTestf)arg1, (Box3f)arg2) -> bool :

    C++ signature :
        bool completelyContains(Imath_3_1::FrustumTest<float> {lvalue},Imath_3_1::Box<Imath_3_1::Vec3<float> >)'''
    ...
    def isVisible (self, *args, **kwargs):
      '''
isVisible( (FrustumTestf)arg1, (object)arg2) -> bool :

    C++ signature :
        bool isVisible(Imath_3_1::FrustumTest<float> {lvalue},Imath_3_1::Sphere3<float>)

isVisible( (FrustumTestf)arg1, (Box3f)arg2) -> bool :

    C++ signature :
        bool isVisible(Imath_3_1::FrustumTest<float> {lvalue},Imath_3_1::Box<Imath_3_1::Vec3<float> >)

isVisible( (FrustumTestf)arg1, (V3f)arg2) -> bool :

    C++ signature :
        bool isVisible(Imath_3_1::FrustumTest<float> {lvalue},Imath_3_1::Vec3<float>)

isVisible( (FrustumTestf)arg1, (V3fArray)arg2) -> IntArray :

    C++ signature :
        PyImath::FixedArray<int> isVisible(Imath_3_1::FrustumTest<float> {lvalue},PyImath::FixedArray<Imath_3_1::Vec3<float> >)'''
    ...

def Frustumd (*args):
      '''
__init__(_object*, double, double, double, double, double)
__init__(_object*, double, double, double, double, double, double, bool)
__init__(_object*)
__init__(_object*, Imath_3_1::Frustum<double>)

'''      
    ...

class Frustumd:
    def DepthToZ (self, *args, **kwargs):
      '''
DepthToZ( (Frustumd)arg1, (float)arg2, (int)arg3, (int)arg4) -> int :
    F.DepthToZ(depth, zMin, zMax) -- converts depth (Z in the local space of the frustum F) to z (a result of  transformation by F's projection matrix) which is normalized to [zMin, zMax]

    C++ signature :
        long DepthToZ(Imath_3_1::Frustum<double> {lvalue},double,long,long)'''
    ...
    def ZToDepth (self, *args, **kwargs):
      '''
ZToDepth( (Frustumd)arg1, (int)arg2, (int)arg3, (int)arg4) -> float :
    F.ZToDepth(z, zMin, zMax) -- returns the depth (Z in the local space of the frustum F) corresponding to z (a result of transformation by F's projection matrix) after normalizing z to be between zMin and zMax

    C++ signature :
        double ZToDepth(Imath_3_1::Frustum<double> {lvalue},long,long,long)'''
    ...
    def aspect (self, *args, **kwargs):
      '''
aspect( (Frustumd)arg1) -> float :
    F.aspect() -- derives and returns the aspect ratio for frustum F

    C++ signature :
        double aspect(Imath_3_1::Frustum<double> {lvalue})'''
    ...
    def bottom (self, *args, **kwargs):
      '''
bottom( (Frustumd)arg1) -> float :
    F.bottom() -- returns the bottom coordinate of the near clipping window of frustum F

    C++ signature :
        double bottom(Imath_3_1::Frustum<double> {lvalue})'''
    ...
    def far (self, *args, **kwargs):
      '''
far( (Frustumd)arg1) -> float :
    F.far() -- returns the coordinate of the far clipping plane of frustum F

    C++ signature :
        double far(Imath_3_1::Frustum<double> {lvalue})'''
    ...
    def farPlane (self, *args, **kwargs):
      '''
farPlane( (Frustumd)arg1) -> float :
    F.farPlane() -- returns the coordinate of the far clipping plane of frustum F

    C++ signature :
        double farPlane(Imath_3_1::Frustum<double> {lvalue})'''
    ...
    def fovx (self, *args, **kwargs):
      '''
fovx( (Frustumd)arg1) -> float :
    F.fovx() -- derives and returns the x field of view (in radians) for frustum F

    C++ signature :
        double fovx(Imath_3_1::Frustum<double> {lvalue})'''
    ...
    def fovy (self, *args, **kwargs):
      '''
fovy( (Frustumd)arg1) -> float :
    F.fovy() -- derives and returns the y field of view (in radians) for frustum F

    C++ signature :
        double fovy(Imath_3_1::Frustum<double> {lvalue})'''
    ...
    def left (self, *args, **kwargs):
      '''
left( (Frustumd)arg1) -> float :
    F.left() -- returns the left coordinate of the near clipping window of frustum F

    C++ signature :
        double left(Imath_3_1::Frustum<double> {lvalue})'''
    ...
    def modifyNearAndFar (self, *args, **kwargs):
      '''
modifyNearAndFar( (Frustumd)arg1, (float)arg2, (float)arg3) -> None :
    F.modifyNearAndFar(nearPlane, farPlane) -- modifies the already-valid frustum F as specified

    C++ signature :
        void modifyNearAndFar(Imath_3_1::Frustum<double> {lvalue},double,double)'''
    ...
    def near (self, *args, **kwargs):
      '''
near( (Frustumd)arg1) -> float :
    F.near() -- returns the coordinate of the near clipping plane of frustum F

    C++ signature :
        double near(Imath_3_1::Frustum<double> {lvalue})'''
    ...
    def nearPlane (self, *args, **kwargs):
      '''
nearPlane( (Frustumd)arg1) -> float :
    F.nearPlane() -- returns the coordinate of the near clipping plane of frustum F

    C++ signature :
        double nearPlane(Imath_3_1::Frustum<double> {lvalue})'''
    ...
    def normalizedZToDepth (self, *args, **kwargs):
      '''
normalizedZToDepth( (Frustumd)arg1, (float)arg2) -> float :
    F.normalizedZToDepth(z) -- returns the depth (Z in the local space of the frustum F) corresponding to z (a result of transformation by F's projection matrix), which is assumed to have been normalized to [-1, 1]

    C++ signature :
        double normalizedZToDepth(Imath_3_1::Frustum<double> {lvalue},double)'''
    ...
    def orthographic (self, *args, **kwargs):
      '''
orthographic( (Frustumd)arg1) -> bool :
    F.orthographic() -- returns whether frustum F is orthographic or not

    C++ signature :
        bool orthographic(Imath_3_1::Frustum<double> {lvalue})'''
    ...
    def planes (self, *args, **kwargs):
      '''
planes( (Frustumd)arg1, (Plane3d)arg2) -> None :
    F.planes([M]) -- returns a sequence of 6 Plane3s, the sides of the frustum F (top, right, bottom, left, nearPlane, farPlane), optionally transformed by the matrix M if specified

    C++ signature :
        void planes(Imath_3_1::Frustum<double> {lvalue},Imath_3_1::Plane3<double>*)

planes( (Frustumd)arg1, (Plane3d)arg2, (M44d)arg3) -> None :

    C++ signature :
        void planes(Imath_3_1::Frustum<double> {lvalue},Imath_3_1::Plane3<double>*,Imath_3_1::Matrix44<double>)

planes( (Frustumd)arg1 [, (M44d)arg2]) -> tuple :

    C++ signature :
        boost::python::tuple planes(Imath_3_1::Frustum<double> {lvalue} [,Imath_3_1::Matrix44<double>])'''
    ...
    def projectPointToScreen (self, *args, **kwargs):
      '''
projectPointToScreen( (Frustumd)arg1, (V3d)arg2) -> V2d :
    F.projectPointToScreen(V) -- returns the projection of V3 V into screen space

    C++ signature :
        Imath_3_1::Vec2<double> projectPointToScreen(Imath_3_1::Frustum<double> {lvalue},Imath_3_1::Vec3<double>)

projectPointToScreen( (Frustumd)arg1, (tuple)arg2) -> V2d :

    C++ signature :
        Imath_3_1::Vec2<double> projectPointToScreen(Imath_3_1::Frustum<double> {lvalue},boost::python::tuple)

projectPointToScreen( (Frustumd)arg1, (object)arg2) -> V2d :

    C++ signature :
        Imath_3_1::Vec2<double> projectPointToScreen(Imath_3_1::Frustum<double> {lvalue},boost::python::api::object)'''
    ...
    def projectScreenToRay (self, *args, **kwargs):
      '''
projectScreenToRay( (Frustumd)arg1, (V2d)arg2) -> Line3d :
    F.projectScreenToRay(V) -- returns a Line3 through V, a V2 point in screen space

    C++ signature :
        Imath_3_1::Line3<double> projectScreenToRay(Imath_3_1::Frustum<double> {lvalue},Imath_3_1::Vec2<double>)

projectScreenToRay( (Frustumd)arg1, (tuple)arg2) -> Line3d :

    C++ signature :
        Imath_3_1::Line3<double> projectScreenToRay(Imath_3_1::Frustum<double> {lvalue},boost::python::tuple)'''
    ...
    def projectionMatrix (self, *args, **kwargs):
      '''
projectionMatrix( (Frustumd)arg1) -> M44d :
    F.projectionMatrix() -- derives and returns the projection matrix for frustum F

    C++ signature :
        Imath_3_1::Matrix44<double> projectionMatrix(Imath_3_1::Frustum<double> {lvalue})'''
    ...
    def right (self, *args, **kwargs):
      '''
right( (Frustumd)arg1) -> float :
    F.right() -- returns the right coordinate of the near clipping window of frustum F

    C++ signature :
        double right(Imath_3_1::Frustum<double> {lvalue})'''
    ...
    def screenRadius (self, *args, **kwargs):
      '''
screenRadius( (Frustumd)arg1, (V3d)arg2, (float)arg3) -> float :
    F.screenRadius(V, r) -- returns the radius in screen space corresponding to the point V and radius r in F's local space

    C++ signature :
        double screenRadius(Imath_3_1::Frustum<double> {lvalue},Imath_3_1::Vec3<double>,double)

screenRadius( (Frustumd)arg1, (tuple)arg2, (float)arg3) -> float :

    C++ signature :
        double screenRadius(Imath_3_1::Frustum<double> {lvalue},boost::python::tuple,double)'''
    ...
    def set (self, *args, **kwargs):
      '''
set( (Frustumd)arg1, (float)arg2, (float)arg3, (float)arg4, (float)arg5, (float)arg6, (float)arg7, (bool)arg8) -> None :
    F.set(nearPlane, farPlane, left, right, top, bottom, [ortho])
    F.set(nearPlane, farPlane, fovx, fovy, aspect)                -- sets the entire state of frustum F as specified.  Only one of fovx or fovy may be non-zero.

    C++ signature :
        void set(Imath_3_1::Frustum<double> {lvalue},double,double,double,double,double,double,bool)

set( (Frustumd)arg1, (float)arg2, (float)arg3, (float)arg4, (float)arg5, (float)arg6) -> None :

    C++ signature :
        void set(Imath_3_1::Frustum<double> {lvalue},double,double,double,double,double)'''
    ...
    def setOrthographic (self, *args, **kwargs):
      '''
setOrthographic( (Frustumd)arg1, (bool)arg2) -> None :
    F.setOrthographic(b) -- modifies the already-valid frustum F to be orthographic or not

    C++ signature :
        void setOrthographic(Imath_3_1::Frustum<double> {lvalue},bool)'''
    ...
    def top (self, *args, **kwargs):
      '''
top( (Frustumd)arg1) -> float :
    F.top() -- returns the top coordinate of the near clipping window of frustum F

    C++ signature :
        double top(Imath_3_1::Frustum<double> {lvalue})'''
    ...
    def window (self, *args, **kwargs):
      '''
window( (Frustumd)arg1, (float)arg2, (float)arg3, (float)arg4, (float)arg5) -> Frustumd :
    F.window(l,r,b,t) -- takes a rectangle in the screen space (i.e., -1 <= l <= r <= 1, -1 <= b <= t <= 1) of F and returns a new Frustum whose near clipping-plane window is that rectangle in local space

    C++ signature :
        Imath_3_1::Frustum<double> window(Imath_3_1::Frustum<double> {lvalue},double,double,double,double)'''
    ...
    def worldRadius (self, *args, **kwargs):
      '''
worldRadius( (Frustumd)arg1, (V3d)arg2, (float)arg3) -> float :
    F.worldRadius(V, r) -- returns the radius in F's local space corresponding to the point V and radius r in screen space

    C++ signature :
        double worldRadius(Imath_3_1::Frustum<double> {lvalue},Imath_3_1::Vec3<double>,double)

worldRadius( (Frustumd)arg1, (tuple)arg2, (float)arg3) -> float :

    C++ signature :
        double worldRadius(Imath_3_1::Frustum<double> {lvalue},boost::python::tuple,double)'''
    ...

def Frustumf (*args):
      '''
__init__(_object*, float, float, float, float, float)
__init__(_object*, float, float, float, float, float, float, bool)
__init__(_object*)
__init__(_object*, Imath_3_1::Frustum<float>)

'''      
    ...

class Frustumf:
    def DepthToZ (self, *args, **kwargs):
      '''
DepthToZ( (Frustumf)arg1, (float)arg2, (int)arg3, (int)arg4) -> int :
    F.DepthToZ(depth, zMin, zMax) -- converts depth (Z in the local space of the frustum F) to z (a result of  transformation by F's projection matrix) which is normalized to [zMin, zMax]

    C++ signature :
        long DepthToZ(Imath_3_1::Frustum<float> {lvalue},float,long,long)'''
    ...
    def ZToDepth (self, *args, **kwargs):
      '''
ZToDepth( (Frustumf)arg1, (int)arg2, (int)arg3, (int)arg4) -> float :
    F.ZToDepth(z, zMin, zMax) -- returns the depth (Z in the local space of the frustum F) corresponding to z (a result of transformation by F's projection matrix) after normalizing z to be between zMin and zMax

    C++ signature :
        float ZToDepth(Imath_3_1::Frustum<float> {lvalue},long,long,long)'''
    ...
    def aspect (self, *args, **kwargs):
      '''
aspect( (Frustumf)arg1) -> float :
    F.aspect() -- derives and returns the aspect ratio for frustum F

    C++ signature :
        float aspect(Imath_3_1::Frustum<float> {lvalue})'''
    ...
    def bottom (self, *args, **kwargs):
      '''
bottom( (Frustumf)arg1) -> float :
    F.bottom() -- returns the bottom coordinate of the near clipping window of frustum F

    C++ signature :
        float bottom(Imath_3_1::Frustum<float> {lvalue})'''
    ...
    def far (self, *args, **kwargs):
      '''
far( (Frustumf)arg1) -> float :
    F.far() -- returns the coordinate of the far clipping plane of frustum F

    C++ signature :
        float far(Imath_3_1::Frustum<float> {lvalue})'''
    ...
    def farPlane (self, *args, **kwargs):
      '''
farPlane( (Frustumf)arg1) -> float :
    F.farPlane() -- returns the coordinate of the far clipping plane of frustum F

    C++ signature :
        float farPlane(Imath_3_1::Frustum<float> {lvalue})'''
    ...
    def fovx (self, *args, **kwargs):
      '''
fovx( (Frustumf)arg1) -> float :
    F.fovx() -- derives and returns the x field of view (in radians) for frustum F

    C++ signature :
        float fovx(Imath_3_1::Frustum<float> {lvalue})'''
    ...
    def fovy (self, *args, **kwargs):
      '''
fovy( (Frustumf)arg1) -> float :
    F.fovy() -- derives and returns the y field of view (in radians) for frustum F

    C++ signature :
        float fovy(Imath_3_1::Frustum<float> {lvalue})'''
    ...
    def left (self, *args, **kwargs):
      '''
left( (Frustumf)arg1) -> float :
    F.left() -- returns the left coordinate of the near clipping window of frustum F

    C++ signature :
        float left(Imath_3_1::Frustum<float> {lvalue})'''
    ...
    def modifyNearAndFar (self, *args, **kwargs):
      '''
modifyNearAndFar( (Frustumf)arg1, (float)arg2, (float)arg3) -> None :
    F.modifyNearAndFar(nearPlane, farPlane) -- modifies the already-valid frustum F as specified

    C++ signature :
        void modifyNearAndFar(Imath_3_1::Frustum<float> {lvalue},float,float)'''
    ...
    def near (self, *args, **kwargs):
      '''
near( (Frustumf)arg1) -> float :
    F.near() -- returns the coordinate of the near clipping plane of frustum F

    C++ signature :
        float near(Imath_3_1::Frustum<float> {lvalue})'''
    ...
    def nearPlane (self, *args, **kwargs):
      '''
nearPlane( (Frustumf)arg1) -> float :
    F.nearPlane() -- returns the coordinate of the near clipping plane of frustum F

    C++ signature :
        float nearPlane(Imath_3_1::Frustum<float> {lvalue})'''
    ...
    def normalizedZToDepth (self, *args, **kwargs):
      '''
normalizedZToDepth( (Frustumf)arg1, (float)arg2) -> float :
    F.normalizedZToDepth(z) -- returns the depth (Z in the local space of the frustum F) corresponding to z (a result of transformation by F's projection matrix), which is assumed to have been normalized to [-1, 1]

    C++ signature :
        float normalizedZToDepth(Imath_3_1::Frustum<float> {lvalue},float)'''
    ...
    def orthographic (self, *args, **kwargs):
      '''
orthographic( (Frustumf)arg1) -> bool :
    F.orthographic() -- returns whether frustum F is orthographic or not

    C++ signature :
        bool orthographic(Imath_3_1::Frustum<float> {lvalue})'''
    ...
    def planes (self, *args, **kwargs):
      '''
planes( (Frustumf)arg1, (Plane3f)arg2) -> None :
    F.planes([M]) -- returns a sequence of 6 Plane3s, the sides of the frustum F (top, right, bottom, left, nearPlane, farPlane), optionally transformed by the matrix M if specified

    C++ signature :
        void planes(Imath_3_1::Frustum<float> {lvalue},Imath_3_1::Plane3<float>*)

planes( (Frustumf)arg1, (Plane3f)arg2, (M44f)arg3) -> None :

    C++ signature :
        void planes(Imath_3_1::Frustum<float> {lvalue},Imath_3_1::Plane3<float>*,Imath_3_1::Matrix44<float>)

planes( (Frustumf)arg1 [, (M44f)arg2]) -> tuple :

    C++ signature :
        boost::python::tuple planes(Imath_3_1::Frustum<float> {lvalue} [,Imath_3_1::Matrix44<float>])'''
    ...
    def projectPointToScreen (self, *args, **kwargs):
      '''
projectPointToScreen( (Frustumf)arg1, (V3f)arg2) -> V2f :
    F.projectPointToScreen(V) -- returns the projection of V3 V into screen space

    C++ signature :
        Imath_3_1::Vec2<float> projectPointToScreen(Imath_3_1::Frustum<float> {lvalue},Imath_3_1::Vec3<float>)

projectPointToScreen( (Frustumf)arg1, (tuple)arg2) -> V2f :

    C++ signature :
        Imath_3_1::Vec2<float> projectPointToScreen(Imath_3_1::Frustum<float> {lvalue},boost::python::tuple)

projectPointToScreen( (Frustumf)arg1, (object)arg2) -> V2f :

    C++ signature :
        Imath_3_1::Vec2<float> projectPointToScreen(Imath_3_1::Frustum<float> {lvalue},boost::python::api::object)'''
    ...
    def projectScreenToRay (self, *args, **kwargs):
      '''
projectScreenToRay( (Frustumf)arg1, (V2f)arg2) -> Line3f :
    F.projectScreenToRay(V) -- returns a Line3 through V, a V2 point in screen space

    C++ signature :
        Imath_3_1::Line3<float> projectScreenToRay(Imath_3_1::Frustum<float> {lvalue},Imath_3_1::Vec2<float>)

projectScreenToRay( (Frustumf)arg1, (tuple)arg2) -> Line3f :

    C++ signature :
        Imath_3_1::Line3<float> projectScreenToRay(Imath_3_1::Frustum<float> {lvalue},boost::python::tuple)'''
    ...
    def projectionMatrix (self, *args, **kwargs):
      '''
projectionMatrix( (Frustumf)arg1) -> M44f :
    F.projectionMatrix() -- derives and returns the projection matrix for frustum F

    C++ signature :
        Imath_3_1::Matrix44<float> projectionMatrix(Imath_3_1::Frustum<float> {lvalue})'''
    ...
    def right (self, *args, **kwargs):
      '''
right( (Frustumf)arg1) -> float :
    F.right() -- returns the right coordinate of the near clipping window of frustum F

    C++ signature :
        float right(Imath_3_1::Frustum<float> {lvalue})'''
    ...
    def screenRadius (self, *args, **kwargs):
      '''
screenRadius( (Frustumf)arg1, (V3f)arg2, (float)arg3) -> float :
    F.screenRadius(V, r) -- returns the radius in screen space corresponding to the point V and radius r in F's local space

    C++ signature :
        float screenRadius(Imath_3_1::Frustum<float> {lvalue},Imath_3_1::Vec3<float>,float)

screenRadius( (Frustumf)arg1, (tuple)arg2, (float)arg3) -> float :

    C++ signature :
        float screenRadius(Imath_3_1::Frustum<float> {lvalue},boost::python::tuple,float)'''
    ...
    def set (self, *args, **kwargs):
      '''
set( (Frustumf)arg1, (float)arg2, (float)arg3, (float)arg4, (float)arg5, (float)arg6, (float)arg7, (bool)arg8) -> None :
    F.set(nearPlane, farPlane, left, right, top, bottom, [ortho])
    F.set(nearPlane, farPlane, fovx, fovy, aspect)                -- sets the entire state of frustum F as specified.  Only one of fovx or fovy may be non-zero.

    C++ signature :
        void set(Imath_3_1::Frustum<float> {lvalue},float,float,float,float,float,float,bool)

set( (Frustumf)arg1, (float)arg2, (float)arg3, (float)arg4, (float)arg5, (float)arg6) -> None :

    C++ signature :
        void set(Imath_3_1::Frustum<float> {lvalue},float,float,float,float,float)'''
    ...
    def setOrthographic (self, *args, **kwargs):
      '''
setOrthographic( (Frustumf)arg1, (bool)arg2) -> None :
    F.setOrthographic(b) -- modifies the already-valid frustum F to be orthographic or not

    C++ signature :
        void setOrthographic(Imath_3_1::Frustum<float> {lvalue},bool)'''
    ...
    def top (self, *args, **kwargs):
      '''
top( (Frustumf)arg1) -> float :
    F.top() -- returns the top coordinate of the near clipping window of frustum F

    C++ signature :
        float top(Imath_3_1::Frustum<float> {lvalue})'''
    ...
    def window (self, *args, **kwargs):
      '''
window( (Frustumf)arg1, (float)arg2, (float)arg3, (float)arg4, (float)arg5) -> Frustumf :
    F.window(l,r,b,t) -- takes a rectangle in the screen space (i.e., -1 <= l <= r <= 1, -1 <= b <= t <= 1) of F and returns a new Frustum whose near clipping-plane window is that rectangle in local space

    C++ signature :
        Imath_3_1::Frustum<float> window(Imath_3_1::Frustum<float> {lvalue},float,float,float,float)'''
    ...
    def worldRadius (self, *args, **kwargs):
      '''
worldRadius( (Frustumf)arg1, (V3f)arg2, (float)arg3) -> float :
    F.worldRadius(V, r) -- returns the radius in F's local space corresponding to the point V and radius r in screen space

    C++ signature :
        float worldRadius(Imath_3_1::Frustum<float> {lvalue},Imath_3_1::Vec3<float>,float)

worldRadius( (Frustumf)arg1, (tuple)arg2, (float)arg3) -> float :

    C++ signature :
        float worldRadius(Imath_3_1::Frustum<float> {lvalue},boost::python::tuple,float)'''
    ...

def INT_EPS (*args):
      '''

'''      
    ...

def INT_LOWEST (*args):
      '''

'''      
    ...

def INT_MAX (*args):
      '''

'''      
    ...

def INT_MIN (*args):
      '''

'''      
    ...

def IntArray (*args):
      '''
__init__(_object*, PyImath::FixedArray<double>)
__init__(_object*, PyImath::FixedArray<float>)
__init__(_object*, int, unsigned long)
__init__(_object*, PyImath::FixedArray<int>)
__init__(_object*, unsigned long)

'''      
    ...

class IntArray:
    def ifelse (self, *args, **kwargs):
      '''
ifelse( (IntArray)arg1, (IntArray)arg2, (int)arg3) -> IntArray :

    C++ signature :
        PyImath::FixedArray<int> ifelse(PyImath::FixedArray<int> {lvalue},PyImath::FixedArray<int>,int)

ifelse( (IntArray)arg1, (IntArray)arg2, (IntArray)arg3) -> IntArray :

    C++ signature :
        PyImath::FixedArray<int> ifelse(PyImath::FixedArray<int> {lvalue},PyImath::FixedArray<int>,PyImath::FixedArray<int>)'''
    ...
    def makeReadOnly (self, *args, **kwargs):
      '''
makeReadOnly( (IntArray)arg1) -> None :

    C++ signature :
        void makeReadOnly(PyImath::FixedArray<int> {lvalue})'''
    ...
    def reduce (self, *args, **kwargs):
      '''
reduce( (IntArray)arg1) -> int :

    C++ signature :
        int reduce(PyImath::FixedArray<int>)'''
    ...
    def writable (self, *args, **kwargs):
      '''
writable( (IntArray)arg1) -> bool :

    C++ signature :
        bool writable(PyImath::FixedArray<int> {lvalue})'''
    ...

def IntArray2D (*args):
      '''
__init__(_object*, PyImath::FixedArray2D<double>)
__init__(_object*, PyImath::FixedArray2D<float>)
__init__(_object*, int, unsigned long, unsigned long)
__init__(_object*, PyImath::FixedArray2D<int>)
__init__(_object*, unsigned long, unsigned long)

'''      
    ...

class IntArray2D:
    def ifelse (self, *args, **kwargs):
      '''
ifelse( (IntArray2D)arg1, (IntArray2D)arg2, (int)arg3) -> IntArray2D :

    C++ signature :
        PyImath::FixedArray2D<int> ifelse(PyImath::FixedArray2D<int> {lvalue},PyImath::FixedArray2D<int>,int)

ifelse( (IntArray2D)arg1, (IntArray2D)arg2, (IntArray2D)arg3) -> IntArray2D :

    C++ signature :
        PyImath::FixedArray2D<int> ifelse(PyImath::FixedArray2D<int> {lvalue},PyImath::FixedArray2D<int>,PyImath::FixedArray2D<int>)'''
    ...
    def item (self, *args, **kwargs):
      '''
item( (IntArray2D)arg1, (int)arg2, (int)arg3) -> int :

    C++ signature :
        int item(PyImath::FixedArray2D<int> {lvalue},long,long)'''
    ...
    def size (self, *args, **kwargs):
      '''
size( (IntArray2D)arg1) -> tuple :

    C++ signature :
        boost::python::tuple size(PyImath::FixedArray2D<int> {lvalue})'''
    ...

def IntArrayFromBuffer (*args):
      '''

'''      
    ...

def IntMatrix (*args):
      '''
__init__(_object*, int, int)

'''      
    ...

class IntMatrix:
    def columns (self, *args, **kwargs):
      '''
columns( (IntMatrix)arg1) -> int :

    C++ signature :
        int columns(PyImath::FixedMatrix<int> {lvalue})'''
    ...
    def rows (self, *args, **kwargs):
      '''
rows( (IntMatrix)arg1) -> int :

    C++ signature :
        int rows(PyImath::FixedMatrix<int> {lvalue})'''
    ...

def Line3d (*args):
      '''
__init__(_object*, Imath_3_1::Vec3<double>, Imath_3_1::Vec3<double>)
__init__(_object*, Imath_3_1::Vec3<float>, Imath_3_1::Vec3<float>)
__init__(boost::python::api::object, Imath_3_1::Line3<double>)
__init__(boost::python::api::object, Imath_3_1::Line3<float>)
__init__(boost::python::api::object, boost::python::tuple, boost::python::tuple)
__init__(boost::python::api::object)
__init__(_object*)

'''      
    ...

class Line3d:
    def closestPointTo (self, *args, **kwargs):
      '''
closestPointTo( (Line3d)arg1, (V3d)arg2) -> V3d :
    l.closestPointTo(p) -- returns the point on
       line l that is closest to point p
    
    

    C++ signature :
        Imath_3_1::Vec3<double> closestPointTo(Imath_3_1::Line3<double>,Imath_3_1::Vec3<double>)

closestPointTo( (Line3d)arg1, (tuple)arg2) -> V3d :

    C++ signature :
        Imath_3_1::Vec3<double> closestPointTo(Imath_3_1::Line3<double>,boost::python::tuple)

closestPointTo( (Line3d)arg1, (Line3d)arg2) -> V3d :
    l1.closestPointTo(l2) -- returns the point on
       line l1 that is closest to line l2
    

    C++ signature :
        Imath_3_1::Vec3<double> closestPointTo(Imath_3_1::Line3<double>,Imath_3_1::Line3<double>)'''
    ...
    def closestPoints (self, *args, **kwargs):
      '''
closestPoints( (Line3d)arg1, (Line3d)arg2, (V3d)arg3, (V3d)arg4) -> None :
    l1.closestPoints(l2,p0,p1)

    C++ signature :
        void closestPoints(Imath_3_1::Line3<double> {lvalue},Imath_3_1::Line3<double>,Imath_3_1::Vec3<double> {lvalue},Imath_3_1::Vec3<double> {lvalue})

closestPoints( (Line3d)arg1, (Line3d)arg2) -> tuple :
    l1.closestPoints(l2) -- returns a tuple with
    two points:
       (l1.closestPoint(l2), l2.closestPoint(l1)
    

    C++ signature :
        boost::python::tuple closestPoints(Imath_3_1::Line3<double> {lvalue},Imath_3_1::Line3<double>)'''
    ...
    def closestTriangleVertex (self, *args, **kwargs):
      '''
closestTriangleVertex( (Line3d)arg1, (V3d)arg2, (V3d)arg3, (V3d)arg4) -> V3d :
    l.closestTriangleVertex(v0, v1, v2) -- returns
    a copy of v0, v1, or v2, depending on which is
    closest to line l.
    

    C++ signature :
        Imath_3_1::Vec3<double> closestTriangleVertex(Imath_3_1::Line3<double> {lvalue},Imath_3_1::Vec3<double>,Imath_3_1::Vec3<double>,Imath_3_1::Vec3<double>)

closestTriangleVertex( (Line3d)arg1, (tuple)arg2, (tuple)arg3, (tuple)arg4) -> V3d :

    C++ signature :
        Imath_3_1::Vec3<double> closestTriangleVertex(Imath_3_1::Line3<double> {lvalue},boost::python::tuple,boost::python::tuple,boost::python::tuple)'''
    ...
    def dir (self, *args, **kwargs):
      '''
dir( (Line3d)arg1) -> V3d :
    l.dir() -- returns the direction of line l
    

    C++ signature :
        Imath_3_1::Vec3<double> dir(Imath_3_1::Line3<double> {lvalue})'''
    ...
    def distanceTo (self, *args, **kwargs):
      '''
distanceTo( (Line3d)arg1, (V3d)arg2) -> float :
    l.distanceTo(p) -- returns the distance from
       line l to point p
    

    C++ signature :
        double distanceTo(Imath_3_1::Line3<double> {lvalue},Imath_3_1::Vec3<double> {lvalue})

distanceTo( (Line3d)arg1, (Line3d)arg2) -> float :
    l1.distanceTo(l2) -- returns the distance from
       line l1 to line l2
    

    C++ signature :
        double distanceTo(Imath_3_1::Line3<double> {lvalue},Imath_3_1::Line3<double> {lvalue})

distanceTo( (Line3d)arg1, (tuple)arg2) -> float :

    C++ signature :
        double distanceTo(Imath_3_1::Line3<double>,boost::python::tuple)'''
    ...
    def intersectWithTriangle (self, *args, **kwargs):
      '''
intersectWithTriangle( (Line3d)arg1, (V3d)arg2, (V3d)arg3, (V3d)arg4) -> object :

    C++ signature :
        boost::python::api::object intersectWithTriangle(Imath_3_1::Line3<double> {lvalue},Imath_3_1::Vec3<double>,Imath_3_1::Vec3<double>,Imath_3_1::Vec3<double>)

intersectWithTriangle( (Line3d)arg1, (V3d)arg2, (V3d)arg3, (V3d)arg4, (V3d)arg5, (V3d)arg6, (bool)arg7) -> bool :
    l.intersectWithTriangle(v0, v1, v2) -- computes the
    intersection of line l and triangle (v0, v1, v2).
    
    If the line and the triangle do not intersect,
    None is returned.
    If the line and the triangle intersect, a tuple
    (p, b, f) is returned:
    
       p  intersection point in 3D space
    
       b  intersection point in barycentric coordinates
    
       f  1 if the line hits the triangle from the
          front (((v2-v1) % (v1-v2)) ^ l.dir() < 0),
          0 if the line hits the trianble from the
          back
    
    

    C++ signature :
        bool intersectWithTriangle(Imath_3_1::Line3<double> {lvalue},Imath_3_1::Vec3<double>,Imath_3_1::Vec3<double>,Imath_3_1::Vec3<double>,Imath_3_1::Vec3<double> {lvalue},Imath_3_1::Vec3<double> {lvalue},bool {lvalue})

intersectWithTriangle( (Line3d)arg1, (tuple)arg2, (tuple)arg3, (tuple)arg4) -> tuple :

    C++ signature :
        boost::python::tuple intersectWithTriangle(Imath_3_1::Line3<double> {lvalue},boost::python::tuple,boost::python::tuple,boost::python::tuple)'''
    ...
    def pointAt (self, *args, **kwargs):
      '''
pointAt( (Line3d)arg1, (float)arg2) -> V3d :
    l.pointAt(t) -- returns l.pos() + t * l.dir()

    C++ signature :
        Imath_3_1::Vec3<double> pointAt(Imath_3_1::Line3<double> {lvalue},double)'''
    ...
    def pos (self, *args, **kwargs):
      '''
pos( (Line3d)arg1) -> V3d :
    l.pos() -- returns the start point of line l

    C++ signature :
        Imath_3_1::Vec3<double> pos(Imath_3_1::Line3<double> {lvalue})'''
    ...
    def rotatePoint (self, *args, **kwargs):
      '''
rotatePoint( (Line3d)arg1, (V3d)arg2, (float)arg3) -> V3d :
    l.rotatePoint(p,r) -- rotates point p around
    line by angle r (in radians), and returns the
    result (p is not modified)
    

    C++ signature :
        Imath_3_1::Vec3<double> rotatePoint(Imath_3_1::Line3<double> {lvalue},Imath_3_1::Vec3<double>,double)

rotatePoint( (Line3d)arg1, (tuple)arg2, (float)arg3) -> V3d :

    C++ signature :
        Imath_3_1::Vec3<double> rotatePoint(Imath_3_1::Line3<double> {lvalue},boost::python::tuple,double)'''
    ...
    def set (self, *args, **kwargs):
      '''
set( (Line3d)arg1, (V3d)arg2, (V3d)arg3) -> None :
    l.set(p1, p2) -- sets the start point
    and direction of line l by calling
       l.setPos (p1)
       l.setDir (p2 - p1)
    

    C++ signature :
        void set(Imath_3_1::Line3<double> {lvalue},Imath_3_1::Vec3<double>,Imath_3_1::Vec3<double>)

set( (Line3d)arg1, (tuple)arg2, (tuple)arg3) -> None :

    C++ signature :
        void set(Imath_3_1::Line3<double> {lvalue},boost::python::tuple,boost::python::tuple)'''
    ...
    def setDir (self, *args, **kwargs):
      '''
setDir( (Line3d)arg1, (V3d)arg2) -> None :
    l.setDir(d) -- sets the direction of line l
    to d.normalized().
    

    C++ signature :
        void setDir(Imath_3_1::Line3<double> {lvalue},Imath_3_1::Vec3<double>)

setDir( (Line3d)arg1, (tuple)arg2) -> None :

    C++ signature :
        void setDir(Imath_3_1::Line3<double> {lvalue},boost::python::tuple)'''
    ...
    def setPos (self, *args, **kwargs):
      '''
setPos( (Line3d)arg1, (V3d)arg2) -> None :
    l.setPos(p) -- sets the start point of line l to p

    C++ signature :
        void setPos(Imath_3_1::Line3<double> {lvalue},Imath_3_1::Vec3<double>)

setPos( (Line3d)arg1, (tuple)arg2) -> None :

    C++ signature :
        void setPos(Imath_3_1::Line3<double> {lvalue},boost::python::tuple)'''
    ...

def Line3f (*args):
      '''
__init__(_object*, Imath_3_1::Vec3<double>, Imath_3_1::Vec3<double>)
__init__(_object*, Imath_3_1::Vec3<float>, Imath_3_1::Vec3<float>)
__init__(boost::python::api::object, Imath_3_1::Line3<double>)
__init__(boost::python::api::object, Imath_3_1::Line3<float>)
__init__(boost::python::api::object, boost::python::tuple, boost::python::tuple)
__init__(boost::python::api::object)
__init__(_object*)

'''      
    ...

class Line3f:
    def closestPointTo (self, *args, **kwargs):
      '''
closestPointTo( (Line3f)arg1, (V3f)arg2) -> V3f :
    l.closestPointTo(p) -- returns the point on
       line l that is closest to point p
    
    

    C++ signature :
        Imath_3_1::Vec3<float> closestPointTo(Imath_3_1::Line3<float>,Imath_3_1::Vec3<float>)

closestPointTo( (Line3f)arg1, (tuple)arg2) -> V3f :

    C++ signature :
        Imath_3_1::Vec3<float> closestPointTo(Imath_3_1::Line3<float>,boost::python::tuple)

closestPointTo( (Line3f)arg1, (Line3f)arg2) -> V3f :
    l1.closestPointTo(l2) -- returns the point on
       line l1 that is closest to line l2
    

    C++ signature :
        Imath_3_1::Vec3<float> closestPointTo(Imath_3_1::Line3<float>,Imath_3_1::Line3<float>)'''
    ...
    def closestPoints (self, *args, **kwargs):
      '''
closestPoints( (Line3f)arg1, (Line3f)arg2, (V3f)arg3, (V3f)arg4) -> None :
    l1.closestPoints(l2,p0,p1)

    C++ signature :
        void closestPoints(Imath_3_1::Line3<float> {lvalue},Imath_3_1::Line3<float>,Imath_3_1::Vec3<float> {lvalue},Imath_3_1::Vec3<float> {lvalue})

closestPoints( (Line3f)arg1, (Line3f)arg2) -> tuple :
    l1.closestPoints(l2) -- returns a tuple with
    two points:
       (l1.closestPoint(l2), l2.closestPoint(l1)
    

    C++ signature :
        boost::python::tuple closestPoints(Imath_3_1::Line3<float> {lvalue},Imath_3_1::Line3<float>)'''
    ...
    def closestTriangleVertex (self, *args, **kwargs):
      '''
closestTriangleVertex( (Line3f)arg1, (V3f)arg2, (V3f)arg3, (V3f)arg4) -> V3f :
    l.closestTriangleVertex(v0, v1, v2) -- returns
    a copy of v0, v1, or v2, depending on which is
    closest to line l.
    

    C++ signature :
        Imath_3_1::Vec3<float> closestTriangleVertex(Imath_3_1::Line3<float> {lvalue},Imath_3_1::Vec3<float>,Imath_3_1::Vec3<float>,Imath_3_1::Vec3<float>)

closestTriangleVertex( (Line3f)arg1, (tuple)arg2, (tuple)arg3, (tuple)arg4) -> V3f :

    C++ signature :
        Imath_3_1::Vec3<float> closestTriangleVertex(Imath_3_1::Line3<float> {lvalue},boost::python::tuple,boost::python::tuple,boost::python::tuple)'''
    ...
    def dir (self, *args, **kwargs):
      '''
dir( (Line3f)arg1) -> V3f :
    l.dir() -- returns the direction of line l
    

    C++ signature :
        Imath_3_1::Vec3<float> dir(Imath_3_1::Line3<float> {lvalue})'''
    ...
    def distanceTo (self, *args, **kwargs):
      '''
distanceTo( (Line3f)arg1, (V3f)arg2) -> float :
    l.distanceTo(p) -- returns the distance from
       line l to point p
    

    C++ signature :
        float distanceTo(Imath_3_1::Line3<float> {lvalue},Imath_3_1::Vec3<float> {lvalue})

distanceTo( (Line3f)arg1, (Line3f)arg2) -> float :
    l1.distanceTo(l2) -- returns the distance from
       line l1 to line l2
    

    C++ signature :
        float distanceTo(Imath_3_1::Line3<float> {lvalue},Imath_3_1::Line3<float> {lvalue})

distanceTo( (Line3f)arg1, (tuple)arg2) -> float :

    C++ signature :
        float distanceTo(Imath_3_1::Line3<float>,boost::python::tuple)'''
    ...
    def intersectWithTriangle (self, *args, **kwargs):
      '''
intersectWithTriangle( (Line3f)arg1, (V3f)arg2, (V3f)arg3, (V3f)arg4) -> object :

    C++ signature :
        boost::python::api::object intersectWithTriangle(Imath_3_1::Line3<float> {lvalue},Imath_3_1::Vec3<float>,Imath_3_1::Vec3<float>,Imath_3_1::Vec3<float>)

intersectWithTriangle( (Line3f)arg1, (V3f)arg2, (V3f)arg3, (V3f)arg4, (V3f)arg5, (V3f)arg6, (bool)arg7) -> bool :
    l.intersectWithTriangle(v0, v1, v2) -- computes the
    intersection of line l and triangle (v0, v1, v2).
    
    If the line and the triangle do not intersect,
    None is returned.
    If the line and the triangle intersect, a tuple
    (p, b, f) is returned:
    
       p  intersection point in 3D space
    
       b  intersection point in barycentric coordinates
    
       f  1 if the line hits the triangle from the
          front (((v2-v1) % (v1-v2)) ^ l.dir() < 0),
          0 if the line hits the trianble from the
          back
    
    

    C++ signature :
        bool intersectWithTriangle(Imath_3_1::Line3<float> {lvalue},Imath_3_1::Vec3<float>,Imath_3_1::Vec3<float>,Imath_3_1::Vec3<float>,Imath_3_1::Vec3<float> {lvalue},Imath_3_1::Vec3<float> {lvalue},bool {lvalue})

intersectWithTriangle( (Line3f)arg1, (tuple)arg2, (tuple)arg3, (tuple)arg4) -> tuple :

    C++ signature :
        boost::python::tuple intersectWithTriangle(Imath_3_1::Line3<float> {lvalue},boost::python::tuple,boost::python::tuple,boost::python::tuple)'''
    ...
    def pointAt (self, *args, **kwargs):
      '''
pointAt( (Line3f)arg1, (float)arg2) -> V3f :
    l.pointAt(t) -- returns l.pos() + t * l.dir()

    C++ signature :
        Imath_3_1::Vec3<float> pointAt(Imath_3_1::Line3<float> {lvalue},float)'''
    ...
    def pos (self, *args, **kwargs):
      '''
pos( (Line3f)arg1) -> V3f :
    l.pos() -- returns the start point of line l

    C++ signature :
        Imath_3_1::Vec3<float> pos(Imath_3_1::Line3<float> {lvalue})'''
    ...
    def rotatePoint (self, *args, **kwargs):
      '''
rotatePoint( (Line3f)arg1, (V3f)arg2, (float)arg3) -> V3f :
    l.rotatePoint(p,r) -- rotates point p around
    line by angle r (in radians), and returns the
    result (p is not modified)
    

    C++ signature :
        Imath_3_1::Vec3<float> rotatePoint(Imath_3_1::Line3<float> {lvalue},Imath_3_1::Vec3<float>,float)

rotatePoint( (Line3f)arg1, (tuple)arg2, (float)arg3) -> V3f :

    C++ signature :
        Imath_3_1::Vec3<float> rotatePoint(Imath_3_1::Line3<float> {lvalue},boost::python::tuple,float)'''
    ...
    def set (self, *args, **kwargs):
      '''
set( (Line3f)arg1, (V3f)arg2, (V3f)arg3) -> None :
    l.set(p1, p2) -- sets the start point
    and direction of line l by calling
       l.setPos (p1)
       l.setDir (p2 - p1)
    

    C++ signature :
        void set(Imath_3_1::Line3<float> {lvalue},Imath_3_1::Vec3<float>,Imath_3_1::Vec3<float>)

set( (Line3f)arg1, (tuple)arg2, (tuple)arg3) -> None :

    C++ signature :
        void set(Imath_3_1::Line3<float> {lvalue},boost::python::tuple,boost::python::tuple)'''
    ...
    def setDir (self, *args, **kwargs):
      '''
setDir( (Line3f)arg1, (V3f)arg2) -> None :
    l.setDir(d) -- sets the direction of line l
    to d.normalized().
    

    C++ signature :
        void setDir(Imath_3_1::Line3<float> {lvalue},Imath_3_1::Vec3<float>)

setDir( (Line3f)arg1, (tuple)arg2) -> None :

    C++ signature :
        void setDir(Imath_3_1::Line3<float> {lvalue},boost::python::tuple)'''
    ...
    def setPos (self, *args, **kwargs):
      '''
setPos( (Line3f)arg1, (V3f)arg2) -> None :
    l.setPos(p) -- sets the start point of line l to p

    C++ signature :
        void setPos(Imath_3_1::Line3<float> {lvalue},Imath_3_1::Vec3<float>)

setPos( (Line3f)arg1, (tuple)arg2) -> None :

    C++ signature :
        void setPos(Imath_3_1::Line3<float> {lvalue},boost::python::tuple)'''
    ...

def M22d (*args):
      '''
__init__(boost::python::api::object, Imath_3_1::Matrix22<double>)
__init__(boost::python::api::object, Imath_3_1::Matrix22<float>)
__init__(boost::python::api::object, boost::python::tuple, boost::python::tuple)
__init__(_object*, double, double, double, double)
__init__(_object*, double)
__init__(_object*)
__init__(_object*, Imath_3_1::Matrix22<double>)

'''      
    ...

class M22d:
    def baseTypeEpsilon (self, *args, **kwargs):
      '''
baseTypeEpsilon() -> float :
    baseTypeEpsilon() epsilon value of the base type of the vector

    C++ signature :
        double baseTypeEpsilon()'''
    ...
    def baseTypeLowest (self, *args, **kwargs):
      '''
baseTypeLowest() -> float :
    baseTypeLowest() largest negative value of the base type of the vector

    C++ signature :
        double baseTypeLowest()'''
    ...
    def baseTypeMax (self, *args, **kwargs):
      '''
baseTypeMax() -> float :
    baseTypeMax() max value of the base type of the vector

    C++ signature :
        double baseTypeMax()'''
    ...
    def baseTypeSmallest (self, *args, **kwargs):
      '''
baseTypeSmallest() -> float :
    baseTypeSmallest() smallest value of the base type of the vector

    C++ signature :
        double baseTypeSmallest()'''
    ...
    def determinant (self, *args, **kwargs):
      '''
determinant( (M22d)arg1) -> float :
    determinant() return the determinant of this matrix

    C++ signature :
        double determinant(Imath_3_1::Matrix22<double> {lvalue})'''
    ...
    def equalWithAbsError (self, *args, **kwargs):
      '''
equalWithAbsError( (M22d)arg1, (M22d)arg2, (float)arg3) -> bool :
    m1.equalWithAbsError(m2,e) true if the elements of v1 and v2 are the same with an absolute error of no more than e, i.e., abs(m1[i] - m2[i]) <= e

    C++ signature :
        bool equalWithAbsError(Imath_3_1::Matrix22<double> {lvalue},Imath_3_1::Matrix22<double>,double)'''
    ...
    def equalWithRelError (self, *args, **kwargs):
      '''
equalWithRelError( (M22d)arg1, (M22d)arg2, (float)arg3) -> bool :
    m1.equalWithAbsError(m2,e) true if the elements of m1 and m2 are the same with an absolute error of no more than e, i.e., abs(m1[i] - m2[i]) <= e * abs(m1[i])

    C++ signature :
        bool equalWithRelError(Imath_3_1::Matrix22<double> {lvalue},Imath_3_1::Matrix22<double>,double)'''
    ...
    def extractEuler (self, *args, **kwargs):
      '''
extractEuler( (M22d)arg1, (V2d)arg2) -> None :
    M.extractEuler(r) -- extracts the rotation component of M into r. Assumes that M contains no shear or non-uniform scaling; results are meaningless if it does.

    C++ signature :
        void extractEuler(Imath_3_1::Matrix22<double> {lvalue},Imath_3_1::Vec2<double> {lvalue})'''
    ...
    def inverse (self, *args, **kwargs):
      '''
inverse( (M22d)arg1 [, (bool)arg2]) -> M22d :
    inverse() return an inverted copy of this matrix

    C++ signature :
        Imath_3_1::Matrix22<double> inverse(Imath_3_1::Matrix22<double> {lvalue} [,bool])'''
    ...
    def invert (self, *args, **kwargs):
      '''
invert( (M22d)arg1 [, (bool)arg2]) -> M22d :
    invert() invert this matrix

    C++ signature :
        Imath_3_1::Matrix22<double> invert(Imath_3_1::Matrix22<double> {lvalue} [,bool])'''
    ...
    def makeIdentity (self, *args, **kwargs):
      '''
makeIdentity( (M22d)arg1) -> None :
    makeIdentity() make this matrix the identity matrix

    C++ signature :
        void makeIdentity(Imath_3_1::Matrix22<double> {lvalue})'''
    ...
    def multDirMatrix (self, *args, **kwargs):
      '''
multDirMatrix( (M22d)arg1, (V2d)arg2, (V2d)arg3) -> None :
    mult matrix

    C++ signature :
        void multDirMatrix(Imath_3_1::Matrix22<double> {lvalue},Imath_3_1::Vec2<double>,Imath_3_1::Vec2<double> {lvalue})

multDirMatrix( (M22d)arg1, (V2d)arg2) -> V2d :
    mult matrix

    C++ signature :
        Imath_3_1::Vec2<double> multDirMatrix(Imath_3_1::Matrix22<double> {lvalue},Imath_3_1::Vec2<double>)

multDirMatrix( (M22d)arg1, (V2dArray)arg2) -> V2dArray :
    mult matrix

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec2<double> > multDirMatrix(Imath_3_1::Matrix22<double> {lvalue},PyImath::FixedArray<Imath_3_1::Vec2<double> >)

multDirMatrix( (M22d)arg1, (V2f)arg2, (V2f)arg3) -> None :
    mult matrix

    C++ signature :
        void multDirMatrix(Imath_3_1::Matrix22<double> {lvalue},Imath_3_1::Vec2<float>,Imath_3_1::Vec2<float> {lvalue})

multDirMatrix( (M22d)arg1, (V2f)arg2) -> V2f :
    mult matrix

    C++ signature :
        Imath_3_1::Vec2<float> multDirMatrix(Imath_3_1::Matrix22<double> {lvalue},Imath_3_1::Vec2<float>)

multDirMatrix( (M22d)arg1, (V2fArray)arg2) -> V2fArray :
    mult matrix

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec2<float> > multDirMatrix(Imath_3_1::Matrix22<double> {lvalue},PyImath::FixedArray<Imath_3_1::Vec2<float> >)'''
    ...
    def negate (self, *args, **kwargs):
      '''
negate( (M22d)arg1) -> M22d :
    negate() negate all entries in this matrix

    C++ signature :
        Imath_3_1::Matrix22<double> negate(Imath_3_1::Matrix22<double> {lvalue})'''
    ...
    def rotate (self, *args, **kwargs):
      '''
rotate( (M22d)arg1, (float)arg2) -> M22d :
    rotate matrix

    C++ signature :
        Imath_3_1::Matrix22<double> rotate(Imath_3_1::Matrix22<double> {lvalue},double)'''
    ...
    def scale (self, *args, **kwargs):
      '''
scale( (M22d)arg1, (float)arg2) -> M22d :
    scale matrix

    C++ signature :
        Imath_3_1::Matrix22<double> scale(Imath_3_1::Matrix22<double> {lvalue},double)

scale( (M22d)arg1, (V2d)arg2) -> M22d :
    scale matrix

    C++ signature :
        Imath_3_1::Matrix22<double> scale(Imath_3_1::Matrix22<double> {lvalue},Imath_3_1::Vec2<double>)

scale( (M22d)arg1, (tuple)arg2) -> M22d :
    scale matrix

    C++ signature :
        Imath_3_1::Matrix22<double> scale(Imath_3_1::Matrix22<double> {lvalue},boost::python::tuple)'''
    ...
    def setRotation (self, *args, **kwargs):
      '''
setRotation( (M22d)arg1, (float)arg2) -> M22d :
    setRotation()

    C++ signature :
        Imath_3_1::Matrix22<double> setRotation(Imath_3_1::Matrix22<double> {lvalue},double)'''
    ...
    def setScale (self, *args, **kwargs):
      '''
setScale( (M22d)arg1, (float)arg2) -> M22d :
    setScale()

    C++ signature :
        Imath_3_1::Matrix22<double> setScale(Imath_3_1::Matrix22<double> {lvalue},double)

setScale( (M22d)arg1, (V2d)arg2) -> M22d :
    setScale()

    C++ signature :
        Imath_3_1::Matrix22<double> setScale(Imath_3_1::Matrix22<double> {lvalue},Imath_3_1::Vec2<double>)

setScale( (M22d)arg1, (tuple)arg2) -> M22d :
    setScale()

    C++ signature :
        Imath_3_1::Matrix22<double> setScale(Imath_3_1::Matrix22<double> {lvalue},boost::python::tuple)'''
    ...
    def setValue (self, *args, **kwargs):
      '''
setValue( (M22d)arg1, (M22d)arg2) -> None :
    setValue()

    C++ signature :
        void setValue(Imath_3_1::Matrix22<double> {lvalue},Imath_3_1::Matrix22<double>)'''
    ...
    def transpose (self, *args, **kwargs):
      '''
transpose( (M22d)arg1) -> M22d :
    transpose() transpose this matrix

    C++ signature :
        Imath_3_1::Matrix22<double> transpose(Imath_3_1::Matrix22<double> {lvalue})'''
    ...
    def transposed (self, *args, **kwargs):
      '''
transposed( (M22d)arg1) -> M22d :
    transposed() return a transposed copy of this matrix

    C++ signature :
        Imath_3_1::Matrix22<double> transposed(Imath_3_1::Matrix22<double> {lvalue})'''
    ...

def M22dArray (*args):
      '''
__init__(_object*, PyImath::FixedArray<Imath_3_1::Matrix22<double> >)
__init__(_object*, Imath_3_1::Matrix22<double>, unsigned long)
__init__(_object*, PyImath::FixedArray<Imath_3_1::Matrix22<double> >)
__init__(_object*, unsigned long)

'''      
    ...

class M22dArray:
    def ifelse (self, *args, **kwargs):
      '''
ifelse( (M22dArray)arg1, (IntArray)arg2, (M22d)arg3) -> M22dArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Matrix22<double> > ifelse(PyImath::FixedArray<Imath_3_1::Matrix22<double> > {lvalue},PyImath::FixedArray<int>,Imath_3_1::Matrix22<double>)

ifelse( (M22dArray)arg1, (IntArray)arg2, (M22dArray)arg3) -> M22dArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Matrix22<double> > ifelse(PyImath::FixedArray<Imath_3_1::Matrix22<double> > {lvalue},PyImath::FixedArray<int>,PyImath::FixedArray<Imath_3_1::Matrix22<double> >)'''
    ...
    def inverse (self, *args, **kwargs):
      '''
inverse( (M22dArray)arg1 [, (bool)arg2]) -> M22dArray :
    inverse() return an inverted copy of this matrix

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Matrix22<double> > inverse(PyImath::FixedArray<Imath_3_1::Matrix22<double> > {lvalue} [,bool])'''
    ...
    def invert (self, *args, **kwargs):
      '''
invert( (M22dArray)arg1 [, (bool)arg2]) -> M22dArray :
    invert() invert these matricies

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Matrix22<double> > {lvalue} invert(PyImath::FixedArray<Imath_3_1::Matrix22<double> > {lvalue} [,bool])'''
    ...
    def makeReadOnly (self, *args, **kwargs):
      '''
makeReadOnly( (M22dArray)arg1) -> None :

    C++ signature :
        void makeReadOnly(PyImath::FixedArray<Imath_3_1::Matrix22<double> > {lvalue})'''
    ...
    def writable (self, *args, **kwargs):
      '''
writable( (M22dArray)arg1) -> bool :

    C++ signature :
        bool writable(PyImath::FixedArray<Imath_3_1::Matrix22<double> > {lvalue})'''
    ...

def M22dRow (*args):
      '''

'''      
    ...

class M22dRow:

def M22f (*args):
      '''
__init__(boost::python::api::object, Imath_3_1::Matrix22<double>)
__init__(boost::python::api::object, Imath_3_1::Matrix22<float>)
__init__(boost::python::api::object, boost::python::tuple, boost::python::tuple)
__init__(_object*, float, float, float, float)
__init__(_object*, float)
__init__(_object*)
__init__(_object*, Imath_3_1::Matrix22<float>)

'''      
    ...

class M22f:
    def baseTypeEpsilon (self, *args, **kwargs):
      '''
baseTypeEpsilon() -> float :
    baseTypeEpsilon() epsilon value of the base type of the vector

    C++ signature :
        float baseTypeEpsilon()'''
    ...
    def baseTypeLowest (self, *args, **kwargs):
      '''
baseTypeLowest() -> float :
    baseTypeLowest() largest negative value of the base type of the vector

    C++ signature :
        float baseTypeLowest()'''
    ...
    def baseTypeMax (self, *args, **kwargs):
      '''
baseTypeMax() -> float :
    baseTypeMax() max value of the base type of the vector

    C++ signature :
        float baseTypeMax()'''
    ...
    def baseTypeSmallest (self, *args, **kwargs):
      '''
baseTypeSmallest() -> float :
    baseTypeSmallest() smallest value of the base type of the vector

    C++ signature :
        float baseTypeSmallest()'''
    ...
    def determinant (self, *args, **kwargs):
      '''
determinant( (M22f)arg1) -> float :
    determinant() return the determinant of this matrix

    C++ signature :
        float determinant(Imath_3_1::Matrix22<float> {lvalue})'''
    ...
    def equalWithAbsError (self, *args, **kwargs):
      '''
equalWithAbsError( (M22f)arg1, (M22f)arg2, (float)arg3) -> bool :
    m1.equalWithAbsError(m2,e) true if the elements of v1 and v2 are the same with an absolute error of no more than e, i.e., abs(m1[i] - m2[i]) <= e

    C++ signature :
        bool equalWithAbsError(Imath_3_1::Matrix22<float> {lvalue},Imath_3_1::Matrix22<float>,float)'''
    ...
    def equalWithRelError (self, *args, **kwargs):
      '''
equalWithRelError( (M22f)arg1, (M22f)arg2, (float)arg3) -> bool :
    m1.equalWithAbsError(m2,e) true if the elements of m1 and m2 are the same with an absolute error of no more than e, i.e., abs(m1[i] - m2[i]) <= e * abs(m1[i])

    C++ signature :
        bool equalWithRelError(Imath_3_1::Matrix22<float> {lvalue},Imath_3_1::Matrix22<float>,float)'''
    ...
    def extractEuler (self, *args, **kwargs):
      '''
extractEuler( (M22f)arg1, (V2f)arg2) -> None :
    M.extractEuler(r) -- extracts the rotation component of M into r. Assumes that M contains no shear or non-uniform scaling; results are meaningless if it does.

    C++ signature :
        void extractEuler(Imath_3_1::Matrix22<float> {lvalue},Imath_3_1::Vec2<float> {lvalue})'''
    ...
    def inverse (self, *args, **kwargs):
      '''
inverse( (M22f)arg1 [, (bool)arg2]) -> M22f :
    inverse() return an inverted copy of this matrix

    C++ signature :
        Imath_3_1::Matrix22<float> inverse(Imath_3_1::Matrix22<float> {lvalue} [,bool])'''
    ...
    def invert (self, *args, **kwargs):
      '''
invert( (M22f)arg1 [, (bool)arg2]) -> M22f :
    invert() invert this matrix

    C++ signature :
        Imath_3_1::Matrix22<float> invert(Imath_3_1::Matrix22<float> {lvalue} [,bool])'''
    ...
    def makeIdentity (self, *args, **kwargs):
      '''
makeIdentity( (M22f)arg1) -> None :
    makeIdentity() make this matrix the identity matrix

    C++ signature :
        void makeIdentity(Imath_3_1::Matrix22<float> {lvalue})'''
    ...
    def multDirMatrix (self, *args, **kwargs):
      '''
multDirMatrix( (M22f)arg1, (V2d)arg2, (V2d)arg3) -> None :
    mult matrix

    C++ signature :
        void multDirMatrix(Imath_3_1::Matrix22<float> {lvalue},Imath_3_1::Vec2<double>,Imath_3_1::Vec2<double> {lvalue})

multDirMatrix( (M22f)arg1, (V2d)arg2) -> V2d :
    mult matrix

    C++ signature :
        Imath_3_1::Vec2<double> multDirMatrix(Imath_3_1::Matrix22<float> {lvalue},Imath_3_1::Vec2<double>)

multDirMatrix( (M22f)arg1, (V2dArray)arg2) -> V2dArray :
    mult matrix

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec2<double> > multDirMatrix(Imath_3_1::Matrix22<float> {lvalue},PyImath::FixedArray<Imath_3_1::Vec2<double> >)

multDirMatrix( (M22f)arg1, (V2f)arg2, (V2f)arg3) -> None :
    mult matrix

    C++ signature :
        void multDirMatrix(Imath_3_1::Matrix22<float> {lvalue},Imath_3_1::Vec2<float>,Imath_3_1::Vec2<float> {lvalue})

multDirMatrix( (M22f)arg1, (V2f)arg2) -> V2f :
    mult matrix

    C++ signature :
        Imath_3_1::Vec2<float> multDirMatrix(Imath_3_1::Matrix22<float> {lvalue},Imath_3_1::Vec2<float>)

multDirMatrix( (M22f)arg1, (V2fArray)arg2) -> V2fArray :
    mult matrix

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec2<float> > multDirMatrix(Imath_3_1::Matrix22<float> {lvalue},PyImath::FixedArray<Imath_3_1::Vec2<float> >)'''
    ...
    def negate (self, *args, **kwargs):
      '''
negate( (M22f)arg1) -> M22f :
    negate() negate all entries in this matrix

    C++ signature :
        Imath_3_1::Matrix22<float> negate(Imath_3_1::Matrix22<float> {lvalue})'''
    ...
    def rotate (self, *args, **kwargs):
      '''
rotate( (M22f)arg1, (float)arg2) -> M22f :
    rotate matrix

    C++ signature :
        Imath_3_1::Matrix22<float> rotate(Imath_3_1::Matrix22<float> {lvalue},float)'''
    ...
    def scale (self, *args, **kwargs):
      '''
scale( (M22f)arg1, (float)arg2) -> M22f :
    scale matrix

    C++ signature :
        Imath_3_1::Matrix22<float> scale(Imath_3_1::Matrix22<float> {lvalue},float)

scale( (M22f)arg1, (V2f)arg2) -> M22f :
    scale matrix

    C++ signature :
        Imath_3_1::Matrix22<float> scale(Imath_3_1::Matrix22<float> {lvalue},Imath_3_1::Vec2<float>)

scale( (M22f)arg1, (tuple)arg2) -> M22f :
    scale matrix

    C++ signature :
        Imath_3_1::Matrix22<float> scale(Imath_3_1::Matrix22<float> {lvalue},boost::python::tuple)'''
    ...
    def setRotation (self, *args, **kwargs):
      '''
setRotation( (M22f)arg1, (float)arg2) -> M22f :
    setRotation()

    C++ signature :
        Imath_3_1::Matrix22<float> setRotation(Imath_3_1::Matrix22<float> {lvalue},float)'''
    ...
    def setScale (self, *args, **kwargs):
      '''
setScale( (M22f)arg1, (float)arg2) -> M22f :
    setScale()

    C++ signature :
        Imath_3_1::Matrix22<float> setScale(Imath_3_1::Matrix22<float> {lvalue},float)

setScale( (M22f)arg1, (V2f)arg2) -> M22f :
    setScale()

    C++ signature :
        Imath_3_1::Matrix22<float> setScale(Imath_3_1::Matrix22<float> {lvalue},Imath_3_1::Vec2<float>)

setScale( (M22f)arg1, (tuple)arg2) -> M22f :
    setScale()

    C++ signature :
        Imath_3_1::Matrix22<float> setScale(Imath_3_1::Matrix22<float> {lvalue},boost::python::tuple)'''
    ...
    def setValue (self, *args, **kwargs):
      '''
setValue( (M22f)arg1, (M22f)arg2) -> None :
    setValue()

    C++ signature :
        void setValue(Imath_3_1::Matrix22<float> {lvalue},Imath_3_1::Matrix22<float>)'''
    ...
    def transpose (self, *args, **kwargs):
      '''
transpose( (M22f)arg1) -> M22f :
    transpose() transpose this matrix

    C++ signature :
        Imath_3_1::Matrix22<float> transpose(Imath_3_1::Matrix22<float> {lvalue})'''
    ...
    def transposed (self, *args, **kwargs):
      '''
transposed( (M22f)arg1) -> M22f :
    transposed() return a transposed copy of this matrix

    C++ signature :
        Imath_3_1::Matrix22<float> transposed(Imath_3_1::Matrix22<float> {lvalue})'''
    ...

def M22fArray (*args):
      '''
__init__(_object*, PyImath::FixedArray<Imath_3_1::Matrix22<float> >)
__init__(_object*, Imath_3_1::Matrix22<float>, unsigned long)
__init__(_object*, PyImath::FixedArray<Imath_3_1::Matrix22<float> >)
__init__(_object*, unsigned long)

'''      
    ...

class M22fArray:
    def ifelse (self, *args, **kwargs):
      '''
ifelse( (M22fArray)arg1, (IntArray)arg2, (M22f)arg3) -> M22fArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Matrix22<float> > ifelse(PyImath::FixedArray<Imath_3_1::Matrix22<float> > {lvalue},PyImath::FixedArray<int>,Imath_3_1::Matrix22<float>)

ifelse( (M22fArray)arg1, (IntArray)arg2, (M22fArray)arg3) -> M22fArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Matrix22<float> > ifelse(PyImath::FixedArray<Imath_3_1::Matrix22<float> > {lvalue},PyImath::FixedArray<int>,PyImath::FixedArray<Imath_3_1::Matrix22<float> >)'''
    ...
    def inverse (self, *args, **kwargs):
      '''
inverse( (M22fArray)arg1 [, (bool)arg2]) -> M22fArray :
    inverse() return an inverted copy of this matrix

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Matrix22<float> > inverse(PyImath::FixedArray<Imath_3_1::Matrix22<float> > {lvalue} [,bool])'''
    ...
    def invert (self, *args, **kwargs):
      '''
invert( (M22fArray)arg1 [, (bool)arg2]) -> M22fArray :
    invert() invert these matricies

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Matrix22<float> > {lvalue} invert(PyImath::FixedArray<Imath_3_1::Matrix22<float> > {lvalue} [,bool])'''
    ...
    def makeReadOnly (self, *args, **kwargs):
      '''
makeReadOnly( (M22fArray)arg1) -> None :

    C++ signature :
        void makeReadOnly(PyImath::FixedArray<Imath_3_1::Matrix22<float> > {lvalue})'''
    ...
    def writable (self, *args, **kwargs):
      '''
writable( (M22fArray)arg1) -> bool :

    C++ signature :
        bool writable(PyImath::FixedArray<Imath_3_1::Matrix22<float> > {lvalue})'''
    ...

def M22fRow (*args):
      '''

'''      
    ...

class M22fRow:

def M33d (*args):
      '''
__init__(boost::python::api::object, Imath_3_1::Matrix33<double>)
__init__(boost::python::api::object, Imath_3_1::Matrix33<float>)
__init__(boost::python::api::object, boost::python::tuple, boost::python::tuple, boost::python::tuple)
__init__(_object*, double, double, double, double, double, double, double, double, double)
__init__(_object*, double)
__init__(_object*)
__init__(_object*, Imath_3_1::Matrix33<double>)

'''      
    ...

class M33d:
    def baseTypeEpsilon (self, *args, **kwargs):
      '''
baseTypeEpsilon() -> float :
    baseTypeEpsilon() epsilon value of the base type of the vector

    C++ signature :
        double baseTypeEpsilon()'''
    ...
    def baseTypeLowest (self, *args, **kwargs):
      '''
baseTypeLowest() -> float :
    baseTypeLowest() largest negative value of the base type of the vector

    C++ signature :
        double baseTypeLowest()'''
    ...
    def baseTypeMax (self, *args, **kwargs):
      '''
baseTypeMax() -> float :
    baseTypeMax() max value of the base type of the vector

    C++ signature :
        double baseTypeMax()'''
    ...
    def baseTypeSmallest (self, *args, **kwargs):
      '''
baseTypeSmallest() -> float :
    baseTypeSmallest() smallest value of the base type of the vector

    C++ signature :
        double baseTypeSmallest()'''
    ...
    def determinant (self, *args, **kwargs):
      '''
determinant( (M33d)arg1) -> float :
    determinant() return the determinant of this matrix

    C++ signature :
        double determinant(Imath_3_1::Matrix33<double> {lvalue})'''
    ...
    def equalWithAbsError (self, *args, **kwargs):
      '''
equalWithAbsError( (M33d)arg1, (M33d)arg2, (float)arg3) -> bool :
    m1.equalWithAbsError(m2,e) true if the elements of v1 and v2 are the same with an absolute error of no more than e, i.e., abs(m1[i] - m2[i]) <= e

    C++ signature :
        bool equalWithAbsError(Imath_3_1::Matrix33<double> {lvalue},Imath_3_1::Matrix33<double>,double)'''
    ...
    def equalWithRelError (self, *args, **kwargs):
      '''
equalWithRelError( (M33d)arg1, (M33d)arg2, (float)arg3) -> bool :
    m1.equalWithAbsError(m2,e) true if the elements of m1 and m2 are the same with an absolute error of no more than e, i.e., abs(m1[i] - m2[i]) <= e * abs(m1[i])

    C++ signature :
        bool equalWithRelError(Imath_3_1::Matrix33<double> {lvalue},Imath_3_1::Matrix33<double>,double)'''
    ...
    def extractAndRemoveScalingAndShear (self, *args, **kwargs):
      '''
extractAndRemoveScalingAndShear( (M33d)arg1, (V2d)arg2, (V2d)arg3 [, (int)arg4]) -> None :
    M.extractAndRemoveScalingAndShear(scl, shr, [exc]) -- extracts the scaling component of M into scl and the shearing component of M into shr.  Also removes the scaling and shearing components from M.  Returns 1 unless the scaling component is nearly 0, in which case 0 is returned. If optional arg. exc == 1, then if the scaling component is nearly 0, then MathExc is thrown. 

    C++ signature :
        void extractAndRemoveScalingAndShear(Imath_3_1::Matrix33<double> {lvalue},Imath_3_1::Vec2<double> {lvalue},Imath_3_1::Vec2<double> {lvalue} [,int])'''
    ...
    def extractEuler (self, *args, **kwargs):
      '''
extractEuler( (M33d)arg1, (V2d)arg2) -> None :
    M.extractEulerZYX(r) -- extracts the rotation component of M into r. Assumes that M contains no shear or non-uniform scaling; results are meaningless if it does.

    C++ signature :
        void extractEuler(Imath_3_1::Matrix33<double> {lvalue},Imath_3_1::Vec2<double> {lvalue})'''
    ...
    def extractSHRT (self, *args, **kwargs):
      '''
extractSHRT( (M33d)arg1, (V2d)arg2, (V2d)arg3, (V2d)arg4, (V2d)arg5 [, (int)arg6]) -> int :
    M.extractSHRT(Vs, Vh, Vr, Vt, [exc]) -- extracts the scaling component of M into Vs, the shearing component of M in Vh (as XY, XZ, YZ shear factors), the rotation of M into Vr (as Euler angles in the order XYZ), and the translaation of M into Vt. If optional arg. exc == 1, then if the scaling component is nearly 0, then MathExc is thrown. 

    C++ signature :
        int extractSHRT(Imath_3_1::Matrix33<double> {lvalue},Imath_3_1::Vec2<double> {lvalue},Imath_3_1::Vec2<double> {lvalue},Imath_3_1::Vec2<double> {lvalue},Imath_3_1::Vec2<double> {lvalue} [,int])'''
    ...
    def extractScaling (self, *args, **kwargs):
      '''
extractScaling( (M33d)arg1, (V2d)arg2 [, (int)arg3]) -> None :
    extract scaling

    C++ signature :
        void extractScaling(Imath_3_1::Matrix33<double> {lvalue},Imath_3_1::Vec2<double> {lvalue} [,int])'''
    ...
    def extractScalingAndShear (self, *args, **kwargs):
      '''
extractScalingAndShear( (M33d)arg1, (V2d)arg2, (V2d)arg3 [, (int)arg4]) -> None :
    extract scaling

    C++ signature :
        void extractScalingAndShear(Imath_3_1::Matrix33<double> {lvalue},Imath_3_1::Vec2<double> {lvalue},Imath_3_1::Vec2<double> {lvalue} [,int])'''
    ...
    def fastMinor (self, *args, **kwargs):
      '''
fastMinor( (M33d)arg1, (int)arg2, (int)arg3, (int)arg4, (int)arg5) -> float :
    fastMinor() return the matrix minor using the specified rows and columns of this matrix

    C++ signature :
        double fastMinor(Imath_3_1::Matrix33<double> {lvalue},int,int,int,int)'''
    ...
    def gjInverse (self, *args, **kwargs):
      '''
gjInverse( (M33d)arg1 [, (bool)arg2]) -> M33d :
    gjInverse() return an inverted copy of this matrix

    C++ signature :
        Imath_3_1::Matrix33<double> gjInverse(Imath_3_1::Matrix33<double> {lvalue} [,bool])'''
    ...
    def gjInvert (self, *args, **kwargs):
      '''
gjInvert( (M33d)arg1 [, (bool)arg2]) -> M33d :
    gjInvert() invert this matrix

    C++ signature :
        Imath_3_1::Matrix33<double> gjInvert(Imath_3_1::Matrix33<double> {lvalue} [,bool])'''
    ...
    def inverse (self, *args, **kwargs):
      '''
inverse( (M33d)arg1 [, (bool)arg2]) -> M33d :
    inverse() return an inverted copy of this matrix

    C++ signature :
        Imath_3_1::Matrix33<double> inverse(Imath_3_1::Matrix33<double> {lvalue} [,bool])'''
    ...
    def invert (self, *args, **kwargs):
      '''
invert( (M33d)arg1 [, (bool)arg2]) -> M33d :
    invert() invert this matrix

    C++ signature :
        Imath_3_1::Matrix33<double> invert(Imath_3_1::Matrix33<double> {lvalue} [,bool])'''
    ...
    def makeIdentity (self, *args, **kwargs):
      '''
makeIdentity( (M33d)arg1) -> None :
    makeIdentity() make this matrix the identity matrix

    C++ signature :
        void makeIdentity(Imath_3_1::Matrix33<double> {lvalue})'''
    ...
    def minorOf (self, *args, **kwargs):
      '''
minorOf( (M33d)arg1, (int)arg2, (int)arg3) -> float :
    minorOf() return the matrix minor of the (row,col) element of this matrix

    C++ signature :
        double minorOf(Imath_3_1::Matrix33<double> {lvalue},int,int)'''
    ...
    def multDirMatrix (self, *args, **kwargs):
      '''
multDirMatrix( (M33d)arg1, (V2d)arg2, (V2d)arg3) -> None :
    mult matrix

    C++ signature :
        void multDirMatrix(Imath_3_1::Matrix33<double> {lvalue},Imath_3_1::Vec2<double>,Imath_3_1::Vec2<double> {lvalue})

multDirMatrix( (M33d)arg1, (V2d)arg2) -> V2d :
    mult matrix

    C++ signature :
        Imath_3_1::Vec2<double> multDirMatrix(Imath_3_1::Matrix33<double> {lvalue},Imath_3_1::Vec2<double>)

multDirMatrix( (M33d)arg1, (V2dArray)arg2) -> V2dArray :
    mult matrix

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec2<double> > multDirMatrix(Imath_3_1::Matrix33<double> {lvalue},PyImath::FixedArray<Imath_3_1::Vec2<double> >)

multDirMatrix( (M33d)arg1, (V2f)arg2, (V2f)arg3) -> None :
    mult matrix

    C++ signature :
        void multDirMatrix(Imath_3_1::Matrix33<double> {lvalue},Imath_3_1::Vec2<float>,Imath_3_1::Vec2<float> {lvalue})

multDirMatrix( (M33d)arg1, (V2f)arg2) -> V2f :
    mult matrix

    C++ signature :
        Imath_3_1::Vec2<float> multDirMatrix(Imath_3_1::Matrix33<double> {lvalue},Imath_3_1::Vec2<float>)

multDirMatrix( (M33d)arg1, (V2fArray)arg2) -> V2fArray :
    mult matrix

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec2<float> > multDirMatrix(Imath_3_1::Matrix33<double> {lvalue},PyImath::FixedArray<Imath_3_1::Vec2<float> >)'''
    ...
    def multVecMatrix (self, *args, **kwargs):
      '''
multVecMatrix( (M33d)arg1, (V2d)arg2, (V2d)arg3) -> None :
    mult matrix

    C++ signature :
        void multVecMatrix(Imath_3_1::Matrix33<double> {lvalue},Imath_3_1::Vec2<double>,Imath_3_1::Vec2<double> {lvalue})

multVecMatrix( (M33d)arg1, (V2d)arg2) -> V2d :
    mult matrix

    C++ signature :
        Imath_3_1::Vec2<double> multVecMatrix(Imath_3_1::Matrix33<double> {lvalue},Imath_3_1::Vec2<double>)

multVecMatrix( (M33d)arg1, (V2dArray)arg2) -> V2dArray :
    mult matrix

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec2<double> > multVecMatrix(Imath_3_1::Matrix33<double> {lvalue},PyImath::FixedArray<Imath_3_1::Vec2<double> >)

multVecMatrix( (M33d)arg1, (V2f)arg2, (V2f)arg3) -> None :
    mult matrix

    C++ signature :
        void multVecMatrix(Imath_3_1::Matrix33<double> {lvalue},Imath_3_1::Vec2<float>,Imath_3_1::Vec2<float> {lvalue})

multVecMatrix( (M33d)arg1, (V2f)arg2) -> V2f :
    mult matrix

    C++ signature :
        Imath_3_1::Vec2<float> multVecMatrix(Imath_3_1::Matrix33<double> {lvalue},Imath_3_1::Vec2<float>)

multVecMatrix( (M33d)arg1, (V2fArray)arg2) -> V2fArray :
    mult matrix

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec2<float> > multVecMatrix(Imath_3_1::Matrix33<double> {lvalue},PyImath::FixedArray<Imath_3_1::Vec2<float> >)'''
    ...
    def negate (self, *args, **kwargs):
      '''
negate( (M33d)arg1) -> M33d :
    negate() negate all entries in this matrix

    C++ signature :
        Imath_3_1::Matrix33<double> negate(Imath_3_1::Matrix33<double> {lvalue})'''
    ...
    def outerProduct (self, *args, **kwargs):
      '''
outerProduct( (M33d)arg1, (V3d)arg2, (V3d)arg3) -> None :
    M.outerProduct(Va,Vb) -- Performs the outer product, or tensor product, of two 3D vectors, Va and Vb

    C++ signature :
        void outerProduct(Imath_3_1::Matrix33<double> {lvalue},Imath_3_1::Vec3<double>,Imath_3_1::Vec3<double>)'''
    ...
    def removeScaling (self, *args, **kwargs):
      '''
removeScaling( (M33d)arg1 [, (int)arg2]) -> int :
    remove scaling

    C++ signature :
        int removeScaling(Imath_3_1::Matrix33<double> {lvalue} [,int])'''
    ...
    def removeScalingAndShear (self, *args, **kwargs):
      '''
removeScalingAndShear( (M33d)arg1 [, (int)arg2]) -> int :
    remove scaling

    C++ signature :
        int removeScalingAndShear(Imath_3_1::Matrix33<double> {lvalue} [,int])'''
    ...
    def rotate (self, *args, **kwargs):
      '''
rotate( (M33d)arg1, (float)arg2) -> M33d :
    rotate matrix

    C++ signature :
        Imath_3_1::Matrix33<double> rotate(Imath_3_1::Matrix33<double> {lvalue},double)'''
    ...
    def sansScaling (self, *args, **kwargs):
      '''
sansScaling( (M33d)arg1 [, (bool)arg2]) -> M33d :
    sans scaling

    C++ signature :
        Imath_3_1::Matrix33<double> sansScaling(Imath_3_1::Matrix33<double> [,bool])'''
    ...
    def sansScalingAndShear (self, *args, **kwargs):
      '''
sansScalingAndShear( (M33d)arg1 [, (bool)arg2]) -> M33d :
    sans scaling and shear

    C++ signature :
        Imath_3_1::Matrix33<double> sansScalingAndShear(Imath_3_1::Matrix33<double> [,bool])'''
    ...
    def scale (self, *args, **kwargs):
      '''
scale( (M33d)arg1, (float)arg2) -> M33d :
    scale matrix

    C++ signature :
        Imath_3_1::Matrix33<double> scale(Imath_3_1::Matrix33<double> {lvalue},double)

scale( (M33d)arg1, (V2d)arg2) -> M33d :
    scale matrix

    C++ signature :
        Imath_3_1::Matrix33<double> scale(Imath_3_1::Matrix33<double> {lvalue},Imath_3_1::Vec2<double>)

scale( (M33d)arg1, (tuple)arg2) -> M33d :
    scale matrix

    C++ signature :
        Imath_3_1::Matrix33<double> scale(Imath_3_1::Matrix33<double> {lvalue},boost::python::tuple)'''
    ...
    def setRotation (self, *args, **kwargs):
      '''
setRotation( (M33d)arg1, (float)arg2) -> M33d :
    setRotation()

    C++ signature :
        Imath_3_1::Matrix33<double> setRotation(Imath_3_1::Matrix33<double> {lvalue},double)'''
    ...
    def setScale (self, *args, **kwargs):
      '''
setScale( (M33d)arg1, (float)arg2) -> M33d :
    setScale()

    C++ signature :
        Imath_3_1::Matrix33<double> setScale(Imath_3_1::Matrix33<double> {lvalue},double)

setScale( (M33d)arg1, (V2d)arg2) -> M33d :
    setScale()

    C++ signature :
        Imath_3_1::Matrix33<double> setScale(Imath_3_1::Matrix33<double> {lvalue},Imath_3_1::Vec2<double>)

setScale( (M33d)arg1, (tuple)arg2) -> M33d :
    setScale()

    C++ signature :
        Imath_3_1::Matrix33<double> setScale(Imath_3_1::Matrix33<double> {lvalue},boost::python::tuple)'''
    ...
    def setShear (self, *args, **kwargs):
      '''
setShear( (M33d)arg1, (float)arg2) -> M33d :
    setShear()

    C++ signature :
        Imath_3_1::Matrix33<double> setShear(Imath_3_1::Matrix33<double> {lvalue},double)

setShear( (M33d)arg1, (V2d)arg2) -> M33d :
    setShear()

    C++ signature :
        Imath_3_1::Matrix33<double> setShear(Imath_3_1::Matrix33<double> {lvalue},Imath_3_1::Vec2<double>)

setShear( (M33d)arg1, (tuple)arg2) -> M33d :
    setShear()

    C++ signature :
        Imath_3_1::Matrix33<double> setShear(Imath_3_1::Matrix33<double> {lvalue},boost::python::tuple)'''
    ...
    def setTranslation (self, *args, **kwargs):
      '''
setTranslation( (M33d)arg1, (V2d)arg2) -> M33d :
    setTranslation()

    C++ signature :
        Imath_3_1::Matrix33<double> setTranslation(Imath_3_1::Matrix33<double> {lvalue},Imath_3_1::Vec2<double>)

setTranslation( (M33d)arg1, (tuple)arg2) -> M33d :
    setTranslation()

    C++ signature :
        Imath_3_1::Matrix33<double> setTranslation(Imath_3_1::Matrix33<double> {lvalue},boost::python::tuple)

setTranslation( (M33d)arg1, (object)arg2) -> M33d :
    setTranslation()

    C++ signature :
        Imath_3_1::Matrix33<double> setTranslation(Imath_3_1::Matrix33<double> {lvalue},boost::python::api::object)'''
    ...
    def setValue (self, *args, **kwargs):
      '''
setValue( (M33d)arg1, (M33d)arg2) -> None :
    setValue()

    C++ signature :
        void setValue(Imath_3_1::Matrix33<double> {lvalue},Imath_3_1::Matrix33<double>)'''
    ...
    def shear (self, *args, **kwargs):
      '''
shear( (M33d)arg1, (float)arg2) -> M33d :
    shear()

    C++ signature :
        Imath_3_1::Matrix33<double> shear(Imath_3_1::Matrix33<double> {lvalue},double)

shear( (M33d)arg1, (V2d)arg2) -> M33d :
    shear()

    C++ signature :
        Imath_3_1::Matrix33<double> shear(Imath_3_1::Matrix33<double> {lvalue},Imath_3_1::Vec2<double>)

shear( (M33d)arg1, (tuple)arg2) -> M33d :
    shear()

    C++ signature :
        Imath_3_1::Matrix33<double> shear(Imath_3_1::Matrix33<double> {lvalue},boost::python::tuple)'''
    ...
    def singularValueDecomposition (self, *args, **kwargs):
      '''
singularValueDecomposition( (M33d)matrix, (bool)forcePositiveDeterminant) -> tuple :
    Decomposes the matrix using the singular value decomposition (SVD) into three
    matrices U, S, and V which have the following properties: 
      1. U and V are both orthonormal matrices, 
      2. S is the diagonal matrix of singular values, 
      3. U * S * V.transposed() gives back the original matrix.
    The result is returned as a tuple [U, S, V].  Note that since S is diagonal we
    don't need to return the entire matrix, so we return it as a three-vector.  
    
    The 'forcePositiveDeterminant' argument can be used to force the U and V^T to
    have positive determinant (that is, to be proper rotation matrices); if
    forcePositiveDeterminant is False, then the singular values are guaranteed to
    be nonnegative but the U and V matrices might contain negative scale along one
    of the axes; if forcePositiveDeterminant is True, then U and V cannot contain
    negative scale but S[2] might be negative.  
    
    Our SVD implementation uses two-sided Jacobi rotations to iteratively
    diagonalize the matrix, which should be quite robust and significantly faster
    than the more general SVD solver in LAPACK.  
    

    C++ signature :
        boost::python::tuple singularValueDecomposition(Imath_3_1::Matrix33<double>,bool)'''
    ...
    def symmetricEigensolve (self, *args, **kwargs):
      '''
symmetricEigensolve( (M33d)arg1) -> tuple :
    Decomposes the matrix A using a symmetric eigensolver into matrices Q and S 
    which have the following properties: 
      1. Q is the orthonormal matrix of eigenvectors, 
      2. S is the diagonal matrix of eigenvalues, 
      3. Q * S * Q.transposed() gives back the original matrix.
    
    IMPORTANT: It is vital that the passed-in matrix be symmetric, or the result 
    won't make any sense.  This function will return an error if passed an 
    unsymmetric matrix.
    
    The result is returned as a tuple [Q, S].  Note that since S is diagonal 
    we don't need to return the entire matrix, so we return it as a three-vector. 
    
    Our eigensolver implementation uses one-sided Jacobi rotations to iteratively 
    diagonalize the matrix, which should be quite robust and significantly faster 
    than the more general symmetric eigenvalue solver in LAPACK.  
    

    C++ signature :
        boost::python::tuple symmetricEigensolve(Imath_3_1::Matrix33<double>)'''
    ...
    def translate (self, *args, **kwargs):
      '''
translate( (M33d)arg1, (object)arg2) -> M33d :
    translate()

    C++ signature :
        Imath_3_1::Matrix33<double> translate(Imath_3_1::Matrix33<double> {lvalue},boost::python::api::object)

translate( (M33d)arg1, (tuple)arg2) -> M33d :
    translate()

    C++ signature :
        Imath_3_1::Matrix33<double> translate(Imath_3_1::Matrix33<double> {lvalue},boost::python::tuple)'''
    ...
    def translation (self, *args, **kwargs):
      '''
translation( (M33d)arg1) -> V2d :
    translation()

    C++ signature :
        Imath_3_1::Vec2<double> translation(Imath_3_1::Matrix33<double> {lvalue})'''
    ...
    def transpose (self, *args, **kwargs):
      '''
transpose( (M33d)arg1) -> M33d :
    transpose() transpose this matrix

    C++ signature :
        Imath_3_1::Matrix33<double> transpose(Imath_3_1::Matrix33<double> {lvalue})'''
    ...
    def transposed (self, *args, **kwargs):
      '''
transposed( (M33d)arg1) -> M33d :
    transposed() return a transposed copy of this matrix

    C++ signature :
        Imath_3_1::Matrix33<double> transposed(Imath_3_1::Matrix33<double> {lvalue})'''
    ...

def M33dArray (*args):
      '''
__init__(_object*, PyImath::FixedArray<Imath_3_1::Matrix33<double> >)
__init__(boost::python::api::object, PyImath::FixedArray<double>, PyImath::FixedArray<double>, PyImath::FixedArray<double>, PyImath::FixedArray<double>, PyImath::FixedArray<double>, PyImath::FixedArray<double>, PyImath::FixedArray<double>, PyImath::FixedArray<double>, PyImath::FixedArray<double>)
__init__(_object*, Imath_3_1::Matrix33<double>, unsigned long)
__init__(_object*, PyImath::FixedArray<Imath_3_1::Matrix33<double> >)
__init__(_object*, unsigned long)

'''      
    ...

class M33dArray:
    def ifelse (self, *args, **kwargs):
      '''
ifelse( (M33dArray)arg1, (IntArray)arg2, (M33d)arg3) -> M33dArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Matrix33<double> > ifelse(PyImath::FixedArray<Imath_3_1::Matrix33<double> > {lvalue},PyImath::FixedArray<int>,Imath_3_1::Matrix33<double>)

ifelse( (M33dArray)arg1, (IntArray)arg2, (M33dArray)arg3) -> M33dArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Matrix33<double> > ifelse(PyImath::FixedArray<Imath_3_1::Matrix33<double> > {lvalue},PyImath::FixedArray<int>,PyImath::FixedArray<Imath_3_1::Matrix33<double> >)'''
    ...
    def inverse (self, *args, **kwargs):
      '''
inverse( (M33dArray)vector) -> M33dArray :
    Return M^-1 for each element M.

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Matrix33<double> > inverse(PyImath::FixedArray<Imath_3_1::Matrix33<double> >)'''
    ...
    def makeReadOnly (self, *args, **kwargs):
      '''
makeReadOnly( (M33dArray)arg1) -> None :

    C++ signature :
        void makeReadOnly(PyImath::FixedArray<Imath_3_1::Matrix33<double> > {lvalue})'''
    ...
    def writable (self, *args, **kwargs):
      '''
writable( (M33dArray)arg1) -> bool :

    C++ signature :
        bool writable(PyImath::FixedArray<Imath_3_1::Matrix33<double> > {lvalue})'''
    ...

def M33dRow (*args):
      '''

'''      
    ...

class M33dRow:

def M33f (*args):
      '''
__init__(boost::python::api::object, Imath_3_1::Matrix33<double>)
__init__(boost::python::api::object, Imath_3_1::Matrix33<float>)
__init__(boost::python::api::object, boost::python::tuple, boost::python::tuple, boost::python::tuple)
__init__(_object*, float, float, float, float, float, float, float, float, float)
__init__(_object*, float)
__init__(_object*)
__init__(_object*, Imath_3_1::Matrix33<float>)

'''      
    ...

class M33f:
    def baseTypeEpsilon (self, *args, **kwargs):
      '''
baseTypeEpsilon() -> float :
    baseTypeEpsilon() epsilon value of the base type of the vector

    C++ signature :
        float baseTypeEpsilon()'''
    ...
    def baseTypeLowest (self, *args, **kwargs):
      '''
baseTypeLowest() -> float :
    baseTypeLowest() largest negative value of the base type of the vector

    C++ signature :
        float baseTypeLowest()'''
    ...
    def baseTypeMax (self, *args, **kwargs):
      '''
baseTypeMax() -> float :
    baseTypeMax() max value of the base type of the vector

    C++ signature :
        float baseTypeMax()'''
    ...
    def baseTypeSmallest (self, *args, **kwargs):
      '''
baseTypeSmallest() -> float :
    baseTypeSmallest() smallest value of the base type of the vector

    C++ signature :
        float baseTypeSmallest()'''
    ...
    def determinant (self, *args, **kwargs):
      '''
determinant( (M33f)arg1) -> float :
    determinant() return the determinant of this matrix

    C++ signature :
        float determinant(Imath_3_1::Matrix33<float> {lvalue})'''
    ...
    def equalWithAbsError (self, *args, **kwargs):
      '''
equalWithAbsError( (M33f)arg1, (M33f)arg2, (float)arg3) -> bool :
    m1.equalWithAbsError(m2,e) true if the elements of v1 and v2 are the same with an absolute error of no more than e, i.e., abs(m1[i] - m2[i]) <= e

    C++ signature :
        bool equalWithAbsError(Imath_3_1::Matrix33<float> {lvalue},Imath_3_1::Matrix33<float>,float)'''
    ...
    def equalWithRelError (self, *args, **kwargs):
      '''
equalWithRelError( (M33f)arg1, (M33f)arg2, (float)arg3) -> bool :
    m1.equalWithAbsError(m2,e) true if the elements of m1 and m2 are the same with an absolute error of no more than e, i.e., abs(m1[i] - m2[i]) <= e * abs(m1[i])

    C++ signature :
        bool equalWithRelError(Imath_3_1::Matrix33<float> {lvalue},Imath_3_1::Matrix33<float>,float)'''
    ...
    def extractAndRemoveScalingAndShear (self, *args, **kwargs):
      '''
extractAndRemoveScalingAndShear( (M33f)arg1, (V2f)arg2, (V2f)arg3 [, (int)arg4]) -> None :
    M.extractAndRemoveScalingAndShear(scl, shr, [exc]) -- extracts the scaling component of M into scl and the shearing component of M into shr.  Also removes the scaling and shearing components from M.  Returns 1 unless the scaling component is nearly 0, in which case 0 is returned. If optional arg. exc == 1, then if the scaling component is nearly 0, then MathExc is thrown. 

    C++ signature :
        void extractAndRemoveScalingAndShear(Imath_3_1::Matrix33<float> {lvalue},Imath_3_1::Vec2<float> {lvalue},Imath_3_1::Vec2<float> {lvalue} [,int])'''
    ...
    def extractEuler (self, *args, **kwargs):
      '''
extractEuler( (M33f)arg1, (V2f)arg2) -> None :
    M.extractEulerZYX(r) -- extracts the rotation component of M into r. Assumes that M contains no shear or non-uniform scaling; results are meaningless if it does.

    C++ signature :
        void extractEuler(Imath_3_1::Matrix33<float> {lvalue},Imath_3_1::Vec2<float> {lvalue})'''
    ...
    def extractSHRT (self, *args, **kwargs):
      '''
extractSHRT( (M33f)arg1, (V2f)arg2, (V2f)arg3, (V2f)arg4, (V2f)arg5 [, (int)arg6]) -> int :
    M.extractSHRT(Vs, Vh, Vr, Vt, [exc]) -- extracts the scaling component of M into Vs, the shearing component of M in Vh (as XY, XZ, YZ shear factors), the rotation of M into Vr (as Euler angles in the order XYZ), and the translaation of M into Vt. If optional arg. exc == 1, then if the scaling component is nearly 0, then MathExc is thrown. 

    C++ signature :
        int extractSHRT(Imath_3_1::Matrix33<float> {lvalue},Imath_3_1::Vec2<float> {lvalue},Imath_3_1::Vec2<float> {lvalue},Imath_3_1::Vec2<float> {lvalue},Imath_3_1::Vec2<float> {lvalue} [,int])'''
    ...
    def extractScaling (self, *args, **kwargs):
      '''
extractScaling( (M33f)arg1, (V2f)arg2 [, (int)arg3]) -> None :
    extract scaling

    C++ signature :
        void extractScaling(Imath_3_1::Matrix33<float> {lvalue},Imath_3_1::Vec2<float> {lvalue} [,int])'''
    ...
    def extractScalingAndShear (self, *args, **kwargs):
      '''
extractScalingAndShear( (M33f)arg1, (V2f)arg2, (V2f)arg3 [, (int)arg4]) -> None :
    extract scaling

    C++ signature :
        void extractScalingAndShear(Imath_3_1::Matrix33<float> {lvalue},Imath_3_1::Vec2<float> {lvalue},Imath_3_1::Vec2<float> {lvalue} [,int])'''
    ...
    def fastMinor (self, *args, **kwargs):
      '''
fastMinor( (M33f)arg1, (int)arg2, (int)arg3, (int)arg4, (int)arg5) -> float :
    fastMinor() return the matrix minor using the specified rows and columns of this matrix

    C++ signature :
        float fastMinor(Imath_3_1::Matrix33<float> {lvalue},int,int,int,int)'''
    ...
    def gjInverse (self, *args, **kwargs):
      '''
gjInverse( (M33f)arg1 [, (bool)arg2]) -> M33f :
    gjInverse() return an inverted copy of this matrix

    C++ signature :
        Imath_3_1::Matrix33<float> gjInverse(Imath_3_1::Matrix33<float> {lvalue} [,bool])'''
    ...
    def gjInvert (self, *args, **kwargs):
      '''
gjInvert( (M33f)arg1 [, (bool)arg2]) -> M33f :
    gjInvert() invert this matrix

    C++ signature :
        Imath_3_1::Matrix33<float> gjInvert(Imath_3_1::Matrix33<float> {lvalue} [,bool])'''
    ...
    def inverse (self, *args, **kwargs):
      '''
inverse( (M33f)arg1 [, (bool)arg2]) -> M33f :
    inverse() return an inverted copy of this matrix

    C++ signature :
        Imath_3_1::Matrix33<float> inverse(Imath_3_1::Matrix33<float> {lvalue} [,bool])'''
    ...
    def invert (self, *args, **kwargs):
      '''
invert( (M33f)arg1 [, (bool)arg2]) -> M33f :
    invert() invert this matrix

    C++ signature :
        Imath_3_1::Matrix33<float> invert(Imath_3_1::Matrix33<float> {lvalue} [,bool])'''
    ...
    def makeIdentity (self, *args, **kwargs):
      '''
makeIdentity( (M33f)arg1) -> None :
    makeIdentity() make this matrix the identity matrix

    C++ signature :
        void makeIdentity(Imath_3_1::Matrix33<float> {lvalue})'''
    ...
    def minorOf (self, *args, **kwargs):
      '''
minorOf( (M33f)arg1, (int)arg2, (int)arg3) -> float :
    minorOf() return the matrix minor of the (row,col) element of this matrix

    C++ signature :
        float minorOf(Imath_3_1::Matrix33<float> {lvalue},int,int)'''
    ...
    def multDirMatrix (self, *args, **kwargs):
      '''
multDirMatrix( (M33f)arg1, (V2d)arg2, (V2d)arg3) -> None :
    mult matrix

    C++ signature :
        void multDirMatrix(Imath_3_1::Matrix33<float> {lvalue},Imath_3_1::Vec2<double>,Imath_3_1::Vec2<double> {lvalue})

multDirMatrix( (M33f)arg1, (V2d)arg2) -> V2d :
    mult matrix

    C++ signature :
        Imath_3_1::Vec2<double> multDirMatrix(Imath_3_1::Matrix33<float> {lvalue},Imath_3_1::Vec2<double>)

multDirMatrix( (M33f)arg1, (V2dArray)arg2) -> V2dArray :
    mult matrix

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec2<double> > multDirMatrix(Imath_3_1::Matrix33<float> {lvalue},PyImath::FixedArray<Imath_3_1::Vec2<double> >)

multDirMatrix( (M33f)arg1, (V2f)arg2, (V2f)arg3) -> None :
    mult matrix

    C++ signature :
        void multDirMatrix(Imath_3_1::Matrix33<float> {lvalue},Imath_3_1::Vec2<float>,Imath_3_1::Vec2<float> {lvalue})

multDirMatrix( (M33f)arg1, (V2f)arg2) -> V2f :
    mult matrix

    C++ signature :
        Imath_3_1::Vec2<float> multDirMatrix(Imath_3_1::Matrix33<float> {lvalue},Imath_3_1::Vec2<float>)

multDirMatrix( (M33f)arg1, (V2fArray)arg2) -> V2fArray :
    mult matrix

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec2<float> > multDirMatrix(Imath_3_1::Matrix33<float> {lvalue},PyImath::FixedArray<Imath_3_1::Vec2<float> >)'''
    ...
    def multVecMatrix (self, *args, **kwargs):
      '''
multVecMatrix( (M33f)arg1, (V2d)arg2, (V2d)arg3) -> None :
    mult matrix

    C++ signature :
        void multVecMatrix(Imath_3_1::Matrix33<float> {lvalue},Imath_3_1::Vec2<double>,Imath_3_1::Vec2<double> {lvalue})

multVecMatrix( (M33f)arg1, (V2d)arg2) -> V2d :
    mult matrix

    C++ signature :
        Imath_3_1::Vec2<double> multVecMatrix(Imath_3_1::Matrix33<float> {lvalue},Imath_3_1::Vec2<double>)

multVecMatrix( (M33f)arg1, (V2dArray)arg2) -> V2dArray :
    mult matrix

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec2<double> > multVecMatrix(Imath_3_1::Matrix33<float> {lvalue},PyImath::FixedArray<Imath_3_1::Vec2<double> >)

multVecMatrix( (M33f)arg1, (V2f)arg2, (V2f)arg3) -> None :
    mult matrix

    C++ signature :
        void multVecMatrix(Imath_3_1::Matrix33<float> {lvalue},Imath_3_1::Vec2<float>,Imath_3_1::Vec2<float> {lvalue})

multVecMatrix( (M33f)arg1, (V2f)arg2) -> V2f :
    mult matrix

    C++ signature :
        Imath_3_1::Vec2<float> multVecMatrix(Imath_3_1::Matrix33<float> {lvalue},Imath_3_1::Vec2<float>)

multVecMatrix( (M33f)arg1, (V2fArray)arg2) -> V2fArray :
    mult matrix

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec2<float> > multVecMatrix(Imath_3_1::Matrix33<float> {lvalue},PyImath::FixedArray<Imath_3_1::Vec2<float> >)'''
    ...
    def negate (self, *args, **kwargs):
      '''
negate( (M33f)arg1) -> M33f :
    negate() negate all entries in this matrix

    C++ signature :
        Imath_3_1::Matrix33<float> negate(Imath_3_1::Matrix33<float> {lvalue})'''
    ...
    def outerProduct (self, *args, **kwargs):
      '''
outerProduct( (M33f)arg1, (V3f)arg2, (V3f)arg3) -> None :
    M.outerProduct(Va,Vb) -- Performs the outer product, or tensor product, of two 3D vectors, Va and Vb

    C++ signature :
        void outerProduct(Imath_3_1::Matrix33<float> {lvalue},Imath_3_1::Vec3<float>,Imath_3_1::Vec3<float>)'''
    ...
    def removeScaling (self, *args, **kwargs):
      '''
removeScaling( (M33f)arg1 [, (int)arg2]) -> int :
    remove scaling

    C++ signature :
        int removeScaling(Imath_3_1::Matrix33<float> {lvalue} [,int])'''
    ...
    def removeScalingAndShear (self, *args, **kwargs):
      '''
removeScalingAndShear( (M33f)arg1 [, (int)arg2]) -> int :
    remove scaling

    C++ signature :
        int removeScalingAndShear(Imath_3_1::Matrix33<float> {lvalue} [,int])'''
    ...
    def rotate (self, *args, **kwargs):
      '''
rotate( (M33f)arg1, (float)arg2) -> M33f :
    rotate matrix

    C++ signature :
        Imath_3_1::Matrix33<float> rotate(Imath_3_1::Matrix33<float> {lvalue},float)'''
    ...
    def sansScaling (self, *args, **kwargs):
      '''
sansScaling( (M33f)arg1 [, (bool)arg2]) -> M33f :
    sans scaling

    C++ signature :
        Imath_3_1::Matrix33<float> sansScaling(Imath_3_1::Matrix33<float> [,bool])'''
    ...
    def sansScalingAndShear (self, *args, **kwargs):
      '''
sansScalingAndShear( (M33f)arg1 [, (bool)arg2]) -> M33f :
    sans scaling and shear

    C++ signature :
        Imath_3_1::Matrix33<float> sansScalingAndShear(Imath_3_1::Matrix33<float> [,bool])'''
    ...
    def scale (self, *args, **kwargs):
      '''
scale( (M33f)arg1, (float)arg2) -> M33f :
    scale matrix

    C++ signature :
        Imath_3_1::Matrix33<float> scale(Imath_3_1::Matrix33<float> {lvalue},float)

scale( (M33f)arg1, (V2f)arg2) -> M33f :
    scale matrix

    C++ signature :
        Imath_3_1::Matrix33<float> scale(Imath_3_1::Matrix33<float> {lvalue},Imath_3_1::Vec2<float>)

scale( (M33f)arg1, (tuple)arg2) -> M33f :
    scale matrix

    C++ signature :
        Imath_3_1::Matrix33<float> scale(Imath_3_1::Matrix33<float> {lvalue},boost::python::tuple)'''
    ...
    def setRotation (self, *args, **kwargs):
      '''
setRotation( (M33f)arg1, (float)arg2) -> M33f :
    setRotation()

    C++ signature :
        Imath_3_1::Matrix33<float> setRotation(Imath_3_1::Matrix33<float> {lvalue},float)'''
    ...
    def setScale (self, *args, **kwargs):
      '''
setScale( (M33f)arg1, (float)arg2) -> M33f :
    setScale()

    C++ signature :
        Imath_3_1::Matrix33<float> setScale(Imath_3_1::Matrix33<float> {lvalue},float)

setScale( (M33f)arg1, (V2f)arg2) -> M33f :
    setScale()

    C++ signature :
        Imath_3_1::Matrix33<float> setScale(Imath_3_1::Matrix33<float> {lvalue},Imath_3_1::Vec2<float>)

setScale( (M33f)arg1, (tuple)arg2) -> M33f :
    setScale()

    C++ signature :
        Imath_3_1::Matrix33<float> setScale(Imath_3_1::Matrix33<float> {lvalue},boost::python::tuple)'''
    ...
    def setShear (self, *args, **kwargs):
      '''
setShear( (M33f)arg1, (float)arg2) -> M33f :
    setShear()

    C++ signature :
        Imath_3_1::Matrix33<float> setShear(Imath_3_1::Matrix33<float> {lvalue},float)

setShear( (M33f)arg1, (V2f)arg2) -> M33f :
    setShear()

    C++ signature :
        Imath_3_1::Matrix33<float> setShear(Imath_3_1::Matrix33<float> {lvalue},Imath_3_1::Vec2<float>)

setShear( (M33f)arg1, (tuple)arg2) -> M33f :
    setShear()

    C++ signature :
        Imath_3_1::Matrix33<float> setShear(Imath_3_1::Matrix33<float> {lvalue},boost::python::tuple)'''
    ...
    def setTranslation (self, *args, **kwargs):
      '''
setTranslation( (M33f)arg1, (V2f)arg2) -> M33f :
    setTranslation()

    C++ signature :
        Imath_3_1::Matrix33<float> setTranslation(Imath_3_1::Matrix33<float> {lvalue},Imath_3_1::Vec2<float>)

setTranslation( (M33f)arg1, (tuple)arg2) -> M33f :
    setTranslation()

    C++ signature :
        Imath_3_1::Matrix33<float> setTranslation(Imath_3_1::Matrix33<float> {lvalue},boost::python::tuple)

setTranslation( (M33f)arg1, (object)arg2) -> M33f :
    setTranslation()

    C++ signature :
        Imath_3_1::Matrix33<float> setTranslation(Imath_3_1::Matrix33<float> {lvalue},boost::python::api::object)'''
    ...
    def setValue (self, *args, **kwargs):
      '''
setValue( (M33f)arg1, (M33f)arg2) -> None :
    setValue()

    C++ signature :
        void setValue(Imath_3_1::Matrix33<float> {lvalue},Imath_3_1::Matrix33<float>)'''
    ...
    def shear (self, *args, **kwargs):
      '''
shear( (M33f)arg1, (float)arg2) -> M33f :
    shear()

    C++ signature :
        Imath_3_1::Matrix33<float> shear(Imath_3_1::Matrix33<float> {lvalue},float)

shear( (M33f)arg1, (V2f)arg2) -> M33f :
    shear()

    C++ signature :
        Imath_3_1::Matrix33<float> shear(Imath_3_1::Matrix33<float> {lvalue},Imath_3_1::Vec2<float>)

shear( (M33f)arg1, (tuple)arg2) -> M33f :
    shear()

    C++ signature :
        Imath_3_1::Matrix33<float> shear(Imath_3_1::Matrix33<float> {lvalue},boost::python::tuple)'''
    ...
    def singularValueDecomposition (self, *args, **kwargs):
      '''
singularValueDecomposition( (M33f)matrix, (bool)forcePositiveDeterminant) -> tuple :
    Decomposes the matrix using the singular value decomposition (SVD) into three
    matrices U, S, and V which have the following properties: 
      1. U and V are both orthonormal matrices, 
      2. S is the diagonal matrix of singular values, 
      3. U * S * V.transposed() gives back the original matrix.
    The result is returned as a tuple [U, S, V].  Note that since S is diagonal we
    don't need to return the entire matrix, so we return it as a three-vector.  
    
    The 'forcePositiveDeterminant' argument can be used to force the U and V^T to
    have positive determinant (that is, to be proper rotation matrices); if
    forcePositiveDeterminant is False, then the singular values are guaranteed to
    be nonnegative but the U and V matrices might contain negative scale along one
    of the axes; if forcePositiveDeterminant is True, then U and V cannot contain
    negative scale but S[2] might be negative.  
    
    Our SVD implementation uses two-sided Jacobi rotations to iteratively
    diagonalize the matrix, which should be quite robust and significantly faster
    than the more general SVD solver in LAPACK.  
    

    C++ signature :
        boost::python::tuple singularValueDecomposition(Imath_3_1::Matrix33<float>,bool)'''
    ...
    def symmetricEigensolve (self, *args, **kwargs):
      '''
symmetricEigensolve( (M33f)arg1) -> tuple :
    Decomposes the matrix A using a symmetric eigensolver into matrices Q and S 
    which have the following properties: 
      1. Q is the orthonormal matrix of eigenvectors, 
      2. S is the diagonal matrix of eigenvalues, 
      3. Q * S * Q.transposed() gives back the original matrix.
    
    IMPORTANT: It is vital that the passed-in matrix be symmetric, or the result 
    won't make any sense.  This function will return an error if passed an 
    unsymmetric matrix.
    
    The result is returned as a tuple [Q, S].  Note that since S is diagonal 
    we don't need to return the entire matrix, so we return it as a three-vector. 
    
    Our eigensolver implementation uses one-sided Jacobi rotations to iteratively 
    diagonalize the matrix, which should be quite robust and significantly faster 
    than the more general symmetric eigenvalue solver in LAPACK.  
    

    C++ signature :
        boost::python::tuple symmetricEigensolve(Imath_3_1::Matrix33<float>)'''
    ...
    def translate (self, *args, **kwargs):
      '''
translate( (M33f)arg1, (object)arg2) -> M33f :
    translate()

    C++ signature :
        Imath_3_1::Matrix33<float> translate(Imath_3_1::Matrix33<float> {lvalue},boost::python::api::object)

translate( (M33f)arg1, (tuple)arg2) -> M33f :
    translate()

    C++ signature :
        Imath_3_1::Matrix33<float> translate(Imath_3_1::Matrix33<float> {lvalue},boost::python::tuple)'''
    ...
    def translation (self, *args, **kwargs):
      '''
translation( (M33f)arg1) -> V2f :
    translation()

    C++ signature :
        Imath_3_1::Vec2<float> translation(Imath_3_1::Matrix33<float> {lvalue})'''
    ...
    def transpose (self, *args, **kwargs):
      '''
transpose( (M33f)arg1) -> M33f :
    transpose() transpose this matrix

    C++ signature :
        Imath_3_1::Matrix33<float> transpose(Imath_3_1::Matrix33<float> {lvalue})'''
    ...
    def transposed (self, *args, **kwargs):
      '''
transposed( (M33f)arg1) -> M33f :
    transposed() return a transposed copy of this matrix

    C++ signature :
        Imath_3_1::Matrix33<float> transposed(Imath_3_1::Matrix33<float> {lvalue})'''
    ...

def M33fArray (*args):
      '''
__init__(_object*, PyImath::FixedArray<Imath_3_1::Matrix33<float> >)
__init__(boost::python::api::object, PyImath::FixedArray<float>, PyImath::FixedArray<float>, PyImath::FixedArray<float>, PyImath::FixedArray<float>, PyImath::FixedArray<float>, PyImath::FixedArray<float>, PyImath::FixedArray<float>, PyImath::FixedArray<float>, PyImath::FixedArray<float>)
__init__(_object*, Imath_3_1::Matrix33<float>, unsigned long)
__init__(_object*, PyImath::FixedArray<Imath_3_1::Matrix33<float> >)
__init__(_object*, unsigned long)

'''      
    ...

class M33fArray:
    def ifelse (self, *args, **kwargs):
      '''
ifelse( (M33fArray)arg1, (IntArray)arg2, (M33f)arg3) -> M33fArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Matrix33<float> > ifelse(PyImath::FixedArray<Imath_3_1::Matrix33<float> > {lvalue},PyImath::FixedArray<int>,Imath_3_1::Matrix33<float>)

ifelse( (M33fArray)arg1, (IntArray)arg2, (M33fArray)arg3) -> M33fArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Matrix33<float> > ifelse(PyImath::FixedArray<Imath_3_1::Matrix33<float> > {lvalue},PyImath::FixedArray<int>,PyImath::FixedArray<Imath_3_1::Matrix33<float> >)'''
    ...
    def inverse (self, *args, **kwargs):
      '''
inverse( (M33fArray)vector) -> M33fArray :
    Return M^-1 for each element M.

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Matrix33<float> > inverse(PyImath::FixedArray<Imath_3_1::Matrix33<float> >)'''
    ...
    def makeReadOnly (self, *args, **kwargs):
      '''
makeReadOnly( (M33fArray)arg1) -> None :

    C++ signature :
        void makeReadOnly(PyImath::FixedArray<Imath_3_1::Matrix33<float> > {lvalue})'''
    ...
    def writable (self, *args, **kwargs):
      '''
writable( (M33fArray)arg1) -> bool :

    C++ signature :
        bool writable(PyImath::FixedArray<Imath_3_1::Matrix33<float> > {lvalue})'''
    ...

def M33fRow (*args):
      '''

'''      
    ...

class M33fRow:

def M44d (*args):
      '''
__init__(_object*, double, double, double, double, double, double, double, double, double, double, double, double, double, double, double, double)
__init__(boost::python::api::object, Imath_3_1::Matrix44<double>)
__init__(boost::python::api::object, Imath_3_1::Matrix44<float>)
__init__(boost::python::api::object, boost::python::tuple, boost::python::tuple, boost::python::tuple, boost::python::tuple)
__init__(_object*, double)
__init__(_object*)
__init__(_object*, Imath_3_1::Matrix44<double>)

'''      
    ...

class M44d:
    def baseTypeEpsilon (self, *args, **kwargs):
      '''
baseTypeEpsilon() -> float :
    baseTypeEpsilon() epsilon value of the base type of the vector

    C++ signature :
        double baseTypeEpsilon()'''
    ...
    def baseTypeLowest (self, *args, **kwargs):
      '''
baseTypeLowest() -> float :
    baseTypeLowest() largest negative value of the base type of the vector

    C++ signature :
        double baseTypeLowest()'''
    ...
    def baseTypeMax (self, *args, **kwargs):
      '''
baseTypeMax() -> float :
    baseTypeMax() max value of the base type of the vector

    C++ signature :
        double baseTypeMax()'''
    ...
    def baseTypeSmallest (self, *args, **kwargs):
      '''
baseTypeSmallest() -> float :
    baseTypeSmallest() smallest value of the base type of the vector

    C++ signature :
        double baseTypeSmallest()'''
    ...
    def determinant (self, *args, **kwargs):
      '''
determinant( (M44d)arg1) -> float :
    determinant() return the determinant of this matrix

    C++ signature :
        double determinant(Imath_3_1::Matrix44<double> {lvalue})'''
    ...
    def equalWithAbsError (self, *args, **kwargs):
      '''
equalWithAbsError( (M44d)arg1, (M44d)arg2, (float)arg3) -> bool :
    m1.equalWithAbsError(m2,e) true if the elements of v1 and v2 are the same with an absolute error of no more than e, i.e., abs(m1[i] - m2[i]) <= e

    C++ signature :
        bool equalWithAbsError(Imath_3_1::Matrix44<double> {lvalue},Imath_3_1::Matrix44<double>,double)'''
    ...
    def equalWithRelError (self, *args, **kwargs):
      '''
equalWithRelError( (M44d)arg1, (M44d)arg2, (float)arg3) -> bool :
    m1.equalWithAbsError(m2,e) true if the elements of m1 and m2 are the same with an absolute error of no more than e, i.e., abs(m1[i] - m2[i]) <= e * abs(m1[i])

    C++ signature :
        bool equalWithRelError(Imath_3_1::Matrix44<double> {lvalue},Imath_3_1::Matrix44<double>,double)'''
    ...
    def extractAndRemoveScalingAndShear (self, *args, **kwargs):
      '''
extractAndRemoveScalingAndShear( (M44d)arg1, (V3d)arg2, (V3d)arg3 [, (int)arg4]) -> None :
    M.extractAndRemoveScalingAndShear(scl, shr, [exc]) -- extracts the scaling component of M into scl and the shearing component of M into shr.  Also removes the scaling and shearing components from M.  Returns 1 unless the scaling component is nearly 0, in which case 0 is returned. If optional arg. exc == 1, then if the scaling component is nearly 0, then MathExc is thrown.

    C++ signature :
        void extractAndRemoveScalingAndShear(Imath_3_1::Matrix44<double> {lvalue},Imath_3_1::Vec3<double> {lvalue},Imath_3_1::Vec3<double> {lvalue} [,int])'''
    ...
    def extractEulerXYZ (self, *args, **kwargs):
      '''
extractEulerXYZ( (M44d)arg1, (V3d)arg2) -> None :
    extract Euler

    C++ signature :
        void extractEulerXYZ(Imath_3_1::Matrix44<double> {lvalue},Imath_3_1::Vec3<double> {lvalue})'''
    ...
    def extractEulerZYX (self, *args, **kwargs):
      '''
extractEulerZYX( (M44d)arg1, (V3d)arg2) -> None :
    extract Euler

    C++ signature :
        void extractEulerZYX(Imath_3_1::Matrix44<double> {lvalue},Imath_3_1::Vec3<double> {lvalue})'''
    ...
    def extractSHRT (self, *args, **kwargs):
      '''
extractSHRT( (M44d)arg1, (V3d)arg2, (V3d)arg3, (V3d)arg4, (V3d)arg5 [, (int)arg6]) -> int :
    M.extractSHRT(Vs, Vh, Vr, Vt, [exc]) -- extracts the scaling component of M into Vs, the shearing component of M in Vh (as XY, XZ, YZ shear factors), the rotation of M into Vr (as Euler angles in the order XYZ), and the translaation of M into Vt. If optional arg. exc == 1, then if the scaling component is nearly 0, then MathExc is thrown. 

    C++ signature :
        int extractSHRT(Imath_3_1::Matrix44<double> {lvalue},Imath_3_1::Vec3<double> {lvalue},Imath_3_1::Vec3<double> {lvalue},Imath_3_1::Vec3<double> {lvalue},Imath_3_1::Vec3<double> {lvalue} [,int])'''
    ...
    def extractScaling (self, *args, **kwargs):
      '''
extractScaling( (M44d)arg1, (V3d)arg2 [, (int)arg3]) -> None :
    extract scaling

    C++ signature :
        void extractScaling(Imath_3_1::Matrix44<double> {lvalue},Imath_3_1::Vec3<double> {lvalue} [,int])'''
    ...
    def extractScalingAndShear (self, *args, **kwargs):
      '''
extractScalingAndShear( (M44d)arg1, (V3d)arg2, (V3d)arg3 [, (int)arg4]) -> None :
    extract scaling

    C++ signature :
        void extractScalingAndShear(Imath_3_1::Matrix44<double> {lvalue},Imath_3_1::Vec3<double> {lvalue},Imath_3_1::Vec3<double> {lvalue} [,int])'''
    ...
    def fastMinor (self, *args, **kwargs):
      '''
fastMinor( (M44d)arg1, (int)arg2, (int)arg3, (int)arg4, (int)arg5, (int)arg6, (int)arg7) -> float :
    fastMinor() return matrix minor using the specified rows and columns of this matrix

    C++ signature :
        double fastMinor(Imath_3_1::Matrix44<double> {lvalue},int,int,int,int,int,int)'''
    ...
    def gjInverse (self, *args, **kwargs):
      '''
gjInverse( (M44d)arg1 [, (bool)arg2]) -> M44d :
    gjInverse() return an inverted copy of this matrix

    C++ signature :
        Imath_3_1::Matrix44<double> gjInverse(Imath_3_1::Matrix44<double> {lvalue} [,bool])'''
    ...
    def gjInvert (self, *args, **kwargs):
      '''
gjInvert( (M44d)arg1 [, (bool)arg2]) -> M44d :
    gjInvert() invert this matrix

    C++ signature :
        Imath_3_1::Matrix44<double> gjInvert(Imath_3_1::Matrix44<double> {lvalue} [,bool])'''
    ...
    def inverse (self, *args, **kwargs):
      '''
inverse( (M44d)arg1 [, (bool)arg2]) -> M44d :
    inverse() return an inverted copy of this matrix

    C++ signature :
        Imath_3_1::Matrix44<double> inverse(Imath_3_1::Matrix44<double> {lvalue} [,bool])'''
    ...
    def invert (self, *args, **kwargs):
      '''
invert( (M44d)arg1 [, (bool)arg2]) -> M44d :
    invert() invert this matrix

    C++ signature :
        Imath_3_1::Matrix44<double> invert(Imath_3_1::Matrix44<double> {lvalue} [,bool])'''
    ...
    def makeIdentity (self, *args, **kwargs):
      '''
makeIdentity( (M44d)arg1) -> None :
    makeIdentity() make this matrix the identity matrix

    C++ signature :
        void makeIdentity(Imath_3_1::Matrix44<double> {lvalue})'''
    ...
    def minorOf (self, *args, **kwargs):
      '''
minorOf( (M44d)arg1, (int)arg2, (int)arg3) -> float :
    minorOf() return matrix minor of the (row,col) element of this matrix

    C++ signature :
        double minorOf(Imath_3_1::Matrix44<double> {lvalue},int,int)'''
    ...
    def multDirMatrix (self, *args, **kwargs):
      '''
multDirMatrix( (M44d)arg1, (V3d)arg2, (V3d)arg3) -> None :
    mult matrix

    C++ signature :
        void multDirMatrix(Imath_3_1::Matrix44<double> {lvalue},Imath_3_1::Vec3<double>,Imath_3_1::Vec3<double> {lvalue})

multDirMatrix( (M44d)arg1, (V3d)arg2) -> V3d :
    mult matrix

    C++ signature :
        Imath_3_1::Vec3<double> multDirMatrix(Imath_3_1::Matrix44<double> {lvalue},Imath_3_1::Vec3<double>)

multDirMatrix( (M44d)arg1, (V3dArray)arg2) -> V3dArray :
    mult matrix

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec3<double> > multDirMatrix(Imath_3_1::Matrix44<double> {lvalue},PyImath::FixedArray<Imath_3_1::Vec3<double> >)

multDirMatrix( (M44d)arg1, (V3f)arg2, (V3f)arg3) -> None :
    mult matrix

    C++ signature :
        void multDirMatrix(Imath_3_1::Matrix44<double> {lvalue},Imath_3_1::Vec3<float>,Imath_3_1::Vec3<float> {lvalue})

multDirMatrix( (M44d)arg1, (V3f)arg2) -> V3f :
    mult matrix

    C++ signature :
        Imath_3_1::Vec3<float> multDirMatrix(Imath_3_1::Matrix44<double> {lvalue},Imath_3_1::Vec3<float>)

multDirMatrix( (M44d)arg1, (V3fArray)arg2) -> V3fArray :
    mult matrix

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec3<float> > multDirMatrix(Imath_3_1::Matrix44<double> {lvalue},PyImath::FixedArray<Imath_3_1::Vec3<float> >)'''
    ...
    def multVecMatrix (self, *args, **kwargs):
      '''
multVecMatrix( (M44d)arg1, (V3d)arg2, (V3d)arg3) -> None :
    mult matrix

    C++ signature :
        void multVecMatrix(Imath_3_1::Matrix44<double> {lvalue},Imath_3_1::Vec3<double>,Imath_3_1::Vec3<double> {lvalue})

multVecMatrix( (M44d)arg1, (V3d)arg2) -> V3d :
    mult matrix

    C++ signature :
        Imath_3_1::Vec3<double> multVecMatrix(Imath_3_1::Matrix44<double> {lvalue},Imath_3_1::Vec3<double>)

multVecMatrix( (M44d)arg1, (V3dArray)arg2) -> V3dArray :
    mult matrix

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec3<double> > multVecMatrix(Imath_3_1::Matrix44<double> {lvalue},PyImath::FixedArray<Imath_3_1::Vec3<double> >)

multVecMatrix( (M44d)arg1, (V3f)arg2, (V3f)arg3) -> None :
    mult matrix

    C++ signature :
        void multVecMatrix(Imath_3_1::Matrix44<double> {lvalue},Imath_3_1::Vec3<float>,Imath_3_1::Vec3<float> {lvalue})

multVecMatrix( (M44d)arg1, (V3f)arg2) -> V3f :
    mult matrix

    C++ signature :
        Imath_3_1::Vec3<float> multVecMatrix(Imath_3_1::Matrix44<double> {lvalue},Imath_3_1::Vec3<float>)

multVecMatrix( (M44d)arg1, (V3fArray)arg2) -> V3fArray :
    mult matrix

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec3<float> > multVecMatrix(Imath_3_1::Matrix44<double> {lvalue},PyImath::FixedArray<Imath_3_1::Vec3<float> >)'''
    ...
    def negate (self, *args, **kwargs):
      '''
negate( (M44d)arg1) -> M44d :
    negate() negate all entries in this matrix

    C++ signature :
        Imath_3_1::Matrix44<double> negate(Imath_3_1::Matrix44<double> {lvalue})'''
    ...
    def removeScaling (self, *args, **kwargs):
      '''
removeScaling( (M44d)arg1 [, (int)arg2]) -> int :
    remove scaling

    C++ signature :
        int removeScaling(Imath_3_1::Matrix44<double> {lvalue} [,int])'''
    ...
    def removeScalingAndShear (self, *args, **kwargs):
      '''
removeScalingAndShear( (M44d)arg1 [, (int)arg2]) -> int :
    remove scaling

    C++ signature :
        int removeScalingAndShear(Imath_3_1::Matrix44<double> {lvalue} [,int])'''
    ...
    def rotate (self, *args, **kwargs):
      '''
rotate( (M44d)arg1, (V3d)arg2) -> M44d :
    rotate matrix

    C++ signature :
        Imath_3_1::Matrix44<double> rotate(Imath_3_1::Matrix44<double> {lvalue},Imath_3_1::Vec3<double>)'''
    ...
    def rotationMatrix (self, *args, **kwargs):
      '''
rotationMatrix( (M44d)arg1, (object)arg2, (object)arg3) -> M44d :
    rotationMatrix()

    C++ signature :
        Imath_3_1::Matrix44<double> rotationMatrix(Imath_3_1::Matrix44<double> {lvalue},boost::python::api::object,boost::python::api::object)'''
    ...
    def rotationMatrixWithUpDir (self, *args, **kwargs):
      '''
rotationMatrixWithUpDir( (M44d)arg1, (object)arg2, (object)arg3, (object)arg4) -> M44d :
    roationMatrixWithUp()

    C++ signature :
        Imath_3_1::Matrix44<double> rotationMatrixWithUpDir(Imath_3_1::Matrix44<double> {lvalue},boost::python::api::object,boost::python::api::object,boost::python::api::object)'''
    ...
    def sansScaling (self, *args, **kwargs):
      '''
sansScaling( (M44d)arg1 [, (bool)arg2]) -> M44d :
    sans scaling

    C++ signature :
        Imath_3_1::Matrix44<double> sansScaling(Imath_3_1::Matrix44<double> [,bool])'''
    ...
    def sansScalingAndShear (self, *args, **kwargs):
      '''
sansScalingAndShear( (M44d)arg1 [, (bool)arg2]) -> M44d :
    sans scaling and shear

    C++ signature :
        Imath_3_1::Matrix44<double> sansScalingAndShear(Imath_3_1::Matrix44<double> [,bool])'''
    ...
    def scale (self, *args, **kwargs):
      '''
scale( (M44d)arg1, (float)arg2) -> M44d :
    scale matrix

    C++ signature :
        Imath_3_1::Matrix44<double> scale(Imath_3_1::Matrix44<double> {lvalue},double)

scale( (M44d)arg1, (V3d)arg2) -> M44d :
    scale matrix

    C++ signature :
        Imath_3_1::Matrix44<double> scale(Imath_3_1::Matrix44<double> {lvalue},Imath_3_1::Vec3<double>)

scale( (M44d)arg1, (tuple)arg2) -> M44d :
    scale matrix

    C++ signature :
        Imath_3_1::Matrix44<double> scale(Imath_3_1::Matrix44<double> {lvalue},boost::python::tuple)'''
    ...
    def setScale (self, *args, **kwargs):
      '''
setScale( (M44d)arg1, (float)arg2) -> M44d :
    setScale()

    C++ signature :
        Imath_3_1::Matrix44<double> setScale(Imath_3_1::Matrix44<double> {lvalue},double)

setScale( (M44d)arg1, (V3d)arg2) -> M44d :
    setScale()

    C++ signature :
        Imath_3_1::Matrix44<double> setScale(Imath_3_1::Matrix44<double> {lvalue},Imath_3_1::Vec3<double>)

setScale( (M44d)arg1, (tuple)arg2) -> M44d :
    setScale()

    C++ signature :
        Imath_3_1::Matrix44<double> setScale(Imath_3_1::Matrix44<double> {lvalue},boost::python::tuple)'''
    ...
    def setShear (self, *args, **kwargs):
      '''
setShear( (M44d)arg1, (V3d)arg2) -> M44d :
    setShear()

    C++ signature :
        Imath_3_1::Matrix44<double> setShear(Imath_3_1::Matrix44<double> {lvalue},Imath_3_1::Vec3<double>)

setShear( (M44d)arg1, (Shear6d)arg2) -> M44d :
    setShear()

    C++ signature :
        Imath_3_1::Matrix44<double> setShear(Imath_3_1::Matrix44<double> {lvalue},Imath_3_1::Shear6<double>)

setShear( (M44d)arg1, (tuple)arg2) -> M44d :
    setShear()

    C++ signature :
        Imath_3_1::Matrix44<double> setShear(Imath_3_1::Matrix44<double> {lvalue},boost::python::tuple)'''
    ...
    def setTranslation (self, *args, **kwargs):
      '''
setTranslation( (M44d)arg1, (V3d)arg2) -> M44d :
    setTranslation()

    C++ signature :
        Imath_3_1::Matrix44<double> setTranslation(Imath_3_1::Matrix44<double> {lvalue},Imath_3_1::Vec3<double>)

setTranslation( (M44d)arg1, (tuple)arg2) -> M44d :
    setTranslation()

    C++ signature :
        Imath_3_1::Matrix44<double> setTranslation(Imath_3_1::Matrix44<double> {lvalue},boost::python::tuple)

setTranslation( (M44d)arg1, (object)arg2) -> M44d :
    setTranslation()

    C++ signature :
        Imath_3_1::Matrix44<double> setTranslation(Imath_3_1::Matrix44<double> {lvalue},boost::python::api::object)'''
    ...
    def setValue (self, *args, **kwargs):
      '''
setValue( (M44d)arg1, (M44d)arg2) -> None :
    setValue()

    C++ signature :
        void setValue(Imath_3_1::Matrix44<double> {lvalue},Imath_3_1::Matrix44<double>)'''
    ...
    def shear (self, *args, **kwargs):
      '''
shear( (M44d)arg1, (V3d)arg2) -> M44d :
    shear()

    C++ signature :
        Imath_3_1::Matrix44<double> shear(Imath_3_1::Matrix44<double> {lvalue},Imath_3_1::Vec3<double>)

shear( (M44d)arg1, (Shear6d)arg2) -> M44d :
    shear()

    C++ signature :
        Imath_3_1::Matrix44<double> shear(Imath_3_1::Matrix44<double> {lvalue},Imath_3_1::Shear6<double>)

shear( (M44d)arg1, (tuple)arg2) -> M44d :
    shear()

    C++ signature :
        Imath_3_1::Matrix44<double> shear(Imath_3_1::Matrix44<double> {lvalue},boost::python::tuple)'''
    ...
    def singularValueDecomposition (self, *args, **kwargs):
      '''
singularValueDecomposition( (M44d)matrix, (bool)forcePositiveDeterminant) -> tuple :
    Decomposes the matrix using the singular value decomposition (SVD) into three
    matrices U, S, and V which have the following properties: 
      1. U and V are both orthonormal matrices, 
      2. S is the diagonal matrix of singular values, 
      3. U * S * V.transposed() gives back the original matrix.
    The result is returned as a tuple [U, S, V].  Note that since S is diagonal we
    don't need to return the entire matrix, so we return it as a three-vector.  
    
    The 'forcePositiveDeterminant' argument can be used to force the U and V^T to
    have positive determinant (that is, to be proper rotation matrices); if
    forcePositiveDeterminant is False, then the singular values are guaranteed to
    be nonnegative but the U and V matrices might contain negative scale along one
    of the axes; if forcePositiveDeterminant is True, then U and V cannot contain
    negative scale but S[3] might be negative.  
    
    Our SVD implementation uses two-sided Jacobi rotations to iteratively
    diagonalize the matrix, which should be quite robust and significantly faster
    than the more general SVD solver in LAPACK.  
    

    C++ signature :
        boost::python::tuple singularValueDecomposition(Imath_3_1::Matrix44<double>,bool)'''
    ...
    def symmetricEigensolve (self, *args, **kwargs):
      '''
symmetricEigensolve( (M44d)arg1) -> tuple :
    Decomposes the matrix A using a symmetric eigensolver into matrices Q and S 
    which have the following properties: 
      1. Q is the orthonormal matrix of eigenvectors, 
      2. S is the diagonal matrix of eigenvalues, 
      3. Q.transposed() * S * Q gives back the original matrix.
    
    IMPORTANT: It is vital that the passed-in matrix be symmetric, or the result 
    won't make any sense.  This function will return an error if passed an 
    unsymmetric matrix.
    
    The result is returned as a tuple [Q, S].  Note that since S is diagonal 
    we don't need to return the entire matrix, so we return it as a three-vector. 
    
    Our eigensolver implementation uses one-sided Jacobi rotations to iteratively 
    diagonalize the matrix, which should be quite robust and significantly faster 
    than the more general symmetric eigenvalue solver in LAPACK.  
    

    C++ signature :
        boost::python::tuple symmetricEigensolve(Imath_3_1::Matrix44<double>)'''
    ...
    def translate (self, *args, **kwargs):
      '''
translate( (M44d)arg1, (object)arg2) -> M44d :
    translate()

    C++ signature :
        Imath_3_1::Matrix44<double> translate(Imath_3_1::Matrix44<double> {lvalue},boost::python::api::object)

translate( (M44d)arg1, (tuple)arg2) -> M44d :
    translate()

    C++ signature :
        Imath_3_1::Matrix44<double> translate(Imath_3_1::Matrix44<double> {lvalue},boost::python::tuple)'''
    ...
    def translation (self, *args, **kwargs):
      '''
translation( (M44d)arg1) -> V3d :
    translation()

    C++ signature :
        Imath_3_1::Vec3<double> translation(Imath_3_1::Matrix44<double> {lvalue})'''
    ...
    def transpose (self, *args, **kwargs):
      '''
transpose( (M44d)arg1) -> M44d :
    transpose() transpose this matrix

    C++ signature :
        Imath_3_1::Matrix44<double> transpose(Imath_3_1::Matrix44<double> {lvalue})'''
    ...
    def transposed (self, *args, **kwargs):
      '''
transposed( (M44d)arg1) -> M44d :
    transposed() return a transposed copy of this matrix

    C++ signature :
        Imath_3_1::Matrix44<double> transposed(Imath_3_1::Matrix44<double> {lvalue})'''
    ...

def M44dArray (*args):
      '''
__init__(_object*, PyImath::FixedArray<Imath_3_1::Matrix44<double> >)
__init__(boost::python::api::object, PyImath::FixedArray<double>, PyImath::FixedArray<double>, PyImath::FixedArray<double>, PyImath::FixedArray<double>, PyImath::FixedArray<double>, PyImath::FixedArray<double>, PyImath::FixedArray<double>, PyImath::FixedArray<double>, PyImath::FixedArray<double>, PyImath::FixedArray<double>, PyImath::FixedArray<double>, PyImath::FixedArray<double>, PyImath::FixedArray<double>, PyImath::FixedArray<double>, PyImath::FixedArray<double>, PyImath::FixedArray<double>)
__init__(_object*, Imath_3_1::Matrix44<double>, unsigned long)
__init__(_object*, PyImath::FixedArray<Imath_3_1::Matrix44<double> >)
__init__(_object*, unsigned long)

'''      
    ...

class M44dArray:
    def ifelse (self, *args, **kwargs):
      '''
ifelse( (M44dArray)arg1, (IntArray)arg2, (M44d)arg3) -> M44dArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Matrix44<double> > ifelse(PyImath::FixedArray<Imath_3_1::Matrix44<double> > {lvalue},PyImath::FixedArray<int>,Imath_3_1::Matrix44<double>)

ifelse( (M44dArray)arg1, (IntArray)arg2, (M44dArray)arg3) -> M44dArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Matrix44<double> > ifelse(PyImath::FixedArray<Imath_3_1::Matrix44<double> > {lvalue},PyImath::FixedArray<int>,PyImath::FixedArray<Imath_3_1::Matrix44<double> >)'''
    ...
    def inverse (self, *args, **kwargs):
      '''
inverse( (M44dArray)vector) -> M44dArray :
    Return M^-1 for each element M.

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Matrix44<double> > inverse(PyImath::FixedArray<Imath_3_1::Matrix44<double> >)'''
    ...
    def invert (self, *args, **kwargs):
      '''
invert( (M44dArray)arg1) -> None :
    Perform M^-1 in place for each element M.

    C++ signature :
        void invert(PyImath::FixedArray<Imath_3_1::Matrix44<double> > {lvalue})'''
    ...
    def makeReadOnly (self, *args, **kwargs):
      '''
makeReadOnly( (M44dArray)arg1) -> None :

    C++ signature :
        void makeReadOnly(PyImath::FixedArray<Imath_3_1::Matrix44<double> > {lvalue})'''
    ...
    def multDirMatrix (self, *args, **kwargs):
      '''
multDirMatrix( (M44dArray)arg1, (V3dArray)vector) -> V3dArray :
    Multiply an array of vectors element by element with the matrix array.

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec3<double> > multDirMatrix(PyImath::FixedArray<Imath_3_1::Matrix44<double> >,PyImath::FixedArray<Imath_3_1::Vec3<double> >)'''
    ...
    def multVecMatrix (self, *args, **kwargs):
      '''
multVecMatrix( (M44dArray)arg1, (V3dArray)vector) -> V3dArray :
    Multiply an array of normals element by element with the matrix array.

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec3<double> > multVecMatrix(PyImath::FixedArray<Imath_3_1::Matrix44<double> >,PyImath::FixedArray<Imath_3_1::Vec3<double> >)'''
    ...
    def transpose (self, *args, **kwargs):
      '''
transpose( (M44dArray)arg1) -> None :
    Perform M^T in place for each element M.

    C++ signature :
        void transpose(PyImath::FixedArray<Imath_3_1::Matrix44<double> > {lvalue})'''
    ...
    def writable (self, *args, **kwargs):
      '''
writable( (M44dArray)arg1) -> bool :

    C++ signature :
        bool writable(PyImath::FixedArray<Imath_3_1::Matrix44<double> > {lvalue})'''
    ...

def M44dRow (*args):
      '''

'''      
    ...

class M44dRow:

def M44f (*args):
      '''
__init__(_object*, float, float, float, float, float, float, float, float, float, float, float, float, float, float, float, float)
__init__(boost::python::api::object, Imath_3_1::Matrix44<double>)
__init__(boost::python::api::object, Imath_3_1::Matrix44<float>)
__init__(boost::python::api::object, boost::python::tuple, boost::python::tuple, boost::python::tuple, boost::python::tuple)
__init__(_object*, float)
__init__(_object*)
__init__(_object*, Imath_3_1::Matrix44<float>)

'''      
    ...

class M44f:
    def baseTypeEpsilon (self, *args, **kwargs):
      '''
baseTypeEpsilon() -> float :
    baseTypeEpsilon() epsilon value of the base type of the vector

    C++ signature :
        float baseTypeEpsilon()'''
    ...
    def baseTypeLowest (self, *args, **kwargs):
      '''
baseTypeLowest() -> float :
    baseTypeLowest() largest negative value of the base type of the vector

    C++ signature :
        float baseTypeLowest()'''
    ...
    def baseTypeMax (self, *args, **kwargs):
      '''
baseTypeMax() -> float :
    baseTypeMax() max value of the base type of the vector

    C++ signature :
        float baseTypeMax()'''
    ...
    def baseTypeSmallest (self, *args, **kwargs):
      '''
baseTypeSmallest() -> float :
    baseTypeSmallest() smallest value of the base type of the vector

    C++ signature :
        float baseTypeSmallest()'''
    ...
    def determinant (self, *args, **kwargs):
      '''
determinant( (M44f)arg1) -> float :
    determinant() return the determinant of this matrix

    C++ signature :
        float determinant(Imath_3_1::Matrix44<float> {lvalue})'''
    ...
    def equalWithAbsError (self, *args, **kwargs):
      '''
equalWithAbsError( (M44f)arg1, (M44f)arg2, (float)arg3) -> bool :
    m1.equalWithAbsError(m2,e) true if the elements of v1 and v2 are the same with an absolute error of no more than e, i.e., abs(m1[i] - m2[i]) <= e

    C++ signature :
        bool equalWithAbsError(Imath_3_1::Matrix44<float> {lvalue},Imath_3_1::Matrix44<float>,float)'''
    ...
    def equalWithRelError (self, *args, **kwargs):
      '''
equalWithRelError( (M44f)arg1, (M44f)arg2, (float)arg3) -> bool :
    m1.equalWithAbsError(m2,e) true if the elements of m1 and m2 are the same with an absolute error of no more than e, i.e., abs(m1[i] - m2[i]) <= e * abs(m1[i])

    C++ signature :
        bool equalWithRelError(Imath_3_1::Matrix44<float> {lvalue},Imath_3_1::Matrix44<float>,float)'''
    ...
    def extractAndRemoveScalingAndShear (self, *args, **kwargs):
      '''
extractAndRemoveScalingAndShear( (M44f)arg1, (V3f)arg2, (V3f)arg3 [, (int)arg4]) -> None :
    M.extractAndRemoveScalingAndShear(scl, shr, [exc]) -- extracts the scaling component of M into scl and the shearing component of M into shr.  Also removes the scaling and shearing components from M.  Returns 1 unless the scaling component is nearly 0, in which case 0 is returned. If optional arg. exc == 1, then if the scaling component is nearly 0, then MathExc is thrown.

    C++ signature :
        void extractAndRemoveScalingAndShear(Imath_3_1::Matrix44<float> {lvalue},Imath_3_1::Vec3<float> {lvalue},Imath_3_1::Vec3<float> {lvalue} [,int])'''
    ...
    def extractEulerXYZ (self, *args, **kwargs):
      '''
extractEulerXYZ( (M44f)arg1, (V3f)arg2) -> None :
    extract Euler

    C++ signature :
        void extractEulerXYZ(Imath_3_1::Matrix44<float> {lvalue},Imath_3_1::Vec3<float> {lvalue})'''
    ...
    def extractEulerZYX (self, *args, **kwargs):
      '''
extractEulerZYX( (M44f)arg1, (V3f)arg2) -> None :
    extract Euler

    C++ signature :
        void extractEulerZYX(Imath_3_1::Matrix44<float> {lvalue},Imath_3_1::Vec3<float> {lvalue})'''
    ...
    def extractSHRT (self, *args, **kwargs):
      '''
extractSHRT( (M44f)arg1, (V3f)arg2, (V3f)arg3, (V3f)arg4, (V3f)arg5 [, (int)arg6]) -> int :
    M.extractSHRT(Vs, Vh, Vr, Vt, [exc]) -- extracts the scaling component of M into Vs, the shearing component of M in Vh (as XY, XZ, YZ shear factors), the rotation of M into Vr (as Euler angles in the order XYZ), and the translaation of M into Vt. If optional arg. exc == 1, then if the scaling component is nearly 0, then MathExc is thrown. 

    C++ signature :
        int extractSHRT(Imath_3_1::Matrix44<float> {lvalue},Imath_3_1::Vec3<float> {lvalue},Imath_3_1::Vec3<float> {lvalue},Imath_3_1::Vec3<float> {lvalue},Imath_3_1::Vec3<float> {lvalue} [,int])'''
    ...
    def extractScaling (self, *args, **kwargs):
      '''
extractScaling( (M44f)arg1, (V3f)arg2 [, (int)arg3]) -> None :
    extract scaling

    C++ signature :
        void extractScaling(Imath_3_1::Matrix44<float> {lvalue},Imath_3_1::Vec3<float> {lvalue} [,int])'''
    ...
    def extractScalingAndShear (self, *args, **kwargs):
      '''
extractScalingAndShear( (M44f)arg1, (V3f)arg2, (V3f)arg3 [, (int)arg4]) -> None :
    extract scaling

    C++ signature :
        void extractScalingAndShear(Imath_3_1::Matrix44<float> {lvalue},Imath_3_1::Vec3<float> {lvalue},Imath_3_1::Vec3<float> {lvalue} [,int])'''
    ...
    def fastMinor (self, *args, **kwargs):
      '''
fastMinor( (M44f)arg1, (int)arg2, (int)arg3, (int)arg4, (int)arg5, (int)arg6, (int)arg7) -> float :
    fastMinor() return matrix minor using the specified rows and columns of this matrix

    C++ signature :
        float fastMinor(Imath_3_1::Matrix44<float> {lvalue},int,int,int,int,int,int)'''
    ...
    def gjInverse (self, *args, **kwargs):
      '''
gjInverse( (M44f)arg1 [, (bool)arg2]) -> M44f :
    gjInverse() return an inverted copy of this matrix

    C++ signature :
        Imath_3_1::Matrix44<float> gjInverse(Imath_3_1::Matrix44<float> {lvalue} [,bool])'''
    ...
    def gjInvert (self, *args, **kwargs):
      '''
gjInvert( (M44f)arg1 [, (bool)arg2]) -> M44f :
    gjInvert() invert this matrix

    C++ signature :
        Imath_3_1::Matrix44<float> gjInvert(Imath_3_1::Matrix44<float> {lvalue} [,bool])'''
    ...
    def inverse (self, *args, **kwargs):
      '''
inverse( (M44f)arg1 [, (bool)arg2]) -> M44f :
    inverse() return an inverted copy of this matrix

    C++ signature :
        Imath_3_1::Matrix44<float> inverse(Imath_3_1::Matrix44<float> {lvalue} [,bool])'''
    ...
    def invert (self, *args, **kwargs):
      '''
invert( (M44f)arg1 [, (bool)arg2]) -> M44f :
    invert() invert this matrix

    C++ signature :
        Imath_3_1::Matrix44<float> invert(Imath_3_1::Matrix44<float> {lvalue} [,bool])'''
    ...
    def makeIdentity (self, *args, **kwargs):
      '''
makeIdentity( (M44f)arg1) -> None :
    makeIdentity() make this matrix the identity matrix

    C++ signature :
        void makeIdentity(Imath_3_1::Matrix44<float> {lvalue})'''
    ...
    def minorOf (self, *args, **kwargs):
      '''
minorOf( (M44f)arg1, (int)arg2, (int)arg3) -> float :
    minorOf() return matrix minor of the (row,col) element of this matrix

    C++ signature :
        float minorOf(Imath_3_1::Matrix44<float> {lvalue},int,int)'''
    ...
    def multDirMatrix (self, *args, **kwargs):
      '''
multDirMatrix( (M44f)arg1, (V3d)arg2, (V3d)arg3) -> None :
    mult matrix

    C++ signature :
        void multDirMatrix(Imath_3_1::Matrix44<float> {lvalue},Imath_3_1::Vec3<double>,Imath_3_1::Vec3<double> {lvalue})

multDirMatrix( (M44f)arg1, (V3d)arg2) -> V3d :
    mult matrix

    C++ signature :
        Imath_3_1::Vec3<double> multDirMatrix(Imath_3_1::Matrix44<float> {lvalue},Imath_3_1::Vec3<double>)

multDirMatrix( (M44f)arg1, (V3dArray)arg2) -> V3dArray :
    mult matrix

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec3<double> > multDirMatrix(Imath_3_1::Matrix44<float> {lvalue},PyImath::FixedArray<Imath_3_1::Vec3<double> >)

multDirMatrix( (M44f)arg1, (V3f)arg2, (V3f)arg3) -> None :
    mult matrix

    C++ signature :
        void multDirMatrix(Imath_3_1::Matrix44<float> {lvalue},Imath_3_1::Vec3<float>,Imath_3_1::Vec3<float> {lvalue})

multDirMatrix( (M44f)arg1, (V3f)arg2) -> V3f :
    mult matrix

    C++ signature :
        Imath_3_1::Vec3<float> multDirMatrix(Imath_3_1::Matrix44<float> {lvalue},Imath_3_1::Vec3<float>)

multDirMatrix( (M44f)arg1, (V3fArray)arg2) -> V3fArray :
    mult matrix

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec3<float> > multDirMatrix(Imath_3_1::Matrix44<float> {lvalue},PyImath::FixedArray<Imath_3_1::Vec3<float> >)'''
    ...
    def multVecMatrix (self, *args, **kwargs):
      '''
multVecMatrix( (M44f)arg1, (V3d)arg2, (V3d)arg3) -> None :
    mult matrix

    C++ signature :
        void multVecMatrix(Imath_3_1::Matrix44<float> {lvalue},Imath_3_1::Vec3<double>,Imath_3_1::Vec3<double> {lvalue})

multVecMatrix( (M44f)arg1, (V3d)arg2) -> V3d :
    mult matrix

    C++ signature :
        Imath_3_1::Vec3<double> multVecMatrix(Imath_3_1::Matrix44<float> {lvalue},Imath_3_1::Vec3<double>)

multVecMatrix( (M44f)arg1, (V3dArray)arg2) -> V3dArray :
    mult matrix

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec3<double> > multVecMatrix(Imath_3_1::Matrix44<float> {lvalue},PyImath::FixedArray<Imath_3_1::Vec3<double> >)

multVecMatrix( (M44f)arg1, (V3f)arg2, (V3f)arg3) -> None :
    mult matrix

    C++ signature :
        void multVecMatrix(Imath_3_1::Matrix44<float> {lvalue},Imath_3_1::Vec3<float>,Imath_3_1::Vec3<float> {lvalue})

multVecMatrix( (M44f)arg1, (V3f)arg2) -> V3f :
    mult matrix

    C++ signature :
        Imath_3_1::Vec3<float> multVecMatrix(Imath_3_1::Matrix44<float> {lvalue},Imath_3_1::Vec3<float>)

multVecMatrix( (M44f)arg1, (V3fArray)arg2) -> V3fArray :
    mult matrix

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec3<float> > multVecMatrix(Imath_3_1::Matrix44<float> {lvalue},PyImath::FixedArray<Imath_3_1::Vec3<float> >)'''
    ...
    def negate (self, *args, **kwargs):
      '''
negate( (M44f)arg1) -> M44f :
    negate() negate all entries in this matrix

    C++ signature :
        Imath_3_1::Matrix44<float> negate(Imath_3_1::Matrix44<float> {lvalue})'''
    ...
    def removeScaling (self, *args, **kwargs):
      '''
removeScaling( (M44f)arg1 [, (int)arg2]) -> int :
    remove scaling

    C++ signature :
        int removeScaling(Imath_3_1::Matrix44<float> {lvalue} [,int])'''
    ...
    def removeScalingAndShear (self, *args, **kwargs):
      '''
removeScalingAndShear( (M44f)arg1 [, (int)arg2]) -> int :
    remove scaling

    C++ signature :
        int removeScalingAndShear(Imath_3_1::Matrix44<float> {lvalue} [,int])'''
    ...
    def rotate (self, *args, **kwargs):
      '''
rotate( (M44f)arg1, (V3f)arg2) -> M44f :
    rotate matrix

    C++ signature :
        Imath_3_1::Matrix44<float> rotate(Imath_3_1::Matrix44<float> {lvalue},Imath_3_1::Vec3<float>)'''
    ...
    def rotationMatrix (self, *args, **kwargs):
      '''
rotationMatrix( (M44f)arg1, (object)arg2, (object)arg3) -> M44f :
    rotationMatrix()

    C++ signature :
        Imath_3_1::Matrix44<float> rotationMatrix(Imath_3_1::Matrix44<float> {lvalue},boost::python::api::object,boost::python::api::object)'''
    ...
    def rotationMatrixWithUpDir (self, *args, **kwargs):
      '''
rotationMatrixWithUpDir( (M44f)arg1, (object)arg2, (object)arg3, (object)arg4) -> M44f :
    roationMatrixWithUp()

    C++ signature :
        Imath_3_1::Matrix44<float> rotationMatrixWithUpDir(Imath_3_1::Matrix44<float> {lvalue},boost::python::api::object,boost::python::api::object,boost::python::api::object)'''
    ...
    def sansScaling (self, *args, **kwargs):
      '''
sansScaling( (M44f)arg1 [, (bool)arg2]) -> M44f :
    sans scaling

    C++ signature :
        Imath_3_1::Matrix44<float> sansScaling(Imath_3_1::Matrix44<float> [,bool])'''
    ...
    def sansScalingAndShear (self, *args, **kwargs):
      '''
sansScalingAndShear( (M44f)arg1 [, (bool)arg2]) -> M44f :
    sans scaling and shear

    C++ signature :
        Imath_3_1::Matrix44<float> sansScalingAndShear(Imath_3_1::Matrix44<float> [,bool])'''
    ...
    def scale (self, *args, **kwargs):
      '''
scale( (M44f)arg1, (float)arg2) -> M44f :
    scale matrix

    C++ signature :
        Imath_3_1::Matrix44<float> scale(Imath_3_1::Matrix44<float> {lvalue},float)

scale( (M44f)arg1, (V3f)arg2) -> M44f :
    scale matrix

    C++ signature :
        Imath_3_1::Matrix44<float> scale(Imath_3_1::Matrix44<float> {lvalue},Imath_3_1::Vec3<float>)

scale( (M44f)arg1, (tuple)arg2) -> M44f :
    scale matrix

    C++ signature :
        Imath_3_1::Matrix44<float> scale(Imath_3_1::Matrix44<float> {lvalue},boost::python::tuple)'''
    ...
    def setScale (self, *args, **kwargs):
      '''
setScale( (M44f)arg1, (float)arg2) -> M44f :
    setScale()

    C++ signature :
        Imath_3_1::Matrix44<float> setScale(Imath_3_1::Matrix44<float> {lvalue},float)

setScale( (M44f)arg1, (V3f)arg2) -> M44f :
    setScale()

    C++ signature :
        Imath_3_1::Matrix44<float> setScale(Imath_3_1::Matrix44<float> {lvalue},Imath_3_1::Vec3<float>)

setScale( (M44f)arg1, (tuple)arg2) -> M44f :
    setScale()

    C++ signature :
        Imath_3_1::Matrix44<float> setScale(Imath_3_1::Matrix44<float> {lvalue},boost::python::tuple)'''
    ...
    def setShear (self, *args, **kwargs):
      '''
setShear( (M44f)arg1, (V3f)arg2) -> M44f :
    setShear()

    C++ signature :
        Imath_3_1::Matrix44<float> setShear(Imath_3_1::Matrix44<float> {lvalue},Imath_3_1::Vec3<float>)

setShear( (M44f)arg1, (Shear6f)arg2) -> M44f :
    setShear()

    C++ signature :
        Imath_3_1::Matrix44<float> setShear(Imath_3_1::Matrix44<float> {lvalue},Imath_3_1::Shear6<float>)

setShear( (M44f)arg1, (tuple)arg2) -> M44f :
    setShear()

    C++ signature :
        Imath_3_1::Matrix44<float> setShear(Imath_3_1::Matrix44<float> {lvalue},boost::python::tuple)'''
    ...
    def setTranslation (self, *args, **kwargs):
      '''
setTranslation( (M44f)arg1, (V3f)arg2) -> M44f :
    setTranslation()

    C++ signature :
        Imath_3_1::Matrix44<float> setTranslation(Imath_3_1::Matrix44<float> {lvalue},Imath_3_1::Vec3<float>)

setTranslation( (M44f)arg1, (tuple)arg2) -> M44f :
    setTranslation()

    C++ signature :
        Imath_3_1::Matrix44<float> setTranslation(Imath_3_1::Matrix44<float> {lvalue},boost::python::tuple)

setTranslation( (M44f)arg1, (object)arg2) -> M44f :
    setTranslation()

    C++ signature :
        Imath_3_1::Matrix44<float> setTranslation(Imath_3_1::Matrix44<float> {lvalue},boost::python::api::object)'''
    ...
    def setValue (self, *args, **kwargs):
      '''
setValue( (M44f)arg1, (M44f)arg2) -> None :
    setValue()

    C++ signature :
        void setValue(Imath_3_1::Matrix44<float> {lvalue},Imath_3_1::Matrix44<float>)'''
    ...
    def shear (self, *args, **kwargs):
      '''
shear( (M44f)arg1, (V3f)arg2) -> M44f :
    shear()

    C++ signature :
        Imath_3_1::Matrix44<float> shear(Imath_3_1::Matrix44<float> {lvalue},Imath_3_1::Vec3<float>)

shear( (M44f)arg1, (Shear6f)arg2) -> M44f :
    shear()

    C++ signature :
        Imath_3_1::Matrix44<float> shear(Imath_3_1::Matrix44<float> {lvalue},Imath_3_1::Shear6<float>)

shear( (M44f)arg1, (tuple)arg2) -> M44f :
    shear()

    C++ signature :
        Imath_3_1::Matrix44<float> shear(Imath_3_1::Matrix44<float> {lvalue},boost::python::tuple)'''
    ...
    def singularValueDecomposition (self, *args, **kwargs):
      '''
singularValueDecomposition( (M44f)matrix, (bool)forcePositiveDeterminant) -> tuple :
    Decomposes the matrix using the singular value decomposition (SVD) into three
    matrices U, S, and V which have the following properties: 
      1. U and V are both orthonormal matrices, 
      2. S is the diagonal matrix of singular values, 
      3. U * S * V.transposed() gives back the original matrix.
    The result is returned as a tuple [U, S, V].  Note that since S is diagonal we
    don't need to return the entire matrix, so we return it as a three-vector.  
    
    The 'forcePositiveDeterminant' argument can be used to force the U and V^T to
    have positive determinant (that is, to be proper rotation matrices); if
    forcePositiveDeterminant is False, then the singular values are guaranteed to
    be nonnegative but the U and V matrices might contain negative scale along one
    of the axes; if forcePositiveDeterminant is True, then U and V cannot contain
    negative scale but S[3] might be negative.  
    
    Our SVD implementation uses two-sided Jacobi rotations to iteratively
    diagonalize the matrix, which should be quite robust and significantly faster
    than the more general SVD solver in LAPACK.  
    

    C++ signature :
        boost::python::tuple singularValueDecomposition(Imath_3_1::Matrix44<float>,bool)'''
    ...
    def symmetricEigensolve (self, *args, **kwargs):
      '''
symmetricEigensolve( (M44f)arg1) -> tuple :
    Decomposes the matrix A using a symmetric eigensolver into matrices Q and S 
    which have the following properties: 
      1. Q is the orthonormal matrix of eigenvectors, 
      2. S is the diagonal matrix of eigenvalues, 
      3. Q.transposed() * S * Q gives back the original matrix.
    
    IMPORTANT: It is vital that the passed-in matrix be symmetric, or the result 
    won't make any sense.  This function will return an error if passed an 
    unsymmetric matrix.
    
    The result is returned as a tuple [Q, S].  Note that since S is diagonal 
    we don't need to return the entire matrix, so we return it as a three-vector. 
    
    Our eigensolver implementation uses one-sided Jacobi rotations to iteratively 
    diagonalize the matrix, which should be quite robust and significantly faster 
    than the more general symmetric eigenvalue solver in LAPACK.  
    

    C++ signature :
        boost::python::tuple symmetricEigensolve(Imath_3_1::Matrix44<float>)'''
    ...
    def translate (self, *args, **kwargs):
      '''
translate( (M44f)arg1, (object)arg2) -> M44f :
    translate()

    C++ signature :
        Imath_3_1::Matrix44<float> translate(Imath_3_1::Matrix44<float> {lvalue},boost::python::api::object)

translate( (M44f)arg1, (tuple)arg2) -> M44f :
    translate()

    C++ signature :
        Imath_3_1::Matrix44<float> translate(Imath_3_1::Matrix44<float> {lvalue},boost::python::tuple)'''
    ...
    def translation (self, *args, **kwargs):
      '''
translation( (M44f)arg1) -> V3f :
    translation()

    C++ signature :
        Imath_3_1::Vec3<float> translation(Imath_3_1::Matrix44<float> {lvalue})'''
    ...
    def transpose (self, *args, **kwargs):
      '''
transpose( (M44f)arg1) -> M44f :
    transpose() transpose this matrix

    C++ signature :
        Imath_3_1::Matrix44<float> transpose(Imath_3_1::Matrix44<float> {lvalue})'''
    ...
    def transposed (self, *args, **kwargs):
      '''
transposed( (M44f)arg1) -> M44f :
    transposed() return a transposed copy of this matrix

    C++ signature :
        Imath_3_1::Matrix44<float> transposed(Imath_3_1::Matrix44<float> {lvalue})'''
    ...

def M44fArray (*args):
      '''
__init__(_object*, PyImath::FixedArray<Imath_3_1::Matrix44<float> >)
__init__(boost::python::api::object, PyImath::FixedArray<float>, PyImath::FixedArray<float>, PyImath::FixedArray<float>, PyImath::FixedArray<float>, PyImath::FixedArray<float>, PyImath::FixedArray<float>, PyImath::FixedArray<float>, PyImath::FixedArray<float>, PyImath::FixedArray<float>, PyImath::FixedArray<float>, PyImath::FixedArray<float>, PyImath::FixedArray<float>, PyImath::FixedArray<float>, PyImath::FixedArray<float>, PyImath::FixedArray<float>, PyImath::FixedArray<float>)
__init__(_object*, Imath_3_1::Matrix44<float>, unsigned long)
__init__(_object*, PyImath::FixedArray<Imath_3_1::Matrix44<float> >)
__init__(_object*, unsigned long)

'''      
    ...

class M44fArray:
    def ifelse (self, *args, **kwargs):
      '''
ifelse( (M44fArray)arg1, (IntArray)arg2, (M44f)arg3) -> M44fArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Matrix44<float> > ifelse(PyImath::FixedArray<Imath_3_1::Matrix44<float> > {lvalue},PyImath::FixedArray<int>,Imath_3_1::Matrix44<float>)

ifelse( (M44fArray)arg1, (IntArray)arg2, (M44fArray)arg3) -> M44fArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Matrix44<float> > ifelse(PyImath::FixedArray<Imath_3_1::Matrix44<float> > {lvalue},PyImath::FixedArray<int>,PyImath::FixedArray<Imath_3_1::Matrix44<float> >)'''
    ...
    def inverse (self, *args, **kwargs):
      '''
inverse( (M44fArray)vector) -> M44fArray :
    Return M^-1 for each element M.

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Matrix44<float> > inverse(PyImath::FixedArray<Imath_3_1::Matrix44<float> >)'''
    ...
    def invert (self, *args, **kwargs):
      '''
invert( (M44fArray)arg1) -> None :
    Perform M^-1 in place for each element M.

    C++ signature :
        void invert(PyImath::FixedArray<Imath_3_1::Matrix44<float> > {lvalue})'''
    ...
    def makeReadOnly (self, *args, **kwargs):
      '''
makeReadOnly( (M44fArray)arg1) -> None :

    C++ signature :
        void makeReadOnly(PyImath::FixedArray<Imath_3_1::Matrix44<float> > {lvalue})'''
    ...
    def multDirMatrix (self, *args, **kwargs):
      '''
multDirMatrix( (M44fArray)arg1, (V3fArray)vector) -> V3fArray :
    Multiply an array of vectors element by element with the matrix array.

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec3<float> > multDirMatrix(PyImath::FixedArray<Imath_3_1::Matrix44<float> >,PyImath::FixedArray<Imath_3_1::Vec3<float> >)'''
    ...
    def multVecMatrix (self, *args, **kwargs):
      '''
multVecMatrix( (M44fArray)arg1, (V3fArray)vector) -> V3fArray :
    Multiply an array of normals element by element with the matrix array.

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec3<float> > multVecMatrix(PyImath::FixedArray<Imath_3_1::Matrix44<float> >,PyImath::FixedArray<Imath_3_1::Vec3<float> >)'''
    ...
    def transpose (self, *args, **kwargs):
      '''
transpose( (M44fArray)arg1) -> None :
    Perform M^T in place for each element M.

    C++ signature :
        void transpose(PyImath::FixedArray<Imath_3_1::Matrix44<float> > {lvalue})'''
    ...
    def writable (self, *args, **kwargs):
      '''
writable( (M44fArray)arg1) -> bool :

    C++ signature :
        bool writable(PyImath::FixedArray<Imath_3_1::Matrix44<float> > {lvalue})'''
    ...

def M44fRow (*args):
      '''

'''      
    ...

class M44fRow:

def Plane3d (*args):
      '''
__init__(_object*, Imath_3_1::Vec3<double>, Imath_3_1::Vec3<double>, Imath_3_1::Vec3<double>)
__init__(_object*, Imath_3_1::Vec3<double>, Imath_3_1::Vec3<double>)
__init__(_object*, Imath_3_1::Vec3<double>, double)
__init__(boost::python::api::object, boost::python::api::object)
__init__(boost::python::api::object, boost::python::tuple, boost::python::tuple, boost::python::tuple)
__init__(boost::python::api::object, boost::python::tuple, boost::python::tuple)
__init__(boost::python::api::object, boost::python::tuple, double)
__init__(boost::python::api::object)
__init__(_object*)

'''      
    ...

class Plane3d:
    def distance (self, *args, **kwargs):
      '''
distance( (Plane3d)arg1) -> float :
    distance()

    C++ signature :
        double distance(Imath_3_1::Plane3<double> {lvalue})'''
    ...
    def distanceTo (self, *args, **kwargs):
      '''
distanceTo( (Plane3d)arg1, (V3d)arg2) -> float :
    distanceTo()

    C++ signature :
        double distanceTo(Imath_3_1::Plane3<double> {lvalue},Imath_3_1::Vec3<double>)

distanceTo( (Plane3d)arg1, (tuple)arg2) -> float :

    C++ signature :
        double distanceTo(Imath_3_1::Plane3<double> {lvalue},boost::python::tuple)'''
    ...
    def intersect (self, *args, **kwargs):
      '''
intersect( (Plane3d)arg1, (Line3d)arg2, (V3d)arg3) -> bool :
    pl.intersect(ln, pt) -- returns true if the line intersects
    the plane, false if it doesn't.  The point where plane
    pl and line ln intersect is stored in pt

    C++ signature :
        bool intersect(Imath_3_1::Plane3<double>,Imath_3_1::Line3<double>,Imath_3_1::Vec3<double> {lvalue})

intersect( (Plane3d)arg1, (Line3f)arg2) -> object :
    pl.intersect(ln) -- returns the point where plane
    pl and line ln intersect, or None if pl and ln do
    not intersect

    C++ signature :
        boost::python::api::object intersect(Imath_3_1::Plane3<double>,Imath_3_1::Line3<float>)

intersect( (Plane3d)arg1, (Line3d)arg2) -> object :
    pl.intersect(ln) -- returns the point where plane
    pl and line ln intersect, or None if pl and ln do
    not intersect

    C++ signature :
        boost::python::api::object intersect(Imath_3_1::Plane3<double>,Imath_3_1::Line3<double>)'''
    ...
    def intersectT (self, *args, **kwargs):
      '''
intersectT( (Plane3d)arg1, (Line3f)arg2) -> object :
    pl.intersectT(ln) -- computes the intersection,
    i, of plane pl and line ln, and returns t, so that
    ln.pos() + t * ln.dir() == i.
    If pl and ln do not intersect, pl.intersectT(ln)
    returns None.
    

    C++ signature :
        boost::python::api::object intersectT(Imath_3_1::Plane3<double>,Imath_3_1::Line3<float>)

intersectT( (Plane3d)arg1, (Line3d)arg2) -> object :

    C++ signature :
        boost::python::api::object intersectT(Imath_3_1::Plane3<double>,Imath_3_1::Line3<double>)'''
    ...
    def normal (self, *args, **kwargs):
      '''
normal( (Plane3d)arg1) -> V3d :
    normal()

    C++ signature :
        Imath_3_1::Vec3<double> normal(Imath_3_1::Plane3<double> {lvalue})'''
    ...
    def reflectPoint (self, *args, **kwargs):
      '''
reflectPoint( (Plane3d)arg1, (V3d)arg2) -> V3d :
    reflectPoint()

    C++ signature :
        Imath_3_1::Vec3<double> reflectPoint(Imath_3_1::Plane3<double> {lvalue},Imath_3_1::Vec3<double>)

reflectPoint( (Plane3d)arg1, (tuple)arg2) -> V3d :

    C++ signature :
        Imath_3_1::Vec3<double> reflectPoint(Imath_3_1::Plane3<double> {lvalue},boost::python::tuple)'''
    ...
    def reflectVector (self, *args, **kwargs):
      '''
reflectVector( (Plane3d)arg1, (V3d)arg2) -> V3d :
    reflectVector()

    C++ signature :
        Imath_3_1::Vec3<double> reflectVector(Imath_3_1::Plane3<double> {lvalue},Imath_3_1::Vec3<double>)

reflectVector( (Plane3d)arg1, (tuple)arg2) -> V3d :

    C++ signature :
        Imath_3_1::Vec3<double> reflectVector(Imath_3_1::Plane3<double> {lvalue},boost::python::tuple)'''
    ...
    def set (self, *args, **kwargs):
      '''
set( (Plane3d)arg1, (V3d)arg2, (float)arg3) -> None :
    set()

    C++ signature :
        void set(Imath_3_1::Plane3<double> {lvalue},Imath_3_1::Vec3<double>,double)

set( (Plane3d)arg1, (V3d)arg2, (V3d)arg3) -> None :
    set()

    C++ signature :
        void set(Imath_3_1::Plane3<double> {lvalue},Imath_3_1::Vec3<double>,Imath_3_1::Vec3<double>)

set( (Plane3d)arg1, (V3d)arg2, (V3d)arg3, (V3d)arg4) -> None :
    set()

    C++ signature :
        void set(Imath_3_1::Plane3<double> {lvalue},Imath_3_1::Vec3<double>,Imath_3_1::Vec3<double>,Imath_3_1::Vec3<double>)

set( (Plane3d)arg1, (tuple)arg2, (float)arg3) -> None :
    set()

    C++ signature :
        void set(Imath_3_1::Plane3<double> {lvalue},boost::python::tuple,double)

set( (Plane3d)arg1, (tuple)arg2, (tuple)arg3) -> None :
    set()

    C++ signature :
        void set(Imath_3_1::Plane3<double> {lvalue},boost::python::tuple,boost::python::tuple)

set( (Plane3d)arg1, (tuple)arg2, (tuple)arg3, (tuple)arg4) -> None :
    set()

    C++ signature :
        void set(Imath_3_1::Plane3<double> {lvalue},boost::python::tuple,boost::python::tuple,boost::python::tuple)'''
    ...
    def setDistance (self, *args, **kwargs):
      '''
setDistance( (Plane3d)arg1, (float)arg2) -> None :
    setDistance()

    C++ signature :
        void setDistance(Imath_3_1::Plane3<double> {lvalue},double)'''
    ...
    def setNormal (self, *args, **kwargs):
      '''
setNormal( (Plane3d)arg1, (V3d)arg2) -> None :
    setNormal()

    C++ signature :
        void setNormal(Imath_3_1::Plane3<double> {lvalue},Imath_3_1::Vec3<double>)'''
    ...

def Plane3f (*args):
      '''
__init__(_object*, Imath_3_1::Vec3<float>, Imath_3_1::Vec3<float>, Imath_3_1::Vec3<float>)
__init__(_object*, Imath_3_1::Vec3<float>, Imath_3_1::Vec3<float>)
__init__(_object*, Imath_3_1::Vec3<float>, float)
__init__(boost::python::api::object, boost::python::api::object)
__init__(boost::python::api::object, boost::python::tuple, boost::python::tuple, boost::python::tuple)
__init__(boost::python::api::object, boost::python::tuple, boost::python::tuple)
__init__(boost::python::api::object, boost::python::tuple, float)
__init__(boost::python::api::object)
__init__(_object*)

'''      
    ...

class Plane3f:
    def distance (self, *args, **kwargs):
      '''
distance( (Plane3f)arg1) -> float :
    distance()

    C++ signature :
        float distance(Imath_3_1::Plane3<float> {lvalue})'''
    ...
    def distanceTo (self, *args, **kwargs):
      '''
distanceTo( (Plane3f)arg1, (V3f)arg2) -> float :
    distanceTo()

    C++ signature :
        float distanceTo(Imath_3_1::Plane3<float> {lvalue},Imath_3_1::Vec3<float>)

distanceTo( (Plane3f)arg1, (tuple)arg2) -> float :

    C++ signature :
        float distanceTo(Imath_3_1::Plane3<float> {lvalue},boost::python::tuple)'''
    ...
    def intersect (self, *args, **kwargs):
      '''
intersect( (Plane3f)arg1, (Line3f)arg2, (V3f)arg3) -> bool :
    pl.intersect(ln, pt) -- returns true if the line intersects
    the plane, false if it doesn't.  The point where plane
    pl and line ln intersect is stored in pt

    C++ signature :
        bool intersect(Imath_3_1::Plane3<float>,Imath_3_1::Line3<float>,Imath_3_1::Vec3<float> {lvalue})

intersect( (Plane3f)arg1, (Line3f)arg2) -> object :
    pl.intersect(ln) -- returns the point where plane
    pl and line ln intersect, or None if pl and ln do
    not intersect

    C++ signature :
        boost::python::api::object intersect(Imath_3_1::Plane3<float>,Imath_3_1::Line3<float>)

intersect( (Plane3f)arg1, (Line3d)arg2) -> object :
    pl.intersect(ln) -- returns the point where plane
    pl and line ln intersect, or None if pl and ln do
    not intersect

    C++ signature :
        boost::python::api::object intersect(Imath_3_1::Plane3<float>,Imath_3_1::Line3<double>)'''
    ...
    def intersectT (self, *args, **kwargs):
      '''
intersectT( (Plane3f)arg1, (Line3f)arg2) -> object :
    pl.intersectT(ln) -- computes the intersection,
    i, of plane pl and line ln, and returns t, so that
    ln.pos() + t * ln.dir() == i.
    If pl and ln do not intersect, pl.intersectT(ln)
    returns None.
    

    C++ signature :
        boost::python::api::object intersectT(Imath_3_1::Plane3<float>,Imath_3_1::Line3<float>)

intersectT( (Plane3f)arg1, (Line3d)arg2) -> object :

    C++ signature :
        boost::python::api::object intersectT(Imath_3_1::Plane3<float>,Imath_3_1::Line3<double>)'''
    ...
    def normal (self, *args, **kwargs):
      '''
normal( (Plane3f)arg1) -> V3f :
    normal()

    C++ signature :
        Imath_3_1::Vec3<float> normal(Imath_3_1::Plane3<float> {lvalue})'''
    ...
    def reflectPoint (self, *args, **kwargs):
      '''
reflectPoint( (Plane3f)arg1, (V3f)arg2) -> V3f :
    reflectPoint()

    C++ signature :
        Imath_3_1::Vec3<float> reflectPoint(Imath_3_1::Plane3<float> {lvalue},Imath_3_1::Vec3<float>)

reflectPoint( (Plane3f)arg1, (tuple)arg2) -> V3f :

    C++ signature :
        Imath_3_1::Vec3<float> reflectPoint(Imath_3_1::Plane3<float> {lvalue},boost::python::tuple)'''
    ...
    def reflectVector (self, *args, **kwargs):
      '''
reflectVector( (Plane3f)arg1, (V3f)arg2) -> V3f :
    reflectVector()

    C++ signature :
        Imath_3_1::Vec3<float> reflectVector(Imath_3_1::Plane3<float> {lvalue},Imath_3_1::Vec3<float>)

reflectVector( (Plane3f)arg1, (tuple)arg2) -> V3f :

    C++ signature :
        Imath_3_1::Vec3<float> reflectVector(Imath_3_1::Plane3<float> {lvalue},boost::python::tuple)'''
    ...
    def set (self, *args, **kwargs):
      '''
set( (Plane3f)arg1, (V3f)arg2, (float)arg3) -> None :
    set()

    C++ signature :
        void set(Imath_3_1::Plane3<float> {lvalue},Imath_3_1::Vec3<float>,float)

set( (Plane3f)arg1, (V3f)arg2, (V3f)arg3) -> None :
    set()

    C++ signature :
        void set(Imath_3_1::Plane3<float> {lvalue},Imath_3_1::Vec3<float>,Imath_3_1::Vec3<float>)

set( (Plane3f)arg1, (V3f)arg2, (V3f)arg3, (V3f)arg4) -> None :
    set()

    C++ signature :
        void set(Imath_3_1::Plane3<float> {lvalue},Imath_3_1::Vec3<float>,Imath_3_1::Vec3<float>,Imath_3_1::Vec3<float>)

set( (Plane3f)arg1, (tuple)arg2, (float)arg3) -> None :
    set()

    C++ signature :
        void set(Imath_3_1::Plane3<float> {lvalue},boost::python::tuple,float)

set( (Plane3f)arg1, (tuple)arg2, (tuple)arg3) -> None :
    set()

    C++ signature :
        void set(Imath_3_1::Plane3<float> {lvalue},boost::python::tuple,boost::python::tuple)

set( (Plane3f)arg1, (tuple)arg2, (tuple)arg3, (tuple)arg4) -> None :
    set()

    C++ signature :
        void set(Imath_3_1::Plane3<float> {lvalue},boost::python::tuple,boost::python::tuple,boost::python::tuple)'''
    ...
    def setDistance (self, *args, **kwargs):
      '''
setDistance( (Plane3f)arg1, (float)arg2) -> None :
    setDistance()

    C++ signature :
        void setDistance(Imath_3_1::Plane3<float> {lvalue},float)'''
    ...
    def setNormal (self, *args, **kwargs):
      '''
setNormal( (Plane3f)arg1, (V3f)arg2) -> None :
    setNormal()

    C++ signature :
        void setNormal(Imath_3_1::Plane3<float> {lvalue},Imath_3_1::Vec3<float>)'''
    ...

def Quatd (*args):
      '''
__init__(boost::python::api::object, Imath_3_1::Matrix44<double>)
__init__(boost::python::api::object, Imath_3_1::Matrix33<double>)
__init__(boost::python::api::object, Imath_3_1::Euler<double>)
__init__(_object*, double, Imath_3_1::Vec3<double>)
__init__(_object*, double, double, double, double)
__init__(_object*, Imath_3_1::Quat<double>)
__init__(_object*, Imath_3_1::Quat<float>)
__init__(_object*)
__init__(_object*, Imath_3_1::Quat<double>)

'''      
    ...

class Quatd:
    def angle (self, *args, **kwargs):
      '''
angle( (Quatd)arg1) -> float :
    q.angle() -- returns the rotation angle
    (in radians) represented by quaternion q

    C++ signature :
        double angle(Imath_3_1::Quat<double> {lvalue})'''
    ...
    def axis (self, *args, **kwargs):
      '''
axis( (Quatd)arg1) -> V3d :
    q.axis() -- returns the rotation axis
    represented by quaternion q

    C++ signature :
        Imath_3_1::Vec3<double> axis(Imath_3_1::Quat<double> {lvalue})'''
    ...
    def exp (self, *args, **kwargs):
      '''
exp( (Quatd)arg1) -> Quatd :

    C++ signature :
        Imath_3_1::Quat<double> exp(Imath_3_1::Quat<double> {lvalue})'''
    ...
    def extract (self, *args, **kwargs):
      '''
extract( (Quatd)arg1, (M44d)arg2) -> None :
    q.extract(m) -- extracts the rotation component
    from 4x4 matrix m and stores the result in q

    C++ signature :
        void extract(Imath_3_1::Quat<double> {lvalue},Imath_3_1::Matrix44<double>)'''
    ...
    def identity (self, *args, **kwargs):
      '''
identity() -> Quatd :

    C++ signature :
        Imath_3_1::Quat<double> identity()'''
    ...
    def inverse (self, *args, **kwargs):
      '''
inverse( (Quatd)arg1) -> Quatd :
    q.inverse() -- returns the inverse of
    quaternion q; q is not modified
    

    C++ signature :
        Imath_3_1::Quat<double> inverse(Imath_3_1::Quat<double> {lvalue})'''
    ...
    def invert (self, *args, **kwargs):
      '''
invert( (Quatd)arg1) -> Quatd :
    q.invert() -- inverts quaternion q
    (modifying q); returns q

    C++ signature :
        Imath_3_1::Quat<double> {lvalue} invert(Imath_3_1::Quat<double> {lvalue})'''
    ...
    def length (self, *args, **kwargs):
      '''
length( (Quatd)arg1) -> float :

    C++ signature :
        double length(Imath_3_1::Quat<double> {lvalue})'''
    ...
    def log (self, *args, **kwargs):
      '''
log( (Quatd)arg1) -> Quatd :

    C++ signature :
        Imath_3_1::Quat<double> log(Imath_3_1::Quat<double> {lvalue})'''
    ...
    def normalize (self, *args, **kwargs):
      '''
normalize( (Quatd)arg1) -> Quatd :
    q.normalize() -- normalizes quaternion q
    (modifying q); returns q

    C++ signature :
        Imath_3_1::Quat<double> {lvalue} normalize(Imath_3_1::Quat<double> {lvalue})'''
    ...
    def normalized (self, *args, **kwargs):
      '''
normalized( (Quatd)arg1) -> Quatd :
    q.normalized() -- returns a normalized version
    of quaternion q; q is not modified
    

    C++ signature :
        Imath_3_1::Quat<double> normalized(Imath_3_1::Quat<double> {lvalue})'''
    ...
    def r (self, *args, **kwargs):
      '''
r( (Quatd)arg1) -> float :
    q.r() -- returns the r (scalar) component
    of quaternion q

    C++ signature :
        double r(Imath_3_1::Quat<double> {lvalue})'''
    ...
    def rotateVector (self, *args, **kwargs):
      '''
rotateVector( (Quatd)arg1, (V3d)arg2) -> V3d :
    q.rotateVector(orig) -- Given a vector orig,
       calculate orig' = q x orig x q*
    
       Assumes unit quaternions

    C++ signature :
        Imath_3_1::Vec3<double> rotateVector(Imath_3_1::Quat<double>,Imath_3_1::Vec3<double>)'''
    ...
    def setAxisAngle (self, *args, **kwargs):
      '''
setAxisAngle( (Quatd)arg1, (V3d)arg2, (float)arg3) -> Quatd :
    q.setAxisAngle(x,r) -- sets the value of
    quaternion q so that q represents a rotation
    of r radians around axis x

    C++ signature :
        Imath_3_1::Quat<double> {lvalue} setAxisAngle(Imath_3_1::Quat<double> {lvalue},Imath_3_1::Vec3<double>,double)'''
    ...
    def setR (self, *args, **kwargs):
      '''
setR( (Quatd)arg1, (float)arg2) -> None :
    q.setR(s) -- sets the r (scalar) component
    of quaternion q to s

    C++ signature :
        void setR(Imath_3_1::Quat<double> {lvalue},double)'''
    ...
    def setRotation (self, *args, **kwargs):
      '''
setRotation( (Quatd)arg1, (V3d)arg2, (V3d)arg3) -> Quatd :
    q.setRotation(v,w) -- sets the value of
    quaternion q so that rotating vector v by
    q produces vector w

    C++ signature :
        Imath_3_1::Quat<double> {lvalue} setRotation(Imath_3_1::Quat<double> {lvalue},Imath_3_1::Vec3<double>,Imath_3_1::Vec3<double>)'''
    ...
    def setV (self, *args, **kwargs):
      '''
setV( (Quatd)arg1, (V3d)arg2) -> None :
    q.setV(w) -- sets the v (vector) component
    of quaternion q to w

    C++ signature :
        void setV(Imath_3_1::Quat<double> {lvalue},Imath_3_1::Vec3<double>)'''
    ...
    def slerp (self, *args, **kwargs):
      '''
slerp( (Quatd)arg1, (Quatd)arg2, (float)arg3) -> Quatd :
    q.slerp(p,t) -- performs sperical linear
    interpolation between quaternions q and p:
    q.slerp(p,0) returns q; q.slerp(p,1) returns p.
    q and p must be normalized
    

    C++ signature :
        Imath_3_1::Quat<double> slerp(Imath_3_1::Quat<double>,Imath_3_1::Quat<double>,double)'''
    ...
    def slerpShortestArc (self, *args, **kwargs):
      '''
slerpShortestArc( (Quatd)arg1, (Quatd)arg2, (float)arg3) -> Quatd :
    q.slerpShortestArc(p,t) -- performs spherical linear
    interpolation along the shortest arc between
    quaternions q and either p or -p, whichever is
    closer. q and p must be normalized
    

    C++ signature :
        Imath_3_1::Quat<double> slerpShortestArc(Imath_3_1::Quat<double>,Imath_3_1::Quat<double>,double)'''
    ...
    def toMatrix33 (self, *args, **kwargs):
      '''
toMatrix33( (Quatd)arg1) -> M33d :
    q.toMatrix33() -- returns a 3x3 matrix that
    represents the same rotation as quaternion q

    C++ signature :
        Imath_3_1::Matrix33<double> toMatrix33(Imath_3_1::Quat<double> {lvalue})'''
    ...
    def toMatrix44 (self, *args, **kwargs):
      '''
toMatrix44( (Quatd)arg1) -> M44d :
    q.toMatrix44() -- returns a 4x4 matrix that
    represents the same rotation as quaternion q

    C++ signature :
        Imath_3_1::Matrix44<double> toMatrix44(Imath_3_1::Quat<double> {lvalue})'''
    ...
    def v (self, *args, **kwargs):
      '''
v( (Quatd)arg1) -> V3d :
    q.v() -- returns the v (vector) component
    of quaternion q

    C++ signature :
        Imath_3_1::Vec3<double> v(Imath_3_1::Quat<double> {lvalue})'''
    ...

def QuatdArray (*args):
      '''
__init__(_object*, PyImath::FixedArray<Imath_3_1::Quat<float> >)
__init__(boost::python::api::object, PyImath::FixedArray<Imath_3_1::Euler<double> >)
__init__(_object*, Imath_3_1::Quat<double>, unsigned long)
__init__(_object*, PyImath::FixedArray<Imath_3_1::Quat<double> >)
__init__(_object*, unsigned long)

'''      
    ...

class QuatdArray:
    def angle (self, *args, **kwargs):
      '''
angle( (QuatdArray)arg1) -> DoubleArray :
    get rotation angle about the axis returned by axis() for each quat

    C++ signature :
        PyImath::FixedArray<double> angle(PyImath::FixedArray<Imath_3_1::Quat<double> >)'''
    ...
    def axis (self, *args, **kwargs):
      '''
axis( (QuatdArray)arg1) -> V3dArray :
    get rotation axis for each quat

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec3<double> > axis(PyImath::FixedArray<Imath_3_1::Quat<double> >)'''
    ...
    def dot (self, *args, **kwargs):
      '''
dot( (QuatdArray)arg1, (Quatd)qB) -> DoubleArray :
    dot(qB) - Return the element-by-element Euclidean inner product

    C++ signature :
        PyImath::FixedArray<double> dot(PyImath::FixedArray<Imath_3_1::Quat<double> >,Imath_3_1::Quat<double>)

dot( (QuatdArray)arg1, (QuatdArray)qB) -> DoubleArray :
    dot(qB) - Return the element-by-element Euclidean inner product

    C++ signature :
        PyImath::FixedArray<double> dot(PyImath::FixedArray<Imath_3_1::Quat<double> >,PyImath::FixedArray<Imath_3_1::Quat<double> >)'''
    ...
    def euclideanInnerProduct (self, *args, **kwargs):
      '''
euclideanInnerProduct( (QuatdArray)arg1, (Quatd)qB) -> DoubleArray :
    euclideanInnerProduct(qB) - Return the element-by-element Euclidean inner product

    C++ signature :
        PyImath::FixedArray<double> euclideanInnerProduct(PyImath::FixedArray<Imath_3_1::Quat<double> >,Imath_3_1::Quat<double>)

euclideanInnerProduct( (QuatdArray)arg1, (QuatdArray)qB) -> DoubleArray :
    euclideanInnerProduct(qB) - Return the element-by-element Euclidean inner product

    C++ signature :
        PyImath::FixedArray<double> euclideanInnerProduct(PyImath::FixedArray<Imath_3_1::Quat<double> >,PyImath::FixedArray<Imath_3_1::Quat<double> >)'''
    ...
    def extract (self, *args, **kwargs):
      '''
extract( (QuatdArray)arg1, (M44dArray)lxform) -> None :
    Extract the rotation component of an M44d and return it as a quaternion.

    C++ signature :
        void extract(PyImath::FixedArray<Imath_3_1::Quat<double> > {lvalue},PyImath::FixedArray<Imath_3_1::Matrix44<double> >)'''
    ...
    def ifelse (self, *args, **kwargs):
      '''
ifelse( (QuatdArray)arg1, (IntArray)arg2, (Quatd)arg3) -> QuatdArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Quat<double> > ifelse(PyImath::FixedArray<Imath_3_1::Quat<double> > {lvalue},PyImath::FixedArray<int>,Imath_3_1::Quat<double>)

ifelse( (QuatdArray)arg1, (IntArray)arg2, (QuatdArray)arg3) -> QuatdArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Quat<double> > ifelse(PyImath::FixedArray<Imath_3_1::Quat<double> > {lvalue},PyImath::FixedArray<int>,PyImath::FixedArray<Imath_3_1::Quat<double> >)'''
    ...
    def inverse (self, *args, **kwargs):
      '''
inverse( (QuatdArray)QuatArray) -> QuatdArray :
    Return 1/Q for each quaternion.

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Quat<double> > inverse(PyImath::FixedArray<Imath_3_1::Quat<double> >)'''
    ...
    def makeReadOnly (self, *args, **kwargs):
      '''
makeReadOnly( (QuatdArray)arg1) -> None :

    C++ signature :
        void makeReadOnly(PyImath::FixedArray<Imath_3_1::Quat<double> > {lvalue})'''
    ...
    def normalize (self, *args, **kwargs):
      '''
normalize( (QuatdArray)arg1) -> QuatdArray :
    Normalize each quaternion in the array

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Quat<double> > {lvalue} normalize(PyImath::FixedArray<Imath_3_1::Quat<double> > {lvalue})'''
    ...
    def normalized (self, *args, **kwargs):
      '''
normalized( (QuatdArray)arg1) -> QuatdArray :
    Return a new quaternion array with unit quaternions.

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Quat<double> > normalized(PyImath::FixedArray<Imath_3_1::Quat<double> >)'''
    ...
    def orientToVectors (self, *args, **kwargs):
      '''
orientToVectors( (QuatdArray)arg1, (V3dArray)forward, (V3dArray)up, (bool)alignForward) -> None :
    Sets the orientations to match the given forward and up vectors, matching the forward vector exactly if 'alignForward' is True, matching the up vector exactly if 'alignForward' is False.  If the vectors are already orthogonal, both vectors will be matched exactly.

    C++ signature :
        void orientToVectors(PyImath::FixedArray<Imath_3_1::Quat<double> > {lvalue},PyImath::FixedArray<Imath_3_1::Vec3<double> >,PyImath::FixedArray<Imath_3_1::Vec3<double> >,bool)'''
    ...
    def r (self, *args, **kwargs):
      '''None'''
    ...
    def rotateVector (self, *args, **kwargs):
      '''
rotateVector( (QuatdArray)arg1, (V3dArray)vector) -> V3dArray :
    Rotate the supplied vectors by the quaternions.  Assumes quaternions are normalized.

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec3<double> > rotateVector(PyImath::FixedArray<Imath_3_1::Quat<double> >,PyImath::FixedArray<Imath_3_1::Vec3<double> >)'''
    ...
    def setAxisAngle (self, *args, **kwargs):
      '''
setAxisAngle( (QuatdArray)arg1, (V3dArray)axis, (DoubleArray)angle) -> QuatdArray :
    set the quaternion arrays from a given axis and angle

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Quat<double> > {lvalue} setAxisAngle(PyImath::FixedArray<Imath_3_1::Quat<double> > {lvalue},PyImath::FixedArray<Imath_3_1::Vec3<double> >,PyImath::FixedArray<double>)'''
    ...
    def setEulerXYZ (self, *args, **kwargs):
      '''
setEulerXYZ( (QuatdArray)arg1, (V3dArray)euler) -> None :
    set the quaternion arrays from a given euler XYZ angle vector

    C++ signature :
        void setEulerXYZ(PyImath::FixedArray<Imath_3_1::Quat<double> > {lvalue},PyImath::FixedArray<Imath_3_1::Vec3<double> >)'''
    ...
    def setRotation (self, *args, **kwargs):
      '''
setRotation( (QuatdArray)arg1, (V3dArray)from, (V3dArray)to) -> None :
    set rotation angles for each quat

    C++ signature :
        void setRotation(PyImath::FixedArray<Imath_3_1::Quat<double> > {lvalue},PyImath::FixedArray<Imath_3_1::Vec3<double> >,PyImath::FixedArray<Imath_3_1::Vec3<double> >)'''
    ...
    def slerp (self, *args, **kwargs):
      '''
slerp( (QuatdArray)arg1, (Quatd)qB, (float)t) -> QuatdArray :
    slerp(qB,t) - Return the element-by-element shortest arc spherical linear interpolation between self and B.

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Quat<double> > slerp(PyImath::FixedArray<Imath_3_1::Quat<double> >,Imath_3_1::Quat<double>,double)

slerp( (QuatdArray)arg1, (QuatdArray)qB, (float)t) -> QuatdArray :
    slerp(qB,t) - Return the element-by-element shortest arc spherical linear interpolation between self and B.

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Quat<double> > slerp(PyImath::FixedArray<Imath_3_1::Quat<double> >,PyImath::FixedArray<Imath_3_1::Quat<double> >,double)'''
    ...
    def writable (self, *args, **kwargs):
      '''
writable( (QuatdArray)arg1) -> bool :

    C++ signature :
        bool writable(PyImath::FixedArray<Imath_3_1::Quat<double> > {lvalue})'''
    ...
    def x (self, *args, **kwargs):
      '''None'''
    ...
    def y (self, *args, **kwargs):
      '''None'''
    ...
    def z (self, *args, **kwargs):
      '''None'''
    ...

def Quatf (*args):
      '''
__init__(boost::python::api::object, Imath_3_1::Matrix44<float>)
__init__(boost::python::api::object, Imath_3_1::Matrix33<float>)
__init__(boost::python::api::object, Imath_3_1::Euler<float>)
__init__(_object*, float, Imath_3_1::Vec3<float>)
__init__(_object*, float, float, float, float)
__init__(_object*, Imath_3_1::Quat<double>)
__init__(_object*, Imath_3_1::Quat<float>)
__init__(_object*)
__init__(_object*, Imath_3_1::Quat<float>)

'''      
    ...

class Quatf:
    def angle (self, *args, **kwargs):
      '''
angle( (Quatf)arg1) -> float :
    q.angle() -- returns the rotation angle
    (in radians) represented by quaternion q

    C++ signature :
        float angle(Imath_3_1::Quat<float> {lvalue})'''
    ...
    def axis (self, *args, **kwargs):
      '''
axis( (Quatf)arg1) -> V3f :
    q.axis() -- returns the rotation axis
    represented by quaternion q

    C++ signature :
        Imath_3_1::Vec3<float> axis(Imath_3_1::Quat<float> {lvalue})'''
    ...
    def exp (self, *args, **kwargs):
      '''
exp( (Quatf)arg1) -> Quatf :

    C++ signature :
        Imath_3_1::Quat<float> exp(Imath_3_1::Quat<float> {lvalue})'''
    ...
    def extract (self, *args, **kwargs):
      '''
extract( (Quatf)arg1, (M44f)arg2) -> None :
    q.extract(m) -- extracts the rotation component
    from 4x4 matrix m and stores the result in q

    C++ signature :
        void extract(Imath_3_1::Quat<float> {lvalue},Imath_3_1::Matrix44<float>)'''
    ...
    def identity (self, *args, **kwargs):
      '''
identity() -> Quatf :

    C++ signature :
        Imath_3_1::Quat<float> identity()'''
    ...
    def inverse (self, *args, **kwargs):
      '''
inverse( (Quatf)arg1) -> Quatf :
    q.inverse() -- returns the inverse of
    quaternion q; q is not modified
    

    C++ signature :
        Imath_3_1::Quat<float> inverse(Imath_3_1::Quat<float> {lvalue})'''
    ...
    def invert (self, *args, **kwargs):
      '''
invert( (Quatf)arg1) -> Quatf :
    q.invert() -- inverts quaternion q
    (modifying q); returns q

    C++ signature :
        Imath_3_1::Quat<float> {lvalue} invert(Imath_3_1::Quat<float> {lvalue})'''
    ...
    def length (self, *args, **kwargs):
      '''
length( (Quatf)arg1) -> float :

    C++ signature :
        float length(Imath_3_1::Quat<float> {lvalue})'''
    ...
    def log (self, *args, **kwargs):
      '''
log( (Quatf)arg1) -> Quatf :

    C++ signature :
        Imath_3_1::Quat<float> log(Imath_3_1::Quat<float> {lvalue})'''
    ...
    def normalize (self, *args, **kwargs):
      '''
normalize( (Quatf)arg1) -> Quatf :
    q.normalize() -- normalizes quaternion q
    (modifying q); returns q

    C++ signature :
        Imath_3_1::Quat<float> {lvalue} normalize(Imath_3_1::Quat<float> {lvalue})'''
    ...
    def normalized (self, *args, **kwargs):
      '''
normalized( (Quatf)arg1) -> Quatf :
    q.normalized() -- returns a normalized version
    of quaternion q; q is not modified
    

    C++ signature :
        Imath_3_1::Quat<float> normalized(Imath_3_1::Quat<float> {lvalue})'''
    ...
    def r (self, *args, **kwargs):
      '''
r( (Quatf)arg1) -> float :
    q.r() -- returns the r (scalar) component
    of quaternion q

    C++ signature :
        float r(Imath_3_1::Quat<float> {lvalue})'''
    ...
    def rotateVector (self, *args, **kwargs):
      '''
rotateVector( (Quatf)arg1, (V3f)arg2) -> V3f :
    q.rotateVector(orig) -- Given a vector orig,
       calculate orig' = q x orig x q*
    
       Assumes unit quaternions

    C++ signature :
        Imath_3_1::Vec3<float> rotateVector(Imath_3_1::Quat<float>,Imath_3_1::Vec3<float>)'''
    ...
    def setAxisAngle (self, *args, **kwargs):
      '''
setAxisAngle( (Quatf)arg1, (V3f)arg2, (float)arg3) -> Quatf :
    q.setAxisAngle(x,r) -- sets the value of
    quaternion q so that q represents a rotation
    of r radians around axis x

    C++ signature :
        Imath_3_1::Quat<float> {lvalue} setAxisAngle(Imath_3_1::Quat<float> {lvalue},Imath_3_1::Vec3<float>,float)'''
    ...
    def setR (self, *args, **kwargs):
      '''
setR( (Quatf)arg1, (float)arg2) -> None :
    q.setR(s) -- sets the r (scalar) component
    of quaternion q to s

    C++ signature :
        void setR(Imath_3_1::Quat<float> {lvalue},double)'''
    ...
    def setRotation (self, *args, **kwargs):
      '''
setRotation( (Quatf)arg1, (V3f)arg2, (V3f)arg3) -> Quatf :
    q.setRotation(v,w) -- sets the value of
    quaternion q so that rotating vector v by
    q produces vector w

    C++ signature :
        Imath_3_1::Quat<float> {lvalue} setRotation(Imath_3_1::Quat<float> {lvalue},Imath_3_1::Vec3<float>,Imath_3_1::Vec3<float>)'''
    ...
    def setV (self, *args, **kwargs):
      '''
setV( (Quatf)arg1, (V3f)arg2) -> None :
    q.setV(w) -- sets the v (vector) component
    of quaternion q to w

    C++ signature :
        void setV(Imath_3_1::Quat<float> {lvalue},Imath_3_1::Vec3<float>)'''
    ...
    def slerp (self, *args, **kwargs):
      '''
slerp( (Quatf)arg1, (Quatf)arg2, (float)arg3) -> Quatf :
    q.slerp(p,t) -- performs sperical linear
    interpolation between quaternions q and p:
    q.slerp(p,0) returns q; q.slerp(p,1) returns p.
    q and p must be normalized
    

    C++ signature :
        Imath_3_1::Quat<float> slerp(Imath_3_1::Quat<float>,Imath_3_1::Quat<float>,float)'''
    ...
    def slerpShortestArc (self, *args, **kwargs):
      '''
slerpShortestArc( (Quatf)arg1, (Quatf)arg2, (float)arg3) -> Quatf :
    q.slerpShortestArc(p,t) -- performs spherical linear
    interpolation along the shortest arc between
    quaternions q and either p or -p, whichever is
    closer. q and p must be normalized
    

    C++ signature :
        Imath_3_1::Quat<float> slerpShortestArc(Imath_3_1::Quat<float>,Imath_3_1::Quat<float>,float)'''
    ...
    def toMatrix33 (self, *args, **kwargs):
      '''
toMatrix33( (Quatf)arg1) -> M33f :
    q.toMatrix33() -- returns a 3x3 matrix that
    represents the same rotation as quaternion q

    C++ signature :
        Imath_3_1::Matrix33<float> toMatrix33(Imath_3_1::Quat<float> {lvalue})'''
    ...
    def toMatrix44 (self, *args, **kwargs):
      '''
toMatrix44( (Quatf)arg1) -> M44f :
    q.toMatrix44() -- returns a 4x4 matrix that
    represents the same rotation as quaternion q

    C++ signature :
        Imath_3_1::Matrix44<float> toMatrix44(Imath_3_1::Quat<float> {lvalue})'''
    ...
    def v (self, *args, **kwargs):
      '''
v( (Quatf)arg1) -> V3f :
    q.v() -- returns the v (vector) component
    of quaternion q

    C++ signature :
        Imath_3_1::Vec3<float> v(Imath_3_1::Quat<float> {lvalue})'''
    ...

def QuatfArray (*args):
      '''
__init__(_object*, PyImath::FixedArray<Imath_3_1::Quat<double> >)
__init__(boost::python::api::object, PyImath::FixedArray<Imath_3_1::Euler<float> >)
__init__(_object*, Imath_3_1::Quat<float>, unsigned long)
__init__(_object*, PyImath::FixedArray<Imath_3_1::Quat<float> >)
__init__(_object*, unsigned long)

'''      
    ...

class QuatfArray:
    def angle (self, *args, **kwargs):
      '''
angle( (QuatfArray)arg1) -> FloatArray :
    get rotation angle about the axis returned by axis() for each quat

    C++ signature :
        PyImath::FixedArray<float> angle(PyImath::FixedArray<Imath_3_1::Quat<float> >)'''
    ...
    def axis (self, *args, **kwargs):
      '''
axis( (QuatfArray)arg1) -> V3fArray :
    get rotation axis for each quat

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec3<float> > axis(PyImath::FixedArray<Imath_3_1::Quat<float> >)'''
    ...
    def dot (self, *args, **kwargs):
      '''
dot( (QuatfArray)arg1, (Quatf)qB) -> FloatArray :
    dot(qB) - Return the element-by-element Euclidean inner product

    C++ signature :
        PyImath::FixedArray<float> dot(PyImath::FixedArray<Imath_3_1::Quat<float> >,Imath_3_1::Quat<float>)

dot( (QuatfArray)arg1, (QuatfArray)qB) -> FloatArray :
    dot(qB) - Return the element-by-element Euclidean inner product

    C++ signature :
        PyImath::FixedArray<float> dot(PyImath::FixedArray<Imath_3_1::Quat<float> >,PyImath::FixedArray<Imath_3_1::Quat<float> >)'''
    ...
    def euclideanInnerProduct (self, *args, **kwargs):
      '''
euclideanInnerProduct( (QuatfArray)arg1, (Quatf)qB) -> FloatArray :
    euclideanInnerProduct(qB) - Return the element-by-element Euclidean inner product

    C++ signature :
        PyImath::FixedArray<float> euclideanInnerProduct(PyImath::FixedArray<Imath_3_1::Quat<float> >,Imath_3_1::Quat<float>)

euclideanInnerProduct( (QuatfArray)arg1, (QuatfArray)qB) -> FloatArray :
    euclideanInnerProduct(qB) - Return the element-by-element Euclidean inner product

    C++ signature :
        PyImath::FixedArray<float> euclideanInnerProduct(PyImath::FixedArray<Imath_3_1::Quat<float> >,PyImath::FixedArray<Imath_3_1::Quat<float> >)'''
    ...
    def extract (self, *args, **kwargs):
      '''
extract( (QuatfArray)arg1, (M44dArray)lxform) -> None :
    Extract the rotation component of an M44d and return it as a quaternion.

    C++ signature :
        void extract(PyImath::FixedArray<Imath_3_1::Quat<float> > {lvalue},PyImath::FixedArray<Imath_3_1::Matrix44<double> >)'''
    ...
    def ifelse (self, *args, **kwargs):
      '''
ifelse( (QuatfArray)arg1, (IntArray)arg2, (Quatf)arg3) -> QuatfArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Quat<float> > ifelse(PyImath::FixedArray<Imath_3_1::Quat<float> > {lvalue},PyImath::FixedArray<int>,Imath_3_1::Quat<float>)

ifelse( (QuatfArray)arg1, (IntArray)arg2, (QuatfArray)arg3) -> QuatfArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Quat<float> > ifelse(PyImath::FixedArray<Imath_3_1::Quat<float> > {lvalue},PyImath::FixedArray<int>,PyImath::FixedArray<Imath_3_1::Quat<float> >)'''
    ...
    def inverse (self, *args, **kwargs):
      '''
inverse( (QuatfArray)QuatArray) -> QuatfArray :
    Return 1/Q for each quaternion.

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Quat<float> > inverse(PyImath::FixedArray<Imath_3_1::Quat<float> >)'''
    ...
    def makeReadOnly (self, *args, **kwargs):
      '''
makeReadOnly( (QuatfArray)arg1) -> None :

    C++ signature :
        void makeReadOnly(PyImath::FixedArray<Imath_3_1::Quat<float> > {lvalue})'''
    ...
    def normalize (self, *args, **kwargs):
      '''
normalize( (QuatfArray)arg1) -> QuatfArray :
    Normalize each quaternion in the array

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Quat<float> > {lvalue} normalize(PyImath::FixedArray<Imath_3_1::Quat<float> > {lvalue})'''
    ...
    def normalized (self, *args, **kwargs):
      '''
normalized( (QuatfArray)arg1) -> QuatfArray :
    Return a new quaternion array with unit quaternions.

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Quat<float> > normalized(PyImath::FixedArray<Imath_3_1::Quat<float> >)'''
    ...
    def orientToVectors (self, *args, **kwargs):
      '''
orientToVectors( (QuatfArray)arg1, (V3fArray)forward, (V3fArray)up, (bool)alignForward) -> None :
    Sets the orientations to match the given forward and up vectors, matching the forward vector exactly if 'alignForward' is True, matching the up vector exactly if 'alignForward' is False.  If the vectors are already orthogonal, both vectors will be matched exactly.

    C++ signature :
        void orientToVectors(PyImath::FixedArray<Imath_3_1::Quat<float> > {lvalue},PyImath::FixedArray<Imath_3_1::Vec3<float> >,PyImath::FixedArray<Imath_3_1::Vec3<float> >,bool)'''
    ...
    def r (self, *args, **kwargs):
      '''None'''
    ...
    def rotateVector (self, *args, **kwargs):
      '''
rotateVector( (QuatfArray)arg1, (V3fArray)vector) -> V3fArray :
    Rotate the supplied vectors by the quaternions.  Assumes quaternions are normalized.

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec3<float> > rotateVector(PyImath::FixedArray<Imath_3_1::Quat<float> >,PyImath::FixedArray<Imath_3_1::Vec3<float> >)'''
    ...
    def setAxisAngle (self, *args, **kwargs):
      '''
setAxisAngle( (QuatfArray)arg1, (V3fArray)axis, (FloatArray)angle) -> QuatfArray :
    set the quaternion arrays from a given axis and angle

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Quat<float> > {lvalue} setAxisAngle(PyImath::FixedArray<Imath_3_1::Quat<float> > {lvalue},PyImath::FixedArray<Imath_3_1::Vec3<float> >,PyImath::FixedArray<float>)'''
    ...
    def setEulerXYZ (self, *args, **kwargs):
      '''
setEulerXYZ( (QuatfArray)arg1, (V3fArray)euler) -> None :
    set the quaternion arrays from a given euler XYZ angle vector

    C++ signature :
        void setEulerXYZ(PyImath::FixedArray<Imath_3_1::Quat<float> > {lvalue},PyImath::FixedArray<Imath_3_1::Vec3<float> >)'''
    ...
    def setRotation (self, *args, **kwargs):
      '''
setRotation( (QuatfArray)arg1, (V3fArray)from, (V3fArray)to) -> None :
    set rotation angles for each quat

    C++ signature :
        void setRotation(PyImath::FixedArray<Imath_3_1::Quat<float> > {lvalue},PyImath::FixedArray<Imath_3_1::Vec3<float> >,PyImath::FixedArray<Imath_3_1::Vec3<float> >)'''
    ...
    def slerp (self, *args, **kwargs):
      '''
slerp( (QuatfArray)arg1, (Quatf)qB, (float)t) -> QuatfArray :
    slerp(qB,t) - Return the element-by-element shortest arc spherical linear interpolation between self and B.

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Quat<float> > slerp(PyImath::FixedArray<Imath_3_1::Quat<float> >,Imath_3_1::Quat<float>,float)

slerp( (QuatfArray)arg1, (QuatfArray)qB, (float)t) -> QuatfArray :
    slerp(qB,t) - Return the element-by-element shortest arc spherical linear interpolation between self and B.

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Quat<float> > slerp(PyImath::FixedArray<Imath_3_1::Quat<float> >,PyImath::FixedArray<Imath_3_1::Quat<float> >,float)'''
    ...
    def writable (self, *args, **kwargs):
      '''
writable( (QuatfArray)arg1) -> bool :

    C++ signature :
        bool writable(PyImath::FixedArray<Imath_3_1::Quat<float> > {lvalue})'''
    ...
    def x (self, *args, **kwargs):
      '''None'''
    ...
    def y (self, *args, **kwargs):
      '''None'''
    ...
    def z (self, *args, **kwargs):
      '''None'''
    ...

def Rand32 (*args):
      '''
__init__(boost::python::api::object, Imath_3_1::Rand32)
__init__(boost::python::api::object, unsigned long)
__init__(_object*)
__init__(_object*)

'''      
    ...

class Rand32:
    def init (self, *args, **kwargs):
      '''
init( (Rand32)arg1, (int)arg2) -> None :
    r.init(i) -- initialize with integer seed i

    C++ signature :
        void init(Imath_3_1::Rand32 {lvalue},unsigned long)'''
    ...
    def nextGauss (self, *args, **kwargs):
      '''
nextGauss( (Rand32)arg1) -> float :
    r.nextGauss() -- returns the next floating-point value in the normally (Gaussian) distributed sequence

    C++ signature :
        float nextGauss(Imath_3_1::Rand32 {lvalue})'''
    ...
    def nextGaussSphere (self, *args, **kwargs):
      '''
nextGaussSphere( (Rand32)arg1, (V3f)arg2) -> V3f :
    r.nextGaussSphere(v) -- returns the next point whose distance from the origin has a normal (Gaussian) distribution with mean 0 and variance 1.  The vector argument, v, specifies the dimension and number type.

    C++ signature :
        Imath_3_1::Vec3<float> nextGaussSphere(Imath_3_1::Rand32 {lvalue},Imath_3_1::Vec3<float>)

nextGaussSphere( (Rand32)arg1, (V3d)arg2) -> V3d :

    C++ signature :
        Imath_3_1::Vec3<double> nextGaussSphere(Imath_3_1::Rand32 {lvalue},Imath_3_1::Vec3<double>)

nextGaussSphere( (Rand32)arg1, (V2f)arg2) -> V2f :

    C++ signature :
        Imath_3_1::Vec2<float> nextGaussSphere(Imath_3_1::Rand32 {lvalue},Imath_3_1::Vec2<float>)

nextGaussSphere( (Rand32)arg1, (V2d)arg2) -> V2d :

    C++ signature :
        Imath_3_1::Vec2<double> nextGaussSphere(Imath_3_1::Rand32 {lvalue},Imath_3_1::Vec2<double>)'''
    ...
    def nextHollowSphere (self, *args, **kwargs):
      '''
nextHollowSphere( (Rand32)arg1, (V3f)arg2) -> V3f :
    r.nextHollowSphere(v) -- return the next point uniformly distributed on the surface of a sphere of radius 1 centered at the origin.  The vector argument, v, specifies the dimension and number type.

    C++ signature :
        Imath_3_1::Vec3<float> nextHollowSphere(Imath_3_1::Rand32 {lvalue},Imath_3_1::Vec3<float>)

nextHollowSphere( (Rand32)arg1, (V3d)arg2) -> V3d :

    C++ signature :
        Imath_3_1::Vec3<double> nextHollowSphere(Imath_3_1::Rand32 {lvalue},Imath_3_1::Vec3<double>)

nextHollowSphere( (Rand32)arg1, (V2f)arg2) -> V2f :

    C++ signature :
        Imath_3_1::Vec2<float> nextHollowSphere(Imath_3_1::Rand32 {lvalue},Imath_3_1::Vec2<float>)

nextHollowSphere( (Rand32)arg1, (V2d)arg2) -> V2d :

    C++ signature :
        Imath_3_1::Vec2<double> nextHollowSphere(Imath_3_1::Rand32 {lvalue},Imath_3_1::Vec2<double>)'''
    ...
    def nextSolidSphere (self, *args, **kwargs):
      '''
nextSolidSphere( (Rand32)arg1, (V3f)arg2) -> V3f :
    r.nextSolidSphere(v) -- return the next point uniformly distributed in a sphere of radius 1 centered at the origin.  The vector argument, v, specifies the dimension and number type.

    C++ signature :
        Imath_3_1::Vec3<float> nextSolidSphere(Imath_3_1::Rand32 {lvalue},Imath_3_1::Vec3<float>)

nextSolidSphere( (Rand32)arg1, (V3d)arg2) -> V3d :

    C++ signature :
        Imath_3_1::Vec3<double> nextSolidSphere(Imath_3_1::Rand32 {lvalue},Imath_3_1::Vec3<double>)

nextSolidSphere( (Rand32)arg1, (V2f)arg2) -> V2f :

    C++ signature :
        Imath_3_1::Vec2<float> nextSolidSphere(Imath_3_1::Rand32 {lvalue},Imath_3_1::Vec2<float>)

nextSolidSphere( (Rand32)arg1, (V2d)arg2) -> V2d :

    C++ signature :
        Imath_3_1::Vec2<double> nextSolidSphere(Imath_3_1::Rand32 {lvalue},Imath_3_1::Vec2<double>)'''
    ...
    def nextb (self, *args, **kwargs):
      '''
nextb( (Rand32)arg1) -> bool :
    r.nextb() -- return the next boolean value in the uniformly-distributed sequence

    C++ signature :
        bool nextb(Imath_3_1::Rand32 {lvalue})'''
    ...
    def nextf (self, *args, **kwargs):
      '''
nextf( (Rand32)arg1) -> float :
    r.nextf() -- return the next floating-point value in the uniformly-distributed sequence
    r.nextf(float, float) -- return the next floating-point value in the uniformly-distributed sequence

    C++ signature :
        float nextf(Imath_3_1::Rand32 {lvalue})

nextf( (Rand32)arg1, (float)arg2, (float)arg3) -> float :

    C++ signature :
        float nextf(Imath_3_1::Rand32 {lvalue},float,float)'''
    ...
    def nexti (self, *args, **kwargs):
      '''
nexti( (Rand32)arg1) -> int :
    r.nexti() -- return the next integer value in the uniformly-distributed sequence

    C++ signature :
        unsigned long nexti(Imath_3_1::Rand32 {lvalue})'''
    ...

def Rand48 (*args):
      '''
__init__(boost::python::api::object, Imath_3_1::Rand48)
__init__(boost::python::api::object, unsigned long)
__init__(_object*)
__init__(_object*)

'''      
    ...

class Rand48:
    def init (self, *args, **kwargs):
      '''
init( (Rand48)arg1, (int)arg2) -> None :
    r.init(i) -- initialize with integer seed i

    C++ signature :
        void init(Imath_3_1::Rand48 {lvalue},unsigned long)'''
    ...
    def nextGauss (self, *args, **kwargs):
      '''
nextGauss( (Rand48)arg1) -> float :
    r.nextGauss() -- returns the next floating-point value in the normally (Gaussian) distributed sequence

    C++ signature :
        float nextGauss(Imath_3_1::Rand48 {lvalue})'''
    ...
    def nextGaussSphere (self, *args, **kwargs):
      '''
nextGaussSphere( (Rand48)arg1, (V3f)arg2) -> V3f :
    r.nextGaussSphere(v) -- returns the next point whose distance from the origin has a normal (Gaussian) distribution with mean 0 and variance 1.  The vector argument, v, specifies the dimension and number type.

    C++ signature :
        Imath_3_1::Vec3<float> nextGaussSphere(Imath_3_1::Rand48 {lvalue},Imath_3_1::Vec3<float>)

nextGaussSphere( (Rand48)arg1, (V3d)arg2) -> V3d :

    C++ signature :
        Imath_3_1::Vec3<double> nextGaussSphere(Imath_3_1::Rand48 {lvalue},Imath_3_1::Vec3<double>)

nextGaussSphere( (Rand48)arg1, (V2f)arg2) -> V2f :

    C++ signature :
        Imath_3_1::Vec2<float> nextGaussSphere(Imath_3_1::Rand48 {lvalue},Imath_3_1::Vec2<float>)

nextGaussSphere( (Rand48)arg1, (V2d)arg2) -> V2d :

    C++ signature :
        Imath_3_1::Vec2<double> nextGaussSphere(Imath_3_1::Rand48 {lvalue},Imath_3_1::Vec2<double>)'''
    ...
    def nextHollowSphere (self, *args, **kwargs):
      '''
nextHollowSphere( (Rand48)arg1, (V3f)arg2) -> V3f :
    r.nextHollowSphere(v) -- return the next point uniformly distributed on the surface of a sphere of radius 1 centered at the origin.  The vector argument, v, specifies the dimension and number type.

    C++ signature :
        Imath_3_1::Vec3<float> nextHollowSphere(Imath_3_1::Rand48 {lvalue},Imath_3_1::Vec3<float>)

nextHollowSphere( (Rand48)arg1, (V3d)arg2) -> V3d :

    C++ signature :
        Imath_3_1::Vec3<double> nextHollowSphere(Imath_3_1::Rand48 {lvalue},Imath_3_1::Vec3<double>)

nextHollowSphere( (Rand48)arg1, (V2f)arg2) -> V2f :

    C++ signature :
        Imath_3_1::Vec2<float> nextHollowSphere(Imath_3_1::Rand48 {lvalue},Imath_3_1::Vec2<float>)

nextHollowSphere( (Rand48)arg1, (V2d)arg2) -> V2d :

    C++ signature :
        Imath_3_1::Vec2<double> nextHollowSphere(Imath_3_1::Rand48 {lvalue},Imath_3_1::Vec2<double>)'''
    ...
    def nextSolidSphere (self, *args, **kwargs):
      '''
nextSolidSphere( (Rand48)arg1, (V3f)arg2) -> V3f :
    r.nextSolidSphere(v) -- return the next point uniformly distributed in a sphere of radius 1 centered at the origin.  The vector argument, v, specifies the dimension and number type.

    C++ signature :
        Imath_3_1::Vec3<float> nextSolidSphere(Imath_3_1::Rand48 {lvalue},Imath_3_1::Vec3<float>)

nextSolidSphere( (Rand48)arg1, (V3d)arg2) -> V3d :

    C++ signature :
        Imath_3_1::Vec3<double> nextSolidSphere(Imath_3_1::Rand48 {lvalue},Imath_3_1::Vec3<double>)

nextSolidSphere( (Rand48)arg1, (V2f)arg2) -> V2f :

    C++ signature :
        Imath_3_1::Vec2<float> nextSolidSphere(Imath_3_1::Rand48 {lvalue},Imath_3_1::Vec2<float>)

nextSolidSphere( (Rand48)arg1, (V2d)arg2) -> V2d :

    C++ signature :
        Imath_3_1::Vec2<double> nextSolidSphere(Imath_3_1::Rand48 {lvalue},Imath_3_1::Vec2<double>)'''
    ...
    def nextb (self, *args, **kwargs):
      '''
nextb( (Rand48)arg1) -> bool :
    r.nextb() -- return the next boolean value in the uniformly-distributed sequence

    C++ signature :
        bool nextb(Imath_3_1::Rand48 {lvalue})'''
    ...
    def nextf (self, *args, **kwargs):
      '''
nextf( (Rand48)arg1) -> float :
    r.nextf() -- return the next double value in the uniformly-distributed sequence
    r.nextf(double,double) -- return the next double value in the uniformly-distributed sequence

    C++ signature :
        double nextf(Imath_3_1::Rand48 {lvalue})

nextf( (Rand48)arg1, (float)arg2, (float)arg3) -> float :

    C++ signature :
        double nextf(Imath_3_1::Rand48 {lvalue},double,double)'''
    ...
    def nexti (self, *args, **kwargs):
      '''
nexti( (Rand48)arg1) -> int :
    r.nexti() -- return the next integer value in the uniformly-distributed sequence

    C++ signature :
        long nexti(Imath_3_1::Rand48 {lvalue})'''
    ...

def Shear6d (*args):
      '''
__init__(boost::python::api::object, Imath_3_1::Shear6<int>)
__init__(boost::python::api::object, Imath_3_1::Shear6<double>)
__init__(boost::python::api::object, Imath_3_1::Shear6<float>)
__init__(boost::python::api::object, boost::python::tuple)
__init__(boost::python::api::object, double)
__init__(_object*, double, double, double, double, double, double)
__init__(_object*, Imath_3_1::Vec3<int>)
__init__(_object*, Imath_3_1::Vec3<double>)
__init__(_object*, Imath_3_1::Vec3<float>)
__init__(_object*, double, double, double)
__init__(_object*)
__init__(_object*, Imath_3_1::Shear6<double>)

'''      
    ...

class Shear6d:
    def baseTypeEpsilon (self, *args, **kwargs):
      '''
baseTypeEpsilon() -> float :

    C++ signature :
        double baseTypeEpsilon()'''
    ...
    def baseTypeLowest (self, *args, **kwargs):
      '''
baseTypeLowest() -> float :

    C++ signature :
        double baseTypeLowest()'''
    ...
    def baseTypeMax (self, *args, **kwargs):
      '''
baseTypeMax() -> float :

    C++ signature :
        double baseTypeMax()'''
    ...
    def baseTypeSmallest (self, *args, **kwargs):
      '''
baseTypeSmallest() -> float :

    C++ signature :
        double baseTypeSmallest()'''
    ...
    def equalWithAbsError (self, *args, **kwargs):
      '''
equalWithAbsError( (Shear6d)arg1, (Shear6d)arg2, (float)arg3) -> bool :

    C++ signature :
        bool equalWithAbsError(Imath_3_1::Shear6<double> {lvalue},Imath_3_1::Shear6<double>,double)'''
    ...
    def equalWithRelError (self, *args, **kwargs):
      '''
equalWithRelError( (Shear6d)arg1, (Shear6d)arg2, (float)arg3) -> bool :

    C++ signature :
        bool equalWithRelError(Imath_3_1::Shear6<double> {lvalue},Imath_3_1::Shear6<double>,double)'''
    ...
    def getValue (self, *args, **kwargs):
      '''
getValue( (Shear6d)arg1, (Shear6d)arg2) -> None :

    C++ signature :
        void getValue(Imath_3_1::Shear6<double> {lvalue},Imath_3_1::Shear6<double> {lvalue})'''
    ...
    def negate (self, *args, **kwargs):
      '''
negate( (Shear6d)arg1) -> Shear6d :

    C++ signature :
        Imath_3_1::Shear6<double> negate(Imath_3_1::Shear6<double> {lvalue})'''
    ...
    def setValue (self, *args, **kwargs):
      '''
setValue( (Shear6d)arg1, (float)arg2, (float)arg3, (float)arg4, (float)arg5, (float)arg6, (float)arg7) -> None :

    C++ signature :
        void setValue(Imath_3_1::Shear6<double> {lvalue},double,double,double,double,double,double)

setValue( (Shear6d)arg1, (Shear6d)arg2) -> None :

    C++ signature :
        void setValue(Imath_3_1::Shear6<double> {lvalue},Imath_3_1::Shear6<double>)'''
    ...

def Shear6f (*args):
      '''
__init__(boost::python::api::object, Imath_3_1::Shear6<int>)
__init__(boost::python::api::object, Imath_3_1::Shear6<double>)
__init__(boost::python::api::object, Imath_3_1::Shear6<float>)
__init__(boost::python::api::object, boost::python::tuple)
__init__(boost::python::api::object, float)
__init__(_object*, float, float, float, float, float, float)
__init__(_object*, Imath_3_1::Vec3<int>)
__init__(_object*, Imath_3_1::Vec3<double>)
__init__(_object*, Imath_3_1::Vec3<float>)
__init__(_object*, float, float, float)
__init__(_object*)
__init__(_object*, Imath_3_1::Shear6<float>)

'''      
    ...

class Shear6f:
    def baseTypeEpsilon (self, *args, **kwargs):
      '''
baseTypeEpsilon() -> float :

    C++ signature :
        float baseTypeEpsilon()'''
    ...
    def baseTypeLowest (self, *args, **kwargs):
      '''
baseTypeLowest() -> float :

    C++ signature :
        float baseTypeLowest()'''
    ...
    def baseTypeMax (self, *args, **kwargs):
      '''
baseTypeMax() -> float :

    C++ signature :
        float baseTypeMax()'''
    ...
    def baseTypeSmallest (self, *args, **kwargs):
      '''
baseTypeSmallest() -> float :

    C++ signature :
        float baseTypeSmallest()'''
    ...
    def equalWithAbsError (self, *args, **kwargs):
      '''
equalWithAbsError( (Shear6f)arg1, (Shear6f)arg2, (float)arg3) -> bool :

    C++ signature :
        bool equalWithAbsError(Imath_3_1::Shear6<float> {lvalue},Imath_3_1::Shear6<float>,float)'''
    ...
    def equalWithRelError (self, *args, **kwargs):
      '''
equalWithRelError( (Shear6f)arg1, (Shear6f)arg2, (float)arg3) -> bool :

    C++ signature :
        bool equalWithRelError(Imath_3_1::Shear6<float> {lvalue},Imath_3_1::Shear6<float>,float)'''
    ...
    def getValue (self, *args, **kwargs):
      '''
getValue( (Shear6f)arg1, (Shear6f)arg2) -> None :

    C++ signature :
        void getValue(Imath_3_1::Shear6<float> {lvalue},Imath_3_1::Shear6<float> {lvalue})'''
    ...
    def negate (self, *args, **kwargs):
      '''
negate( (Shear6f)arg1) -> Shear6f :

    C++ signature :
        Imath_3_1::Shear6<float> negate(Imath_3_1::Shear6<float> {lvalue})'''
    ...
    def setValue (self, *args, **kwargs):
      '''
setValue( (Shear6f)arg1, (float)arg2, (float)arg3, (float)arg4, (float)arg5, (float)arg6, (float)arg7) -> None :

    C++ signature :
        void setValue(Imath_3_1::Shear6<float> {lvalue},float,float,float,float,float,float)

setValue( (Shear6f)arg1, (Shear6f)arg2) -> None :

    C++ signature :
        void setValue(Imath_3_1::Shear6<float> {lvalue},Imath_3_1::Shear6<float>)'''
    ...

def ShortArray (*args):
      '''
__init__(_object*, short, unsigned long)
__init__(_object*, PyImath::FixedArray<short>)
__init__(_object*, unsigned long)

'''      
    ...

class ShortArray:
    def ifelse (self, *args, **kwargs):
      '''
ifelse( (ShortArray)arg1, (IntArray)arg2, (int)arg3) -> ShortArray :

    C++ signature :
        PyImath::FixedArray<short> ifelse(PyImath::FixedArray<short> {lvalue},PyImath::FixedArray<int>,short)

ifelse( (ShortArray)arg1, (IntArray)arg2, (ShortArray)arg3) -> ShortArray :

    C++ signature :
        PyImath::FixedArray<short> ifelse(PyImath::FixedArray<short> {lvalue},PyImath::FixedArray<int>,PyImath::FixedArray<short>)'''
    ...
    def makeReadOnly (self, *args, **kwargs):
      '''
makeReadOnly( (ShortArray)arg1) -> None :

    C++ signature :
        void makeReadOnly(PyImath::FixedArray<short> {lvalue})'''
    ...
    def reduce (self, *args, **kwargs):
      '''
reduce( (ShortArray)arg1) -> int :

    C++ signature :
        short reduce(PyImath::FixedArray<short>)'''
    ...
    def writable (self, *args, **kwargs):
      '''
writable( (ShortArray)arg1) -> bool :

    C++ signature :
        bool writable(PyImath::FixedArray<short> {lvalue})'''
    ...

def SignedCharArray (*args):
      '''
__init__(_object*, signed char, unsigned long)
__init__(_object*, PyImath::FixedArray<signed char>)
__init__(_object*, unsigned long)

'''      
    ...

class SignedCharArray:
    def ifelse (self, *args, **kwargs):
      '''
ifelse( (SignedCharArray)arg1, (IntArray)arg2, (int)arg3) -> SignedCharArray :

    C++ signature :
        PyImath::FixedArray<signed char> ifelse(PyImath::FixedArray<signed char> {lvalue},PyImath::FixedArray<int>,signed char)

ifelse( (SignedCharArray)arg1, (IntArray)arg2, (SignedCharArray)arg3) -> SignedCharArray :

    C++ signature :
        PyImath::FixedArray<signed char> ifelse(PyImath::FixedArray<signed char> {lvalue},PyImath::FixedArray<int>,PyImath::FixedArray<signed char>)'''
    ...
    def makeReadOnly (self, *args, **kwargs):
      '''
makeReadOnly( (SignedCharArray)arg1) -> None :

    C++ signature :
        void makeReadOnly(PyImath::FixedArray<signed char> {lvalue})'''
    ...
    def reduce (self, *args, **kwargs):
      '''
reduce( (SignedCharArray)arg1) -> int :

    C++ signature :
        signed char reduce(PyImath::FixedArray<signed char>)'''
    ...
    def writable (self, *args, **kwargs):
      '''
writable( (SignedCharArray)arg1) -> bool :

    C++ signature :
        bool writable(PyImath::FixedArray<signed char> {lvalue})'''
    ...

def StringArray (*args):
      '''
__init__(boost::python::api::object, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, unsigned long)
__init__(boost::python::api::object, unsigned long)

'''      
    ...

class StringArray:
    def makeReadOnly (self, *args, **kwargs):
      '''
makeReadOnly( (StringArray)arg1) -> None :

    C++ signature :
        void makeReadOnly(PyImath::StringArrayT<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > {lvalue})'''
    ...
    def writable (self, *args, **kwargs):
      '''
writable( (StringArray)arg1) -> bool :

    C++ signature :
        bool writable(PyImath::StringArrayT<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > {lvalue})'''
    ...

def UnsignedCharArray (*args):
      '''
__init__(_object*, unsigned char, unsigned long)
__init__(_object*, PyImath::FixedArray<unsigned char>)
__init__(_object*, unsigned long)

'''      
    ...

class UnsignedCharArray:
    def ifelse (self, *args, **kwargs):
      '''
ifelse( (UnsignedCharArray)arg1, (IntArray)arg2, (int)arg3) -> UnsignedCharArray :

    C++ signature :
        PyImath::FixedArray<unsigned char> ifelse(PyImath::FixedArray<unsigned char> {lvalue},PyImath::FixedArray<int>,unsigned char)

ifelse( (UnsignedCharArray)arg1, (IntArray)arg2, (UnsignedCharArray)arg3) -> UnsignedCharArray :

    C++ signature :
        PyImath::FixedArray<unsigned char> ifelse(PyImath::FixedArray<unsigned char> {lvalue},PyImath::FixedArray<int>,PyImath::FixedArray<unsigned char>)'''
    ...
    def makeReadOnly (self, *args, **kwargs):
      '''
makeReadOnly( (UnsignedCharArray)arg1) -> None :

    C++ signature :
        void makeReadOnly(PyImath::FixedArray<unsigned char> {lvalue})'''
    ...
    def reduce (self, *args, **kwargs):
      '''
reduce( (UnsignedCharArray)arg1) -> int :

    C++ signature :
        unsigned char reduce(PyImath::FixedArray<unsigned char>)'''
    ...
    def writable (self, *args, **kwargs):
      '''
writable( (UnsignedCharArray)arg1) -> bool :

    C++ signature :
        bool writable(PyImath::FixedArray<unsigned char> {lvalue})'''
    ...

def UnsignedIntArray (*args):
      '''
__init__(_object*, PyImath::FixedArray<double>)
__init__(_object*, PyImath::FixedArray<float>)
__init__(_object*, unsigned int, unsigned long)
__init__(_object*, PyImath::FixedArray<unsigned int>)
__init__(_object*, unsigned long)

'''      
    ...

class UnsignedIntArray:
    def ifelse (self, *args, **kwargs):
      '''
ifelse( (UnsignedIntArray)arg1, (IntArray)arg2, (int)arg3) -> UnsignedIntArray :

    C++ signature :
        PyImath::FixedArray<unsigned int> ifelse(PyImath::FixedArray<unsigned int> {lvalue},PyImath::FixedArray<int>,unsigned int)

ifelse( (UnsignedIntArray)arg1, (IntArray)arg2, (UnsignedIntArray)arg3) -> UnsignedIntArray :

    C++ signature :
        PyImath::FixedArray<unsigned int> ifelse(PyImath::FixedArray<unsigned int> {lvalue},PyImath::FixedArray<int>,PyImath::FixedArray<unsigned int>)'''
    ...
    def makeReadOnly (self, *args, **kwargs):
      '''
makeReadOnly( (UnsignedIntArray)arg1) -> None :

    C++ signature :
        void makeReadOnly(PyImath::FixedArray<unsigned int> {lvalue})'''
    ...
    def reduce (self, *args, **kwargs):
      '''
reduce( (UnsignedIntArray)arg1) -> int :

    C++ signature :
        unsigned int reduce(PyImath::FixedArray<unsigned int>)'''
    ...
    def writable (self, *args, **kwargs):
      '''
writable( (UnsignedIntArray)arg1) -> bool :

    C++ signature :
        bool writable(PyImath::FixedArray<unsigned int> {lvalue})'''
    ...

def UnsignedShortArray (*args):
      '''
__init__(_object*, unsigned short, unsigned long)
__init__(_object*, PyImath::FixedArray<unsigned short>)
__init__(_object*, unsigned long)

'''      
    ...

class UnsignedShortArray:
    def ifelse (self, *args, **kwargs):
      '''
ifelse( (UnsignedShortArray)arg1, (IntArray)arg2, (int)arg3) -> UnsignedShortArray :

    C++ signature :
        PyImath::FixedArray<unsigned short> ifelse(PyImath::FixedArray<unsigned short> {lvalue},PyImath::FixedArray<int>,unsigned short)

ifelse( (UnsignedShortArray)arg1, (IntArray)arg2, (UnsignedShortArray)arg3) -> UnsignedShortArray :

    C++ signature :
        PyImath::FixedArray<unsigned short> ifelse(PyImath::FixedArray<unsigned short> {lvalue},PyImath::FixedArray<int>,PyImath::FixedArray<unsigned short>)'''
    ...
    def makeReadOnly (self, *args, **kwargs):
      '''
makeReadOnly( (UnsignedShortArray)arg1) -> None :

    C++ signature :
        void makeReadOnly(PyImath::FixedArray<unsigned short> {lvalue})'''
    ...
    def reduce (self, *args, **kwargs):
      '''
reduce( (UnsignedShortArray)arg1) -> int :

    C++ signature :
        unsigned short reduce(PyImath::FixedArray<unsigned short>)'''
    ...
    def writable (self, *args, **kwargs):
      '''
writable( (UnsignedShortArray)arg1) -> bool :

    C++ signature :
        bool writable(PyImath::FixedArray<unsigned short> {lvalue})'''
    ...

def V2d (*args):
      '''
__init__(boost::python::api::object, boost::python::api::object, boost::python::api::object)
__init__(boost::python::api::object, boost::python::api::object)
__init__(boost::python::api::object)
__init__(_object*, Imath_3_1::Vec2<double>)

'''      
    ...

class V2d:
    def baseTypeEpsilon (self, *args, **kwargs):
      '''
baseTypeEpsilon() -> float :
    baseTypeEpsilon() epsilon value of the base type of the vector

    C++ signature :
        double baseTypeEpsilon()'''
    ...
    def baseTypeLowest (self, *args, **kwargs):
      '''
baseTypeLowest() -> float :
    baseTypeLowest() largest negative value of the base type of the vector

    C++ signature :
        double baseTypeLowest()'''
    ...
    def baseTypeMax (self, *args, **kwargs):
      '''
baseTypeMax() -> float :
    baseTypeMax() max value of the base type of the vector

    C++ signature :
        double baseTypeMax()'''
    ...
    def baseTypeSmallest (self, *args, **kwargs):
      '''
baseTypeSmallest() -> float :
    baseTypeSmallest() smallest value of the base type of the vector

    C++ signature :
        double baseTypeSmallest()'''
    ...
    def closestVertex (self, *args, **kwargs):
      '''
closestVertex( (V2d)arg1, (V2d)arg2, (V2d)arg3, (V2d)arg4) -> V2d :

    C++ signature :
        Imath_3_1::Vec2<double> closestVertex(Imath_3_1::Vec2<double> {lvalue},Imath_3_1::Vec2<double>,Imath_3_1::Vec2<double>,Imath_3_1::Vec2<double>)'''
    ...
    def cross (self, *args, **kwargs):
      '''
cross( (V2d)arg1, (V2d)arg2) -> float :
    v1.cross(v2) right handed cross product

    C++ signature :
        double cross(Imath_3_1::Vec2<double>,Imath_3_1::Vec2<double>)

cross( (V2d)arg1, (V2dArray)arg2) -> DoubleArray :
    v1.cross(v2) right handed array cross product

    C++ signature :
        PyImath::FixedArray<double> cross(Imath_3_1::Vec2<double>,PyImath::FixedArray<Imath_3_1::Vec2<double> >)'''
    ...
    def dimensions (self, *args, **kwargs):
      '''
dimensions() -> int :
    dimensions() number of dimensions in the vector

    C++ signature :
        unsigned int dimensions()'''
    ...
    def dot (self, *args, **kwargs):
      '''
dot( (V2d)arg1, (V2d)arg2) -> float :
    v1.dot(v2) inner product of the two vectors

    C++ signature :
        double dot(Imath_3_1::Vec2<double>,Imath_3_1::Vec2<double>)

dot( (V2d)arg1, (V2dArray)arg2) -> DoubleArray :
    v1.dot(v2) array inner product

    C++ signature :
        PyImath::FixedArray<double> dot(Imath_3_1::Vec2<double>,PyImath::FixedArray<Imath_3_1::Vec2<double> >)'''
    ...
    def equalWithAbsError (self, *args, **kwargs):
      '''
equalWithAbsError( (V2d)arg1, (V2d)arg2, (float)arg3) -> bool :
    v1.equalWithAbsError(v2) true if the elements of v1 and v2 are the same with an absolute error of no more than e, i.e., abs(v1[i] - v2[i]) <= e

    C++ signature :
        bool equalWithAbsError(Imath_3_1::Vec2<double> {lvalue},Imath_3_1::Vec2<double>,double)

equalWithAbsError( (V2d)arg1, (object)arg2, (object)arg3) -> bool :

    C++ signature :
        bool equalWithAbsError(Imath_3_1::Vec2<double>,boost::python::api::object,boost::python::api::object)'''
    ...
    def equalWithRelError (self, *args, **kwargs):
      '''
equalWithRelError( (V2d)arg1, (V2d)arg2, (float)arg3) -> bool :
    v1.equalWithAbsError(v2) true if the elements of v1 and v2 are the same with an absolute error of no more than e, i.e., abs(v1[i] - v2[i]) <= e * abs(v1[i])

    C++ signature :
        bool equalWithRelError(Imath_3_1::Vec2<double> {lvalue},Imath_3_1::Vec2<double>,double)

equalWithRelError( (V2d)arg1, (object)arg2, (object)arg3) -> bool :

    C++ signature :
        bool equalWithRelError(Imath_3_1::Vec2<double>,boost::python::api::object,boost::python::api::object)'''
    ...
    def length (self, *args, **kwargs):
      '''
length( (V2d)arg1) -> float :
    length() magnitude of the vector

    C++ signature :
        double length(Imath_3_1::Vec2<double>)'''
    ...
    def length2 (self, *args, **kwargs):
      '''
length2( (V2d)arg1) -> float :
    length2() square magnitude of the vector

    C++ signature :
        double length2(Imath_3_1::Vec2<double>)'''
    ...
    def negate (self, *args, **kwargs):
      '''
negate( (V2d)arg1) -> V2d :

    C++ signature :
        Imath_3_1::Vec2<double> negate(Imath_3_1::Vec2<double> {lvalue})'''
    ...
    def normalize (self, *args, **kwargs):
      '''
normalize( (V2d)arg1) -> V2d :
    v.normalize() destructively normalizes v and returns a reference to it

    C++ signature :
        Imath_3_1::Vec2<double> normalize(Imath_3_1::Vec2<double> {lvalue})'''
    ...
    def normalizeExc (self, *args, **kwargs):
      '''
normalizeExc( (V2d)arg1) -> V2d :
    v.normalizeExc() destructively normalizes V and returns a reference to it, throwing an exception if length() == 0

    C++ signature :
        Imath_3_1::Vec2<double> normalizeExc(Imath_3_1::Vec2<double> {lvalue})'''
    ...
    def normalizeNonNull (self, *args, **kwargs):
      '''
normalizeNonNull( (V2d)arg1) -> V2d :
    v.normalizeNonNull() destructively normalizes V and returns a reference to it, faster if lngth() != 0

    C++ signature :
        Imath_3_1::Vec2<double> normalizeNonNull(Imath_3_1::Vec2<double> {lvalue})'''
    ...
    def normalized (self, *args, **kwargs):
      '''
normalized( (V2d)arg1) -> V2d :
    v.normalized() returns a normalized copy of v

    C++ signature :
        Imath_3_1::Vec2<double> normalized(Imath_3_1::Vec2<double>)'''
    ...
    def normalizedExc (self, *args, **kwargs):
      '''
normalizedExc( (V2d)arg1) -> V2d :
    v.normalizedExc() returns a normalized copy of v, throwing an exception if length() == 0

    C++ signature :
        Imath_3_1::Vec2<double> normalizedExc(Imath_3_1::Vec2<double>)'''
    ...
    def normalizedNonNull (self, *args, **kwargs):
      '''
normalizedNonNull( (V2d)arg1) -> V2d :
    v.normalizedNonNull() returns a normalized copy of v, faster if lngth() != 0

    C++ signature :
        Imath_3_1::Vec2<double> normalizedNonNull(Imath_3_1::Vec2<double>)'''
    ...
    def orthogonal (self, *args, **kwargs):
      '''
orthogonal( (V2d)arg1, (V2d)arg2) -> V2d :

    C++ signature :
        Imath_3_1::Vec2<double> orthogonal(Imath_3_1::Vec2<double>,Imath_3_1::Vec2<double>)'''
    ...
    def project (self, *args, **kwargs):
      '''
project( (V2d)arg1, (V2d)arg2) -> V2d :

    C++ signature :
        Imath_3_1::Vec2<double> project(Imath_3_1::Vec2<double>,Imath_3_1::Vec2<double>)'''
    ...
    def reflect (self, *args, **kwargs):
      '''
reflect( (V2d)arg1, (V2d)arg2) -> V2d :

    C++ signature :
        Imath_3_1::Vec2<double> reflect(Imath_3_1::Vec2<double>,Imath_3_1::Vec2<double>)'''
    ...
    def setValue (self, *args, **kwargs):
      '''
setValue( (V2d)arg1, (float)arg2, (float)arg3) -> None :

    C++ signature :
        void setValue(Imath_3_1::Vec2<double> {lvalue},double,double)'''
    ...
    def x (self, *args, **kwargs):
      '''None'''
    ...
    def y (self, *args, **kwargs):
      '''None'''
    ...

def V2dArray (*args):
      '''
__init__(_object*, PyImath::FixedArray<Imath_3_1::Vec2<float> >)
__init__(_object*, PyImath::FixedArray<Imath_3_1::Vec2<long> >)
__init__(_object*, PyImath::FixedArray<Imath_3_1::Vec2<int> >)
__init__(_object*, PyImath::FixedArray<Imath_3_1::Vec2<short> >)
__init__(_object*, Imath_3_1::Vec2<double>, unsigned long)
__init__(_object*, PyImath::FixedArray<Imath_3_1::Vec2<double> >)
__init__(_object*, unsigned long)

'''      
    ...

class V2dArray:
    def bounds (self, *args, **kwargs):
      '''
bounds( (V2dArray)arg1) -> Box2d :

    C++ signature :
        Imath_3_1::Box<Imath_3_1::Vec2<double> > bounds(PyImath::FixedArray<Imath_3_1::Vec2<double> >)'''
    ...
    def cross (self, *args, **kwargs):
      '''
cross( (V2dArray)arg1, (V2d)x) -> DoubleArray :
    cross(x) - return the cross product of (self,x)

    C++ signature :
        PyImath::FixedArray<double> cross(PyImath::FixedArray<Imath_3_1::Vec2<double> >,Imath_3_1::Vec2<double>)

cross( (V2dArray)arg1, (V2dArray)x) -> DoubleArray :
    cross(x) - return the cross product of (self,x)

    C++ signature :
        PyImath::FixedArray<double> cross(PyImath::FixedArray<Imath_3_1::Vec2<double> >,PyImath::FixedArray<Imath_3_1::Vec2<double> >)'''
    ...
    def dot (self, *args, **kwargs):
      '''
dot( (V2dArray)arg1, (V2d)x) -> DoubleArray :
    dot(x) - return the inner product of (self,x)

    C++ signature :
        PyImath::FixedArray<double> dot(PyImath::FixedArray<Imath_3_1::Vec2<double> >,Imath_3_1::Vec2<double>)

dot( (V2dArray)arg1, (V2dArray)x) -> DoubleArray :
    dot(x) - return the inner product of (self,x)

    C++ signature :
        PyImath::FixedArray<double> dot(PyImath::FixedArray<Imath_3_1::Vec2<double> >,PyImath::FixedArray<Imath_3_1::Vec2<double> >)'''
    ...
    def ifelse (self, *args, **kwargs):
      '''
ifelse( (V2dArray)arg1, (IntArray)arg2, (V2d)arg3) -> V2dArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec2<double> > ifelse(PyImath::FixedArray<Imath_3_1::Vec2<double> > {lvalue},PyImath::FixedArray<int>,Imath_3_1::Vec2<double>)

ifelse( (V2dArray)arg1, (IntArray)arg2, (V2dArray)arg3) -> V2dArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec2<double> > ifelse(PyImath::FixedArray<Imath_3_1::Vec2<double> > {lvalue},PyImath::FixedArray<int>,PyImath::FixedArray<Imath_3_1::Vec2<double> >)'''
    ...
    def length (self, *args, **kwargs):
      '''
length( (V2dArray)arg1) -> DoubleArray :

    C++ signature :
        PyImath::FixedArray<double> length(PyImath::FixedArray<Imath_3_1::Vec2<double> >)'''
    ...
    def length2 (self, *args, **kwargs):
      '''
length2( (V2dArray)arg1) -> DoubleArray :

    C++ signature :
        PyImath::FixedArray<double> length2(PyImath::FixedArray<Imath_3_1::Vec2<double> >)'''
    ...
    def makeReadOnly (self, *args, **kwargs):
      '''
makeReadOnly( (V2dArray)arg1) -> None :

    C++ signature :
        void makeReadOnly(PyImath::FixedArray<Imath_3_1::Vec2<double> > {lvalue})'''
    ...
    def max (self, *args, **kwargs):
      '''
max( (V2dArray)arg1) -> V2d :

    C++ signature :
        Imath_3_1::Vec2<double> max(PyImath::FixedArray<Imath_3_1::Vec2<double> >)'''
    ...
    def min (self, *args, **kwargs):
      '''
min( (V2dArray)arg1) -> V2d :

    C++ signature :
        Imath_3_1::Vec2<double> min(PyImath::FixedArray<Imath_3_1::Vec2<double> >)'''
    ...
    def normalize (self, *args, **kwargs):
      '''
normalize( (V2dArray)arg1) -> V2dArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec2<double> > {lvalue} normalize(PyImath::FixedArray<Imath_3_1::Vec2<double> > {lvalue})'''
    ...
    def normalizeExc (self, *args, **kwargs):
      '''
normalizeExc( (V2dArray)arg1) -> V2dArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec2<double> > {lvalue} normalizeExc(PyImath::FixedArray<Imath_3_1::Vec2<double> > {lvalue})'''
    ...
    def normalized (self, *args, **kwargs):
      '''
normalized( (V2dArray)arg1) -> V2dArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec2<double> > normalized(PyImath::FixedArray<Imath_3_1::Vec2<double> >)'''
    ...
    def normalizedExc (self, *args, **kwargs):
      '''
normalizedExc( (V2dArray)arg1) -> V2dArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec2<double> > normalizedExc(PyImath::FixedArray<Imath_3_1::Vec2<double> >)'''
    ...
    def reduce (self, *args, **kwargs):
      '''
reduce( (V2dArray)arg1) -> V2d :

    C++ signature :
        Imath_3_1::Vec2<double> reduce(PyImath::FixedArray<Imath_3_1::Vec2<double> >)'''
    ...
    def writable (self, *args, **kwargs):
      '''
writable( (V2dArray)arg1) -> bool :

    C++ signature :
        bool writable(PyImath::FixedArray<Imath_3_1::Vec2<double> > {lvalue})'''
    ...
    def x (self, *args, **kwargs):
      '''None'''
    ...
    def y (self, *args, **kwargs):
      '''None'''
    ...

def V2dArrayFromBuffer (*args):
      '''

'''      
    ...

def V2f (*args):
      '''
__init__(boost::python::api::object, boost::python::api::object, boost::python::api::object)
__init__(boost::python::api::object, boost::python::api::object)
__init__(boost::python::api::object)
__init__(_object*, Imath_3_1::Vec2<float>)

'''      
    ...

class V2f:
    def baseTypeEpsilon (self, *args, **kwargs):
      '''
baseTypeEpsilon() -> float :
    baseTypeEpsilon() epsilon value of the base type of the vector

    C++ signature :
        float baseTypeEpsilon()'''
    ...
    def baseTypeLowest (self, *args, **kwargs):
      '''
baseTypeLowest() -> float :
    baseTypeLowest() largest negative value of the base type of the vector

    C++ signature :
        float baseTypeLowest()'''
    ...
    def baseTypeMax (self, *args, **kwargs):
      '''
baseTypeMax() -> float :
    baseTypeMax() max value of the base type of the vector

    C++ signature :
        float baseTypeMax()'''
    ...
    def baseTypeSmallest (self, *args, **kwargs):
      '''
baseTypeSmallest() -> float :
    baseTypeSmallest() smallest value of the base type of the vector

    C++ signature :
        float baseTypeSmallest()'''
    ...
    def closestVertex (self, *args, **kwargs):
      '''
closestVertex( (V2f)arg1, (V2f)arg2, (V2f)arg3, (V2f)arg4) -> V2f :

    C++ signature :
        Imath_3_1::Vec2<float> closestVertex(Imath_3_1::Vec2<float> {lvalue},Imath_3_1::Vec2<float>,Imath_3_1::Vec2<float>,Imath_3_1::Vec2<float>)'''
    ...
    def cross (self, *args, **kwargs):
      '''
cross( (V2f)arg1, (V2f)arg2) -> float :
    v1.cross(v2) right handed cross product

    C++ signature :
        float cross(Imath_3_1::Vec2<float>,Imath_3_1::Vec2<float>)

cross( (V2f)arg1, (V2fArray)arg2) -> FloatArray :
    v1.cross(v2) right handed array cross product

    C++ signature :
        PyImath::FixedArray<float> cross(Imath_3_1::Vec2<float>,PyImath::FixedArray<Imath_3_1::Vec2<float> >)'''
    ...
    def dimensions (self, *args, **kwargs):
      '''
dimensions() -> int :
    dimensions() number of dimensions in the vector

    C++ signature :
        unsigned int dimensions()'''
    ...
    def dot (self, *args, **kwargs):
      '''
dot( (V2f)arg1, (V2f)arg2) -> float :
    v1.dot(v2) inner product of the two vectors

    C++ signature :
        float dot(Imath_3_1::Vec2<float>,Imath_3_1::Vec2<float>)

dot( (V2f)arg1, (V2fArray)arg2) -> FloatArray :
    v1.dot(v2) array inner product

    C++ signature :
        PyImath::FixedArray<float> dot(Imath_3_1::Vec2<float>,PyImath::FixedArray<Imath_3_1::Vec2<float> >)'''
    ...
    def equalWithAbsError (self, *args, **kwargs):
      '''
equalWithAbsError( (V2f)arg1, (V2f)arg2, (float)arg3) -> bool :
    v1.equalWithAbsError(v2) true if the elements of v1 and v2 are the same with an absolute error of no more than e, i.e., abs(v1[i] - v2[i]) <= e

    C++ signature :
        bool equalWithAbsError(Imath_3_1::Vec2<float> {lvalue},Imath_3_1::Vec2<float>,float)

equalWithAbsError( (V2f)arg1, (object)arg2, (object)arg3) -> bool :

    C++ signature :
        bool equalWithAbsError(Imath_3_1::Vec2<float>,boost::python::api::object,boost::python::api::object)'''
    ...
    def equalWithRelError (self, *args, **kwargs):
      '''
equalWithRelError( (V2f)arg1, (V2f)arg2, (float)arg3) -> bool :
    v1.equalWithAbsError(v2) true if the elements of v1 and v2 are the same with an absolute error of no more than e, i.e., abs(v1[i] - v2[i]) <= e * abs(v1[i])

    C++ signature :
        bool equalWithRelError(Imath_3_1::Vec2<float> {lvalue},Imath_3_1::Vec2<float>,float)

equalWithRelError( (V2f)arg1, (object)arg2, (object)arg3) -> bool :

    C++ signature :
        bool equalWithRelError(Imath_3_1::Vec2<float>,boost::python::api::object,boost::python::api::object)'''
    ...
    def length (self, *args, **kwargs):
      '''
length( (V2f)arg1) -> float :
    length() magnitude of the vector

    C++ signature :
        float length(Imath_3_1::Vec2<float>)'''
    ...
    def length2 (self, *args, **kwargs):
      '''
length2( (V2f)arg1) -> float :
    length2() square magnitude of the vector

    C++ signature :
        float length2(Imath_3_1::Vec2<float>)'''
    ...
    def negate (self, *args, **kwargs):
      '''
negate( (V2f)arg1) -> V2f :

    C++ signature :
        Imath_3_1::Vec2<float> negate(Imath_3_1::Vec2<float> {lvalue})'''
    ...
    def normalize (self, *args, **kwargs):
      '''
normalize( (V2f)arg1) -> V2f :
    v.normalize() destructively normalizes v and returns a reference to it

    C++ signature :
        Imath_3_1::Vec2<float> normalize(Imath_3_1::Vec2<float> {lvalue})'''
    ...
    def normalizeExc (self, *args, **kwargs):
      '''
normalizeExc( (V2f)arg1) -> V2f :
    v.normalizeExc() destructively normalizes V and returns a reference to it, throwing an exception if length() == 0

    C++ signature :
        Imath_3_1::Vec2<float> normalizeExc(Imath_3_1::Vec2<float> {lvalue})'''
    ...
    def normalizeNonNull (self, *args, **kwargs):
      '''
normalizeNonNull( (V2f)arg1) -> V2f :
    v.normalizeNonNull() destructively normalizes V and returns a reference to it, faster if lngth() != 0

    C++ signature :
        Imath_3_1::Vec2<float> normalizeNonNull(Imath_3_1::Vec2<float> {lvalue})'''
    ...
    def normalized (self, *args, **kwargs):
      '''
normalized( (V2f)arg1) -> V2f :
    v.normalized() returns a normalized copy of v

    C++ signature :
        Imath_3_1::Vec2<float> normalized(Imath_3_1::Vec2<float>)'''
    ...
    def normalizedExc (self, *args, **kwargs):
      '''
normalizedExc( (V2f)arg1) -> V2f :
    v.normalizedExc() returns a normalized copy of v, throwing an exception if length() == 0

    C++ signature :
        Imath_3_1::Vec2<float> normalizedExc(Imath_3_1::Vec2<float>)'''
    ...
    def normalizedNonNull (self, *args, **kwargs):
      '''
normalizedNonNull( (V2f)arg1) -> V2f :
    v.normalizedNonNull() returns a normalized copy of v, faster if lngth() != 0

    C++ signature :
        Imath_3_1::Vec2<float> normalizedNonNull(Imath_3_1::Vec2<float>)'''
    ...
    def orthogonal (self, *args, **kwargs):
      '''
orthogonal( (V2f)arg1, (V2f)arg2) -> V2f :

    C++ signature :
        Imath_3_1::Vec2<float> orthogonal(Imath_3_1::Vec2<float>,Imath_3_1::Vec2<float>)'''
    ...
    def project (self, *args, **kwargs):
      '''
project( (V2f)arg1, (V2f)arg2) -> V2f :

    C++ signature :
        Imath_3_1::Vec2<float> project(Imath_3_1::Vec2<float>,Imath_3_1::Vec2<float>)'''
    ...
    def reflect (self, *args, **kwargs):
      '''
reflect( (V2f)arg1, (V2f)arg2) -> V2f :

    C++ signature :
        Imath_3_1::Vec2<float> reflect(Imath_3_1::Vec2<float>,Imath_3_1::Vec2<float>)'''
    ...
    def setValue (self, *args, **kwargs):
      '''
setValue( (V2f)arg1, (float)arg2, (float)arg3) -> None :

    C++ signature :
        void setValue(Imath_3_1::Vec2<float> {lvalue},float,float)'''
    ...
    def x (self, *args, **kwargs):
      '''None'''
    ...
    def y (self, *args, **kwargs):
      '''None'''
    ...

def V2fArray (*args):
      '''
__init__(_object*, PyImath::FixedArray<Imath_3_1::Vec2<double> >)
__init__(_object*, PyImath::FixedArray<Imath_3_1::Vec2<long> >)
__init__(_object*, PyImath::FixedArray<Imath_3_1::Vec2<int> >)
__init__(_object*, PyImath::FixedArray<Imath_3_1::Vec2<short> >)
__init__(_object*, Imath_3_1::Vec2<float>, unsigned long)
__init__(_object*, PyImath::FixedArray<Imath_3_1::Vec2<float> >)
__init__(_object*, unsigned long)

'''      
    ...

class V2fArray:
    def bounds (self, *args, **kwargs):
      '''
bounds( (V2fArray)arg1) -> Box2f :

    C++ signature :
        Imath_3_1::Box<Imath_3_1::Vec2<float> > bounds(PyImath::FixedArray<Imath_3_1::Vec2<float> >)'''
    ...
    def cross (self, *args, **kwargs):
      '''
cross( (V2fArray)arg1, (V2f)x) -> FloatArray :
    cross(x) - return the cross product of (self,x)

    C++ signature :
        PyImath::FixedArray<float> cross(PyImath::FixedArray<Imath_3_1::Vec2<float> >,Imath_3_1::Vec2<float>)

cross( (V2fArray)arg1, (V2fArray)x) -> FloatArray :
    cross(x) - return the cross product of (self,x)

    C++ signature :
        PyImath::FixedArray<float> cross(PyImath::FixedArray<Imath_3_1::Vec2<float> >,PyImath::FixedArray<Imath_3_1::Vec2<float> >)'''
    ...
    def dot (self, *args, **kwargs):
      '''
dot( (V2fArray)arg1, (V2f)x) -> FloatArray :
    dot(x) - return the inner product of (self,x)

    C++ signature :
        PyImath::FixedArray<float> dot(PyImath::FixedArray<Imath_3_1::Vec2<float> >,Imath_3_1::Vec2<float>)

dot( (V2fArray)arg1, (V2fArray)x) -> FloatArray :
    dot(x) - return the inner product of (self,x)

    C++ signature :
        PyImath::FixedArray<float> dot(PyImath::FixedArray<Imath_3_1::Vec2<float> >,PyImath::FixedArray<Imath_3_1::Vec2<float> >)'''
    ...
    def ifelse (self, *args, **kwargs):
      '''
ifelse( (V2fArray)arg1, (IntArray)arg2, (V2f)arg3) -> V2fArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec2<float> > ifelse(PyImath::FixedArray<Imath_3_1::Vec2<float> > {lvalue},PyImath::FixedArray<int>,Imath_3_1::Vec2<float>)

ifelse( (V2fArray)arg1, (IntArray)arg2, (V2fArray)arg3) -> V2fArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec2<float> > ifelse(PyImath::FixedArray<Imath_3_1::Vec2<float> > {lvalue},PyImath::FixedArray<int>,PyImath::FixedArray<Imath_3_1::Vec2<float> >)'''
    ...
    def length (self, *args, **kwargs):
      '''
length( (V2fArray)arg1) -> FloatArray :

    C++ signature :
        PyImath::FixedArray<float> length(PyImath::FixedArray<Imath_3_1::Vec2<float> >)'''
    ...
    def length2 (self, *args, **kwargs):
      '''
length2( (V2fArray)arg1) -> FloatArray :

    C++ signature :
        PyImath::FixedArray<float> length2(PyImath::FixedArray<Imath_3_1::Vec2<float> >)'''
    ...
    def makeReadOnly (self, *args, **kwargs):
      '''
makeReadOnly( (V2fArray)arg1) -> None :

    C++ signature :
        void makeReadOnly(PyImath::FixedArray<Imath_3_1::Vec2<float> > {lvalue})'''
    ...
    def max (self, *args, **kwargs):
      '''
max( (V2fArray)arg1) -> V2f :

    C++ signature :
        Imath_3_1::Vec2<float> max(PyImath::FixedArray<Imath_3_1::Vec2<float> >)'''
    ...
    def min (self, *args, **kwargs):
      '''
min( (V2fArray)arg1) -> V2f :

    C++ signature :
        Imath_3_1::Vec2<float> min(PyImath::FixedArray<Imath_3_1::Vec2<float> >)'''
    ...
    def normalize (self, *args, **kwargs):
      '''
normalize( (V2fArray)arg1) -> V2fArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec2<float> > {lvalue} normalize(PyImath::FixedArray<Imath_3_1::Vec2<float> > {lvalue})'''
    ...
    def normalizeExc (self, *args, **kwargs):
      '''
normalizeExc( (V2fArray)arg1) -> V2fArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec2<float> > {lvalue} normalizeExc(PyImath::FixedArray<Imath_3_1::Vec2<float> > {lvalue})'''
    ...
    def normalized (self, *args, **kwargs):
      '''
normalized( (V2fArray)arg1) -> V2fArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec2<float> > normalized(PyImath::FixedArray<Imath_3_1::Vec2<float> >)'''
    ...
    def normalizedExc (self, *args, **kwargs):
      '''
normalizedExc( (V2fArray)arg1) -> V2fArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec2<float> > normalizedExc(PyImath::FixedArray<Imath_3_1::Vec2<float> >)'''
    ...
    def reduce (self, *args, **kwargs):
      '''
reduce( (V2fArray)arg1) -> V2f :

    C++ signature :
        Imath_3_1::Vec2<float> reduce(PyImath::FixedArray<Imath_3_1::Vec2<float> >)'''
    ...
    def writable (self, *args, **kwargs):
      '''
writable( (V2fArray)arg1) -> bool :

    C++ signature :
        bool writable(PyImath::FixedArray<Imath_3_1::Vec2<float> > {lvalue})'''
    ...
    def x (self, *args, **kwargs):
      '''None'''
    ...
    def y (self, *args, **kwargs):
      '''None'''
    ...

def V2fArrayFromBuffer (*args):
      '''

'''      
    ...

def V2i (*args):
      '''
__init__(boost::python::api::object, boost::python::api::object, boost::python::api::object)
__init__(boost::python::api::object, boost::python::api::object)
__init__(boost::python::api::object)
__init__(_object*, Imath_3_1::Vec2<int>)

'''      
    ...

class V2i:
    def baseTypeEpsilon (self, *args, **kwargs):
      '''
baseTypeEpsilon() -> int :
    baseTypeEpsilon() epsilon value of the base type of the vector

    C++ signature :
        int baseTypeEpsilon()'''
    ...
    def baseTypeLowest (self, *args, **kwargs):
      '''
baseTypeLowest() -> int :
    baseTypeLowest() largest negative value of the base type of the vector

    C++ signature :
        int baseTypeLowest()'''
    ...
    def baseTypeMax (self, *args, **kwargs):
      '''
baseTypeMax() -> int :
    baseTypeMax() max value of the base type of the vector

    C++ signature :
        int baseTypeMax()'''
    ...
    def baseTypeSmallest (self, *args, **kwargs):
      '''
baseTypeSmallest() -> int :
    baseTypeSmallest() smallest value of the base type of the vector

    C++ signature :
        int baseTypeSmallest()'''
    ...
    def closestVertex (self, *args, **kwargs):
      '''
closestVertex( (V2i)arg1, (V2i)arg2, (V2i)arg3, (V2i)arg4) -> V2i :

    C++ signature :
        Imath_3_1::Vec2<int> closestVertex(Imath_3_1::Vec2<int> {lvalue},Imath_3_1::Vec2<int>,Imath_3_1::Vec2<int>,Imath_3_1::Vec2<int>)'''
    ...
    def cross (self, *args, **kwargs):
      '''
cross( (V2i)arg1, (V2i)arg2) -> int :
    v1.cross(v2) right handed cross product

    C++ signature :
        int cross(Imath_3_1::Vec2<int>,Imath_3_1::Vec2<int>)

cross( (V2i)arg1, (V2iArray)arg2) -> IntArray :
    v1.cross(v2) right handed array cross product

    C++ signature :
        PyImath::FixedArray<int> cross(Imath_3_1::Vec2<int>,PyImath::FixedArray<Imath_3_1::Vec2<int> >)'''
    ...
    def dimensions (self, *args, **kwargs):
      '''
dimensions() -> int :
    dimensions() number of dimensions in the vector

    C++ signature :
        unsigned int dimensions()'''
    ...
    def dot (self, *args, **kwargs):
      '''
dot( (V2i)arg1, (V2i)arg2) -> int :
    v1.dot(v2) inner product of the two vectors

    C++ signature :
        int dot(Imath_3_1::Vec2<int>,Imath_3_1::Vec2<int>)

dot( (V2i)arg1, (V2iArray)arg2) -> IntArray :
    v1.dot(v2) array inner product

    C++ signature :
        PyImath::FixedArray<int> dot(Imath_3_1::Vec2<int>,PyImath::FixedArray<Imath_3_1::Vec2<int> >)'''
    ...
    def equalWithAbsError (self, *args, **kwargs):
      '''
equalWithAbsError( (V2i)arg1, (V2i)arg2, (int)arg3) -> bool :
    v1.equalWithAbsError(v2) true if the elements of v1 and v2 are the same with an absolute error of no more than e, i.e., abs(v1[i] - v2[i]) <= e

    C++ signature :
        bool equalWithAbsError(Imath_3_1::Vec2<int> {lvalue},Imath_3_1::Vec2<int>,int)

equalWithAbsError( (V2i)arg1, (object)arg2, (object)arg3) -> bool :

    C++ signature :
        bool equalWithAbsError(Imath_3_1::Vec2<int>,boost::python::api::object,boost::python::api::object)'''
    ...
    def equalWithRelError (self, *args, **kwargs):
      '''
equalWithRelError( (V2i)arg1, (V2i)arg2, (int)arg3) -> bool :
    v1.equalWithAbsError(v2) true if the elements of v1 and v2 are the same with an absolute error of no more than e, i.e., abs(v1[i] - v2[i]) <= e * abs(v1[i])

    C++ signature :
        bool equalWithRelError(Imath_3_1::Vec2<int> {lvalue},Imath_3_1::Vec2<int>,int)

equalWithRelError( (V2i)arg1, (object)arg2, (object)arg3) -> bool :

    C++ signature :
        bool equalWithRelError(Imath_3_1::Vec2<int>,boost::python::api::object,boost::python::api::object)'''
    ...
    def length2 (self, *args, **kwargs):
      '''
length2( (V2i)arg1) -> int :
    length2() square magnitude of the vector

    C++ signature :
        int length2(Imath_3_1::Vec2<int>)'''
    ...
    def negate (self, *args, **kwargs):
      '''
negate( (V2i)arg1) -> V2i :

    C++ signature :
        Imath_3_1::Vec2<int> negate(Imath_3_1::Vec2<int> {lvalue})'''
    ...
    def setValue (self, *args, **kwargs):
      '''
setValue( (V2i)arg1, (int)arg2, (int)arg3) -> None :

    C++ signature :
        void setValue(Imath_3_1::Vec2<int> {lvalue},int,int)'''
    ...
    def x (self, *args, **kwargs):
      '''None'''
    ...
    def y (self, *args, **kwargs):
      '''None'''
    ...

def V2i64 (*args):
      '''
__init__(boost::python::api::object, boost::python::api::object, boost::python::api::object)
__init__(boost::python::api::object, boost::python::api::object)
__init__(boost::python::api::object)
__init__(_object*, Imath_3_1::Vec2<long>)

'''      
    ...

class V2i64:
    def baseTypeEpsilon (self, *args, **kwargs):
      '''
baseTypeEpsilon() -> int :
    baseTypeEpsilon() epsilon value of the base type of the vector

    C++ signature :
        long baseTypeEpsilon()'''
    ...
    def baseTypeLowest (self, *args, **kwargs):
      '''
baseTypeLowest() -> int :
    baseTypeLowest() largest negative value of the base type of the vector

    C++ signature :
        long baseTypeLowest()'''
    ...
    def baseTypeMax (self, *args, **kwargs):
      '''
baseTypeMax() -> int :
    baseTypeMax() max value of the base type of the vector

    C++ signature :
        long baseTypeMax()'''
    ...
    def baseTypeSmallest (self, *args, **kwargs):
      '''
baseTypeSmallest() -> int :
    baseTypeSmallest() smallest value of the base type of the vector

    C++ signature :
        long baseTypeSmallest()'''
    ...
    def closestVertex (self, *args, **kwargs):
      '''
closestVertex( (V2i64)arg1, (V2i64)arg2, (V2i64)arg3, (V2i64)arg4) -> V2i64 :

    C++ signature :
        Imath_3_1::Vec2<long> closestVertex(Imath_3_1::Vec2<long> {lvalue},Imath_3_1::Vec2<long>,Imath_3_1::Vec2<long>,Imath_3_1::Vec2<long>)'''
    ...
    def cross (self, *args, **kwargs):
      '''
cross( (V2i64)arg1, (V2i64)arg2) -> int :
    v1.cross(v2) right handed cross product

    C++ signature :
        long cross(Imath_3_1::Vec2<long>,Imath_3_1::Vec2<long>)

cross( (V2i64)arg1, (V2i64Array)arg2) -> object :
    v1.cross(v2) right handed array cross product

    C++ signature :
        PyImath::FixedArray<long> cross(Imath_3_1::Vec2<long>,PyImath::FixedArray<Imath_3_1::Vec2<long> >)'''
    ...
    def dimensions (self, *args, **kwargs):
      '''
dimensions() -> int :
    dimensions() number of dimensions in the vector

    C++ signature :
        unsigned int dimensions()'''
    ...
    def dot (self, *args, **kwargs):
      '''
dot( (V2i64)arg1, (V2i64)arg2) -> int :
    v1.dot(v2) inner product of the two vectors

    C++ signature :
        long dot(Imath_3_1::Vec2<long>,Imath_3_1::Vec2<long>)

dot( (V2i64)arg1, (V2i64Array)arg2) -> object :
    v1.dot(v2) array inner product

    C++ signature :
        PyImath::FixedArray<long> dot(Imath_3_1::Vec2<long>,PyImath::FixedArray<Imath_3_1::Vec2<long> >)'''
    ...
    def equalWithAbsError (self, *args, **kwargs):
      '''
equalWithAbsError( (V2i64)arg1, (V2i64)arg2, (int)arg3) -> bool :
    v1.equalWithAbsError(v2) true if the elements of v1 and v2 are the same with an absolute error of no more than e, i.e., abs(v1[i] - v2[i]) <= e

    C++ signature :
        bool equalWithAbsError(Imath_3_1::Vec2<long> {lvalue},Imath_3_1::Vec2<long>,long)

equalWithAbsError( (V2i64)arg1, (object)arg2, (object)arg3) -> bool :

    C++ signature :
        bool equalWithAbsError(Imath_3_1::Vec2<long>,boost::python::api::object,boost::python::api::object)'''
    ...
    def equalWithRelError (self, *args, **kwargs):
      '''
equalWithRelError( (V2i64)arg1, (V2i64)arg2, (int)arg3) -> bool :
    v1.equalWithAbsError(v2) true if the elements of v1 and v2 are the same with an absolute error of no more than e, i.e., abs(v1[i] - v2[i]) <= e * abs(v1[i])

    C++ signature :
        bool equalWithRelError(Imath_3_1::Vec2<long> {lvalue},Imath_3_1::Vec2<long>,long)

equalWithRelError( (V2i64)arg1, (object)arg2, (object)arg3) -> bool :

    C++ signature :
        bool equalWithRelError(Imath_3_1::Vec2<long>,boost::python::api::object,boost::python::api::object)'''
    ...
    def length2 (self, *args, **kwargs):
      '''
length2( (V2i64)arg1) -> int :
    length2() square magnitude of the vector

    C++ signature :
        long length2(Imath_3_1::Vec2<long>)'''
    ...
    def negate (self, *args, **kwargs):
      '''
negate( (V2i64)arg1) -> V2i64 :

    C++ signature :
        Imath_3_1::Vec2<long> negate(Imath_3_1::Vec2<long> {lvalue})'''
    ...
    def setValue (self, *args, **kwargs):
      '''
setValue( (V2i64)arg1, (int)arg2, (int)arg3) -> None :

    C++ signature :
        void setValue(Imath_3_1::Vec2<long> {lvalue},long,long)'''
    ...
    def x (self, *args, **kwargs):
      '''None'''
    ...
    def y (self, *args, **kwargs):
      '''None'''
    ...

def V2i64Array (*args):
      '''
__init__(_object*, PyImath::FixedArray<Imath_3_1::Vec2<double> >)
__init__(_object*, PyImath::FixedArray<Imath_3_1::Vec2<float> >)
__init__(_object*, PyImath::FixedArray<Imath_3_1::Vec2<int> >)
__init__(_object*, PyImath::FixedArray<Imath_3_1::Vec2<short> >)
__init__(_object*, Imath_3_1::Vec2<long>, unsigned long)
__init__(_object*, PyImath::FixedArray<Imath_3_1::Vec2<long> >)
__init__(_object*, unsigned long)

'''      
    ...

class V2i64Array:
    def bounds (self, *args, **kwargs):
      '''
bounds( (V2i64Array)arg1) -> Box2i64 :

    C++ signature :
        Imath_3_1::Box<Imath_3_1::Vec2<long> > bounds(PyImath::FixedArray<Imath_3_1::Vec2<long> >)'''
    ...
    def cross (self, *args, **kwargs):
      '''
cross( (V2i64Array)arg1, (V2i64)x) -> object :
    cross(x) - return the cross product of (self,x)

    C++ signature :
        PyImath::FixedArray<long> cross(PyImath::FixedArray<Imath_3_1::Vec2<long> >,Imath_3_1::Vec2<long>)

cross( (V2i64Array)arg1, (V2i64Array)x) -> object :
    cross(x) - return the cross product of (self,x)

    C++ signature :
        PyImath::FixedArray<long> cross(PyImath::FixedArray<Imath_3_1::Vec2<long> >,PyImath::FixedArray<Imath_3_1::Vec2<long> >)'''
    ...
    def dot (self, *args, **kwargs):
      '''
dot( (V2i64Array)arg1, (V2i64)x) -> object :
    dot(x) - return the inner product of (self,x)

    C++ signature :
        PyImath::FixedArray<long> dot(PyImath::FixedArray<Imath_3_1::Vec2<long> >,Imath_3_1::Vec2<long>)

dot( (V2i64Array)arg1, (V2i64Array)x) -> object :
    dot(x) - return the inner product of (self,x)

    C++ signature :
        PyImath::FixedArray<long> dot(PyImath::FixedArray<Imath_3_1::Vec2<long> >,PyImath::FixedArray<Imath_3_1::Vec2<long> >)'''
    ...
    def ifelse (self, *args, **kwargs):
      '''
ifelse( (V2i64Array)arg1, (IntArray)arg2, (V2i64)arg3) -> V2i64Array :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec2<long> > ifelse(PyImath::FixedArray<Imath_3_1::Vec2<long> > {lvalue},PyImath::FixedArray<int>,Imath_3_1::Vec2<long>)

ifelse( (V2i64Array)arg1, (IntArray)arg2, (V2i64Array)arg3) -> V2i64Array :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec2<long> > ifelse(PyImath::FixedArray<Imath_3_1::Vec2<long> > {lvalue},PyImath::FixedArray<int>,PyImath::FixedArray<Imath_3_1::Vec2<long> >)'''
    ...
    def length2 (self, *args, **kwargs):
      '''
length2( (V2i64Array)arg1) -> object :

    C++ signature :
        PyImath::FixedArray<long> length2(PyImath::FixedArray<Imath_3_1::Vec2<long> >)'''
    ...
    def makeReadOnly (self, *args, **kwargs):
      '''
makeReadOnly( (V2i64Array)arg1) -> None :

    C++ signature :
        void makeReadOnly(PyImath::FixedArray<Imath_3_1::Vec2<long> > {lvalue})'''
    ...
    def max (self, *args, **kwargs):
      '''
max( (V2i64Array)arg1) -> V2i64 :

    C++ signature :
        Imath_3_1::Vec2<long> max(PyImath::FixedArray<Imath_3_1::Vec2<long> >)'''
    ...
    def min (self, *args, **kwargs):
      '''
min( (V2i64Array)arg1) -> V2i64 :

    C++ signature :
        Imath_3_1::Vec2<long> min(PyImath::FixedArray<Imath_3_1::Vec2<long> >)'''
    ...
    def reduce (self, *args, **kwargs):
      '''
reduce( (V2i64Array)arg1) -> V2i64 :

    C++ signature :
        Imath_3_1::Vec2<long> reduce(PyImath::FixedArray<Imath_3_1::Vec2<long> >)'''
    ...
    def writable (self, *args, **kwargs):
      '''
writable( (V2i64Array)arg1) -> bool :

    C++ signature :
        bool writable(PyImath::FixedArray<Imath_3_1::Vec2<long> > {lvalue})'''
    ...
    def x (self, *args, **kwargs):
      '''None'''
    ...
    def y (self, *args, **kwargs):
      '''None'''
    ...

def V2iArray (*args):
      '''
__init__(_object*, PyImath::FixedArray<Imath_3_1::Vec2<double> >)
__init__(_object*, PyImath::FixedArray<Imath_3_1::Vec2<float> >)
__init__(_object*, PyImath::FixedArray<Imath_3_1::Vec2<long> >)
__init__(_object*, PyImath::FixedArray<Imath_3_1::Vec2<short> >)
__init__(_object*, Imath_3_1::Vec2<int>, unsigned long)
__init__(_object*, PyImath::FixedArray<Imath_3_1::Vec2<int> >)
__init__(_object*, unsigned long)

'''      
    ...

class V2iArray:
    def bounds (self, *args, **kwargs):
      '''
bounds( (V2iArray)arg1) -> Box2i :

    C++ signature :
        Imath_3_1::Box<Imath_3_1::Vec2<int> > bounds(PyImath::FixedArray<Imath_3_1::Vec2<int> >)'''
    ...
    def cross (self, *args, **kwargs):
      '''
cross( (V2iArray)arg1, (V2i)x) -> IntArray :
    cross(x) - return the cross product of (self,x)

    C++ signature :
        PyImath::FixedArray<int> cross(PyImath::FixedArray<Imath_3_1::Vec2<int> >,Imath_3_1::Vec2<int>)

cross( (V2iArray)arg1, (V2iArray)x) -> IntArray :
    cross(x) - return the cross product of (self,x)

    C++ signature :
        PyImath::FixedArray<int> cross(PyImath::FixedArray<Imath_3_1::Vec2<int> >,PyImath::FixedArray<Imath_3_1::Vec2<int> >)'''
    ...
    def dot (self, *args, **kwargs):
      '''
dot( (V2iArray)arg1, (V2i)x) -> IntArray :
    dot(x) - return the inner product of (self,x)

    C++ signature :
        PyImath::FixedArray<int> dot(PyImath::FixedArray<Imath_3_1::Vec2<int> >,Imath_3_1::Vec2<int>)

dot( (V2iArray)arg1, (V2iArray)x) -> IntArray :
    dot(x) - return the inner product of (self,x)

    C++ signature :
        PyImath::FixedArray<int> dot(PyImath::FixedArray<Imath_3_1::Vec2<int> >,PyImath::FixedArray<Imath_3_1::Vec2<int> >)'''
    ...
    def ifelse (self, *args, **kwargs):
      '''
ifelse( (V2iArray)arg1, (IntArray)arg2, (V2i)arg3) -> V2iArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec2<int> > ifelse(PyImath::FixedArray<Imath_3_1::Vec2<int> > {lvalue},PyImath::FixedArray<int>,Imath_3_1::Vec2<int>)

ifelse( (V2iArray)arg1, (IntArray)arg2, (V2iArray)arg3) -> V2iArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec2<int> > ifelse(PyImath::FixedArray<Imath_3_1::Vec2<int> > {lvalue},PyImath::FixedArray<int>,PyImath::FixedArray<Imath_3_1::Vec2<int> >)'''
    ...
    def length2 (self, *args, **kwargs):
      '''
length2( (V2iArray)arg1) -> IntArray :

    C++ signature :
        PyImath::FixedArray<int> length2(PyImath::FixedArray<Imath_3_1::Vec2<int> >)'''
    ...
    def makeReadOnly (self, *args, **kwargs):
      '''
makeReadOnly( (V2iArray)arg1) -> None :

    C++ signature :
        void makeReadOnly(PyImath::FixedArray<Imath_3_1::Vec2<int> > {lvalue})'''
    ...
    def max (self, *args, **kwargs):
      '''
max( (V2iArray)arg1) -> V2i :

    C++ signature :
        Imath_3_1::Vec2<int> max(PyImath::FixedArray<Imath_3_1::Vec2<int> >)'''
    ...
    def min (self, *args, **kwargs):
      '''
min( (V2iArray)arg1) -> V2i :

    C++ signature :
        Imath_3_1::Vec2<int> min(PyImath::FixedArray<Imath_3_1::Vec2<int> >)'''
    ...
    def reduce (self, *args, **kwargs):
      '''
reduce( (V2iArray)arg1) -> V2i :

    C++ signature :
        Imath_3_1::Vec2<int> reduce(PyImath::FixedArray<Imath_3_1::Vec2<int> >)'''
    ...
    def writable (self, *args, **kwargs):
      '''
writable( (V2iArray)arg1) -> bool :

    C++ signature :
        bool writable(PyImath::FixedArray<Imath_3_1::Vec2<int> > {lvalue})'''
    ...
    def x (self, *args, **kwargs):
      '''None'''
    ...
    def y (self, *args, **kwargs):
      '''None'''
    ...

def V2iArrayFromBuffer (*args):
      '''

'''      
    ...

def V2s (*args):
      '''
__init__(boost::python::api::object, boost::python::api::object, boost::python::api::object)
__init__(boost::python::api::object, boost::python::api::object)
__init__(boost::python::api::object)
__init__(_object*, Imath_3_1::Vec2<short>)

'''      
    ...

class V2s:
    def baseTypeEpsilon (self, *args, **kwargs):
      '''
baseTypeEpsilon() -> int :
    baseTypeEpsilon() epsilon value of the base type of the vector

    C++ signature :
        short baseTypeEpsilon()'''
    ...
    def baseTypeLowest (self, *args, **kwargs):
      '''
baseTypeLowest() -> int :
    baseTypeLowest() largest negative value of the base type of the vector

    C++ signature :
        short baseTypeLowest()'''
    ...
    def baseTypeMax (self, *args, **kwargs):
      '''
baseTypeMax() -> int :
    baseTypeMax() max value of the base type of the vector

    C++ signature :
        short baseTypeMax()'''
    ...
    def baseTypeSmallest (self, *args, **kwargs):
      '''
baseTypeSmallest() -> int :
    baseTypeSmallest() smallest value of the base type of the vector

    C++ signature :
        short baseTypeSmallest()'''
    ...
    def closestVertex (self, *args, **kwargs):
      '''
closestVertex( (V2s)arg1, (V2s)arg2, (V2s)arg3, (V2s)arg4) -> V2s :

    C++ signature :
        Imath_3_1::Vec2<short> closestVertex(Imath_3_1::Vec2<short> {lvalue},Imath_3_1::Vec2<short>,Imath_3_1::Vec2<short>,Imath_3_1::Vec2<short>)'''
    ...
    def cross (self, *args, **kwargs):
      '''
cross( (V2s)arg1, (V2s)arg2) -> int :
    v1.cross(v2) right handed cross product

    C++ signature :
        short cross(Imath_3_1::Vec2<short>,Imath_3_1::Vec2<short>)

cross( (V2s)arg1, (V2sArray)arg2) -> ShortArray :
    v1.cross(v2) right handed array cross product

    C++ signature :
        PyImath::FixedArray<short> cross(Imath_3_1::Vec2<short>,PyImath::FixedArray<Imath_3_1::Vec2<short> >)'''
    ...
    def dimensions (self, *args, **kwargs):
      '''
dimensions() -> int :
    dimensions() number of dimensions in the vector

    C++ signature :
        unsigned int dimensions()'''
    ...
    def dot (self, *args, **kwargs):
      '''
dot( (V2s)arg1, (V2s)arg2) -> int :
    v1.dot(v2) inner product of the two vectors

    C++ signature :
        short dot(Imath_3_1::Vec2<short>,Imath_3_1::Vec2<short>)

dot( (V2s)arg1, (V2sArray)arg2) -> ShortArray :
    v1.dot(v2) array inner product

    C++ signature :
        PyImath::FixedArray<short> dot(Imath_3_1::Vec2<short>,PyImath::FixedArray<Imath_3_1::Vec2<short> >)'''
    ...
    def equalWithAbsError (self, *args, **kwargs):
      '''
equalWithAbsError( (V2s)arg1, (V2s)arg2, (int)arg3) -> bool :
    v1.equalWithAbsError(v2) true if the elements of v1 and v2 are the same with an absolute error of no more than e, i.e., abs(v1[i] - v2[i]) <= e

    C++ signature :
        bool equalWithAbsError(Imath_3_1::Vec2<short> {lvalue},Imath_3_1::Vec2<short>,short)

equalWithAbsError( (V2s)arg1, (object)arg2, (object)arg3) -> bool :

    C++ signature :
        bool equalWithAbsError(Imath_3_1::Vec2<short>,boost::python::api::object,boost::python::api::object)'''
    ...
    def equalWithRelError (self, *args, **kwargs):
      '''
equalWithRelError( (V2s)arg1, (V2s)arg2, (int)arg3) -> bool :
    v1.equalWithAbsError(v2) true if the elements of v1 and v2 are the same with an absolute error of no more than e, i.e., abs(v1[i] - v2[i]) <= e * abs(v1[i])

    C++ signature :
        bool equalWithRelError(Imath_3_1::Vec2<short> {lvalue},Imath_3_1::Vec2<short>,short)

equalWithRelError( (V2s)arg1, (object)arg2, (object)arg3) -> bool :

    C++ signature :
        bool equalWithRelError(Imath_3_1::Vec2<short>,boost::python::api::object,boost::python::api::object)'''
    ...
    def length2 (self, *args, **kwargs):
      '''
length2( (V2s)arg1) -> int :
    length2() square magnitude of the vector

    C++ signature :
        short length2(Imath_3_1::Vec2<short>)'''
    ...
    def negate (self, *args, **kwargs):
      '''
negate( (V2s)arg1) -> V2s :

    C++ signature :
        Imath_3_1::Vec2<short> negate(Imath_3_1::Vec2<short> {lvalue})'''
    ...
    def setValue (self, *args, **kwargs):
      '''
setValue( (V2s)arg1, (int)arg2, (int)arg3) -> None :

    C++ signature :
        void setValue(Imath_3_1::Vec2<short> {lvalue},short,short)'''
    ...
    def x (self, *args, **kwargs):
      '''None'''
    ...
    def y (self, *args, **kwargs):
      '''None'''
    ...

def V2sArray (*args):
      '''
__init__(_object*, PyImath::FixedArray<Imath_3_1::Vec2<double> >)
__init__(_object*, PyImath::FixedArray<Imath_3_1::Vec2<float> >)
__init__(_object*, PyImath::FixedArray<Imath_3_1::Vec2<long> >)
__init__(_object*, PyImath::FixedArray<Imath_3_1::Vec2<int> >)
__init__(_object*, Imath_3_1::Vec2<short>, unsigned long)
__init__(_object*, PyImath::FixedArray<Imath_3_1::Vec2<short> >)
__init__(_object*, unsigned long)

'''      
    ...

class V2sArray:
    def bounds (self, *args, **kwargs):
      '''
bounds( (V2sArray)arg1) -> Box2s :

    C++ signature :
        Imath_3_1::Box<Imath_3_1::Vec2<short> > bounds(PyImath::FixedArray<Imath_3_1::Vec2<short> >)'''
    ...
    def cross (self, *args, **kwargs):
      '''
cross( (V2sArray)arg1, (V2s)x) -> ShortArray :
    cross(x) - return the cross product of (self,x)

    C++ signature :
        PyImath::FixedArray<short> cross(PyImath::FixedArray<Imath_3_1::Vec2<short> >,Imath_3_1::Vec2<short>)

cross( (V2sArray)arg1, (V2sArray)x) -> ShortArray :
    cross(x) - return the cross product of (self,x)

    C++ signature :
        PyImath::FixedArray<short> cross(PyImath::FixedArray<Imath_3_1::Vec2<short> >,PyImath::FixedArray<Imath_3_1::Vec2<short> >)'''
    ...
    def dot (self, *args, **kwargs):
      '''
dot( (V2sArray)arg1, (V2s)x) -> ShortArray :
    dot(x) - return the inner product of (self,x)

    C++ signature :
        PyImath::FixedArray<short> dot(PyImath::FixedArray<Imath_3_1::Vec2<short> >,Imath_3_1::Vec2<short>)

dot( (V2sArray)arg1, (V2sArray)x) -> ShortArray :
    dot(x) - return the inner product of (self,x)

    C++ signature :
        PyImath::FixedArray<short> dot(PyImath::FixedArray<Imath_3_1::Vec2<short> >,PyImath::FixedArray<Imath_3_1::Vec2<short> >)'''
    ...
    def ifelse (self, *args, **kwargs):
      '''
ifelse( (V2sArray)arg1, (IntArray)arg2, (V2s)arg3) -> V2sArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec2<short> > ifelse(PyImath::FixedArray<Imath_3_1::Vec2<short> > {lvalue},PyImath::FixedArray<int>,Imath_3_1::Vec2<short>)

ifelse( (V2sArray)arg1, (IntArray)arg2, (V2sArray)arg3) -> V2sArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec2<short> > ifelse(PyImath::FixedArray<Imath_3_1::Vec2<short> > {lvalue},PyImath::FixedArray<int>,PyImath::FixedArray<Imath_3_1::Vec2<short> >)'''
    ...
    def length2 (self, *args, **kwargs):
      '''
length2( (V2sArray)arg1) -> ShortArray :

    C++ signature :
        PyImath::FixedArray<short> length2(PyImath::FixedArray<Imath_3_1::Vec2<short> >)'''
    ...
    def makeReadOnly (self, *args, **kwargs):
      '''
makeReadOnly( (V2sArray)arg1) -> None :

    C++ signature :
        void makeReadOnly(PyImath::FixedArray<Imath_3_1::Vec2<short> > {lvalue})'''
    ...
    def max (self, *args, **kwargs):
      '''
max( (V2sArray)arg1) -> V2s :

    C++ signature :
        Imath_3_1::Vec2<short> max(PyImath::FixedArray<Imath_3_1::Vec2<short> >)'''
    ...
    def min (self, *args, **kwargs):
      '''
min( (V2sArray)arg1) -> V2s :

    C++ signature :
        Imath_3_1::Vec2<short> min(PyImath::FixedArray<Imath_3_1::Vec2<short> >)'''
    ...
    def reduce (self, *args, **kwargs):
      '''
reduce( (V2sArray)arg1) -> V2s :

    C++ signature :
        Imath_3_1::Vec2<short> reduce(PyImath::FixedArray<Imath_3_1::Vec2<short> >)'''
    ...
    def writable (self, *args, **kwargs):
      '''
writable( (V2sArray)arg1) -> bool :

    C++ signature :
        bool writable(PyImath::FixedArray<Imath_3_1::Vec2<short> > {lvalue})'''
    ...
    def x (self, *args, **kwargs):
      '''None'''
    ...
    def y (self, *args, **kwargs):
      '''None'''
    ...

def V3c (*args):
      '''
__init__(boost::python::api::object, boost::python::api::object, boost::python::api::object, boost::python::api::object)
__init__(boost::python::api::object, boost::python::api::object)
__init__(boost::python::api::object)
__init__(_object*, Imath_3_1::Vec3<unsigned char>)

'''      
    ...

class V3c:
    def baseTypeEpsilon (self, *args, **kwargs):
      '''
baseTypeEpsilon() -> int :
    baseTypeEpsilon() epsilon value of the base type of the vector

    C++ signature :
        unsigned char baseTypeEpsilon()'''
    ...
    def baseTypeLowest (self, *args, **kwargs):
      '''
baseTypeLowest() -> int :
    baseTypeLowest() largest negative value of the base type of the vector

    C++ signature :
        unsigned char baseTypeLowest()'''
    ...
    def baseTypeMax (self, *args, **kwargs):
      '''
baseTypeMax() -> int :
    baseTypeMax() max value of the base type of the vector

    C++ signature :
        unsigned char baseTypeMax()'''
    ...
    def baseTypeSmallest (self, *args, **kwargs):
      '''
baseTypeSmallest() -> int :
    baseTypeSmallest() smallest value of the base type of the vector

    C++ signature :
        unsigned char baseTypeSmallest()'''
    ...
    def closestVertex (self, *args, **kwargs):
      '''
closestVertex( (V3c)arg1, (V3c)arg2, (V3c)arg3, (V3c)arg4) -> V3c :

    C++ signature :
        Imath_3_1::Vec3<unsigned char> closestVertex(Imath_3_1::Vec3<unsigned char> {lvalue},Imath_3_1::Vec3<unsigned char>,Imath_3_1::Vec3<unsigned char>,Imath_3_1::Vec3<unsigned char>)'''
    ...
    def cross (self, *args, **kwargs):
      '''
cross( (V3c)arg1, (V3c)arg2) -> V3c :
    v1.cross(v2) right handed cross product

    C++ signature :
        Imath_3_1::Vec3<unsigned char> cross(Imath_3_1::Vec3<unsigned char>,Imath_3_1::Vec3<unsigned char>)

cross( (V3c)arg1, (object)arg2) -> object :
    v1.cross(v2) right handed array cross product

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec3<unsigned char> > cross(Imath_3_1::Vec3<unsigned char>,PyImath::FixedArray<Imath_3_1::Vec3<unsigned char> >)'''
    ...
    def dimensions (self, *args, **kwargs):
      '''
dimensions() -> int :
    dimensions() number of dimensions in the vector

    C++ signature :
        unsigned int dimensions()'''
    ...
    def dot (self, *args, **kwargs):
      '''
dot( (V3c)arg1, (V3c)arg2) -> int :
    v1.dot(v2) inner product of the two vectors

    C++ signature :
        unsigned char dot(Imath_3_1::Vec3<unsigned char>,Imath_3_1::Vec3<unsigned char>)

dot( (V3c)arg1, (object)arg2) -> UnsignedCharArray :
    v1.dot(v2) array inner product

    C++ signature :
        PyImath::FixedArray<unsigned char> dot(Imath_3_1::Vec3<unsigned char>,PyImath::FixedArray<Imath_3_1::Vec3<unsigned char> >)'''
    ...
    def equalWithAbsError (self, *args, **kwargs):
      '''
equalWithAbsError( (V3c)arg1, (V3c)arg2, (int)arg3) -> bool :
    v1.equalWithAbsError(v2) true if the elements of v1 and v2 are the same with an absolute error of no more than e, i.e., abs(v1[i] - v2[i]) <= e

    C++ signature :
        bool equalWithAbsError(Imath_3_1::Vec3<unsigned char> {lvalue},Imath_3_1::Vec3<unsigned char>,unsigned char)

equalWithAbsError( (V3c)arg1, (object)arg2, (object)arg3) -> bool :

    C++ signature :
        bool equalWithAbsError(Imath_3_1::Vec3<unsigned char>,boost::python::api::object,boost::python::api::object)'''
    ...
    def equalWithRelError (self, *args, **kwargs):
      '''
equalWithRelError( (V3c)arg1, (V3c)arg2, (int)arg3) -> bool :
    v1.equalWithAbsError(v2) true if the elements of v1 and v2 are the same with an absolute error of no more than e, i.e., abs(v1[i] - v2[i]) <= e * abs(v1[i])

    C++ signature :
        bool equalWithRelError(Imath_3_1::Vec3<unsigned char> {lvalue},Imath_3_1::Vec3<unsigned char>,unsigned char)

equalWithRelError( (V3c)arg1, (object)arg2, (object)arg3) -> bool :

    C++ signature :
        bool equalWithRelError(Imath_3_1::Vec3<unsigned char>,boost::python::api::object,boost::python::api::object)'''
    ...
    def length2 (self, *args, **kwargs):
      '''
length2( (V3c)arg1) -> int :
    length2() square magnitude of the vector

    C++ signature :
        unsigned char length2(Imath_3_1::Vec3<unsigned char>)'''
    ...
    def negate (self, *args, **kwargs):
      '''
negate( (V3c)arg1) -> V3c :

    C++ signature :
        Imath_3_1::Vec3<unsigned char> negate(Imath_3_1::Vec3<unsigned char> {lvalue})'''
    ...
    def setValue (self, *args, **kwargs):
      '''
setValue( (V3c)arg1, (int)arg2, (int)arg3, (int)arg4) -> None :

    C++ signature :
        void setValue(Imath_3_1::Vec3<unsigned char> {lvalue},unsigned char,unsigned char,unsigned char)'''
    ...
    def x (self, *args, **kwargs):
      '''None'''
    ...
    def y (self, *args, **kwargs):
      '''None'''
    ...
    def z (self, *args, **kwargs):
      '''None'''
    ...

def V3d (*args):
      '''
__init__(boost::python::api::object, boost::python::api::object, boost::python::api::object, boost::python::api::object)
__init__(boost::python::api::object, boost::python::api::object)
__init__(boost::python::api::object)
__init__(_object*, Imath_3_1::Vec3<double>)

'''      
    ...

class V3d:
    def baseTypeEpsilon (self, *args, **kwargs):
      '''
baseTypeEpsilon() -> float :
    baseTypeEpsilon() epsilon value of the base type of the vector

    C++ signature :
        double baseTypeEpsilon()'''
    ...
    def baseTypeLowest (self, *args, **kwargs):
      '''
baseTypeLowest() -> float :
    baseTypeLowest() largest negative value of the base type of the vector

    C++ signature :
        double baseTypeLowest()'''
    ...
    def baseTypeMax (self, *args, **kwargs):
      '''
baseTypeMax() -> float :
    baseTypeMax() max value of the base type of the vector

    C++ signature :
        double baseTypeMax()'''
    ...
    def baseTypeSmallest (self, *args, **kwargs):
      '''
baseTypeSmallest() -> float :
    baseTypeSmallest() smallest value of the base type of the vector

    C++ signature :
        double baseTypeSmallest()'''
    ...
    def closestVertex (self, *args, **kwargs):
      '''
closestVertex( (V3d)arg1, (V3d)arg2, (V3d)arg3, (V3d)arg4) -> V3d :

    C++ signature :
        Imath_3_1::Vec3<double> closestVertex(Imath_3_1::Vec3<double> {lvalue},Imath_3_1::Vec3<double>,Imath_3_1::Vec3<double>,Imath_3_1::Vec3<double>)'''
    ...
    def cross (self, *args, **kwargs):
      '''
cross( (V3d)arg1, (V3d)arg2) -> V3d :
    v1.cross(v2) right handed cross product

    C++ signature :
        Imath_3_1::Vec3<double> cross(Imath_3_1::Vec3<double>,Imath_3_1::Vec3<double>)

cross( (V3d)arg1, (V3dArray)arg2) -> V3dArray :
    v1.cross(v2) right handed array cross product

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec3<double> > cross(Imath_3_1::Vec3<double>,PyImath::FixedArray<Imath_3_1::Vec3<double> >)'''
    ...
    def dimensions (self, *args, **kwargs):
      '''
dimensions() -> int :
    dimensions() number of dimensions in the vector

    C++ signature :
        unsigned int dimensions()'''
    ...
    def dot (self, *args, **kwargs):
      '''
dot( (V3d)arg1, (V3d)arg2) -> float :
    v1.dot(v2) inner product of the two vectors

    C++ signature :
        double dot(Imath_3_1::Vec3<double>,Imath_3_1::Vec3<double>)

dot( (V3d)arg1, (V3dArray)arg2) -> DoubleArray :
    v1.dot(v2) array inner product

    C++ signature :
        PyImath::FixedArray<double> dot(Imath_3_1::Vec3<double>,PyImath::FixedArray<Imath_3_1::Vec3<double> >)'''
    ...
    def equalWithAbsError (self, *args, **kwargs):
      '''
equalWithAbsError( (V3d)arg1, (V3d)arg2, (float)arg3) -> bool :
    v1.equalWithAbsError(v2) true if the elements of v1 and v2 are the same with an absolute error of no more than e, i.e., abs(v1[i] - v2[i]) <= e

    C++ signature :
        bool equalWithAbsError(Imath_3_1::Vec3<double> {lvalue},Imath_3_1::Vec3<double>,double)

equalWithAbsError( (V3d)arg1, (object)arg2, (object)arg3) -> bool :

    C++ signature :
        bool equalWithAbsError(Imath_3_1::Vec3<double>,boost::python::api::object,boost::python::api::object)'''
    ...
    def equalWithRelError (self, *args, **kwargs):
      '''
equalWithRelError( (V3d)arg1, (V3d)arg2, (float)arg3) -> bool :
    v1.equalWithAbsError(v2) true if the elements of v1 and v2 are the same with an absolute error of no more than e, i.e., abs(v1[i] - v2[i]) <= e * abs(v1[i])

    C++ signature :
        bool equalWithRelError(Imath_3_1::Vec3<double> {lvalue},Imath_3_1::Vec3<double>,double)

equalWithRelError( (V3d)arg1, (object)arg2, (object)arg3) -> bool :

    C++ signature :
        bool equalWithRelError(Imath_3_1::Vec3<double>,boost::python::api::object,boost::python::api::object)'''
    ...
    def length (self, *args, **kwargs):
      '''
length( (V3d)arg1) -> float :
    length() magnitude of the vector

    C++ signature :
        double length(Imath_3_1::Vec3<double>)'''
    ...
    def length2 (self, *args, **kwargs):
      '''
length2( (V3d)arg1) -> float :
    length2() square magnitude of the vector

    C++ signature :
        double length2(Imath_3_1::Vec3<double>)'''
    ...
    def negate (self, *args, **kwargs):
      '''
negate( (V3d)arg1) -> V3d :

    C++ signature :
        Imath_3_1::Vec3<double> negate(Imath_3_1::Vec3<double> {lvalue})'''
    ...
    def normalize (self, *args, **kwargs):
      '''
normalize( (V3d)arg1) -> V3d :
    v.normalize() destructively normalizes v and returns a reference to it

    C++ signature :
        Imath_3_1::Vec3<double> normalize(Imath_3_1::Vec3<double> {lvalue})'''
    ...
    def normalizeExc (self, *args, **kwargs):
      '''
normalizeExc( (V3d)arg1) -> V3d :
    v.normalizeExc() destructively normalizes V and returns a reference to it, throwing an exception if length() == 0

    C++ signature :
        Imath_3_1::Vec3<double> normalizeExc(Imath_3_1::Vec3<double> {lvalue})'''
    ...
    def normalizeNonNull (self, *args, **kwargs):
      '''
normalizeNonNull( (V3d)arg1) -> V3d :
    v.normalizeNonNull() destructively normalizes V and returns a reference to it, faster if lngth() != 0

    C++ signature :
        Imath_3_1::Vec3<double> normalizeNonNull(Imath_3_1::Vec3<double> {lvalue})'''
    ...
    def normalized (self, *args, **kwargs):
      '''
normalized( (V3d)arg1) -> V3d :
    v.normalized() returns a normalized copy of v

    C++ signature :
        Imath_3_1::Vec3<double> normalized(Imath_3_1::Vec3<double>)'''
    ...
    def normalizedExc (self, *args, **kwargs):
      '''
normalizedExc( (V3d)arg1) -> V3d :
    v.normalizedExc() returns a normalized copy of v, throwing an exception if length() == 0

    C++ signature :
        Imath_3_1::Vec3<double> normalizedExc(Imath_3_1::Vec3<double>)'''
    ...
    def normalizedNonNull (self, *args, **kwargs):
      '''
normalizedNonNull( (V3d)arg1) -> V3d :
    v.normalizedNonNull() returns a normalized copy of v, faster if lngth() != 0

    C++ signature :
        Imath_3_1::Vec3<double> normalizedNonNull(Imath_3_1::Vec3<double>)'''
    ...
    def orthogonal (self, *args, **kwargs):
      '''
orthogonal( (V3d)arg1, (V3d)arg2) -> V3d :

    C++ signature :
        Imath_3_1::Vec3<double> orthogonal(Imath_3_1::Vec3<double>,Imath_3_1::Vec3<double>)'''
    ...
    def project (self, *args, **kwargs):
      '''
project( (V3d)arg1, (V3d)arg2) -> V3d :

    C++ signature :
        Imath_3_1::Vec3<double> project(Imath_3_1::Vec3<double>,Imath_3_1::Vec3<double>)'''
    ...
    def reflect (self, *args, **kwargs):
      '''
reflect( (V3d)arg1, (V3d)arg2) -> V3d :

    C++ signature :
        Imath_3_1::Vec3<double> reflect(Imath_3_1::Vec3<double>,Imath_3_1::Vec3<double>)'''
    ...
    def setValue (self, *args, **kwargs):
      '''
setValue( (V3d)arg1, (float)arg2, (float)arg3, (float)arg4) -> None :

    C++ signature :
        void setValue(Imath_3_1::Vec3<double> {lvalue},double,double,double)'''
    ...
    def x (self, *args, **kwargs):
      '''None'''
    ...
    def y (self, *args, **kwargs):
      '''None'''
    ...
    def z (self, *args, **kwargs):
      '''None'''
    ...

def V3dArray (*args):
      '''
__init__(_object*, PyImath::FixedArray<Imath_3_1::Vec3<float> >)
__init__(_object*, PyImath::FixedArray<Imath_3_1::Vec3<long> >)
__init__(_object*, PyImath::FixedArray<Imath_3_1::Vec3<int> >)
__init__(_object*, PyImath::FixedArray<Imath_3_1::Vec3<short> >)
__init__(_object*, Imath_3_1::Vec3<double>, unsigned long)
__init__(_object*, PyImath::FixedArray<Imath_3_1::Vec3<double> >)
__init__(_object*, unsigned long)

'''      
    ...

class V3dArray:
    def bounds (self, *args, **kwargs):
      '''
bounds( (V3dArray)arg1) -> Box3d :

    C++ signature :
        Imath_3_1::Box<Imath_3_1::Vec3<double> > bounds(PyImath::FixedArray<Imath_3_1::Vec3<double> >)'''
    ...
    def cross (self, *args, **kwargs):
      '''
cross( (V3dArray)arg1, (V3d)x) -> V3dArray :
    cross(x) - return the cross product of (self,x)

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec3<double> > cross(PyImath::FixedArray<Imath_3_1::Vec3<double> >,Imath_3_1::Vec3<double>)

cross( (V3dArray)arg1, (V3dArray)x) -> V3dArray :
    cross(x) - return the cross product of (self,x)

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec3<double> > cross(PyImath::FixedArray<Imath_3_1::Vec3<double> >,PyImath::FixedArray<Imath_3_1::Vec3<double> >)'''
    ...
    def dot (self, *args, **kwargs):
      '''
dot( (V3dArray)arg1, (V3d)x) -> DoubleArray :
    dot(x) - return the inner product of (self,x)

    C++ signature :
        PyImath::FixedArray<double> dot(PyImath::FixedArray<Imath_3_1::Vec3<double> >,Imath_3_1::Vec3<double>)

dot( (V3dArray)arg1, (V3dArray)x) -> DoubleArray :
    dot(x) - return the inner product of (self,x)

    C++ signature :
        PyImath::FixedArray<double> dot(PyImath::FixedArray<Imath_3_1::Vec3<double> >,PyImath::FixedArray<Imath_3_1::Vec3<double> >)'''
    ...
    def ifelse (self, *args, **kwargs):
      '''
ifelse( (V3dArray)arg1, (IntArray)arg2, (V3d)arg3) -> V3dArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec3<double> > ifelse(PyImath::FixedArray<Imath_3_1::Vec3<double> > {lvalue},PyImath::FixedArray<int>,Imath_3_1::Vec3<double>)

ifelse( (V3dArray)arg1, (IntArray)arg2, (V3dArray)arg3) -> V3dArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec3<double> > ifelse(PyImath::FixedArray<Imath_3_1::Vec3<double> > {lvalue},PyImath::FixedArray<int>,PyImath::FixedArray<Imath_3_1::Vec3<double> >)'''
    ...
    def length (self, *args, **kwargs):
      '''
length( (V3dArray)arg1) -> DoubleArray :

    C++ signature :
        PyImath::FixedArray<double> length(PyImath::FixedArray<Imath_3_1::Vec3<double> >)'''
    ...
    def length2 (self, *args, **kwargs):
      '''
length2( (V3dArray)arg1) -> DoubleArray :

    C++ signature :
        PyImath::FixedArray<double> length2(PyImath::FixedArray<Imath_3_1::Vec3<double> >)'''
    ...
    def makeReadOnly (self, *args, **kwargs):
      '''
makeReadOnly( (V3dArray)arg1) -> None :

    C++ signature :
        void makeReadOnly(PyImath::FixedArray<Imath_3_1::Vec3<double> > {lvalue})'''
    ...
    def max (self, *args, **kwargs):
      '''
max( (V3dArray)arg1) -> V3d :

    C++ signature :
        Imath_3_1::Vec3<double> max(PyImath::FixedArray<Imath_3_1::Vec3<double> >)'''
    ...
    def min (self, *args, **kwargs):
      '''
min( (V3dArray)arg1) -> V3d :

    C++ signature :
        Imath_3_1::Vec3<double> min(PyImath::FixedArray<Imath_3_1::Vec3<double> >)'''
    ...
    def normalize (self, *args, **kwargs):
      '''
normalize( (V3dArray)arg1) -> V3dArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec3<double> > {lvalue} normalize(PyImath::FixedArray<Imath_3_1::Vec3<double> > {lvalue})'''
    ...
    def normalizeExc (self, *args, **kwargs):
      '''
normalizeExc( (V3dArray)arg1) -> V3dArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec3<double> > {lvalue} normalizeExc(PyImath::FixedArray<Imath_3_1::Vec3<double> > {lvalue})'''
    ...
    def normalized (self, *args, **kwargs):
      '''
normalized( (V3dArray)arg1) -> V3dArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec3<double> > normalized(PyImath::FixedArray<Imath_3_1::Vec3<double> >)'''
    ...
    def normalizedExc (self, *args, **kwargs):
      '''
normalizedExc( (V3dArray)arg1) -> V3dArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec3<double> > normalizedExc(PyImath::FixedArray<Imath_3_1::Vec3<double> >)'''
    ...
    def reduce (self, *args, **kwargs):
      '''
reduce( (V3dArray)arg1) -> V3d :

    C++ signature :
        Imath_3_1::Vec3<double> reduce(PyImath::FixedArray<Imath_3_1::Vec3<double> >)'''
    ...
    def writable (self, *args, **kwargs):
      '''
writable( (V3dArray)arg1) -> bool :

    C++ signature :
        bool writable(PyImath::FixedArray<Imath_3_1::Vec3<double> > {lvalue})'''
    ...
    def x (self, *args, **kwargs):
      '''None'''
    ...
    def y (self, *args, **kwargs):
      '''None'''
    ...
    def z (self, *args, **kwargs):
      '''None'''
    ...

def V3dArrayFromBuffer (*args):
      '''

'''      
    ...

def V3f (*args):
      '''
__init__(boost::python::api::object, boost::python::api::object, boost::python::api::object, boost::python::api::object)
__init__(boost::python::api::object, boost::python::api::object)
__init__(boost::python::api::object)
__init__(_object*, Imath_3_1::Vec3<float>)

'''      
    ...

class V3f:
    def baseTypeEpsilon (self, *args, **kwargs):
      '''
baseTypeEpsilon() -> float :
    baseTypeEpsilon() epsilon value of the base type of the vector

    C++ signature :
        float baseTypeEpsilon()'''
    ...
    def baseTypeLowest (self, *args, **kwargs):
      '''
baseTypeLowest() -> float :
    baseTypeLowest() largest negative value of the base type of the vector

    C++ signature :
        float baseTypeLowest()'''
    ...
    def baseTypeMax (self, *args, **kwargs):
      '''
baseTypeMax() -> float :
    baseTypeMax() max value of the base type of the vector

    C++ signature :
        float baseTypeMax()'''
    ...
    def baseTypeSmallest (self, *args, **kwargs):
      '''
baseTypeSmallest() -> float :
    baseTypeSmallest() smallest value of the base type of the vector

    C++ signature :
        float baseTypeSmallest()'''
    ...
    def closestVertex (self, *args, **kwargs):
      '''
closestVertex( (V3f)arg1, (V3f)arg2, (V3f)arg3, (V3f)arg4) -> V3f :

    C++ signature :
        Imath_3_1::Vec3<float> closestVertex(Imath_3_1::Vec3<float> {lvalue},Imath_3_1::Vec3<float>,Imath_3_1::Vec3<float>,Imath_3_1::Vec3<float>)'''
    ...
    def cross (self, *args, **kwargs):
      '''
cross( (V3f)arg1, (V3f)arg2) -> V3f :
    v1.cross(v2) right handed cross product

    C++ signature :
        Imath_3_1::Vec3<float> cross(Imath_3_1::Vec3<float>,Imath_3_1::Vec3<float>)

cross( (V3f)arg1, (V3fArray)arg2) -> V3fArray :
    v1.cross(v2) right handed array cross product

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec3<float> > cross(Imath_3_1::Vec3<float>,PyImath::FixedArray<Imath_3_1::Vec3<float> >)'''
    ...
    def dimensions (self, *args, **kwargs):
      '''
dimensions() -> int :
    dimensions() number of dimensions in the vector

    C++ signature :
        unsigned int dimensions()'''
    ...
    def dot (self, *args, **kwargs):
      '''
dot( (V3f)arg1, (V3f)arg2) -> float :
    v1.dot(v2) inner product of the two vectors

    C++ signature :
        float dot(Imath_3_1::Vec3<float>,Imath_3_1::Vec3<float>)

dot( (V3f)arg1, (V3fArray)arg2) -> FloatArray :
    v1.dot(v2) array inner product

    C++ signature :
        PyImath::FixedArray<float> dot(Imath_3_1::Vec3<float>,PyImath::FixedArray<Imath_3_1::Vec3<float> >)'''
    ...
    def equalWithAbsError (self, *args, **kwargs):
      '''
equalWithAbsError( (V3f)arg1, (V3f)arg2, (float)arg3) -> bool :
    v1.equalWithAbsError(v2) true if the elements of v1 and v2 are the same with an absolute error of no more than e, i.e., abs(v1[i] - v2[i]) <= e

    C++ signature :
        bool equalWithAbsError(Imath_3_1::Vec3<float> {lvalue},Imath_3_1::Vec3<float>,float)

equalWithAbsError( (V3f)arg1, (object)arg2, (object)arg3) -> bool :

    C++ signature :
        bool equalWithAbsError(Imath_3_1::Vec3<float>,boost::python::api::object,boost::python::api::object)'''
    ...
    def equalWithRelError (self, *args, **kwargs):
      '''
equalWithRelError( (V3f)arg1, (V3f)arg2, (float)arg3) -> bool :
    v1.equalWithAbsError(v2) true if the elements of v1 and v2 are the same with an absolute error of no more than e, i.e., abs(v1[i] - v2[i]) <= e * abs(v1[i])

    C++ signature :
        bool equalWithRelError(Imath_3_1::Vec3<float> {lvalue},Imath_3_1::Vec3<float>,float)

equalWithRelError( (V3f)arg1, (object)arg2, (object)arg3) -> bool :

    C++ signature :
        bool equalWithRelError(Imath_3_1::Vec3<float>,boost::python::api::object,boost::python::api::object)'''
    ...
    def length (self, *args, **kwargs):
      '''
length( (V3f)arg1) -> float :
    length() magnitude of the vector

    C++ signature :
        float length(Imath_3_1::Vec3<float>)'''
    ...
    def length2 (self, *args, **kwargs):
      '''
length2( (V3f)arg1) -> float :
    length2() square magnitude of the vector

    C++ signature :
        float length2(Imath_3_1::Vec3<float>)'''
    ...
    def negate (self, *args, **kwargs):
      '''
negate( (V3f)arg1) -> V3f :

    C++ signature :
        Imath_3_1::Vec3<float> negate(Imath_3_1::Vec3<float> {lvalue})'''
    ...
    def normalize (self, *args, **kwargs):
      '''
normalize( (V3f)arg1) -> V3f :
    v.normalize() destructively normalizes v and returns a reference to it

    C++ signature :
        Imath_3_1::Vec3<float> normalize(Imath_3_1::Vec3<float> {lvalue})'''
    ...
    def normalizeExc (self, *args, **kwargs):
      '''
normalizeExc( (V3f)arg1) -> V3f :
    v.normalizeExc() destructively normalizes V and returns a reference to it, throwing an exception if length() == 0

    C++ signature :
        Imath_3_1::Vec3<float> normalizeExc(Imath_3_1::Vec3<float> {lvalue})'''
    ...
    def normalizeNonNull (self, *args, **kwargs):
      '''
normalizeNonNull( (V3f)arg1) -> V3f :
    v.normalizeNonNull() destructively normalizes V and returns a reference to it, faster if lngth() != 0

    C++ signature :
        Imath_3_1::Vec3<float> normalizeNonNull(Imath_3_1::Vec3<float> {lvalue})'''
    ...
    def normalized (self, *args, **kwargs):
      '''
normalized( (V3f)arg1) -> V3f :
    v.normalized() returns a normalized copy of v

    C++ signature :
        Imath_3_1::Vec3<float> normalized(Imath_3_1::Vec3<float>)'''
    ...
    def normalizedExc (self, *args, **kwargs):
      '''
normalizedExc( (V3f)arg1) -> V3f :
    v.normalizedExc() returns a normalized copy of v, throwing an exception if length() == 0

    C++ signature :
        Imath_3_1::Vec3<float> normalizedExc(Imath_3_1::Vec3<float>)'''
    ...
    def normalizedNonNull (self, *args, **kwargs):
      '''
normalizedNonNull( (V3f)arg1) -> V3f :
    v.normalizedNonNull() returns a normalized copy of v, faster if lngth() != 0

    C++ signature :
        Imath_3_1::Vec3<float> normalizedNonNull(Imath_3_1::Vec3<float>)'''
    ...
    def orthogonal (self, *args, **kwargs):
      '''
orthogonal( (V3f)arg1, (V3f)arg2) -> V3f :

    C++ signature :
        Imath_3_1::Vec3<float> orthogonal(Imath_3_1::Vec3<float>,Imath_3_1::Vec3<float>)'''
    ...
    def project (self, *args, **kwargs):
      '''
project( (V3f)arg1, (V3f)arg2) -> V3f :

    C++ signature :
        Imath_3_1::Vec3<float> project(Imath_3_1::Vec3<float>,Imath_3_1::Vec3<float>)'''
    ...
    def reflect (self, *args, **kwargs):
      '''
reflect( (V3f)arg1, (V3f)arg2) -> V3f :

    C++ signature :
        Imath_3_1::Vec3<float> reflect(Imath_3_1::Vec3<float>,Imath_3_1::Vec3<float>)'''
    ...
    def setValue (self, *args, **kwargs):
      '''
setValue( (V3f)arg1, (float)arg2, (float)arg3, (float)arg4) -> None :

    C++ signature :
        void setValue(Imath_3_1::Vec3<float> {lvalue},float,float,float)'''
    ...
    def x (self, *args, **kwargs):
      '''None'''
    ...
    def y (self, *args, **kwargs):
      '''None'''
    ...
    def z (self, *args, **kwargs):
      '''None'''
    ...

def V3fArray (*args):
      '''
__init__(_object*, PyImath::FixedArray<Imath_3_1::Vec3<double> >)
__init__(_object*, PyImath::FixedArray<Imath_3_1::Vec3<long> >)
__init__(_object*, PyImath::FixedArray<Imath_3_1::Vec3<int> >)
__init__(_object*, PyImath::FixedArray<Imath_3_1::Vec3<short> >)
__init__(_object*, Imath_3_1::Vec3<float>, unsigned long)
__init__(_object*, PyImath::FixedArray<Imath_3_1::Vec3<float> >)
__init__(_object*, unsigned long)

'''      
    ...

class V3fArray:
    def bounds (self, *args, **kwargs):
      '''
bounds( (V3fArray)arg1) -> Box3f :

    C++ signature :
        Imath_3_1::Box<Imath_3_1::Vec3<float> > bounds(PyImath::FixedArray<Imath_3_1::Vec3<float> >)'''
    ...
    def cross (self, *args, **kwargs):
      '''
cross( (V3fArray)arg1, (V3f)x) -> V3fArray :
    cross(x) - return the cross product of (self,x)

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec3<float> > cross(PyImath::FixedArray<Imath_3_1::Vec3<float> >,Imath_3_1::Vec3<float>)

cross( (V3fArray)arg1, (V3fArray)x) -> V3fArray :
    cross(x) - return the cross product of (self,x)

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec3<float> > cross(PyImath::FixedArray<Imath_3_1::Vec3<float> >,PyImath::FixedArray<Imath_3_1::Vec3<float> >)'''
    ...
    def dot (self, *args, **kwargs):
      '''
dot( (V3fArray)arg1, (V3f)x) -> FloatArray :
    dot(x) - return the inner product of (self,x)

    C++ signature :
        PyImath::FixedArray<float> dot(PyImath::FixedArray<Imath_3_1::Vec3<float> >,Imath_3_1::Vec3<float>)

dot( (V3fArray)arg1, (V3fArray)x) -> FloatArray :
    dot(x) - return the inner product of (self,x)

    C++ signature :
        PyImath::FixedArray<float> dot(PyImath::FixedArray<Imath_3_1::Vec3<float> >,PyImath::FixedArray<Imath_3_1::Vec3<float> >)'''
    ...
    def ifelse (self, *args, **kwargs):
      '''
ifelse( (V3fArray)arg1, (IntArray)arg2, (V3f)arg3) -> V3fArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec3<float> > ifelse(PyImath::FixedArray<Imath_3_1::Vec3<float> > {lvalue},PyImath::FixedArray<int>,Imath_3_1::Vec3<float>)

ifelse( (V3fArray)arg1, (IntArray)arg2, (V3fArray)arg3) -> V3fArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec3<float> > ifelse(PyImath::FixedArray<Imath_3_1::Vec3<float> > {lvalue},PyImath::FixedArray<int>,PyImath::FixedArray<Imath_3_1::Vec3<float> >)'''
    ...
    def length (self, *args, **kwargs):
      '''
length( (V3fArray)arg1) -> FloatArray :

    C++ signature :
        PyImath::FixedArray<float> length(PyImath::FixedArray<Imath_3_1::Vec3<float> >)'''
    ...
    def length2 (self, *args, **kwargs):
      '''
length2( (V3fArray)arg1) -> FloatArray :

    C++ signature :
        PyImath::FixedArray<float> length2(PyImath::FixedArray<Imath_3_1::Vec3<float> >)'''
    ...
    def makeReadOnly (self, *args, **kwargs):
      '''
makeReadOnly( (V3fArray)arg1) -> None :

    C++ signature :
        void makeReadOnly(PyImath::FixedArray<Imath_3_1::Vec3<float> > {lvalue})'''
    ...
    def max (self, *args, **kwargs):
      '''
max( (V3fArray)arg1) -> V3f :

    C++ signature :
        Imath_3_1::Vec3<float> max(PyImath::FixedArray<Imath_3_1::Vec3<float> >)'''
    ...
    def min (self, *args, **kwargs):
      '''
min( (V3fArray)arg1) -> V3f :

    C++ signature :
        Imath_3_1::Vec3<float> min(PyImath::FixedArray<Imath_3_1::Vec3<float> >)'''
    ...
    def normalize (self, *args, **kwargs):
      '''
normalize( (V3fArray)arg1) -> V3fArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec3<float> > {lvalue} normalize(PyImath::FixedArray<Imath_3_1::Vec3<float> > {lvalue})'''
    ...
    def normalizeExc (self, *args, **kwargs):
      '''
normalizeExc( (V3fArray)arg1) -> V3fArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec3<float> > {lvalue} normalizeExc(PyImath::FixedArray<Imath_3_1::Vec3<float> > {lvalue})'''
    ...
    def normalized (self, *args, **kwargs):
      '''
normalized( (V3fArray)arg1) -> V3fArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec3<float> > normalized(PyImath::FixedArray<Imath_3_1::Vec3<float> >)'''
    ...
    def normalizedExc (self, *args, **kwargs):
      '''
normalizedExc( (V3fArray)arg1) -> V3fArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec3<float> > normalizedExc(PyImath::FixedArray<Imath_3_1::Vec3<float> >)'''
    ...
    def reduce (self, *args, **kwargs):
      '''
reduce( (V3fArray)arg1) -> V3f :

    C++ signature :
        Imath_3_1::Vec3<float> reduce(PyImath::FixedArray<Imath_3_1::Vec3<float> >)'''
    ...
    def writable (self, *args, **kwargs):
      '''
writable( (V3fArray)arg1) -> bool :

    C++ signature :
        bool writable(PyImath::FixedArray<Imath_3_1::Vec3<float> > {lvalue})'''
    ...
    def x (self, *args, **kwargs):
      '''None'''
    ...
    def y (self, *args, **kwargs):
      '''None'''
    ...
    def z (self, *args, **kwargs):
      '''None'''
    ...

def V3fArrayFromBuffer (*args):
      '''

'''      
    ...

def V3i (*args):
      '''
__init__(boost::python::api::object, boost::python::api::object, boost::python::api::object, boost::python::api::object)
__init__(boost::python::api::object, boost::python::api::object)
__init__(boost::python::api::object)
__init__(_object*, Imath_3_1::Vec3<int>)

'''      
    ...

class V3i:
    def baseTypeEpsilon (self, *args, **kwargs):
      '''
baseTypeEpsilon() -> int :
    baseTypeEpsilon() epsilon value of the base type of the vector

    C++ signature :
        int baseTypeEpsilon()'''
    ...
    def baseTypeLowest (self, *args, **kwargs):
      '''
baseTypeLowest() -> int :
    baseTypeLowest() largest negative value of the base type of the vector

    C++ signature :
        int baseTypeLowest()'''
    ...
    def baseTypeMax (self, *args, **kwargs):
      '''
baseTypeMax() -> int :
    baseTypeMax() max value of the base type of the vector

    C++ signature :
        int baseTypeMax()'''
    ...
    def baseTypeSmallest (self, *args, **kwargs):
      '''
baseTypeSmallest() -> int :
    baseTypeSmallest() smallest value of the base type of the vector

    C++ signature :
        int baseTypeSmallest()'''
    ...
    def closestVertex (self, *args, **kwargs):
      '''
closestVertex( (V3i)arg1, (V3i)arg2, (V3i)arg3, (V3i)arg4) -> V3i :

    C++ signature :
        Imath_3_1::Vec3<int> closestVertex(Imath_3_1::Vec3<int> {lvalue},Imath_3_1::Vec3<int>,Imath_3_1::Vec3<int>,Imath_3_1::Vec3<int>)'''
    ...
    def cross (self, *args, **kwargs):
      '''
cross( (V3i)arg1, (V3i)arg2) -> V3i :
    v1.cross(v2) right handed cross product

    C++ signature :
        Imath_3_1::Vec3<int> cross(Imath_3_1::Vec3<int>,Imath_3_1::Vec3<int>)

cross( (V3i)arg1, (V3iArray)arg2) -> V3iArray :
    v1.cross(v2) right handed array cross product

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec3<int> > cross(Imath_3_1::Vec3<int>,PyImath::FixedArray<Imath_3_1::Vec3<int> >)'''
    ...
    def dimensions (self, *args, **kwargs):
      '''
dimensions() -> int :
    dimensions() number of dimensions in the vector

    C++ signature :
        unsigned int dimensions()'''
    ...
    def dot (self, *args, **kwargs):
      '''
dot( (V3i)arg1, (V3i)arg2) -> int :
    v1.dot(v2) inner product of the two vectors

    C++ signature :
        int dot(Imath_3_1::Vec3<int>,Imath_3_1::Vec3<int>)

dot( (V3i)arg1, (V3iArray)arg2) -> IntArray :
    v1.dot(v2) array inner product

    C++ signature :
        PyImath::FixedArray<int> dot(Imath_3_1::Vec3<int>,PyImath::FixedArray<Imath_3_1::Vec3<int> >)'''
    ...
    def equalWithAbsError (self, *args, **kwargs):
      '''
equalWithAbsError( (V3i)arg1, (V3i)arg2, (int)arg3) -> bool :
    v1.equalWithAbsError(v2) true if the elements of v1 and v2 are the same with an absolute error of no more than e, i.e., abs(v1[i] - v2[i]) <= e

    C++ signature :
        bool equalWithAbsError(Imath_3_1::Vec3<int> {lvalue},Imath_3_1::Vec3<int>,int)

equalWithAbsError( (V3i)arg1, (object)arg2, (object)arg3) -> bool :

    C++ signature :
        bool equalWithAbsError(Imath_3_1::Vec3<int>,boost::python::api::object,boost::python::api::object)'''
    ...
    def equalWithRelError (self, *args, **kwargs):
      '''
equalWithRelError( (V3i)arg1, (V3i)arg2, (int)arg3) -> bool :
    v1.equalWithAbsError(v2) true if the elements of v1 and v2 are the same with an absolute error of no more than e, i.e., abs(v1[i] - v2[i]) <= e * abs(v1[i])

    C++ signature :
        bool equalWithRelError(Imath_3_1::Vec3<int> {lvalue},Imath_3_1::Vec3<int>,int)

equalWithRelError( (V3i)arg1, (object)arg2, (object)arg3) -> bool :

    C++ signature :
        bool equalWithRelError(Imath_3_1::Vec3<int>,boost::python::api::object,boost::python::api::object)'''
    ...
    def length2 (self, *args, **kwargs):
      '''
length2( (V3i)arg1) -> int :
    length2() square magnitude of the vector

    C++ signature :
        int length2(Imath_3_1::Vec3<int>)'''
    ...
    def negate (self, *args, **kwargs):
      '''
negate( (V3i)arg1) -> V3i :

    C++ signature :
        Imath_3_1::Vec3<int> negate(Imath_3_1::Vec3<int> {lvalue})'''
    ...
    def setValue (self, *args, **kwargs):
      '''
setValue( (V3i)arg1, (int)arg2, (int)arg3, (int)arg4) -> None :

    C++ signature :
        void setValue(Imath_3_1::Vec3<int> {lvalue},int,int,int)'''
    ...
    def x (self, *args, **kwargs):
      '''None'''
    ...
    def y (self, *args, **kwargs):
      '''None'''
    ...
    def z (self, *args, **kwargs):
      '''None'''
    ...

def V3i64 (*args):
      '''
__init__(boost::python::api::object, boost::python::api::object, boost::python::api::object, boost::python::api::object)
__init__(boost::python::api::object, boost::python::api::object)
__init__(boost::python::api::object)
__init__(_object*, Imath_3_1::Vec3<long>)

'''      
    ...

class V3i64:
    def baseTypeEpsilon (self, *args, **kwargs):
      '''
baseTypeEpsilon() -> int :
    baseTypeEpsilon() epsilon value of the base type of the vector

    C++ signature :
        long baseTypeEpsilon()'''
    ...
    def baseTypeLowest (self, *args, **kwargs):
      '''
baseTypeLowest() -> int :
    baseTypeLowest() largest negative value of the base type of the vector

    C++ signature :
        long baseTypeLowest()'''
    ...
    def baseTypeMax (self, *args, **kwargs):
      '''
baseTypeMax() -> int :
    baseTypeMax() max value of the base type of the vector

    C++ signature :
        long baseTypeMax()'''
    ...
    def baseTypeSmallest (self, *args, **kwargs):
      '''
baseTypeSmallest() -> int :
    baseTypeSmallest() smallest value of the base type of the vector

    C++ signature :
        long baseTypeSmallest()'''
    ...
    def closestVertex (self, *args, **kwargs):
      '''
closestVertex( (V3i64)arg1, (V3i64)arg2, (V3i64)arg3, (V3i64)arg4) -> V3i64 :

    C++ signature :
        Imath_3_1::Vec3<long> closestVertex(Imath_3_1::Vec3<long> {lvalue},Imath_3_1::Vec3<long>,Imath_3_1::Vec3<long>,Imath_3_1::Vec3<long>)'''
    ...
    def cross (self, *args, **kwargs):
      '''
cross( (V3i64)arg1, (V3i64)arg2) -> V3i64 :
    v1.cross(v2) right handed cross product

    C++ signature :
        Imath_3_1::Vec3<long> cross(Imath_3_1::Vec3<long>,Imath_3_1::Vec3<long>)

cross( (V3i64)arg1, (V3i64Array)arg2) -> V3i64Array :
    v1.cross(v2) right handed array cross product

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec3<long> > cross(Imath_3_1::Vec3<long>,PyImath::FixedArray<Imath_3_1::Vec3<long> >)'''
    ...
    def dimensions (self, *args, **kwargs):
      '''
dimensions() -> int :
    dimensions() number of dimensions in the vector

    C++ signature :
        unsigned int dimensions()'''
    ...
    def dot (self, *args, **kwargs):
      '''
dot( (V3i64)arg1, (V3i64)arg2) -> int :
    v1.dot(v2) inner product of the two vectors

    C++ signature :
        long dot(Imath_3_1::Vec3<long>,Imath_3_1::Vec3<long>)

dot( (V3i64)arg1, (V3i64Array)arg2) -> object :
    v1.dot(v2) array inner product

    C++ signature :
        PyImath::FixedArray<long> dot(Imath_3_1::Vec3<long>,PyImath::FixedArray<Imath_3_1::Vec3<long> >)'''
    ...
    def equalWithAbsError (self, *args, **kwargs):
      '''
equalWithAbsError( (V3i64)arg1, (V3i64)arg2, (int)arg3) -> bool :
    v1.equalWithAbsError(v2) true if the elements of v1 and v2 are the same with an absolute error of no more than e, i.e., abs(v1[i] - v2[i]) <= e

    C++ signature :
        bool equalWithAbsError(Imath_3_1::Vec3<long> {lvalue},Imath_3_1::Vec3<long>,long)

equalWithAbsError( (V3i64)arg1, (object)arg2, (object)arg3) -> bool :

    C++ signature :
        bool equalWithAbsError(Imath_3_1::Vec3<long>,boost::python::api::object,boost::python::api::object)'''
    ...
    def equalWithRelError (self, *args, **kwargs):
      '''
equalWithRelError( (V3i64)arg1, (V3i64)arg2, (int)arg3) -> bool :
    v1.equalWithAbsError(v2) true if the elements of v1 and v2 are the same with an absolute error of no more than e, i.e., abs(v1[i] - v2[i]) <= e * abs(v1[i])

    C++ signature :
        bool equalWithRelError(Imath_3_1::Vec3<long> {lvalue},Imath_3_1::Vec3<long>,long)

equalWithRelError( (V3i64)arg1, (object)arg2, (object)arg3) -> bool :

    C++ signature :
        bool equalWithRelError(Imath_3_1::Vec3<long>,boost::python::api::object,boost::python::api::object)'''
    ...
    def length2 (self, *args, **kwargs):
      '''
length2( (V3i64)arg1) -> int :
    length2() square magnitude of the vector

    C++ signature :
        long length2(Imath_3_1::Vec3<long>)'''
    ...
    def negate (self, *args, **kwargs):
      '''
negate( (V3i64)arg1) -> V3i64 :

    C++ signature :
        Imath_3_1::Vec3<long> negate(Imath_3_1::Vec3<long> {lvalue})'''
    ...
    def setValue (self, *args, **kwargs):
      '''
setValue( (V3i64)arg1, (int)arg2, (int)arg3, (int)arg4) -> None :

    C++ signature :
        void setValue(Imath_3_1::Vec3<long> {lvalue},long,long,long)'''
    ...
    def x (self, *args, **kwargs):
      '''None'''
    ...
    def y (self, *args, **kwargs):
      '''None'''
    ...
    def z (self, *args, **kwargs):
      '''None'''
    ...

def V3i64Array (*args):
      '''
__init__(_object*, PyImath::FixedArray<Imath_3_1::Vec3<double> >)
__init__(_object*, PyImath::FixedArray<Imath_3_1::Vec3<float> >)
__init__(_object*, PyImath::FixedArray<Imath_3_1::Vec3<int> >)
__init__(_object*, PyImath::FixedArray<Imath_3_1::Vec3<short> >)
__init__(_object*, Imath_3_1::Vec3<long>, unsigned long)
__init__(_object*, PyImath::FixedArray<Imath_3_1::Vec3<long> >)
__init__(_object*, unsigned long)

'''      
    ...

class V3i64Array:
    def bounds (self, *args, **kwargs):
      '''
bounds( (V3i64Array)arg1) -> Box3i64 :

    C++ signature :
        Imath_3_1::Box<Imath_3_1::Vec3<long> > bounds(PyImath::FixedArray<Imath_3_1::Vec3<long> >)'''
    ...
    def cross (self, *args, **kwargs):
      '''
cross( (V3i64Array)arg1, (V3i64)x) -> V3i64Array :
    cross(x) - return the cross product of (self,x)

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec3<long> > cross(PyImath::FixedArray<Imath_3_1::Vec3<long> >,Imath_3_1::Vec3<long>)

cross( (V3i64Array)arg1, (V3i64Array)x) -> V3i64Array :
    cross(x) - return the cross product of (self,x)

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec3<long> > cross(PyImath::FixedArray<Imath_3_1::Vec3<long> >,PyImath::FixedArray<Imath_3_1::Vec3<long> >)'''
    ...
    def dot (self, *args, **kwargs):
      '''
dot( (V3i64Array)arg1, (V3i64)x) -> object :
    dot(x) - return the inner product of (self,x)

    C++ signature :
        PyImath::FixedArray<long> dot(PyImath::FixedArray<Imath_3_1::Vec3<long> >,Imath_3_1::Vec3<long>)

dot( (V3i64Array)arg1, (V3i64Array)x) -> object :
    dot(x) - return the inner product of (self,x)

    C++ signature :
        PyImath::FixedArray<long> dot(PyImath::FixedArray<Imath_3_1::Vec3<long> >,PyImath::FixedArray<Imath_3_1::Vec3<long> >)'''
    ...
    def ifelse (self, *args, **kwargs):
      '''
ifelse( (V3i64Array)arg1, (IntArray)arg2, (V3i64)arg3) -> V3i64Array :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec3<long> > ifelse(PyImath::FixedArray<Imath_3_1::Vec3<long> > {lvalue},PyImath::FixedArray<int>,Imath_3_1::Vec3<long>)

ifelse( (V3i64Array)arg1, (IntArray)arg2, (V3i64Array)arg3) -> V3i64Array :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec3<long> > ifelse(PyImath::FixedArray<Imath_3_1::Vec3<long> > {lvalue},PyImath::FixedArray<int>,PyImath::FixedArray<Imath_3_1::Vec3<long> >)'''
    ...
    def length2 (self, *args, **kwargs):
      '''
length2( (V3i64Array)arg1) -> object :

    C++ signature :
        PyImath::FixedArray<long> length2(PyImath::FixedArray<Imath_3_1::Vec3<long> >)'''
    ...
    def makeReadOnly (self, *args, **kwargs):
      '''
makeReadOnly( (V3i64Array)arg1) -> None :

    C++ signature :
        void makeReadOnly(PyImath::FixedArray<Imath_3_1::Vec3<long> > {lvalue})'''
    ...
    def max (self, *args, **kwargs):
      '''
max( (V3i64Array)arg1) -> V3i64 :

    C++ signature :
        Imath_3_1::Vec3<long> max(PyImath::FixedArray<Imath_3_1::Vec3<long> >)'''
    ...
    def min (self, *args, **kwargs):
      '''
min( (V3i64Array)arg1) -> V3i64 :

    C++ signature :
        Imath_3_1::Vec3<long> min(PyImath::FixedArray<Imath_3_1::Vec3<long> >)'''
    ...
    def reduce (self, *args, **kwargs):
      '''
reduce( (V3i64Array)arg1) -> V3i64 :

    C++ signature :
        Imath_3_1::Vec3<long> reduce(PyImath::FixedArray<Imath_3_1::Vec3<long> >)'''
    ...
    def writable (self, *args, **kwargs):
      '''
writable( (V3i64Array)arg1) -> bool :

    C++ signature :
        bool writable(PyImath::FixedArray<Imath_3_1::Vec3<long> > {lvalue})'''
    ...
    def x (self, *args, **kwargs):
      '''None'''
    ...
    def y (self, *args, **kwargs):
      '''None'''
    ...
    def z (self, *args, **kwargs):
      '''None'''
    ...

def V3iArray (*args):
      '''
__init__(_object*, PyImath::FixedArray<Imath_3_1::Vec3<double> >)
__init__(_object*, PyImath::FixedArray<Imath_3_1::Vec3<float> >)
__init__(_object*, PyImath::FixedArray<Imath_3_1::Vec3<long> >)
__init__(_object*, PyImath::FixedArray<Imath_3_1::Vec3<short> >)
__init__(_object*, Imath_3_1::Vec3<int>, unsigned long)
__init__(_object*, PyImath::FixedArray<Imath_3_1::Vec3<int> >)
__init__(_object*, unsigned long)

'''      
    ...

class V3iArray:
    def bounds (self, *args, **kwargs):
      '''
bounds( (V3iArray)arg1) -> Box3i :

    C++ signature :
        Imath_3_1::Box<Imath_3_1::Vec3<int> > bounds(PyImath::FixedArray<Imath_3_1::Vec3<int> >)'''
    ...
    def cross (self, *args, **kwargs):
      '''
cross( (V3iArray)arg1, (V3i)x) -> V3iArray :
    cross(x) - return the cross product of (self,x)

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec3<int> > cross(PyImath::FixedArray<Imath_3_1::Vec3<int> >,Imath_3_1::Vec3<int>)

cross( (V3iArray)arg1, (V3iArray)x) -> V3iArray :
    cross(x) - return the cross product of (self,x)

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec3<int> > cross(PyImath::FixedArray<Imath_3_1::Vec3<int> >,PyImath::FixedArray<Imath_3_1::Vec3<int> >)'''
    ...
    def dot (self, *args, **kwargs):
      '''
dot( (V3iArray)arg1, (V3i)x) -> IntArray :
    dot(x) - return the inner product of (self,x)

    C++ signature :
        PyImath::FixedArray<int> dot(PyImath::FixedArray<Imath_3_1::Vec3<int> >,Imath_3_1::Vec3<int>)

dot( (V3iArray)arg1, (V3iArray)x) -> IntArray :
    dot(x) - return the inner product of (self,x)

    C++ signature :
        PyImath::FixedArray<int> dot(PyImath::FixedArray<Imath_3_1::Vec3<int> >,PyImath::FixedArray<Imath_3_1::Vec3<int> >)'''
    ...
    def ifelse (self, *args, **kwargs):
      '''
ifelse( (V3iArray)arg1, (IntArray)arg2, (V3i)arg3) -> V3iArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec3<int> > ifelse(PyImath::FixedArray<Imath_3_1::Vec3<int> > {lvalue},PyImath::FixedArray<int>,Imath_3_1::Vec3<int>)

ifelse( (V3iArray)arg1, (IntArray)arg2, (V3iArray)arg3) -> V3iArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec3<int> > ifelse(PyImath::FixedArray<Imath_3_1::Vec3<int> > {lvalue},PyImath::FixedArray<int>,PyImath::FixedArray<Imath_3_1::Vec3<int> >)'''
    ...
    def length2 (self, *args, **kwargs):
      '''
length2( (V3iArray)arg1) -> IntArray :

    C++ signature :
        PyImath::FixedArray<int> length2(PyImath::FixedArray<Imath_3_1::Vec3<int> >)'''
    ...
    def makeReadOnly (self, *args, **kwargs):
      '''
makeReadOnly( (V3iArray)arg1) -> None :

    C++ signature :
        void makeReadOnly(PyImath::FixedArray<Imath_3_1::Vec3<int> > {lvalue})'''
    ...
    def max (self, *args, **kwargs):
      '''
max( (V3iArray)arg1) -> V3i :

    C++ signature :
        Imath_3_1::Vec3<int> max(PyImath::FixedArray<Imath_3_1::Vec3<int> >)'''
    ...
    def min (self, *args, **kwargs):
      '''
min( (V3iArray)arg1) -> V3i :

    C++ signature :
        Imath_3_1::Vec3<int> min(PyImath::FixedArray<Imath_3_1::Vec3<int> >)'''
    ...
    def reduce (self, *args, **kwargs):
      '''
reduce( (V3iArray)arg1) -> V3i :

    C++ signature :
        Imath_3_1::Vec3<int> reduce(PyImath::FixedArray<Imath_3_1::Vec3<int> >)'''
    ...
    def writable (self, *args, **kwargs):
      '''
writable( (V3iArray)arg1) -> bool :

    C++ signature :
        bool writable(PyImath::FixedArray<Imath_3_1::Vec3<int> > {lvalue})'''
    ...
    def x (self, *args, **kwargs):
      '''None'''
    ...
    def y (self, *args, **kwargs):
      '''None'''
    ...
    def z (self, *args, **kwargs):
      '''None'''
    ...

def V3iArrayFromBuffer (*args):
      '''

'''      
    ...

def V3s (*args):
      '''
__init__(boost::python::api::object, boost::python::api::object, boost::python::api::object, boost::python::api::object)
__init__(boost::python::api::object, boost::python::api::object)
__init__(boost::python::api::object)
__init__(_object*, Imath_3_1::Vec3<short>)

'''      
    ...

class V3s:
    def baseTypeEpsilon (self, *args, **kwargs):
      '''
baseTypeEpsilon() -> int :
    baseTypeEpsilon() epsilon value of the base type of the vector

    C++ signature :
        short baseTypeEpsilon()'''
    ...
    def baseTypeLowest (self, *args, **kwargs):
      '''
baseTypeLowest() -> int :
    baseTypeLowest() largest negative value of the base type of the vector

    C++ signature :
        short baseTypeLowest()'''
    ...
    def baseTypeMax (self, *args, **kwargs):
      '''
baseTypeMax() -> int :
    baseTypeMax() max value of the base type of the vector

    C++ signature :
        short baseTypeMax()'''
    ...
    def baseTypeSmallest (self, *args, **kwargs):
      '''
baseTypeSmallest() -> int :
    baseTypeSmallest() smallest value of the base type of the vector

    C++ signature :
        short baseTypeSmallest()'''
    ...
    def closestVertex (self, *args, **kwargs):
      '''
closestVertex( (V3s)arg1, (V3s)arg2, (V3s)arg3, (V3s)arg4) -> V3s :

    C++ signature :
        Imath_3_1::Vec3<short> closestVertex(Imath_3_1::Vec3<short> {lvalue},Imath_3_1::Vec3<short>,Imath_3_1::Vec3<short>,Imath_3_1::Vec3<short>)'''
    ...
    def cross (self, *args, **kwargs):
      '''
cross( (V3s)arg1, (V3s)arg2) -> V3s :
    v1.cross(v2) right handed cross product

    C++ signature :
        Imath_3_1::Vec3<short> cross(Imath_3_1::Vec3<short>,Imath_3_1::Vec3<short>)

cross( (V3s)arg1, (V3sArray)arg2) -> V3sArray :
    v1.cross(v2) right handed array cross product

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec3<short> > cross(Imath_3_1::Vec3<short>,PyImath::FixedArray<Imath_3_1::Vec3<short> >)'''
    ...
    def dimensions (self, *args, **kwargs):
      '''
dimensions() -> int :
    dimensions() number of dimensions in the vector

    C++ signature :
        unsigned int dimensions()'''
    ...
    def dot (self, *args, **kwargs):
      '''
dot( (V3s)arg1, (V3s)arg2) -> int :
    v1.dot(v2) inner product of the two vectors

    C++ signature :
        short dot(Imath_3_1::Vec3<short>,Imath_3_1::Vec3<short>)

dot( (V3s)arg1, (V3sArray)arg2) -> ShortArray :
    v1.dot(v2) array inner product

    C++ signature :
        PyImath::FixedArray<short> dot(Imath_3_1::Vec3<short>,PyImath::FixedArray<Imath_3_1::Vec3<short> >)'''
    ...
    def equalWithAbsError (self, *args, **kwargs):
      '''
equalWithAbsError( (V3s)arg1, (V3s)arg2, (int)arg3) -> bool :
    v1.equalWithAbsError(v2) true if the elements of v1 and v2 are the same with an absolute error of no more than e, i.e., abs(v1[i] - v2[i]) <= e

    C++ signature :
        bool equalWithAbsError(Imath_3_1::Vec3<short> {lvalue},Imath_3_1::Vec3<short>,short)

equalWithAbsError( (V3s)arg1, (object)arg2, (object)arg3) -> bool :

    C++ signature :
        bool equalWithAbsError(Imath_3_1::Vec3<short>,boost::python::api::object,boost::python::api::object)'''
    ...
    def equalWithRelError (self, *args, **kwargs):
      '''
equalWithRelError( (V3s)arg1, (V3s)arg2, (int)arg3) -> bool :
    v1.equalWithAbsError(v2) true if the elements of v1 and v2 are the same with an absolute error of no more than e, i.e., abs(v1[i] - v2[i]) <= e * abs(v1[i])

    C++ signature :
        bool equalWithRelError(Imath_3_1::Vec3<short> {lvalue},Imath_3_1::Vec3<short>,short)

equalWithRelError( (V3s)arg1, (object)arg2, (object)arg3) -> bool :

    C++ signature :
        bool equalWithRelError(Imath_3_1::Vec3<short>,boost::python::api::object,boost::python::api::object)'''
    ...
    def length2 (self, *args, **kwargs):
      '''
length2( (V3s)arg1) -> int :
    length2() square magnitude of the vector

    C++ signature :
        short length2(Imath_3_1::Vec3<short>)'''
    ...
    def negate (self, *args, **kwargs):
      '''
negate( (V3s)arg1) -> V3s :

    C++ signature :
        Imath_3_1::Vec3<short> negate(Imath_3_1::Vec3<short> {lvalue})'''
    ...
    def setValue (self, *args, **kwargs):
      '''
setValue( (V3s)arg1, (int)arg2, (int)arg3, (int)arg4) -> None :

    C++ signature :
        void setValue(Imath_3_1::Vec3<short> {lvalue},short,short,short)'''
    ...
    def x (self, *args, **kwargs):
      '''None'''
    ...
    def y (self, *args, **kwargs):
      '''None'''
    ...
    def z (self, *args, **kwargs):
      '''None'''
    ...

def V3sArray (*args):
      '''
__init__(_object*, PyImath::FixedArray<Imath_3_1::Vec3<double> >)
__init__(_object*, PyImath::FixedArray<Imath_3_1::Vec3<float> >)
__init__(_object*, PyImath::FixedArray<Imath_3_1::Vec3<long> >)
__init__(_object*, PyImath::FixedArray<Imath_3_1::Vec3<int> >)
__init__(_object*, Imath_3_1::Vec3<short>, unsigned long)
__init__(_object*, PyImath::FixedArray<Imath_3_1::Vec3<short> >)
__init__(_object*, unsigned long)

'''      
    ...

class V3sArray:
    def bounds (self, *args, **kwargs):
      '''
bounds( (V3sArray)arg1) -> Box3s :

    C++ signature :
        Imath_3_1::Box<Imath_3_1::Vec3<short> > bounds(PyImath::FixedArray<Imath_3_1::Vec3<short> >)'''
    ...
    def cross (self, *args, **kwargs):
      '''
cross( (V3sArray)arg1, (V3s)x) -> V3sArray :
    cross(x) - return the cross product of (self,x)

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec3<short> > cross(PyImath::FixedArray<Imath_3_1::Vec3<short> >,Imath_3_1::Vec3<short>)

cross( (V3sArray)arg1, (V3sArray)x) -> V3sArray :
    cross(x) - return the cross product of (self,x)

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec3<short> > cross(PyImath::FixedArray<Imath_3_1::Vec3<short> >,PyImath::FixedArray<Imath_3_1::Vec3<short> >)'''
    ...
    def dot (self, *args, **kwargs):
      '''
dot( (V3sArray)arg1, (V3s)x) -> ShortArray :
    dot(x) - return the inner product of (self,x)

    C++ signature :
        PyImath::FixedArray<short> dot(PyImath::FixedArray<Imath_3_1::Vec3<short> >,Imath_3_1::Vec3<short>)

dot( (V3sArray)arg1, (V3sArray)x) -> ShortArray :
    dot(x) - return the inner product of (self,x)

    C++ signature :
        PyImath::FixedArray<short> dot(PyImath::FixedArray<Imath_3_1::Vec3<short> >,PyImath::FixedArray<Imath_3_1::Vec3<short> >)'''
    ...
    def ifelse (self, *args, **kwargs):
      '''
ifelse( (V3sArray)arg1, (IntArray)arg2, (V3s)arg3) -> V3sArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec3<short> > ifelse(PyImath::FixedArray<Imath_3_1::Vec3<short> > {lvalue},PyImath::FixedArray<int>,Imath_3_1::Vec3<short>)

ifelse( (V3sArray)arg1, (IntArray)arg2, (V3sArray)arg3) -> V3sArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec3<short> > ifelse(PyImath::FixedArray<Imath_3_1::Vec3<short> > {lvalue},PyImath::FixedArray<int>,PyImath::FixedArray<Imath_3_1::Vec3<short> >)'''
    ...
    def length2 (self, *args, **kwargs):
      '''
length2( (V3sArray)arg1) -> ShortArray :

    C++ signature :
        PyImath::FixedArray<short> length2(PyImath::FixedArray<Imath_3_1::Vec3<short> >)'''
    ...
    def makeReadOnly (self, *args, **kwargs):
      '''
makeReadOnly( (V3sArray)arg1) -> None :

    C++ signature :
        void makeReadOnly(PyImath::FixedArray<Imath_3_1::Vec3<short> > {lvalue})'''
    ...
    def max (self, *args, **kwargs):
      '''
max( (V3sArray)arg1) -> V3s :

    C++ signature :
        Imath_3_1::Vec3<short> max(PyImath::FixedArray<Imath_3_1::Vec3<short> >)'''
    ...
    def min (self, *args, **kwargs):
      '''
min( (V3sArray)arg1) -> V3s :

    C++ signature :
        Imath_3_1::Vec3<short> min(PyImath::FixedArray<Imath_3_1::Vec3<short> >)'''
    ...
    def reduce (self, *args, **kwargs):
      '''
reduce( (V3sArray)arg1) -> V3s :

    C++ signature :
        Imath_3_1::Vec3<short> reduce(PyImath::FixedArray<Imath_3_1::Vec3<short> >)'''
    ...
    def writable (self, *args, **kwargs):
      '''
writable( (V3sArray)arg1) -> bool :

    C++ signature :
        bool writable(PyImath::FixedArray<Imath_3_1::Vec3<short> > {lvalue})'''
    ...
    def x (self, *args, **kwargs):
      '''None'''
    ...
    def y (self, *args, **kwargs):
      '''None'''
    ...
    def z (self, *args, **kwargs):
      '''None'''
    ...

def V4c (*args):
      '''
__init__(boost::python::api::object, boost::python::api::object, boost::python::api::object, boost::python::api::object, boost::python::api::object)
__init__(boost::python::api::object, boost::python::api::object)
__init__(boost::python::api::object)
__init__(_object*, Imath_3_1::Vec4<unsigned char>)

'''      
    ...

class V4c:
    def baseTypeEpsilon (self, *args, **kwargs):
      '''
baseTypeEpsilon() -> int :
    baseTypeEpsilon() epsilon value of the base type of the vector

    C++ signature :
        unsigned char baseTypeEpsilon()'''
    ...
    def baseTypeLowest (self, *args, **kwargs):
      '''
baseTypeLowest() -> int :
    baseTypeLowest() largest negative value of the base type of the vector

    C++ signature :
        unsigned char baseTypeLowest()'''
    ...
    def baseTypeMax (self, *args, **kwargs):
      '''
baseTypeMax() -> int :
    baseTypeMax() max value of the base type of the vector

    C++ signature :
        unsigned char baseTypeMax()'''
    ...
    def baseTypeSmallest (self, *args, **kwargs):
      '''
baseTypeSmallest() -> int :
    baseTypeSmallest() smallest value of the base type of the vector

    C++ signature :
        unsigned char baseTypeSmallest()'''
    ...
    def dimensions (self, *args, **kwargs):
      '''
dimensions() -> int :
    dimensions() number of dimensions in the vector

    C++ signature :
        unsigned int dimensions()'''
    ...
    def dot (self, *args, **kwargs):
      '''
dot( (V4c)arg1, (V4c)arg2) -> int :
    v1.dot(v2) inner product of the two vectors

    C++ signature :
        unsigned char dot(Imath_3_1::Vec4<unsigned char>,Imath_3_1::Vec4<unsigned char>)

dot( (V4c)arg1, (object)arg2) -> UnsignedCharArray :
    v1.dot(v2) array inner product

    C++ signature :
        PyImath::FixedArray<unsigned char> dot(Imath_3_1::Vec4<unsigned char>,PyImath::FixedArray<Imath_3_1::Vec4<unsigned char> >)'''
    ...
    def equalWithAbsError (self, *args, **kwargs):
      '''
equalWithAbsError( (V4c)arg1, (V4c)arg2, (int)arg3) -> bool :
    v1.equalWithAbsError(v2) true if the elements of v1 and v2 are the same with an absolute error of no more than e, i.e., abs(v1[i] - v2[i]) <= e

    C++ signature :
        bool equalWithAbsError(Imath_3_1::Vec4<unsigned char> {lvalue},Imath_3_1::Vec4<unsigned char>,unsigned char)

equalWithAbsError( (V4c)arg1, (object)arg2, (object)arg3) -> bool :

    C++ signature :
        bool equalWithAbsError(Imath_3_1::Vec4<unsigned char>,boost::python::api::object,boost::python::api::object)'''
    ...
    def equalWithRelError (self, *args, **kwargs):
      '''
equalWithRelError( (V4c)arg1, (V4c)arg2, (int)arg3) -> bool :
    v1.equalWithAbsError(v2) true if the elements of v1 and v2 are the same with an absolute error of no more than e, i.e., abs(v1[i] - v2[i]) <= e * abs(v1[i])

    C++ signature :
        bool equalWithRelError(Imath_3_1::Vec4<unsigned char> {lvalue},Imath_3_1::Vec4<unsigned char>,unsigned char)

equalWithRelError( (V4c)arg1, (object)arg2, (object)arg3) -> bool :

    C++ signature :
        bool equalWithRelError(Imath_3_1::Vec4<unsigned char>,boost::python::api::object,boost::python::api::object)'''
    ...
    def length2 (self, *args, **kwargs):
      '''
length2( (V4c)arg1) -> int :
    length2() square magnitude of the vector

    C++ signature :
        unsigned char length2(Imath_3_1::Vec4<unsigned char>)'''
    ...
    def negate (self, *args, **kwargs):
      '''
negate( (V4c)arg1) -> V4c :

    C++ signature :
        Imath_3_1::Vec4<unsigned char> negate(Imath_3_1::Vec4<unsigned char> {lvalue})'''
    ...
    def setValue (self, *args, **kwargs):
      '''
setValue( (V4c)arg1, (int)arg2, (int)arg3, (int)arg4, (int)arg5) -> None :

    C++ signature :
        void setValue(Imath_3_1::Vec4<unsigned char> {lvalue},unsigned char,unsigned char,unsigned char,unsigned char)'''
    ...
    def w (self, *args, **kwargs):
      '''None'''
    ...
    def x (self, *args, **kwargs):
      '''None'''
    ...
    def y (self, *args, **kwargs):
      '''None'''
    ...
    def z (self, *args, **kwargs):
      '''None'''
    ...

def V4d (*args):
      '''
__init__(boost::python::api::object, boost::python::api::object, boost::python::api::object, boost::python::api::object, boost::python::api::object)
__init__(boost::python::api::object, boost::python::api::object)
__init__(boost::python::api::object)
__init__(_object*, Imath_3_1::Vec4<double>)

'''      
    ...

class V4d:
    def baseTypeEpsilon (self, *args, **kwargs):
      '''
baseTypeEpsilon() -> float :
    baseTypeEpsilon() epsilon value of the base type of the vector

    C++ signature :
        double baseTypeEpsilon()'''
    ...
    def baseTypeLowest (self, *args, **kwargs):
      '''
baseTypeLowest() -> float :
    baseTypeLowest() largest negative value of the base type of the vector

    C++ signature :
        double baseTypeLowest()'''
    ...
    def baseTypeMax (self, *args, **kwargs):
      '''
baseTypeMax() -> float :
    baseTypeMax() max value of the base type of the vector

    C++ signature :
        double baseTypeMax()'''
    ...
    def baseTypeSmallest (self, *args, **kwargs):
      '''
baseTypeSmallest() -> float :
    baseTypeSmallest() smallest value of the base type of the vector

    C++ signature :
        double baseTypeSmallest()'''
    ...
    def dimensions (self, *args, **kwargs):
      '''
dimensions() -> int :
    dimensions() number of dimensions in the vector

    C++ signature :
        unsigned int dimensions()'''
    ...
    def dot (self, *args, **kwargs):
      '''
dot( (V4d)arg1, (V4d)arg2) -> float :
    v1.dot(v2) inner product of the two vectors

    C++ signature :
        double dot(Imath_3_1::Vec4<double>,Imath_3_1::Vec4<double>)

dot( (V4d)arg1, (V4dArray)arg2) -> DoubleArray :
    v1.dot(v2) array inner product

    C++ signature :
        PyImath::FixedArray<double> dot(Imath_3_1::Vec4<double>,PyImath::FixedArray<Imath_3_1::Vec4<double> >)'''
    ...
    def equalWithAbsError (self, *args, **kwargs):
      '''
equalWithAbsError( (V4d)arg1, (V4d)arg2, (float)arg3) -> bool :
    v1.equalWithAbsError(v2) true if the elements of v1 and v2 are the same with an absolute error of no more than e, i.e., abs(v1[i] - v2[i]) <= e

    C++ signature :
        bool equalWithAbsError(Imath_3_1::Vec4<double> {lvalue},Imath_3_1::Vec4<double>,double)

equalWithAbsError( (V4d)arg1, (object)arg2, (object)arg3) -> bool :

    C++ signature :
        bool equalWithAbsError(Imath_3_1::Vec4<double>,boost::python::api::object,boost::python::api::object)'''
    ...
    def equalWithRelError (self, *args, **kwargs):
      '''
equalWithRelError( (V4d)arg1, (V4d)arg2, (float)arg3) -> bool :
    v1.equalWithAbsError(v2) true if the elements of v1 and v2 are the same with an absolute error of no more than e, i.e., abs(v1[i] - v2[i]) <= e * abs(v1[i])

    C++ signature :
        bool equalWithRelError(Imath_3_1::Vec4<double> {lvalue},Imath_3_1::Vec4<double>,double)

equalWithRelError( (V4d)arg1, (object)arg2, (object)arg3) -> bool :

    C++ signature :
        bool equalWithRelError(Imath_3_1::Vec4<double>,boost::python::api::object,boost::python::api::object)'''
    ...
    def length (self, *args, **kwargs):
      '''
length( (V4d)arg1) -> float :
    length() magnitude of the vector

    C++ signature :
        double length(Imath_3_1::Vec4<double>)'''
    ...
    def length2 (self, *args, **kwargs):
      '''
length2( (V4d)arg1) -> float :
    length2() square magnitude of the vector

    C++ signature :
        double length2(Imath_3_1::Vec4<double>)'''
    ...
    def negate (self, *args, **kwargs):
      '''
negate( (V4d)arg1) -> V4d :

    C++ signature :
        Imath_3_1::Vec4<double> negate(Imath_3_1::Vec4<double> {lvalue})'''
    ...
    def normalize (self, *args, **kwargs):
      '''
normalize( (V4d)arg1) -> V4d :
    v.normalize() destructively normalizes v and returns a reference to it

    C++ signature :
        Imath_3_1::Vec4<double> normalize(Imath_3_1::Vec4<double> {lvalue})'''
    ...
    def normalizeExc (self, *args, **kwargs):
      '''
normalizeExc( (V4d)arg1) -> V4d :
    v.normalizeExc() destructively normalizes V and returns a reference to it, throwing an exception if length() == 0

    C++ signature :
        Imath_3_1::Vec4<double> normalizeExc(Imath_3_1::Vec4<double> {lvalue})'''
    ...
    def normalizeNonNull (self, *args, **kwargs):
      '''
normalizeNonNull( (V4d)arg1) -> V4d :
    v.normalizeNonNull() destructively normalizes V and returns a reference to it, faster if lngth() != 0

    C++ signature :
        Imath_3_1::Vec4<double> normalizeNonNull(Imath_3_1::Vec4<double> {lvalue})'''
    ...
    def normalized (self, *args, **kwargs):
      '''
normalized( (V4d)arg1) -> V4d :
    v.normalized() returns a normalized copy of v

    C++ signature :
        Imath_3_1::Vec4<double> normalized(Imath_3_1::Vec4<double>)'''
    ...
    def normalizedExc (self, *args, **kwargs):
      '''
normalizedExc( (V4d)arg1) -> V4d :
    v.normalizedExc() returns a normalized copy of v, throwing an exception if length() == 0

    C++ signature :
        Imath_3_1::Vec4<double> normalizedExc(Imath_3_1::Vec4<double>)'''
    ...
    def normalizedNonNull (self, *args, **kwargs):
      '''
normalizedNonNull( (V4d)arg1) -> V4d :
    v.normalizedNonNull() returns a normalized copy of v, faster if lngth() != 0

    C++ signature :
        Imath_3_1::Vec4<double> normalizedNonNull(Imath_3_1::Vec4<double>)'''
    ...
    def orthogonal (self, *args, **kwargs):
      '''
orthogonal( (V4d)arg1, (V4d)arg2) -> V4d :

    C++ signature :
        Imath_3_1::Vec4<double> orthogonal(Imath_3_1::Vec4<double>,Imath_3_1::Vec4<double>)'''
    ...
    def project (self, *args, **kwargs):
      '''
project( (V4d)arg1, (V4d)arg2) -> V4d :

    C++ signature :
        Imath_3_1::Vec4<double> project(Imath_3_1::Vec4<double>,Imath_3_1::Vec4<double>)'''
    ...
    def reflect (self, *args, **kwargs):
      '''
reflect( (V4d)arg1, (V4d)arg2) -> V4d :

    C++ signature :
        Imath_3_1::Vec4<double> reflect(Imath_3_1::Vec4<double>,Imath_3_1::Vec4<double>)'''
    ...
    def setValue (self, *args, **kwargs):
      '''
setValue( (V4d)arg1, (float)arg2, (float)arg3, (float)arg4, (float)arg5) -> None :

    C++ signature :
        void setValue(Imath_3_1::Vec4<double> {lvalue},double,double,double,double)'''
    ...
    def w (self, *args, **kwargs):
      '''None'''
    ...
    def x (self, *args, **kwargs):
      '''None'''
    ...
    def y (self, *args, **kwargs):
      '''None'''
    ...
    def z (self, *args, **kwargs):
      '''None'''
    ...

def V4dArray (*args):
      '''
__init__(_object*, PyImath::FixedArray<Imath_3_1::Vec4<float> >)
__init__(_object*, PyImath::FixedArray<Imath_3_1::Vec4<long> >)
__init__(_object*, PyImath::FixedArray<Imath_3_1::Vec4<int> >)
__init__(_object*, PyImath::FixedArray<Imath_3_1::Vec4<short> >)
__init__(_object*, Imath_3_1::Vec4<double>, unsigned long)
__init__(_object*, PyImath::FixedArray<Imath_3_1::Vec4<double> >)
__init__(_object*, unsigned long)

'''      
    ...

class V4dArray:
    def dot (self, *args, **kwargs):
      '''
dot( (V4dArray)arg1, (V4d)x) -> DoubleArray :
    dot(x) - return the inner product of (self,x)

    C++ signature :
        PyImath::FixedArray<double> dot(PyImath::FixedArray<Imath_3_1::Vec4<double> >,Imath_3_1::Vec4<double>)

dot( (V4dArray)arg1, (V4dArray)x) -> DoubleArray :
    dot(x) - return the inner product of (self,x)

    C++ signature :
        PyImath::FixedArray<double> dot(PyImath::FixedArray<Imath_3_1::Vec4<double> >,PyImath::FixedArray<Imath_3_1::Vec4<double> >)'''
    ...
    def ifelse (self, *args, **kwargs):
      '''
ifelse( (V4dArray)arg1, (IntArray)arg2, (V4d)arg3) -> V4dArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec4<double> > ifelse(PyImath::FixedArray<Imath_3_1::Vec4<double> > {lvalue},PyImath::FixedArray<int>,Imath_3_1::Vec4<double>)

ifelse( (V4dArray)arg1, (IntArray)arg2, (V4dArray)arg3) -> V4dArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec4<double> > ifelse(PyImath::FixedArray<Imath_3_1::Vec4<double> > {lvalue},PyImath::FixedArray<int>,PyImath::FixedArray<Imath_3_1::Vec4<double> >)'''
    ...
    def length (self, *args, **kwargs):
      '''
length( (V4dArray)arg1) -> DoubleArray :

    C++ signature :
        PyImath::FixedArray<double> length(PyImath::FixedArray<Imath_3_1::Vec4<double> >)'''
    ...
    def length2 (self, *args, **kwargs):
      '''
length2( (V4dArray)arg1) -> DoubleArray :

    C++ signature :
        PyImath::FixedArray<double> length2(PyImath::FixedArray<Imath_3_1::Vec4<double> >)'''
    ...
    def makeReadOnly (self, *args, **kwargs):
      '''
makeReadOnly( (V4dArray)arg1) -> None :

    C++ signature :
        void makeReadOnly(PyImath::FixedArray<Imath_3_1::Vec4<double> > {lvalue})'''
    ...
    def max (self, *args, **kwargs):
      '''
max( (V4dArray)arg1) -> V4d :

    C++ signature :
        Imath_3_1::Vec4<double> max(PyImath::FixedArray<Imath_3_1::Vec4<double> >)'''
    ...
    def min (self, *args, **kwargs):
      '''
min( (V4dArray)arg1) -> V4d :

    C++ signature :
        Imath_3_1::Vec4<double> min(PyImath::FixedArray<Imath_3_1::Vec4<double> >)'''
    ...
    def normalize (self, *args, **kwargs):
      '''
normalize( (V4dArray)arg1) -> V4dArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec4<double> > {lvalue} normalize(PyImath::FixedArray<Imath_3_1::Vec4<double> > {lvalue})'''
    ...
    def normalizeExc (self, *args, **kwargs):
      '''
normalizeExc( (V4dArray)arg1) -> V4dArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec4<double> > {lvalue} normalizeExc(PyImath::FixedArray<Imath_3_1::Vec4<double> > {lvalue})'''
    ...
    def normalized (self, *args, **kwargs):
      '''
normalized( (V4dArray)arg1) -> V4dArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec4<double> > normalized(PyImath::FixedArray<Imath_3_1::Vec4<double> >)'''
    ...
    def normalizedExc (self, *args, **kwargs):
      '''
normalizedExc( (V4dArray)arg1) -> V4dArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec4<double> > normalizedExc(PyImath::FixedArray<Imath_3_1::Vec4<double> >)'''
    ...
    def reduce (self, *args, **kwargs):
      '''
reduce( (V4dArray)arg1) -> V4d :

    C++ signature :
        Imath_3_1::Vec4<double> reduce(PyImath::FixedArray<Imath_3_1::Vec4<double> >)'''
    ...
    def w (self, *args, **kwargs):
      '''None'''
    ...
    def writable (self, *args, **kwargs):
      '''
writable( (V4dArray)arg1) -> bool :

    C++ signature :
        bool writable(PyImath::FixedArray<Imath_3_1::Vec4<double> > {lvalue})'''
    ...
    def x (self, *args, **kwargs):
      '''None'''
    ...
    def y (self, *args, **kwargs):
      '''None'''
    ...
    def z (self, *args, **kwargs):
      '''None'''
    ...

def V4dArrayFromBuffer (*args):
      '''

'''      
    ...

def V4f (*args):
      '''
__init__(boost::python::api::object, boost::python::api::object, boost::python::api::object, boost::python::api::object, boost::python::api::object)
__init__(boost::python::api::object, boost::python::api::object)
__init__(boost::python::api::object)
__init__(_object*, Imath_3_1::Vec4<float>)

'''      
    ...

class V4f:
    def baseTypeEpsilon (self, *args, **kwargs):
      '''
baseTypeEpsilon() -> float :
    baseTypeEpsilon() epsilon value of the base type of the vector

    C++ signature :
        float baseTypeEpsilon()'''
    ...
    def baseTypeLowest (self, *args, **kwargs):
      '''
baseTypeLowest() -> float :
    baseTypeLowest() largest negative value of the base type of the vector

    C++ signature :
        float baseTypeLowest()'''
    ...
    def baseTypeMax (self, *args, **kwargs):
      '''
baseTypeMax() -> float :
    baseTypeMax() max value of the base type of the vector

    C++ signature :
        float baseTypeMax()'''
    ...
    def baseTypeSmallest (self, *args, **kwargs):
      '''
baseTypeSmallest() -> float :
    baseTypeSmallest() smallest value of the base type of the vector

    C++ signature :
        float baseTypeSmallest()'''
    ...
    def dimensions (self, *args, **kwargs):
      '''
dimensions() -> int :
    dimensions() number of dimensions in the vector

    C++ signature :
        unsigned int dimensions()'''
    ...
    def dot (self, *args, **kwargs):
      '''
dot( (V4f)arg1, (V4f)arg2) -> float :
    v1.dot(v2) inner product of the two vectors

    C++ signature :
        float dot(Imath_3_1::Vec4<float>,Imath_3_1::Vec4<float>)

dot( (V4f)arg1, (V4fArray)arg2) -> FloatArray :
    v1.dot(v2) array inner product

    C++ signature :
        PyImath::FixedArray<float> dot(Imath_3_1::Vec4<float>,PyImath::FixedArray<Imath_3_1::Vec4<float> >)'''
    ...
    def equalWithAbsError (self, *args, **kwargs):
      '''
equalWithAbsError( (V4f)arg1, (V4f)arg2, (float)arg3) -> bool :
    v1.equalWithAbsError(v2) true if the elements of v1 and v2 are the same with an absolute error of no more than e, i.e., abs(v1[i] - v2[i]) <= e

    C++ signature :
        bool equalWithAbsError(Imath_3_1::Vec4<float> {lvalue},Imath_3_1::Vec4<float>,float)

equalWithAbsError( (V4f)arg1, (object)arg2, (object)arg3) -> bool :

    C++ signature :
        bool equalWithAbsError(Imath_3_1::Vec4<float>,boost::python::api::object,boost::python::api::object)'''
    ...
    def equalWithRelError (self, *args, **kwargs):
      '''
equalWithRelError( (V4f)arg1, (V4f)arg2, (float)arg3) -> bool :
    v1.equalWithAbsError(v2) true if the elements of v1 and v2 are the same with an absolute error of no more than e, i.e., abs(v1[i] - v2[i]) <= e * abs(v1[i])

    C++ signature :
        bool equalWithRelError(Imath_3_1::Vec4<float> {lvalue},Imath_3_1::Vec4<float>,float)

equalWithRelError( (V4f)arg1, (object)arg2, (object)arg3) -> bool :

    C++ signature :
        bool equalWithRelError(Imath_3_1::Vec4<float>,boost::python::api::object,boost::python::api::object)'''
    ...
    def length (self, *args, **kwargs):
      '''
length( (V4f)arg1) -> float :
    length() magnitude of the vector

    C++ signature :
        float length(Imath_3_1::Vec4<float>)'''
    ...
    def length2 (self, *args, **kwargs):
      '''
length2( (V4f)arg1) -> float :
    length2() square magnitude of the vector

    C++ signature :
        float length2(Imath_3_1::Vec4<float>)'''
    ...
    def negate (self, *args, **kwargs):
      '''
negate( (V4f)arg1) -> V4f :

    C++ signature :
        Imath_3_1::Vec4<float> negate(Imath_3_1::Vec4<float> {lvalue})'''
    ...
    def normalize (self, *args, **kwargs):
      '''
normalize( (V4f)arg1) -> V4f :
    v.normalize() destructively normalizes v and returns a reference to it

    C++ signature :
        Imath_3_1::Vec4<float> normalize(Imath_3_1::Vec4<float> {lvalue})'''
    ...
    def normalizeExc (self, *args, **kwargs):
      '''
normalizeExc( (V4f)arg1) -> V4f :
    v.normalizeExc() destructively normalizes V and returns a reference to it, throwing an exception if length() == 0

    C++ signature :
        Imath_3_1::Vec4<float> normalizeExc(Imath_3_1::Vec4<float> {lvalue})'''
    ...
    def normalizeNonNull (self, *args, **kwargs):
      '''
normalizeNonNull( (V4f)arg1) -> V4f :
    v.normalizeNonNull() destructively normalizes V and returns a reference to it, faster if lngth() != 0

    C++ signature :
        Imath_3_1::Vec4<float> normalizeNonNull(Imath_3_1::Vec4<float> {lvalue})'''
    ...
    def normalized (self, *args, **kwargs):
      '''
normalized( (V4f)arg1) -> V4f :
    v.normalized() returns a normalized copy of v

    C++ signature :
        Imath_3_1::Vec4<float> normalized(Imath_3_1::Vec4<float>)'''
    ...
    def normalizedExc (self, *args, **kwargs):
      '''
normalizedExc( (V4f)arg1) -> V4f :
    v.normalizedExc() returns a normalized copy of v, throwing an exception if length() == 0

    C++ signature :
        Imath_3_1::Vec4<float> normalizedExc(Imath_3_1::Vec4<float>)'''
    ...
    def normalizedNonNull (self, *args, **kwargs):
      '''
normalizedNonNull( (V4f)arg1) -> V4f :
    v.normalizedNonNull() returns a normalized copy of v, faster if lngth() != 0

    C++ signature :
        Imath_3_1::Vec4<float> normalizedNonNull(Imath_3_1::Vec4<float>)'''
    ...
    def orthogonal (self, *args, **kwargs):
      '''
orthogonal( (V4f)arg1, (V4f)arg2) -> V4f :

    C++ signature :
        Imath_3_1::Vec4<float> orthogonal(Imath_3_1::Vec4<float>,Imath_3_1::Vec4<float>)'''
    ...
    def project (self, *args, **kwargs):
      '''
project( (V4f)arg1, (V4f)arg2) -> V4f :

    C++ signature :
        Imath_3_1::Vec4<float> project(Imath_3_1::Vec4<float>,Imath_3_1::Vec4<float>)'''
    ...
    def reflect (self, *args, **kwargs):
      '''
reflect( (V4f)arg1, (V4f)arg2) -> V4f :

    C++ signature :
        Imath_3_1::Vec4<float> reflect(Imath_3_1::Vec4<float>,Imath_3_1::Vec4<float>)'''
    ...
    def setValue (self, *args, **kwargs):
      '''
setValue( (V4f)arg1, (float)arg2, (float)arg3, (float)arg4, (float)arg5) -> None :

    C++ signature :
        void setValue(Imath_3_1::Vec4<float> {lvalue},float,float,float,float)'''
    ...
    def w (self, *args, **kwargs):
      '''None'''
    ...
    def x (self, *args, **kwargs):
      '''None'''
    ...
    def y (self, *args, **kwargs):
      '''None'''
    ...
    def z (self, *args, **kwargs):
      '''None'''
    ...

def V4fArray (*args):
      '''
__init__(_object*, PyImath::FixedArray<Imath_3_1::Vec4<double> >)
__init__(_object*, PyImath::FixedArray<Imath_3_1::Vec4<long> >)
__init__(_object*, PyImath::FixedArray<Imath_3_1::Vec4<int> >)
__init__(_object*, PyImath::FixedArray<Imath_3_1::Vec4<short> >)
__init__(_object*, Imath_3_1::Vec4<float>, unsigned long)
__init__(_object*, PyImath::FixedArray<Imath_3_1::Vec4<float> >)
__init__(_object*, unsigned long)

'''      
    ...

class V4fArray:
    def dot (self, *args, **kwargs):
      '''
dot( (V4fArray)arg1, (V4f)x) -> FloatArray :
    dot(x) - return the inner product of (self,x)

    C++ signature :
        PyImath::FixedArray<float> dot(PyImath::FixedArray<Imath_3_1::Vec4<float> >,Imath_3_1::Vec4<float>)

dot( (V4fArray)arg1, (V4fArray)x) -> FloatArray :
    dot(x) - return the inner product of (self,x)

    C++ signature :
        PyImath::FixedArray<float> dot(PyImath::FixedArray<Imath_3_1::Vec4<float> >,PyImath::FixedArray<Imath_3_1::Vec4<float> >)'''
    ...
    def ifelse (self, *args, **kwargs):
      '''
ifelse( (V4fArray)arg1, (IntArray)arg2, (V4f)arg3) -> V4fArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec4<float> > ifelse(PyImath::FixedArray<Imath_3_1::Vec4<float> > {lvalue},PyImath::FixedArray<int>,Imath_3_1::Vec4<float>)

ifelse( (V4fArray)arg1, (IntArray)arg2, (V4fArray)arg3) -> V4fArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec4<float> > ifelse(PyImath::FixedArray<Imath_3_1::Vec4<float> > {lvalue},PyImath::FixedArray<int>,PyImath::FixedArray<Imath_3_1::Vec4<float> >)'''
    ...
    def length (self, *args, **kwargs):
      '''
length( (V4fArray)arg1) -> FloatArray :

    C++ signature :
        PyImath::FixedArray<float> length(PyImath::FixedArray<Imath_3_1::Vec4<float> >)'''
    ...
    def length2 (self, *args, **kwargs):
      '''
length2( (V4fArray)arg1) -> FloatArray :

    C++ signature :
        PyImath::FixedArray<float> length2(PyImath::FixedArray<Imath_3_1::Vec4<float> >)'''
    ...
    def makeReadOnly (self, *args, **kwargs):
      '''
makeReadOnly( (V4fArray)arg1) -> None :

    C++ signature :
        void makeReadOnly(PyImath::FixedArray<Imath_3_1::Vec4<float> > {lvalue})'''
    ...
    def max (self, *args, **kwargs):
      '''
max( (V4fArray)arg1) -> V4f :

    C++ signature :
        Imath_3_1::Vec4<float> max(PyImath::FixedArray<Imath_3_1::Vec4<float> >)'''
    ...
    def min (self, *args, **kwargs):
      '''
min( (V4fArray)arg1) -> V4f :

    C++ signature :
        Imath_3_1::Vec4<float> min(PyImath::FixedArray<Imath_3_1::Vec4<float> >)'''
    ...
    def normalize (self, *args, **kwargs):
      '''
normalize( (V4fArray)arg1) -> V4fArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec4<float> > {lvalue} normalize(PyImath::FixedArray<Imath_3_1::Vec4<float> > {lvalue})'''
    ...
    def normalizeExc (self, *args, **kwargs):
      '''
normalizeExc( (V4fArray)arg1) -> V4fArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec4<float> > {lvalue} normalizeExc(PyImath::FixedArray<Imath_3_1::Vec4<float> > {lvalue})'''
    ...
    def normalized (self, *args, **kwargs):
      '''
normalized( (V4fArray)arg1) -> V4fArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec4<float> > normalized(PyImath::FixedArray<Imath_3_1::Vec4<float> >)'''
    ...
    def normalizedExc (self, *args, **kwargs):
      '''
normalizedExc( (V4fArray)arg1) -> V4fArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec4<float> > normalizedExc(PyImath::FixedArray<Imath_3_1::Vec4<float> >)'''
    ...
    def reduce (self, *args, **kwargs):
      '''
reduce( (V4fArray)arg1) -> V4f :

    C++ signature :
        Imath_3_1::Vec4<float> reduce(PyImath::FixedArray<Imath_3_1::Vec4<float> >)'''
    ...
    def w (self, *args, **kwargs):
      '''None'''
    ...
    def writable (self, *args, **kwargs):
      '''
writable( (V4fArray)arg1) -> bool :

    C++ signature :
        bool writable(PyImath::FixedArray<Imath_3_1::Vec4<float> > {lvalue})'''
    ...
    def x (self, *args, **kwargs):
      '''None'''
    ...
    def y (self, *args, **kwargs):
      '''None'''
    ...
    def z (self, *args, **kwargs):
      '''None'''
    ...

def V4fArrayFromBuffer (*args):
      '''

'''      
    ...

def V4i (*args):
      '''
__init__(boost::python::api::object, boost::python::api::object, boost::python::api::object, boost::python::api::object, boost::python::api::object)
__init__(boost::python::api::object, boost::python::api::object)
__init__(boost::python::api::object)
__init__(_object*, Imath_3_1::Vec4<int>)

'''      
    ...

class V4i:
    def baseTypeEpsilon (self, *args, **kwargs):
      '''
baseTypeEpsilon() -> int :
    baseTypeEpsilon() epsilon value of the base type of the vector

    C++ signature :
        int baseTypeEpsilon()'''
    ...
    def baseTypeLowest (self, *args, **kwargs):
      '''
baseTypeLowest() -> int :
    baseTypeLowest() largest negative value of the base type of the vector

    C++ signature :
        int baseTypeLowest()'''
    ...
    def baseTypeMax (self, *args, **kwargs):
      '''
baseTypeMax() -> int :
    baseTypeMax() max value of the base type of the vector

    C++ signature :
        int baseTypeMax()'''
    ...
    def baseTypeSmallest (self, *args, **kwargs):
      '''
baseTypeSmallest() -> int :
    baseTypeSmallest() smallest value of the base type of the vector

    C++ signature :
        int baseTypeSmallest()'''
    ...
    def dimensions (self, *args, **kwargs):
      '''
dimensions() -> int :
    dimensions() number of dimensions in the vector

    C++ signature :
        unsigned int dimensions()'''
    ...
    def dot (self, *args, **kwargs):
      '''
dot( (V4i)arg1, (V4i)arg2) -> int :
    v1.dot(v2) inner product of the two vectors

    C++ signature :
        int dot(Imath_3_1::Vec4<int>,Imath_3_1::Vec4<int>)

dot( (V4i)arg1, (V4iArray)arg2) -> IntArray :
    v1.dot(v2) array inner product

    C++ signature :
        PyImath::FixedArray<int> dot(Imath_3_1::Vec4<int>,PyImath::FixedArray<Imath_3_1::Vec4<int> >)'''
    ...
    def equalWithAbsError (self, *args, **kwargs):
      '''
equalWithAbsError( (V4i)arg1, (V4i)arg2, (int)arg3) -> bool :
    v1.equalWithAbsError(v2) true if the elements of v1 and v2 are the same with an absolute error of no more than e, i.e., abs(v1[i] - v2[i]) <= e

    C++ signature :
        bool equalWithAbsError(Imath_3_1::Vec4<int> {lvalue},Imath_3_1::Vec4<int>,int)

equalWithAbsError( (V4i)arg1, (object)arg2, (object)arg3) -> bool :

    C++ signature :
        bool equalWithAbsError(Imath_3_1::Vec4<int>,boost::python::api::object,boost::python::api::object)'''
    ...
    def equalWithRelError (self, *args, **kwargs):
      '''
equalWithRelError( (V4i)arg1, (V4i)arg2, (int)arg3) -> bool :
    v1.equalWithAbsError(v2) true if the elements of v1 and v2 are the same with an absolute error of no more than e, i.e., abs(v1[i] - v2[i]) <= e * abs(v1[i])

    C++ signature :
        bool equalWithRelError(Imath_3_1::Vec4<int> {lvalue},Imath_3_1::Vec4<int>,int)

equalWithRelError( (V4i)arg1, (object)arg2, (object)arg3) -> bool :

    C++ signature :
        bool equalWithRelError(Imath_3_1::Vec4<int>,boost::python::api::object,boost::python::api::object)'''
    ...
    def length2 (self, *args, **kwargs):
      '''
length2( (V4i)arg1) -> int :
    length2() square magnitude of the vector

    C++ signature :
        int length2(Imath_3_1::Vec4<int>)'''
    ...
    def negate (self, *args, **kwargs):
      '''
negate( (V4i)arg1) -> V4i :

    C++ signature :
        Imath_3_1::Vec4<int> negate(Imath_3_1::Vec4<int> {lvalue})'''
    ...
    def setValue (self, *args, **kwargs):
      '''
setValue( (V4i)arg1, (int)arg2, (int)arg3, (int)arg4, (int)arg5) -> None :

    C++ signature :
        void setValue(Imath_3_1::Vec4<int> {lvalue},int,int,int,int)'''
    ...
    def w (self, *args, **kwargs):
      '''None'''
    ...
    def x (self, *args, **kwargs):
      '''None'''
    ...
    def y (self, *args, **kwargs):
      '''None'''
    ...
    def z (self, *args, **kwargs):
      '''None'''
    ...

def V4i64 (*args):
      '''
__init__(boost::python::api::object, boost::python::api::object, boost::python::api::object, boost::python::api::object, boost::python::api::object)
__init__(boost::python::api::object, boost::python::api::object)
__init__(boost::python::api::object)
__init__(_object*, Imath_3_1::Vec4<long>)

'''      
    ...

class V4i64:
    def baseTypeEpsilon (self, *args, **kwargs):
      '''
baseTypeEpsilon() -> int :
    baseTypeEpsilon() epsilon value of the base type of the vector

    C++ signature :
        long baseTypeEpsilon()'''
    ...
    def baseTypeLowest (self, *args, **kwargs):
      '''
baseTypeLowest() -> int :
    baseTypeLowest() largest negative value of the base type of the vector

    C++ signature :
        long baseTypeLowest()'''
    ...
    def baseTypeMax (self, *args, **kwargs):
      '''
baseTypeMax() -> int :
    baseTypeMax() max value of the base type of the vector

    C++ signature :
        long baseTypeMax()'''
    ...
    def baseTypeSmallest (self, *args, **kwargs):
      '''
baseTypeSmallest() -> int :
    baseTypeSmallest() smallest value of the base type of the vector

    C++ signature :
        long baseTypeSmallest()'''
    ...
    def dimensions (self, *args, **kwargs):
      '''
dimensions() -> int :
    dimensions() number of dimensions in the vector

    C++ signature :
        unsigned int dimensions()'''
    ...
    def dot (self, *args, **kwargs):
      '''
dot( (V4i64)arg1, (V4i64)arg2) -> int :
    v1.dot(v2) inner product of the two vectors

    C++ signature :
        long dot(Imath_3_1::Vec4<long>,Imath_3_1::Vec4<long>)

dot( (V4i64)arg1, (V4i64Array)arg2) -> object :
    v1.dot(v2) array inner product

    C++ signature :
        PyImath::FixedArray<long> dot(Imath_3_1::Vec4<long>,PyImath::FixedArray<Imath_3_1::Vec4<long> >)'''
    ...
    def equalWithAbsError (self, *args, **kwargs):
      '''
equalWithAbsError( (V4i64)arg1, (V4i64)arg2, (int)arg3) -> bool :
    v1.equalWithAbsError(v2) true if the elements of v1 and v2 are the same with an absolute error of no more than e, i.e., abs(v1[i] - v2[i]) <= e

    C++ signature :
        bool equalWithAbsError(Imath_3_1::Vec4<long> {lvalue},Imath_3_1::Vec4<long>,long)

equalWithAbsError( (V4i64)arg1, (object)arg2, (object)arg3) -> bool :

    C++ signature :
        bool equalWithAbsError(Imath_3_1::Vec4<long>,boost::python::api::object,boost::python::api::object)'''
    ...
    def equalWithRelError (self, *args, **kwargs):
      '''
equalWithRelError( (V4i64)arg1, (V4i64)arg2, (int)arg3) -> bool :
    v1.equalWithAbsError(v2) true if the elements of v1 and v2 are the same with an absolute error of no more than e, i.e., abs(v1[i] - v2[i]) <= e * abs(v1[i])

    C++ signature :
        bool equalWithRelError(Imath_3_1::Vec4<long> {lvalue},Imath_3_1::Vec4<long>,long)

equalWithRelError( (V4i64)arg1, (object)arg2, (object)arg3) -> bool :

    C++ signature :
        bool equalWithRelError(Imath_3_1::Vec4<long>,boost::python::api::object,boost::python::api::object)'''
    ...
    def length2 (self, *args, **kwargs):
      '''
length2( (V4i64)arg1) -> int :
    length2() square magnitude of the vector

    C++ signature :
        long length2(Imath_3_1::Vec4<long>)'''
    ...
    def negate (self, *args, **kwargs):
      '''
negate( (V4i64)arg1) -> V4i64 :

    C++ signature :
        Imath_3_1::Vec4<long> negate(Imath_3_1::Vec4<long> {lvalue})'''
    ...
    def setValue (self, *args, **kwargs):
      '''
setValue( (V4i64)arg1, (int)arg2, (int)arg3, (int)arg4, (int)arg5) -> None :

    C++ signature :
        void setValue(Imath_3_1::Vec4<long> {lvalue},long,long,long,long)'''
    ...
    def w (self, *args, **kwargs):
      '''None'''
    ...
    def x (self, *args, **kwargs):
      '''None'''
    ...
    def y (self, *args, **kwargs):
      '''None'''
    ...
    def z (self, *args, **kwargs):
      '''None'''
    ...

def V4i64Array (*args):
      '''
__init__(_object*, PyImath::FixedArray<Imath_3_1::Vec4<double> >)
__init__(_object*, PyImath::FixedArray<Imath_3_1::Vec4<float> >)
__init__(_object*, PyImath::FixedArray<Imath_3_1::Vec4<int> >)
__init__(_object*, PyImath::FixedArray<Imath_3_1::Vec4<short> >)
__init__(_object*, Imath_3_1::Vec4<long>, unsigned long)
__init__(_object*, PyImath::FixedArray<Imath_3_1::Vec4<long> >)
__init__(_object*, unsigned long)

'''      
    ...

class V4i64Array:
    def dot (self, *args, **kwargs):
      '''
dot( (V4i64Array)arg1, (V4i64)x) -> object :
    dot(x) - return the inner product of (self,x)

    C++ signature :
        PyImath::FixedArray<long> dot(PyImath::FixedArray<Imath_3_1::Vec4<long> >,Imath_3_1::Vec4<long>)

dot( (V4i64Array)arg1, (V4i64Array)x) -> object :
    dot(x) - return the inner product of (self,x)

    C++ signature :
        PyImath::FixedArray<long> dot(PyImath::FixedArray<Imath_3_1::Vec4<long> >,PyImath::FixedArray<Imath_3_1::Vec4<long> >)'''
    ...
    def ifelse (self, *args, **kwargs):
      '''
ifelse( (V4i64Array)arg1, (IntArray)arg2, (V4i64)arg3) -> V4i64Array :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec4<long> > ifelse(PyImath::FixedArray<Imath_3_1::Vec4<long> > {lvalue},PyImath::FixedArray<int>,Imath_3_1::Vec4<long>)

ifelse( (V4i64Array)arg1, (IntArray)arg2, (V4i64Array)arg3) -> V4i64Array :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec4<long> > ifelse(PyImath::FixedArray<Imath_3_1::Vec4<long> > {lvalue},PyImath::FixedArray<int>,PyImath::FixedArray<Imath_3_1::Vec4<long> >)'''
    ...
    def length2 (self, *args, **kwargs):
      '''
length2( (V4i64Array)arg1) -> object :

    C++ signature :
        PyImath::FixedArray<long> length2(PyImath::FixedArray<Imath_3_1::Vec4<long> >)'''
    ...
    def makeReadOnly (self, *args, **kwargs):
      '''
makeReadOnly( (V4i64Array)arg1) -> None :

    C++ signature :
        void makeReadOnly(PyImath::FixedArray<Imath_3_1::Vec4<long> > {lvalue})'''
    ...
    def max (self, *args, **kwargs):
      '''
max( (V4i64Array)arg1) -> V4i64 :

    C++ signature :
        Imath_3_1::Vec4<long> max(PyImath::FixedArray<Imath_3_1::Vec4<long> >)'''
    ...
    def min (self, *args, **kwargs):
      '''
min( (V4i64Array)arg1) -> V4i64 :

    C++ signature :
        Imath_3_1::Vec4<long> min(PyImath::FixedArray<Imath_3_1::Vec4<long> >)'''
    ...
    def reduce (self, *args, **kwargs):
      '''
reduce( (V4i64Array)arg1) -> V4i64 :

    C++ signature :
        Imath_3_1::Vec4<long> reduce(PyImath::FixedArray<Imath_3_1::Vec4<long> >)'''
    ...
    def w (self, *args, **kwargs):
      '''None'''
    ...
    def writable (self, *args, **kwargs):
      '''
writable( (V4i64Array)arg1) -> bool :

    C++ signature :
        bool writable(PyImath::FixedArray<Imath_3_1::Vec4<long> > {lvalue})'''
    ...
    def x (self, *args, **kwargs):
      '''None'''
    ...
    def y (self, *args, **kwargs):
      '''None'''
    ...
    def z (self, *args, **kwargs):
      '''None'''
    ...

def V4iArray (*args):
      '''
__init__(_object*, PyImath::FixedArray<Imath_3_1::Vec4<double> >)
__init__(_object*, PyImath::FixedArray<Imath_3_1::Vec4<float> >)
__init__(_object*, PyImath::FixedArray<Imath_3_1::Vec4<long> >)
__init__(_object*, PyImath::FixedArray<Imath_3_1::Vec4<short> >)
__init__(_object*, Imath_3_1::Vec4<int>, unsigned long)
__init__(_object*, PyImath::FixedArray<Imath_3_1::Vec4<int> >)
__init__(_object*, unsigned long)

'''      
    ...

class V4iArray:
    def dot (self, *args, **kwargs):
      '''
dot( (V4iArray)arg1, (V4i)x) -> IntArray :
    dot(x) - return the inner product of (self,x)

    C++ signature :
        PyImath::FixedArray<int> dot(PyImath::FixedArray<Imath_3_1::Vec4<int> >,Imath_3_1::Vec4<int>)

dot( (V4iArray)arg1, (V4iArray)x) -> IntArray :
    dot(x) - return the inner product of (self,x)

    C++ signature :
        PyImath::FixedArray<int> dot(PyImath::FixedArray<Imath_3_1::Vec4<int> >,PyImath::FixedArray<Imath_3_1::Vec4<int> >)'''
    ...
    def ifelse (self, *args, **kwargs):
      '''
ifelse( (V4iArray)arg1, (IntArray)arg2, (V4i)arg3) -> V4iArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec4<int> > ifelse(PyImath::FixedArray<Imath_3_1::Vec4<int> > {lvalue},PyImath::FixedArray<int>,Imath_3_1::Vec4<int>)

ifelse( (V4iArray)arg1, (IntArray)arg2, (V4iArray)arg3) -> V4iArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec4<int> > ifelse(PyImath::FixedArray<Imath_3_1::Vec4<int> > {lvalue},PyImath::FixedArray<int>,PyImath::FixedArray<Imath_3_1::Vec4<int> >)'''
    ...
    def length2 (self, *args, **kwargs):
      '''
length2( (V4iArray)arg1) -> IntArray :

    C++ signature :
        PyImath::FixedArray<int> length2(PyImath::FixedArray<Imath_3_1::Vec4<int> >)'''
    ...
    def makeReadOnly (self, *args, **kwargs):
      '''
makeReadOnly( (V4iArray)arg1) -> None :

    C++ signature :
        void makeReadOnly(PyImath::FixedArray<Imath_3_1::Vec4<int> > {lvalue})'''
    ...
    def max (self, *args, **kwargs):
      '''
max( (V4iArray)arg1) -> V4i :

    C++ signature :
        Imath_3_1::Vec4<int> max(PyImath::FixedArray<Imath_3_1::Vec4<int> >)'''
    ...
    def min (self, *args, **kwargs):
      '''
min( (V4iArray)arg1) -> V4i :

    C++ signature :
        Imath_3_1::Vec4<int> min(PyImath::FixedArray<Imath_3_1::Vec4<int> >)'''
    ...
    def reduce (self, *args, **kwargs):
      '''
reduce( (V4iArray)arg1) -> V4i :

    C++ signature :
        Imath_3_1::Vec4<int> reduce(PyImath::FixedArray<Imath_3_1::Vec4<int> >)'''
    ...
    def w (self, *args, **kwargs):
      '''None'''
    ...
    def writable (self, *args, **kwargs):
      '''
writable( (V4iArray)arg1) -> bool :

    C++ signature :
        bool writable(PyImath::FixedArray<Imath_3_1::Vec4<int> > {lvalue})'''
    ...
    def x (self, *args, **kwargs):
      '''None'''
    ...
    def y (self, *args, **kwargs):
      '''None'''
    ...
    def z (self, *args, **kwargs):
      '''None'''
    ...

def V4iArrayFromBuffer (*args):
      '''

'''      
    ...

def V4s (*args):
      '''
__init__(boost::python::api::object, boost::python::api::object, boost::python::api::object, boost::python::api::object, boost::python::api::object)
__init__(boost::python::api::object, boost::python::api::object)
__init__(boost::python::api::object)
__init__(_object*, Imath_3_1::Vec4<short>)

'''      
    ...

class V4s:
    def baseTypeEpsilon (self, *args, **kwargs):
      '''
baseTypeEpsilon() -> int :
    baseTypeEpsilon() epsilon value of the base type of the vector

    C++ signature :
        short baseTypeEpsilon()'''
    ...
    def baseTypeLowest (self, *args, **kwargs):
      '''
baseTypeLowest() -> int :
    baseTypeLowest() largest negative value of the base type of the vector

    C++ signature :
        short baseTypeLowest()'''
    ...
    def baseTypeMax (self, *args, **kwargs):
      '''
baseTypeMax() -> int :
    baseTypeMax() max value of the base type of the vector

    C++ signature :
        short baseTypeMax()'''
    ...
    def baseTypeSmallest (self, *args, **kwargs):
      '''
baseTypeSmallest() -> int :
    baseTypeSmallest() smallest value of the base type of the vector

    C++ signature :
        short baseTypeSmallest()'''
    ...
    def dimensions (self, *args, **kwargs):
      '''
dimensions() -> int :
    dimensions() number of dimensions in the vector

    C++ signature :
        unsigned int dimensions()'''
    ...
    def dot (self, *args, **kwargs):
      '''
dot( (V4s)arg1, (V4s)arg2) -> int :
    v1.dot(v2) inner product of the two vectors

    C++ signature :
        short dot(Imath_3_1::Vec4<short>,Imath_3_1::Vec4<short>)

dot( (V4s)arg1, (V4sArray)arg2) -> ShortArray :
    v1.dot(v2) array inner product

    C++ signature :
        PyImath::FixedArray<short> dot(Imath_3_1::Vec4<short>,PyImath::FixedArray<Imath_3_1::Vec4<short> >)'''
    ...
    def equalWithAbsError (self, *args, **kwargs):
      '''
equalWithAbsError( (V4s)arg1, (V4s)arg2, (int)arg3) -> bool :
    v1.equalWithAbsError(v2) true if the elements of v1 and v2 are the same with an absolute error of no more than e, i.e., abs(v1[i] - v2[i]) <= e

    C++ signature :
        bool equalWithAbsError(Imath_3_1::Vec4<short> {lvalue},Imath_3_1::Vec4<short>,short)

equalWithAbsError( (V4s)arg1, (object)arg2, (object)arg3) -> bool :

    C++ signature :
        bool equalWithAbsError(Imath_3_1::Vec4<short>,boost::python::api::object,boost::python::api::object)'''
    ...
    def equalWithRelError (self, *args, **kwargs):
      '''
equalWithRelError( (V4s)arg1, (V4s)arg2, (int)arg3) -> bool :
    v1.equalWithAbsError(v2) true if the elements of v1 and v2 are the same with an absolute error of no more than e, i.e., abs(v1[i] - v2[i]) <= e * abs(v1[i])

    C++ signature :
        bool equalWithRelError(Imath_3_1::Vec4<short> {lvalue},Imath_3_1::Vec4<short>,short)

equalWithRelError( (V4s)arg1, (object)arg2, (object)arg3) -> bool :

    C++ signature :
        bool equalWithRelError(Imath_3_1::Vec4<short>,boost::python::api::object,boost::python::api::object)'''
    ...
    def length2 (self, *args, **kwargs):
      '''
length2( (V4s)arg1) -> int :
    length2() square magnitude of the vector

    C++ signature :
        short length2(Imath_3_1::Vec4<short>)'''
    ...
    def negate (self, *args, **kwargs):
      '''
negate( (V4s)arg1) -> V4s :

    C++ signature :
        Imath_3_1::Vec4<short> negate(Imath_3_1::Vec4<short> {lvalue})'''
    ...
    def setValue (self, *args, **kwargs):
      '''
setValue( (V4s)arg1, (int)arg2, (int)arg3, (int)arg4, (int)arg5) -> None :

    C++ signature :
        void setValue(Imath_3_1::Vec4<short> {lvalue},short,short,short,short)'''
    ...
    def w (self, *args, **kwargs):
      '''None'''
    ...
    def x (self, *args, **kwargs):
      '''None'''
    ...
    def y (self, *args, **kwargs):
      '''None'''
    ...
    def z (self, *args, **kwargs):
      '''None'''
    ...

def V4sArray (*args):
      '''
__init__(_object*, PyImath::FixedArray<Imath_3_1::Vec4<double> >)
__init__(_object*, PyImath::FixedArray<Imath_3_1::Vec4<float> >)
__init__(_object*, PyImath::FixedArray<Imath_3_1::Vec4<long> >)
__init__(_object*, PyImath::FixedArray<Imath_3_1::Vec4<int> >)
__init__(_object*, Imath_3_1::Vec4<short>, unsigned long)
__init__(_object*, PyImath::FixedArray<Imath_3_1::Vec4<short> >)
__init__(_object*, unsigned long)

'''      
    ...

class V4sArray:
    def dot (self, *args, **kwargs):
      '''
dot( (V4sArray)arg1, (V4s)x) -> ShortArray :
    dot(x) - return the inner product of (self,x)

    C++ signature :
        PyImath::FixedArray<short> dot(PyImath::FixedArray<Imath_3_1::Vec4<short> >,Imath_3_1::Vec4<short>)

dot( (V4sArray)arg1, (V4sArray)x) -> ShortArray :
    dot(x) - return the inner product of (self,x)

    C++ signature :
        PyImath::FixedArray<short> dot(PyImath::FixedArray<Imath_3_1::Vec4<short> >,PyImath::FixedArray<Imath_3_1::Vec4<short> >)'''
    ...
    def ifelse (self, *args, **kwargs):
      '''
ifelse( (V4sArray)arg1, (IntArray)arg2, (V4s)arg3) -> V4sArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec4<short> > ifelse(PyImath::FixedArray<Imath_3_1::Vec4<short> > {lvalue},PyImath::FixedArray<int>,Imath_3_1::Vec4<short>)

ifelse( (V4sArray)arg1, (IntArray)arg2, (V4sArray)arg3) -> V4sArray :

    C++ signature :
        PyImath::FixedArray<Imath_3_1::Vec4<short> > ifelse(PyImath::FixedArray<Imath_3_1::Vec4<short> > {lvalue},PyImath::FixedArray<int>,PyImath::FixedArray<Imath_3_1::Vec4<short> >)'''
    ...
    def length2 (self, *args, **kwargs):
      '''
length2( (V4sArray)arg1) -> ShortArray :

    C++ signature :
        PyImath::FixedArray<short> length2(PyImath::FixedArray<Imath_3_1::Vec4<short> >)'''
    ...
    def makeReadOnly (self, *args, **kwargs):
      '''
makeReadOnly( (V4sArray)arg1) -> None :

    C++ signature :
        void makeReadOnly(PyImath::FixedArray<Imath_3_1::Vec4<short> > {lvalue})'''
    ...
    def max (self, *args, **kwargs):
      '''
max( (V4sArray)arg1) -> V4s :

    C++ signature :
        Imath_3_1::Vec4<short> max(PyImath::FixedArray<Imath_3_1::Vec4<short> >)'''
    ...
    def min (self, *args, **kwargs):
      '''
min( (V4sArray)arg1) -> V4s :

    C++ signature :
        Imath_3_1::Vec4<short> min(PyImath::FixedArray<Imath_3_1::Vec4<short> >)'''
    ...
    def reduce (self, *args, **kwargs):
      '''
reduce( (V4sArray)arg1) -> V4s :

    C++ signature :
        Imath_3_1::Vec4<short> reduce(PyImath::FixedArray<Imath_3_1::Vec4<short> >)'''
    ...
    def w (self, *args, **kwargs):
      '''None'''
    ...
    def writable (self, *args, **kwargs):
      '''
writable( (V4sArray)arg1) -> bool :

    C++ signature :
        bool writable(PyImath::FixedArray<Imath_3_1::Vec4<short> > {lvalue})'''
    ...
    def x (self, *args, **kwargs):
      '''None'''
    ...
    def y (self, *args, **kwargs):
      '''None'''
    ...
    def z (self, *args, **kwargs):
      '''None'''
    ...

def VFloatArray (*args):
      '''
__init__(_object*, PyImath::FixedArray<int>, float)
__init__(_object*, float, long)
__init__(_object*, PyImath::FixedVArray<float>)
__init__(_object*, long)

'''      
    ...

class VFloatArray:
    def SizeHelper (self, *args, **kwargs):
      '''None'''
    ...
    def makeReadOnly (self, *args, **kwargs):
      '''
makeReadOnly( (VFloatArray)arg1) -> None :

    C++ signature :
        void makeReadOnly(PyImath::FixedVArray<float> {lvalue})'''
    ...
    def size (self, *args, **kwargs):
      '''None'''
    ...
    def writable (self, *args, **kwargs):
      '''
writable( (VFloatArray)arg1) -> bool :

    C++ signature :
        bool writable(PyImath::FixedVArray<float> {lvalue})'''
    ...

def VIntArray (*args):
      '''
__init__(_object*, PyImath::FixedArray<int>, int)
__init__(_object*, int, long)
__init__(_object*, PyImath::FixedVArray<int>)
__init__(_object*, long)

'''      
    ...

class VIntArray:
    def SizeHelper (self, *args, **kwargs):
      '''None'''
    ...
    def makeReadOnly (self, *args, **kwargs):
      '''
makeReadOnly( (VIntArray)arg1) -> None :

    C++ signature :
        void makeReadOnly(PyImath::FixedVArray<int> {lvalue})'''
    ...
    def size (self, *args, **kwargs):
      '''None'''
    ...
    def writable (self, *args, **kwargs):
      '''
writable( (VIntArray)arg1) -> bool :

    C++ signature :
        bool writable(PyImath::FixedVArray<int> {lvalue})'''
    ...

def VV2fArray (*args):
      '''
__init__(_object*, PyImath::FixedArray<int>, Imath_3_1::Vec2<float>)
__init__(_object*, Imath_3_1::Vec2<float>, long)
__init__(_object*, PyImath::FixedVArray<Imath_3_1::Vec2<float> >)
__init__(_object*, long)

'''      
    ...

class VV2fArray:
    def SizeHelper (self, *args, **kwargs):
      '''None'''
    ...
    def makeReadOnly (self, *args, **kwargs):
      '''
makeReadOnly( (VV2fArray)arg1) -> None :

    C++ signature :
        void makeReadOnly(PyImath::FixedVArray<Imath_3_1::Vec2<float> > {lvalue})'''
    ...
    def size (self, *args, **kwargs):
      '''None'''
    ...
    def writable (self, *args, **kwargs):
      '''
writable( (VV2fArray)arg1) -> bool :

    C++ signature :
        bool writable(PyImath::FixedVArray<Imath_3_1::Vec2<float> > {lvalue})'''
    ...

def VV2iArray (*args):
      '''
__init__(_object*, PyImath::FixedArray<int>, Imath_3_1::Vec2<int>)
__init__(_object*, Imath_3_1::Vec2<int>, long)
__init__(_object*, PyImath::FixedVArray<Imath_3_1::Vec2<int> >)
__init__(_object*, long)

'''      
    ...

class VV2iArray:
    def SizeHelper (self, *args, **kwargs):
      '''None'''
    ...
    def makeReadOnly (self, *args, **kwargs):
      '''
makeReadOnly( (VV2iArray)arg1) -> None :

    C++ signature :
        void makeReadOnly(PyImath::FixedVArray<Imath_3_1::Vec2<int> > {lvalue})'''
    ...
    def size (self, *args, **kwargs):
      '''None'''
    ...
    def writable (self, *args, **kwargs):
      '''
writable( (VV2iArray)arg1) -> bool :

    C++ signature :
        bool writable(PyImath::FixedVArray<Imath_3_1::Vec2<int> > {lvalue})'''
    ...

def WstringArray (*args):
      '''
__init__(boost::python::api::object, std::__cxx11::basic_string<wchar_t, std::char_traits<wchar_t>, std::allocator<wchar_t> >, unsigned long)
__init__(boost::python::api::object, unsigned long)

'''      
    ...

class WstringArray:

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

def __spec__ (*args):
      '''

'''      
    ...

def __version__ (*args):
      '''

'''      
    ...

def abs (*args):
      '''

'''      
    ...

def acos (*args):
      '''

'''      
    ...

def asin (*args):
      '''

'''      
    ...

def atan (*args):
      '''

'''      
    ...

def atan2 (*args):
      '''

'''      
    ...

def bias (*args):
      '''

'''      
    ...

def ceil (*args):
      '''

'''      
    ...

def clamp (*args):
      '''

'''      
    ...

def cmp (*args):
      '''

'''      
    ...

def cmpt (*args):
      '''

'''      
    ...

def computeBoundingBox (*args):
      '''

'''      
    ...

def cos (*args):
      '''

'''      
    ...

def cosh (*args):
      '''

'''      
    ...

def divp (*args):
      '''

'''      
    ...

def divs (*args):
      '''

'''      
    ...

def equal (*args):
      '''

'''      
    ...

def exp (*args):
      '''

'''      
    ...

def floor (*args):
      '''

'''      
    ...

def gain (*args):
      '''

'''      
    ...

def hollowSphereRand (*args):
      '''

'''      
    ...

def hsv2rgb (*args):
      '''

'''      
    ...

def iszero (*args):
      '''

'''      
    ...

def lerp (*args):
      '''

'''      
    ...

def lerpfactor (*args):
      '''

'''      
    ...

def log (*args):
      '''

'''      
    ...

def log10 (*args):
      '''

'''      
    ...

def modp (*args):
      '''

'''      
    ...

def mods (*args):
      '''

'''      
    ...

def pow (*args):
      '''

'''      
    ...

def procrustesRotationAndTranslation (*args):
      '''

'''      
    ...

def rangeX (*args):
      '''

'''      
    ...

def rangeY (*args):
      '''

'''      
    ...

def rgb2hsv (*args):
      '''

'''      
    ...

def rotationXYZWithUpDir (*args):
      '''

'''      
    ...

def sign (*args):
      '''

'''      
    ...

def sin (*args):
      '''

'''      
    ...

def sinh (*args):
      '''

'''      
    ...

def solidSphereRand (*args):
      '''

'''      
    ...

def sqrt (*args):
      '''

'''      
    ...

def tan (*args):
      '''

'''      
    ...

def trunc (*args):
      '''

'''      
    ...
