# tpJointOrient
Tool to orient joints quickly for Maya.
Main joint orientation algorithm based on legend Michael Comet "cometJointOrient" script (http://www.comet-cartoons.com/melscript.php)

![](http://cgart3d.com/wp-content/uploads/2017/08/tpJointOrientImage.png)

Features
=========================================================
* Orient joints with aim, up, up world axis setup
* Orient selected joints and/or its hierarchy
* Easy manual rotation of local rotation axis (add, substract or set exact value)
* Set rotation axis of selected joints
* List with common rotation axis for different rigs (arms, legs, etc)
* Display/Hide LRA

Installation
=========================================================
Copy tpJointOrient.py file into your Documents/Maya/(Version)/scripts folder and execute this code in Maya command panel

``` python
import tpJointOrient
reload(tpJointOrient)
```
